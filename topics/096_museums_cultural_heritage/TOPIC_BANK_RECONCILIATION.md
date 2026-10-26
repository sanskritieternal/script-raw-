# 096 — Topic-bank reconciliation

[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)

Status: **archived_pitches_routed_museum_cases_open**. Subject coverage remains open; selected institutional premises have bounded source checks.

| Record family | Count | Treatment |
|---|---:|---|
| Active BANK proposals | 56 | Counted once |
| Categories / subcategories | 7 / 15 | Navigation |
| Preserved imported detailed proposals | 28 | Original fields, IDs and questions retained |
| Reconciled local roadmap proposals | 0 | Original questions/scopes reused without a second count |
| Archived generic local framework records | 0 | IDs and wording preserved; inactive |
| Newly authored BANK proposals | 28 | Seven existing additions plus 21 named cases |
| Local legacy source records | 27 | Original status values retained; excluded from active BANK count |

## Preservation and integration

- ZIP: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Source member: `files/topics/096_museums_cultural_heritage/IN_DEPTH_TOPIC_BANK.json`; SHA256 `1ebb7d1e6c939635e4078d6a227903d121b40b78f7ea965376d99fe5fc278951`. Checked against the bundle manifest and extracted copy before import.
- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.
- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.
- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.
- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.
- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.

## Archived pitch routing, 24 October 2026

- All 27 archived pitches have explicit stable-position `legacy_topic_crosswalk` routes. Twenty-one distinct new questions identify a museum, object, collection, site, policy or documented incident. Four routes reuse local scopes for labels, community curatorial authority, digital tours and storage. The Parthenon dispute and Rosetta decipherment route to verified neighboring cases `BANK-039-063` and `BANK-041-052`.
- Questions distinguish object-specific custody from ownership, estimated counts from verified events, and conservation decisions from universal recipes. The British Museum archive headline blends missing, stolen and damaged items into a stronger claim; the new case uses dated institutional categories and leaves culpability to legal records.
- [CASE_SOURCE_NOTES.md](CASE_SOURCE_NOTES.md) records bounded museum-source checks for Mary Rose conservation, the Met’s Open Access program, and the British Museum’s missing-item report. Other archive figures, provenance assertions, legal rights and motive stories remain unverified.

## Validation and remaining work

Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.
All other questions require case selection, source inspection, overlap review and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.

Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.
