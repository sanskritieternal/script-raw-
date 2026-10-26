# 080 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **archived_pitches_routed_film_cases_open**. Subject coverage remains open; selected production premises have bounded source checks.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 64 | Counted once |
| Categories / subcategories | 5 / 14 | Navigation |
| Preserved imported detailed proposals | 32 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 0 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 32 | Eight existing additions plus 24 named cases |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/080_film_entertainment_analysis/IN_DEPTH_TOPIC_BANK.json`; SHA256 `108f9625d8d32569d3ae950dbc94112e04dc2c54c3e4291710200c0c980d90c6`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Archived pitch routing, 24 October 2026

- All 27 archived pitches have explicit `legacy_topic_crosswalk` routes. Twenty-four distinct new questions identify a film, scene, production, release or contract. The broad visual grammar, sound-design and dialogue-intelligibility pitches route to existing scoped proposals without duplicate active questions.
- Film cases require a named edition, cut or sequence and relevant production credits before analysis. Industry cases distinguish gross from profit, producer claims from independent audience evidence, and a contract’s actual scope from speculation. Specific scene cases retain their formal focus rather than repeating the existing generic cinematography, editing and music proposals.
- [CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md) records bounded first-hand checks for *Oppenheimer* formats, ILM StageCraft on *The Mandalorian*, and the WGA’s 2023 AI agreement. Other archived budgets, motives, production anecdotes and viewer-effect claims remain unverified; clip and still use also requires rights review.

## Validation and remaining work

Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.
All other questions require case selection, source inspection, overlap review and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.
