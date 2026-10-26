# 297 — Blockchain: main topic bank

Updated: 2026-10-23 · **14 active BANK proposals · 11 categories · 12 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Ledgers](#catalog-297-r01).
- **Intermediate:** [Execution](#catalog-297-r02) → [Oracles](#catalog-297-r03) → [Supply chains](#catalog-297-r05) → [Merkle trees](#catalog-297-r07) → [Finality](#catalog-297-r08).
- **Advanced:** [Upgrades](#catalog-297-r04) → [Permissioned systems](#catalog-297-r06) → [Layer two](#catalog-297-r09) → [Contract upgrades](#catalog-297-r10) → [Throughput claims](#catalog-297-r11) → [Faults](#catalog-297-r12).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Data structures](#domain-297-01) | 1 | 0 | 0 |
| [Contracts](#domain-297-02) | 0 | 1 | 0 |
| [Inputs](#domain-297-03) | 0 | 1 | 0 |
| [Governance](#domain-297-04) | 0 | 0 | 2 |
| [Applications](#domain-297-05) | 0 | 1 | 0 |
| [Economics](#domain-297-06) | 0 | 0 | 2 |
| [Verification](#domain-297-07) | 0 | 1 | 0 |
| [Settlement](#domain-297-08) | 0 | 1 | 0 |
| [Scaling](#domain-297-09) | 0 | 0 | 2 |
| [Performance](#domain-297-10) | 0 | 0 | 1 |
| [Consensus](#domain-297-11) | 0 | 0 | 1 |

<a id="domain-297-01"></a>
## Category: Data structures

<a id="catalog-297-r01"></a>
### Ledgers

Subcategory `CATALOG-297-R01` · foundation.

<a id="bank-297-030"></a>
#### BANK-297-030 — What does a blockchain add to an ordinary append-only database?

**Individual coverage scope:** Compare hash linking, replication, consensus and trust assumptions; identify cases where a conventional database is sufficient.


<a id="domain-297-02"></a>
## Category: Contracts

<a id="catalog-297-r02"></a>
### Execution

Subcategory `CATALOG-297-R02` · intermediate.

<a id="bank-297-031"></a>
#### BANK-297-031 — Why can a smart contract execute correctly and still produce an unwanted outcome?

**Individual coverage scope:** Separate code behavior, specification, input assumptions and governance without exploit instructions.


<a id="domain-297-03"></a>
## Category: Inputs

<a id="catalog-297-r03"></a>
### Oracles

Subcategory `CATALOG-297-R03` · intermediate.

<a id="bank-297-032"></a>
#### BANK-297-032 — How does outside-world data enter a blockchain application?

**Individual coverage scope:** Trace data providers, aggregation, update timing and trust; distinguish on-chain agreement from off-chain truth.


<a id="domain-297-04"></a>
## Category: Governance

<a id="catalog-297-r04"></a>
### Upgrades

Subcategory `CATALOG-297-R04` · advanced.

<a id="bank-297-033"></a>
#### BANK-297-033 — Who decides what changes when a blockchain protocol upgrades?

**Individual coverage scope:** Compare developers, validators, users, coordination and forks without treating decentralization as a binary label.

<a id="catalog-297-r10"></a>
### Contract upgrades

Subcategory `CATALOG-297-R10` · advanced.

<a id="bank-297-039"></a>
#### BANK-297-039 — How can an upgradeable smart contract change assumptions about immutability?

**Individual coverage scope:** Compare administrators, proxies, permissions, timelocks and audit evidence descriptively; exclude exploit or unauthorized upgrade instructions.


<a id="domain-297-05"></a>
## Category: Applications

<a id="catalog-297-r05"></a>
### Supply chains

Subcategory `CATALOG-297-R05` · intermediate.

<a id="bank-297-034"></a>
#### BANK-297-034 — Why does putting a product record on a blockchain not prove the product's physical history?

**Individual coverage scope:** Trace identity, data entry, custody, audits and off-chain verification using a hypothetical shipment.


<a id="domain-297-06"></a>
## Category: Economics

<a id="catalog-297-r06"></a>
### Permissioned systems

Subcategory `CATALOG-297-R06` · advanced.

<a id="bank-297-035"></a>
#### BANK-297-035 — What changes when a blockchain's validators are a known group of institutions?

**Individual coverage scope:** Compare governance, access, consensus, accountability and trust assumptions rather than treating all ledgers as public networks.

<a id="bank-297-043"></a>
#### BANK-297-043 — What does a Fabric 2.5 private data collection put on each peer's ledger?

**Individual coverage scope:** Use versioned Hyperledger Fabric 2.5 documentation to trace private payload distribution and public hash commitments. Test what hash verification proves while bounding access controls and low-entropy guessing risk.

**Research follow-up:** [Bounded case and source-access note](297_BLOCKCHAIN_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-297-035](#bank-297-035) — Fabric 2.5 private collections versus general known-validator governance.

**Neighboring scope:** [BANK-293-032](../293_banking/IN_DEPTH_TOPIC_BANK.md#bank-293-032) — Ledger hash auditability versus banking payment final settlement.


<a id="domain-297-07"></a>
## Category: Verification

<a id="catalog-297-r07"></a>
### Merkle trees

Subcategory `CATALOG-297-R07` · intermediate.

<a id="bank-297-036"></a>
#### BANK-297-036 — How can a Merkle proof check inclusion without transmitting an entire dataset?

**Individual coverage scope:** Trace hashes, tree structure, proof paths, assumptions and limits; distinguish inclusion from the truth of recorded content.


<a id="domain-297-08"></a>
## Category: Settlement

<a id="catalog-297-r08"></a>
### Finality

Subcategory `CATALOG-297-R08` · intermediate.

<a id="bank-297-037"></a>
#### BANK-297-037 — Why does seeing a blockchain transaction not always mean its outcome is final?

**Individual coverage scope:** Compare probabilistic confirmation, protocol finality, reorganizations and application assumptions conceptually.


<a id="domain-297-09"></a>
## Category: Scaling

<a id="catalog-297-r09"></a>
### Layer two

Subcategory `CATALOG-297-R09` · advanced.

<a id="bank-297-038"></a>
#### BANK-297-038 — What trust and settlement assumptions change when transactions move to a layer-two system?

**Individual coverage scope:** Compare execution, proof or challenge mechanisms, data availability, withdrawal and base-layer dependence without vendor endorsements.

<a id="bank-297-042"></a>
#### BANK-297-042 — What did EIP-4844 change about Ethereum rollup data after Dencun?

**Individual coverage scope:** Read EIP-4844 and the 13 March 2024 activation record for blob-carrying transactions and temporary data availability. Distinguish protocol data design from a guaranteed fee reduction for every user or later parameter settings.

**Research follow-up:** [Bounded case and source-access note](297_BLOCKCHAIN_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-297-038](#bank-297-038) — Named Ethereum blob transaction upgrade versus generic layer-two trust/settlement assumptions.

**Neighboring scope:** [BANK-296-036](../296_cryptocurrency/IN_DEPTH_TOPIC_BANK.md#bank-296-036) — Data-availability protocol change versus cryptocurrency consensus incentive comparison.


<a id="domain-297-10"></a>
## Category: Performance

<a id="catalog-297-r11"></a>
### Throughput claims

Subcategory `CATALOG-297-R11` · advanced.

<a id="bank-297-040"></a>
#### BANK-297-040 — Why can a blockchain's advertised transaction capacity be incomparable with another network's figure?

**Individual coverage scope:** Compare transaction definitions, hardware, validator count, finality, batching and test conditions.


<a id="domain-297-11"></a>
## Category: Consensus

<a id="catalog-297-r12"></a>
### Faults

Subcategory `CATALOG-297-R12` · advanced.

<a id="bank-297-041"></a>
#### BANK-297-041 — How can a distributed ledger reach agreement when some participants or connections fail?

**Individual coverage scope:** Compare fault assumptions, message timing, quorum, safety and progress in a conceptual model without attack instructions.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-297-010"></a>
### pending_topics/0 — The Architecture of Blockchain: From Ledger to Blockchain

**Original question:** Which technical ideas and deployments preceded a named network?

**Original planning scope:** Use dated specifications and code histories. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-030](#bank-297-030).

<a id="bank-297-011"></a>
### pending_topics/1 — Blockchain: A Widely Cited Deployment Tested

**Original question:** What problem did one blockchain actually solve?

**Original planning scope:** Compare requirements, users, costs, and alternatives. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** new_case. Dated regulator, issuer or versioned protocol document supports a bounded case; the linked note limits jurisdiction, claims and version.

**Scoped proposals:** [BANK-297-043](#bank-297-043).

<a id="bank-297-012"></a>
### pending_topics/2 — Blockchain: Operators Behind a Distributed System

**Original question:** Who maintains nodes, keys, infrastructure, and support?

**Original planning scope:** Trace incentives, labor, and concentration. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-035](#bank-297-035).

<a id="bank-297-013"></a>
### pending_topics/3 — Blockchain: A Transaction's Path

**Original question:** How does a signed request become a recorded state change?

**Original planning scope:** Map client, validator, consensus, and confirmation. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-037](#bank-297-037).

<a id="bank-297-014"></a>
### pending_topics/4 — Blockchain: Finality and Trust Assumptions

**Original question:** When is a transaction treated as irreversible?

**Original planning scope:** Name protocol, adversary model, and reorganization risk. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-037](#bank-297-037).

<a id="bank-297-015"></a>
### pending_topics/5 — Blockchain: An Unexplained Chain Incident

**Original question:** Which public records identify the cause?

**Original planning scope:** Compare logs, code, governance, and known unknowns. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-041](#bank-297-041).

<a id="bank-297-016"></a>
### pending_topics/6 — Blockchain: A New Consensus Design

**Original question:** What trade-off did it change?

**Original planning scope:** Measure security assumptions, latency, throughput, and energy. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** new_case. Dated regulator, issuer or versioned protocol document supports a bounded case; the linked note limits jurisdiction, claims and version.

**Scoped proposals:** [BANK-297-042](#bank-297-042).

<a id="bank-297-017"></a>
### pending_topics/7 — Blockchain: A Protocol Governance Decision

**Original question:** Who proposed and adopted one rule change?

**Original planning scope:** Use proposals, votes, code, and dissent. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-033](#bank-297-033).

<a id="bank-297-018"></a>
### pending_topics/8 — Blockchain: A Fork or Outage

**Original question:** How did a documented event split or interrupt a network?

**Original planning scope:** Build a dated timeline of blocks and responses. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-041](#bank-297-041).

<a id="bank-297-019"></a>
### pending_topics/9 — Blockchain: Blocks, Nodes, and Consensus

**Original question:** How does a named implementation maintain shared state?

**Original planning scope:** Trace data structures and validation rules. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-030](#bank-297-030).

<a id="bank-297-020"></a>
### pending_topics/10 — Blockchain: Network Use Over Time

**Original question:** What does a transaction-count trend actually mean?

**Original planning scope:** Separate users, transfers, batching, bots, and fees. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-040](#bank-297-040).

<a id="bank-297-021"></a>
### pending_topics/11 — Blockchain: One Protocol Across Versions

**Original question:** What changed in security and user experience?

**Original planning scope:** Compare specifications, code, incidents, and measurements. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** new_case. Dated regulator, issuer or versioned protocol document supports a bounded case; the linked note limits jurisdiction, claims and version.

**Scoped proposals:** [BANK-297-042](#bank-297-042).

<a id="bank-297-022"></a>
### pending_topics/12 — Blockchain: Conditional Scaling Claims

**Original question:** Which assumptions must hold for a proposed improvement?

**Original planning scope:** State workload, hardware, trust, and governance conditions. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-030](#bank-297-030).

<a id="bank-297-023"></a>
### pending_topics/13 — Blockchain: Immutable Means Error-Proof?

**Original question:** What can and cannot be changed after a bad input?

**Original planning scope:** Distinguish ledger history from off-chain facts and keys. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-039](#bank-297-039).

<a id="bank-297-024"></a>
### pending_topics/14 — Blockchain: One Verified Transaction

**Original question:** What happened from submission through settlement?

**Original planning scope:** Use public data carefully and protect linked identities. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-036](#bank-297-036).

<a id="bank-297-025"></a>
### pending_topics/15 — Blockchain: Where the Blockchain Ends

**Original question:** Which parties and databases sit outside the chain?

**Original planning scope:** Map oracle, wallet, exchange, user, and legal boundary. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** new_case. Dated regulator, issuer or versioned protocol document supports a bounded case; the linked note limits jurisdiction, claims and version.

**Scoped proposals:** [BANK-297-043](#bank-297-043).

<a id="bank-297-026"></a>
### pending_topics/16 — Blockchain: Following One State Update

**Original question:** What inputs produce each visible output?

**Original planning scope:** Use test network or consented public transaction data. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-031](#bank-297-031).

<a id="bank-297-027"></a>
### pending_topics/17 — Blockchain: Replication Versus Efficiency

**Original question:** What does decentralization cost for a defined use case?

**Original planning scope:** Compare latency, storage, energy, and operator control. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-040](#bank-297-040).

<a id="bank-297-028"></a>
### pending_topics/18 — Blockchain: A Smart Contract Failure

**Original question:** Which design or operational choices contributed?

**Original planning scope:** Use published incident and audited code; avoid exploit instructions. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-031](#bank-297-031).

<a id="bank-297-029"></a>
### pending_topics/19 — Blockchain: What an Audit Can Prove

**Original question:** Which bugs or assumptions did one audit test?

**Original planning scope:** Read scope, version, methods, exclusions, and later changes. Evidence base: dated protocol specifications and code, public network data, independent audits, incident reports, and reproducible measurements.

**Editorial disposition:** new_case. Dated regulator, issuer or versioned protocol document supports a bounded case; the linked note limits jurisdiction, claims and version.

**Scoped proposals:** [BANK-297-043](#bank-297-043).

### trending_topics/0 — Blockchain: Record Extremes & Superlatives

**Editorial disposition:** merge_existing. The archived superlative/popularity claim is unverified; this active question can assess evidence without adopting that claim.

**Scoped proposals:** [BANK-297-040](#bank-297-040).

### trending_topics/1 — Blockchain: An Unexplained Chain Incident

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-041](#bank-297-041).

### trending_topics/2 — Blockchain: A New Consensus Design

**Editorial disposition:** new_case. Dated regulator, issuer or versioned protocol document supports a bounded case; the linked note limits jurisdiction, claims and version.

**Scoped proposals:** [BANK-297-042](#bank-297-042).

### trending_topics/3 — Blockchain: Immutable Means Error-Proof?

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-039](#bank-297-039).

### trending_topics/4 — Blockchain: A Fork or Outage

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-041](#bank-297-041).

### trending_topics/5 — Blockchain: Operators Behind a Distributed System

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-035](#bank-297-035).

### trending_topics/6 — Blockchain: One Verified Transaction

**Editorial disposition:** merge_existing. Existing active topic absorbs this generic archive pitch; select a dated incident, product or protocol version before production.

**Scoped proposals:** [BANK-297-036](#bank-297-036).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-297-01"></a>
### Distributed ledgers

<a id="bank-297-001"></a>
- `BANK-297-001` — Consensus under network faults → [BANK-297-041](#bank-297-041)
<a id="bank-297-002"></a>
- `BANK-297-002` — Transaction finality → [BANK-297-037](#bank-297-037)
<a id="bank-297-003"></a>
- `BANK-297-003` — Merkle-tree verification → [BANK-297-036](#bank-297-036)

<a id="catalog-297-02"></a>
### Design choices

<a id="bank-297-004"></a>
- `BANK-297-004` — Permissioned versus public chains → [BANK-297-035](#bank-297-035)
<a id="bank-297-005"></a>
- `BANK-297-005` — Smart-contract upgradeability → [BANK-297-039](#bank-297-039)
<a id="bank-297-006"></a>
- `BANK-297-006` — Layer-two settlement assumptions → [BANK-297-038](#bank-297-038)

<a id="catalog-297-03"></a>
### Evaluation

<a id="bank-297-007"></a>
- `BANK-297-007` — Throughput versus decentralization claims → [BANK-297-040](#bank-297-040)
<a id="bank-297-008"></a>
- `BANK-297-008` — Oracle trust boundaries → [BANK-297-032](#bank-297-032)
<a id="bank-297-009"></a>
- `BANK-297-009` — When a database is the simpler solution → [BANK-297-030](#bank-297-030)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [323 Databases](../323_databases/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/297_blockchain/NICHE_297_blockchain.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
