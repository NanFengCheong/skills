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
   - Skeptic: assumptions, edge cases, adversarial break hypotheses, missing tests, and rollout risk.

## Agent Team Rules

Use Codex subagents when the active runtime policy permits spawning agents for this user request. If subagents are unavailable, execute the same tracks locally and label the skeptic pass separately.

When spawning workers:

- Give each worker a bounded write scope and the relevant plan slice only.
- Avoid overlapping file ownership unless unavoidable.
- Ask each worker to edit files directly and report changed paths plus verification.
- Keep the skeptic read-only unless you explicitly assign a narrow fix.
- Ask the skeptic to save adversarial break hypotheses to the plan's hypothesis file before TDD starts.
- Continue useful lead work while workers run.

## Execution Loop

For each slice:

1. Re-read the slice and current files in scope.
2. Generate or update adversarial hypotheses for how this slice could break while happy-path tests pass.
3. Add or update one failing test at the seam named in the plan.
4. Implement the smallest change that satisfies that test.
5. Repeat red-green for selected adversarial hypotheses, highest risk first.
6. Run the slice verification.
7. Integrate worker output, resolving conflicts without reverting unrelated user work.
8. Run the skeptic pass for that slice; fix confirmed issues.

## Verification

Before finishing:

- Run every verification command listed in the plan that is feasible locally.
- Run focused checks for files you touched.
- Re-run any failing check after fixes.
- Confirm tested adversarial hypotheses are marked in the hypothesis file, with deferrals explained.
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
