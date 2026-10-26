# 001 — Topic-bank status and reconciliation

[Read the main topic bank](IN_DEPTH_TOPIC_BANK.md)

Updated: 2026-10-23. Status: **proposals; coverage remains open**.

| Record family | Count | Treatment |
|---|---:|---|
| Active detailed video proposals | 210 | Counted once |
| Top-level categories / subcategories | 11 / 41 | Navigation only |
| Imported active ZIP proposals | 121 | IDs, questions, scopes and original fields preserved |
| New proposals in this reconciliation | 89 | Individually scoped additions |
| ZIP starter proposals | 12 | prior_initial_map retained; inactive and excluded |
| Repository legacy roadmap records | 27 | Original IDs and fields preserved; linked to detailed proposals |
| Registry depth topics / ideas / series | 8 / 3 / 1 | Existing records preserved; not extra bank proposals |
| Completed episodes in status data | 0 | Existing completion status retained |
| Sources verified for this expansion | 0 | No research or source verification performed |

## Inputs and merge decisions

- Supplied archive: `Youtube bank topic/YouTube-Topic-Banks-All-550-Niches.zip`; SHA256 `7892756232c9d04ba0ac99e8227317a4094d647335eddd629a76c9409ebd49da`.
- Imported member: `files/topics/001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.json`; SHA256 `3306062225bc2e870ed7b06df5745ca4bab609d1946e512f414f133d9586cd48`. ZIP member and supplied extracted file matched byte for byte before integration.
- Read the archive instructions and inspected its niche 001 records and both patch path lists. The exported niche 001 bank was absent locally. Integrated its final JSON deliberately; neither broad patch was applied.
- Existing repository roadmap, status data, registry TOP/IDEA/series records and angle definitions were inspected. Kept integer legacy IDs separate from BANK, CATALOG, TOP and IDEA IDs.
- Old roadmap surveys overlap narrower ZIP entries. Linked each survey to detailed questions rather than importing it as an extra active episode. The original 20 roadmap questions and all 20 angle questions are retained. The seven legacy trend candidates retain their original fields with no assertion of current popularity.
- Preserved the ZIP prior_initial_map and every imported active record. Added a category layer, levels, related-topic links and new subcategories without replacing original IDs/questions/scopes.
- Left shared sources, CAT questions, existing ideas, registry depth files, other niches, bundle files and unrelated working-tree changes intact. The shared topics index changes only its niche 001 report cell.

## Duplicate and progression review

Reviewed all imported and added questions against their scopes, grouped by subject. Token segmentation versus tokenizer-to-tokenizer counts; gradient calculation versus optimizer updates; throughput versus kernel profiling; source relevance versus citation validity; general demonstrations versus robot intervention accounting; task productivity including organizational hidden work, kept within BANK-001-047; generation versus media authenticity; and public authorization versus technical execution remain separate questions with explicit boundaries and related links. Legacy surveys are crosswalk references rather than new active proposals. No repeated question-angle matrix was added.

Exact normalized questions and IDs are checked automatically. Related-but-distinct boundaries are recorded with topic links below each relevant question. Archived starter questions and legacy roadmap references are outside the active duplicate/count set. This does not claim mathematical detection of every semantic overlap.

## Validation and limits

Run `python Scripts/manage_ai_topics.py validate` for reproducible content checks. The command exits nonzero on errors and prints checked record/link counts. The generated views must match their JSON inputs.

The repository-wide validator was run before edits and reported existing `Identity drift: 281_ayurveda` and `Output landing drift: 281_ayurveda`. Those unrelated findings were left unchanged. Existing depth-plan validation passed before this work.

Final checks passed for niche-only validation, all five existing depth-planning tests, generated depth-view freshness, Python compilation and whitespace. The final repository-wide check retained the same two Ayurveda findings. In-memory negative checks confirmed rejection of duplicate questions, incorrect counts, missing crosswalk targets and prerequisite cycles. Pre-existing Ayurveda/helper/prompt edits were compared with the initial byte hashes and preserved; only the niche 001 row changed in the shared index.

No new production project, research ledger, source-verification status, episode script or GitHub push is included.

## Coverage still open

- **Language and script cases:** The added normalization, transliteration and morphology questions cover distinct missing mechanisms. Select qualified language reviewers and declared datasets; dialect speech and accessibility remain in 068, 103 and 133 rather than cloned language-name episodes.
- **Versioned cases and regional institutions:** Select systems, dates, facilities, jurisdictions and participant groups within the existing energy, rights and deployment questions. Add a new proposal only when the case changes the mechanism, decision or outcome question.
- **Frontier and longitudinal evidence:** Memory, adaptation, reasoning and physical learning already have active questions. Evaluate newly documented mechanisms and longer-term deployment outcomes as evidence becomes available; a product launch alone does not warrant another episode.
- **Research and production readiness:** All questions remain proposals requiring actual source discovery, case selection, registered-angle review and claim work. Existing registry IDEA readiness remains unchanged.

## Supporting files

- [Editable bank](IN_DEPTH_TOPIC_BANK.json): active proposals, archived starters, merge evidence and crosswalks.
- [Legacy status](topics_status.json): original 27 records and bank references; original queue/trend fields are historical planning metadata.
- [Compatibility roadmap](001_AI_TECHNOLOGY_EXPLAINERS_CHANNEL_TOPIC_ROADMAP.md): directs readers to the main file.
- [Registry identity](../../REGISTRY/Niches/001_ai_technology_explainers/NICHE_001_ai_technology_explainers.md): existing supporting structure.

## Files changed by this work

- [IN_DEPTH_TOPIC_BANK.md](IN_DEPTH_TOPIC_BANK.md) and [IN_DEPTH_TOPIC_BANK.json](IN_DEPTH_TOPIC_BANK.json): new reconciled main reading file and editable catalog.
- [Original roadmap](001_AI_TECHNOLOGY_EXPLAINERS_CHANNEL_TOPIC_ROADMAP.md): compatibility entry point; original text is preserved in the catalog snapshot and main crosswalk.
- [TOPICS_COVERED_REPORT.md](TOPICS_COVERED_REPORT.md) and [topics_status.json](topics_status.json): reconciliation, counts and legacy cross-references.
- [Shared topics index](../README.md): niche 001 cell only; pre-existing changes to other cells retained.
- [Niche 001 render/validator](../../Scripts/manage_ai_topics.py): targeted maintenance command; no all-niche writer was imported.
