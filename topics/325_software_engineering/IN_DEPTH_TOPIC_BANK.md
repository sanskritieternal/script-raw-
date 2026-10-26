# 325 — Software Engineering: main topic bank

Updated: 2026-10-23 · **15 active BANK proposals · 12 categories · 13 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Requirements](#catalog-325-r01).
- **Intermediate:** [Version control](#catalog-325-r02) → [Testing](#catalog-325-r03) → [Architecture decisions](#catalog-325-r05) → [Contract tests](#catalog-325-r06) → [Traceability](#catalog-325-r09) → [Incremental change](#catalog-325-r10).
- **Advanced:** [Incidents](#catalog-325-r04) → [Rollback](#catalog-325-r07) → [Legacy systems](#catalog-325-r08) → [Code ownership](#catalog-325-r11) → [Effectiveness](#catalog-325-r12) → [Supply-chain inventory](#catalog-325-r13).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Lifecycle](#domain-325-01) | 1 | 0 | 0 |
| [Collaboration](#domain-325-02) | 0 | 1 | 0 |
| [Reliability](#domain-325-03) | 0 | 1 | 0 |
| [Operations](#domain-325-04) | 0 | 0 | 2 |
| [Documentation](#domain-325-05) | 0 | 1 | 0 |
| [Delivery](#domain-325-06) | 0 | 3 | 0 |
| [Change](#domain-325-07) | 0 | 0 | 1 |
| [Maintenance](#domain-325-08) | 0 | 0 | 1 |
| [Planning](#domain-325-09) | 0 | 1 | 0 |
| [Organization](#domain-325-10) | 0 | 0 | 1 |
| [Review](#domain-325-11) | 0 | 0 | 1 |
| [Dependability](#domain-325-12) | 0 | 0 | 1 |

<a id="domain-325-01"></a>
## Category: Lifecycle

<a id="catalog-325-r01"></a>
### Requirements

Subcategory `CATALOG-325-R01` · foundation.

<a id="bank-325-030"></a>
#### BANK-325-030 — Why can software meet its written specification and still disappoint users?

**Individual coverage scope:** Compare requirements, assumptions, usability and real workflows through a hypothetical delivery.


<a id="domain-325-02"></a>
## Category: Collaboration

<a id="catalog-325-r02"></a>
### Version control

Subcategory `CATALOG-325-R02` · intermediate.

<a id="bank-325-031"></a>
#### BANK-325-031 — How can two correct code changes break a system when combined?

**Individual coverage scope:** Trace conflicting assumptions, shared interfaces, merge order and integration tests.


<a id="domain-325-03"></a>
## Category: Reliability

<a id="catalog-325-r03"></a>
### Testing

Subcategory `CATALOG-325-R03` · intermediate.

<a id="bank-325-032"></a>
#### BANK-325-032 — What can a test suite establish and what can it miss?

**Individual coverage scope:** Compare unit, integration, system and exploratory evidence; distinguish passing tests from proven absence of bugs.


<a id="domain-325-04"></a>
## Category: Operations

<a id="catalog-325-r04"></a>
### Incidents

Subcategory `CATALOG-325-R04` · advanced.

<a id="bank-325-033"></a>
#### BANK-325-033 — How does a blameless incident review investigate causes without erasing accountability?

**Individual coverage scope:** Trace timeline, system conditions, decisions, safeguards and owned follow-up actions.

<a id="bank-325-043"></a>
#### BANK-325-043 — What did the SEC's Knight Capital order reveal about code deployment and safeguards in the August 2012 trading incident?

**Individual coverage scope:** Examine the SEC's documented router changes, deployment failure and risk-control findings as an attributed case; distinguish regulatory findings from a universal account of trading-system failures.

**Research follow-up:** [Bounded case and source-access note](325_SOFTWARE_ENGINEERING_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-325-031](#bank-325-031) — A specific deployment/control incident versus the general interaction of individually correct changes.

**Neighboring scope:** [BANK-325-039](#bank-325-039) — SEC-documented incident sequence versus a general argument for smaller releases.


<a id="domain-325-05"></a>
## Category: Documentation

<a id="catalog-325-r05"></a>
### Architecture decisions

Subcategory `CATALOG-325-R05` · intermediate.

<a id="bank-325-034"></a>
#### BANK-325-034 — What should an architecture decision record preserve after the original team leaves?

**Individual coverage scope:** Include context, alternatives, constraints, decision and consequences; distinguish a rationale record from a permanent command.


<a id="domain-325-06"></a>
## Category: Delivery

<a id="catalog-325-r06"></a>
### Contract tests

Subcategory `CATALOG-325-R06` · intermediate.

<a id="bank-325-035"></a>
#### BANK-325-035 — How can contract testing detect disagreement between services that pass their own tests?

**Individual coverage scope:** Compare provider assumptions, consumer expectations, versions and integration limits.

<a id="bank-325-044"></a>
#### BANK-325-044 — How did the Mars Climate Orbiter unit mismatch expose an interface-verification failure in 1999?

**Individual coverage scope:** Use NASA/JPL's dated preliminary account of information transfer between spacecraft and navigation teams; bound the case to engineering interfaces and verification rather than a claim that one code typo alone caused the loss.

**Research follow-up:** [Bounded case and source-access note](325_SOFTWARE_ENGINEERING_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-325-035](#bank-325-035) — A specific mission-team units interface versus general service contract testing.

**Neighboring scope:** [BANK-324-034](../324_programming/IN_DEPTH_TOPIC_BANK.md#bank-324-034) — Systems-interface verification versus type inference in programming languages.

<a id="catalog-325-r10"></a>
### Incremental change

Subcategory `CATALOG-325-R10` · intermediate.

<a id="bank-325-039"></a>
#### BANK-325-039 — Why can smaller software releases make problems easier to understand?

**Individual coverage scope:** Compare batch size, feedback, dependencies, rollout and rollback; identify cases where splitting changes is difficult.


<a id="domain-325-07"></a>
## Category: Change

<a id="catalog-325-r07"></a>
### Rollback

Subcategory `CATALOG-325-R07` · advanced.

<a id="bank-325-036"></a>
#### BANK-325-036 — Why can reverting application code fail to reverse a software migration?

**Individual coverage scope:** Trace data changes, external effects, schema compatibility and forward-recovery alternatives.


<a id="domain-325-08"></a>
## Category: Maintenance

<a id="catalog-325-r08"></a>
### Legacy systems

Subcategory `CATALOG-325-R08` · advanced.

<a id="bank-325-037"></a>
#### BANK-325-037 — How can a team change a legacy system whose behavior is poorly documented?

**Individual coverage scope:** Compare characterization tests, observation, dependency boundaries, incremental change and unknown requirements.


<a id="domain-325-09"></a>
## Category: Planning

<a id="catalog-325-r09"></a>
### Traceability

Subcategory `CATALOG-325-R09` · intermediate.

<a id="bank-325-038"></a>
#### BANK-325-038 — How can a team connect a requirement to the code and evidence that implement it?

**Individual coverage scope:** Compare acceptance criteria, design, changes, tests and versioned decisions without equating traceability with correctness.


<a id="domain-325-10"></a>
## Category: Organization

<a id="catalog-325-r11"></a>
### Code ownership

Subcategory `CATALOG-325-R11` · advanced.

<a id="bank-325-040"></a>
#### BANK-325-040 — How do ownership boundaries affect the maintenance of a shared software component?

**Individual coverage scope:** Compare responsibility, review, escalation, expertise and bottlenecks rather than assuming one team model fits all.


<a id="domain-325-11"></a>
## Category: Review

<a id="catalog-325-r12"></a>
### Effectiveness

Subcategory `CATALOG-325-R12` · advanced.

<a id="bank-325-041"></a>
#### BANK-325-041 — How can a team evaluate code review beyond counting comments?

**Individual coverage scope:** Compare defects, design understanding, latency, learning and reviewer workload with observational limits.


<a id="domain-325-12"></a>
## Category: Dependability

<a id="catalog-325-r13"></a>
### Supply-chain inventory

Subcategory `CATALOG-325-R13` · advanced.

<a id="bank-325-042"></a>
#### BANK-325-042 — Why does knowing a software dependency's version not fully describe the risk of using it?

**Individual coverage scope:** Compare transitive dependencies, build inputs, provenance, maintainer support, deployment exposure and replacement costs; exclude exploit instructions.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-325-010"></a>
### pending_topics/0 — The Architecture of Software Engineering: A Software Process Emerges

**Original question:** Which project problem prompted one engineering practice?

**Original planning scope:** Use dated reports and distinguish origin from later adoption. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 1 (The Architecture of Software Engineering: A Software Process Emerges). Target: What should an architecture decision record preserve after the original team leaves? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-034](#bank-325-034).

<a id="bank-325-011"></a>
### pending_topics/1 — Software Engineering: A Project Postmortem Rechecked

**Original question:** What does one celebrated success or failure actually show?

**Original planning scope:** Compare stated goals, delivery evidence, and user outcomes. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 2 (Software Engineering: A Project Postmortem Rechecked). Target: What did the SEC's Knight Capital order reveal about code deployment and safeguards in the August 2012 trading incident? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-043](#bank-325-043).

<a id="bank-325-012"></a>
### pending_topics/2 — Software Engineering: Invisible Engineering Work

**Original question:** Who maintains tests, documentation, operations, and accessibility?

**Original planning scope:** Use team records and consented accounts. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 3 (Software Engineering: Invisible Engineering Work). Target: How do ownership boundaries affect the maintenance of a shared software component? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-040](#bank-325-040).

<a id="bank-325-013"></a>
### pending_topics/3 — Software Engineering: From Requirement to Release

**Original question:** How does a user need become a shipped change?

**Original planning scope:** Trace requirement, design, code, test, deployment, and feedback. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 4 (Software Engineering: From Requirement to Release). Target: How can a team connect a requirement to the code and evidence that implement it? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-038](#bank-325-038).

<a id="bank-325-014"></a>
### pending_topics/4 — Software Engineering: Reliability as a Measured Property

**Original question:** Which design and operating choices support a target level?

**Original planning scope:** Define service, failure, time window, and measurement. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 5 (Software Engineering: Reliability as a Measured Property). Target: What can a test suite establish and what can it miss? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-032](#bank-325-032).

<a id="bank-325-015"></a>
### pending_topics/5 — Software Engineering: A Regression That Escaped Review

**Original question:** Which assumption let a fault reach users?

**Original planning scope:** Use issue timeline and safe reproduction evidence. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 6 (Software Engineering: A Regression That Escaped Review). Target: What did the SEC's Knight Capital order reveal about code deployment and safeguards in the August 2012 trading incident? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-043](#bank-325-043).

<a id="bank-325-016"></a>
### pending_topics/6 — Software Engineering: A New Engineering Tool

**Original question:** Did one tool shorten feedback or improve defect discovery?

**Original planning scope:** Compare matched teams, tasks, and costs. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 7 (Software Engineering: A New Engineering Tool). Target: How can contract testing detect disagreement between services that pass their own tests? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-035](#bank-325-035).

<a id="bank-325-017"></a>
### pending_topics/7 — Software Engineering: A Design Decision in Context

**Original question:** Who had authority and whose needs were represented?

**Original planning scope:** Review design records and stakeholder feedback. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 8 (Software Engineering: A Design Decision in Context). Target: How did the Mars Climate Orbiter unit mismatch expose an interface-verification failure in 1999? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-044](#bank-325-044).

<a id="bank-325-018"></a>
### pending_topics/8 — Software Engineering: A Release and Rollback

**Original question:** What triggered rollback and how was impact limited?

**Original planning scope:** Use dated deployment, monitoring, and incident records. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 9 (Software Engineering: A Release and Rollback). Target: What did the SEC's Knight Capital order reveal about code deployment and safeguards in the August 2012 trading incident? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-043](#bank-325-043).

<a id="bank-325-019"></a>
### pending_topics/9 — Software Engineering: A Change Through a Pipeline

**Original question:** Which checks run before and after deployment?

**Original planning scope:** Trace source, review, build, tests, artifact, and monitoring. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 10 (Software Engineering: A Change Through a Pipeline). Target: Why can smaller software releases make problems easier to understand? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-039](#bank-325-039).

<a id="bank-325-020"></a>
### pending_topics/10 — Software Engineering: Why a Development Method Spread

**Original question:** What problems did adopters seek to solve?

**Original planning scope:** Separate marketing, measured outcomes, and context. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 11 (Software Engineering: Why a Development Method Spread). Target: What should an architecture decision record preserve after the original team leaves? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-034](#bank-325-034).

<a id="bank-325-021"></a>
### pending_topics/11 — Software Engineering: One Team Before and After a Practice

**Original question:** Did delivery quality and workload change?

**Original planning scope:** Match release size, team, users, and measurement period. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 12 (Software Engineering: One Team Before and After a Practice). Target: Why can smaller software releases make problems easier to understand? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-039](#bank-325-039).

<a id="bank-325-022"></a>
### pending_topics/12 — Software Engineering: An Engineering Practice Proposal

**Original question:** What evidence would justify adoption?

**Original planning scope:** Specify expected outcome, costs, trial, and stop criteria. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 13 (Software Engineering: An Engineering Practice Proposal). Target: What should an architecture decision record preserve after the original team leaves? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-034](#bank-325-034).

<a id="bank-325-023"></a>
### pending_topics/13 — Software Engineering: More Tests Mean Quality?

**Original question:** Which defects can tests detect and which needs require user evidence?

**Original planning scope:** Check coverage, assertions, environments, and acceptance. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 14 (Software Engineering: More Tests Mean Quality?). Target: What can a test suite establish and what can it miss? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-032](#bank-325-032).

<a id="bank-325-024"></a>
### pending_topics/14 — Software Engineering: An Incident and Its Fix

**Original question:** How did a team learn from a production failure?

**Original planning scope:** Follow detection, response, root-cause evidence, and follow-up. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 15 (Software Engineering: An Incident and Its Fix). Target: What did the SEC's Knight Capital order reveal about code deployment and safeguards in the August 2012 trading incident? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-043](#bank-325-043).

<a id="bank-325-025"></a>
### pending_topics/15 — Software Engineering: Who Owns a Software Outcome?

**Original question:** Where do product, development, operations, vendor, and users intersect?

**Original planning scope:** Map responsibilities for one service. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 16 (Software Engineering: Who Owns a Software Outcome?). Target: How do ownership boundaries affect the maintenance of a shared software component? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-040](#bank-325-040).

<a id="bank-325-026"></a>
### pending_topics/16 — Software Engineering: A Requirement to Observable Behavior

**Original question:** What evidence shows a promised feature works?

**Original planning scope:** Link acceptance criterion, test, telemetry, and user task. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 17 (Software Engineering: A Requirement to Observable Behavior). Target: How did the Mars Climate Orbiter unit mismatch expose an interface-verification failure in 1999? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-044](#bank-325-044).

<a id="bank-325-027"></a>
### pending_topics/17 — Software Engineering: Speed of Delivery Versus Change Risk

**Original question:** How do batch size and review affect outcomes?

**Original planning scope:** Compare matched releases and failure rates. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 18 (Software Engineering: Speed of Delivery Versus Change Risk). Target: Why can smaller software releases make problems easier to understand? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-039](#bank-325-039).

<a id="bank-325-028"></a>
### pending_topics/18 — Software Engineering: A Dependency Change Breaks Service

**Original question:** Why did checks miss an incompatible version?

**Original planning scope:** Trace lockfile, build, staging, and recovery. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 19 (Software Engineering: A Dependency Change Breaks Service). Target: Why does knowing a software dependency's version not fully describe the risk of using it? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-042](#bank-325-042).

<a id="bank-325-029"></a>
### pending_topics/19 — Software Engineering: What Staging Cannot Prove

**Original question:** Which production load or user condition is absent?

**Original planning scope:** List test assumptions and monitoring safeguards. Evidence base: project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research.

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 20 (Software Engineering: What Staging Cannot Prove). Target: How did the Mars Climate Orbiter unit mismatch expose an interface-verification failure in 1999? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-044](#bank-325-044).

### trending_topics/0 — Software Engineering: Record Extremes & Superlatives

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 21 (Software Engineering: Record Extremes & Superlatives). Target: What can a test suite establish and what can it miss? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-032](#bank-325-032).

### trending_topics/1 — Software Engineering: A Regression That Escaped Review

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 22 (Software Engineering: A Regression That Escaped Review). Target: What did the SEC's Knight Capital order reveal about code deployment and safeguards in the August 2012 trading incident? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-043](#bank-325-043).

### trending_topics/2 — Software Engineering: A New Engineering Tool

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 23 (Software Engineering: A New Engineering Tool). Target: How can contract testing detect disagreement between services that pass their own tests? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-035](#bank-325-035).

### trending_topics/3 — Software Engineering: More Tests Mean Quality?

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 24 (Software Engineering: More Tests Mean Quality?). Target: What can a test suite establish and what can it miss? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-032](#bank-325-032).

### trending_topics/4 — Software Engineering: A Release and Rollback

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 25 (Software Engineering: A Release and Rollback). Target: What did the SEC's Knight Capital order reveal about code deployment and safeguards in the August 2012 trading incident? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-043](#bank-325-043).

### trending_topics/5 — Software Engineering: Invisible Engineering Work

**Editorial disposition:** merge_existing. This broad pitch is merged into the existing scope for archived pitch 26 (Software Engineering: Invisible Engineering Work). Target: How do ownership boundaries affect the maintenance of a shared software component? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-040](#bank-325-040).

### trending_topics/6 — Software Engineering: An Incident and Its Fix

**Editorial disposition:** new_case. A named source-backed case was selected for archived pitch 27 (Software Engineering: An Incident and Its Fix). Target: What did the SEC's Knight Capital order reveal about code deployment and safeguards in the August 2012 trading incident? The archive wording does not establish a superlative, outcome or production readiness.

**Scoped proposals:** [BANK-325-043](#bank-325-043).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-325-01"></a>
### Engineering lifecycle

<a id="bank-325-001"></a>
- `BANK-325-001` — Requirements traceability → [BANK-325-038](#bank-325-038)
<a id="bank-325-002"></a>
- `BANK-325-002` — Architecture decision records → [BANK-325-034](#bank-325-034)
<a id="bank-325-003"></a>
- `BANK-325-003` — Incremental delivery → [BANK-325-039](#bank-325-039)

<a id="catalog-325-02"></a>
### Reliability

<a id="bank-325-004"></a>
- `BANK-325-004` — Contract testing → [BANK-325-035](#bank-325-035)
<a id="bank-325-005"></a>
- `BANK-325-005` — Migration rollback planning → [BANK-325-036](#bank-325-036)
<a id="bank-325-006"></a>
- `BANK-325-006` — Incident postmortems → [BANK-325-033](#bank-325-033)

<a id="catalog-325-03"></a>
### Teams

<a id="bank-325-007"></a>
- `BANK-325-007` — Code review effectiveness → [BANK-325-041](#bank-325-041)
<a id="bank-325-008"></a>
- `BANK-325-008` — Ownership boundaries → [BANK-325-040](#bank-325-040)
<a id="bank-325-009"></a>
- `BANK-325-009` — Maintaining legacy systems → [BANK-325-037](#bank-325-037)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/325_software_engineering/NICHE_325_software_engineering.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
