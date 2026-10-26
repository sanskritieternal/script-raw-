# 140 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **legacy_pitches_routed_case_research_open**. Subject coverage remains open; selected primary case records have been inspected.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 36 | Counted once |
| Categories / subcategories | 8 / 11 | Navigation |
| Preserved imported detailed proposals | 0 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 20 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 16 | Fourteen prior additions plus two bounded cases |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/140_sailing_yachting/IN_DEPTH_TOPIC_BANK.json`; SHA256 `ef704fed41d210839e424b25c5e1fb502310b8754f7fe25cecb67560cc9f47c1`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Validation and remaining work

All 20 pending and 7 trending pitches have stable-position `legacy_topic_crosswalk` routes. Twenty-four use existing local scopes, the Harrison H4 pitch routes to neighboring maritime BANK-048-057, and two dated trend cases receive new questions. Original pitch records, statuses and IDs remain unchanged. Semantic review distinguished the existing orca narrative from a named 2024 workshop's evidence, the existing foiling-speed question from 2024 AC75 class constraints, and Harrison's H4 from duplicate maritime coverage.

[CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md) links the Spanish-Portuguese-sponsored orca workshop and 37th America's Cup organizer and supplier records. It bounds claims about animal motive, encounter rates, current navigation advice, fixed versus open class components and boat speed. Preserved original safety and historical assertions still need individual fact review before production.

Targeted `python Scripts/manage_all_topic_banks.py render --start 140 --end 140` and `check_bank` validate structure, preservation and rendered links. They do not certify exhaustive semantic uniqueness, current passage conditions, accident causes or safe operational procedures. All questions remain proposed and require the production readiness process.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md, CASE_SOURCE_NOTES.md and this reconciliation report.
