# 064 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **archived_pitches_routed_household_cases_open**. All 27 archived pitches have active BANK routes. Subject coverage remains open; three selected source trails were inspected.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 57 | Counted once |
| Categories / subcategories | 5 / 13 | Navigation |
| Preserved imported detailed proposals | 29 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 0 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 28 | Six earlier additions plus 22 bounded household questions |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/064_home_lifestyle/IN_DEPTH_TOPIC_BANK.json`; SHA256 `79882c1b3dc58f48073966b3ce7a6cbacba297cca486d6aafd498e4b448297d5`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Archived pitch routing, 24 October 2026

- All 27 archived records have explicit `legacy_topic_crosswalk` routes: 22 distinct new household questions, two existing cross-niche questions (home automation during outage BANK-487-039 and heat-pump energy transfer BANK-360-036), and three trending variants to their matching new primary questions.
- New questions distinguish a documented routine, building system or measurable claim from the bank's general home-care primers. Fixed sleep, cognition, mold, potable-water and bill-savings promises in the archive are treated as claims needing specific evidence, not as advice or guaranteed outcomes.
- [CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md) records bounded primary-source checks for indoor air quality, mold and a low-flow showerhead. The remaining cases require individual research and location-specific checks before production.

## Validation and remaining work

Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.
All questions require source inspection and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.
