# Scene planning and index

## Ownership and reading order

CONFIG owns identity and timing; Phase 1 owns evidence; Phase 2 owns production decisions and the chapter/beat outline. Phase 3 owns scene ordering, batch planning and the master scene index. Link the existing episode STATUS.md or PROGRESS.md rather than maintaining another independent state file. Do not copy Reference project instructions or runtime into a new episode.

## Plan before drafting

Record exact Q14 runtime, Q42 timing method, scene count and any final shorter scene. For VARIABLE timing, list actual durations and check their sum. Map chapters and beats to scene ranges, story purpose, claims and chronology. Mark preliminary planning as proposed until reconciled with the actual scenes. Batch sizes and review gates come from current configuration/contract; a reference project's batch count is not a universal rule.

## One authoritative scene format

Use Scene_Breakdown.md, or retain existing Batch_*_Scenes_*.md files for a batch-based episode. Never keep both as competing scene sources. Put the navigation index and batch plan in the master file's opening section before the first **Scene N**, or in a separate SCENE_INDEX.md with no duplicated full scene blocks. List scene ranges, exact times, chapter/beat, narrative purpose, file links and drafting/review status based on actual records.

## Linked design and evidence records

Where applicable, reference character IDs, active appearance variants, location IDs, prop/costume IDs and start/end states from Phase 2. Preserve required Characters and Location fields as readable descriptions. Link each material factual claim to Phase 1 claim IDs and source locators. Retain explicit fictional/reconstruction labels. An index does not replace scene-level claims, citations, durations or generation prompts.

## Reconcile before compilation

Ensure unique sequential scenes, exact duration total, chapter boundaries and non-overlapping beat coverage. Reconcile production manifest beats/assets/chapters with actual scenes and metadata. Update the Phase 2 navigation links and existing status record. Treat design changes as revisions affecting scenes/prompts, not as permission to silently alter protected scene fields. The compiler preserves scene records and fingerprints Phase 3 Markdown; planning notes cannot substitute for completed scene content.
## Templates and generated index

Use [SCENE_PLANNER_TEMPLATE.md](SCENE_PLANNER_TEMPLATE.md), populated with CONFIG timing by `python -m Tools.projects.production_workflow prepare-planning "<episode>" --write`. Complete its editorial planning fields before Phase 3 validation. It is a plan, not proof that scenes exist.

After actual scenes match CONFIG, preview `python -m Tools.projects.production_workflow scene-index "<episode>"`; add `--write` to generate MASTER_SCENES_INDEX.md. The index has no full scene blocks and cannot become a competing screenplay. Its timing, chapter and claim rows are derived from actual scenes. Rebuild after changes; opted-in generated indexes are checked for staleness by Phase 3 validation. Existing manual indexes are preserved and need deliberate reconciliation before adopting generation.

