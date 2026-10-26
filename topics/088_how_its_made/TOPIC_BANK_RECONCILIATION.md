# 088 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **archived_pitches_routed_manufacturing_cases_open**. Subject coverage remains open; selected producer claims have bounded source checks.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 57 | Counted once |
| Categories / subcategories | 7 / 16 | Navigation |
| Preserved imported detailed proposals | 31 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 0 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 26 | Eight existing additions plus 18 named process cases |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/088_how_its_made/IN_DEPTH_TOPIC_BANK.json`; SHA256 `d949fe12931c58a5a58b7072faa9eb3c0fd7f3fe0b44d9fa83f39ab05ff85fb0`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Archived pitch routing, 24 October 2026

- All 27 archived pitches have explicit `legacy_topic_crosswalk` routes. Eighteen new questions name a process, material, product or producer at a bounded manufacturing stage. Seven pitches reuse existing local scopes for cans, bottles, corrugation, steel, paper, bearings and lenses. LEGO and ballpoint pens route to verified neighboring cases `BANK-051-064` and `BANK-051-073`.
- [CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md) records bounded producer-source checks for TSMC N2 and Nissin Chicken Ramen, plus the LEGO tolerance discrepancy behind an external route. Producer statements do not verify the archive's exact tolerances, cycle times, performance rankings or factorywide generalizations.
- New questions distinguish raw materials, intermediate goods, fabrication, assembly, inspection and installation. Undisclosed plant details and practical chemical or ignition procedures remain outside these proposal scopes.

## Validation and remaining work

Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.
All other questions require case selection, source inspection, overlap review and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.
