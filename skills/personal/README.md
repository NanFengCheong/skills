# Personal skills

These skills are tied to the owner's Cucuma setup. They are intentionally excluded from the top-level skill catalog and plugin manifest.

## Cucuma

Twenty role entry points compose seven independent step modules through six recipes. Start with the [composition contract](cucuma-chief-of-staff/references/composition.md), [recipes](cucuma-chief-of-staff/references/recipes.json), or the [role roster](cucuma-chief-of-staff/references/roles.md). Each module declares its inputs, outputs, owner and revision; existing artifacts can enter a workflow at any step.

- [cucuma-backend-engineer](cucuma-backend-engineer/SKILL.md) — Build authoritative commerce and BFF behavior.
- [cucuma-booking-operations](cucuma-booking-operations/SKILL.md) — Resolve booking exceptions without duplicate effects.
- [cucuma-catalog-merchandiser](cucuma-catalog-merchandiser/SKILL.md) — Normalize catalog drafts and sellability evidence.
- [cucuma-chief-of-staff](cucuma-chief-of-staff/SKILL.md) — Coordinate business and engineering specialists.
- [cucuma-compliance-risk](cucuma-compliance-risk/SKILL.md) — Prepare bounded launch, privacy, and contract evidence.
- [cucuma-content-seo](cucuma-content-seo/SKILL.md) — Source editorial drafts and truthful search content.
- [cucuma-customer-support](cucuma-customer-support/SKILL.md) — Triage cases and draft careful customer replies.
- [cucuma-data-analyst](cucuma-data-analyst/SKILL.md) — Define metrics and explain conversion evidence.
- [cucuma-finance-reconciliation](cucuma-finance-reconciliation/SKILL.md) — Match settlements, refunds, fees, and cash forecasts.
- [cucuma-growth-marketer](cucuma-growth-marketer/SKILL.md) — Design growth experiments and budget proposals.
- [cucuma-mobile-engineer](cucuma-mobile-engineer/SKILL.md) — Build native journeys with device recovery proof.
- [cucuma-platform-operator](cucuma-platform-operator/SKILL.md) — Plan safe Cloudflare rollouts and diagnose incidents.
- [cucuma-product-manager](cucuma-product-manager/SKILL.md) — Prioritize customer problems and acceptance.
- [cucuma-quality-engineer](cucuma-quality-engineer/SKILL.md) — Verify acceptance and adversarial behavior independently.
- [cucuma-sales-crm](cucuma-sales-crm/SKILL.md) — Qualify leads and draft proposals and follow-ups.
- [cucuma-security-engineer](cucuma-security-engineer/SKILL.md) — Review threats, tenant isolation, secrets, and privacy.
- [cucuma-solution-architect](cucuma-solution-architect/SKILL.md) — Resolve authority and delivery boundary decisions.
- [cucuma-supplier-partnerships](cucuma-supplier-partnerships/SKILL.md) — Onboard partners from websites, brochures or cards.
- [cucuma-ux-designer](cucuma-ux-designer/SKILL.md) — Design accessible web and native customer journeys.
- [cucuma-web-engineer](cucuma-web-engineer/SKILL.md) — Build TanStack storefront journeys and recovery.

Run from the repository root:

```sh
python3 skills/personal/cucuma-chief-of-staff/scripts/validate_composition.py
```

Behavioral review cases live in [composition-scenarios.json](cucuma-chief-of-staff/references/composition-scenarios.json). Skills and recipes define work; they do not create running agents or activate automations. Design, prepare and execute scopes are distinct. Local workspace/account references are personal defaults to verify before operational use. No credentials, partner cases or automation configuration are distributed here.
