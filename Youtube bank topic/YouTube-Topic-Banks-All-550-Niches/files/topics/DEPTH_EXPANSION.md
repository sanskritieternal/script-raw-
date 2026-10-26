# In-depth niche expansion: batch 1

Later coverage: [all 550 niche banks](./ALL_NICHE_TOPIC_BANKS.md) and [the all-niche expansion method](./ALL_NICHE_EXPANSION_GUIDE.md). This document retains the original three-niche pilot record.

Updated: 2026-10-22. Scope: **278 Meditation, 279 Pranayama, 280 Yoga**. This batch drafts 360 specific YouTube episode questions in 60 subject categories. The other 547 niche folders are outside this batch. This catalog is a starting coverage map, not an assertion of exhaustive coverage or verified research.

| Niche | Categories | Specific episode proposals | Catalog |
|---|---:|---:|---|
| 278 Meditation | 20 | 120 | [Read](./278_meditation/IN_DEPTH_TOPIC_BANK.md) · [Editable JSON](./278_meditation/IN_DEPTH_TOPIC_BANK.json) |
| 279 Pranayama | 20 | 120 | [Read](./279_pranayama/IN_DEPTH_TOPIC_BANK.md) · [Editable JSON](./279_pranayama/IN_DEPTH_TOPIC_BANK.json) |
| 280 Yoga | 20 | 120 | [Read](./280_yoga/IN_DEPTH_TOPIC_BANK.md) · [Editable JSON](./280_yoga/IN_DEPTH_TOPIC_BANK.json) |
| **Batch total** | **60** | **360** | **12 suggested six-episode learning sequences** |

## What the hierarchy means

**Niche → subject category → detailed subtopics/coverage → specific video question.**

For example, Meditation → Japa and mantra contemplation → audible, whispered and mental repetition → “Spoken, whispered, and mental japa: how does one tradition distinguish them?” The coverage boundary asks for a named manual and teacher account. This is substantially narrower than a reusable angle such as history or beginner explanation.

Each proposal has a stable `BANK-<niche>-<number>` ID, a concrete question, a distinct coverage boundary, a registered angle, proposed status and an empty verified-source list. Categories have learning levels, prerequisites and tailored research profiles. The learning levels organize viewing and research; they never prescribe a physical practice progression.

The four suggested series per niche provide an editorial viewing order and learning outcome. They are not the registered `SER-*` objects used in the formal planning system. Repeated concepts across neighboring banks are allowed only when their questions differ: Yoga covers pranayama's place in a system; Pranayama covers particular breath methods; Meditation covers attention and contemplative experience. This relationship is documented in all three banks.

## Editing and generation

`IN_DEPTH_TOPIC_BANK.json` is the editable source for each bank. `IN_DEPTH_TOPIC_BANK.md` is its generated reading view. Existing roadmaps, reports and the central index link to these banks. Each existing `topics_status.json` has an additive `in_depth_topic_bank` field, with `counts_in_production_summary: false`.

The existing 20 queued items, seven legacy trend candidates and completed-topic arrays are preserved. The bank's 120 entries are not added to those totals: existing questions may overlap them, and source feasibility has not been assessed for each new proposal. Legacy trend scores are not validated by this batch and should not be presented as current demand evidence. The existing report's “Last Synced” date still refers to its old production queue; the expansion has its own date.

Run from the repository root:

```bash
python Scripts/render_topic_banks.py --write
python Scripts/render_topic_banks.py --check
```

The renderer discovers all `topics/*/IN_DEPTH_TOPIC_BANK.json` files. It checks identities, counts, duplicate IDs/questions within a bank, learning levels, prerequisite references/cycles, registered angles, series membership and generated-view freshness. It intentionally imposes no fixed category or topic count. These checks do not establish historical accuracy, medical efficacy, semantic uniqueness, comprehensive coverage or human editorial approval.

When extending the catalog, retain IDs for revised questions, add new IDs for genuinely new questions, and update the bank counts. Select actual cases before producing episodes: an edition, institution, study, population or product version must replace any deliberate case-selection slot. Do not claim an unspecified source has been inspected.

## Relationship to the existing registry

These files are browsing catalogs under the existing `topics/` tree. They introduce no new niche identity, CAT defaults, Q numbers or competing executable registry. They are not formal `Planning/DEPTH_PLAN.json` or `IDEA_BANK.json` files, and no entry is `ready_for_project`.

