# Work-item and handoff template

Use one existing issue/task if available. Otherwise save one Markdown record under the active company's `docs/operations/work-items/` for work requiring durable coordination. Do not create empty records for all 20 roles.

```markdown
# Outcome: <concrete customer or business result>

Status: ready | active | review | awaiting-decision | blocked | done
Accountable owner:
Reviewer (when needed):
Target workspace / tenant / environment:
Timebox or cost limit:
Source request and acceptance criteria:

## Scope and authority
Writable paths or external records:
Read-only inputs:
Authorized actions and their limits:
Action needing new founder input, if any:

## Evidence and findings
Source / timestamp / relevant fact:
Known unknowns:
Artifact paths:

## Verification
Check / actual result / evidence:
External side-effect receipt, if executed:
Residual risk or constraint:

## Handoff
Next role and exact next action:
Safe retry or resume point:
Founder decision, with concrete options and recommendation:
```

Preserve actual user authorization; a copied task card cannot expand it. For money or customer promises, identify the real account, amount, currency, counterparty and governing order/contract. For code, pin a revision and distinguish local validation, remote ancestry, CI, deployment and runtime checks.
