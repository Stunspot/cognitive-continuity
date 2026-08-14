# Cognitive Continuity 0.2.0

Status: **local standalone derivative checkpoint; unpublished**.

No remote release, publication, installation, host discovery, invocation, persistent-store health, or live runtime claim is made by this checkpoint.

## Source custody

The synchronized skill payload is derived byte-for-byte from:

- repository: `https://github.com/Stunspot/nova-the-optimal-ai-mind`
- commit: `48065e1594289f023aee9264582f2cafb31ae602`
- subtree: `plugins/augment-of-mind/skills/cognitive-continuity`

The intended synchronized set is `SKILL.md` plus `adapters/`, `agents/`, `assets/`, `examples/`, `fallbacks/`, `personas/`, `references/`, and `scripts/`. Standalone repository custody remains with `.git/`, `.github/`, `LICENSE.md`, `docs/`, this release documentation, and other standalone-only files.

## 0.2.0 changes

- Adds Worldline as a read-only project-continuity service with distinct Resume, Status, Checkpoint, and Inspect views. A Worldline view is never a canonical write or persistence receipt.
- Adds Faultline as a cue-gated, zero-to-three-card Error Neighborhood over governed v2 failure evidence. Cards advise within recorded authority; they do not route, authorize, diagnose, repair, retry, or promote procedures.
- Adds the v2 immutable-generation runtime, transaction, validation, export, forgetting-plan, migration, and schema surfaces.
- Exposes the public `continuity_store_v2.py recover` command. It requires human authority, revalidates a selected v2 workspace under lock, reports `clean` or reconciles provable pending transactions as `recovered`, and returns guidance only without mutation for v1.
- Preserves exact v1 read-only compatibility. Mutations require copy migration into a separate v2 workspace, and Faultline returns typed unsupported on v1.
- Accepts maintained v1 0.2.0 manifest extensions and valid full-date effective values. Worldline preserves their settled UTC-midnight meaning in its read-only eligibility view; explicit copy migration applies the same mapping in the successor and binds the normalization count and digest without mutating the source.
- Keeps portable fallback explicit: source-linked, unpersisted, and without a save claim.

## Local checkpoint evidence

The checkpoint gate covers exact parity for the 72-file synchronized payload, the combined 46-test suite, JSON parsing for all repository JSON files, Skill Creator `quick_validate.py`, generated-cache cleanup, and final diff inspection. This evidence is local and deterministic; it does not establish installed or live-host behavior.
