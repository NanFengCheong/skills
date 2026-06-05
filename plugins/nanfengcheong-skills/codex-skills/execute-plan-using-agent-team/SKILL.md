---
name: execute-plan-using-agent-team
description: Execute an implementation plan with a Codex agent team, including lead integration, bounded worker tracks, a skepticism track, and final verification. Use after `$to-implementation-plan`, or when the user asks to execute a plan with agents.
---

# Execute Plan Using Agent Team

Execute the plan end to end. Do not stop between steps unless blocked by a real dependency, an unsafe decision, or user-requested checkpoint.

## Start

1. Read the implementation plan.
2. Check `git status --short --branch`; preserve unrelated user changes.
3. Identify verification commands before editing.
4. Restate execution tracks briefly:
   - Lead: sequencing, integration, conflict resolution, final checks.
   - Workers: disjoint write scopes from the plan.
   - Skeptic: assumptions, edge cases, failure modes, missing tests, and rollout risk.

## Agent Team Rules

Use Codex subagents when the active runtime policy permits spawning agents for this user request. If subagents are unavailable, execute the same tracks locally and label the skeptic pass separately.

When spawning workers:

- Give each worker a bounded write scope and the relevant plan slice only.
- Avoid overlapping file ownership unless unavoidable.
- Ask each worker to edit files directly and report changed paths plus verification.
- Keep the skeptic read-only unless you explicitly assign a narrow fix.
- Continue useful lead work while workers run.

## Execution Loop

For each slice:

1. Re-read the slice and current files in scope.
2. Implement the smallest change that satisfies the slice.
3. Add or update tests at the seam named in the plan.
4. Run the slice verification.
5. Integrate worker output, resolving conflicts without reverting unrelated user work.
6. Run the skeptic pass for that slice; fix confirmed issues.

## Verification

Before finishing:

- Run every verification command listed in the plan that is feasible locally.
- Run focused checks for files you touched.
- Re-run any failing check after fixes.
- If a check cannot run, record the exact blocker and what remains unverified.
- Inspect `git diff --check`.
- Summarize changed files and behavioral proof.

## Finish

Report:

- Plan path executed.
- Slices completed.
- Tests/checks run and results.
- Any skipped checks with blockers.
- Remaining manual deploy or release steps, if any.
