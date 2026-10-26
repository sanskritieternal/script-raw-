# 148 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **legacy_pitches_routed_case_research_open**. Subject coverage remains open; selected primary humanitarian records have been inspected.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 38 | Counted once |
| Categories / subcategories | 8 / 12 | Navigation |
| Preserved imported detailed proposals | 0 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 20 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 18 | Fifteen prior additions plus three bounded case questions |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/148_humanitarian_stories/IN_DEPTH_TOPIC_BANK.json`; SHA256 `8dfda1d240ae3304b53ee9d2b23d70f5b740da873f5e9ad4160b0d85213ae9bb`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Validation and remaining work

The `legacy_topic_crosswalk` routes all 20 pending and 7 trending pitches by stable original position. Twenty-three entries use existing local scopes; the AI early-warning pitch routes to disaster-survival BANK-046-029; three trends use new bounded source questions. Two other trends route to more than one existing local scope where funding, accountability or outcome measurement cannot be collapsed into one. Original pitch records, statuses and IDs remain unchanged.

[CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md) links a dated OCHA Gaza access snapshot, WHO psychological first-aid guide and UNHCR statelessness reporting. It bounds claims about airdrop reach, clinical benefit, “all known” nationality cases and predictive lives saved. Neighbor review found the disaster-survival early-warning scope and distinguished existing local worker mental-health, responder and accountability questions. Research and any eventual storytelling must protect consent, privacy and the agency of affected people.

Targeted `python Scripts/manage_all_topic_banks.py render --start 148 --end 148` and `check_bank` validate local structure, preservation and rendered links. They do not certify exhaustive semantic uniqueness, current humanitarian access, clinical benefit or individual legal status. All topics remain proposed and require the production readiness process.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md, CASE_SOURCE_NOTES.md and this reconciliation report.
