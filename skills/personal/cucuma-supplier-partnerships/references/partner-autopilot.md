# Partner workflow recipes

This is the routing map, not the procedure for every stage. Use the [composition contract](../../cucuma-chief-of-staff/references/composition.md) and select a recipe from [the registry](../../cucuma-chief-of-staff/references/recipes.json). Each linked module can run independently with supplied inputs.

| Module | Owner | Produces |
|---|---|---|
| [Source intake](source-intake.md) | Supplier partnerships | partner_brief, product_candidates |
| [Qualification](qualification.md) | Supplier partnerships | qualification |
| [Pitch and conversation](pitch-and-conversation.md) | Supplier partnerships | conversation |
| [Commercial terms](commercial-terms.md) | Supplier partnerships | commercial_terms |
| [Product setup](../../cucuma-catalog-merchandiser/references/product-setup.md) | Catalog merchandiser | catalog_package |
| [Partner activation](../../cucuma-quality-engineer/references/partner-activation.md) | Quality engineer | activation_decision |
| [Partner lifecycle](partner-lifecycle.md) | Supplier partnerships, routing to operational owners | lifecycle_actions |

## Select the smallest composition

- **partner-onboarding:** source → intake → qualification → conversation → terms → catalog → activation assessment. Catalog drafts may proceed alongside negotiation after intake.
- **source-to-drafts:** intake → product setup. No outreach or commercial negotiation required.
- **pitch-only:** supplied partner brief → qualification → pitch preparation. Sending needs its own operational scope.
- **catalog-refresh:** supplied brief and product candidates → product setup. Preserve stable IDs; do not repeat recruitment.
- **readiness-review:** supplied brief, terms and catalog → activation assessment.
- **partner-operations:** supplied brief, terms and activation decision → only the lifecycle branch matching the current event.

Stop or branch on the module's result, not merely whether it returned an artifact. A defer decision stops outreach; missing supplier rights stop publication; an unknown send stops further outbound actions. A complete readiness assessment may correctly reject activation.

The case coordinator transfers artifacts and tracks the requested outcome. Each module owns its detailed procedure and completion evidence. Do not duplicate those rules here. Existing evidence lets a recipe start in the middle; invalidated sources cause only affected steps to rerun.

## Scope

A skills/workflow design request finishes with validated instructions and examples. No partner, connected account or deployed API is required. Do not create cases, send messages, mutate catalogs or activate a scheduler during design. Operational execution uses the user's actual scope and the shared contract; these recipe names grant no authority. The previously created partner heartbeat is paused and must remain so unless the user requests scheduled operation.
