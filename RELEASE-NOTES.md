# Cognitive Continuity 0.2.3

Status: **canonical standalone successor checkpoint; local and unpublished**.

No remote release, publication, installation, host discovery, invocation, persistent-store health, or live runtime claim is made by this checkpoint.

## Canonical custody and lineage

The standalone `cognitive-continuity` repository is the canonical source authority for the `0.2.3` successor release. Its recorded lineage base is the exact `0.2.2` synchronized payload from:

- repository: `https://github.com/Stunspot/nova-the-optimal-ai-mind`
- commit: `c48a25b0a1d510d075bc3a519bbc5fab1c6afa33`
- subtree: `plugins/augment-of-mind/skills/cognitive-continuity`

The integrated commit is lineage evidence, not continuing source authority for the standalone line. The `0.2.2` synchronized set was `SKILL.md` plus `adapters/`, `agents/`, `assets/`, `examples/`, `fallbacks/`, `personas/`, `references/`, and `scripts/`. Version `0.2.3` deliberately changes the canonical standalone runtime, focused tests, README, portability reference, and release metadata; it no longer claims byte-for-byte subtree parity. Free Nova `2.1.3` remains an earlier consumer until a separately governed adoption. Standalone repository custody remains with `.git/`, `.github/`, `LICENSE.md`, `docs/`, this release documentation, and other standalone-only files.

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
- Preserves bounded v1 episode content above the ordinary v2 limit without truncation through migration-only provenance tied to generation 0, the migration receipt, and each retained generation receipt.
- Keeps ordinary v2 writes capped, rejects forged or relabeled provenance histories, and protects the retained generation chain required to validate governed forgetting and exact restoration.

## 0.2.0 changes

- Adds Worldline as a read-only project-continuity service with distinct Resume, Status, Checkpoint, and Inspect views. A Worldline view is never a canonical write or persistence receipt.
- Adds Faultline as a cue-gated, zero-to-three-card Error Neighborhood over governed v2 failure evidence. Cards advise within recorded authority; they do not route, authorize, diagnose, repair, retry, or promote procedures.
- Adds the v2 immutable-generation runtime, transaction, validation, export, forgetting-plan, migration, and schema surfaces.
- Exposes the public `continuity_store_v2.py recover` command. It requires human authority, revalidates a selected v2 workspace under lock, reports `clean` or reconciles provable pending transactions as `recovered`, and returns guidance only without mutation for v1.
- Preserves exact v1 read-only compatibility. Mutations require copy migration into a separate v2 workspace, and Faultline returns typed unsupported on v1.
- Accepts maintained v1 0.2.0 manifest extensions and valid full-date effective values. Worldline preserves their settled UTC-midnight meaning in its read-only eligibility view; explicit copy migration applies the same mapping in the successor and binds the normalization count and digest without mutating the source.
- Keeps portable fallback explicit: source-linked, unpersisted, and without a save claim.

## Local checkpoint evidence

The Windows test gate ran 61 tests in 177.552 seconds: 59 passed, the native Darwin smoke skipped on the non-Darwin host, and the real broken-symlink creation check skipped because this Windows token lacks symlink privilege; the controlled lexical-edge test passed. JSON parsing, generated-cache cleanup, and final diff inspection remain part of the local gate. Windows seam evidence does not establish native Darwin behavior; the Darwin smoke command above remains the explicit live-host gate. This checkpoint does not establish publication, installation, host discovery, consumer adoption, or persistent-store health.
