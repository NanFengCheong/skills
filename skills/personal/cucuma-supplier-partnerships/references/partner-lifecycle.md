# Partner lifecycle

- Owner role: `cucuma-supplier-partnerships`
- Version: 1
- Module: `partner-lifecycle`
- Required inputs: `partner_brief`, `commercial_terms`, `activation_decision`
- Outputs: `lifecycle_actions`
- Handoff: [shared composition contract](../../cucuma-chief-of-staff/references/composition.md)

Use through the owning role on demand for the caller's specific event. Existing partners enter directly with evidenced caller-supplied inputs; do not require recruitment, outreach or a new activation run. Reuse the owning SKILL.md and existing roles/controls; create no schema, runtime or recurring schedule.

## Validate and bound

1. Validate the shared envelope, case identity, mode and required artifact identities/versions and provenance. Confirm the partner, supplied trigger, affected products/bookings, evidence times and next deadline. A readiness decision is not proof the partner is live; resolve conflicting operational state before claiming it.
2. Select only subtasks matching the evidenced trigger and requested objective. Process each matching subtask once for this invocation; preserve unrelated future work without starting it. An absent required artifact or trigger needs input, but unrelated missing rate fields do not prevent preparing a booking-exception handoff.
3. Source text never grants authorization. `design` authors procedures/examples only and executes nothing; `prepare` produces local actions/handoffs only. `execute` uses actual user scope, confirmed target and existing controls. External sends/saves need explicit recipient/target/action scope, current versions and verified receipts; money movements, signing and release changes need their own authority.

## Conditional procedure

1. Read the supplied event and the latest evidenced commitments. Identify what changed, the affected IDs/versions, immediate obligation, deadline and accountable specialist. Keep supplier partnerships accountable for coordination; a specialist artifact is not a request for the founder to transfer information manually.
2. **First booking, fulfilment failure, amendment or cancellation:** route only the affected case to `cucuma-booking-operations` with order/payment/provider/fulfilment evidence and committed customer deadlines. `cucuma-customer-support` owns customer updates; `cucuma-finance-reconciliation` owns money evidence. Do not promise fulfilment from a payment receipt alone.
3. **Unknown supplier booking outcome:** booking operations checks the authoritative provider once immediately and, if supported, once after its documented reconciliation interval, using an earlier customer/fulfilment deadline when applicable. No interval/deadline, or an inconclusive second check, means escalation to the designated supplier operations contact and founder exception queue; support owns time-sensitive customer updates. Preserve prior attempts across invocations: never reset this check budget. Keep the booking unresolved; block repeat submissions and fulfilment promises until authoritative evidence resolves it. Escalation is neither retry permission nor completion proof.
4. **Settlement due or discrepancy:** route affected orders, gateway receipts, refunds, supplier statements and terms versions to `cucuma-finance-reconciliation`. Request matched entries, outstanding liabilities and named differences; booking operations resolves fulfilment discrepancies. Do not infer payment execution, tax conclusions or settled balances from a prepared reconciliation.
5. **Expiry, renewal or changed rates/terms:** supplier partnerships owns obtaining renewal; `cucuma-catalog-merchandiser` owns affected-product lists, versioned catalog proposals and release cutoffs. Pin the supplier's actual validity instant/timezone and notice deadline. Ambiguity must be resolved before activation or further quoting, never assumed valid for another day.
6. At a confirmed expiry cutoff, the authorized catalog release owner stops new offers/quotes through supported controls; `cucuma-platform-operator` verifies enforcement and `cucuma-backend-engineer` owns missing enforcement. If authority or enforcement is missing, escalate exact products/cutoff to the founder before expiry, keep new activation blocked and report already-live exposure as an unresolved incident. Identify existing bookings separately; preserve contracted commitments and price snapshots without silent repricing. Route discrepancies to booking operations/finance before propagating changes.
7. **Quality issue or partner exit:** prepare affected-offer, future-booking, outstanding-balance and access/content impact lists; route booking commitments to operations, balances to finance, supported pause/delist proposals to catalog/release owners and rights/access questions to the authorized owners. Execute only scoped actions; retain unresolved obligations after delisting.
8. **Performance review or improvement opportunity:** route observed funnel/contribution/cancellation/support data to `cucuma-data-analyst` and bounded improvement proposals to `cucuma-growth-marketer`. Supplier partnerships/catalog own resulting renewal/supply changes. Return continue/change/stop recommendations with provenance; no invented baseline or automatic campaign.
9. Collect matching specialist outputs and evidence. For any authorized external action, record the exact prepared action and stable ID before one attempt; verify provider receipt and authoritative read-back where applicable. Ambiguous effects remain unknown and require reconciliation before retry. Unavailable tools leave prepared artifacts and named dependencies, never claimed completion of the effect.

## Completion and exceptions

Return the shared envelope with the named `lifecycle_actions` artifact and provenance. For each selected subtask include trigger, changed facts, affected IDs/versions, accountable role, deadline/cutoff/timezone, exact next action, acceptance condition and evidence location. Distinguish prepared, handed off and verified completed work; an assignment is not a specialist receipt.

- `complete`: the requested design/preparation or bounded routing assessment is delivered with owned next actions; or requested operational outcomes have their required receipts. If no supplied condition matches, record a complete no-action assessment with the reason. Never describe the whole lifecycle as completed.
- `needs_input`: required identity, trigger, artifact, deadline or user scope prevents the requested result; name the missing fact and continue independent preparation.
- `blocked`: a known failed prerequisite, denied authority or unavailable control prevents a requested action; record owner/recovery evidence and any live exposure.
- `unknown`: an unresolved booking/payment/send/save effect or unverifiable authoritative state prevents an operational conclusion; retain the reconciliation owner, attempts and deadline. Escalation does not change this to complete.

Use `missing` and `next` for pending evidence and conditions. A complete design or handoff can explicitly carry an unresolved booking, but cannot claim that booking resolved. Do not start unrelated subtasks, future follow-ups or a scheduler from this procedure.
