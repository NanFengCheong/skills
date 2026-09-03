# The 20 Cucuma roles

Invoke a role with its `$cucuma-...` skill name. The chief of staff selects and integrates specialists; it is one of the 20 roles. Each skill includes a distinct workflow and UI invocation metadata. These are reusable role instructions, not 20 scheduled processes or registered custom runtime agent types.

| # | Skill / role | Route here for | Expected output |
|---|---|---|---|
| 1 | [Chief of Staff](../../cucuma-chief-of-staff/SKILL.md) — `$cucuma-chief-of-staff` | Cross-functional priorities and accountable handoffs | One operating brief, decision queue and verified closure |
| 2 | [Product Manager](../../cucuma-product-manager/SKILL.md) — `$cucuma-product-manager` | Customer problems, scope and acceptance criteria | Prioritized brief and a testable engineering increment |
| 3 | [Supplier Partnerships](../../cucuma-supplier-partnerships/SKILL.md) — `$cucuma-supplier-partnerships` | Supplier discovery, onboarding and commercial readiness | Evidence-backed supplier dossier and contract questions |
| 4 | [Catalog & Merchandising](../../cucuma-catalog-merchandiser/SKILL.md) — `$cucuma-catalog-merchandiser` | Source normalization, product completeness and offer readiness | Traceable draft catalog with explicit publication gaps |
| 5 | [Growth Marketing](../../cucuma-growth-marketer/SKILL.md) — `$cucuma-growth-marketer` | Acquisition experiments, campaign economics and measurement | Capped experiment proposal with baseline and stop rule |
| 6 | [Sales & CRM](../../cucuma-sales-crm/SKILL.md) — `$cucuma-sales-crm` | Leads, corporate inquiries and proposal follow-up | Qualified pipeline, next actions and verified proposal drafts |
| 7 | [Content & SEO](../../cucuma-content-seo/SKILL.md) — `$cucuma-content-seo` | Editorial pages, organic discovery and campaign copy | Sourced content package with rights and factual checks |
| 8 | [Customer Support](../../cucuma-customer-support/SKILL.md) — `$cucuma-customer-support` | Customer case triage and response ownership | Case summary, response draft and confirmed resolution evidence |
| 9 | [Booking Operations](../../cucuma-booking-operations/SKILL.md) — `$cucuma-booking-operations` | Booking, fulfillment, cancellation and supplier exceptions | Reconciled outcome, safe next action and exception owner |
| 10 | [Finance & Reconciliation](../../cucuma-finance-reconciliation/SKILL.md) — `$cucuma-finance-reconciliation` | Order/gateway/bank/supplier matching and cash exceptions | Accountant-ready reconciliation and settlement proposal |
| 11 | [Compliance & Risk](../../cucuma-compliance-risk/SKILL.md) — `$cucuma-compliance-risk` | Scoped commercial, privacy and launch obligations | Evidence register and questions for qualified approvers |
| 12 | [Data Analyst](../../cucuma-data-analyst/SKILL.md) — `$cucuma-data-analyst` | Metric definitions, data quality and decision analysis | Reproducible analysis with confidence and limitations |
| 13 | [Solution Architect](../../cucuma-solution-architect/SKILL.md) — `$cucuma-solution-architect` | Cross-system design and accepted ADR boundaries | Decision record with concrete tradeoffs and proof plan |
| 14 | [Backend Engineer](../../cucuma-backend-engineer/SKILL.md) — `$cucuma-backend-engineer` | Rantara commands/Store API or owned Cucuma BFF changes | Minimal tested implementation in the correct workspace |
| 15 | [Web Engineer](../../cucuma-web-engineer/SKILL.md) — `$cucuma-web-engineer` | TanStack Start storefront and browser interaction | Accessible web change with browser verification |
| 16 | [Mobile Engineer](../../cucuma-mobile-engineer/SKILL.md) — `$cucuma-mobile-engineer` | Expo/native flows and device behavior | Native implementation with platform-specific evidence |
| 17 | [UX Designer](../../cucuma-ux-designer/SKILL.md) — `$cucuma-ux-designer` | Journey, interaction, content hierarchy and accessibility | Reviewable flow and shared semantic-state specification |
| 18 | [Quality Engineer](../../cucuma-quality-engineer/SKILL.md) — `$cucuma-quality-engineer` | Independent behavior, regression and adversarial verification | Reproducible failure or evidence-backed acceptance report |
| 19 | [Platform & Reliability](../../cucuma-platform-operator/SKILL.md) — `$cucuma-platform-operator` | Cloudflare environments, deployment, observability and incidents | Verified operational change or bounded incident diagnosis |
| 20 | [Security Engineer](../../cucuma-security-engineer/SKILL.md) — `$cucuma-security-engineer` | Threats, authorization, tenant isolation and data exposure | Scoped findings, exploit evidence and verified remediation |

## Resolve common overlaps

- **Chief of staff vs product manager:** chief owns company priorities and handoffs; product manager owns product scope and acceptance.
- **Supplier partnerships vs sales:** supplier develops supply-side relationships; sales develops buyer-side opportunities.
- **Growth vs content vs catalog:** growth selects an experiment; content writes assets; catalog establishes product facts and readiness.
- **Support vs booking operations vs finance:** support owns the customer case and reply; operations establishes fulfillment/provider outcomes; finance establishes money movement and reconciliation.
- **Compliance vs security:** compliance maps business obligations and professional approvals; security tests technical controls and exposure. Privacy changes often need both.
- **Analytics vs finance:** analytics defines metrics and tests business hypotheses; finance reconciles authoritative financial records and accounting exceptions.
- **Product vs UX vs architecture:** product defines the problem and success; UX defines the usable journey; architecture resolves structural tradeoffs.
- **Backend vs web vs mobile:** backend owns commerce/BFF logic in its proper repository; web and mobile own their platform's client behavior.
- **Quality vs platform:** quality verifies behavior against acceptance; platform establishes deployment identity, runtime health and operational evidence.

## Minimum teams for real requests

| Request | Accountable role | Add only if needed |
|---|---|---|
| Normalize another Malaysia.travel seed batch | Catalog | Supplier for terms; compliance for actual reuse questions |
| Diagnose a charged-but-unconfirmed booking | Booking operations | Finance, support, backend if a defect is supported |
| Improve an underperforming product page | Product manager | Analyst, UX, web; content for editorial work |
| Prepare a partner recruitment email | Supplier partnerships | Content or compliance for specific claims/terms |
| Ship an accepted API feature | Backend engineer | Quality and required factory reviewers; architecture for new boundaries |
| Review staging cost and readiness | Platform operator | Analyst for cost attribution; security for access/exposure |

Use the [shared workflow](workflow.md) for authority, ownership, evidence and execution. Automatic skill discovery remains enabled; open a new session if the host has not refreshed the installed skill catalogue. A skill can also be read explicitly from its linked path in the current session.
