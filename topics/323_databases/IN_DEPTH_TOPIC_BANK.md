# 323 — Databases: main topic bank

Updated: 2026-10-24 · **11 active BANK proposals · 11 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Data models](#catalog-323-r01) → [Normalization](#catalog-323-r05).
- **Intermediate:** [Transactions](#catalog-323-r02) → [Indexes](#catalog-323-r03) → [Query planners](#catalog-323-r06) → [Backups](#catalog-323-r07) → [Graph databases](#catalog-323-r09) → [Analytical versus transactional data](#catalog-323-r11).
- **Advanced:** [Consistency](#catalog-323-r04) → [Schema migration](#catalog-323-r08) → [Lag](#catalog-323-r10).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-323-01) | 1 | 0 | 0 |
| [Correctness](#domain-323-02) | 0 | 1 | 0 |
| [Performance](#domain-323-03) | 0 | 0 | 0 |
| [Distributed systems](#domain-323-04) | 0 | 0 | 1 |
| [Structure](#domain-323-05) | 1 | 0 | 0 |
| [Execution](#domain-323-06) | 0 | 1 | 0 |
| [Recovery](#domain-323-07) | 0 | 2 | 0 |
| [Change](#domain-323-08) | 0 | 0 | 1 |
| [Relationships](#domain-323-09) | 0 | 1 | 0 |
| [Replication](#domain-323-10) | 0 | 0 | 1 |
| [Storage](#domain-323-11) | 0 | 1 | 0 |

<a id="domain-323-01"></a>
## Category: Foundations

<a id="catalog-323-r01"></a>
### Data models

Subcategory `CATALOG-323-R01` · foundation.

<a id="bank-323-030"></a>
#### BANK-323-030 — Why do relational tables and document databases organize the same information differently?

**Individual coverage scope:** Compare structure, duplication, queries and constraints with a small invented dataset.


<a id="domain-323-02"></a>
## Category: Correctness

<a id="catalog-323-r02"></a>
### Transactions

Subcategory `CATALOG-323-R02` · intermediate.

<a id="bank-323-031"></a>
#### BANK-323-031 — What does a database transaction protect when several users edit at once?

**Individual coverage scope:** Trace atomicity, isolation, conflicts and rollback through a hypothetical booking example.


<a id="domain-323-03"></a>
## Category: Performance

<a id="catalog-323-r03"></a>
### Indexes

Subcategory `CATALOG-323-R03` · intermediate.

Original subcategory metadata is preserved. Its overlapping proposal records are retained with primary-question referrals below and excluded from the active count.


<a id="domain-323-04"></a>
## Category: Distributed systems

<a id="catalog-323-r04"></a>
### Consistency

Subcategory `CATALOG-323-R04` · advanced.

<a id="bank-323-033"></a>
#### BANK-323-033 — What changes when a database must operate across an unreliable network?

**Individual coverage scope:** Compare replication, partitions, consistency and availability under explicitly stated failure assumptions.


<a id="domain-323-05"></a>
## Category: Structure

<a id="catalog-323-r05"></a>
### Normalization

Subcategory `CATALOG-323-R05` · foundation.

<a id="bank-323-034"></a>
#### BANK-323-034 — Why can splitting one table into several reduce data inconsistency?

**Individual coverage scope:** Use a small invented dataset to compare repeated facts, keys, dependencies and join costs.


<a id="domain-323-06"></a>
## Category: Execution

<a id="catalog-323-r06"></a>
### Query planners

Subcategory `CATALOG-323-R06` · intermediate.

<a id="bank-323-035"></a>
#### BANK-323-035 — How can a database return the same answer through very different query plans?

**Individual coverage scope:** Compare estimates, indexes, join order, statistics and changing data distribution.


<a id="domain-323-07"></a>
## Category: Recovery

<a id="catalog-323-r07"></a>
### Backups

Subcategory `CATALOG-323-R07` · intermediate.

<a id="bank-323-036"></a>
#### BANK-323-036 — Why does successfully creating a database backup not prove the data can be restored?

**Individual coverage scope:** Trace restore testing, dependencies, retention, recovery time and point-in-time gaps.

<a id="bank-323-041"></a>
#### BANK-323-041 — What did GitLab.com's January 2017 database outage show about the gap between backups and restored service?

**Individual coverage scope:** Compare GitLab's contemporaneous incident timeline and 10 February postmortem for replication lag, available copies, restoration delay and bounded data loss. Distinguish the hosted GitLab.com service from self-managed installations and describe failure modes without reproducing destructive commands or a recovery procedure.

**Research follow-up:** [Bounded case and source-access note](CASE_SOURCE_NOTES.md). This does not change proposal or production status.


<a id="domain-323-08"></a>
## Category: Change

<a id="catalog-323-r08"></a>
### Schema migration

Subcategory `CATALOG-323-R08` · advanced.

<a id="bank-323-037"></a>
#### BANK-323-037 — How can a database schema change while old and new application versions overlap?

**Individual coverage scope:** Compare compatibility, staged writes, backfills, validation and rollback assumptions without prescribing a live migration.


<a id="domain-323-09"></a>
## Category: Relationships

<a id="catalog-323-r09"></a>
### Graph databases

Subcategory `CATALOG-323-R09` · intermediate.

<a id="bank-323-038"></a>
#### BANK-323-038 — When does representing data as a graph simplify a relationship query?

**Individual coverage scope:** Compare nodes, edges, traversals, indexes and relational alternatives using invented social or transport data.


<a id="domain-323-10"></a>
## Category: Replication

<a id="catalog-323-r10"></a>
### Lag

Subcategory `CATALOG-323-R10` · advanced.

<a id="bank-323-039"></a>
#### BANK-323-039 — Why can two successful reads from a replicated database return different recent states?

**Individual coverage scope:** Trace asynchronous replication, read placement, causal expectations and application consequences.


<a id="domain-323-11"></a>
## Category: Storage

<a id="catalog-323-r11"></a>
### Analytical versus transactional data

Subcategory `CATALOG-323-R11` · intermediate.

<a id="bank-323-040"></a>
#### BANK-323-040 — Why can a database optimized for individual transactions struggle with a whole-company analytical query?

**Individual coverage scope:** Compare row and column organization, scans, updates, concurrency, data freshness and workload separation; exclude a universal recommendation of one database product.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-323-010"></a>
### pending_topics/0 — The Architecture of Databases: A Database Model Emerges

**Original question:** What problem did a named data model address?

**Original planning scope:** Use dated papers, implementations, and workload context. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-030](#bank-323-030).

<a id="bank-323-011"></a>
### pending_topics/1 — Databases: A Database Migration Revisited

**Original question:** Did one replacement meet its consistency and performance aims?

**Original planning scope:** Compare schema, workload, failure tests, and migration cost. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-037](#bank-323-037).

<a id="bank-323-012"></a>
### pending_topics/2 — Databases: People Maintaining the Data

**Original question:** Who defines schemas, repairs records, operates backups, and answers users?

**Original planning scope:** Credit operators, stewards, and affected communities. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-036](#bank-323-036).

<a id="bank-323-013"></a>
### pending_topics/3 — Databases: From Record to Query

**Original question:** How does one application store and retrieve a record?

**Original planning scope:** Trace schema, index, query, permissions, and returned result. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-030](#bank-323-030).

<a id="bank-323-014"></a>
### pending_topics/4 — Databases: Isolation in a Real Transaction

**Original question:** Which concurrent outcome can a chosen isolation level permit?

**Original planning scope:** Use a named engine, version, workload, and reproducible schedule. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-031](#bank-323-031).

<a id="bank-323-015"></a>
### pending_topics/5 — Databases: Where Did a Record Go?

**Original question:** Which logs, migrations, replicas, or queries explain a missing result?

**Original planning scope:** Protect sensitive data and distinguish deletion from invisibility. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-035](#bank-323-035).

<a id="bank-323-016"></a>
### pending_topics/6 — Databases: A New Database Feature

**Original question:** Did an index or execution change improve the target workload?

**Original planning scope:** Test latency, write cost, storage, and correctness. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-033](#bank-323-033).

<a id="bank-323-017"></a>
### pending_topics/7 — Databases: A Data Design Choice

**Original question:** Who chose a schema or consistency rule and why?

**Original planning scope:** Read design decisions and consequences for users. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-034](#bank-323-034).

<a id="bank-323-018"></a>
### pending_topics/8 — Databases: A Database Incident Timeline

**Original question:** What sequence led from first error to recovery?

**Original planning scope:** Use public postmortem, alerts, and restore evidence. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Distinct bounded incident case added.. Dated operator records support a named incident question.

**Scoped proposals:** [BANK-323-041](#bank-323-041).

<a id="bank-323-019"></a>
### pending_topics/9 — Databases: Commit and Read Back

**Original question:** How does a named engine make a write visible and durable?

**Original planning scope:** Trace transaction, log, storage, cache, and replica path. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-031](#bank-323-031).

<a id="bank-323-020"></a>
### pending_topics/10 — Databases: A Database Technology's Adoption

**Original question:** Which workload and organization choices explain use over time?

**Original planning scope:** Separate popularity metrics from suitability and outcomes. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-030](#bank-323-030).

<a id="bank-323-021"></a>
### pending_topics/11 — Databases: One Query Before and After

**Original question:** What changed after schema or engine migration?

**Original planning scope:** Control data size, hardware, indexes, concurrency, and version. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-035](#bank-323-035).

<a id="bank-323-022"></a>
### pending_topics/12 — Databases: A Proposed Database Capability

**Original question:** What would demonstrate safe usefulness in production?

**Original planning scope:** Define compatibility, correctness, workload, and operational cost. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-033](#bank-323-033).

<a id="bank-323-023"></a>
### pending_topics/13 — Databases: Replication Is Backup?

**Original question:** Which failures can a replica copy but a retained backup recover?

**Original planning scope:** Test deletion, corruption, restore point, and access controls. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-036](#bank-323-036).

<a id="bank-323-024"></a>
### pending_topics/14 — Databases: A Data Recovery Story

**Original question:** How did operators detect, contain, and restore a loss?

**Original planning scope:** Use consented records and distinguish recovery claim from test. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Distinct bounded incident case added.. Dated operator records support a named incident question.

**Scoped proposals:** [BANK-323-041](#bank-323-041).

<a id="bank-323-025"></a>
### pending_topics/15 — Databases: Application Versus Database Guarantee

**Original question:** Which correctness duties belong to app code, schema, and engine?

**Original planning scope:** Name transaction settings and failure assumptions. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-031](#bank-323-031).

<a id="bank-323-026"></a>
### pending_topics/16 — Databases: One Query's Path

**Original question:** What data enters a query and how is the result produced?

**Original planning scope:** Trace parse, plan, index, access, and response for a named engine. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-035](#bank-323-035).

<a id="bank-323-027"></a>
### pending_topics/17 — Databases: Index Gains and Write Costs

**Original question:** When does an index speed reads while increasing maintenance?

**Original planning scope:** Benchmark a defined mix and data distribution. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-035](#bank-323-035).

<a id="bank-323-028"></a>
### pending_topics/18 — Databases: A Failed Commit or Restore

**Original question:** What evidence shows whether data was lost or unavailable?

**Original planning scope:** Use transaction logs, storage state, and restore test. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Distinct bounded incident case added.. Dated operator records support a named incident question.

**Scoped proposals:** [BANK-323-041](#bank-323-041).

<a id="bank-323-029"></a>
### pending_topics/19 — Databases: A Database Benchmark's Blind Spots

**Original question:** Does a headline throughput number match the intended application?

**Original planning scope:** Specify schema, dataset, read-write mix, concurrency, and durability. Evidence base: database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-035](#bank-323-035).

### trending_topics/0 — Databases: Record Extremes & Superlatives

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-040](#bank-323-040).

### trending_topics/1 — Databases: Where Did a Record Go?

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-035](#bank-323-035).

### trending_topics/2 — Databases: A New Database Feature

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-033](#bank-323-033).

### trending_topics/3 — Databases: Replication Is Backup?

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-036](#bank-323-036).

### trending_topics/4 — Databases: A Database Incident Timeline

**Editorial disposition:** Distinct bounded incident case added.. Dated operator records support a named incident question.

**Scoped proposals:** [BANK-323-041](#bank-323-041).

### trending_topics/5 — Databases: People Maintaining the Data

**Editorial disposition:** Routed to existing scoped BANK proposal.. The generic archived framing merges into this narrower active scope; record, trend and universal reliability claims are not adopted.

**Scoped proposals:** [BANK-323-036](#bank-323-036).

### trending_topics/6 — Databases: A Data Recovery Story

**Editorial disposition:** Distinct bounded incident case added.. Dated operator records support a named incident question.

**Scoped proposals:** [BANK-323-041](#bank-323-041).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-323-01"></a>
### Data models

<a id="bank-323-001"></a>
- `BANK-323-001` — Relational normalization → [BANK-323-034](#bank-323-034)
<a id="bank-323-002"></a>
- `BANK-323-002` — Document data modeling → [BANK-323-030](#bank-323-030)
<a id="bank-323-003"></a>
- `BANK-323-003` — Graph relationships → [BANK-323-038](#bank-323-038)

<a id="catalog-323-02"></a>
### Execution

<a id="bank-323-004"></a>
- `BANK-323-004` — Index design → [BANK-061-032](../061_software_programming/IN_DEPTH_TOPIC_BANK.md#bank-061-032)
<a id="bank-323-005"></a>
- `BANK-323-005` — Query planners → [BANK-323-035](#bank-323-035)
<a id="bank-323-006"></a>
- `BANK-323-006` — Transaction isolation → [BANK-323-031](#bank-323-031)

<a id="catalog-323-03"></a>
### Operations

<a id="bank-323-007"></a>
- `BANK-323-007` — Backup restoration tests → [BANK-323-036](#bank-323-036)
<a id="bank-323-008"></a>
- `BANK-323-008` — Schema migration → [BANK-323-037](#bank-323-037)
<a id="bank-323-009"></a>
- `BANK-323-009` — Replication lag → [BANK-323-039](#bank-323-039)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

### Retired overlaps and primary questions

<a id="bank-323-032"></a>
- `BANK-323-032` → [BANK-061-032](../061_software_programming/IN_DEPTH_TOPIC_BANK.md#bank-061-032): The individual scopes describe substantially the same episode: Inspect query plans, selectivity and write overhead on a reproducible sample; avoid universal tuning recipes based on one table. / Compare lookup structure, maintenance, selectivity and storage with illustrative queries. Retain one primary question and preserve the other full record inactive with a referral.

  Preserved inactive question: Why can an index speed up reads while slowing down writes?

  Preserved inactive scope: Compare lookup structure, maintenance, selectivity and storage with illustrative queries.


## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/323_databases/NICHE_323_databases.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
