> **Historical report ? schema 5 supersedes these paths.** See `AUDIT/NICHE_HOME_MIGRATION.md` and `CORE/PIPELINE/CONTRACT.md` for the active layout.

# V6 repository improvement record

> This records the first migration to 14 broad categories. The current 46-category structure, 500-row crosswalk and verification are in `ALL_CATEGORY_RESTRUCTURE.md`.

## Completed technical migration

The active layout now includes 500 niche-specific configuration presets under `REGISTRY/Categories/Niches/` and 500 matching `OUTPUT/<SubjectCategory>/Topics/<ID>_<Slug>/` landing folders. `materialize_niches.py` creates missing files without overwriting existing content; `validate_repository.py` checks the complete set. Episode projects are nested beneath these niche folders.

| Original audit gap | Current resolution | Evidence |
|---|---|---|
| 472 families in `Business_Money` | All 500 stable IDs classified into 14 primary subject categories and moved. Story angle and production format are separate. | `REGISTRY/NICHE_TAXONOMY.csv`, `REGISTRY/LEGACY_TOPIC_PATHS.csv`, `AUDIT/CATEGORY_MIGRATION.md` |
| Q1–Q42 meaning conflicts | Schema 4.0 defines all 42 labels and defaults; 46 active category presets and 7,500 topic presets use them. Old values are preserved. | `REGISTRY/CONFIG_SCHEMA.json`, `REGISTRY/LEGACY_TOPIC_DEFAULTS.csv`, `python validate_repository.py` |
| Conflicting paths, phase and output counts | One six-phase contract defines the active tree and gates. Phase 1 has six research documents plus a claim ledger; Phase 2 has 16 numbered outputs and one optional quick reference. Old instructions and outputs are archived. | `CORE/PIPELINE/CONTRACT.md`, `AUDIT/Legacy_Instructions/`, `OUTPUT/Legacy/` |
| Unsafe autonomous approval | Risk answers and explicit flags mark human review pending; a final certificate for such a project requires named, dated approval. Research and final audit gates remain explicit. | `create_project.py`, `validate_project.py`, `CORE/RULES/autonomous.md` |
| Stale, destructive generators | The niche generator is taxonomy-driven, read-only by default and creates only missing files. The old flat generator is a compatibility wrapper. | `python populate_niches.py --verify-content` reports zero missing and zero drift |
| Missing repeatable validation | Repository, project and file-inventory checks are executable. Fourteen category Phase 0 routing pilots, a variable timing pilot and a sourced two-scene, six-phase text pilot pass. | `validate_repository.py`, `validate_project.py`, `AUDIT/PILOTS/`, `AUDIT/STRUCTURAL_AUDIT.md` |

## Editorial work for each future episode

The 15 generated angle files per niche are **candidates**, not 7,500 researched stories. A new CONFIG requires a specific story question. Before scripting, the producer must confirm audience value, source availability, the intended treatment of contested material, and rights for planned assets. The Phase 1 claim ledger records sources, access dates, confidence and disputed claims; missing facts are not filled from preset defaults.

The repository checks prove structure and internal wiring. They do not verify every source against every claim, approve real-world legal or medical content, render a video, clear assets, or publish to a platform. The six-phase physics pilot verifies one narrow text package with primary SI sources; it is not a substitute for editorial review of all 500 families.

## Maintenance commands

1. `python validate_repository.py` — taxonomy, presets, links and 14 Phase 0 routing pilots.
2. `python populate_niches.py --verify-content` — compare all 7,500 generated topics and 500 indexes with the canonical sources.
3. `python validate_project.py <project-directory> --through 5` — stage-by-stage structural project gates.
4. `python audit_repository.py` — refresh `FILE_VERIFICATION.md` and `STRUCTURAL_AUDIT.md`, including pilot checks.
