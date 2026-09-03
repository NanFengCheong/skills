# Cucuma solo-founder operating workflow

Use these 20 roles on demand. The chief of staff coordinates; the founder remains accountable for business choices. Skills are available instructions, not active services or scheduled workers. No automations, SaaS subscriptions, agent credentials or outbound communications are created by this workflow.

[Role roster](roles.md) · [Company context](company-context.md) · [Work-item template](work-item.md)

For proactive workflow design, apply [five steps ahead](five-steps-ahead.md). A request to create skills/workflows ends with validated instructions and artifacts; do not require a real partner, connected sender, deployed API or active scheduler to complete that design. Define integration contracts and unresolved deployment dependencies without activating them.

## Start with an outcome

Examples:

- `Use $cucuma-chief-of-staff to prepare today's operating brief from available evidence and finish the highest-priority authorized task.`
- `Use $cucuma-supplier-partnerships to prepare onboarding for three Langkawi operators; keep outreach as drafts.`
- `Use $cucuma-supplier-partnerships to onboard this partner: <website, brochure, name card or company name>. Handle pitching, follow-ups and product drafts using my authorized sender and commercial limits.`
- `Use $cucuma-booking-operations to investigate booking <case ID>, establish the provider outcome and prepare the next safe action.`
- `Use $cucuma-product-manager to turn the verified checkout problem into one acceptance-tested engineering increment.`
- `Use $cucuma-platform-operator to inspect Cucuma staging readiness against the recorded deployment and seed evidence.`

Select one accountable role. Add a reviewer or dependency owner only when it changes the result. A content edit should not call all 20 roles; a customer incident may need support, operations, finance and an engineer.

## Work loop

For module-based work, use the [composition contract](composition.md) and [recipes](recipes.json) to select the smallest sequence, pass named artifacts and resume from existing evidence. The lifecycle below coordinates work; it does not require every module or every role on each request.

| Stage | Required outcome | Who acts |
|---|---|---|
| Intake | Concrete outcome, current evidence, target and acceptance check; recover prior authorization | Chief of staff or direct specialist |
| Scope | Exact writable files/records, independent units, estimate, decision limits | Accountable owner |
| Execute | Reusable artifact or authorized change, with progress against the estimate | Owner and bounded specialists |
| Review | Independent evidence check proportional to risk; required repository gates retained | Reviewer / engineering lead |
| Decision when needed | Exact ready-to-execute item and the specific missing authorization or fact | Founder |
| Execute authorized action | Perform the named action once with its intended identity and limits | Authorized operator |
| Verify and close | Read-back or runtime receipt supports each completion claim; record next owner for unresolved work | Owner, integrated by chief of staff |

A decision is a step only when required, not a default approval ceremony. If the user already authorized the exact action, finish it and verify it. Continue safe independent work while awaiting a necessary answer. Do not mark a customer case resolved merely because a draft reply exists.

Use one active business objective and one engineering increment by default. Start at most four parallel specialists; six active specialist workers in total, including nested workers, is the hard ceiling unless runtime capacity is lower. Include nested workers in the count. Divide writes by file or external-record ownership. Only the lead integrates shared files, runs shared verification gates and carries an authorized release forward. Stop completed workers rather than leaving them idle. Serial execution is acceptable for dependent work or when native delegation is unavailable.

Estimate the work and compare elapsed time at meaningful checkpoints. If over budget, change the approach, reduce nonessential work or split independent work. Do not repeat unchanged tests, searches or polling. Use a single shared brief instead of 20 status reports.

## Authority that preserves founder time

| Action | Default handling |
|---|---|
| Read, research, inspect code, analyze supplied records, draft copy, make reversible local files | Proceed within the user's scope |
| Existing authorized mutation | Execute within its account, target, amount, environment and other limits; verify without asking again |
| Send email, WhatsApp, sales outreach or support replies to another person | Require explicit user authorization covering the communication; otherwise prepare the exact draft and recipient |
| Buy ads, incur a new subscription, issue refunds, transfer money, settle suppliers, sign contracts or submit official filings | Prepare exact destination, amount, terms and evidence; execute only when specifically authorized and supported by tool policy |
| Publish a product/campaign, change live customer promises, expose services, create persistent access | Establish current source/rights/target and applicable authorization; do not treat skill installation as permission |
| Deploy or change a database | Follow the target repository's gates and the session's explicit or implied task authorization; pin the account/environment and verify persisted/runtime results |
| Commit code | In Rantara, only when explicitly asked; no force or amend |
| Missing tool or permission | Complete reviewable local work; identify the specific missing capability without claiming a live action |

