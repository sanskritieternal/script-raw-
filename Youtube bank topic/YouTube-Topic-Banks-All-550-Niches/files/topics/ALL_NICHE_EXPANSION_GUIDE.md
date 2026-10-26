# All-niche topic expansion

**Current depth progress:** [113 detailed topic drafts prepared; 437 pending](./DEPTH_COMPLETION_STATUS.md). Current active totals are in the generated index; earlier coverage totals below are historical.

Updated: 2026-10-22. [Browse every niche](./ALL_NICHE_TOPIC_BANKS.md) · [Progress data](./TOPIC_BANK_PROGRESS.json) · [Original three-niche pilot](./DEPTH_EXPANSION.md)

## Historical first all-niche pass

| Coverage | Niches | Subject categories | Proposed topics | Editorial state |
|---|---:|---:|---:|---|
| Meditation, Pranayama and Yoga | 3 | 60 | 360 | Detailed pilot questions with individually written coverage boundaries |
| All remaining niches | 547 | 1,649 | 5,408 | Initial subject maps with authored subject headings and domain-pattern research briefs |
| **Combined** | **550** | **1,709** | **5,768** | **Proposed coverage; no episode sources verified** |

Every taxonomy ID has a bank. This is coverage of the niche list, not comprehensive coverage of every subject. The remaining-niche maps have 9–35 proposals each in this pass; these numbers are the current authored coverage, not minimums, quotas or maximums. The three detailed pilots remain at 120 each. The initial maps are shallower than those pilots and need further domain-specific branching and editorial refinement. Nothing is marked exhausted or publication-ready.

The new headings name actual concepts, systems, places, works, institutions, methods or explicitly original fictional premises. Their episode questions and four-part research outlines use domain-specific patterns rather than implying that an actual case study or source review has been performed. The outlines deepen a proposal; they are not counted as four extra topics. Suggested neighboring-home links are navigation leads, not a certified semantic deduplication result.

## Topic structure

**Niche → subject category → concrete subtopic → episode question → research outline → evidence requirements → selected case and sources.**

For example:

- Royalty and Dynasties → Ancient Indian dynasties → Mauryan provincial governance → an archival/textual research question with a chronology, source comparison, institutional analysis and uncertainty review.
- World Geography → Physical foundations → Global drainage basins → a question about mechanisms and measurements, followed by a bounded basin case and a map-data method check.
- EV Battery Technology → Pack engineering → State-of-health estimation → an engineering question, a worked system example, an alternative approach and a failure/measurement-limit review.
- Ramayana → Textual worlds → Kamban's Tamil epic → an attributed textual question, edition selection, interpretive comparison and translation limits.

These examples describe research routes. They do not assert that a specific interpretation, historical claim, performance result or health effect has been established.

## Files and statuses

Each existing `topics/<ID>_<slug>/` directory has:

- `IN_DEPTH_TOPIC_BANK.json`: editable catalog data, stable IDs, proposal status, questions, outlines and source requirements.
- `IN_DEPTH_TOPIC_BANK.md`: generated reading view.

The main index links all 550 banks. The three original roadmap/report/status updates are retained from batch 1. Existing roadmap queues and trend rankings for the other 547 niches are not rewritten, counted as new proposals or certified as up-to-date by this work. No production outputs are changed.

All 547 new maps leave `angle: null`. A current niche-specific angle plan must be inspected before assigning an episode angle. This avoids claiming angle-scope review that has not occurred. Their `verified_sources` lists are empty. Source **types** describe what to locate, not named sources already read. Their learning levels indicate documentary research organization, not physical exercise difficulty or confirmed learning prerequisites for a whole field.

The three detailed pilots retain their previously checked angle choices. They also remain proposed, with no verified episode sources.

## Unlimited expansion without repeated filler

There is no topic cap in the schemas, builders, renderer or indexer. Add as many useful categories and subtopics as a subject supports. Do not multiply counts by mechanically crossing every subject with every narrative angle.

Develop an actual coverage gap through one or more of these routes:

