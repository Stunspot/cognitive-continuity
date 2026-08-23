from __future__ import annotations

import argparse
import errno
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1]
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import continuity_store_v2 as store
import workspace_runtime as runtime

STORE = SCRIPTS / "continuity_store_v2.py"
VALIDATE = SCRIPTS / "validate_continuity_v2.py"


def temporary_parent() -> str | None:
    candidate = Path("E:/")
    return str(candidate) if os.name == "nt" and candidate.is_dir() else None


class AdapterSeamTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=temporary_parent())
        self.base = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def darwin_observation(*, filesystem: str = "apfs", flags: int = runtime._DARWIN_MNT_LOCAL):
        return lambda _probe: {"filesystem": filesystem, "flags": flags}

    def test_local_writable_apfs_qualifies_through_controlled_darwin_seam(self) -> None:
        self.assertEqual(runtime.ctypes.sizeof(runtime._DarwinStatfs), 2168)
        root = self.base / "workspace"
        adapter = runtime._filesystem_adapter(
            root,
            lexical_root=root,
            platform_name="darwin",
            darwin_observer=self.darwin_observation(),
        )
        self.assertEqual(
            adapter,
            "darwin-fcntl-flock-fsync-F_FULLFSYNC-when-available-rename-parent-fsync-apfs/v1",
        )

    def test_darwin_adapter_rejects_nonlocal_readonly_and_unqualified_filesystems(self) -> None:
        root = self.base / "workspace"
        cases = (
            ("apfs", 0),
            ("apfs", runtime._DARWIN_MNT_LOCAL | runtime._DARWIN_MNT_RDONLY),
            ("nfs", runtime._DARWIN_MNT_LOCAL),
        )
        for filesystem, flags in cases:
            with self.subTest(filesystem=filesystem, flags=flags):
                with self.assertRaises(runtime.ContinuityError) as caught:
                    runtime._filesystem_adapter(
                        root,
                        lexical_root=root,
                        platform_name="darwin",
                        darwin_observer=self.darwin_observation(filesystem=filesystem, flags=flags),
                    )
                self.assertEqual(caught.exception.code, "filesystem_semantics_unsupported")

    def test_adapter_checks_lexical_path_before_resolved_identity(self) -> None:
        root = self.base / "resolved" / "workspace"
        lexical = self.base / "alias" / "workspace"
        with (
            mock.patch.object(runtime, "_has_reparse_component", side_effect=lambda path, boundary=None: Path(path) == lexical),
            mock.patch.object(runtime, "_same_path_identity", return_value=True),
        ):
            with self.assertRaises(runtime.ContinuityError) as caught:
                runtime._filesystem_adapter(
                    root,
                    lexical_root=lexical,
                    platform_name="darwin",
                    darwin_observer=self.darwin_observation(),
                )
        self.assertEqual(caught.exception.code, "custody_reparse_escape")

    def test_broken_symlink_is_an_indirect_edge_when_host_allows_creation(self) -> None:
        target = self.base / "missing-target"
        link = self.base / "broken-link"
        try:
            link.symlink_to(target, target_is_directory=True)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"host cannot create a symlink for this check: {exc}")
        self.assertTrue(runtime._has_reparse_component(link))

    def test_full_fsync_seam_uses_darwin_command_and_has_typed_fallback(self) -> None:
        fcntl_module = mock.Mock()
        self.assertTrue(runtime._darwin_full_fsync(17, fcntl_module))
        fcntl_module.fcntl.assert_called_once_with(17, runtime._F_FULLFSYNC)

        interrupted = mock.Mock()
        interrupted.fcntl.side_effect = [OSError(errno.EINTR, "interrupted"), 0]
        self.assertTrue(runtime._darwin_full_fsync(18, interrupted))
        self.assertEqual(interrupted.fcntl.call_count, 2)

        unavailable = mock.Mock()
        unavailable.fcntl.side_effect = OSError(errno.EINVAL, "not supported")
        self.assertFalse(runtime._darwin_full_fsync(19, unavailable))

    def test_manifest_publication_orders_fullfsync_before_rename_and_parent_fsync(self) -> None:
        source = self.base / "manifest.next"
        destination = self.base / "manifest.json"
        source.write_text('{"generation": 1}\n', encoding="utf-8")
        destination.write_text('{"generation": 0}\n', encoding="utf-8")
        events: list[str] = []

        def full_fsync(_descriptor: int) -> bool:
            events.append("F_FULLFSYNC")
            return True

        def replace(left: Path, right: Path) -> None:
            events.append("rename")
            os.replace(left, right)

        def sync_directory(_path: Path) -> None:
            events.append("parent_fsync")

        adapter = runtime._replace_manifest(
            source,
            destination,
            platform_name="darwin",
            full_fsync_operation=full_fsync,
            replace_operation=replace,
            directory_sync=sync_directory,
        )
        self.assertEqual(events, ["F_FULLFSYNC", "rename", "parent_fsync"])
        self.assertEqual(adapter, "darwin-F_FULLFSYNC-rename-parent-fsync/v1")
        self.assertEqual(json.loads(destination.read_text(encoding="utf-8"))["generation"], 1)

    def test_access_report_separates_read_support_from_mutation_qualification(self) -> None:
        root = self.base / "workspace"
        selector = runtime.ResolutionToken(
            mode="generic_explicit",
            selected_root=str(root),
            selected_lexical=str(root),
            provenance="generic_explicit",
        )
        unsupported = {"status": "unsupported", "reason_code": "filesystem_semantics_unsupported"}
        with mock.patch.object(store, "mutation_filesystem_support", return_value=unsupported):
            v2 = store.workspace_access_support(root, selector, runtime.FORMAT)
        self.assertEqual(v2["read"]["status"], "supported")
        self.assertFalse(v2["read"]["mutation_qualification_required"])
        self.assertEqual(v2["mutation"], unsupported)

        qualified = {"status": "qualified", "adapter": "test-adapter/v1"}
        with mock.patch.object(store, "mutation_filesystem_support", return_value=qualified):
            v1 = store.workspace_access_support(root, selector, runtime.LEGACY_FORMAT)
        self.assertEqual(v1["read"]["status"], "supported")
        self.assertEqual(v1["mutation"]["status"], "unsupported")
        self.assertEqual(v1["mutation"]["reason_code"], "migration_required_for_mutation")
        self.assertEqual(v1["mutation"]["filesystem_qualification"], qualified)

    @unittest.skipUnless(sys.platform in {"win32", "darwin"}, "qualified mutation host required")
    def test_open_report_is_read_only_and_reports_qualified_mutation_separately(self) -> None:
        root = self.base / "workspace"
        runtime.initialize_workspace(
            str(root),
            user="user",
            project="project",
            agent="nova",
            thread=None,
            sensitivity="ordinary",
            retention="until-user-changes",
        )
        before = runtime.tree_digest(root)
        report = store.cmd_open(argparse.Namespace(workspace=str(root)))
        self.assertEqual(report["access_support"]["read"]["status"], "supported")
        self.assertEqual(report["access_support"]["mutation"]["status"], "qualified")
        self.assertEqual(report["capabilities"]["capture"], "supported")
        self.assertFalse(report["source_mutated"])
        self.assertEqual(runtime.tree_digest(root), before)

    @unittest.skipUnless(sys.platform == "win32", "Windows compatibility assertion")
    def test_windows_ntfs_adapter_identity_is_unchanged(self) -> None:
        self.assertEqual(
            runtime._filesystem_adapter(self.base, lexical_root=self.base),
            "windows-LockFileEx-MoveFileExW-write-through-ntfs/v1",
        )


