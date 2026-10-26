# 337 — AI Research: main topic bank

Updated: 2026-10-23 · **13 active BANK proposals · 8 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Research claims](#catalog-337-r01).
- **Intermediate:** [Ablations](#catalog-337-r02) → [Contamination](#catalog-337-r03) → [Self-supervision](#catalog-337-r05).
- **Advanced:** [Scaling](#catalog-337-r04) → [Explanations](#catalog-337-r06) → [Distribution shift](#catalog-337-r07) → [Generative likelihood](#catalog-337-r08) → [Reinforcement learning](#catalog-337-r09) → [Compute comparisons](#catalog-337-r10) → [Benchmark retirement](#catalog-337-r11).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Methods](#domain-337-01) | 2 | 0 | 0 |
| [Experiments](#domain-337-02) | 0 | 1 | 0 |
| [Evaluation](#domain-337-03) | 0 | 1 | 4 |
| [Reproducibility](#domain-337-04) | 0 | 0 | 1 |
| [Learning](#domain-337-05) | 0 | 1 | 0 |
| [Interpretability](#domain-337-06) | 0 | 0 | 1 |
| [Objectives](#domain-337-07) | 0 | 0 | 1 |
| [Efficiency](#domain-337-08) | 0 | 0 | 1 |

<a id="domain-337-01"></a>
## Category: Methods

<a id="catalog-337-r01"></a>
### Research claims

Subcategory `CATALOG-337-R01` · foundation.

<a id="bank-337-030"></a>
#### BANK-337-030 — What separates an AI research benchmark result from a general intelligence claim?

**Individual coverage scope:** Compare task definition, data, metric, baselines and uncertainty without accepting a headline as a finding.

<a id="bank-337-041"></a>
#### BANK-337-041 — What did the 2012 AlexNet ImageNet paper actually establish about a deep convolutional model?

**Individual coverage scope:** Read the original ImageNet classification setup, model description and reported benchmark errors as a dated result; do not infer general visual understanding or sole-cause historical impact.

**Research follow-up:** [Bounded case and source-access note](337_AI_RESEARCH_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-337-030](#bank-337-030) — Named 2012 image-classification result versus general intelligence claims from benchmarks.

**Neighboring scope:** [BANK-001-157](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-157) — Research result and evaluation versus technical explanation of Transformer self-attention.


<a id="domain-337-02"></a>
## Category: Experiments

<a id="catalog-337-r02"></a>
### Ablations

Subcategory `CATALOG-337-R02` · intermediate.

<a id="bank-337-031"></a>
#### BANK-337-031 — How can an ablation study reveal which part of an AI system mattered?

**Individual coverage scope:** Compare matched conditions, interaction effects, compute budgets and repeated runs.


<a id="domain-337-03"></a>
## Category: Evaluation

<a id="catalog-337-r03"></a>
### Contamination

Subcategory `CATALOG-337-R03` · intermediate.

<a id="bank-337-032"></a>
#### BANK-337-032 — Why can training-data overlap inflate an AI model's apparent ability?

**Individual coverage scope:** Trace leakage, memorization, evaluation design and held-out controls conceptually.

<a id="catalog-337-r07"></a>
### Distribution shift

Subcategory `CATALOG-337-R07` · advanced.

<a id="bank-337-036"></a>
#### BANK-337-036 — Why can an AI system's accuracy collapse when the test environment changes slightly?

**Individual coverage scope:** Trace shortcut features, population shifts, labeling and stress tests without assuming every shift causes failure.

<a id="bank-337-042"></a>
#### BANK-337-042 — How did the 2021 WILDS benchmark make distribution shifts visible across its selected datasets?

**Individual coverage scope:** Examine WILDS's curated 10 datasets and in- versus out-of-distribution evaluation; distinguish its chosen domains and model baselines from all deployed AI systems.

**Research follow-up:** [Bounded case and source-access note](337_AI_RESEARCH_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-337-036](#bank-337-036) — A named 2021 shift benchmark versus the general phenomenon of model accuracy under environment change.

**Neighboring scope:** [BANK-336-036](../336_digital_biology/IN_DEPTH_TOPIC_BANK.md#bank-336-036) — General multi-domain benchmark design versus pathology images across hospitals specifically.

<a id="catalog-337-r09"></a>
### Reinforcement learning

Subcategory `CATALOG-337-R09` · advanced.

<a id="bank-337-038"></a>
#### BANK-337-038 — Why can a reinforcement-learning agent maximize its reward without fulfilling the intended task?

**Individual coverage scope:** Compare reward specification, environment, shortcuts and independent evaluation in a benign toy example.

<a id="catalog-337-r11"></a>
### Benchmark retirement

Subcategory `CATALOG-337-R11` · advanced.

<a id="bank-337-040"></a>
#### BANK-337-040 — When should an AI benchmark be revised or retired after repeated public use?

**Individual coverage scope:** Compare contamination, saturation, gaming, task relevance, comparability and replacement costs; retain historical results without interpreting every score gain as new capability.


<a id="domain-337-04"></a>
## Category: Reproducibility

<a id="catalog-337-r04"></a>
### Scaling

Subcategory `CATALOG-337-R04` · advanced.

<a id="bank-337-033"></a>
#### BANK-337-033 — What must be reported before an AI scaling result can be independently assessed?

**Individual coverage scope:** Compare dataset construction, compute, optimization, runs, uncertainty and access limits; exclude claims of replication.


<a id="domain-337-05"></a>
## Category: Learning

<a id="catalog-337-r05"></a>
### Self-supervision

Subcategory `CATALOG-337-R05` · intermediate.

<a id="bank-337-034"></a>
#### BANK-337-034 — How can an AI model learn useful representations from data without task-specific human labels?

**Individual coverage scope:** Compare pretext objectives, data structure, representations and downstream evaluation; distinguish no task labels from no human influence.


<a id="domain-337-06"></a>
## Category: Interpretability

<a id="catalog-337-r06"></a>
### Explanations

Subcategory `CATALOG-337-R06` · advanced.

<a id="bank-337-035"></a>
#### BANK-337-035 — How can an AI explanation sound plausible without describing the model's actual decision process?

**Individual coverage scope:** Compare faithfulness, perturbation tests, alternative explanations and human judgment.


<a id="domain-337-07"></a>
## Category: Objectives

<a id="catalog-337-r08"></a>
### Generative likelihood

Subcategory `CATALOG-337-R08` · advanced.

<a id="bank-337-037"></a>
#### BANK-337-037 — Why can a generative model's likelihood score disagree with perceived output quality?

**Individual coverage scope:** Compare representation, metric, distribution, sampling and human evaluation without declaring one measure sufficient.


<a id="domain-337-08"></a>
## Category: Efficiency

<a id="catalog-337-r10"></a>
### Compute comparisons

Subcategory `CATALOG-337-R10` · advanced.

<a id="bank-337-039"></a>
#### BANK-337-039 — Why do AI research comparisons need matched compute budgets as well as matched datasets?

**Individual coverage scope:** Compare training, search, inference, hardware and repeated runs without equating fewer parameters with lower total cost.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-337-010"></a>
### pending_topics/0 — The Architecture of AI Research: A Research Method Emerges

**Original question:** Which dated experiment established a narrow AI technique?

**Original planning scope:** Read original method, baseline, and replication. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 1 (The Architecture of AI Research: A Research Method Emerges) through: What did the 2012 AlexNet ImageNet paper actually establish about a deep convolutional model? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-041](#bank-337-041).

<a id="bank-337-011"></a>
### pending_topics/1 — AI Research: A Benchmark Result Rechecked

**Original question:** Does a celebrated score transfer to a useful task?

**Original planning scope:** Compare dataset, contamination risk, metric, and field test. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 2 (AI Research: A Benchmark Result Rechecked) through: What separates an AI research benchmark result from a general intelligence claim? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-030](#bank-337-030).

<a id="bank-337-012"></a>
### pending_topics/2 — AI Research: Research Labor Behind a Model

**Original question:** Who labels data, maintains infrastructure, and reproduces results?

**Original planning scope:** Credit contributors and examine conditions. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 3 (AI Research: Research Labor Behind a Model) through: Why do AI research comparisons need matched compute budgets as well as matched datasets? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-039](#bank-337-039).

<a id="bank-337-013"></a>
### pending_topics/3 — AI Research: From Question to AI Experiment

**Original question:** How do hypothesis, data, baseline, model, and evaluation fit?

**Original planning scope:** Trace a published study without assuming its claim is true. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 4 (AI Research: From Question to AI Experiment) through: How can an ablation study reveal which part of an AI system mattered? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-031](#bank-337-031).

<a id="bank-337-014"></a>
### pending_topics/4 — AI Research: Generalization Beyond a Test Set

**Original question:** What evidence supports performance outside training conditions?

**Original planning scope:** Use independent split, shift, and uncertainty measures. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 5 (AI Research: Generalization Beyond a Test Set) through: How did the 2021 WILDS benchmark make distribution shifts visible across its selected datasets? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-042](#bank-337-042).

<a id="bank-337-015"></a>
### pending_topics/5 — AI Research: A Result That Would Not Replicate

**Original question:** Which data, code, compute, or metric differences explain divergence?

**Original planning scope:** Compare public artifacts and unresolved gaps. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 6 (AI Research: A Result That Would Not Replicate) through: Why can training-data overlap inflate an AI model's apparent ability? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-032](#bank-337-032).

<a id="bank-337-016"></a>
### pending_topics/6 — AI Research: A New Model Architecture

**Original question:** Which capability improved under equal evaluation?

**Original planning scope:** Control data, compute, metric, and baseline. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 7 (AI Research: A New Model Architecture) through: What did the 2012 AlexNet ImageNet paper actually establish about a deep convolutional model? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-041](#bank-337-041).

<a id="bank-337-017"></a>
### pending_topics/7 — AI Research: A Research Dispute

**Original question:** How did teams argue over one claim or method?

**Original planning scope:** Read papers, critiques, responses, and replications. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 8 (AI Research: A Research Dispute) through: Why do AI research comparisons need matched compute budgets as well as matched datasets? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-039](#bank-337-039).

<a id="bank-337-018"></a>
### pending_topics/8 — AI Research: An AI Paper's Impact

**Original question:** Which follow-up studies confirmed, limited, or rejected it?

**Original planning scope:** Build dated citation and replication trail. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 9 (AI Research: An AI Paper's Impact) through: What did the 2012 AlexNet ImageNet paper actually establish about a deep convolutional model? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-041](#bank-337-041).

<a id="bank-337-019"></a>
### pending_topics/9 — AI Research: A Research Pipeline

**Original question:** How are data, training, validation, and reporting connected?

**Original planning scope:** Follow a named experiment and versioned artifacts. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 10 (AI Research: A Research Pipeline) through: How can an ablation study reveal which part of an AI system mattered? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-031](#bank-337-031).

<a id="bank-337-020"></a>
### pending_topics/10 — AI Research: A Benchmark Becomes Obsolete

**Original question:** Which saturation, leakage, or task mismatch changed its value?

**Original planning scope:** Compare original purpose with later use. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 11 (AI Research: A Benchmark Becomes Obsolete) through: When should an AI benchmark be revised or retired after repeated public use? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-040](#bank-337-040).

<a id="bank-337-021"></a>
### pending_topics/11 — AI Research: A Capability Across Model Generations

**Original question:** Did progress persist under matched tests?

**Original planning scope:** Control prompt, data access, tools, budget, and scoring. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 12 (AI Research: A Capability Across Model Generations) through: How did the 2021 WILDS benchmark make distribution shifts visible across its selected datasets? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-042](#bank-337-042).

<a id="bank-337-022"></a>
### pending_topics/12 — AI Research: A Promised Research Direction

**Original question:** What falsifiable test would support the proposal?

**Original planning scope:** State hypotheses, resource assumptions, and failure criteria. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 13 (AI Research: A Promised Research Direction) through: What did the 2012 AlexNet ImageNet paper actually establish about a deep convolutional model? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-041](#bank-337-041).

<a id="bank-337-023"></a>
### pending_topics/13 — AI Research: One Score Means General Intelligence?

**Original question:** Which tasks and populations lie outside the benchmark?

**Original planning scope:** Inspect evaluation scope and uncertainty. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 14 (AI Research: One Score Means General Intelligence?) through: What separates an AI research benchmark result from a general intelligence claim? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-030](#bank-337-030).

<a id="bank-337-024"></a>
### pending_topics/14 — AI Research: A Claim from Preprint to Replication

**Original question:** How did the evidence change through review and reuse?

**Original planning scope:** Follow dated versions and independent tests. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 15 (AI Research: A Claim from Preprint to Replication) through: Why can training-data overlap inflate an AI model's apparent ability? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-032](#bank-337-032).

<a id="bank-337-025"></a>
### pending_topics/15 — AI Research: Model or Whole System?

**Original question:** Which results depend on retrieval, tools, humans, or prompt design?

**Original planning scope:** Draw inference and evaluation boundaries. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 16 (AI Research: Model or Whole System?) through: What separates an AI research benchmark result from a general intelligence claim? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-030](#bank-337-030).

<a id="bank-337-026"></a>
### pending_topics/16 — AI Research: One Evaluated Example

**Original question:** What input, context, output, and grading produced a score?

**Original planning scope:** Record protocol while protecting restricted test data. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 17 (AI Research: One Evaluated Example) through: What separates an AI research benchmark result from a general intelligence claim? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-030](#bank-337-030).

<a id="bank-337-027"></a>
### pending_topics/17 — AI Research: Scale Versus Data Quality

**Original question:** Which investment improved the target outcome?

**Original planning scope:** Compare controlled experiments and costs. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 18 (AI Research: Scale Versus Data Quality) through: Why do AI research comparisons need matched compute budgets as well as matched datasets? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-039](#bank-337-039).

<a id="bank-337-028"></a>
### pending_topics/18 — AI Research: A Model's Systematic Error

**Original question:** What conditions reveal a repeatable failure?

**Original planning scope:** Use benign, representative tests and report frequency. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 19 (AI Research: A Model's Systematic Error) through: Why can an AI system's accuracy collapse when the test environment changes slightly? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-036](#bank-337-036).

<a id="bank-337-029"></a>
### pending_topics/19 — AI Research: The Missing Evaluation Population

**Original question:** Who or what was absent from the test?

**Original planning scope:** Inspect dataset construction and external validity. Evidence base: original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 20 (AI Research: The Missing Evaluation Population) through: How did the 2021 WILDS benchmark make distribution shifts visible across its selected datasets? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-042](#bank-337-042).

### trending_topics/0 — AI Research: Record Extremes & Superlatives

**Editorial disposition:** merge_existing. Existing question covers archived pitch 21 (AI Research: Record Extremes & Superlatives) through: What separates an AI research benchmark result from a general intelligence claim? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-030](#bank-337-030).

### trending_topics/1 — AI Research: A Result That Would Not Replicate

**Editorial disposition:** merge_existing. Existing question covers archived pitch 22 (AI Research: A Result That Would Not Replicate) through: Why can training-data overlap inflate an AI model's apparent ability? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-032](#bank-337-032).

### trending_topics/2 — AI Research: A New Model Architecture

**Editorial disposition:** new_case. Named sourced case covers archived pitch 23 (AI Research: A New Model Architecture) through: What did the 2012 AlexNet ImageNet paper actually establish about a deep convolutional model? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-041](#bank-337-041).

### trending_topics/3 — AI Research: One Score Means General Intelligence?

**Editorial disposition:** merge_existing. Existing question covers archived pitch 24 (AI Research: One Score Means General Intelligence?) through: What separates an AI research benchmark result from a general intelligence claim? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-030](#bank-337-030).

### trending_topics/4 — AI Research: An AI Paper's Impact

**Editorial disposition:** new_case. Named sourced case covers archived pitch 25 (AI Research: An AI Paper's Impact) through: What did the 2012 AlexNet ImageNet paper actually establish about a deep convolutional model? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-041](#bank-337-041).

### trending_topics/5 — AI Research: Research Labor Behind a Model

**Editorial disposition:** merge_existing. Existing question covers archived pitch 26 (AI Research: Research Labor Behind a Model) through: Why do AI research comparisons need matched compute budgets as well as matched datasets? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-039](#bank-337-039).

### trending_topics/6 — AI Research: A Claim from Preprint to Replication

**Editorial disposition:** merge_existing. Existing question covers archived pitch 27 (AI Research: A Claim from Preprint to Replication) through: Why can training-data overlap inflate an AI model's apparent ability? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-337-032](#bank-337-032).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-337-01"></a>
### Learning methods

<a id="bank-337-001"></a>
- `BANK-337-001` — Self-supervised objectives → [BANK-337-034](#bank-337-034)
<a id="bank-337-002"></a>
- `BANK-337-002` — Reinforcement learning evaluation → [BANK-337-038](#bank-337-038)
<a id="bank-337-003"></a>
- `BANK-337-003` — Generative model likelihood → [BANK-337-037](#bank-337-037)

<a id="catalog-337-02"></a>
### Research design

<a id="bank-337-004"></a>
- `BANK-337-004` — Ablation studies → [BANK-337-031](#bank-337-031)
<a id="bank-337-005"></a>
- `BANK-337-005` — Reproducibility of training runs → [BANK-337-033](#bank-337-033)
<a id="bank-337-006"></a>
- `BANK-337-006` — Compute-normalized comparisons → [BANK-337-039](#bank-337-039)

<a id="catalog-337-03"></a>
### Limits

<a id="bank-337-007"></a>
- `BANK-337-007` — Data contamination → [BANK-337-032](#bank-337-032)
<a id="bank-337-008"></a>
- `BANK-337-008` — Robustness under distribution shift → [BANK-337-036](#bank-337-036)
<a id="bank-337-009"></a>
- `BANK-337-009` — Interpretability versus explanation plausibility → [BANK-337-035](#bank-337-035)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [001 AI + Technology Explainers](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [007 AI Tools / AI Tutorials](../007_ai_tools_ai_tutorials/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [338 Developer AI](../338_developer_ai/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [531 AI Software Agents](../531_ai_software_agents/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [532 Large Language Model Systems](../532_large_language_model_systems/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/337_ai_research/NICHE_337_ai_research.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
