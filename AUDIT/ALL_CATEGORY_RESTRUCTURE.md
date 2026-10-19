> **Historical report ? schema 5 supersedes these paths.** See `AUDIT/NICHE_HOME_MIGRATION.md` and `CORE/PIPELINE/CONTRACT.md` for the active layout.

# All-category restructuring record

Date: 2026-10-16. All 500 stable niche IDs were reviewed against their titles and assigned to 46 smaller top-level subject categories. The assignment is explicit in `restructure_categories.py`; the 500-row old-to-new path map is `REGISTRY/CATEGORY_RESTRUCTURE_PATHS.csv`. This is a subject taxonomy, not a count-balancing exercise.

## Result

| New category | Niches | Previous broad category source |
|---|---:|---|
| `Ancient_Civilizations` | 5 | History_Civilizations (5) |
| `Careers_Workplace` | 12 | Business_Economy (12) |
| `Childhood_Family` | 3 | Children_Education (3) |
| `Commerce_Industry` | 22 | Business_Economy (22) |
| `Computing_Software` | 19 | Technology_Engineering (19) |
| `Conflict_Power_Exploration` | 6 | History_Civilizations (6) |
| `Craft_Making` | 15 | Lifestyle_Making (15) |
| `Crime_Safety_Public_Services` | 10 | Society_Politics (10) |
| `Cultural_Heritage` | 19 | Culture_Arts (18), Media_Creative (1) |
| `Cybersecurity_Digital_Systems` | 6 | Technology_Engineering (6) |
| `Earth_Environment` | 28 | Science_Nature (28) |
| `Energy_Industry` | 9 | Technology_Engineering (9) |
| `Engineering_Inventions` | 13 | Technology_Engineering (13) |
| `Fiction_Worldbuilding` | 9 | Media_Creative (9) |
| `Film_Production` | 13 | Media_Creative (12), Technology_Engineering (1) |
| `Finance_Banking` | 15 | Business_Economy (15) |
| `Food_Fashion` | 5 | Culture_Arts (5) |
| `Future_Worlds_Systems` | 13 | Future_Scenarios (13) |
| `Games_Puzzles` | 9 | Sports_Games (9) |
| `Geography_Places` | 14 | Travel_Places (14) |
| `Government_Geopolitics` | 8 | Society_Politics (8) |
| `Hindu_Traditions` | 15 | Religion_Philosophy (15) |
| `Historical_People_Cultures` | 8 | History_Civilizations (8) |
| `Home_Living` | 12 | Lifestyle_Making (12) |
| `Hospitality_Travel_Systems` | 4 | Travel_Places (4) |
| `Human_Futures` | 11 | Future_Scenarios (11) |
| `Land_Outdoor` | 4 | Lifestyle_Making (4) |
| `Learning_Education` | 14 | Children_Education (14) |
| `Life_Biology` | 27 | Science_Nature (27) |
| `Literature_Performance` | 15 | Culture_Arts (15) |
| `Math_Scientific_Methods` | 9 | Science_Nature (9) |
| `Media_Formats_People` | 5 | Media_Creative (4), Society_Politics (1) |
| `Medicine_Healthcare` | 4 | Health_Wellness (4) |
| `Mind_Wellness` | 5 | Health_Wellness (5) |
| `People_Communities` | 12 | Society_Politics (11), Business_Economy (1) |
| `Performance_Magic` | 3 | Sports_Games (3) |
| `Philosophy_Spirituality` | 5 | Religion_Philosophy (5) |
| `Physical_Sciences` | 9 | Science_Nature (9) |
| `Robotics_AI` | 8 | Technology_Engineering (8) |
| `Space_Astronomy` | 7 | Science_Nature (7) |
| `Speculative_Stories` | 6 | Future_Scenarios (6) |
| `Sports_Adventure` | 9 | Sports_Games (9) |
| `Transport_Engineering` | 20 | Technology_Engineering (20) |
| `Travel_Experiences` | 9 | Travel_Places (9) |
| `Visual_Arts_Crafts` | 13 | Culture_Arts (13) |
| `World_Religions` | 13 | Religion_Philosophy (8), History_Civilizations (5) |

**Total:** 500 niches across 46 categories. Each niche retains its three-digit ID and slug.

## Files synchronized

- `REGISTRY/NICHE_TAXONOMY.csv` records the new primary category and current path for each ID. Earlier secondary labels were retained in `legacy_secondary_categories`; the active `secondary_categories` field is blank pending a separate cross-category tagging review.
- `REGISTRY/CONFIG_SCHEMA.json` is schema 4.0 with Q1-Q42 and 46 category overrides. Each new category starts from the closest earlier broad subject defaults. The selected topic still sets Q3 and Q15, and project answers override defaults.
- `REGISTRY/Categories/` has 46 active CAT presets and 500 niche presets. `REGISTRY/Topics/` has 500 niche folders and 7,500 angle files. `OUTPUT/` has 500 niche landing folders; existing project content was moved without changing stable IDs.
- `REGISTRY/LEGACY_TOPIC_PATHS.csv` and `REGISTRY/LEGACY_TOPIC_DEFAULTS.csv` now point to current topic paths. `REGISTRY/CATEGORY_RESTRUCTURE_PATHS.csv` records the immediate prior paths and all 500 moves.
- The pre-migration taxonomy, schema, path maps and 14 former category presets are preserved in `AUDIT/Taxonomy_Restructure_2026-10-16/`. Older CAT presets are archived under `AUDIT/Legacy_Instructions/Category_Presets/`.

## Editorial boundary

The 46 labels were assigned from niche titles and the original registry context. A few subjects span more than one category; the single primary route is a filing decision. Category defaults inherited from the prior broad subjects are safe starting points, not a substitute for choosing the audience, format, risk treatment and sources for an individual episode. The 15 angle files per niche remain candidates, not researched stories.

## Verification

`python validate_repository.py`, `python populate_niches.py --verify-content`, both physics pilot validators, the existing Shaktism Phase 0 validator, and `python -m unittest test_contract.py -v` pass. `python audit_repository.py` regenerates the checked-file inventory and structural report. The checks prove structure and internal wiring, not factual quality or rendered assets.

The final `audit_repository.py` run read and hashed 9,125 active source files and found 500 topic directories, zero incomplete topic grids, and zero misnamed topic files. Its captured checks report 46 passing Phase 0 routing pilots, zero generated-content drift, passing full and variable timing pilots, and five passing contract tests.
