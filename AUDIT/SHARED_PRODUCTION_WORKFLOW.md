# Shared production workflow implementation

Date: 2026-10-18. Scope: all future episodes across the 530 registered niches; explicit migration for existing episodes.

## Six tasks

| Task | Implemented system change | Evidence |
|---|---|---|
| 1. Shared templates | Ten reusable supporting templates plus the stable 16 numbered templates; 26-document specification | CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/PRODUCTION_WORKFLOW.json |
| 2. Topic applicability | Document states, allowed Not applicable reasons, documentary/fiction guidance, non-fixed beat count | WORKFLOW_GUIDE.md and template applicability guidance |
| 3. Pipeline wiring | Phase 1-5 masters, authoritative contract, autonomous rules and root agent/usage documents updated | CORE/PIPELINE/CONTRACT.md; CLAUDE.md; USAGE.md; HOW_IT_WORKS.md |
| 4. Generation/compilation | New project scaffolds; preview-first scaffold/migrate CLI; deterministic eleven-section package, preserved scenes, asset index and input/output hashes | create_project.py; production_workflow.py |
| 5. Validation | Completed/draft/N/A states, required fields, local links, lock checks, scene/claim/beat/asset/chapter mapping and stale package checks | validate_project.py; 27 passing tests across both test modules |
| 6. Existing rollout | Existing files preserved; explicit adoption; historical compatibility; tested migrated pilot copy and new-project creation | AUDIT/PILOTS/EXPANDED_WORKFLOW/README.md |

## Verification

- `python -m unittest tests.test_contract tests.test_production_workflow -q`: 27 tests passed.
- Existing six-phase pilot remains valid without enrollment.
- New cartoon-niche creation supplies all 26 draft files and passes only its completed Phase 0 gate.
- Migrated physics pilot copy compiles and validates through Phase 4.
- Negative tests cover incomplete drafts, waived required locks, missing manifest, unknown claim IDs, incomplete beats, invalid asset usage, missing source fields, non-boundary chapters, broken links, stale inputs and direct package edits.
- Fixed and variable timing, preserved editorial bytes and mandatory final human-review evidence remain tested.
- Repository-wide audit result is recorded in STRUCTURAL_AUDIT.md after completion.

## Current workspace limitation

The previously discussed OUTPUT/501_public_health/501_public_health_famous_examples_new_york_smoke_exposure_2003_2004 directory is absent. Only OUTPUT/501_public_health/README.md is present. That episode was not migrated or recreated from conversation memory. Restore its real files before running preview-first migration. No bulk modification of existing niche/episode folders was performed.

## Commands

```powershell
python -m Tools.projects.production_workflow migrate "OUTPUT/<niche>/<episode>"
python -m Tools.projects.production_workflow migrate "OUTPUT/<niche>/<episode>" --write
python -m Tools.projects.production_workflow compile "OUTPUT/<niche>/<episode>"
python -m Tools.projects.production_workflow compile "OUTPUT/<niche>/<episode>" --write
python -m Tools.validation.validate_project "OUTPUT/<niche>/<episode>" --through 4
```

Default workflow CLI invocations preview only. Completing scaffolds and manifest scene mappings is required before compilation. All review, rights and execution decisions remain episode-specific; internal document adoption is not publication approval.


## Repository-wide final result

`python -m Tools.validation.audit_repository` completed with exit code 0: 19,369 active files read/hashed, 530 topic directories, zero incomplete topic grids and zero misnamed topic files. Registry, generated content/scope, historical pilots and all 27 contract/workflow tests passed. Final edited workflow/test source bytes were read again and their inventory rows refreshed after the audit where needed. Detailed results: STRUCTURAL_AUDIT.md and FILE_VERIFICATION.md.
