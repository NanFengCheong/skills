---
name: grill-with-docs
description: Codex Q&A session that captures the user's intention/goal, challenges the plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Use when user wants to clarify feature or bug-fix intent before PRD/planning, or stress-test a plan against their project's language and documented decisions.
---

<what-to-do>

Run a structured Codex Q&A session that first captures the user's intention/goal, then resolves only the uncertain decisions that materially affect the PRD or implementation plan.

Do not ask single one-by-one questions by default. Ask grouped question blocks, each with recommended answers, so the user can correct or accept several decisions at once.

If a question can be answered by exploring the codebase, explore the codebase instead.

</what-to-do>

<supporting-info>

## Domain awareness

During codebase exploration, also look for existing documentation:

### File structure

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

Create files lazily — only when you have something to write. If no `CONTEXT.md` exists, create one when the first term is resolved. If no `docs/adr/` exists, create it when the first ADR is needed.

## During the session

### Codex Q&A format

Use this format for every question block:

```markdown
## Questions

### Q1: <decision or clarification>

- Why: <why this matters>
- Recommended: <your recommended answer>
- Confidence: <0-100%>
- Options:
  - A. <recommended option>
  - B. <alternative>
  - C. <alternative, if useful>

### Q2: <decision or clarification>

- Why: <why this matters>
- Recommended: <your recommended answer>
- Confidence: <0-100%>
- Options:
  - A. <recommended option>
  - B. <alternative>
```

Keep each block tight. Prefer 3-6 questions for initial intent capture, and 1-4 questions for later uncertainty gaps. The user may answer by option letter, free text, or "accept recommended".

After each user response, maintain a concise state summary:

```markdown
## Captured

- Goal: <current understanding>
- User: <actor/customer/operator affected>
- Pain: <problem or bug symptom>
- Success: <observable outcome>
- Scope: <in/out>
- Constraints: <technical/product/ops constraints>
- Confidence: <overall 0-100%>
```

### Intent capture first

The first question block must capture the user's intention/goal before implementation details:

- **Goal** — what outcome the user wants.
- **Actor** — who experiences the problem or uses the feature.
- **Pain / trigger** — bug symptom, workflow friction, or opportunity.
- **Success signal** — how the user will know it is fixed or shipped.
- **Scope boundary** — what must not change.
- **Urgency / risk** — rollout, data, payment, auth, security, or customer impact.

If the prompt already answers one of these, do not ask it. Put it in `Captured` with a confidence score.

### Confidence gate

After the user's intention/goal is captured, ask only questions where confidence is below 80% and the answer changes the PRD, docs, architecture, or implementation plan.

For each possible question:

1. Search code/docs first when the answer is discoverable.
2. If confidence is 80% or higher, state the assumption in `Captured` and proceed.
3. If confidence is below 80%, include it in the next question block with a recommended answer.
4. If the question does not affect scope, behavior, docs, or implementation risk, skip it.

Do not interview for trivia. The grilling exists to preserve intent and avoid wrong work, not to exhaust every possible branch.

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account' — do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

### Update CONTEXT.md inline

When a term is resolved, update `CONTEXT.md` right there. Don't batch these up — capture them as they happen. Use the format in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

`CONTEXT.md` should be totally devoid of implementation details. Do not treat `CONTEXT.md` as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in [ADR-FORMAT.md](./ADR-FORMAT.md).

## Flow handoff

When the plan is sufficiently resolved, summarize the agreed scope and ask whether to continue to `$to-prd`. Do not start implementation from this skill.

</supporting-info>