To develop a selected question:

1. Resolve its exact subject and primary niche; check neighboring catalogs for an overlapping episode.
2. Read the existing [depth planning guide](../REGISTRY/DEPTH_PLANNING_GUIDE.md), [idea guide](../REGISTRY/IDEA_BANK_GUIDE.md) and niche angle scope.
3. Inspect sources and record genuine feasibility, open gaps and interpretation boundaries. Retain the BANK ID in editorial notes. Create formal TOP/IDEA IDs only through the existing registry workflow when needed.
4. Use the normal readiness gate before selecting an idea for a project. Read the repository-root output configuration when creating a project.
5. Perform claim-level Phase 1 research. Nothing in this batch bypasses production approval, clinical review, rights checks or later source inspection.

## Source discovery and access notes

The following are orientation leads for future topic-specific research. The access notes record only the resources actually opened on 2026-10-22. They do not verify the 360 questions, inspect every cited study, or update the shared source library. No episode-level source was marked verified.

| Resource | URL | Access observation and intended use |
|---|---|---|
| NCCIH, Meditation and Mindfulness: Effectiveness and Safety | https://www.nccih.nih.gov/health/meditation-and-mindfulness-effectiveness-and-safety | Page opened; used to orient program distinctions, evidence questions and potential-harm coverage. Follow its references to original reports and check current clinical guidance for a selected episode. |
| NCCIH, Yoga: Effectiveness and Safety | https://www.nccih.nih.gov/health/yoga-effectiveness-and-safety | Page opened; used to orient variation among interventions, research limitations and safety coverage. It does not establish that every named style or technique has the same outcomes. |
| IIT Kanpur Gita Supersite entry point | https://www.gitasupersite.iitk.ac.in/ | The entry point redirected to https://heritage.iitk.ac.in/gitasupersite and displayed links for the Gita and Yoga Sutra corpora. Landing-page access does not mean individual verses or commentaries were inspected. |
| Legacy Yoga Sutra endpoint | https://www.gitasupersite.iitk.ac.in/yogasutra_content | Direct access timed out. Select and inspect the actual edition/passage before production; the catalog does not claim passage verification. |
| Common Yoga Protocol, Ministry of Ayush PDF lead | https://yoga.ayush.gov.in/YAP/PDF/Common%20Yoga%20Protocol%20Book-English.pdf | Direct request returned 403. Search located the official resource, but the PDF was not inspected. Obtain an accessible official edition and record its year before using it. |
| Common Yoga Protocol, Ministry of External Affairs PDF mirror lead | https://www.mea.gov.in/images/pdf/common-yoga-protocol.pdf | Direct request also returned 403; not inspected. Do not infer content or current applicability from the filename. |
| ClinicalTrials.gov | https://clinicaltrials.gov/ | Search landing page opened; no trial registration was inspected. Future research must select actual registration IDs and compare protocols, results and publications. |

Primary-text topics require edition, translator/commentator and exact passage locators. Institutional teaching topics require the institution's actual curriculum and dated policies. Historical topics require primary records plus critical historical interpretation. Clinical topics require original studies, protocols and current professional guidance. Product topics require a named version, validation evidence and dated privacy/terms records. Public summaries are discovery aids rather than a replacement for these sources.

## Content boundaries

- Traditional prana, nadi, chakra, liberation and attainment concepts remain attributed interpretations; physiological claims need independent measurement evidence.
- Technique and posture entries are explanatory documentary proposals. They provide no advanced breath-holding ratios, forceful-breathing regimen, individualized exercise prescription or treatment plan.
- Cultural and religious comparisons use named texts and communities. An institutional description does not represent every practitioner or establish an uninterrupted ancient lineage.
- Health titles ask research questions; they do not promise cures, universal benefits or replacement of care. High-risk episode decisions follow the existing production contract.
- Search demand, virality and trend velocity have not been researched. No demand scores or priority promises are invented for this batch.

## Validation record

The batch's scoped checks cover all three new banks and their generated views, all 360 angle assignments against the downloaded current niche angle plans, category prerequisite cycles, the 72 series references, and the additive tracking changes. Changed/new local Markdown links are checked against this batch or the repository paths read during inspection. Existing production queue values are compared with their original downloaded snapshots.

The complete repository and its output projects were not downloaded. Consequently the full repository validation command and production tests are not claimed as run. No production files or registered depth/idea plans are changed by this batch.
