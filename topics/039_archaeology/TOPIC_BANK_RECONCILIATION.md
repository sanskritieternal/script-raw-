# 039 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **archived_pitches_routed_case_expansion_open**. All 27 archived pitches have an active BANK route. Subject coverage remains open; three selected case source trails were inspected.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 61 | Counted once |
| Categories / subcategories | 4 / 13 | Navigation |
| Preserved imported detailed proposals | 31 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 0 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 30 | Six earlier additions plus 24 case-specific additions |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/039_archaeology/IN_DEPTH_TOPIC_BANK.json`; SHA256 `beffcce86b274380ea561d87d798d35a267b0b6e128d6c36e08a21ca690342b2`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Archived case routing, 24 October 2026

- The 27 archived records now have one route each in `legacy_topic_crosswalk`: 24 new, individually scoped archaeology BANK proposals; the existing Piltdown route to BANK-002-038; Antikythera wreck assemblage to BANK-002-122; and the Herculaneum scroll-reading challenge to BANK-013-065.
- The new case proposals are distinct from the bank's general methods: for example the Khufu corridor tests versus the general remote-signal decision question, the Pompeii black room versus the two-city eruption comparison, and Upano Valley's documented settlement network versus the general lidar interpretation question.
- Three selected primary-source checks and their limits are in [CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md). The remaining case claims, especially the archive's dates, quantities, labels and superlatives, need research before production.

## Validation and remaining work

Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.
All questions require source inspection and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.
