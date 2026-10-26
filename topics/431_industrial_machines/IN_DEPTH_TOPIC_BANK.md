# 431 — Industrial Machines: main topic bank

Updated: 2026-10-23 · **15 active BANK proposals · 8 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Machine foundations](#catalog-431-r01) → [Industrial control](#catalog-431-r04) → [Industrial robotics](#catalog-431-r07).
- **Intermediate:** [Production integration](#catalog-431-r02) → [Industrial control](#catalog-431-r05) → [Servo tuning concepts](#catalog-431-r08) → [Process instrumentation](#catalog-431-r09).
- **Advanced:** [Reliability decisions](#catalog-431-r03) → [Machine stewardship](#catalog-431-r06) → [Spare-parts obsolescence](#catalog-431-r10) → [Operator training evidence](#catalog-431-r11).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-431-01) | 3 | 0 | 0 |
| [Methods and applications](#domain-431-02) | 0 | 4 | 0 |
| [Systems and interpretation](#domain-431-03) | 0 | 0 | 3 |
| [Production automation](#domain-431-04) | 1 | 0 | 0 |
| [Motion control](#domain-431-05) | 0 | 1 | 0 |
| [Industrial sensing](#domain-431-06) | 0 | 1 | 0 |
| [Industrial lifecycle](#domain-431-07) | 0 | 0 | 1 |
| [Industrial assurance](#domain-431-08) | 0 | 0 | 1 |

<a id="domain-431-01"></a>
## Category: Foundations

<a id="catalog-431-r01"></a>
### Machine foundations

Subcategory `CATALOG-431-R01` · foundation.

<a id="bank-431-030"></a>
#### BANK-431-030 — How does a machine convert rotary motion into controlled linear movement?

**Individual coverage scope:** Compare screws, belts and cylinders conceptually.

<a id="bank-431-031"></a>
#### BANK-431-031 — Why does machine accuracy differ from repeatability?

**Individual coverage scope:** Use repeated positioning examples and measurement uncertainty.

<a id="catalog-431-r04"></a>
### Industrial control

Subcategory `CATALOG-431-R04` · foundation.

<a id="bank-431-036"></a>
#### BANK-431-036 — How do hydraulic presses, conveyors and CNC systems apply different kinds of controlled motion?

**Individual coverage scope:** Compare force, precision and material flow.


<a id="domain-431-02"></a>
## Category: Methods and applications

<a id="catalog-431-r02"></a>
### Production integration

Subcategory `CATALOG-431-R02` · intermediate.

<a id="bank-431-032"></a>
#### BANK-431-032 — How can one slow machine limit an entire production line?

**Individual coverage scope:** Trace bottlenecks, buffers and variability.

<a id="bank-431-033"></a>
#### BANK-431-033 — What changes when an industrial machine becomes connected to a factory network?

**Individual coverage scope:** Map data interfaces, maintenance and access responsibilities.

<a id="bank-431-044"></a>
#### BANK-431-044 — What does NIST?s Smart Manufacturing Systems Test Bed connect between a CNC machine and its design and inspection records?

**Individual coverage scope:** Trace NIST?s described CAx lab, CNC milling/turning and inspection equipment, MTConnect data collection and web publication as a bounded research test bed. Identify what a live data stream cannot by itself establish about part quality, labor or production-scale benefit.

**Research follow-up:** [Bounded case and source-access note](431_INDUSTRIAL_MACHINES_SOURCE_NOTE.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-431-033](#bank-431-033) — A named NIST shop-floor data architecture versus general consequences of connecting any industrial machine.

**Neighboring scope:** [BANK-431-035](#bank-431-035) — Research test-bed data links versus representative production acceptance testing.

**Neighboring scope:** [BANK-431-041](#bank-431-041) — Published machine-signal streams versus interpreting whether a sensor reflects the intended process condition.

**Neighboring scope:** [BANK-429-043](../429_construction/IN_DEPTH_TOPIC_BANK.md#bank-429-043) — Machine/design/inspection data in a manufacturing test bed versus building handover to maintenance teams.

<a id="catalog-431-r05"></a>
### Industrial control

Subcategory `CATALOG-431-R05` · intermediate.

<a id="bank-431-037"></a>
#### BANK-431-037 — How do PLC scan cycles and machine-vision timing affect a production task?

**Individual coverage scope:** Trace sensing, decision and actuation conceptually.


<a id="domain-431-03"></a>
## Category: Systems and interpretation

<a id="catalog-431-r03"></a>
### Reliability decisions

Subcategory `CATALOG-431-R03` · advanced.

<a id="bank-431-034"></a>
#### BANK-431-034 — How can preventive maintenance intervals create both savings and waste?

**Individual coverage scope:** Compare failure modes, inspection evidence and unnecessary replacement.

<a id="bank-431-035"></a>
#### BANK-431-035 — What makes a machine acceptance test representative of real production?

**Individual coverage scope:** Include material variation, operators and sustained duty cycles.

<a id="catalog-431-r06"></a>
### Machine stewardship

Subcategory `CATALOG-431-R06` · advanced.

<a id="bank-431-038"></a>
#### BANK-431-038 — What do vibration monitoring and guarding address that operator training alone cannot?

**Individual coverage scope:** Separate condition detection, engineered protection and qualified isolation procedures.


<a id="domain-431-04"></a>
## Category: Production automation

<a id="catalog-431-r07"></a>
### Industrial robotics

Subcategory `CATALOG-431-R07` · foundation.

<a id="bank-431-039"></a>
#### BANK-431-039 — What distinguishes robot repeatability from an accurate manufacturing process?

**Individual coverage scope:** Include fixturing, parts and sensing.


<a id="domain-431-05"></a>
## Category: Motion control

<a id="catalog-431-r08"></a>
### Servo tuning concepts

Subcategory `CATALOG-431-R08` · intermediate.

<a id="bank-431-040"></a>
#### BANK-431-040 — Why can aggressive motion control cause oscillation instead of precision?

**Individual coverage scope:** Explain feedback and mechanical coupling without tuning settings.


<a id="domain-431-06"></a>
## Category: Industrial sensing

<a id="catalog-431-r09"></a>
### Process instrumentation

Subcategory `CATALOG-431-R09` · intermediate.

<a id="bank-431-041"></a>
#### BANK-431-041 — How can a calibrated sensor measure the wrong process condition?

**Individual coverage scope:** Compare placement, response time and representative sampling.


<a id="domain-431-07"></a>
## Category: Industrial lifecycle

<a id="catalog-431-r10"></a>
### Spare-parts obsolescence

Subcategory `CATALOG-431-R10` · advanced.

<a id="bank-431-042"></a>
#### BANK-431-042 — What happens when a machine depends on a discontinued controller?

**Individual coverage scope:** Compare supported replacement, records and qualified revalidation.


<a id="domain-431-08"></a>
## Category: Industrial assurance

<a id="catalog-431-r11"></a>
### Operator training evidence

Subcategory `CATALOG-431-R11` · advanced.

<a id="bank-431-043"></a>
#### BANK-431-043 — How can a factory distinguish attendance at training from demonstrated operator competence?

**Individual coverage scope:** Define task-specific observation, supervised assessment, refresh needs and records without machine-use procedures.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-431-010"></a>
### pending_topics/0 — The Architecture of Industrial Machines: A Machine Enters Production

**Original question:** Which task and labor conditions led to one machine design?

**Original planning scope:** Trace patents, factory records, and early tests. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Archived pending_topics/0 remains preserved. Its broad framing is routed to existing BANK-431-035; the separately selected named source case does not establish this broader event, mechanism, performance or production history.

**Scoped proposals:** [BANK-431-035](#bank-431-035).

<a id="bank-431-011"></a>
### pending_topics/1 — Industrial Machines: A Defining Industrial Machine

**Original question:** What output and constraints made a model influential?

**Original planning scope:** Use dated specifications and factory data. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 1 (original ID 2, title ?Industrial Machines: A Defining Industrial Machine?) to: How do hydraulic presses, conveyors and CNC systems apply different kinds of controlled motion? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-036](#bank-431-036).

<a id="bank-431-012"></a>
### pending_topics/2 — Industrial Machines: Operators and Maintainers

**Original question:** Which workers' adaptations made a machine productive?

**Original planning scope:** Use documented practice and attributed testimony. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 2 (original ID 3, title ?Industrial Machines: Operators and Maintainers?) to: How can a factory distinguish attendance at training from demonstrated operator competence? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-043](#bank-431-043).

<a id="bank-431-013"></a>
### pending_topics/3 — Industrial Machines: Input, Motion, and Output

**Original question:** How does one machine transform material or energy?

**Original planning scope:** Follow a specific production cycle. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 3 (original ID 4, title ?Industrial Machines: Input, Motion, and Output?) to: How does a machine convert rotary motion into controlled linear movement? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-030](#bank-431-030).

<a id="bank-431-014"></a>
### pending_topics/4 — Industrial Machines: Precision under Wear

**Original question:** How do tolerances, heat, and wear affect repeatability?

**Original planning scope:** Use calibration and inspection data. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 4 (original ID 5, title ?Industrial Machines: Precision under Wear?) to: Why does machine accuracy differ from repeatability? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-031](#bank-431-031).

<a id="bank-431-015"></a>
### pending_topics/5 — Industrial Machines: An Intermittent Machine Fault

**Original question:** Which logs could distinguish sensor, drive, and material causes?

**Original planning scope:** Separate observed symptoms from diagnosis. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 5 (original ID 6, title ?Industrial Machines: An Intermittent Machine Fault?) to: How can preventive maintenance intervals create both savings and waste? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-034](#bank-431-034).

<a id="bank-431-016"></a>
### pending_topics/6 — Industrial Machines: An Automation Upgrade

**Original question:** Did throughput rise without increasing rejects or hazards?

**Original planning scope:** Compare matched runs and workforce impact. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Archived pending_topics/6 remains preserved. Its broad framing is routed to existing BANK-431-034; the separately selected named source case does not establish this broader event, mechanism, performance or production history.

**Scoped proposals:** [BANK-431-034](#bank-431-034).

<a id="bank-431-017"></a>
### pending_topics/7 — Industrial Machines: An Inventor and the Shop Floor

**Original question:** Who proposed, tested, and modified one mechanism?

**Original planning scope:** Use dated designs and team records. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 7 (original ID 8, title ?Industrial Machines: An Inventor and the Shop Floor?) to: How do hydraulic presses, conveyors and CNC systems apply different kinds of controlled motion? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-036](#bank-431-036).

<a id="bank-431-018"></a>
### pending_topics/8 — Industrial Machines: A Machine Incident

**Original question:** What did an official investigation identify and change?

**Original planning scope:** Trace finding, remedy, and later monitoring. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 8 (original ID 9, title ?Industrial Machines: A Machine Incident?) to: What do vibration monitoring and guarding address that operator training alone cannot? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-038](#bank-431-038).

<a id="bank-431-019"></a>
### pending_topics/9 — Industrial Machines: One Production Cell

**Original question:** How do feed, operation, inspection, and unload connect?

**Original planning scope:** Map one machine and operator workflow. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** new_case. Named primary-source case routes archived pending_topics position 9 (original ID 10, title ?Industrial Machines: One Production Cell?) to: What does NIST?s Smart Manufacturing Systems Test Bed connect between a CNC machine and its design and inspection records? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-044](#bank-431-044).

<a id="bank-431-020"></a>
### pending_topics/10 — Industrial Machines: A Machine Type Retired

**Original question:** Which energy, cost, quality, or safety factors explain replacement?

**Original planning scope:** Compare actual factory use. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 10 (original ID 11, title ?Industrial Machines: A Machine Type Retired?) to: What happens when a machine depends on a discontinued controller? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-042](#bank-431-042).

<a id="bank-431-021"></a>
### pending_topics/11 — Industrial Machines: Two Generations of Machines

**Original question:** Which productivity measures are comparable?

**Original planning scope:** Align product, quality threshold, labor, and downtime. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 11 (original ID 12, title ?Industrial Machines: Two Generations of Machines?) to: Why does machine accuracy differ from repeatability? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-031](#bank-431-031).

<a id="bank-431-022"></a>
### pending_topics/12 — Industrial Machines: A Proposed Machine Feature

**Original question:** What prototype and production tests would support adoption?

**Original planning scope:** Define reliability, safety, and maintenance gates. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Archived pending_topics/12 remains preserved. Its broad framing is routed to existing BANK-431-032; the separately selected named source case does not establish this broader event, mechanism, performance or production history.

**Scoped proposals:** [BANK-431-032](#bank-431-032).

<a id="bank-431-023"></a>
### pending_topics/13 — Industrial Machines: Automation Means No Labor?

**Original question:** Which setup, supervision, and repair tasks remain?

**Original planning scope:** Observe one actual shift and records. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 13 (original ID 14, title ?Industrial Machines: Automation Means No Labor??) to: How can a factory distinguish attendance at training from demonstrated operator competence? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-043](#bank-431-043).

<a id="bank-431-024"></a>
### pending_topics/14 — Industrial Machines: Prototype to Factory Floor

**Original question:** How did tests alter a machine before routine use?

**Original planning scope:** Follow drawings, trials, and commissioning. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Archived pending_topics/14 remains preserved. Its broad framing is routed to existing BANK-431-035; the separately selected named source case does not establish this broader event, mechanism, performance or production history.

**Scoped proposals:** [BANK-431-035](#bank-431-035).

<a id="bank-431-025"></a>
### pending_topics/15 — Industrial Machines: Machine or Production Line?

**Original question:** Which throughput depends on supply, inspection, and downstream steps?

**Original planning scope:** Define bottleneck and denominator. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 15 (original ID 16, title ?Industrial Machines: Machine or Production Line??) to: How can one slow machine limit an entire production line? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-032](#bank-431-032).

<a id="bank-431-026"></a>
### pending_topics/16 — Industrial Machines: Signal to Tool Motion

**Original question:** How do controller, drive, transmission, and tool respond?

**Original planning scope:** Use a bounded mode and measured timing. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Archived pending_topics/16 remains preserved. Its broad framing is routed to existing BANK-431-030; the separately selected named source case does not establish this broader event, mechanism, performance or production history.

**Scoped proposals:** [BANK-431-030](#bank-431-030).

<a id="bank-431-027"></a>
### pending_topics/17 — Industrial Machines: Speed and Precision

**Original question:** What quality or wear cost followed higher cycle rate?

**Original planning scope:** Compare matched inputs and inspection outcomes. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 17 (original ID 18, title ?Industrial Machines: Speed and Precision?) to: Why can aggressive motion control cause oscillation instead of precision? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-040](#bank-431-040).

<a id="bank-431-028"></a>
### pending_topics/18 — Industrial Machines: A Guard or Interlock Event

**Original question:** What sequence did inspection establish?

**Original planning scope:** Use official record and avoid bypass instructions. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 18 (original ID 19, title ?Industrial Machines: A Guard or Interlock Event?) to: What do vibration monitoring and guarding address that operator training alone cannot? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-038](#bank-431-038).

<a id="bank-431-029"></a>
### pending_topics/19 — Industrial Machines: Bench Test versus Production

**Original question:** Which loads, materials, or shifts reveal new failures?

**Original planning scope:** Compare trial and service data. Evidence base: dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony.

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived pending_topics position 19 (original ID 20, title ?Industrial Machines: Bench Test versus Production?) to: What makes a machine acceptance test representative of real production? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-035](#bank-431-035).

### trending_topics/0 — Industrial Machines: Record Extremes & Superlatives

**Editorial disposition:** reject_unsubstantiated_superlative. Archived trending_topics position 0 (original ID 21, title ?Industrial Machines: Record Extremes & Superlatives?) lacks a defined ranking measure, comparison set, date and source. Original record remains preserved; no active proposal adopts its ranking/superlative premise.

### trending_topics/1 — Industrial Machines: An Intermittent Machine Fault

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived trending_topics position 1 (original ID 22, title ?Industrial Machines: An Intermittent Machine Fault?) to: How can preventive maintenance intervals create both savings and waste? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-034](#bank-431-034).

### trending_topics/2 — Industrial Machines: An Automation Upgrade

**Editorial disposition:** merge_existing. Archived trending_topics/2 remains preserved. Its broad framing is routed to existing BANK-431-034; the separately selected named source case does not establish this broader event, mechanism, performance or production history.

**Scoped proposals:** [BANK-431-034](#bank-431-034).

### trending_topics/3 — Industrial Machines: Automation Means No Labor?

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived trending_topics position 3 (original ID 24, title ?Industrial Machines: Automation Means No Labor??) to: How can a factory distinguish attendance at training from demonstrated operator competence? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-043](#bank-431-043).

### trending_topics/4 — Industrial Machines: A Machine Incident

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived trending_topics position 4 (original ID 25, title ?Industrial Machines: A Machine Incident?) to: What do vibration monitoring and guarding address that operator training alone cannot? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-038](#bank-431-038).

### trending_topics/5 — Industrial Machines: Operators and Maintainers

**Editorial disposition:** merge_existing. Existing scoped proposal routes archived trending_topics position 5 (original ID 26, title ?Industrial Machines: Operators and Maintainers?) to: How can a factory distinguish attendance at training from demonstrated operator competence? Original archive wording/status remain preserved; this route does not establish rankings, operational performance, incident cause or IDEA readiness.

**Scoped proposals:** [BANK-431-043](#bank-431-043).

### trending_topics/6 — Industrial Machines: Prototype to Factory Floor

**Editorial disposition:** merge_existing. Archived trending_topics/6 remains preserved. Its broad framing is routed to existing BANK-431-035; the separately selected named source case does not establish this broader event, mechanism, performance or production history.

**Scoped proposals:** [BANK-431-035](#bank-431-035).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-431-01"></a>
### Machine systems

<a id="bank-431-001"></a>
- `BANK-431-001` — Hydraulic presses → [BANK-431-036](#bank-431-036)
<a id="bank-431-002"></a>
- `BANK-431-002` — CNC motion control → [BANK-431-036](#bank-431-036)
<a id="bank-431-003"></a>
- `BANK-431-003` — Industrial conveyors → [BANK-431-036](#bank-431-036)

<a id="catalog-431-02"></a>
### Control and monitoring

<a id="bank-431-004"></a>
- `BANK-431-004` — PLC scan cycles → [BANK-431-037](#bank-431-037)
<a id="bank-431-005"></a>
- `BANK-431-005` — Predictive vibration analysis → [BANK-431-038](#bank-431-038)
<a id="bank-431-006"></a>
- `BANK-431-006` — Machine vision inspection → [BANK-431-037](#bank-431-037)

<a id="catalog-431-03"></a>
### Operations

<a id="bank-431-007"></a>
- `BANK-431-007` — Machine guarding → [BANK-431-038](#bank-431-038)
<a id="bank-431-008"></a>
- `BANK-431-008` — Maintenance lockout frameworks → [BANK-431-038](#bank-431-038)
<a id="bank-431-009"></a>
- `BANK-431-009` — Operator training evidence → [BANK-431-043](#bank-431-043)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.


## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- **Concrete case selection for Industrial robotics:** Include fixturing, parts and sensing. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Servo tuning concepts:** Explain feedback and mechanical coupling without tuning settings. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Process instrumentation:** Compare placement, response time and representative sampling. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Spare-parts obsolescence:** Compare supported replacement, records and qualified revalidation. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Operator training evidence:** Define task-specific observation, supervised assessment, refresh needs and records without machine-use procedures. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/431_industrial_machines/NICHE_431_industrial_machines.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
