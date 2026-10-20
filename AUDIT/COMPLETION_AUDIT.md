# V6 migration completion audit

> Historical schema 3.0 completion record. The current schema 4.0 taxonomy has 46 categories; see `ALL_CATEGORY_RESTRUCTURE.md` and the latest `STRUCTURAL_AUDIT.md`.

Date: 2026-10-15. Scope: repository structure, configuration and text pipeline readiness.

| Requirement | Evidence | Result |
|---|---|---|
| Read and account for source files | `FILE_VERIFICATION.md` records checked source paths and hashes; `STRUCTURAL_AUDIT.md` reports 9,093 files read. Generated audit reports are excluded from their own inventory. | Pass |
| Reclassify all 500 niches | `REGISTRY/NICHE_TAXONOMY.csv` has stable IDs in 14 primary subject categories; `REGISTRY/LEGACY_TOPIC_PATHS.csv` maps old paths to new. | Pass |
| Preserve and wire all 7,500 angle presets | `validate_repository.py` checks links and schema; `populate_niches.py --verify-content` reports 0 missing and 0 drift across 500 indexes and 7,500 angles. | Pass |
| Reconcile Q1-Q42 | `REGISTRY/CONFIG_SCHEMA.json` is the canonical schema; 14 active category presets and all topic presets use it. `REGISTRY/LEGACY_TOPIC_DEFAULTS.csv` retains old answers. | Pass |
| Materialize all 500 niches across registry and output | `REGISTRY/Categories/Niches/` has 500 niche presets, `REGISTRY/Topics/` has 500 niche folders, and `OUTPUT/<SubjectCategory>/Topics/` has 500 niche landing folders. `materialize_niches.py` is non-overwriting; `validate_repository.py` checks every expected path and content. | Pass |
| Make a specific episode from an angle | `create_project.py` requires a story question for writes, records answer provenance and uses an episode slug in the project path. Existing CONFIG files and pilot references use this path. | Pass |
| Wire six phase handoffs | `CORE/PIPELINE/CONTRACT.md` and `validate_project.py` define and check phases 0-5, exact timing, claim links, audit rows and review gates. | Pass |
| Check risk and timing branches | Four contract tests cover unverified claims, variable duration, high risk review and the complete text pilot. A separate variable duration Phase 0 fixture passes. | Pass |
| Refresh repeatable audit | `python -m Tools.validation.audit_repository` exits 0 and regenerates `FILE_VERIFICATION.md` and `STRUCTURAL_AUDIT.md`. | Pass |

The 15 angles per niche are candidate prompts, not 7,500 researched episodes. The six phase physics pilot is a validated **text package**; it does not prove rendered assets, rights clearance or publication readiness. For every real episode, an editor must select a useful story question, confirm source support and rights, and complete any required human review.

## Commands run

```text
python -m Tools.validation.validate_repository
python -m Tools.registry.materialize_niches
python -m Tools.registry.populate_niches --verify-content
python -m Tools.validation.validate_project AUDIT/PILOTS/343_physics/343_physics_beginner_explainers_si_light_speed_exact --through 5
python -m Tools.validation.validate_project AUDIT/PILOTS/343_physics/343_physics_advanced_concepts_metre_light_second --through 0
python -m unittest tests.test_contract -v
python -m Tools.validation.audit_repository
```

All commands exited 0 on 2026-10-15. See `STRUCTURAL_AUDIT.md` for their captured outputs.
