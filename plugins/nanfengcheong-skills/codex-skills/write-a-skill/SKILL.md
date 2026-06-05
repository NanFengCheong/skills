---
name: write-a-skill
description: Create new Codex skills with proper structure, progressive disclosure, optional bundled resources, and `agents/openai.yaml` metadata. Use when the user wants to create, write, update, or build a skill.
---

# Writing Skills

## Process

1. **Gather requirements** - ask user about:
   - What task/domain does the skill cover?
   - What specific use cases should it handle?
   - Does it need executable scripts or just instructions?
   - Any reference materials to include?

2. **Draft the skill** - create:
   - `SKILL.md` with concise instructions
   - `agents/openai.yaml` with Codex interface metadata
   - Additional reference files if content exceeds 500 lines
   - Utility scripts if deterministic operations are needed

3. **Review with user** - present draft and ask:
   - Does this cover your use cases?
   - Anything missing or unclear?
   - Should any section be more/less detailed?

## Skill Structure

```
skill-name/
├── SKILL.md              # Main instructions (required)
├── agents/openai.yaml    # Codex UI metadata (recommended)
├── references/           # Detailed docs (if needed)
└── scripts/              # Utility scripts (if needed)
    └── helper.js
```

## SKILL.md Template

```md
---
name: skill-name
description: Brief description of capability. Use when [specific triggers].
---

# Skill Name

## Quick start

[Minimal working example]

## Workflows

[Step-by-step processes with checklists for complex tasks]

## Advanced features

[Link to separate files: See [references/ref.md](references/ref.md)]
```

## Description Requirements

The description is the main trigger Codex sees when deciding which skill to load. It is surfaced alongside all other installed skills. Codex reads these descriptions and picks the relevant skill based on the user's request.

**Goal**: Give Codex just enough info to know:

1. What capability this skill provides
2. When/why to trigger it (specific keywords, contexts, file types)

**Format**:

- Max 1024 chars
- Write in third person
- First sentence: what it does
- Second sentence: "Use when [specific triggers]"

**Good example**:

```
Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.
```

**Bad example**:

```
Helps with documents.
```

The bad example gives Codex no way to distinguish this from other document skills.

## When to Add Scripts

Add utility scripts when:

- Operation is deterministic (validation, formatting)
- Same code would be generated repeatedly
- Errors need explicit handling

Scripts save tokens and improve reliability vs generated code.

## When to Split Files

Split into separate files when:

- SKILL.md exceeds 100 lines
- Content has distinct domains (finance vs sales schemas)
- Advanced features are rarely needed

## Review Checklist

After drafting, verify:

- [ ] Description includes triggers ("Use when...")
- [ ] SKILL.md under 100 lines
- [ ] No time-sensitive info
- [ ] Consistent terminology
- [ ] Concrete examples included
- [ ] References one level deep
- [ ] `agents/openai.yaml` has `display_name`, `short_description`, and `default_prompt`