@unittest.skipUnless(sys.platform == "darwin", "native Darwin live smoke")
class DarwinLiveSmokeTests(unittest.TestCase):
    def run_json(self, script: Path, *args: object) -> dict:
        completed = subprocess.run(
            [sys.executable, str(script), *[str(value) for value in args]],
            text=True,
            capture_output=True,
            timeout=60,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr or completed.stdout)
        stream = completed.stdout if completed.stdout.strip() else completed.stderr
        return json.loads(stream) if stream.strip().startswith("{") else {"text": stream.strip()}

    def test_native_apfs_flock_fullfsync_manifest_publication_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve() / "workspace"
            initialized = self.run_json(
                STORE,
                "init",
                root,
                "--user",
                "user",
                "--project",
                "darwin-smoke",
                "--agent",
                "nova",
            )
            self.assertEqual(initialized["kind"], "initialized")
            mutated = self.run_json(
                STORE,
                "episode",
                root,
                "--type",
                "tool_result",
                "--content",
                "native Darwin durability smoke",
                "--source-kind",
                "tool",
                "--authority",
                "user-stunspot",
                "--idempotency-key",
                "darwin-live-smoke",
                "--expected-generation",
                0,
            )
            self.assertEqual(mutated["generation_after"], 1)
            validated = self.run_json(VALIDATE, root)
            self.assertIn("VALID:", validated["text"])
            opened = self.run_json(STORE, "open", root)
            self.assertEqual(opened["access_support"]["mutation"]["status"], "qualified")
            self.assertIn("-apfs/", opened["access_support"]["mutation"]["adapter"])
            journals = [json.loads(path.read_text(encoding="utf-8")) for path in (root / "transactions").glob("*/journal.json")]
            commit_adapters = [journal.get("commit_adapter") for journal in journals if journal.get("commit_adapter")]
            self.assertIn("darwin-F_FULLFSYNC-rename-parent-fsync/v1", commit_adapters)


if __name__ == "__main__":
    unittest.main()