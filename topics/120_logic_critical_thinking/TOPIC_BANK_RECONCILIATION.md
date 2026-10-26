# 120 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **legacy_pitches_routed_case_research_open**. Subject coverage remains open; selected primary case records have been inspected.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 35 | Counted once |
| Categories / subcategories | 7 / 10 | Navigation |
| Preserved imported detailed proposals | 0 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 20 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 15 | Thirteen prior additions plus two bounded primary-source cases |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/120_logic_critical_thinking/IN_DEPTH_TOPIC_BANK.json`; SHA256 `c386e970f0458ec33e24a42625c75011bb6326fb6a5d6a4289172a2cbfc040dd`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Validation and remaining work

The `legacy_topic_crosswalk` routes all 20 pending and 7 trending pitches by original list position. Twenty-one entries use existing local questions; two Dunning–Kruger entries route to psychology BANK-009-141; and four archive entries share two new primary-source cases. Original pitch records, statuses and IDs remain unchanged. The new *Euthyphro* text analysis differs from the existing broad Socratic-method wording; the Good Judgment scoring question differs from a general forecasting-success claim. Cross-bank review checked psychology's study-specific Dunning–Kruger scope and statistics' correlation/Bayesian scopes rather than duplicating them.

[CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md) traces Plato's dialogue, IARPA's program description, the project team's methods and the original Dunning–Kruger study record. The note bounds claims about historical Socrates, tournament generalization and individual psychology. Broad claims in the preserved original proposals remain unverified and need individual review before production.

Targeted `python Scripts/manage_all_topic_banks.py render --start 120 --end 120` and `check_bank` validate structure, preservation and links. They do not certify exhaustive semantic uniqueness or the archived psychological, statistical or persuasion claims. All records remain proposed and require the production readiness process.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md, CASE_SOURCE_NOTES.md and this reconciliation report.
