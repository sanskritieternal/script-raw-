# Production bible design expansion

Implemented: 2026-10-19. Production workflow 1.1; configuration schema remains 5.0.

## System changes

- Added MAIN_CHARACTERS.md, SUPPORTING_CHARACTERS.md, CHARACTER_APPEARANCE_LOCK.md, LOCATIONS_ENVIRONMENTS.md, PROPS_COSTUMES.md and RELATIONSHIPS_TIMELINE.md as six applicability-aware records. New episodes receive 32 draft documents and a manifest.
- Expanded character/world overview, shot recipes and camera continuity, chapter/beat timing, visual references, cast voices, music motifs, scene design references, asset versions, revision impact and shared external AI generation guidance.
- Registered all six in the workflow specification, required section checks and compiled package. Existing placeholder, local-link, status, applicability and package freshness checks apply. No automatic design-ID graph validation or certification of generated visual identity is claimed.
- Kept Phase 1 as the evidence owner and Phase 3 as the scene-plan/index owner. Added a shared Phase 3 planning guide, production navigation instructions and invocation/contract updates. AI_GENERATION_HANDOFF.md remains shared guidance, not another required episode output.

## Compatibility and migration

PRODUCTION_WORKFLOW_V1.json preserves the 26-document version 1.0 contract. New projects use 1.1. Existing enrolled projects remain on their manifest version until explicitly upgraded. Initial migrate/scaffold remains preview-first for unenrolled projects.

`python -m Tools.projects.production_workflow upgrade "<episode>"` previews six draft records; `--write` creates missing files and updates the manifest. Existing editorial content, CONFIG, statuses, locks and mappings are preserved. Preexisting new design files are preserved and added as draft, not approved. Expanded older guides need editorial incorporation into existing episode copies. Repeat upgrades are a no-op. Changed system/compiler inputs require package rebuilding before Phase 4 freshness can pass.

The open 017 Pip birthday-cake episode receives the six new draft records. This migration does not complete its unfinished cast/world decisions or approve any media. Other episodes are not bulk-upgraded.

## Verification

`python -m unittest tests.test_contract tests.test_production_workflow -q`: 36 tests passed. Coverage includes new-project scaffolding, preserved migration, version 1.0 validation/compilation, upgrade preview/preservation/idempotence, required new-document sections, new-record compilation and package invalidation, existing mapping gates and human-review requirements.

Also verify the 32 template files, unique complete compiler section coverage, template local links and matching active invocation guides. For the selected episode, compare all preexisting file bytes except the intentionally updated manifest and validate Phase 0. New design files remain draft; no Phase 2 completion is asserted.
