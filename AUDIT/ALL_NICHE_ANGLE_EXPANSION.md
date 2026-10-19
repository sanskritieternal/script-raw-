# All-niche angle expansion

## Result

All 500 niche homes have an `ANGLE_PLAN.json` and corresponding Q3-only angle files. The current registry contains **16,016 angles**:

| Plans | Niches | Angles each | Total |
|---|---:|---:|---:|
| Hand-curated AI pilot (001) | 1 | 20 | 20 |
| Hand-curated Sanatan narrative pilot (004) | 1 | 60 | 60 |
| Field-based editorial drafts | 498 | 32 | 15,936 |
| **Total** | **500** | | **16,016** |

For the 498 drafts, the original 15 angle slugs were kept and reframed around each niche. Twelve further angles come from a relevant research field, and five focus on the subject category or a niche-specific override. Every entry includes a scoped direction, an example question, evidence to seek, and an editorial boundary. The generated plans are marked `generated_editorial_draft`, not researched or approved episode plans.

`build_remaining_angle_plans.py` creates only missing draft plans and never overwrites an existing plan. The plans are the editable source. `populate_niches.py --sync-content` writes their angle files and indexes; `--verify-content` checks reproducibility. No fixed maximum number of angles is enforced. The previous 7,550 angle and index files are preserved in `AUDIT/Angle_Expansion_2026-10-16/Before_Sync_Angles.zip`; the adjacent `ANGLE_COUNTS.csv` records before and after counts by niche.

## Field assignment and quality controls

The 46 subject tags were grouped into research fields such as history, technical systems, natural science, social systems, finance, health, religion, and place-based inquiry. Specific titles can override their broad tag: for example, `448_capitals` uses place and geography lenses, `500_retirement_education` uses household finance, and `075_pilgrimage_sacred_places` uses place-based inquiry. Niche 001 and 004 retain their independent hand-curated plans.

An angle is a **questioning route**, not a claim that its premise is true. Generated evidence prompts call for dated records, measurements, named sources, or attributed lived accounts as appropriate. Health, finance, crime, religious, and speculative fields carry explicit boundaries against advice, sensationalism, unsupported historical claims, and forecasts stated as fact. The existing Q8/Q41 and risk-flag review gates still apply when an actual episode is configured.

## Editorial limitations and next use

The 498 plans are structured drafts made from field and subject lenses. They have not been individually fact-checked or judged for audience demand, source availability, overlap with neighboring niches, or local nuance. Some broad titles may benefit from replacing a field lens with a more specific story family, as was done by hand for 001 and 004. Editors should review each `ANGLE_PLAN.json`, remove weak entries, and add niche-specific ones without aiming for a uniform count.

To revise one niche, edit its plan, retain any slug used by an existing project, then run `python populate_niches.py --id <ID> --sync-content`, `python populate_niches.py --id <ID> --verify-content`, and `python validate_repository.py`. A real project still requires a specific `--story-question` and Phase 1 source verification. The [production contract](../CORE/PIPELINE/CONTRACT.md) remains authoritative for project gates.

An existing project's CONFIG is a snapshot of the Q3 answer selected when that project was created. Syncing an angle plan does not rewrite an approved or in-progress project; a new project using the same angle slug receives the current Q3 wording.
