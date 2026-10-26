# 330 — Robotics: main topic bank

Updated: 2026-10-23 · **12 active BANK proposals · 8 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Control loops](#catalog-330-r01) → [Kinematics](#catalog-330-r05).
- **Intermediate:** [Uncertainty](#catalog-330-r02) → [Compliance](#catalog-330-r03) → [Agricultural perception](#catalog-330-r06) → [Sensor fusion](#catalog-330-r08) → [Warehouses](#catalog-330-r09) → [Motion constraints](#catalog-330-r11).
- **Advanced:** [Deployment](#catalog-330-r04) → [Automation costs](#catalog-330-r07) → [Collaborative arms](#catalog-330-r10).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-330-01) | 1 | 0 | 0 |
| [Perception](#domain-330-02) | 0 | 2 | 0 |
| [Design](#domain-330-03) | 0 | 1 | 0 |
| [Evaluation](#domain-330-04) | 0 | 0 | 1 |
| [Geometry](#domain-330-05) | 1 | 0 | 0 |
| [Applications](#domain-330-06) | 0 | 3 | 1 |
| [Economics](#domain-330-07) | 0 | 0 | 1 |
| [Planning](#domain-330-08) | 0 | 1 | 0 |

<a id="domain-330-01"></a>
## Category: Foundations

<a id="catalog-330-r01"></a>
### Control loops

Subcategory `CATALOG-330-R01` · foundation.

<a id="bank-330-030"></a>
#### BANK-330-030 — How does a robot turn a desired movement into corrected motion?

**Individual coverage scope:** Trace sensing, error, actuation and feedback using a simplified arm or mobile robot.


<a id="domain-330-02"></a>
## Category: Perception

<a id="catalog-330-r02"></a>
### Uncertainty

Subcategory `CATALOG-330-R02` · intermediate.

<a id="bank-330-031"></a>
#### BANK-330-031 — Why can a robot recognize an object but still fail to grasp it?

**Individual coverage scope:** Compare depth, occlusion, material, pose uncertainty and gripper limits.

<a id="catalog-330-r08"></a>
### Sensor fusion

Subcategory `CATALOG-330-R08` · intermediate.

<a id="bank-330-037"></a>
#### BANK-330-037 — Why can combining two imperfect robot sensors improve an estimate without making it certain?

**Individual coverage scope:** Compare noise, bias, synchronization, calibration and correlated errors.


<a id="domain-330-03"></a>
## Category: Design

<a id="catalog-330-r03"></a>
### Compliance

Subcategory `CATALOG-330-R03` · intermediate.

<a id="bank-330-032"></a>
#### BANK-330-032 — When can a softer robot outperform a rigid precise mechanism?

**Individual coverage scope:** Compare contact, tolerance, payload, control and task context without universal design rankings.


<a id="domain-330-04"></a>
## Category: Evaluation

<a id="catalog-330-r04"></a>
### Deployment

Subcategory `CATALOG-330-R04` · advanced.

<a id="bank-330-033"></a>
#### BANK-330-033 — Why does a successful robotics demonstration not prove reliable real-world operation?

**Individual coverage scope:** Compare trial selection, resets, environment variation, failure rate and human intervention.


<a id="domain-330-05"></a>
## Category: Geometry

<a id="catalog-330-r05"></a>
### Kinematics

Subcategory `CATALOG-330-R05` · foundation.

<a id="bank-330-034"></a>
#### BANK-330-034 — How do degrees of freedom constrain where a robot arm can reach?

**Individual coverage scope:** Compare joints, links, workspace, singular configurations and task requirements through a diagram.


<a id="domain-330-06"></a>
## Category: Applications

<a id="catalog-330-r06"></a>
### Agricultural perception

Subcategory `CATALOG-330-R06` · intermediate.

<a id="bank-330-035"></a>
#### BANK-330-035 — Why is recognizing crops outdoors harder than recognizing objects in a controlled factory?

**Individual coverage scope:** Compare lighting, occlusion, seasons, biological variation and motion.

<a id="catalog-330-r09"></a>
### Warehouses

Subcategory `CATALOG-330-R09` · intermediate.

<a id="bank-330-038"></a>
#### BANK-330-038 — How do warehouse mobile robots coordinate movement in changing aisles?

**Individual coverage scope:** Compare maps, localization, task allocation, obstacles and human interaction without operator-specific instructions.

<a id="bank-330-041"></a>
#### BANK-330-041 — What did Amazon's 2022 Proteus announcement establish about robots moving GoCarts in shared facility space?

**Individual coverage scope:** Trace the announced outbound GoCart handling task, human-shared navigation claim and planned deployment scope; distinguish the operator announcement from independent safety, reliability, injury or labor-outcome evidence.

**Research follow-up:** [Bounded case and source-access note](CASE_SOURCE_NOTES.md). This does not change proposal or production status.

<a id="catalog-330-r10"></a>
### Collaborative arms

Subcategory `CATALOG-330-R10` · advanced.

<a id="bank-330-039"></a>
#### BANK-330-039 — Why does calling a robot collaborative not certify every surrounding task as safe?

**Individual coverage scope:** Compare tooling, payload, contact, speed, workspace and system-level risk assessment; exclude safety certification.


<a id="domain-330-07"></a>
## Category: Economics

<a id="catalog-330-r07"></a>
### Automation costs

Subcategory `CATALOG-330-R07` · advanced.

<a id="bank-330-036"></a>
#### BANK-330-036 — What belongs in a robot's deployment cost beyond its purchase price?

**Individual coverage scope:** Compare integration, tooling, downtime, maintenance, training and task variability using explicit assumptions.


<a id="domain-330-08"></a>
## Category: Planning

<a id="catalog-330-r11"></a>
### Motion constraints

Subcategory `CATALOG-330-R11` · intermediate.

<a id="bank-330-040"></a>
#### BANK-330-040 — Why can a collision-free path in a robot simulator fail when executed by the real machine?

**Individual coverage scope:** Compare model error, joint limits, payload deformation, control timing and changing obstacles; distinguish path geometry from dynamic feasibility.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-330-010"></a>
### pending_topics/0 — The Architecture of Robotics: A Robot Enters a Workplace

**Original question:** Which task and constraint drove one early robot deployment?

**Original planning scope:** Use dated design, safety, and production records. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Distinct bounded case proposed.. Named dated operator record provides a bounded subject; outcome claims need independent evidence.

**Scoped proposals:** [BANK-330-041](#bank-330-041).

<a id="bank-330-011"></a>
### pending_topics/1 — Robotics: A Famous Robot Demonstration Rechecked

**Original question:** Which tasks did it complete outside a staged demonstration?

**Original planning scope:** Compare trials, conditions, and operator assistance. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-033](#bank-330-033).

<a id="bank-330-012"></a>
### pending_topics/2 — Robotics: Technicians Behind Automation

**Original question:** Who installs, calibrates, repairs, and supervises the system?

**Original planning scope:** Use consented worker accounts and maintenance records. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-036](#bank-330-036).

<a id="bank-330-013"></a>
### pending_topics/3 — Robotics: Sense, Plan, Act

**Original question:** How do sensor readings become a robot movement?

**Original planning scope:** Trace one bounded task through control and actuation. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-030](#bank-330-030).

<a id="bank-330-014"></a>
### pending_topics/4 — Robotics: Precision Versus Robustness

**Original question:** Can a system handle changed objects and environments?

**Original planning scope:** Measure repeatability across defined conditions. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-033](#bank-330-033).

<a id="bank-330-015"></a>
### pending_topics/5 — Robotics: An Unexpected Robot Stop

**Original question:** Which sensor, software, power, or human condition explains an incident?

**Original planning scope:** Use logs and public reports without unsafe troubleshooting steps. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-038](#bank-330-038).

<a id="bank-330-016"></a>
### pending_topics/6 — Robotics: A New Gripper or Sensor

**Original question:** Did it improve a defined task and at what cost?

**Original planning scope:** Compare matched objects, speed, errors, and safety. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-031](#bank-330-031).

<a id="bank-330-017"></a>
### pending_topics/7 — Robotics: A Robot Design Decision

**Original question:** Who set the task and safety requirements?

**Original planning scope:** Trace decisions and affected workers. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-034](#bank-330-034).

<a id="bank-330-018"></a>
### pending_topics/8 — Robotics: A Robot Deployment Timeline

**Original question:** What happened from pilot to routine use?

**Original planning scope:** Compare acceptance tests with operational outcomes. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Distinct bounded case proposed.. Named dated operator record provides a bounded subject; outcome claims need independent evidence.

**Scoped proposals:** [BANK-330-041](#bank-330-041).

<a id="bank-330-019"></a>
### pending_topics/9 — Robotics: A Robot Cell in Operation

**Original question:** How do controller, sensors, actuators, guards, and operator interact?

**Original planning scope:** Map one application and its safe boundaries. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-038](#bank-330-038).

<a id="bank-330-020"></a>
### pending_topics/10 — Robotics: Why a Robot Was Retired

**Original question:** Which performance, maintenance, or task change drove retirement?

**Original planning scope:** Use operating logs and alternatives. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-036](#bank-330-036).

<a id="bank-330-021"></a>
### pending_topics/11 — Robotics: One Task Across Robot Generations

**Original question:** How did throughput, quality, safety, and labor change?

**Original planning scope:** Compare matched tasks and environments. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-038](#bank-330-038).

<a id="bank-330-022"></a>
### pending_topics/12 — Robotics: A Proposed Robot Capability

**Original question:** What test would demonstrate field reliability?

**Original planning scope:** Define task, variation, intervention, and failure threshold. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-033](#bank-330-033).

<a id="bank-330-023"></a>
### pending_topics/13 — Robotics: Autonomous Means No Humans?

**Original question:** Which setup, monitoring, and exception work remains?

**Original planning scope:** Observe a complete workflow. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Distinct bounded case proposed.. Named dated operator record provides a bounded subject; outcome claims need independent evidence.

**Scoped proposals:** [BANK-330-041](#bank-330-041).

<a id="bank-330-024"></a>
### pending_topics/14 — Robotics: A Shift with a Robot

**Original question:** How does one team use and recover the system day to day?

**Original planning scope:** Use consented observation and logs. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Distinct bounded case proposed.. Named dated operator record provides a bounded subject; outcome claims need independent evidence.

**Scoped proposals:** [BANK-330-041](#bank-330-041).

<a id="bank-330-025"></a>
### pending_topics/15 — Robotics: What the Robot Controls

**Original question:** Where do machine, fixtures, software, operator, and facility responsibilities end?

**Original planning scope:** Draw one deployed system boundary. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-030](#bank-330-030).

<a id="bank-330-026"></a>
### pending_topics/16 — Robotics: A Pick-and-Place Cycle

**Original question:** What inputs and outputs shape a single safe cycle?

**Original planning scope:** Trace sensors, decisions, movement, and stop conditions. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-031](#bank-330-031).

<a id="bank-330-027"></a>
### pending_topics/17 — Robotics: Speed and Contact Safety

**Original question:** How do performance goals interact with protection measures?

**Original planning scope:** Use applicable standards and tested configuration. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-039](#bank-330-039).

<a id="bank-330-028"></a>
### pending_topics/18 — Robotics: A Failed Grasp

**Original question:** What conditions cause an object to be dropped or damaged?

**Original planning scope:** Review tests and mitigation, not hazardous operating steps. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-031](#bank-330-031).

<a id="bank-330-029"></a>
### pending_topics/19 — Robotics: Lab Task Versus Working Floor

**Original question:** Which changes in lighting, objects, wear, and people alter results?

**Original planning scope:** State trial conditions and sample size. Evidence base: NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-033](#bank-330-033).

### trending_topics/0 — Robotics: Record Extremes & Superlatives

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-033](#bank-330-033).

### trending_topics/1 — Robotics: An Unexpected Robot Stop

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-038](#bank-330-038).

### trending_topics/2 — Robotics: A New Gripper or Sensor

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-031](#bank-330-031).

### trending_topics/3 — Robotics: Autonomous Means No Humans?

**Editorial disposition:** Distinct bounded case proposed.. Named dated operator record provides a bounded subject; outcome claims need independent evidence.

**Scoped proposals:** [BANK-330-041](#bank-330-041).

### trending_topics/4 — Robotics: A Robot Deployment Timeline

**Editorial disposition:** Distinct bounded case proposed.. Named dated operator record provides a bounded subject; outcome claims need independent evidence.

**Scoped proposals:** [BANK-330-041](#bank-330-041).

### trending_topics/5 — Robotics: Technicians Behind Automation

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-330-036](#bank-330-036).

### trending_topics/6 — Robotics: A Shift with a Robot

**Editorial disposition:** Distinct bounded case proposed.. Named dated operator record provides a bounded subject; outcome claims need independent evidence.

**Scoped proposals:** [BANK-330-041](#bank-330-041).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-330-01"></a>
### Robot fundamentals

<a id="bank-330-001"></a>
- `BANK-330-001` — Kinematics and degrees of freedom → [BANK-330-034](#bank-330-034)
<a id="bank-330-002"></a>
- `BANK-330-002` — Feedback control → [BANK-330-030](#bank-330-030)
<a id="bank-330-003"></a>
- `BANK-330-003` — Sensor fusion in general-purpose robots → [BANK-330-037](#bank-330-037)

<a id="catalog-330-02"></a>
### Applications

<a id="bank-330-004"></a>
- `BANK-330-004` — Warehouse mobile robots → [BANK-330-038](#bank-330-038)
<a id="bank-330-005"></a>
- `BANK-330-005` — Collaborative industrial arms → [BANK-330-039](#bank-330-039)
<a id="bank-330-006"></a>
- `BANK-330-006` — Agricultural robotic perception → [BANK-330-035](#bank-330-035)

<a id="catalog-330-03"></a>
### Evaluation

<a id="bank-330-007"></a>
- `BANK-330-007` — Human safety standards → [BANK-330-039](#bank-330-039)
<a id="bank-330-008"></a>
- `BANK-330-008` — Reliability outside laboratory settings → [BANK-330-033](#bank-330-033)
<a id="bank-330-009"></a>
- `BANK-330-009` — Automation cost assumptions → [BANK-330-036](#bank-330-036)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [331 Humanoid Robots](../331_humanoid_robots/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [332 Drones](../332_drones/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [333 Brain-Computer Interfaces](../333_brain-computer_interfaces/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [334 Virtual Worlds](../334_virtual_worlds/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [335 Digital Humans](../335_digital_humans/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [342 AI Filmmaking](../342_ai_filmmaking/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/330_robotics/NICHE_330_robotics.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
