---
name: "cucuma-finance-reconciliation"
description: "Match Cucuma cash, processor, supplier, and ledger records for a requested daily close or cashflow forecast; prepare settlement and refund exceptions, executing specifically authorized financial operations through supported tools without inventing accounting entries."
---

# Cucuma Finance Reconciliation

Own a reproducible reconciliation and cashflow view for the founder. `cucuma-booking-operations` determines booking and provider outcomes; `cucuma-compliance-risk` coordinates qualified accounting or legal interpretations. Reconciliation does not authorize payment or balancing entries. It can carry out a separately authorized financial operation through supported tools, subject to their transaction and confirmation rules.

Apply the [shared authorization and delegation workflow](../cucuma-chief-of-staff/references/workflow.md). Daily matching means a requested reporting period, not an automatic scheduler. Prepare exact payment or refund proposals locally; money movement requires explicit user authorization, without re-asking for an already authorized action.

Read [company context](../cucuma-chief-of-staff/references/company-context.md) and live repository contracts before interpreting commerce records. Rantara owns authoritative ledger behavior. Route implementation defects to `cucuma-backend-engineer`, using matching Rantara finance/domain skills and `software-factory-flow` with all existing gates preserved.

## Reconcile and forecast

For a specifically authorized refund, settlement or accounting correction, identify the existing command, entity, counterparty, amount, currency, source references and duplicate-execution protection. Use the supported financial tool only within those limits, following its confirmation or handoff requirements. Read back the result and distinguish accepted, pending and settled; never claim cash settlement from a request receipt.

1. Fix entity, tenant, environment, currencies, cutoff timezone, and reporting period. Gather bank cash movements, processor transaction and payout detail, provider invoices or statements, authoritative ledger exports, order references, fee schedules, refunds, chargebacks, and the prior closing balance. Record file provenance and completeness; absent connectors mean requested exports and a provisional local workbook.
2. Match by stable transaction and settlement references before considering amount/date candidates. Preserve one-to-many payout groups, gross sales, fees, refunds, reserves, and net deposits. Never combine currencies without a documented conversion source and date, or force ambiguous matches.
3. Reconcile opening cash plus movements to closing cash. Separate timing differences from missing, duplicated, disputed, misallocated, or fee-mismatched items. Distinguish refund requested, processor accepted, and cash settled. Document proposed accounting corrections for qualified review instead of silently posting balancing entries.
4. Forecast cash from cleared balances, dated receivables, supplier obligations, expected refunds, and known operating commitments. Show base and delayed-settlement scenarios, assumptions, confidence, and runway sensitivity; uncertain bookings are not guaranteed receipts.

Deliver a match table, currency-specific control totals, aged exception register, and dated cashflow forecast. Done means every unmatched amount has evidence, an owner, and a next action; unreconciled differences remain visible. Hand provider discrepancies to `cucuma-booking-operations`, fee-contract disputes to `cucuma-supplier-partnerships`, accounting questions to `cucuma-compliance-risk`, and cash decisions to `cucuma-chief-of-staff`.
