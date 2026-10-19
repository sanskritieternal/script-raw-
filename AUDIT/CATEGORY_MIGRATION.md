> **Historical report ? schema 5 supersedes these paths.** See `AUDIT/NICHE_HOME_MIGRATION.md` and `CORE/PIPELINE/CONTRACT.md` for the active layout.

# Category migration record

> Historical snapshot of the first 14-category migration. The current 46-category taxonomy and all 500 new paths are documented in `ALL_CATEGORY_RESTRUCTURE.md` and `REGISTRY/CATEGORY_RESTRUCTURE_PATHS.csv`.

## Current taxonomy

The primary category describes the **subject**. Story angle (Q3), visual style (Q15), generation method (Q40), audience and language are separate decisions. All 500 stable niche IDs are listed in `REGISTRY/NICHE_TAXONOMY.csv`; the 15 angle presets for each ID remain under its subject folder.

| Subject folder | Niche families |
|---|---:|
| Business_Economy | 50 |
| Children_Education | 17 |
| Culture_Arts | 51 |
| Future_Scenarios | 30 |
| Health_Wellness | 9 |
| History_Civilizations | 24 |
| Lifestyle_Making | 31 |
| Media_Creative | 26 |
| Religion_Philosophy | 28 |
| Science_Nature | 80 |
| Society_Politics | 30 |
| Sports_Games | 21 |
| Technology_Engineering | 76 |
| Travel_Places | 27 |
| **Total** | **500** |

The original repository had 472 of 500 families under `Business_Money`. `build_taxonomy.py` generated the explicit mapping. Ninety-six titles that plausibly span subjects received an explicit primary decision, with alternate categories retained in `secondary_categories`. This was a title and topic-intent classification; it does not certify the factual content of all 7,500 generic angle files.

## Files changed and preserved

- `migrate_topic_paths.py --apply` moved all 500 niche directories into the 14 subject folders without changing their three-digit IDs or slugs.
- `REGISTRY/LEGACY_TOPIC_PATHS.csv` retains every old and new path. Historical output projects are under `OUTPUT/Legacy/` with their original internal text untouched.
- `REGISTRY/CONFIG_SCHEMA.json` and the 14 active `CAT_<SubjectCategory>.md` files replace the old category semantics. The 11 earlier presets are under `AUDIT/Legacy_Instructions/Category_Presets/`; see `CATEGORY_PRESET_RESOLUTION.md` for their disposition.
- `REGISTRY/LEGACY_TOPIC_DEFAULTS.csv` preserves prior Q2–Q42 topic answers. The 7,500 active topic files now match schema 3.0 and the new category paths.
- Active instructions, generators and the master registry route through the taxonomy. `python populate_niches.py --verify-content` confirms the entire generated grid is reproducible without overwriting files.

## Editorial boundary

The 15 generated angles per niche are **candidate angles**. Before a real production, choose a specific story question, check audience value and source availability, and discard angle combinations that do not fit. Do not infer a researched topic, permission to use an asset, or publication readiness from a category assignment. The complete text pilot under `AUDIT/PILOTS/` tests the pipeline, while one Phase 0 pilot per category tests configuration routing.
