---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up. Use when the user asks for a handoff, session summary, continuation note, or context package for a future Codex session.
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user gives a focus for the next session, tailor the doc accordingly.
