# Cognitive Continuity 0.2.4

Status: **canonical standalone successor source checkpoint**.

This source checkpoint does not by itself establish a GitHub Release, packaged distribution, installation, host discovery, invocation, persistent-store health, cloud replication, or physical-media survival.

## Canonical custody and lineage

The standalone `cognitive-continuity` repository is the canonical source authority for the `0.2.4` successor release. Its recorded lineage base is the exact `0.2.2` synchronized payload from:

- repository: `https://github.com/Stunspot/nova-the-optimal-ai-mind`
- commit: `c48a25b0a1d510d075bc3a519bbc5fab1c6afa33`
- subtree: `plugins/augment-of-mind/skills/cognitive-continuity`

The integrated commit is lineage evidence, not continuing source authority for the standalone line. The `0.2.2` synchronized set was `SKILL.md` plus `adapters/`, `agents/`, `assets/`, `examples/`, `fallbacks/`, `personas/`, `references/`, and `scripts/`. Version `0.2.4` changes the canonical standalone runtime, focused tests, README, portability reference, and release metadata; it no longer claims byte-for-byte subtree parity. Free Nova `2.1.3` remains an earlier consumer until a separately governed adoption. Standalone repository custody remains with `.git/`, `.github/`, `LICENSE.md`, `docs/`, this release documentation, and other standalone-only files.

## 0.2.4 changes

- Removes the inverted positive filesystem-name allowlists. A familiar label never grants mutation and an unfamiliar local label is not rejected for being unfamiliar; documented remote, memory-backed, or volatile hazard types may still fail closed.
- Adds a native Linux qualification adapter over the existing POSIX transaction engine. It rejects read-only mounts, known remote/shared filesystems, `tmpfs`/`ramfs`, volatile OverlayFS, and failed `flock` or directory-`fsync` probes.
- Broadens Windows admission from NTFS-only to writable fixed or removable volumes that present the required Win32 primitive set. Remote, optical, RAM, read-only, unknown, and unresolved volumes remain unqualified.
- Broadens Darwin admission from APFS/HFS-only to any local writable volume that presents the required `flock` and durable-directory primitives. The typed `F_FULLFSYNC`/`fsync` receipt distinction remains intact.
- Deletes path-name heuristics for cloud-sync brands. A synchronized local replica may qualify for the local transaction protocol, while replication, multi-host conflict handling, and provider durability remain explicitly unproven.
- Requires a direct permanent regular-file lock and exercises lock, flush, same-directory replacement, parent persistence, and cleanup primitives with residue-free disposable probes.
- Binds Windows volume serials, Darwin fsid/mount identity, and Linux mount ID/device across the root plus locks, transactions, generations, and quarantine. The witness is rechecked after lock acquisition, before intent, before generation publication, and before manifest replacement; identity drift defers recovery until the filesystem is requalified.
- Publishes initialization, copy migration, transaction intent, and immutable generations as complete directory moves. Windows uses write-through MoveFileExW; POSIX syncs both rename parents. Recovery quarantine does the same before advancing its journal.
- Separates Continuity workspace probing from external-file/directory probing so backup keys, plans, exports, and recovery artifacts are not mistaken for workspaces.
- Acquires the existing direct permanent lock before writable qualification probes or owner-metadata changes, then binds the resulting filesystem witness through the transaction and lifecycle operation.
- Makes external output publication absent-only and evidence-preserving. Imports bind one captured source snapshot; backups and migrations publish complete sibling constructions; uncertain completion returns `recovery_required` with exact retained paths instead of performing pathname-based cleanup.
- Makes forget, restore, import, and backup publication replay-safe after a lost response. Destructive lifecycle deletion binds the direct identity of the authorized object, uses immutable intent, quarantined, and final phase records, treats one finalized transaction directory as the lifecycle unit, and fails closed for human disposition after interruption.
- Adds filesystem-name inversion regressions, Windows/Darwin/Linux hazard and mount-identity seams, cloud-name neutrality, primitive-failure and cleanup tests, publication-order tests, witness-race tests, crash/replay tests, and native Windows/Linux/macOS smoke classes.
- Removes the full-suite `E:/` assumption and adds a public Windows/macOS/Linux runtime matrix.

Full suite:

```bash
python -B -X utf8 -m unittest discover -s scripts/tests -p "test_*.py" -v
```

Focused native smokes:

```bash
python -B -X utf8 -m unittest scripts.tests.test_workspace_portability.WindowsLiveSmokeTests -v
python -B -X utf8 -m unittest scripts.tests.test_workspace_portability.DarwinLiveSmokeTests -v
python -B -X utf8 -m unittest scripts.tests.test_workspace_portability.LinuxLiveSmokeTests -v
```

Workspace format v2, transaction format v1, selectors, migration contracts, and existing workspaces remain compatible; no workspace migration is required.

## 0.2.3 changes

