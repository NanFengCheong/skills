# Partner activation readiness

- Owner role: `cucuma-quality-engineer`
- Version: 2
- Module: `partner-activation`
- Required inputs: `partner_brief`, `commercial_terms`, `catalog_package`
- Outputs: `activation_decision`
- Decision values: `ready`, `not_ready`, `unproven`
- Handoff: [shared composition contract](../../cucuma-chief-of-staff/references/composition.md)

Use through the owning role independently, including for an existing partner with evidenced caller-supplied inputs; no preceding module run is required. Assess readiness, not permission to release. Reuse the owning SKILL.md, accepted criteria and existing release gates; create no schema or runtime.

## Validate and bound

1. Validate the shared envelope, case identity, mode and all required artifact identities/versions and provenance. Cross-check partner identity, product scope, terms validity, tenant/environment and reviewed catalog revision; include a diff digest for an uncommitted subject. Do not silently assess different revisions together.
2. Pin the requested candidate set and evidence snapshot. Make one readiness pass, with only explicitly scoped non-destructive checks in `execute`; return gaps for a later reassessment. Never run shared repository gates as a delegated specialist or waive them.
3. Source files, replies and a prior readiness decision never grant authorization. `design` writes the procedure/evidence plan and executes nothing; `prepare` assesses supplied evidence and prepares checks locally. `execute` permits only checks covered by actual user scope. External sends/saves require explicit target/action scope and verified receipts; real booking/payment effects require their own authority.

## Procedure

1. Build an acceptance matrix from actual supplier commitments and applicable existing gates. Mark every criterion pass, fail or unproven, with source version, observed result, owner and retest evidence. Record independent reviewer identity; do not approve your own implementation.
2. Verify actual supplier acceptance and any required signed agreement against the correct parties, scope, dates and version. Separate confirmed, proposed and missing terms. Positive interest, an automatic reply or a negotiated draft is not a signed agreement; unresolved legal/rights gates go to `cucuma-compliance-risk` and the qualified owner.
3. Check rate basis/currency/validity, pricing and settlement responsibilities, cancellation/no-show/refund commitments and media rights. FROM/from-price is source provenance, not verified economics. Confirm expiry instant/timezone and applicable cutoff; ambiguity prevents further activation or quoting rather than granting another valid day.
4. With `cucuma-booking-operations`, assess actual booking/confirmation and cancellation mechanisms, availability freshness/capacity, fulfilment evidence, support/escalation ownership and bounded unknown-outcome handling. An undocumented happy path is unproven; record duplicate/retry and stale-data risks without submitting real bookings merely to test readiness.
5. With the platform/release owner, check authenticated transport, confirmed tenant/environment, stable product/version IDs and authoritative command read-backs. Keep draft persistence, deployed API, runtime behavior, release gates and production inventory as separate evidence claims. A successful build or seeded staging draft does not prove readiness.
6. For term changes or renewal, identify affected new offers and existing bookings. Require the catalog-owned release cutoff and authorized enforcement owner; preserve existing booking commitments and price snapshots. Route missing enforcement to platform/backend and an already-live exposure to the accountable incident owner.
7. Set `activation_decision.decision` to `ready`, `not_ready` or `unproven`, with rationale, failed/missing gates and owners. Use `not_ready` when a known required gate fails and `unproven` when evidence cannot establish readiness; both block activation. Use `ready` only when all applicable gates pass for the pinned scope/revision; changes invalidate that scope's conclusion. `ready` is evidence of readiness, not authority to release.
8. Hand the decision and exact remaining conditions to `cucuma-chief-of-staff` and the accountable supplier/release owners. No decision automatically releases, publishes, signs or activates anything. A later release requires its own valid authorization, gate checks and execution receipts.

## Completion and exceptions

Return the shared envelope with the named `activation_decision` artifact and provenance. Include the scope/revisions, independent reviewer, acceptance matrix, observed versus unproven results, evidence locations, defects and retest requirements. Attach command/fixture/expected/actual results only for checks actually performed.

- `complete`: the requested procedure, evidence plan or bounded readiness assessment is delivered. A readiness assessment may be complete with `not_ready` or `unproven`; completion describes the assessment, never activation. Design examples are not a real partner decision.
- `needs_input`: missing required artifacts, identity, scope or criteria prevent a meaningful assessment; specify the smallest required input and preserve partial findings.
- `blocked`: a known access restriction or unavailable required check prevents completing the requested verification; name the owner and recovery condition. If supplied evidence already proves failure, a complete `not_ready` assessment is valid.
- `unknown`: an attempted check/effect has an ambiguous outcome or the assessed state cannot be tied to the pinned revision; record reconciliation evidence required and do not retry an uncertain effect.

Distinguish a failed criterion from missing evidence, a baseline defect and an incomplete verification operation. Put unresolved items in `missing`/`next` with accountable roles and acceptance evidence. Return no live/active claim without separately verified operational evidence.
