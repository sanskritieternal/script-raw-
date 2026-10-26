# 092 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **archived_pitches_routed_beverage_cases_open**. Subject coverage remains open; selected premises have bounded source checks.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 53 | Counted once |
| Categories / subcategories | 5 / 12 | Navigation |
| Preserved imported detailed proposals | 25 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 0 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 28 | Five existing additions plus 23 bounded beverage cases |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/092_beverage_culture/IN_DEPTH_TOPIC_BANK.json`; SHA256 `e294247fecdd9c2e3dbdd130bc62c56c06333bb40dacbc51d93bd2a3b4a1f68b`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Archived pitch routing, 24 October 2026

- All 27 archived pitches have explicit stable-position `legacy_topic_crosswalk` routes. Twenty-three distinct new questions identify a beverage, method, producer or place. Water composition, tea processing, coffee processing and repeated cocktail-ice claims reuse scoped proposals.
- New questions separate sensory observation from health or valuation claims, current label and geographic rules from universal recipes, and producer statements from independent tests. A neighboring `BANK-090-054` covers why seawater is salty; the new hydration case addresses a different physiological premise.
- [CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md) records bounded primary-source checks for espresso pressure practice, one Red Bull UK label and NOAA/WHO explanations of seawater and desalination. Other archive health, price, taste and future-supply claims remain unverified.

## Validation and remaining work

Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.
All other questions require case selection, source inspection, overlap review and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.
