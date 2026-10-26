# 116 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **legacy_pitches_routed_case_research_open**. Subject coverage remains open; selected primary case records have been inspected.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 37 | Counted once |
| Categories / subcategories | 7 / 11 | Navigation |
| Preserved imported detailed proposals | 0 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 20 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 17 | Fourteen prior additions plus three bounded case questions |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/116_mountains/IN_DEPTH_TOPIC_BANK.json`; SHA256 `21276c5bb40e5398d28181ad5b36ca7eaa09bc3028d163c234cce4add822a450`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Validation and remaining work

All 20 pending and 7 trending pitches have stable-position `legacy_topic_crosswalk` routes. Twenty-three entries use local existing scopes, one 1996 Everest entry routes to neighboring BANK-034-051, and three use new bounded questions. Original pitch records, statuses and IDs are unchanged. Local semantic review kept the existing K2 Bottleneck mechanism separate from the dated 2008 disaster and kept Matterhorn permafrost under BANK-116-026. The neighboring 1996 Everest reconstruction already covers the event, so no competing question was added here.

[CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md) records National Park Service and USGS range evidence, a Norwegian Climbing Federation 2008 K2 chronology, Messner's account and a Swiss SLF Matterhorn field case. It marks the limits of each claim. Original roadmap questions with precise mortality, physiology, Sherpa and climate assertions remain preserved; their wording is not a new verification and must be checked individually before production.

Targeted `python Scripts/manage_all_topic_banks.py render --start 116 --end 116` and `check_bank` validate local structure, preservation and rendered links. They do not certify exhaustive semantic uniqueness, every archived numerical claim or current mountain-hazard conditions. All topics remain proposed and need the production readiness process.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md, CASE_SOURCE_NOTES.md and this reconciliation report.