Tool-specific confirmation rules still apply. A role never grants itself authority, approves its own sensitive change, bypasses a failed gate or expands access to fix an access failure. Founder approval does not substitute for required professional signoff on legal, tax or regulated business obligations.

## Business workflows

For source-led partner onboarding, use [partner autopilot](../../cucuma-supplier-partnerships/references/partner-autopilot.md). It owns the complete case, records next actions and resumes through the configured scheduler. The cadence below remains a separate suggested company review routine; it does not determine whether partner follow-ups are scheduled. Check actual automation state before reporting background coverage.

| Trigger | Sequence and ownership | Completion evidence |
|---|---|---|
| New supplier / destination | Supplier partnerships → compliance for actual contract/licensing questions → catalog → finance for economics → quality for sellability checks | Verified supplier facts, scoped terms, sourced drafts and approved offer/release conditions; public listing alone is insufficient |
| Campaign | Growth defines audience, hypothesis and capped proposal → data analyst baseline → content creates assets → catalog confirms current offers → authorized publisher | Saved/published asset receipt as applicable, spend limit if authorized, tagged measurement and a dated review |
| Lead / corporate inquiry | Sales CRM qualifies need and dates → supplier/catalog verify supply → finance checks quote assumptions → authorized proposal → operations on accepted booking | CRM state and exact proposal/acceptance evidence; an inquiry is not confirmed inventory |
| Support / booking exception | Customer support owns case → booking operations compares Rantara and supplier evidence → finance handles money discrepancies → engineer only if system behavior is implicated | Confirmed outcome or explicit unknown state, safe next action, and communication/refund receipts only if executed |
| Daily cash exceptions | Finance matches orders, gateway transactions, bank entries and supplier statements → operations for delivery disputes → founder for uncovered settlements | Reconciliation with amounts/currencies, unmatched items, owners and actual settlement proof |
| Incident | Platform or security contains within authorization → backend/client owner diagnoses → quality verifies recovery → support drafts affected-customer communication | Timeline, affected scope, deployed fix identity when relevant, runtime recovery and named follow-ups |
| Feature | Product manager → UX and architecture only when needed → backend/web/mobile in dependency waves → quality/security as applicable → platform for authorized release | Accepted criteria, repository gates, separate reviews, deployment/read-back evidence appropriate to the claim |

## Engineering uses the existing factory

The role suite does not replace repository instructions. For Rantara features and fixes, load `software-factory-flow` and the affected domain skills. Preserve spec pin/manifest → expected RED → minimal implementation → required verification → separate Standards, Spec and Global-invariants reviews → fixes/retests → test-generated evidence and process feedback. Keep required checks in their documented order; a failed gate prevents release. Reviewers receive the fixed diff, spec and relevant raw evidence, not a request to endorse the author's conclusion.

For Cucuma work, inspect its own current scripts and implementation requirements. Preserve the accepted clients → BFF → Store SDK/API boundary. Mobile browser checks are not native-device proof. Passing a build is not deployment proof; successful deployment is not persisted-data or end-to-end booking proof.

## Suggested founder cadence

This is a runbook, not a configured schedule. Invoke it manually or explicitly request an automation later.

| Cadence | Run only if relevant data is available | Founder receives |
|---|---|---|
| Start of working day, target 10–15 minutes | Support urgency, booking exceptions, payment/reconciliation gaps, service health and the top business objective | One brief: verified exceptions, today's owner, no more than three decisions |
| End of working day, target 5 minutes | What completed, what changed externally, unresolved customer/money exposure, tomorrow's next action | Evidence links and a resumable queue |
| Weekly, target 30–45 minutes | Growth funnel, contribution margin, supplier readiness, aged cases, cash outlook, product progress and operating cost | Continue/stop/change proposals supported by data |
| Monthly, timed to actual obligations | Accountant-ready reconciliation, approved compliance obligations, permissions review and recovery evidence | Exceptions and scoped professional/owner decisions |

In early-stage operation, unavailable bookings, sales or accounting data are reported as unavailable. Do not invent zero revenue, a healthy service, conversion gains or resolved cases. Use readiness work until real operating records exist.

## Founder brief format

1. **Outcome:** what finished, with source or verification receipt.
2. **Exceptions:** customer, money, security or delivery issues needing attention.
3. **Decisions:** at most three concrete items, recommendation, deadline and consequence; omit if none.
4. **Next action:** accountable role and the next bounded step.

The next step stays with an accountable owner. A closed artifact is not a closed business outcome when a requested external action remains unexecuted.
