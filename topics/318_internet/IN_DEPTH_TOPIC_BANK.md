# 318 — Internet: main topic bank

Updated: 2026-10-23 · **13 active BANK proposals · 9 categories · 12 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Packets](#catalog-318-r01).
- **Intermediate:** [DNS](#catalog-318-r02) → [Routing](#catalog-318-r03) → [Undersea cables](#catalog-318-r05) → [Congestion control](#catalog-318-r07) → [Exchange points and caches](#catalog-318-r08).
- **Advanced:** [Fragmentation](#catalog-318-r04) → [Addressing](#catalog-318-r06) → [Net neutrality](#catalog-318-r09) → [Shutdowns](#catalog-318-r10) → [Universal service](#catalog-318-r11) → [Internet governance](#catalog-318-r12).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Mechanisms](#domain-318-01) | 1 | 0 | 0 |
| [Names](#domain-318-02) | 0 | 1 | 0 |
| [Networks](#domain-318-03) | 0 | 1 | 0 |
| [Governance](#domain-318-04) | 0 | 0 | 2 |
| [Infrastructure](#domain-318-05) | 0 | 2 | 0 |
| [Protocols](#domain-318-06) | 0 | 1 | 1 |
| [Measurement](#domain-318-07) | 0 | 0 | 2 |
| [Access](#domain-318-08) | 0 | 0 | 1 |
| [Standards](#domain-318-09) | 0 | 0 | 1 |

<a id="domain-318-01"></a>
## Category: Mechanisms

<a id="catalog-318-r01"></a>
### Packets

Subcategory `CATALOG-318-R01` · foundation.

<a id="bank-318-030"></a>
#### BANK-318-030 — How can one internet message travel through several networks?

**Individual coverage scope:** Trace packetization, addressing, routers and reassembly using a simplified path; distinguish internet from the web.


<a id="domain-318-02"></a>
## Category: Names

<a id="catalog-318-r02"></a>
### DNS

Subcategory `CATALOG-318-R02` · intermediate.

<a id="bank-318-031"></a>
#### BANK-318-031 — What has to happen before a browser can connect to a domain name?

**Individual coverage scope:** Trace resolver, caches, authoritative responses and expiry; exclude current provider-specific settings.


<a id="domain-318-03"></a>
## Category: Networks

<a id="catalog-318-r03"></a>
### Routing

Subcategory `CATALOG-318-R03` · intermediate.

<a id="bank-318-032"></a>
#### BANK-318-032 — Why can two users reach the same website through different routes?

**Individual coverage scope:** Compare peering, transit, geography, policy and failures conceptually; exclude route-manipulation instructions.


<a id="domain-318-04"></a>
## Category: Governance

<a id="catalog-318-r04"></a>
### Fragmentation

Subcategory `CATALOG-318-R04` · advanced.

<a id="bank-318-033"></a>
#### BANK-318-033 — What would internet fragmentation mean beyond a website being blocked?

**Individual coverage scope:** Compare naming, routing, standards, legal controls and interoperability with clear operational definitions.

<a id="catalog-318-r09"></a>
### Net neutrality

Subcategory `CATALOG-318-R09` · advanced.

<a id="bank-318-038"></a>
#### BANK-318-038 — Which different practices are debated under the term net neutrality?

**Individual coverage scope:** Compare blocking, throttling, prioritization, traffic management and transparency; reserve actual law and provider practices for current research.


<a id="domain-318-05"></a>
## Category: Infrastructure

<a id="catalog-318-r05"></a>
### Undersea cables

Subcategory `CATALOG-318-R05` · intermediate.

<a id="bank-318-034"></a>
#### BANK-318-034 — Why does a global internet connection often depend on physical cables under the sea?

**Individual coverage scope:** Trace landing stations, capacity, redundancy, repair and terrestrial links without sensitive operational details.

<a id="catalog-318-r08"></a>
### Exchange points and caches

Subcategory `CATALOG-318-R08` · intermediate.

<a id="bank-318-037"></a>
#### BANK-318-037 — How do internet exchange points and content delivery networks solve different distance and capacity problems?

**Individual coverage scope:** Compare peering, cache placement, traffic paths, failure and local connectivity rather than treating the internet as one central network.


<a id="domain-318-06"></a>
## Category: Protocols

<a id="catalog-318-r07"></a>
### Congestion control

Subcategory `CATALOG-318-R07` · intermediate.

<a id="bank-318-036"></a>
#### BANK-318-036 — How can internet senders adapt when many users compete for a limited link?

**Individual coverage scope:** Compare feedback, loss, delay, fairness and application needs conceptually without traffic-disruption instructions.

<a id="catalog-318-r06"></a>
### Addressing

Subcategory `CATALOG-318-R06` · advanced.

<a id="bank-318-035"></a>
#### BANK-318-035 — Why is moving from IPv4 to IPv6 more than adding longer addresses?

**Individual coverage scope:** Compare allocation, compatibility, dual operation and network management conceptually without current adoption statistics.


<a id="domain-318-07"></a>
## Category: Measurement

<a id="catalog-318-r10"></a>
### Shutdowns

Subcategory `CATALOG-318-R10` · advanced.

<a id="bank-318-039"></a>
#### BANK-318-039 — How can researchers distinguish an internet shutdown from an outage or a measurement gap?

**Individual coverage scope:** Compare traffic, reachability, routing, local reports, timing and independent corroboration without bypass or disruption guidance.

<a id="bank-318-042"></a>
#### BANK-318-042 — How did Meta's October 2021 backbone outage make its DNS names unreachable?

**Individual coverage scope:** Compare Meta's dated engineering postmortem with an external resolver's BGP observations; distinguish the initial backbone disconnection, route withdrawal, DNS failure and recovery without calling this an outage of the whole internet.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTES/SELECTED_CASES.md). This does not change proposal or production status.


<a id="domain-318-08"></a>
## Category: Access

<a id="catalog-318-r11"></a>
### Universal service

Subcategory `CATALOG-318-R11` · advanced.

<a id="bank-318-040"></a>
#### BANK-318-040 — Why does internet coverage not necessarily mean affordable, usable access?

**Individual coverage scope:** Compare devices, power, price, skills, language, accessibility, reliability and local alternatives.


<a id="domain-318-09"></a>
## Category: Standards

<a id="catalog-318-r12"></a>
### Internet governance

Subcategory `CATALOG-318-R12` · advanced.

<a id="bank-318-041"></a>
#### BANK-318-041 — How does a proposed internet protocol become a standard without one government owning the entire network?

**Individual coverage scope:** Trace open drafts, implementation experience, working groups, compatibility and voluntary adoption; distinguish standards institutions from network operators and domain allocation.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-318-010"></a>
### pending_topics/0 — The Architecture of Internet: How Networks Interconnected

**Original question:** Which protocol and governance decisions enabled one interconnection?

**Original planning scope:** Use dated RFCs, network maps, and operator records. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-030](#bank-318-030), [BANK-318-037](#bank-318-037).

<a id="bank-318-011"></a>
### pending_topics/1 — Internet: A Famous Internet Failure

**Original question:** What did a documented outage reveal about dependencies?

**Original planning scope:** Trace routing, DNS, power, applications, and user effects. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-039](#bank-318-039), [BANK-318-042](#bank-318-042).

<a id="bank-318-012"></a>
### pending_topics/2 — Internet: People Running the Internet

**Original question:** Who maintains cables, exchange points, routing, and support?

**Original planning scope:** Credit operators and local technicians. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-041](#bank-318-041).

<a id="bank-318-013"></a>
### pending_topics/3 — Internet: A Request Across Networks

**Original question:** How does a device reach a named service?

**Original planning scope:** Map address, DNS, routing, transport, and server. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-030](#bank-318-030), [BANK-318-031](#bank-318-031).

<a id="bank-318-014"></a>
### pending_topics/4 — Internet: The End-to-End Trade-off

**Original question:** Where should reliability or security functions live?

**Original planning scope:** Compare protocol design, network controls, and application needs. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-032](#bank-318-032), [BANK-318-036](#bank-318-036).

<a id="bank-318-015"></a>
### pending_topics/5 — Internet: A Route That Disappeared

**Original question:** Which public measurements explain a reachability incident?

**Original planning scope:** Check BGP, DNS, traceroute, and blind spots. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-032](#bank-318-032), [BANK-318-042](#bank-318-042).

<a id="bank-318-016"></a>
### pending_topics/6 — Internet: A New Protocol Deployed

**Original question:** Did one protocol improve a defined user outcome?

**Original planning scope:** Measure adoption, latency, compatibility, and failure. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-035](#bank-318-035).

<a id="bank-318-017"></a>
### pending_topics/7 — Internet: A Standards Decision

**Original question:** How did one working group resolve a design dispute?

**Original planning scope:** Read proposals, minutes, RFCs, and implementation evidence. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-041](#bank-318-041).

<a id="bank-318-018"></a>
### pending_topics/8 — Internet: An Internet Outage Timeline

**Original question:** What failed first and which users were affected?

**Original planning scope:** Use dated operator reports and independent measurements. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-039](#bank-318-039), [BANK-318-042](#bank-318-042).

<a id="bank-318-019"></a>
### pending_topics/9 — Internet: Autonomous Networks Together

**Original question:** How do networks exchange routes and traffic?

**Original planning scope:** Trace one bounded path and peering arrangements. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-030](#bank-318-030), [BANK-318-037](#bank-318-037).

<a id="bank-318-020"></a>
### pending_topics/10 — Internet: Connectivity Over Time

**Original question:** What explains a measured access change?

**Original planning scope:** Separate subscription, usable quality, affordability, and coverage. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-035](#bank-318-035), [BANK-318-040](#bank-318-040).

<a id="bank-318-021"></a>
### pending_topics/11 — Internet: One Service Across Protocol Eras

**Original question:** How did speed, security, and reach change?

**Original planning scope:** Compare matched tasks and dated implementation. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-035](#bank-318-035), [BANK-318-041](#bank-318-041).

<a id="bank-318-022"></a>
### pending_topics/12 — Internet: Conditional Network Evolution

**Original question:** What assumptions shape a proposed change?

**Original planning scope:** State interoperability, incentives, security, and deployment cost. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-035](#bank-318-035), [BANK-318-041](#bank-318-041).

<a id="bank-318-023"></a>
### pending_topics/13 — Internet: The Internet Is the Web?

**Original question:** Which services share IP but differ above it?

**Original planning scope:** Trace a concrete web and non-web task. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-030](#bank-318-030), [BANK-318-032](#bank-318-032).

<a id="bank-318-024"></a>
### pending_topics/14 — Internet: One Packet's Approximate Journey

**Original question:** What can public measurements really show?

**Original planning scope:** Name vantage points and avoid implying exact path certainty. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-037](#bank-318-037).

<a id="bank-318-025"></a>
### pending_topics/15 — Internet: Where the Internet Service Ends

**Original question:** Which device, ISP, DNS, cloud, and app controls matter?

**Original planning scope:** Draw a named service boundary. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-037](#bank-318-037), [BANK-318-040](#bank-318-040).

<a id="bank-318-026"></a>
### pending_topics/16 — Internet: A Domain Lookup to Response

**Original question:** What inputs and outputs occur at each layer?

**Original planning scope:** Use a safe trace and mask personal data. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-031](#bank-318-031).

<a id="bank-318-027"></a>
### pending_topics/17 — Internet: Centralized Service on Distributed Networks

**Original question:** What improves and what fails when a service concentrates?

**Original planning scope:** Compare latency, availability, control, and cost. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-033](#bank-318-033), [BANK-318-037](#bank-318-037).

<a id="bank-318-028"></a>
### pending_topics/18 — Internet: A DNS or Routing Error

**Original question:** How did a bounded error affect users?

**Original planning scope:** Use public postmortem and measurements, not exploit steps. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-031](#bank-318-031), [BANK-318-042](#bank-318-042).

<a id="bank-318-029"></a>
### pending_topics/19 — Internet: What a Speed Test Misses

**Original question:** Does one measurement reflect real experience?

**Original planning scope:** Check endpoint, time, congestion, packet loss, and application. Evidence base: dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts.

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-036](#bank-318-036), [BANK-318-040](#bank-318-040).

### trending_topics/0 — Internet: Record Extremes & Superlatives

**Editorial disposition:** routed. Superlative is a metric-and-source task; no record claim is adopted.

**Scoped proposals:** [BANK-318-034](#bank-318-034), [BANK-318-040](#bank-318-040).

### trending_topics/1 — Internet: A Route That Disappeared

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-032](#bank-318-032), [BANK-318-042](#bank-318-042).

### trending_topics/2 — Internet: A New Protocol Deployed

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-035](#bank-318-035).

### trending_topics/3 — Internet: The Internet Is the Web?

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-035](#bank-318-035), [BANK-318-041](#bank-318-041).

### trending_topics/4 — Internet: An Internet Outage Timeline

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-039](#bank-318-039), [BANK-318-042](#bank-318-042).

### trending_topics/5 — Internet: People Running the Internet

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-041](#bank-318-041).

### trending_topics/6 — Internet: One Packet's Approximate Journey

**Editorial disposition:** routed. Archived format routes to a bounded active mechanism or dated network case; original wording remains preserved.

**Scoped proposals:** [BANK-318-030](#bank-318-030), [BANK-318-032](#bank-318-032).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-318-01"></a>
### Network mechanics

<a id="bank-318-001"></a>
- `BANK-318-001` — Packet routing → [BANK-318-030](#bank-318-030)
<a id="bank-318-002"></a>
- `BANK-318-002` — DNS resolution → [BANK-318-031](#bank-318-031)
<a id="bank-318-003"></a>
- `BANK-318-003` — Transport congestion control → [BANK-318-036](#bank-318-036)

<a id="catalog-318-02"></a>
### Infrastructure

<a id="bank-318-004"></a>
- `BANK-318-004` — Internet exchange points → [BANK-318-037](#bank-318-037)
<a id="bank-318-005"></a>
- `BANK-318-005` — Submarine cables → [BANK-318-034](#bank-318-034)
<a id="bank-318-006"></a>
- `BANK-318-006` — Content delivery networks → [BANK-318-037](#bank-318-037)

<a id="catalog-318-03"></a>
### Governance

<a id="bank-318-007"></a>
- `BANK-318-007` — Net neutrality → [BANK-318-038](#bank-318-038)
<a id="bank-318-008"></a>
- `BANK-318-008` — Internet shutdown measurement → [BANK-318-039](#bank-318-039)
<a id="bank-318-009"></a>
- `BANK-318-009` — Universal access → [BANK-318-040](#bank-318-040)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [321 Satellite Internet](../321_satellite_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Coverage remaining open

- **Case and source readiness:** Reconcile the operator's account with dated independent telemetry or regulator records and affected-user evidence before scripting. A company postmortem or compatibility notice alone does not establish all impacts or production approval.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/318_internet/NICHE_318_internet.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
