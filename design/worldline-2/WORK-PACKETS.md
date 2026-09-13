# Worldline 2 work packets
Case ARC-WORLDLINE-2 revision1. Authority: current explicit owner rebuild. Exact interfaces: CONTRACTS.md C1-C8. Root owns BUILD-STATE.md, integration and shared version/build/release seams.

## WP1: durable occurrence, control and lifecycle
Trace INT1/3/5/6/7; Q3/Q4/Q6/Q7; D1/D2/D4/D5.
Owner: root-assigned runtime implementer. Entry: reviewer-ready frozen C1-C8; no blocking finding.

Permitted surfaces: episode-v2 schema and new event/policy/capture schemas; additive export-v2 support; continuity_store_v2.py; validate_continuity_v2.py; new worldline_domain.py helper; new event/lifecycle tests and directly affected existing tests. No existing v1 query changes, prompt/core edits, live history rewrite or release metadata without root delegation.

Provide capture_worldline(request, registry_path=None) and set_worldline_policy(request, registry_path=None) in continuity_store_v2.py for the WP2 CLI. Keep domain validation independent of queries. Export may lazily call the shared historical selector in worldline_timeline.py so read and transfer eligibility cannot drift; omit any family with a denied required ancestor. Reuse writable selector, transaction, generation, idempotency and receipt machinery. Implement C1-C4/C6/C8: safe metadata, scope, ordinary/off and explicit/current no-retention, committed-order policy resolved under lock, corrections inheriting privacy, retraction, exact family forget and surviving independent-edge severing, event-aware safe export and quarantine import.

Acceptance: process-reopen persistence; same input one event, changed input same key conflicts; unconfigured/off/no-retention no write; ordinary then off wins with regressing/equal recorded timestamps; concurrent off cannot be bypassed; correction ordinary-to-sensitive never reveals old ordinary revision; expired/retracted family cannot revive; family forget scrubs payload/tags/locators, preserves independent neighbors in three-event chain and severs edges; recognized current generated HTML joins the authenticated backup and existing deletion lifecycle before success, while unknown or changed views stay blocked; interruption reports recovery rather than success; secret/cross-owner invalid input fails before journal; safe export/import round trip; old reader fails without mutation.

Handoff: named diff/revision, command/schema examples, public signatures and test evidence. Context is this packet plus C1-C4/C6/C8; root provides governing existing runtime contracts. Escalate a semantic incompatibility, not routine implementation choice. Rollback unshipped code or disable new capture; never silently downgrade evolved live state.

## WP2: navigable past and standalone projection
Trace INT1/2/3/4/5/8; Q1/Q2/Q4/Q5/Q6/Q7; D1/D3/D4.
Owner: query/presentation implementer. Entry: C1-C8 frozen; may build while WP1 works, but integrated CLI waits for its public command seam.

Permitted surfaces: new worldline_timeline.py; new timeline request/view schemas; new timeline/HTML tests and renderer asset if needed. Do not edit continuity_store_v2.py, old worldline.py/v1 schemas, prompts or release files. Query entry: query_worldline(request, registry_path=None); CLI dispatches capture/policy via lazy WP1 import, with convenient manifest-derived exact identity/defaults.

Implement historical owner-safe eligibility, physical generation binding, root/revision family normalization using current privacy envelope, time basis/precision, immediate legacy recognition, search/topics/kinds, full-set overview, deterministic cursors and budget/deadline coverage. Recheck retention at execution time on every page; as_of cannot revive expired content. Counts begin only after owner gating. Render explicit-output-only bounded static HTML with safe text/links, accessible cards/groups, fixed-offset/coverage labels and another-window CLI guidance; no server/CDN/file-fetch loop.

Acceptance: mixed project/projectless/thread-native/legacy month, foreign owner title/ID/facet/count canaries, recorded versus validity time, coarse/unknown labels, repeated titles distinct, multiple equal-time pages without loss/duplication, changed generation typed restart, current expiry with old as_of withheld, byte budget cannot yield nonadvancing cursor, overview counts full filtered set, sensitive latest correction cannot expose root, intact pointers, missing store read-only, hostile HTML inert. Hash tree around read tests.

Handoff: named diff, JSON/schema/CLI examples, representative standalone HTML and test evidence. Root coordinates integration. Re-entry C2/C4-C8; stop only for shared-seam change or unowned invariant. No live canonical-state mutation within this packet.

## WP3: existing Faculty and both edition behavior
Trace INT1/2/6/7/8; Q1/Q7/Q8; D1/D2/D5.
Owner: root for semantic/core edits; delivery worker for explicitly assigned launcher/build/version seams. Entry: frozen case and BEHAVIOR-SEED.md understood as proposed performance seed.

Root or its specifically delegated component owner edits component SKILL.md and Worldline references/docs/examples; root edits existing Free cognitive-continuity.core.md and matching registry/provenance/base-service text through governing tools. Use Promptcraft. Preserve persona, 17 cores, other owners and task-continuity skill. Current edition-owned MIND component moves0.3.1 to0.4.0; retired standalone MIND stays untouched.

Delivery worker updates governing consumer locks/manifests, launchers, package closure and versions: Continuity0.3.0, Free3.2.0, Emergent1.1.0. Root arbitrates any shared file. No implicit runtime dependencies or new hosts.

Behavior admits ordinary curiosity, surveys before content replay, records coherent episodes with established authority without repeat consent, honors off/no-retention, distinguishes attempt/outcome and event/recorded time, and credits only receipts. Customer setup offers ordinary/off once. This owner's rebuild already authorizes ordinary local indexing; no second permission request. Do not promise unobserved automatic host invocation.

Acceptance: no universal project gate or anti-biography instruction remains; same new contract in both editions; 17-core topology unchanged; easy launcher commands reach timeline/capture/control/render; old project routes still work; package closure and examples include sparse/missing/off/ordinary cases. Handoff exact component/consumer revisions and documentation truth. Contract changes invalidate only affected prose/build checks.

## WP4: independent evidence and applicable delivery
Trace all intent IDs. Owner root plus independent verification and existing delivery owners.
Entry: WP1-WP3 integrated, exact candidate named, architecture findings closed. Run focused event/timeline/lifecycle and legacy Worldline checks, then independent verification of the frozen candidate. Broad pre-edit baseline interrupted by root is neither pass nor failure.

Acceptance cutoff: user-important native/legacy survey, scope/time/link/control/cursor/correction/forget/transfer boundaries, safe rendering, old-reader no-mutation, both package closures and real current local invocation. Failures return to bounded owning packets. Repeated support-layer failures receive one credible substitute or exact residual boundary, not expanding testing.

After cutoff reconcile authorized existing repositories, packages, sidecars, shelf/catalog and installed edition using current contracts. Preserve private hosted-Actions hold. Record ordinary policy for this owner once and source-linked current design-conversation event, reopen in new process and render its bounded past. No broad transcript backfill. Root updates BUILD-STATE.md and appends named-revision convergence; final handoff reports usable/current result and exact remaining host limits. New announcement/channel/paid/visibility/destructive-history actions remain outside scope.

## Parallel safety and re-entry
WP1/WP2 own distinct files but share frozen contracts; neither changes schemas or semantics unilaterally. WP3 semantic work can proceed against the same contracts. Root alone assigns shared core provenance/source locks/version files. No agent touches live store until integrated WP4. Work packets are bounded derivatives of the case, not new architecture authority.

