# 322 — Cloud Computing: main topic bank

Updated: 2026-10-24 · **13 active BANK proposals · 10 categories · 12 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Service models](#catalog-322-r01) → [Virtual machines and containers](#catalog-322-r05).
- **Intermediate:** [Failure domains](#catalog-322-r02) → [Usage billing](#catalog-322-r03) → [Serverless](#catalog-322-r06) → [Autoscaling](#catalog-322-r07) → [Managed databases](#catalog-322-r09).
- **Advanced:** [Portability](#catalog-322-r04) → [Data residency](#catalog-322-r08) → [Observability cost](#catalog-322-r10) → [Cost allocation](#catalog-322-r11) → [Cloud exit rehearsal](#catalog-322-r12).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-322-01) | 1 | 0 | 0 |
| [Reliability](#domain-322-02) | 0 | 2 | 0 |
| [Economics](#domain-322-03) | 0 | 1 | 0 |
| [Architecture](#domain-322-04) | 0 | 0 | 1 |
| [Execution](#domain-322-05) | 1 | 0 | 0 |
| [Operations](#domain-322-06) | 0 | 1 | 2 |
| [Control](#domain-322-07) | 0 | 1 | 0 |
| [Governance](#domain-322-08) | 0 | 0 | 1 |
| [Data](#domain-322-09) | 0 | 1 | 0 |
| [Finance](#domain-322-10) | 0 | 0 | 1 |

<a id="domain-322-01"></a>
## Category: Foundations

<a id="catalog-322-r01"></a>
### Service models

Subcategory `CATALOG-322-R01` · foundation.

<a id="bank-322-030"></a>
#### BANK-322-030 — What does a customer manage differently in infrastructure, platform and software cloud services?

**Individual coverage scope:** Compare operating systems, runtime, applications, updates and responsibility through one hypothetical workload.


<a id="domain-322-02"></a>
## Category: Reliability

<a id="catalog-322-r02"></a>
### Failure domains

Subcategory `CATALOG-322-R02` · intermediate.

<a id="bank-322-031"></a>
#### BANK-322-031 — Why can an application fail despite running on many cloud servers?

**Individual coverage scope:** Trace shared dependencies, zones, configuration, storage and control systems rather than equating replication with resilience.

<a id="bank-322-042"></a>
#### BANK-322-042 — What did AWS's 7 December 2021 us-east-1 event reveal about shared control-plane dependencies?

**Individual coverage scope:** Read AWS's dated event summary to distinguish internal networking, monitoring/DNS/authentication and EC2 control-plane effects from running compute workloads. Treat AWS's reconstruction as one operator account; do not infer every customer's impact or promise a fail-proof multi-region design.

**Research follow-up:** [Bounded case and source-access note](CASE_SOURCE_NOTES.md). This does not change proposal or production status.


<a id="domain-322-03"></a>
## Category: Economics

<a id="catalog-322-r03"></a>
### Usage billing

Subcategory `CATALOG-322-R03` · intermediate.

<a id="bank-322-032"></a>
#### BANK-322-032 — How can a small cloud application generate an unexpectedly large bill?

**Individual coverage scope:** Compare compute, storage, requests, egress and idle resources with explicit hypothetical prices.


<a id="domain-322-04"></a>
## Category: Architecture

<a id="catalog-322-r04"></a>
### Portability

Subcategory `CATALOG-322-R04` · advanced.

<a id="bank-322-033"></a>
#### BANK-322-033 — What makes moving a cloud application harder than copying its code?

**Individual coverage scope:** Examine data gravity, identity, managed APIs, operations and testing without promoting a provider.


<a id="domain-322-05"></a>
## Category: Execution

<a id="catalog-322-r05"></a>
### Virtual machines and containers

Subcategory `CATALOG-322-R05` · foundation.

<a id="bank-322-034"></a>
#### BANK-322-034 — Why do virtual machines and containers isolate workloads differently?

**Individual coverage scope:** Compare kernels, guest systems, images, startup and security boundaries without treating lightweight as automatically safer.


<a id="domain-322-06"></a>
## Category: Operations

<a id="catalog-322-r06"></a>
### Serverless

Subcategory `CATALOG-322-R06` · intermediate.

<a id="bank-322-035"></a>
#### BANK-322-035 — What limits remain when a cloud function is described as serverless?

**Individual coverage scope:** Compare runtime, duration, concurrency, state, cold starts and external services; reserve actual product limits for research.

<a id="catalog-322-r10"></a>
### Observability cost

Subcategory `CATALOG-322-R10` · advanced.

<a id="bank-322-039"></a>
#### BANK-322-039 — How can logs, metrics and traces become a cloud application's major cost center?

**Individual coverage scope:** Compare event volume, cardinality, sampling, retention, search and data transfer with a hypothetical workload.

<a id="catalog-322-r12"></a>
### Cloud exit rehearsal

Subcategory `CATALOG-322-R12` · advanced.

<a id="bank-322-041"></a>
#### BANK-322-041 — What does a cloud exit rehearsal reveal that a diagram of portable components cannot?

**Individual coverage scope:** Trace exported data, identity replacement, restored services, downtime, dependencies and measured recovery steps in a fictional workload; keep migration promises separate from demonstrated rehearsal.


<a id="domain-322-07"></a>
## Category: Control

<a id="catalog-322-r07"></a>
### Autoscaling

Subcategory `CATALOG-322-R07` · intermediate.

<a id="bank-322-036"></a>
#### BANK-322-036 — Why can automatic cloud scaling respond too late to a traffic spike?

**Individual coverage scope:** Trace metrics, sampling, startup delay, queues and feedback oscillation with a hypothetical workload.


<a id="domain-322-08"></a>
## Category: Governance

<a id="catalog-322-r08"></a>
### Data residency

Subcategory `CATALOG-322-R08` · advanced.

<a id="bank-322-037"></a>
#### BANK-322-037 — Why is choosing a cloud region different from proving all data stays there?

**Individual coverage scope:** Trace backups, logs, support access, subprocessors and control-plane data; exclude legal compliance certification.


<a id="domain-322-09"></a>
## Category: Data

<a id="catalog-322-r09"></a>
### Managed databases

Subcategory `CATALOG-322-R09` · intermediate.

<a id="bank-322-038"></a>
#### BANK-322-038 — What responsibilities remain after a database is moved to a managed cloud service?

**Individual coverage scope:** Compare schema, queries, access, recovery tests, scaling and service boundaries without provider-specific promises.


<a id="domain-322-10"></a>
## Category: Finance

<a id="catalog-322-r11"></a>
### Cost allocation

Subcategory `CATALOG-322-R11` · advanced.

<a id="bank-322-040"></a>
#### BANK-322-040 — Why can a shared cloud bill be hard to divide between teams fairly?

**Individual coverage scope:** Compare tagging, shared services, idle capacity, commitments and accountability without assuming a single correct allocation rule.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-322-010"></a>
### pending_topics/0 — The Architecture of Cloud Computing: From Hosted Servers to Cloud

**Original question:** Which changes made one service on-demand and metered?

**Original planning scope:** Compare dated provisioning, pooling, elasticity, and billing evidence. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-030](#bank-322-030).

<a id="bank-322-011"></a>
### pending_topics/1 — Cloud Computing: A Cloud Migration Revisited

**Original question:** Did one migration improve its stated outcome?

**Original planning scope:** Compare matched reliability, cost, latency, and operations before and after. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-033](#bank-322-033).

<a id="bank-322-012"></a>
### pending_topics/2 — Cloud Computing: People Operating the Cloud

**Original question:** Who maintains data centers, networks, support, and customer systems?

**Original planning scope:** Trace labor and responsibility across organizations. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-040](#bank-322-040).

<a id="bank-322-013"></a>
### pending_topics/3 — Cloud Computing: What Makes a Service Cloud?

**Original question:** Which features distinguish cloud from ordinary remote hosting?

**Original planning scope:** Test NIST characteristics against a named offer. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-030](#bank-322-030).

<a id="bank-322-014"></a>
### pending_topics/4 — Cloud Computing: Elasticity Under Load

**Original question:** When does autoscaling protect a workload and when does it lag?

**Original planning scope:** Measure trigger, startup delay, capacity limit, and cost. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-036](#bank-322-036).

<a id="bank-322-015"></a>
### pending_topics/5 — Cloud Computing: An Unexplained Cloud Bill

**Original question:** Which resources and price rules explain a bounded cost spike?

**Original planning scope:** Reconcile meter, region, storage, transfer, and discounts. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-032](#bank-322-032).

<a id="bank-322-016"></a>
### pending_topics/6 — Cloud Computing: A Managed Service's Promise

**Original question:** Which operational task did it remove and which controls did it hide?

**Original planning scope:** Compare versions, provider duties, and user evidence. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-038](#bank-322-038).

<a id="bank-322-017"></a>
### pending_topics/7 — Cloud Computing: A Cloud Architecture Decision

**Original question:** Who chose regions, services, and resilience targets?

**Original planning scope:** Use design records and incident outcomes. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-031](#bank-322-031).

<a id="bank-322-018"></a>
### pending_topics/8 — Cloud Computing: A Regional Cloud Outage

**Original question:** What failed first and how did dependencies spread?

**Original planning scope:** Use dated provider postmortem and customer evidence. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Distinct bounded incident case added.. Dated operator records support a named incident question.

**Scoped proposals:** [BANK-322-042](#bank-322-042).

<a id="bank-322-019"></a>
### pending_topics/9 — Cloud Computing: Provisioning a Cloud Workload

**Original question:** How do API, identity, scheduler, compute, storage, and network combine?

**Original planning scope:** Trace a named service model and region. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-034](#bank-322-034).

<a id="bank-322-020"></a>
### pending_topics/10 — Cloud Computing: Why a Service Left the Cloud

**Original question:** Which workload, cost, governance, or performance change drove the move?

**Original planning scope:** Compare documented alternatives and full migration costs. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-041](#bank-322-041).

<a id="bank-322-021"></a>
### pending_topics/11 — Cloud Computing: One Workload Before and After

**Original question:** How did deployment time, reliability, and total cost change?

**Original planning scope:** Normalize traffic, region, team effort, and time period. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-039](#bank-322-039).

<a id="bank-322-022"></a>
### pending_topics/12 — Cloud Computing: A Proposed Cloud Feature

**Original question:** What must be shown before its promised benefit is credible?

**Original planning scope:** Specify availability, compatibility, price, and observed workload. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-035](#bank-322-035).

<a id="bank-322-023"></a>
### pending_topics/13 — Cloud Computing: Cloud Means Infinite Capacity?

**Original question:** Where do quotas, regional supply, and service limits appear?

**Original planning scope:** Use current provider limits and a defined workload. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-036](#bank-322-036).

<a id="bank-322-024"></a>
### pending_topics/14 — Cloud Computing: An Application's Cloud Move

**Original question:** What happened from decision to steady-state operations?

**Original planning scope:** Follow dated design, migration, incident, and billing records. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-033](#bank-322-033).

<a id="bank-322-025"></a>
### pending_topics/15 — Cloud Computing: Who Owns Which Failure?

**Original question:** Which tasks belong to provider, customer, and software supplier?

**Original planning scope:** Map a named IaaS, PaaS, or SaaS service and contract. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-038](#bank-322-038).

<a id="bank-322-026"></a>
### pending_topics/16 — Cloud Computing: A Cloud Request and Bill

**Original question:** What resources does one request consume and how are they charged?

**Original planning scope:** Trace network, compute, storage, logs, and meter. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-032](#bank-322-032).

<a id="bank-322-027"></a>
### pending_topics/17 — Cloud Computing: Multi-Region Resilience

**Original question:** Which failures does a second region address and what does it cost?

**Original planning scope:** Model data consistency, traffic routing, testing, and fees. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Distinct bounded incident case added.. Dated operator records support a named incident question.

**Scoped proposals:** [BANK-322-042](#bank-322-042).

<a id="bank-322-028"></a>
### pending_topics/18 — Cloud Computing: A Dependency Cascade

**Original question:** How did one service failure affect otherwise healthy components?

**Original planning scope:** Use postmortem timelines and distinguish cause from correlation. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Distinct bounded incident case added.. Dated operator records support a named incident question.

**Scoped proposals:** [BANK-322-042](#bank-322-042).

<a id="bank-322-029"></a>
### pending_topics/19 — Cloud Computing: Cloud Benchmark Reality

**Original question:** Does a vendor benchmark predict a particular workload?

**Original planning scope:** Specify hardware, region, concurrency, data, and price basis. Evidence base: NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-036](#bank-322-036).

### trending_topics/0 — Cloud Computing: Record Extremes & Superlatives

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-031](#bank-322-031).

### trending_topics/1 — Cloud Computing: An Unexplained Cloud Bill

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-032](#bank-322-032).

### trending_topics/2 — Cloud Computing: A Managed Service's Promise

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-038](#bank-322-038).

### trending_topics/3 — Cloud Computing: Cloud Means Infinite Capacity?

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-036](#bank-322-036).

### trending_topics/4 — Cloud Computing: A Regional Cloud Outage

**Editorial disposition:** Distinct bounded incident case added.. Dated operator records support a named incident question.

**Scoped proposals:** [BANK-322-042](#bank-322-042).

### trending_topics/5 — Cloud Computing: People Operating the Cloud

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-040](#bank-322-040).

### trending_topics/6 — Cloud Computing: An Application's Cloud Move

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-322-033](#bank-322-033).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-322-01"></a>
### Cloud architectures

<a id="bank-322-001"></a>
- `BANK-322-001` — Virtual machines versus containers → [BANK-322-034](#bank-322-034)
<a id="bank-322-002"></a>
- `BANK-322-002` — Serverless execution limits → [BANK-322-035](#bank-322-035)
<a id="bank-322-003"></a>
- `BANK-322-003` — Managed database tradeoffs → [BANK-322-038](#bank-322-038)

<a id="catalog-322-02"></a>
### Operations

<a id="bank-322-004"></a>
- `BANK-322-004` — Autoscaling signals → [BANK-322-036](#bank-322-036)
<a id="bank-322-005"></a>
- `BANK-322-005` — Multi-region failover → [BANK-322-031](#bank-322-031)
<a id="bank-322-006"></a>
- `BANK-322-006` — Observability costs → [BANK-322-039](#bank-322-039)

<a id="catalog-322-03"></a>
### Business and governance

<a id="bank-322-007"></a>
- `BANK-322-007` — Cloud cost allocation → [BANK-322-040](#bank-322-040)
<a id="bank-322-008"></a>
- `BANK-322-008` — Data residency → [BANK-322-037](#bank-322-037)
<a id="bank-322-009"></a>
- `BANK-322-009` — Vendor portability → [BANK-322-033](#bank-322-033)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/322_cloud_computing/NICHE_322_cloud_computing.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
