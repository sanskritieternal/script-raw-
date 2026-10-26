# 152 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **legacy_pitches_routed_case_research_open** (2026-10-24). Six bounded cases were added as proposals. Selected premises were inspected in [case-source notes](CASE_SOURCE_NOTES.md); complete scripts and inherited claims remain unverified.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 39 | Counted once |
| Categories / subcategories | 7 / 14 | Navigation |
| Preserved imported detailed proposals | 0 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 20 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 19 | Thirteen prior additions and six newly bounded cases |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

All 20 archived pending pitches route positionally to `BANK-152-010` through `BANK-152-029`. The seven trending pitches route, in order, to `BANK-152-015` and `BANK-152-043` through `BANK-152-048`. The original 27 records and their status fields remain intact. The crosswalk gives each position and its claim boundary.

The new cases cover Grindavík evacuation, Hunga Tonga atmospheric observations, Krafla research drilling, Kawah Ijen work, Pinatubo's analogy to climate intervention, and a dated Reykjanes access closure. Existing `BANK-152-015` is the home for Campi Flegrei rather than another broad Naples hazard question. Neighbor `BANK-151-042` treats Hunga Tonga landform change before January 2022; the new atmospheric question needs different evidence. Broad geothermal power, economics and tourist themes already in this bank are kept separate from these named records.

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/152_volcanoes/IN_DEPTH_TOPIC_BANK.json`; SHA256 `b26bcf7e90f879a2d3beb610718e77e17dbfa3f41b9ae84c1092275297defb9a`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Validation and remaining work

Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.
All questions require case selection, source inspection, overlap review and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.
