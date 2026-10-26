# 336 — Digital Biology: main topic bank

Updated: 2026-10-23 · **12 active BANK proposals · 6 categories · 10 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Simulation](#catalog-336-r01).
- **Intermediate:** [Multiscale integration](#catalog-336-r02) → [Prediction](#catalog-336-r03) → [Protein structures](#catalog-336-r05) → [Single-cell atlases](#catalog-336-r06).
- **Advanced:** [Digital twins](#catalog-336-r04) → [Digital pathology](#catalog-336-r07) → [Data provenance](#catalog-336-r08) → [Genomic data](#catalog-336-r09) → [Experimental feedback](#catalog-336-r10).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Models](#domain-336-01) | 1 | 1 | 1 |
| [Data](#domain-336-02) | 0 | 3 | 0 |
| [Applications](#domain-336-03) | 0 | 1 | 0 |
| [Validation](#domain-336-04) | 0 | 0 | 2 |
| [Laboratories](#domain-336-05) | 0 | 0 | 2 |
| [Privacy](#domain-336-06) | 0 | 0 | 1 |

<a id="domain-336-01"></a>
## Category: Models

<a id="catalog-336-r01"></a>
### Simulation

Subcategory `CATALOG-336-R01` · foundation.

<a id="bank-336-030"></a>
#### BANK-336-030 — How is a digital model of a cell different from a complete digital cell?

**Individual coverage scope:** Distinguish selected mechanisms, parameters, boundary conditions and validation rather than implying biological completeness.

<a id="catalog-336-r05"></a>
### Protein structures

Subcategory `CATALOG-336-R05` · intermediate.

<a id="bank-336-034"></a>
#### BANK-336-034 — Why does predicting a protein's structure not fully explain what it does in a cell?

**Individual coverage scope:** Compare conformations, interactions, environment, dynamics and experimental validation.

<a id="catalog-336-r10"></a>
### Experimental feedback

Subcategory `CATALOG-336-R10` · advanced.

<a id="bank-336-039"></a>
#### BANK-336-039 — How can an automated laboratory test a biological model without simply repeating the model's training conditions?

**Individual coverage scope:** Compare experiment selection, perturbations, calibration, held-out conditions, negative results and model revision; distinguish a closed experimental loop from proven mechanistic understanding.


<a id="domain-336-02"></a>
## Category: Data

<a id="catalog-336-r02"></a>
### Multiscale integration

Subcategory `CATALOG-336-R02` · intermediate.

<a id="bank-336-031"></a>
#### BANK-336-031 — Why is combining molecular and organism-level biological data difficult?

**Individual coverage scope:** Compare scale, timing, measurement methods, missing variables and inconsistent labels.

<a id="catalog-336-r06"></a>
### Single-cell atlases

Subcategory `CATALOG-336-R06` · intermediate.

<a id="bank-336-035"></a>
#### BANK-336-035 — How can a single-cell atlas describe tissue diversity without recording every cell state?

**Individual coverage scope:** Compare sampling, dissociation, sequencing depth, clustering and annotation uncertainty.

<a id="bank-336-041"></a>
#### BANK-336-041 — What could the 2022 Tabula Sapiens atlas compare across organs sampled from the same donors?

**Individual coverage scope:** Examine its coordinated single-cell transcriptomic collection across 24 tissues and organs, cell annotation and donor limits; distinguish a sampled reference atlas from an exhaustive human cell catalog.

**Research follow-up:** [Bounded case and source-access note](336_DIGITAL_BIOLOGY_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-336-035](#bank-336-035) — Named multi-organ atlas and donor sampling versus atlas completeness in general.

**Neighboring scope:** [BANK-154-030](../154_microbiology/IN_DEPTH_TOPIC_BANK.md#bank-154-030) — Human cell transcriptomes versus microbial biology.


<a id="domain-336-03"></a>
## Category: Applications

<a id="catalog-336-r03"></a>
### Prediction

Subcategory `CATALOG-336-R03` · intermediate.

<a id="bank-336-032"></a>
#### BANK-336-032 — How can a biological model predict well while explaining mechanisms poorly?

**Individual coverage scope:** Separate statistical fit, causal structure, out-of-distribution tests and mechanistic evidence.


<a id="domain-336-04"></a>
## Category: Validation

<a id="catalog-336-r04"></a>
### Digital twins

Subcategory `CATALOG-336-R04` · advanced.

<a id="bank-336-033"></a>
#### BANK-336-033 — What evidence would justify calling a biological simulation an individual-specific digital twin?

**Individual coverage scope:** Compare calibration, repeated observations, uncertainty and prospective predictions; exclude clinical guidance.

<a id="catalog-336-r07"></a>
### Digital pathology

Subcategory `CATALOG-336-R07` · advanced.

<a id="bank-336-036"></a>
#### BANK-336-036 — Why can a pathology model perform well on one hospital's images and fail elsewhere?

**Individual coverage scope:** Compare scanners, staining, case mix, labels and prospective validation; exclude diagnostic use recommendations.


<a id="domain-336-05"></a>
## Category: Laboratories

<a id="catalog-336-r08"></a>
### Data provenance

Subcategory `CATALOG-336-R08` · advanced.

<a id="bank-336-037"></a>
#### BANK-336-037 — Why does a biological model need the history of how its training measurements were produced?

**Individual coverage scope:** Trace samples, instruments, batches, protocols, labels and transformations rather than treating a dataset as context free.

<a id="bank-336-040"></a>
#### BANK-336-040 — What did the Human Pangenome Reference Consortium's 2023 draft add beyond a single linear human reference genome?

**Individual coverage scope:** Use the 2023 draft's 47 phased diploid assemblies to examine reference design and variant discovery under that study's evaluation; do not call the draft a complete representation of humanity.

**Research follow-up:** [Bounded case and source-access note](336_DIGITAL_BIOLOGY_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-336-038](#bank-336-038) — Reference representation and variation versus genomic reidentification risk.

**Neighboring scope:** [BANK-155-030](../155_biotechnology/IN_DEPTH_TOPIC_BANK.md#bank-155-030) — Digital reference construction versus biotechnology interventions.


<a id="domain-336-06"></a>
## Category: Privacy

<a id="catalog-336-r09"></a>
### Genomic data

Subcategory `CATALOG-336-R09` · advanced.

<a id="bank-336-038"></a>
#### BANK-336-038 — Why can genomic datasets remain identifying after names are removed?

**Individual coverage scope:** Compare familial relationships, rare variants, linkage, consent and controlled access without reidentification instructions.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-336-010"></a>
### pending_topics/0 — The Architecture of Digital Biology: Biology Becomes Computable

**Original question:** Which dataset or computational method changed a defined biological question?

**Original planning scope:** Use dated repository, method, and study records. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 1 (The Architecture of Digital Biology: Biology Becomes Computable) through: What did the Human Pangenome Reference Consortium's 2023 draft add beyond a single linear human reference genome? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-040](#bank-336-040).

<a id="bank-336-011"></a>
### pending_topics/1 — Digital Biology: A Digital Biology Claim Rechecked

**Original question:** Did one model predict a result later tested experimentally?

**Original planning scope:** Compare prediction, independent experiment, and uncertainty. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 2 (Digital Biology: A Digital Biology Claim Rechecked) through: How can a biological model predict well while explaining mechanisms poorly? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-032](#bank-336-032).

<a id="bank-336-012"></a>
### pending_topics/2 — Digital Biology: People Behind Biological Data

**Original question:** Who collected specimens, annotated records, and maintained repositories?

**Original planning scope:** Trace credit, consent, and data provenance. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 3 (Digital Biology: People Behind Biological Data) through: Why does a biological model need the history of how its training measurements were produced? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-037](#bank-336-037).

<a id="bank-336-013"></a>
### pending_topics/3 — Digital Biology: From Sample to Digital Record

**Original question:** How does a biological specimen become analyzable data?

**Original planning scope:** Trace sampling, measurement, metadata, processing, and interpretation. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 4 (Digital Biology: From Sample to Digital Record) through: Why does a biological model need the history of how its training measurements were produced? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-037](#bank-336-037).

<a id="bank-336-014"></a>
### pending_topics/4 — Digital Biology: Model Versus Living System

**Original question:** Which assumptions make a biological simulation useful or misleading?

**Original planning scope:** Compare predictions with independent observations. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 5 (Digital Biology: Model Versus Living System) through: How is a digital model of a cell different from a complete digital cell? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-030](#bank-336-030).

<a id="bank-336-015"></a>
### pending_topics/5 — Digital Biology: A Dataset Disagreement

**Original question:** Why do two biological datasets disagree?

**Original planning scope:** Check species, sampling, protocol, version, and annotation. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 6 (Digital Biology: A Dataset Disagreement) through: Why does a biological model need the history of how its training measurements were produced? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-037](#bank-336-037).

<a id="bank-336-016"></a>
### pending_topics/6 — Digital Biology: A New Biological Model

**Original question:** Did it improve a named research task?

**Original planning scope:** Test external data, baseline, uncertainty, and laboratory confirmation. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 7 (Digital Biology: A New Biological Model) through: What could the 2022 Tabula Sapiens atlas compare across organs sampled from the same donors? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-041](#bank-336-041).

<a id="bank-336-017"></a>
### pending_topics/7 — Digital Biology: A Data Stewardship Decision

**Original question:** Who decided how biological records would be shared?

**Original planning scope:** Examine contributors, communities, access, and attribution. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 8 (Digital Biology: A Data Stewardship Decision) through: Why can genomic datasets remain identifying after names are removed? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-038](#bank-336-038).

<a id="bank-336-018"></a>
### pending_topics/8 — Digital Biology: A Repository or Method Release

**Original question:** What became possible after one data or software release?

**Original planning scope:** Use dated availability and independent reuse evidence. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 9 (Digital Biology: A Repository or Method Release) through: What did the Human Pangenome Reference Consortium's 2023 draft add beyond a single linear human reference genome? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-040](#bank-336-040).

<a id="bank-336-019"></a>
### pending_topics/9 — Digital Biology: A Computational Biology Pipeline

**Original question:** How are raw observations cleaned, analyzed, and interpreted?

**Original planning scope:** Trace a named dataset and versioned workflow. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 10 (Digital Biology: A Computational Biology Pipeline) through: Why does a biological model need the history of how its training measurements were produced? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-037](#bank-336-037).

<a id="bank-336-020"></a>
### pending_topics/10 — Digital Biology: A Biological Hypothesis Reassessed

**Original question:** What new data or method changed confidence?

**Original planning scope:** Compare original and later evidence without claiming universal reversal. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 11 (Digital Biology: A Biological Hypothesis Reassessed) through: How can a biological model predict well while explaining mechanisms poorly? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-032](#bank-336-032).

<a id="bank-336-021"></a>
### pending_topics/11 — Digital Biology: One Question Across Data Generations

**Original question:** Did additional resolution improve biological inference?

**Original planning scope:** Match organism, sampling, outcome, and measurement method. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 12 (Digital Biology: One Question Across Data Generations) through: What did the Human Pangenome Reference Consortium's 2023 draft add beyond a single linear human reference genome? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-040](#bank-336-040).

<a id="bank-336-022"></a>
### pending_topics/12 — Digital Biology: A Proposed Digital Biology Tool

**Original question:** What would validate usefulness beyond training data?

**Original planning scope:** Require external samples, mechanistic checks, and practical outcome. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 13 (Digital Biology: A Proposed Digital Biology Tool) through: How can an automated laboratory test a biological model without simply repeating the model's training conditions? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-039](#bank-336-039).

<a id="bank-336-023"></a>
### pending_topics/13 — Digital Biology: A Model Replaces Experiments?

**Original question:** Which predictions still need observation or intervention?

**Original planning scope:** Separate computational plausibility from biological confirmation. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 14 (Digital Biology: A Model Replaces Experiments?) through: How can an automated laboratory test a biological model without simply repeating the model's training conditions? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-039](#bank-336-039).

<a id="bank-336-024"></a>
### pending_topics/14 — Digital Biology: A Dataset's Journey

**Original question:** How did a specimen and its records reach a published result?

**Original planning scope:** Follow consent, metadata, analysis, and reanalysis. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 15 (Digital Biology: A Dataset's Journey) through: Why does a biological model need the history of how its training measurements were produced? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-037](#bank-336-037).

<a id="bank-336-025"></a>
### pending_topics/15 — Digital Biology: From Record to Biological Account

**Original question:** Which measurements support an explanation rather than correlation?

**Original planning scope:** Trace specimen, instrument, model, and independent evidence. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 16 (Digital Biology: From Record to Biological Account) through: Why is combining molecular and organism-level biological data difficult? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-031](#bank-336-031).

<a id="bank-336-026"></a>
### pending_topics/16 — Digital Biology: How Biological Data Are Measured

**Original question:** Which sampling and instrument choices shape a digital record?

**Original planning scope:** Report protocol, calibration, metadata, and error. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 17 (Digital Biology: How Biological Data Are Measured) through: Why does a biological model need the history of how its training measurements were produced? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-037](#bank-336-037).

<a id="bank-336-027"></a>
### pending_topics/17 — Digital Biology: Scale Changes an Inference

**Original question:** Does a finding hold across molecule, organism, population, or ecosystem?

**Original planning scope:** Define scale and observation period. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 18 (Digital Biology: Scale Changes an Inference) through: Why is combining molecular and organism-level biological data difficult? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-031](#bank-336-031).

<a id="bank-336-028"></a>
### pending_topics/18 — Digital Biology: Digital Prediction Meets Living Context

**Original question:** Does a laboratory or computational result persist in the field?

**Original planning scope:** Compare conditions, controls, and measured outcome. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 19 (Digital Biology: Digital Prediction Meets Living Context) through: Why does predicting a protein's structure not fully explain what it does in a cell? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-034](#bank-336-034).

<a id="bank-336-029"></a>
### pending_topics/19 — Digital Biology: Variation Beyond the Reference

**Original question:** Which organisms or populations differ from a reference dataset?

**Original planning scope:** Check sampling, taxonomy, and uncertainty. Evidence base: versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 20 (Digital Biology: Variation Beyond the Reference) through: What did the Human Pangenome Reference Consortium's 2023 draft add beyond a single linear human reference genome? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-040](#bank-336-040).

### trending_topics/0 — Digital Biology: An Outlier That Tests the Model

**Editorial disposition:** merge_existing. Existing question covers archived pitch 21 (Digital Biology: An Outlier That Tests the Model) through: How can a biological model predict well while explaining mechanisms poorly? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-032](#bank-336-032).

### trending_topics/1 — Digital Biology: A Dataset Disagreement

**Editorial disposition:** merge_existing. Existing question covers archived pitch 22 (Digital Biology: A Dataset Disagreement) through: Why does a biological model need the history of how its training measurements were produced? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-037](#bank-336-037).

### trending_topics/2 — Digital Biology: A New Biological Model

**Editorial disposition:** new_case. Named sourced case covers archived pitch 23 (Digital Biology: A New Biological Model) through: What could the 2022 Tabula Sapiens atlas compare across organs sampled from the same donors? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-041](#bank-336-041).

### trending_topics/3 — Digital Biology: A Model Replaces Experiments?

**Editorial disposition:** merge_existing. Existing question covers archived pitch 24 (Digital Biology: A Model Replaces Experiments?) through: How can an automated laboratory test a biological model without simply repeating the model's training conditions? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-039](#bank-336-039).

### trending_topics/4 — Digital Biology: A Repository or Method Release

**Editorial disposition:** new_case. Named sourced case covers archived pitch 25 (Digital Biology: A Repository or Method Release) through: What did the Human Pangenome Reference Consortium's 2023 draft add beyond a single linear human reference genome? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-040](#bank-336-040).

### trending_topics/5 — Digital Biology: People Behind Biological Data

**Editorial disposition:** merge_existing. Existing question covers archived pitch 26 (Digital Biology: People Behind Biological Data) through: Why does a biological model need the history of how its training measurements were produced? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-037](#bank-336-037).

### trending_topics/6 — Digital Biology: A Dataset's Journey

**Editorial disposition:** merge_existing. Existing question covers archived pitch 27 (Digital Biology: A Dataset's Journey) through: Why does a biological model need the history of how its training measurements were produced? Original wording is retained in topics_status.json; it does not establish a superlative or production readiness.

**Scoped proposals:** [BANK-336-037](#bank-336-037).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-336-01"></a>
### Computational biology

<a id="bank-336-001"></a>
- `BANK-336-001` — Protein structure prediction → [BANK-336-034](#bank-336-034)
<a id="bank-336-002"></a>
- `BANK-336-002` — Single-cell atlas construction → [BANK-336-035](#bank-336-035)
<a id="bank-336-003"></a>
- `BANK-336-003` — Digital pathology models → [BANK-336-036](#bank-336-036)

<a id="catalog-336-02"></a>
### Modeling

<a id="bank-336-004"></a>
- `BANK-336-004` — Biological network simulation → [BANK-336-030](#bank-336-030)
<a id="bank-336-005"></a>
- `BANK-336-005` — Data integration across assays → [BANK-336-031](#bank-336-031)
<a id="bank-336-006"></a>
- `BANK-336-006` — Lab automation data provenance → [BANK-336-037](#bank-336-037)

<a id="catalog-336-03"></a>
### Validation

<a id="bank-336-007"></a>
- `BANK-336-007` — Out-of-distribution biological predictions → [BANK-336-032](#bank-336-032)
<a id="bank-336-008"></a>
- `BANK-336-008` — Experimental confirmation → [BANK-336-032](#bank-336-032)
<a id="bank-336-009"></a>
- `BANK-336-009` — Privacy of genomic datasets → [BANK-336-038](#bank-336-038)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [027 Genetics & Evolution](../027_genetics_evolution/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [154 Microbiology](../154_microbiology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [155 Biotechnology](../155_biotechnology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [350 Biology](../350_biology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [353 Disease Science](../353_disease_science/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [354 Evolution](../354_evolution/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/336_digital_biology/NICHE_336_digital_biology.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
