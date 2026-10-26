# 047 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **archived_pitches_routed_case_expansion_open**. All 27 archived pitches have active BANK routes. Subject coverage remains open; three selected case source trails were inspected.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 65 | Counted once |
| Categories / subcategories | 6 / 16 | Navigation |
| Preserved imported detailed proposals | 32 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 0 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 33 | Eight earlier additions plus 25 case-specific additions |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/047_aviation/IN_DEPTH_TOPIC_BANK.json`; SHA256 `68a0d000012e26d0927acb28716d3663fb490291bf82a2e298ce240a581b2abe`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Archived case routing, 24 October 2026

- All 27 archived records have routes in `legacy_topic_crosswalk`: 25 distinct aviation case and operations proposals; the existing crew-resource-management proposal BANK-047-029; and the niche 162 Boeing 737 MAX MCAS proposal BANK-162-015.
- The new proposals separate named accident evidence from the bank's broad safety-method questions, and individual aircraft programs from design primers. Examples: Aloha 243's lap-joint investigation versus general maintenance records, the Comet test program versus general fatigue, and Concorde service versus early supersonic design tradeoffs.
- Three bounded primary-source trails and editorial limits are in [CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md). Remaining accident, aircraft and consumer claims require their own checks before production. Archived trend labels and superlatives are not treated as current verified facts.

## Validation and remaining work

Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.
All questions require source inspection and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.
