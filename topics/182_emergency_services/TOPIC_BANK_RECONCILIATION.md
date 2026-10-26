# 182 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **legacy_pitches_routed_case_research_open** (2026-10-24). Five bounded case questions were added as proposals; selected records and limits are in [case-source notes](CASE_SOURCE_NOTES.md).

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 38 | Counted once |
| Categories / subcategories | 8 / 13 | Navigation |
| Preserved imported detailed proposals | 0 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 20 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 18 | Thirteen prior additions and five new cases |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

All 20 archived pending pitches route positionally to `BANK-182-010`–`029`. Seven trending pitches route, in order, to existing `BANK-182-026`/`031` and new `BANK-182-043`–`047`. Crosswalk reasons distinguish existing NG911 and vehicle suitability from camera governance, overdose event data, CMS ET3 evaluation, a 2012 911 outage and RFDS service records. Original records and IDs remain intact.

The cases examine organizational evidence and limits, not dispatch or treatment procedures. Existing helicopter, remote-response and performance scopes remain separate. The archived automated-call count, autonomous-ambulance readiness and emergency-department relief claims are unverified. The source note flags patient privacy and incomplete data.

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/182_emergency_services/IN_DEPTH_TOPIC_BANK.json`; SHA256 `500bccbbba87a4f57783c5bb5b14fa21f2f8af5511200dd5e4a4843b93681f90`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Validation and remaining work

Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.
All questions require case selection, source inspection, overlap review and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.