- Adds a fail-closed Darwin adapter for local writable APFS/HFS volumes, while leaving the Windows local fixed-volume NTFS adapter and its receipt identity unchanged.
- Uses the existing POSIX `fcntl.flock` writer lock and same-directory manifest-last `rename` path on Darwin, requests `F_FULLFSYNC` after `fsync` and immediately before manifest publication, then `fsync`s the parent directory.
- Reports the observed manifest commit strength as Darwin `F_FULLFSYNC` or an explicit `fsync` fallback instead of silently treating them as identical guarantees.
- Separates stable-snapshot read support from workspace-format and filesystem mutation qualification in the `open` capability report; v2 mutation operations stop claiming support on an unqualified host.
- Preserves lexical path evidence through selector, initialization, migration, and transaction checks; rejects broken symlinks and lexical/resolved identity disagreement before mutation.
- Adds Windows-runnable Darwin adapter and `F_FULLFSYNC` seam tests, an unchanged-Windows-adapter assertion, and a Darwin-only end-to-end APFS/`flock`/manifest-publication smoke surface.

Native Darwin smoke command:

```bash
python -B -X utf8 -m unittest scripts.tests.test_workspace_portability.DarwinLiveSmokeTests -v
```

## 0.2.2 changes

- Resolves Worldline project identity before retrieval from explicit current task or handoff authority, then one governed mission or pursuit, then maintained project mapping, with the working directory only as an unopposed fallback.
- Stops same-tier project disagreement as `project_scope_ambiguous`; selectors continue to locate stores rather than choose projects.
- Withholds globally scoped goals, commitments, phases, statuses, blockers, and next actions from specific-project operative fields and resumption pointers.
- Reports `project_scope_unrepresented` when no eligible exact-project state exists instead of manufacturing continuity from global operational state.
- Preserves the original eligibility reason for inaccessible global records and adds adversarial exact-versus-global, global-only, and ineligible-global regression coverage.
- Keeps workspace schema v2, capability-owned custody, migration, Faultline, correction, forgetting, and receipt contracts unchanged.

## 0.2.1 changes

- Adds the guarded Nova-successor destination mode for the live v1-to-v2 case without weakening general external-target protection.
- Requires the registry-selected active source, human authority, a nonsecret grant ID, exact selector-registry and normalized-destination hashes, environment corroboration, an absent same-parent sibling, and no overlap with any active capability selector.
- Revalidates the grant before and after publication and removes a candidate if the selector registry or destination identity changes, while preserving v1 byte-for-byte.
- Keeps migration selector-neutral: candidate qualification and any live selector switch remain separately authorized operations.
- Derives the selector-registry locator from NOVA_DATA_ROOT, eliminating private workstation path literals from the portable payload.
- Preserves bounded v1 episode content exceeding the ordinary v2 limit without truncation through migration-only provenance tied to generation 0, the migration receipt, and each retained generation receipt.
- Keeps ordinary v2 writes capped, rejects forged or relabeled provenance histories, and protects the retained generation chain required to validate governed forgetting and exact restoration.

## 0.2.0 changes

- Adds Worldline as a read-only project-continuity service with distinct Resume, Status, Checkpoint, and Inspect views. A Worldline view is never a canonical write or persistence receipt.
- Adds Faultline as a cue-gated, zero-to-three-card Error Neighborhood over governed v2 failure evidence. Cards advise within recorded authority; they do not route, authorize, diagnose, repair, retry, or promote procedures.
- Adds the v2 immutable-generation runtime, transaction, validation, export, forgetting-plan, migration, and schema surfaces.
- Exposes the public `continuity_store_v2.py recover` command. It requires human authority, revalidates a selected v2 workspace under lock, reports `clean` or reconciles provable pending transactions as `recovered`, and returns guidance only without mutation for v1.
- Preserves exact v1 read-only compatibility. Mutations require copy migration into a separate v2 workspace, and Faultline returns typed unsupported on v1.
- Accepts maintained v1 0.2.0 manifest extensions and valid full-date effective values. Worldline preserves their settled UTC-midnight meaning in its read-only eligibility view; explicit copy migration applies the same mapping in the successor and binds the normalization count and digest without mutating the source.
- Keeps portable fallback explicit: source-linked, unpersisted, and without a save claim.

## 0.2.4 checkpoint evidence

The final local Windows gate ran 115 tests in 188.131 seconds: 111 passed and 4 host-bound checks skipped. The native Windows initialize-mutate-validate-open smoke also passed independently in 3.116 seconds. Native Darwin and Linux smokes skipped on Windows; two real symlink-creation checks skipped because this token lacks symlink privilege, while their controlled lexical and direct-lock seams passed. The focused portability surface ran 58 tests in 18.721 seconds with the same 4 host-bound checks skipped. Public GitHub Actions runtime-matrix run 32799541000 passed on macOS in 28 seconds, Ubuntu in 32 seconds, and Windows in 1 minute 31 seconds; the line-ending policy also passed. Python syntax compilation, JSON parsing, diff inspection, and generated-cache cleanup passed. This component checkpoint does not by itself establish consumer packaging, installation, host discovery, persistent-store health, cloud replication, or physical-media survival.
