# 108 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **legacy_pitches_routed_case_research_open**. Subject coverage remains open; selected primary case records have been inspected.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 48 | Counted once |
| Categories / subcategories | 5 / 13 | Navigation |
| Preserved imported detailed proposals | 30 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 0 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 18 | Four prior additions plus fourteen bounded case questions |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/108_logistics_supply_chain/IN_DEPTH_TOPIC_BANK.json`; SHA256 `00f553eb76b8f338ae91554bae2ac9869a630361c9a3aaed2412aace5adf35b7`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Validation and remaining work

All 20 pending and 7 trending entries in the preserved status file now have position-stable `legacy_topic_crosswalk` routes. Existing BANK questions absorb 11 entries; fourteen newly authored questions absorb the other 16, with the Shanghai port question reused for pending 3 and trend 25. Pending 5 routes to two distinct chokepoint cases. The original pitches, statuses and IDs remain unchanged.

The additions focus on named operations, dated regulatory or operator records and one event at a time. Semantic review included local scopes for bullwhip, containerization, modal choice, Ever Given, cold chain, warehouse automation, traceability, reverse logistics, hazardous freight and resilience. It also checked adjacent banks: BANK-014-059 concerns Panama Canal expansion, BANK-031-055 lock design, BANK-035-064 maritime defense cost, and BANK-051-061 Toyota's quality-stop practice. The new questions ask different logistics-record questions. Sources and limitations for selected Red Sea, Panama, Dali, green-corridor and container-loss premises are in [CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md).

Targeted `python Scripts/manage_all_topic_banks.py render --start 108 --end 108` and `check_bank` validate the local bank structure, preservation and rendered links. They cannot certify all semantic uniqueness or the archive's numeric and causal assertions. Proposed questions still require case-specific source inspection and the production readiness process. Existing popularity and completion claims remain source metadata, not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md, CASE_SOURCE_NOTES.md and this reconciliation report.
