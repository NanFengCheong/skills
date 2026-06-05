---
name: to-implementation-plan
description: Convert a PRD or agreed feature/bug-fix scope into an executable implementation plan with vertical slices, agent-team decomposition, verification gates, and risk notes. Use after `$to-prd`, or when the user asks to plan implementation before coding.
---

# To Implementation Plan

Turn a PRD into a concrete execution artifact. Do not write production code in this skill. The output is a plan file that `$execute-plan-using-agent-team` can execute.

## Inputs

Read, in this order:

1. The PRD issue, PRD file, or current conversation context.
2. `CONTEXT.md`, `CONTEXT-MAP.md`, and relevant ADRs.
3. Existing code paths, tests, scripts, package commands, and deployment notes in the touched area.

If the PRD is missing a decision needed to plan safely, ask one focused question. If the answer can be discovered from code or docs, discover it instead.

## Output Location

Write the plan to `docs/plans/YYYY-MM-DD-<slug>-implementation-plan.md`. Create `docs/plans/` if needed. Use the current local date for `YYYY-MM-DD`.

## Plan Rules

- Preserve PRD intent. Do not expand scope.
- Use vertical slices: each slice must produce observable behavior or a verifiable internal capability.
- Prefer existing interfaces and test seams. Add new seams only when the plan explains why existing ones are too shallow.
- Split agent work by disjoint write scopes where possible.
- Include one skepticism track for assumptions, edge cases, rollback risk, and missing tests.
- Keep steps executable without extra interviews unless a decision is genuinely blocked.

## Plan Template

```markdown
# <Title> Implementation Plan

## Source

- PRD: <issue URL or file path>
- Context docs: <paths>
- ADRs: <paths or "none found">

## Goal

<One paragraph outcome statement.>

## Non-Goals

- <Explicit exclusions from the PRD>

## Assumptions

- <Assumption> -> verify: <how execution will prove or disprove it>

## Slices

### Slice 1: <name>

- Scope: <behavior/capability>
- Files likely touched: <paths or modules>
- Tests: <test files/commands>
- Verify: <command or manual check>
- Agent role: <main | worker | skeptic>

## Agent Team

- Lead: owns sequencing, integration, and final verification.
- Worker A: <disjoint write scope>
- Worker B: <disjoint write scope>
- Skeptic: challenges assumptions, edge cases, data migration, auth/security, failure modes, and missing tests.

## Execution Order

1. <Step> -> verify: <check>
2. <Step> -> verify: <check>
3. <Step> -> verify: <check>

## Risks

- <Risk> -> mitigation: <action>

## Completion Criteria

- <User-visible behavior or bug fix proof>
- <Automated checks>
- <Docs/config/deploy notes if relevant>
```

## Finish

After writing the plan, tell the user the plan path and the next command: `$execute-plan-using-agent-team`.
