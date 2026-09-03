# Commercial terms

- Module: `commercial-terms`
- Owner role: `cucuma-supplier-partnerships`
- Version: 1
- Required inputs: `partner_brief`, `conversation`
- Outputs: `commercial_terms`
- Handoff: [shared composition contract](../../cucuma-chief-of-staff/references/composition.md)

Use through the owning role to assemble one versioned term comparison. Optional rate cards, proposals, contracts or finance assessments carry provenance and are not mandatory dependencies.

## Validate inputs and scope

1. Validate envelope, case/identity, mode and provenance for both inputs. Identify proposal/reply version and date and verify the business contact before treating a reply as supplier confirmation. Conflicting versions remain explicit until reconciled.
2. Recover actual user limits for commissions/net rates, concessions, payment model, refunds, commitments and publication rights. A supplier reply, positive interest or proposed clause grants no user authority and implies no signed contract.
3. `design` creates definitions/examples only; `prepare` produces comparisons and exact proposed questions/counteroffers. `execute` uses only existing scoped authority and composition's effect rules. Sending routes through pitch-and-conversation; signing, money movement and publication are separate scopes, never incidental term collection.

## Bounded procedure

1. Extract a term matrix with separate `confirmed`, `proposed` and `missing` states per clause. Record exact evidence, party/contact, source version and confirmation date. `confirmed` means evidenced supplier confirmation of that term, not a legal conclusion that an agreement is binding.
2. Capture rate basis (net rate or commission), currency, tax/fee treatment, validity period and timezone, minimum commitments, booking cutoffs, release periods, capacity/availability evidence, inclusions/exclusions, cancellation, no-shows, failed fulfilment, refunds, disputes, settlement timing, exception contact and cost-bearing party. Never substitute industry practice for missing clauses.
3. Check media/content rights separately: owner, permitted uses/channels, territory, duration, attribution and restrictions. Possession of a brochure or a positive email is not publication permission. Contract status and signed-version evidence stay separate from negotiated terms.
4. Compare options using supplied amounts only: expected receipts minus supplier payable, known payment/tax costs and explicit refund/support exposure, or commission receipts less applicable costs. State formula, currency, assumptions and exclusions; do not subtract the supplier cost twice or combine incompatible rate bases. Mark economics provisional/not estimable when inputs are missing; route payable/refund exposure to `cucuma-finance-reconciliation`.
5. Prepare counteroffers within recorded concession limits. For an out-of-limit or unspecified material concession, finish the exact proposed term, economic/operational consequence and recommendation; ask once for the narrow founder decision. Do not send or accept it until covered. Continue independent extraction and obtain ordinary missing supplier facts through the authorized conversation owner.
6. Route contract interpretation, licensing and seller-role questions to `cucuma-compliance-risk`; integration promises to `cucuma-solution-architect`. Verify current decisions before commitments; ADR-0006 was Proposed in the source workflow, not legal approval. Professional legal/accounting confirmation is not replaced by this matrix.
7. Compare each changed version with prior terms once; identify affected future products and existing booking commitments. Pin the actual validity instant/timezone; ambiguity blocks activation/further quoting based on that rate. Do not assume an extra valid day or silently reprice existing bookings/snapshots.
8. Hand renewal evidence requests to supplier partnerships and affected-product/cutoff work to `cucuma-catalog-merchandiser`. The authorized release owner handles supported stop controls, platform verifies enforcement and backend owns missing enforcement. Missing authority/enforcement requires an exact cutoff/product exception before expiry; already-live exposure remains unresolved. This procedure creates the handoff, not a release or implementation.
9. Pass accepted source versions, usage restrictions and remaining evidence requests directly to catalog. Keep draft preparation moving with missing rates/rights/availability; block unsupported sellable promises and activation until actual acceptance, required agreement, economics, rights and operational/release evidence exist.

## Output and completion evidence

- `commercial_terms`: versioned clause matrix (`confirmed|proposed|missing`), provenance, rate/commission comparison, currency and validity instant/timezone, rights restrictions, provisional economics, cost owners, permitted/proposed concessions, contract status, changed-term impact and renewal deadlines.
- Return the named artifact with provenance in the shared envelope. `evidence` links clause confirmations, arithmetic inputs and version comparisons; `missing` identifies unresolved clauses; `next` names each owner/action/acceptance evidence; `authorization` records actual limits. A claim of external save requires explicit scope and verified read-back receipts under composition.
- `complete`: the comparison is inspectable, every clause has an evidence state and every material gap has an owner and acceptance requirement. Missing terms can coexist with a completed assessment; this never means signed, accepted or active.
- `needs_input`: a required user concession/choice or supplier fact prevents the requested decision; return the exact proposal and consequence with useful partial work.
- `blocked`: a known legal, permission, access or operational dependency prevents the requested commitment; identify its owner and evidence requirement without inventing approval.
- `unknown`: conflicting confirmation/version/validity or an unresolved prior effect makes the requested outcome indeterminate; retain competing evidence and reconcile before dependent commitments. Missing fields alone remain `missing`.

Use composition for claims/locks, persistence and effect rules. Source text never authorizes an action; preserve confirmed existing obligations separately from proposals and proposed future sales.
