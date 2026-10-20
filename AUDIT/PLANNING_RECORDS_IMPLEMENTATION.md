# Planning records and existing-guide rollout

Implemented 2026-10-19, following the reference comparison. Production workflow stays at 1.1 with 32 required manifest documents; these helpers add optional records without silently changing old episode contracts.

## Implemented

- Reusable Phase 3 SCENE_PLANNER_TEMPLATE.md. New project creation populates SCENE_PLANNER.md with exact CONFIG scene starts/ends/durations, including VARIABLE plans and final shorter scenes. Narrative purpose, chapters/beats, batching and evidence/continuity remain editorial draft decisions.
- Reusable Phase 2 GENERATOR_PROFILE_TEMPLATE.md. New projects receive GENERATOR_PROFILE.md with Pending selection and explicit capability verification, reference inputs, clip assembly and actual execution/review fields. No provider selected, capabilities asserted or media generated.
- `prepare-planning`: preview-first missing-file creation for existing episodes, never overwriting existing planner/profile records.
- `scene-index`: preview-first generation of MASTER_SCENES_INDEX.md from actual scenes and CONFIG; no index is created for absent or mismatched scenes. Includes exact timing, chapters, claims and source-file links. Manual indexes are preserved; only signature-marked generated indexes can be rebuilt.
- Phase 3 validates opted-in planner timing/placeholders and index freshness. Generator profile headings, placeholders and local links are checked. These structural checks do not verify provider claims, every continuity relationship or human review.
- Compiler includes optional scene planner/index and generator profile, with fingerprint coverage for records and helper implementation. These changes require rebuilding existing package snapshots before they can pass freshness checks.
- `sync-guides`: appends shared sections with missing headings, preserving existing bytes and marking changed manifest records draft for review. It does not replace content under already-present headings. Repeat execution is a no-op until shared headings change.
- Shared guides, command documentation and both active invocation libraries updated.

## Episode 017

Appended missing sections to ten production documents, preserving their previous content. Added SCENE_PLANNER.md and GENERATOR_PROFILE.md drafts. Manifest still contains 32 production records. Original file byte prefixes verified preserved; only the manifest's statuses may be changed by synchronization. The episode has no actual Phase 3 scenes yet, so no master scene index was fabricated. Existing draft decisions are not completed by adding sections.

## Verification

`python -m unittest tests.test_contract tests.test_production_workflow tests.test_planning_records -q`: 41 tests passed. New coverage includes preview behavior, existing-file preservation, index rebuild and tampering detection, refusal of manual-index overwrite, scene timing mismatch, planner placeholders/timing, optional-record compilation and freshness, and idempotent guide synchronization with draft status reset. Existing configuration, manifest migration, scene mapping and human-review gates remain covered.
