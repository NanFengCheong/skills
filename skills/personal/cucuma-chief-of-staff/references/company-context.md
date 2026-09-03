# Company context

This skill suite supports Cucuma's solo founder across business operations and Rantara development. It is an operating aid, not a set of employees, always-running processes, business licences or connected SaaS accounts. Recheck live sources before acting.

## Workspaces and authority

| Area | Default workspace / evidence | Owner |
|---|---|---|
| Branded storefront, BFF, Expo app, customer UI | [/Users/nanfengcheong/Projects/cucuma](/Users/nanfengcheong/Projects/cucuma), its README and implementation docs | Cucuma |
| Commerce backend, Store API, SDK, orders and finance | [/Users/nanfengcheong/Projects/rantara](/Users/nanfengcheong/Projects/rantara), AGENTS.md, CONTEXT.md, phase docs and accepted ADRs | Rantara |
| Engineering procedure | [Rantara software factory](/Users/nanfengcheong/Projects/rantara/.agents/skills/software-factory-flow/SKILL.md) and the target workspace's current rules | Engineering lead |
| Customer-delivery boundary | [ADR-0021](/Users/nanfengcheong/Projects/rantara/docs/architecture/adr/0021-cucuma-customer-delivery-and-rantara-store-api-boundary.md) | Accepted at inspection |
| Merchant/package-seller operating role | [ADR-0006](/Users/nanfengcheong/Projects/rantara/docs/architecture/adr/0006-cucuma-merchant-package-seller-role.md) | Proposed at inspection; requires scoped professional approvals |

Paths are defaults, not authority to edit arbitrary files. Use the actual selected workspace, inspect its rules and dirty state, and preserve concurrent work. If the workspace moved, locate its replacement before proceeding.

Rantara owns D1-authoritative commerce and public Store API/SDK contracts. Cucuma owns its TanStack Start storefront, separate Customer BFF, React Native/Expo app, HeroUI platform renderers and shared semantic customer UI. Clients call the Cucuma BFF; the BFF calls Rantara through the Store SDK. Neither client nor BFF invents price, availability, payment or booking success. Load the relevant existing Rantara domain skill rather than recreating it inside a role skill.

## Cucuma objectives

Cucuma (`cucuma.my`, short for “Cuti-Cuti Malaysia”) is the Malaysia-first customer and industry destination-commerce network built on Rantara. Product and business decisions optimize for:

- simple, premium, mobile-first booking of Malaysian attractions, tours, transport, stays, travel passes and bundles;
- local supplier onboarding that starts with controlled manual or CSV workflows and request-to-book, then adds one proven connector at a time;
- state or segment pilots through Tourism Malaysia, state tourism bodies, TM Networking, associations and licensed operators, with a default first proof bounded to one state, one segment, about 20 suppliers, three example bundles and 90 days;
- direct merchant/package-seller economics only after ADR-0006 launch gates close; until then use an explicit licensed seller or operating partner and preserve contracting, payment, fiscal-document, refund and fulfilment ownership;
- official tourism data, events and media as permissioned discovery, content, campaign and merchandising inputs, never live inventory truth or assumed publication rights;
- grant and incentive programmes for eligible market activation, supplier recruitment, promotion and measurable campaign evidence, without treating core platform development as eligible unless the programme explicitly permits it;
- public-sector and industry white-label or procurement opportunities while Rantara remains generic and Cucuma-specific behavior stays in the customer composition; and
- success measured by sellable supply, conversion, fulfilled orders, refund and reconciliation performance, supplier economics, repeat customers and campaign impact rather than feature count.

The current commercial priority is to validate Malaysian demand with domestic attractions, day tours and practical bundles, secure a licensed operating route, recruit suppliers and prepare one bookable state-level pilot before broad national marketplace expansion. Source: [Tourism Malaysia opportunity assessment](https://chatgpt.com/share/6a98d0b7-de34-83ec-9067-e351b766ef00), reviewed 3 September 2026.

## Operational baseline, inspected 3 September 2026

The Cloudflare account named Cheongnanfeng@gmail.com's Account has account ID `ce90920ba9d910fcad13943cf0c062fb`. The staging database `cucuma-rantara-staging`, ID `da127fd5-3815-4371-bddb-c6e15da470bd`, contains tenant `cucuma`, nine migrations and 16 Malaysia.travel source drafts. [Seed evidence](/Users/nanfengcheong/Projects/rantara/data/seeds/cucuma/staging-seed-receipt.json) and [database operations configuration](/Users/nanfengcheong/Projects/rantara/data/seeds/cucuma/wrangler.staging.jsonc) record that work.

This is a dated baseline, not a promise of present state: reverify account, binding, environment and affected rows before mutations. At seeding, no API Worker was deployed by that task; drafts were not published, images had no verified publication rights, and advertised FROM prices were not executable offers. Do not promote these facts into launch or supplier-contract evidence.

The founder has not supplied a permanent spending allowance, external-message authorization, legal-entity profile, settled launch date or standing production-release permission through this suite. Existing authorization in each actual session still applies. Missing information blocks only the action that needs it; research, review and draft preparation can continue.

## Source systems

Prefer the user's existing connected CRM, support inbox, supplier portal, accounting system and monitoring tools when present. Discover callable tools before claiming access. No installation is required to use these skills locally. A missing connector means a local artifact and an explicit connection requirement, not a fabricated live update.

Keep customer documents, credentials, raw payment data and sensitive supplier records in their appropriate restricted systems. Repository work items contain minimized case references and evidence links, not copied secrets or unnecessary personal data.
