# NanFengCheong Skills

Codex-optimized skills for planning, implementing, debugging, triage, architecture review, and concise collaboration.

[![skills.sh](https://skills.sh/b/NanFengCheong/skills)](https://skills.sh/NanFengCheong/skills)

## Install

### Via npx (any project, no Codex marketplace needed)

```bash
npx @nanfengcheong/skills link
```

This symlinks all skills to `~/.claude/skills` so they're available to Codex, opencode, and Claude CLI.

List available skills:

```bash
npx @nanfengcheong/skills list
```

### Via npx skills (Vercel ecosystem)

```bash
npx skills add NanFengCheong/skills
```

Install to specific agents:

```bash
npx skills add NanFengCheong/skills --all -y
```

Use a single skill without installing:

```bash
npx skills use NanFengCheong/skills@diagnose
```

### Via Codex marketplace

```bash
codex plugin marketplace add NanFengCheong/skills --ref main
codex plugin add nanfengcheong-skills@nanfengcheong-skills
```

Restart Codex or start a new session so the installed skills are loaded.

## Default Flow

Use this sequence for feature work and bug fixes:

1. `$grill-with-docs` -> capture intent, clarify scope, sharpen vocabulary, update `CONTEXT.md`/ADRs when useful.
2. `$to-prd` -> publish the agreed scope as a PRD.
3. `$to-implementation-plan` -> convert the PRD into executable slices, checks, and agent-team tracks.
4. `$execute-plan-using-agent-team` -> implement with lead, worker, and skeptic tracks, then verify.

## Setup Per Repo

Run `$setup-matt-pocock-skills` once in each repo that uses the engineering skills. It records:

- Issue tracker workflow.
- Triage label vocabulary.
- Domain doc layout.

The generated files live under `docs/agents/`.

## Skills

### Engineering

- **[diagnose](./skills/engineering/diagnose/SKILL.md)** - Disciplined diagnosis loop for hard bugs and performance regressions.
- **[execute-plan-using-agent-team](./skills/engineering/execute-plan-using-agent-team/SKILL.md)** - Execute an implementation plan with Codex agent-team tracks.
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** - Capture intent, challenge plans against the domain model, and update docs inline.
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** - Find deepening opportunities informed by `CONTEXT.md` and ADRs.
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** - Configure repo-local issue tracker, triage, and domain-doc context.
- **[tdd](./skills/engineering/tdd/SKILL.md)** - Test-driven development with red-green-refactor loops.
- **[to-implementation-plan](./skills/engineering/to-implementation-plan/SKILL.md)** - Turn a PRD into executable slices and verification gates.
- **[to-prd](./skills/engineering/to-prd/SKILL.md)** - Turn current context into a PRD and publish it to the issue tracker.
- **[triage](./skills/engineering/triage/SKILL.md)** - Move issues through canonical triage states.
- **[zoom-out](./skills/engineering/zoom-out/SKILL.md)** - Explain unfamiliar code in a broader system context.

### Productivity

- **[caveman](./skills/productivity/caveman/SKILL.md)** - Ultra-compressed communication mode.
- **[grill-me](./skills/productivity/grill-me/SKILL.md)** - Resolve a non-code plan or decision tree.
- **[handoff](./skills/productivity/handoff/SKILL.md)** - Write a continuation note for another agent/session.
- **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** - Create or update Codex skill files.

## Repo Layout

- `.agents/plugins/marketplace.json` - Codex marketplace entry.
- `plugins/nanfengcheong-skills/` - marketplace plugin wrapper.
- `.codex-plugin/plugin.json` - plugin manifest.
- `skills.sh.json` - grouping config for [skills.sh](https://skills.sh) directory.
- `skills/engineering/` - code-work skills.
- `skills/productivity/` - general workflow skills.

Each stable skill has an `agents/openai.yaml` file for Codex UI metadata.
