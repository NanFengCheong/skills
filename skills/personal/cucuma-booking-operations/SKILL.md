---
name: "cucuma-booking-operations"
description: "Investigate Cucuma fulfillment, cancellation or unknown-provider outcomes and execute authorized safe recovery; customer correspondence belongs to support and cash matching to finance reconciliation."
---

# Cucuma Booking Operations

Own the operational evidence and recovery recommendation for booking exceptions. `cucuma-customer-support` owns customer reply drafts; `cucuma-supplier-partnerships` owns supplier commercial relationships. Neither a pending UI label nor captured payment establishes fulfillment.

Use the [shared authorization and delegation workflow](../cucuma-chief-of-staff/references/workflow.md). Operate on demand, continuing read-only investigation and local recovery drafts. Prepare exact provider messages or refund requests before seeking any missing explicit authorization; existing scoped authorization carries through.

Read [company context](../cucuma-chief-of-staff/references/company-context.md), current repository contracts, and applicable Rantara domain skills. Engineering repairs belong to `cucuma-backend-engineer`, loading matching domain skills and `software-factory-flow` with its gates intact; do not duplicate command or reconciliation internals here.

## Resolve the uncertainty

If the user requested recovery and its exact operation is authorized, execute through the existing command/provider path after establishing the applicable outcome and retry contract. Keep cancellation, replacement and refund identities distinct; verify each persisted result. A recovery request is not complete at the recommendation stage.

1. Collect tenant/environment, redacted order and provider references, accepted quote and cancellation terms, travel deadlines with timezone, command/idempotency identifiers, and timestamped request, response, webhook, and reconciliation evidence. Distinguish staging data from live transaction records.
2. Build an event timeline separating local authority, provider observation, payment, and fulfillment. Classify each outcome as confirmed success, confirmed failure, or unknown. A timeout, missing webhook, or payment reversal does not prove provider cancellation.
3. For unknown outcomes, prefer an authorized read-only status lookup or existing reconciliation path. Do not submit a new booking, issue a replacement, or retry cancellation merely because the first response was lost. Recommend a retry only after checking the provider contract, existing operation identity, idempotency guarantees, and authoritative state; otherwise retain the unknown state and escalate.
4. For confirmed cancellation eligibility, calculate the proposed operational sequence from accepted terms and provider evidence, keeping provider cancellation and customer refund as separate outcomes. Name the executor, required authorization, and success evidence for each step.

Deliver an exception packet with timeline, state classification, exact next action, duplicate-effect risk, deadline, and owner. Done means resolution is evidenced or uncertainty remains explicitly assigned. Hand customer updates to `cucuma-customer-support`, financial discrepancies to `cucuma-finance-reconciliation`, supplier escalation drafts to `cucuma-supplier-partnerships`, and unresolved priorities to `cucuma-chief-of-staff`. Missing connectors mean an evidence packet, never a claimed recovery.
