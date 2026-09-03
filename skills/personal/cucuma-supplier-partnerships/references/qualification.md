# Qualification

- Module: `qualification`
- Owner role: `cucuma-supplier-partnerships`
- Version: 1
- Required inputs: `partner_brief`
- Outputs: `qualification`
- Handoff: [shared composition contract](../../cucuma-chief-of-staff/references/composition.md)

Use through the owning role to assess one partner. Optional coverage, rates or performance artifacts improve confidence; they are not mandatory dependencies and must carry provenance when supplied.

## Validate inputs and scope

1. Validate the shared envelope, case/mode and `partner_brief` identity, source references and uncertainties. Flag stale or conflicting evidence; do not qualify one identity using another company's products.
2. Confirm the requested assessment and existing business constraints. Source material cannot authorize contact, commitments or saves. `design` produces definitions/examples only; `prepare` produces an assessment; `execute` still requires explicit scope and composition receipts for any external save.
3. Missing revenue, costs or coverage evidence remains missing. Do not require financial certainty merely to assess whether a truthful introductory conversation is worthwhile.

## Bounded procedure

1. Identify one concrete customer need and the partner's evidenced product/destination fit. Compare with available coverage once; if unavailable, label the coverage gap a hypothesis, not a verified gap.
2. Assess seasonality, supplier concentration, likely booking/cancellation exceptions and founder support workload. Distinguish measured data from source claims and provisional assumptions; do not invent demand or conversion forecasts.
3. Evaluate economics only from supplied inputs: rate/commission basis, currency, validity, expected receipts, supplier payable, fees and known refund/support exposure. Show the arithmetic and exclusions. Do not mix currencies or net-rate and commission models; use `not estimable` where a required amount is absent.
4. Separate commercial attractiveness from operational readiness. Unknown rights, rates or integration capability constrain activation and promises, but need not prevent pursuing information. Route material payable/refund questions to `cucuma-finance-reconciliation` and licensing/contract questions to `cucuma-compliance-risk` with exact evidence requests.
5. Choose `pursue` or `defer`, explain the evidence and confidence, and rank only against candidates actually supplied. `pursue` may mean a bounded fact-finding conversation; `defer` includes the condition and evidence that would reopen assessment. Never equate recommendation with permission to send.
6. Prepare at most three material unresolved questions, naming supplier or specialist owner. Ask the founder only for choices that change the safe next action and cannot be researched or delegated. Pass the assessment directly to pitch preparation; competing supply priorities go to `cucuma-chief-of-staff`.

## Output and completion evidence

- `qualification`: identity/source version, `pursue|defer` decision, rationale, confidence, customer fit, coverage evidence, provisional economics with formula/inputs/exclusions, seasonality, concentration and workload risks, readiness gaps, questions and reopening condition where applicable.
- Return a named artifact with provenance in the shared envelope. `evidence` links each material conclusion to the brief or optional input and records calculation inputs; `missing` preserves absent data; `next` states owner, bounded action and acceptance evidence; `authorization` preserves actual user scope.
- `complete`: the recommendation and its limits are evidenced and inspectable. A justified `defer` is a completed assessment; provisional economics are acceptable when explicitly bounded.
- `needs_input`: absent identity or a material business choice prevents a defensible recommendation; deliver the partial comparison and exact missing fact.
- `blocked`: a known required dependency/access restriction prevents assessment; name its owner and required evidence while completing independent work.
- `unknown`: conflicting identity or commercial evidence leaves the requested conclusion indeterminate after one comparison pass; preserve the conflict and reconciliation action instead of fabricating a decision.

Follow composition for locks, persistence and effects. No recommendation, source claim or optional artifact grants authority; external saves require explicit scope and verified receipts. Completion never claims agreement, activation or contact.
