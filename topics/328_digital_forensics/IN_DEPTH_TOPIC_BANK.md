# 328 — Digital Forensics: main topic bank

Updated: 2026-10-23 · **10 active BANK proposals · 9 categories · 9 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Digital traces](#catalog-328-r01) → [Scope](#catalog-328-r08).
- **Intermediate:** [Clock drift](#catalog-328-r02) → [Deleted data](#catalog-328-r03) → [Write blockers](#catalog-328-r05).
- **Advanced:** [Reproducibility](#catalog-328-r04) → [Browser records](#catalog-328-r06) → [Audit logs](#catalog-328-r07) → [Mobile extraction limits](#catalog-328-r09).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-328-01) | 1 | 0 | 0 |
| [Timelines](#domain-328-02) | 0 | 1 | 0 |
| [Evidence](#domain-328-03) | 0 | 1 | 0 |
| [Methods](#domain-328-04) | 0 | 0 | 1 |
| [Acquisition](#domain-328-05) | 0 | 1 | 0 |
| [Artifacts](#domain-328-06) | 0 | 0 | 1 |
| [Cloud evidence](#domain-328-07) | 0 | 0 | 1 |
| [Authority](#domain-328-08) | 1 | 0 | 0 |
| [Interpretation](#domain-328-09) | 0 | 0 | 2 |

<a id="domain-328-01"></a>
## Category: Foundations

<a id="catalog-328-r01"></a>
### Digital traces

Subcategory `CATALOG-328-R01` · foundation.

<a id="bank-328-030"></a>
#### BANK-328-030 — Why is a digital forensic copy different from opening files on a device?

**Individual coverage scope:** Compare preservation, hashes, metadata, chain of custody and authorized scope without bypass instructions.


<a id="domain-328-02"></a>
## Category: Timelines

<a id="catalog-328-r02"></a>
### Clock drift

Subcategory `CATALOG-328-R02` · intermediate.

<a id="bank-328-031"></a>
#### BANK-328-031 — How can investigators build a timeline when device clocks disagree?

**Individual coverage scope:** Trace time zones, clock offsets, logs, synchronization and uncertainty intervals using fictional evidence.


<a id="domain-328-03"></a>
## Category: Evidence

<a id="catalog-328-r03"></a>
### Deleted data

Subcategory `CATALOG-328-R03` · intermediate.

<a id="bank-328-032"></a>
#### BANK-328-032 — What does finding a deleted file establish and what does it not?

**Individual coverage scope:** Distinguish remnants, attribution, timestamps, application behavior and access history; avoid asserting guilt from possession alone.


<a id="domain-328-04"></a>
## Category: Methods

<a id="catalog-328-r04"></a>
### Reproducibility

Subcategory `CATALOG-328-R04` · advanced.

<a id="bank-328-033"></a>
#### BANK-328-033 — How can digital forensic conclusions be independently checked?

**Individual coverage scope:** Compare tool versions, acquisition records, validation, repeatable steps and documented limitations within lawful authorized analysis.


<a id="domain-328-05"></a>
## Category: Acquisition

<a id="catalog-328-r05"></a>
### Write blockers

Subcategory `CATALOG-328-R05` · intermediate.

<a id="bank-328-034"></a>
#### BANK-328-034 — What does a write blocker protect during forensic acquisition and what remains outside its scope?

**Individual coverage scope:** Compare media writes, device behavior, acquisition logs and method validation under authorized analysis.


<a id="domain-328-06"></a>
## Category: Artifacts

<a id="catalog-328-r06"></a>
### Browser records

Subcategory `CATALOG-328-R06` · advanced.

<a id="bank-328-035"></a>
#### BANK-328-035 — Why does a browser artifact not always prove a person deliberately visited a page?

**Individual coverage scope:** Compare redirects, cached resources, background activity, profiles and corroborating evidence using fictional records.


<a id="domain-328-07"></a>
## Category: Cloud evidence

<a id="catalog-328-r07"></a>
### Audit logs

Subcategory `CATALOG-328-R07` · advanced.

<a id="bank-328-036"></a>
#### BANK-328-036 — Why can a cloud audit log record an account action without identifying the human responsible?

**Individual coverage scope:** Compare service identities, shared credentials, API calls, time, logging gaps and independent corroboration in authorized analysis.


<a id="domain-328-08"></a>
## Category: Authority

<a id="catalog-328-r08"></a>
### Scope

Subcategory `CATALOG-328-R08` · foundation.

<a id="bank-328-037"></a>
#### BANK-328-037 — Why must digital forensic authority specify both devices and kinds of data?

**Individual coverage scope:** Compare consent, ownership, warrants, third parties and changing scope conceptually; require jurisdiction-specific legal review before real collection.


<a id="domain-328-09"></a>
## Category: Interpretation

<a id="catalog-328-r09"></a>
### Mobile extraction limits

Subcategory `CATALOG-328-R09` · advanced.

<a id="bank-328-038"></a>
#### BANK-328-038 — Why can two authorized forensic tools extract different artifacts from the same phone image?

**Individual coverage scope:** Compare supported versions, parsing, encrypted data, deleted structures, tool logs and validation samples; exclude bypass instructions or claims that absent artifacts prove absent activity.

<a id="bank-328-039"></a>
#### BANK-328-039 — What did NIST's 2010 UFED mobile extraction test exceptions actually show?

**Individual coverage scope:** Read the named tool-version, device and artifact test matrix in the NIST report; distinguish a failed or truncated tested extraction from a claim that all versions, devices or evidence types fail.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTES/SELECTED_CASES.md). This does not change proposal or production status.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-328-010"></a>
### pending_topics/0 — The Architecture of Digital Forensics: A Digital Evidence Method Emerges

**Original question:** Which technical change created a new evidence problem?

**Original planning scope:** Use dated standards, tools, and cases. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-034](#bank-328-034).

<a id="bank-328-011"></a>
### pending_topics/1 — Digital Forensics: A Famous Digital Trace Rechecked

**Original question:** What does the preserved artifact actually support?

**Original planning scope:** Separate observation, interpretation, and later retelling. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-031](#bank-328-031), [BANK-328-035](#bank-328-035).

<a id="bank-328-012"></a>
### pending_topics/2 — Digital Forensics: Evidence Handlers Behind the Case

**Original question:** Who collected, stored, reviewed, and challenged the record?

**Original planning scope:** Trace documented roles without revealing private material. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-037](#bank-328-037).

<a id="bank-328-013"></a>
### pending_topics/3 — Digital Forensics: From Device to Report

**Original question:** How is digital material preserved and interpreted?

**Original planning scope:** Explain authorization, acquisition, integrity, analysis, and reporting. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-033](#bank-328-033).

<a id="bank-328-014"></a>
### pending_topics/4 — Digital Forensics: A Timestamp's Uncertainty

**Original question:** What can clock settings and system behavior do to an event order?

**Original planning scope:** Compare sources, time zones, and known clock offsets. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-031](#bank-328-031).

<a id="bank-328-015"></a>
### pending_topics/5 — Digital Forensics: An Unexplained File Change

**Original question:** Which hypotheses fit the artifact and which cannot be resolved?

**Original planning scope:** Compare provenance, logs, and missing evidence. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-032](#bank-328-032), [BANK-328-035](#bank-328-035).

<a id="bank-328-016"></a>
### pending_topics/6 — Digital Forensics: A Forensic Tool Validated

**Original question:** Does a new extraction method recover what it claims?

**Original planning scope:** Compare known test data, error rates, and versions. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-038](#bank-328-038), [BANK-328-039](#bank-328-039).

<a id="bank-328-017"></a>
### pending_topics/7 — Digital Forensics: An Expert's Bounded Opinion

**Original question:** Which observations underpin an examiner's conclusion?

**Original planning scope:** Read method, qualifications, counteranalysis, and uncertainty. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-033](#bank-328-033).

<a id="bank-328-018"></a>
### pending_topics/8 — Digital Forensics: A Digital Evidence Turning Point

**Original question:** How did a decision change handling or admissibility?

**Original planning scope:** Use dated court or standards records and jurisdiction. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-037](#bank-328-037).

<a id="bank-328-019"></a>
### pending_topics/9 — Digital Forensics: Preserving One Digital Artifact

**Original question:** What establishes continuity from collection to examination?

**Original planning scope:** Describe documented custody and integrity checks, not access bypass. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-034](#bank-328-034).

<a id="bank-328-020"></a>
### pending_topics/10 — Digital Forensics: An Artifact Becomes Unreliable

**Original question:** How did software or platform change reduce interpretability?

**Original planning scope:** Compare versions, metadata, and validation studies. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-031](#bank-328-031), [BANK-328-032](#bank-328-032).

<a id="bank-328-021"></a>
### pending_topics/11 — Digital Forensics: One Artifact Across Device Generations

**Original question:** What can investigators recover under different systems?

**Original planning scope:** Use authorized test devices and matching data. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-038](#bank-328-038).

<a id="bank-328-022"></a>
### pending_topics/12 — Digital Forensics: A New Evidence Source

**Original question:** What validation is needed before relying on it?

**Original planning scope:** Specify acquisition, error, retention, and interpretive limits. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-036](#bank-328-036).

<a id="bank-328-023"></a>
### pending_topics/13 — Digital Forensics: Metadata Tells the Whole Story?

**Original question:** Which provenance and timestamp claims exceed the record?

**Original planning scope:** Contrast metadata with corroborating evidence. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-031](#bank-328-031), [BANK-328-035](#bank-328-035).

<a id="bank-328-024"></a>
### pending_topics/14 — Digital Forensics: An Evidence Chain Reconstructed

**Original question:** What happened to one artifact from seizure to report?

**Original planning scope:** Use public filings with privacy-preserving summaries. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-033](#bank-328-033).

<a id="bank-328-025"></a>
### pending_topics/15 — Digital Forensics: Device, Cloud, and Human Action

**Original question:** Which part of a record comes from each system?

**Original planning scope:** Map synchronization, accounts, devices, and logging. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-036](#bank-328-036), [BANK-328-037](#bank-328-037).

<a id="bank-328-026"></a>
### pending_topics/16 — Digital Forensics: A Forensic Tool's Result

**Original question:** What input produced a reported artifact and with what settings?

**Original planning scope:** Record tool version, source image, process, and uncertainty. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-038](#bank-328-038), [BANK-328-039](#bank-328-039).

<a id="bank-328-027"></a>
### pending_topics/17 — Digital Forensics: Preservation Versus Immediate Access

**Original question:** How do urgent needs affect evidence integrity?

**Original planning scope:** Discuss authorization, documentation, and alternatives at a high level. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-034](#bank-328-034).

<a id="bank-328-028"></a>
### pending_topics/18 — Digital Forensics: A False or Missing Artifact

**Original question:** What validation exposed a tool error or interpretation mistake?

**Original planning scope:** Use controlled test data and published corrections. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-032](#bank-328-032), [BANK-328-035](#bank-328-035).

<a id="bank-328-029"></a>
### pending_topics/19 — Digital Forensics: What a Forensic Test Did Not Cover

**Original question:** Which device, OS, app, or data state lies outside validation?

**Original planning scope:** State test population and error bounds. Evidence base: NIST evidence-preservation guidance, public case records, tool validation studies, custody logs, and controlled test data.

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-038](#bank-328-038), [BANK-328-039](#bank-328-039).

### trending_topics/0 — Digital Forensics: Record Extremes & Superlatives

**Editorial disposition:** routed. Superlative is a metric-and-source task; no record claim is adopted.

**Scoped proposals:** [BANK-328-033](#bank-328-033), [BANK-328-038](#bank-328-038).

### trending_topics/1 — Digital Forensics: An Unexplained File Change

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-032](#bank-328-032), [BANK-328-035](#bank-328-035).

### trending_topics/2 — Digital Forensics: A Forensic Tool Validated

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-038](#bank-328-038), [BANK-328-039](#bank-328-039).

### trending_topics/3 — Digital Forensics: Metadata Tells the Whole Story?

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-031](#bank-328-031), [BANK-328-035](#bank-328-035).

### trending_topics/4 — Digital Forensics: A Digital Evidence Turning Point

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-037](#bank-328-037).

### trending_topics/5 — Digital Forensics: Evidence Handlers Behind the Case

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-034](#bank-328-034).

### trending_topics/6 — Digital Forensics: An Evidence Chain Reconstructed

**Editorial disposition:** routed. Archived format routes to bounded active evidence, tool-test or incident question; original wording remains preserved.

**Scoped proposals:** [BANK-328-030](#bank-328-030), [BANK-328-033](#bank-328-033).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-328-01"></a>
### Evidence acquisition

<a id="bank-328-001"></a>
- `BANK-328-001` — Forensic imaging integrity → [BANK-328-030](#bank-328-030)
<a id="bank-328-002"></a>
- `BANK-328-002` — Write blockers → [BANK-328-034](#bank-328-034)
<a id="bank-328-003"></a>
- `BANK-328-003` — Hash verification → [BANK-328-030](#bank-328-030)

<a id="catalog-328-02"></a>
### Analysis

<a id="bank-328-004"></a>
- `BANK-328-004` — Filesystem timelines → [BANK-328-031](#bank-328-031)
<a id="bank-328-005"></a>
- `BANK-328-005` — Browser artifact interpretation → [BANK-328-035](#bank-328-035)
<a id="bank-328-006"></a>
- `BANK-328-006` — Cloud audit logs → [BANK-328-036](#bank-328-036)

<a id="catalog-328-03"></a>
### Legal and ethical scope

<a id="bank-328-007"></a>
- `BANK-328-007` — Authorization boundaries → [BANK-328-037](#bank-328-037)
<a id="bank-328-008"></a>
- `BANK-328-008` — Chain of custody for digital evidence → [BANK-328-030](#bank-328-030)
<a id="bank-328-009"></a>
- `BANK-328-009` — Attribution uncertainty → [BANK-328-032](#bank-328-032)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [010 True Crime Documentary](../010_true_crime_documentary/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [098 Law & Justice](../098_law_justice/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [099 Intelligence & Espionage](../099_intelligence_espionage/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [100 Forensics & Investigation](../100_forensics_investigation/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Coverage remaining open

- **Case and source readiness:** Inspect the full test matrix or incident investigation, including sampling and dated definitions, before scripting. One tool report or organizational audit does not establish every device result or patient outcome; no production approval follows.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/328_digital_forensics/NICHE_328_digital_forensics.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
