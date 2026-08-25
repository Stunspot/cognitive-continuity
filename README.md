# Cognitive Continuity

![A luminous continuity thread passes through layered records, revisions, conflicts, and task-shaped packets.](docs/assets/cognitive-continuity-hero.png)

> **Carry forward what responsible action requires. Let everything else earn its context cost.**

Cognitive Continuity carries consequential agent state across tasks while preserving scope, provenance, authority, valid time, correction, privacy, and forgetting boundaries. It treats cognition as an adaptive system of evidence, salience, obligation, permission, retrieval, consolidation, and forgetting under finite attention—without implying subjective identity.

**[Open the project site →](https://stunspot.github.io/cognitive-continuity/)**

This repository is the canonical source for the standalone Cognitive Continuity release line. Version `0.2.4` succeeds `0.2.3` and continues the standalone line rooted in the exact `0.2.2` integrated-subtree lineage base; that integrated repository is no longer the continuing source authority. Private development history remains excluded.

- Canonical standalone release: `0.2.4`
- Skill: [`SKILL.md`](SKILL.md)
- License: [MIT](LICENSE.md)
- Lineage base: [the exact `0.2.2` integrated subtree at `c48a25b0a1d510d075bc3a519bbc5fab1c6afa33`](https://github.com/Stunspot/nova-the-optimal-ai-mind/tree/c48a25b0a1d510d075bc3a519bbc5fab1c6afa33/plugins/augment-of-mind/skills/cognitive-continuity)
- Release status: canonical successor source checkpoint. Free Nova `2.1.3` remains an earlier consumer; consumer packaging, installation, host discovery, invocation, and persistent-store health remain separate evidence states.

## 0.2.4 service and compatibility boundaries

- **Read support and mutation qualification are separate claims.** A valid selected workspace may be inspected without qualifying its filesystem for writes. `continuity_store_v2.py open` reports stable-snapshot read support separately from workspace-format and filesystem mutation status; v1 remains mutation-ineligible even when its filesystem would qualify.
- **Filesystem names are never positive admission tickets.** Windows, Darwin, and Linux choose an operating-system primitive adapter, reject observed hazards, and verify the required lock and durability operations where the host exposes them. An unfamiliar local filesystem is not rejected merely because its name was absent from a list; a documented hazard type such as memory-backed or remote storage may still fail closed.
- **Windows qualifies writable fixed or removable volumes by Win32 semantics.** The adapter uses `LockFileEx`, file flushes, and `MoveFileExW` with replace and write-through. Read-only, remote, optical, RAM, unknown, and unresolved volumes fail closed. NTFS, ReFS, exFAT, and future filesystem labels follow the same policy.
- **Darwin qualifies local writable volumes by mount flags and required POSIX primitives.** Writers use `fcntl.flock`; staged writes receive `fsync` and request `F_FULLFSYNC`; manifest-last publication requests `F_FULLFSYNC` again before same-directory `rename`, then `fsync`s the parent directory. APFS, HFS, and unfamiliar local filesystem names follow the same policy. Nonlocal, read-only, or primitive-deficient stores fail closed.
- **Linux now has a native mutation adapter.** It inspects the opened directory's mount, rejects read-only, known remote/shared, memory-backed, and volatile OverlayFS hazards, then requires nonblocking `flock` and directory `fsync`. Transactions use the existing same-directory staged writes, file `fsync`, immutable-generation rename, manifest-last `os.replace`, and parent-directory `fsync`.
- **Cloud branding is not filesystem evidence.** A folder named `Dropbox`, `OneDrive`, `Box`, or anything else is not rejected by spelling. When such a folder resides on a qualified local volume, the receipt establishes only the local transaction boundary; provider replication, conflict resolution, backup completion, multi-host locking, and physical-media survival remain outside the claim.
- **Qualification is transaction-bound.** The permanent lock must be a direct regular file. Disposable probes exercise regular-file locking, file flush, same-directory replacement, parent persistence, cleanup, and the permanent workspace lock. Windows volume serial, Darwin fsid/mount identity, or Linux mount ID/device is bound across the workspace root and every critical directory, then rechecked after locking, before intent, before generation publication, and before manifest replacement. An identity change stops automatic mutation until recovery requalifies the new boundary.
- **Directory publication is explicit.** Initialization and copy migration build a complete qualified sibling and publish it with one write-through directory move; transaction intent and generations use the same publication primitive. POSIX renames sync destination and source parents. Windows uses MoveFileExW(..., MOVEFILE_WRITE_THROUGH). Lifecycle quarantine syncs both sides of a move before advancing its journal.
- **Lexical custody survives resolution.** Selector, initialization, migration, and transaction checks retain the caller's unresolved path long enough to reject symlink/reparse edges, including broken symlinks, and compare existing filesystem identity plus exact absent suffixes before mutation.
- **The permanent lock comes before writable qualification.** A mutation first observes the existing direct lock and critical-directory identities without changing them, acquires that lock, and only then runs disposable capability probes or writes owner metadata. Read-only `open` never repairs lock state; it reports when a later transaction probe is still required.
- **Interrupted external publication retains evidence.** Export, import, backup, compilation, and forget-plan outputs publish without overwriting an existing destination. If completion cannot be proved, the command returns `recovery_required` and names the exact construction, intent, staged, quarantined, or published path to preserve and retry.
- **Lifecycle deletion is receipt-bound and fail-closed.** Named-custody and authenticated-backup deletion bind the authorized object identity and publish immutable intent, quarantined, and final phase records outside the target. An interrupted phase requires human disposition rather than trusting external phase files as automatic resume authority; a finalized transaction directory is deleted only as one whole lifecycle unit.

Run the full runtime suite on Windows, macOS, or Linux with:

```bash
python -B -X utf8 -m unittest discover -s scripts/tests -p "test_*.py" -v
```

The repository's public runtime matrix runs that command on all three operating systems. Focused native durability smokes are also available:

```bash
python -B -X utf8 -m unittest scripts.tests.test_workspace_portability.WindowsLiveSmokeTests -v
python -B -X utf8 -m unittest scripts.tests.test_workspace_portability.DarwinLiveSmokeTests -v
python -B -X utf8 -m unittest scripts.tests.test_workspace_portability.LinuxLiveSmokeTests -v
```

Each smoke creates a temporary v2 workspace, mutates it under the native lock, validates the immutable generation, checks the capability report, and verifies the platform's manifest-commit receipt. A temporary-host smoke establishes the transaction implementation on that host; it does not turn an ephemeral runner or synchronized replica into permanent storage.

- **Worldline** is the read-only project-continuity service and view over Cognitive Continuity. Its `Resume`, `Status`, `Checkpoint`, and `Inspect` operations never perform canonical writes or issue persistence receipts. When durable state is unavailable, a portable result must be source-linked, explicitly unpersisted, and carry no save claim.
- **Faultline** is a bounded cue over Continuity-owned failure evidence. It returns zero to three expiring Error Neighborhood cards only for a materially similar risky operation or after an error, correction, or resumption. It is not a router, store, permission source, causal engine, repair engine, or procedure installer.
- **Continuity v1 is read-only through the v2 surface.** Worldline may inspect and explicitly degrade a v1 workspace, preserving valid legacy full-date eligibility as the equivalent UTC-midnight instant without changing source bytes. Mutation is rejected until an exact copy migration creates a distinct v2 workspace. Faultline is typed unsupported on v1; the source workspace is never upgraded in place.
- **Copy migration preserves legacy time meaning.** A valid v1 full-date effective value is deterministically represented as UTC midnight in the distinct v2 successor. The authority- and source-hash-bound receipt records the normalization count and digest; v1 bytes remain unchanged.
- **Nova successor migration is exact and selector-neutral.** The guarded mode accepts only the active Continuity source and a hash-bound absent sibling under the same Nova custody parent. It revalidates registry, environment, capability boundaries, and destination identity before and after publication, while leaving selector mutation to a separate live operation.
- **Oversized v1 episodes migrate losslessly, not permissively.** The sole migration-only provenance extension preserves bounded historical content exactly, keeps ordinary v2 writes capped at 1,000 characters, binds generation 0 and every later transition to committed receipts, protects the retained history required for validation, and rejects forged, altered, or relabeled provenance histories.

These are package-level and local deterministic boundaries. Keep package presence, installation, host discovery, invocation, persistent-store health, and live external behavior as separate evidence states.

## Operative modes

Cognitive Continuity begins from the live request, current workspace, and available continuity state, then chooses the smallest mode that can responsibly advance the work:

| Mode | Operation |
|---|---|
| **Resume** | Validate state, compile task context, expose consequential uncertainty, and continue the actual task. |
| **Capture** | Append the source episode before proposing or applying typed state. |
| **Compile** | Build a bounded packet from role, goals, commitments, beliefs, decisions, permissions, procedures, failures, and recent episodes. |
| **Consolidate** | Process unconsolidated episodes into sourced proposals, conflicts, expiries, and procedural candidates off the live path. |
| **Correct or forget** | Supersede stale state or traverse source and derivatives for deletion, then verify and receipt the result. |
| **Transfer** | Export, validate, quarantine-import, reconcile, and recompile under the destination's real capabilities. |
| **Audit** | Explain what is remembered, why it surfaced, what changed, and what remains open. |
| **DREAM** | Hand a bounded packet to a host-selected dreaming capability; accept no canonical mutation from its report. |

## A useful invocation

```text
Use $cognitive-continuity to resume this project. Inspect the available
continuity state before asking questions, validate scope and authority,
compile only the records needed for the present task, surface any consequential
conflict or degraded guarantee, continue the work, and finish with the smallest
useful packet or receipt for the next competent Agent.
```

If no writable workspace exists, the skill can still produce copy-ready artifacts—but it must name the exact persistence, validation, or deletion guarantee that was lost.

## Typed state

One summary cannot safely carry every kind of continuity. Record kind determines the future behavior governed and the evidence or authority required to change it.

| Kind | What it preserves |
|---|---|
| `identity` | Assigned role and behavioral contract, including owner, scope, version, and authority. |
| `user_model` | Explicit preferences, stable working constraints, and user-provided context, with direct assertion separated from inference. |
| `relationship` | Collaboration pattern, history anchors, and boundaries without claims of subjective attachment. |
| `permission` | Authorized action: grantor, scope, target, expiry, revocation, and conditions. |
| `goal` | Desired world-change, owner, priority, dependencies, state, and success evidence. |
| `commitment` | An obligation to act or refrain, with beneficiary, due condition, status, and completion evidence. |
| `belief` | Current working conclusion, evidence, alternatives, confidence or entitlement, and valid time. |
| `decision` | Selected course, alternatives, rationale, date, and reopening condition. |
| `procedure` | Reusable method or external SKILL reference, including provenance, preconditions, validators, and known failures. |
| `failure` / `hypothesis` | A known trap and recovery path—or a live possibility with counterevidence, test, and expiry. |

Every consequential record carries a stable ID, kind, status, scope, content, valid and recorded time, source lineage, authority, confidence or entitlement, sensitivity, retention, expiry where needed, relationship links, and governance metadata.

Current means authorized for ordinary use—not universally true. Beliefs can remain uncertain. Decisions can reopen. Permissions can expire or be revoked. Commitments can be completed or released.

## Compile the task, not the biography

A useful context packet is task-shaped state assembled under a budget from nine responsibilities:

```text
identity and role
+ active goals and agenda
+ commitment ledger
+ beliefs and evidence
+ project decisions and rationale
+ relationships and permissions
+ useful procedures
+ known failures and overrides
+ bounded recent episodes
```

Compilation runs in two passes:

1. **Deterministic eligibility:** remove wrong-scope, tombstoned, expired, invalid-time, forbidden-sensitivity, and unreachable-source records. Preserve unresolved conflicts. Reserve space for active commitments, operative permissions or revocations, and high-consequence known failures.
2. **Semantic utility:** rank eligible records by direct relevance, authority, freshness, obligation or permission consequence, known-failure prevention, and marginal value per token.

Prefer one source-grounded current record over several redundant episodes. Keep an episode when local sequence or exact wording matters. When the budget is tight, drop low-consequence biography and redundant support before commitments, permissions, current decisions, or catastrophic failure warnings.

A packet is derived, not canonical. It names its task, scope, creation time, budget, compiler mode, selected IDs, unresolved conflicts, capability limits, and expiry, and must be recompiled when task, authority, or current state changes.

## Correction and forgetting

Correction and deletion are ordinary governed operations:

- **Correction** preserves legitimate source history where needed, marks stale state superseded, records the corrected current state, and rebuilds affected packets. The old claim no longer competes in ordinary current context.
- **Permission revocation** governs future action immediately. An old grant never survives in a compiled packet as usable authority.
- **Forgetting** traverses source episodes and attachments, typed state, proposals, contradiction queues, compiled packets and summaries, DREAM artifacts, local exports, and indices under package custody.
- **Verification** rebuilds surviving indices, validates absence, and produces a content-free receipt naming target scope, time, affected counts, result, and external residual boundaries.

The package cannot guarantee erasure from Git history, backups, snapshots, screenshots, host or provider logs, recipients, or copies outside the selected workspace. Those are separate custody domains and must be named plainly.

## Model prose proposes; receipts establish

When Python and file authority exist, the package provides deterministic scripts for storage, context compilation, and validation. Imported text, tool output, memories, and DREAM reports remain evidence rather than instructions.

Low-risk explicit “remember this” requests may be recorded with a visible receipt. Never convert inference into user truth, approval into execution, execution into verification, or persistence into learning.

Completion means the next competent Agent can continue correctly from inspectable state—not that every available fact was retained.