1. **Named cases:** a particular dynasty, city, technology implementation, trial, artwork, product or community.
2. **Source families:** primary text, commentary, inscription, archive, physical artifact, original dataset or observed practice.
3. **Time and place:** compare bounded periods or regions with a clear reason for comparison.
4. **Internal structure:** unpack components, mechanisms, actors, institutions, stages or competing classifications.
5. **Evidence problems:** measurement validity, missing records, rival interpretations, failure cases or replication.
6. **Consequences:** distribution of benefits and costs, accessibility, environmental effects or lived experience.

Each added entry should introduce a genuinely distinct question. Keep the subject in its primary home and add cross-links where another niche needs it. For example, a general explanation of sensor fusion is not a second autonomous-driving episode until the road context, sensor limits and operational question are specified. Shared words do not always identify the same topic: indoor/outdoor exposure means different things in lightning and air-pollution research.

## Editing and rebuilding

Edit an existing JSON bank directly. Retain IDs when improving wording and append new IDs for new topics. Update its counts after adding or removing entries. No source list or readiness state should be filled speculatively.

```bash
python Scripts/render_topic_banks.py --write --require-all-niches
python Scripts/render_topic_banks.py --check --require-all-niches
python Scripts/index_topic_banks.py
```

`Scripts/initial_subject_map_seeds.txt` preserves the authored starting headings for the 547 maps. `build_initial_subject_maps.py` creates missing initial banks and **never overwrites an existing JSON bank**. JSON is authoritative after creation; rerunning the seed builder does not update editorial changes. Its preview mode is the default; `--write` is needed to create a missing bank. The builder's seed-ID check intentionally refers to this 550-niche taxonomy snapshot; revise that manifest if the taxonomy itself changes.

The renderer can use unassigned angles for initial maps. Assigned angles require the actual local angle plan and are checked against it. The full taxonomy is required for `--require-all-niches`. The indexer reports separate detailed-pilot and initial-map states instead of treating folder presence as equal editorial completion.

## Research and production handoff

Select the exact case, source edition, population, product version, jurisdiction, place or fictional premise. Inspect source feasibility and refine the episode question. Then use the existing [depth-planning](../REGISTRY/DEPTH_PLANNING_GUIDE.md), [idea-bank](../REGISTRY/IDEA_BANK_GUIDE.md) and production-contract workflow. Catalog `BANK-*` IDs are not formal TOP/IDEA IDs and cannot be used as ready project ideas automatically.

Do not change Q1–Q42, niche identities, CAT defaults, project snapshots or output configuration merely to accommodate a catalog. Claim verification, approval gates and publication review remain separate. Record genuine evidence in Phase 1 with precise locators. Neither a generated question nor an empty verified-source list certifies its premise.

Health and finance proposals require current professional/official context and actual evidence before scripting. Legal and travel topics require a named jurisdiction/date and current official information. Religious claims require attribution and source context. Speculative futures remain conditional scenarios. Fictional premises remain labeled fiction. Cybersecurity topics stay within defensive, authorized and non-abusive scope; the research outline supplies no operational intrusion guide. Hazardous engineering subjects remain explanatory and require qualified domain review before any procedural content.

## Verification scope

Checks cover the taxonomy's 550 identities, generated-file freshness, counts, stable-ID uniqueness, category prerequisite references/cycles, the three pilots' assigned angles, unassigned-angle status in all 547 new maps, outline presence, proposed status, empty verified-source lists, series references, neighbor references and new navigation links. Scoped checks also compare the original three production status records with their downloaded baseline and verify patch application.

The full repository, all angle plans and production outputs were not downloaded, so full repository validation and production tests are not claimed. Structural checks cannot establish factual accuracy, exhaustive subject coverage, complete semantic uniqueness, real search demand or editorial quality. The all-niche index is a truthful first-pass progress map, not a completion certificate.

## GitHub delivery

The inspected main branch is commit `751dc234534e9eea18fe022b831ed0da5630fe53`. The connected GitHub integration previously returned HTTP 403, `Resource not accessible by integration`, for branch creation. Public visibility supplies read access; it does not grant write authority. This package does not contain a remote commit or pull request. Do not put access tokens in catalog files, patch files, prompts or chat messages. Direct delivery requires an appropriately authorized GitHub connection or a repository checkout with securely configured write access.
