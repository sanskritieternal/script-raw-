# 331 — Humanoid Robots: main topic bank

Updated: 2026-10-23 · **12 active BANK proposals · 11 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Human environments](#catalog-331-r01).
- **Intermediate:** [Balance](#catalog-331-r02) → [Hands](#catalog-331-r03) → [Retargeting](#catalog-331-r05) → [Foot estimation](#catalog-331-r07) → [Occlusion](#catalog-331-r09).
- **Advanced:** [Autonomy](#catalog-331-r04) → [Endurance](#catalog-331-r06) → [Whole body](#catalog-331-r08) → [Interaction](#catalog-331-r10) → [Fall testing](#catalog-331-r11).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Form](#domain-331-01) | 2 | 0 | 0 |
| [Movement](#domain-331-02) | 0 | 1 | 0 |
| [Manipulation](#domain-331-03) | 0 | 1 | 0 |
| [Evaluation](#domain-331-04) | 0 | 0 | 1 |
| [Motion](#domain-331-05) | 0 | 1 | 0 |
| [Power](#domain-331-06) | 0 | 0 | 1 |
| [Contact](#domain-331-07) | 0 | 1 | 0 |
| [Control](#domain-331-08) | 0 | 0 | 1 |
| [Perception](#domain-331-09) | 0 | 1 | 0 |
| [Work](#domain-331-10) | 0 | 0 | 1 |
| [Embodiment](#domain-331-11) | 0 | 0 | 1 |

<a id="domain-331-01"></a>
## Category: Form

<a id="catalog-331-r01"></a>
### Human environments

Subcategory `CATALOG-331-R01` · foundation.

<a id="bank-331-030"></a>
#### BANK-331-030 — Why build a humanoid robot instead of a wheeled machine?

**Individual coverage scope:** Compare stairs, tools, workspaces, energy and complexity; distinguish task justification from visual resemblance.

<a id="bank-331-041"></a>
#### BANK-331-041 — What changed when Boston Dynamics retired hydraulic Atlas and announced an electric Atlas in 2024?

**Individual coverage scope:** Compare the company-announced platform transition, intended industrial testing and anticipated manipulator designs; separate announced goals from demonstrated task performance, independent reliability and commercial deployment.

**Research follow-up:** [Bounded case and source-access note](CASE_SOURCE_NOTES.md). This does not change proposal or production status.


<a id="domain-331-02"></a>
## Category: Movement

<a id="catalog-331-r02"></a>
### Balance

Subcategory `CATALOG-331-R02` · intermediate.

<a id="bank-331-031"></a>
#### BANK-331-031 — Why is standing still an active control problem for a humanoid robot?

**Individual coverage scope:** Trace support regions, joint torque, sensing, disturbances and compliant contact conceptually.


<a id="domain-331-03"></a>
## Category: Manipulation

<a id="catalog-331-r03"></a>
### Hands

Subcategory `CATALOG-331-R03` · intermediate.

<a id="bank-331-032"></a>
#### BANK-331-032 — Why can a robot hand with many joints still struggle with everyday objects?

**Individual coverage scope:** Compare sensing, friction, coordination, deformation and training distribution.


<a id="domain-331-04"></a>
## Category: Evaluation

<a id="catalog-331-r04"></a>
### Autonomy

Subcategory `CATALOG-331-R04` · advanced.

<a id="bank-331-033"></a>
#### BANK-331-033 — How can viewers tell which parts of a humanoid demonstration are autonomous?

**Individual coverage scope:** Compare teleoperation, preplanned motion, environmental preparation, interventions and disclosed evaluation protocols.


<a id="domain-331-05"></a>
## Category: Motion

<a id="catalog-331-r05"></a>
### Retargeting

Subcategory `CATALOG-331-R05` · intermediate.

<a id="bank-331-034"></a>
#### BANK-331-034 — Why can't a humanoid simply replay a human's captured joint motions?

**Individual coverage scope:** Compare proportions, joint ranges, balance, contact and actuator limits without unsafe control instructions.


<a id="domain-331-06"></a>
## Category: Power

<a id="catalog-331-r06"></a>
### Endurance

Subcategory `CATALOG-331-R06` · advanced.

<a id="bank-331-035"></a>
#### BANK-331-035 — Why does standing time reveal little about a humanoid robot's useful working endurance?

**Individual coverage scope:** Compare loads, walking, manipulation, computation, cooling and recharge under specified task cycles.


<a id="domain-331-07"></a>
## Category: Contact

<a id="catalog-331-r07"></a>
### Foot estimation

Subcategory `CATALOG-331-R07` · intermediate.

<a id="bank-331-036"></a>
#### BANK-331-036 — How does a humanoid estimate whether a foot is securely supporting weight?

**Individual coverage scope:** Compare force sensing, joint estimates, slip, terrain and contact uncertainty.


<a id="domain-331-08"></a>
## Category: Control

<a id="catalog-331-r08"></a>
### Whole body

Subcategory `CATALOG-331-R08` · advanced.

<a id="bank-331-037"></a>
#### BANK-331-037 — Why can moving a humanoid's arm require changes in its legs and torso?

**Individual coverage scope:** Compare balance, momentum, reach, contacts and actuator constraints in a whole-body control problem.


<a id="domain-331-09"></a>
## Category: Perception

<a id="catalog-331-r09"></a>
### Occlusion

Subcategory `CATALOG-331-R09` · intermediate.

<a id="bank-331-038"></a>
#### BANK-331-038 — How does a humanoid continue a task when its hands block its cameras?

**Individual coverage scope:** Compare camera placement, memory, touch, prediction and uncertainty rather than assuming full visibility.


<a id="domain-331-10"></a>
## Category: Work

<a id="catalog-331-r10"></a>
### Interaction

Subcategory `CATALOG-331-R10` · advanced.

<a id="bank-331-039"></a>
#### BANK-331-039 — What must be measured before a humanoid can work reliably alongside people?

**Individual coverage scope:** Compare communication, predictability, task boundaries, failures, supervision and ergonomic effects without deployment approval.


<a id="domain-331-11"></a>
## Category: Embodiment

<a id="catalog-331-r11"></a>
### Fall testing

Subcategory `CATALOG-331-R11` · advanced.

<a id="bank-331-040"></a>
#### BANK-331-040 — How should a humanoid reliability evaluation account for falls and near-falls rather than report only successful tasks?

**Individual coverage scope:** Compare exposure hours, surfaces, interventions, damage, reset labor and reporting exclusions using a documented evaluation plan; exclude physical fall-test procedures.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-331-010"></a>
### pending_topics/0 — The Architecture of Humanoid Robots: Why Give a Robot Human Form?

**Original question:** Which intended task justified one humanoid design?

**Original planning scope:** Use dated research goals and deployment evidence. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-030](#bank-331-030).

<a id="bank-331-011"></a>
### pending_topics/1 — Humanoid Robots: A Humanoid Demo Rechecked

**Original question:** What was autonomous, scripted, or remotely assisted?

**Original planning scope:** Review disclosed setup and repeated trials. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-033](#bank-331-033).

<a id="bank-331-012"></a>
### pending_topics/2 — Humanoid Robots: Operators Behind the Humanoid

**Original question:** Who teleoperates, labels data, repairs hardware, and keeps it balanced?

**Original planning scope:** Use consented worker accounts and documentation. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-039](#bank-331-039).

<a id="bank-331-013"></a>
### pending_topics/3 — Humanoid Robots: Balance and Manipulation

**Original question:** How does a humanoid coordinate sensors, joints, and contact?

**Original planning scope:** Explain one bounded movement and its limits. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-037](#bank-331-037).

<a id="bank-331-014"></a>
### pending_topics/4 — Humanoid Robots: General-Purpose Claims Tested

**Original question:** How many tasks transfer without rebuilding the setup?

**Original planning scope:** Compare task diversity, interventions, and repeatability. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-033](#bank-331-033).

<a id="bank-331-015"></a>
### pending_topics/5 — Humanoid Robots: A Fall in a Demonstration

**Original question:** Which conditions could explain a documented loss of balance?

**Original planning scope:** Use video limits, telemetry, and operator account. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-040](#bank-331-040).

<a id="bank-331-016"></a>
### pending_topics/6 — Humanoid Robots: A New Humanoid Hand

**Original question:** Does dexterity improve useful work rather than appearance?

**Original planning scope:** Measure objects handled, force, failures, and time. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-032](#bank-331-032).

<a id="bank-331-017"></a>
### pending_topics/7 — Humanoid Robots: Choosing the Human Shape

**Original question:** Who argued for that form and which users were consulted?

**Original planning scope:** Trace design records and alternatives. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-030](#bank-331-030).

<a id="bank-331-018"></a>
### pending_topics/8 — Humanoid Robots: A Humanoid Pilot in Practice

**Original question:** What changed between announcement and actual deployment?

**Original planning scope:** Build dated task and safety timeline. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-039](#bank-331-039).

<a id="bank-331-019"></a>
### pending_topics/9 — Humanoid Robots: A Humanoid Completes a Task

**Original question:** How do perception, locomotion, grasping, and supervision combine?

**Original planning scope:** Follow one real workflow. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-033](#bank-331-033).

<a id="bank-331-020"></a>
### pending_topics/10 — Humanoid Robots: A Humanoid Program Changes Direction

**Original question:** What technical or market evidence drove redesign?

**Original planning scope:** Compare goals, trials, cost, and customer needs. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Distinct bounded case proposed.. Named dated operator record provides a bounded subject; outcome claims need independent evidence.

**Scoped proposals:** [BANK-331-041](#bank-331-041).

<a id="bank-331-021"></a>
### pending_topics/11 — Humanoid Robots: Two Humanoid Generations

**Original question:** Did endurance, manipulation, safety, or intervention improve?

**Original planning scope:** Use matched tasks and test conditions. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Distinct bounded case proposed.. Named dated operator record provides a bounded subject; outcome claims need independent evidence.

**Scoped proposals:** [BANK-331-041](#bank-331-041).

<a id="bank-331-022"></a>
### pending_topics/12 — Humanoid Robots: A Humanoid Work Claim

**Original question:** Which field evidence would justify scale-up?

**Original planning scope:** Require task rate, safety, maintenance, and economics. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-033](#bank-331-033).

<a id="bank-331-023"></a>
### pending_topics/13 — Humanoid Robots: Human Shape Means Human Ability?

**Original question:** Which physical and cognitive tasks remain unproven?

**Original planning scope:** Separate appearance from measured capabilities. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-030](#bank-331-030).

<a id="bank-331-024"></a>
### pending_topics/14 — Humanoid Robots: One Shift with a Humanoid Pilot

**Original question:** What work did it complete and what did humans rescue?

**Original planning scope:** Use consented observation and full task accounting. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-039](#bank-331-039).

<a id="bank-331-025"></a>
### pending_topics/15 — Humanoid Robots: Autonomy Versus Remote Help

**Original question:** Which decisions came from onboard system, cloud, or operator?

**Original planning scope:** Draw control and disclosure boundary. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-033](#bank-331-033).

<a id="bank-331-026"></a>
### pending_topics/16 — Humanoid Robots: A Humanoid Picking an Object

**Original question:** What observations and commands precede a safe grasp?

**Original planning scope:** Trace system states without hazardous directions. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-032](#bank-331-032).

<a id="bank-331-027"></a>
### pending_topics/17 — Humanoid Robots: Bipedal Form or Stable Base

**Original question:** When does walking justify its energy and stability cost?

**Original planning scope:** Compare a matched task and environment. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-030](#bank-331-030).

<a id="bank-331-028"></a>
### pending_topics/18 — Humanoid Robots: A Failed Balance Recovery

**Original question:** How does the system limit harm after a loss of stability?

**Original planning scope:** Use safe trials and protective design evidence. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-040](#bank-331-040).

<a id="bank-331-029"></a>
### pending_topics/19 — Humanoid Robots: Demo Choreography Versus Routine Work

**Original question:** Which props, resets, and human interventions change the result?

**Original planning scope:** Request full trial denominator. Evidence base: dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts.

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-033](#bank-331-033).

### trending_topics/0 — Humanoid Robots: Record Extremes & Superlatives

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-031](#bank-331-031).

### trending_topics/1 — Humanoid Robots: A Fall in a Demonstration

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-040](#bank-331-040).

### trending_topics/2 — Humanoid Robots: A New Humanoid Hand

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-032](#bank-331-032).

### trending_topics/3 — Humanoid Robots: Human Shape Means Human Ability?

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-030](#bank-331-030).

### trending_topics/4 — Humanoid Robots: A Humanoid Pilot in Practice

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-039](#bank-331-039).

### trending_topics/5 — Humanoid Robots: Operators Behind the Humanoid

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-039](#bank-331-039).

### trending_topics/6 — Humanoid Robots: One Shift with a Humanoid Pilot

**Editorial disposition:** Routed to existing scoped BANK proposal.. The archived framing merges into this narrower active scope; generic trend, record and universal capability claims are not adopted.

**Scoped proposals:** [BANK-331-039](#bank-331-039).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-331-01"></a>
### Embodied design

<a id="bank-331-001"></a>
- `BANK-331-001` — Bipedal balance → [BANK-331-031](#bank-331-031)
<a id="bank-331-002"></a>
- `BANK-331-002` — Whole-body control → [BANK-331-037](#bank-331-037)
<a id="bank-331-003"></a>
- `BANK-331-003` — Dexterous manipulation → [BANK-331-032](#bank-331-032)

<a id="catalog-331-02"></a>
### Perception

<a id="bank-331-004"></a>
- `BANK-331-004` — Foot contact estimation → [BANK-331-036](#bank-331-036)
<a id="bank-331-005"></a>
- `BANK-331-005` — Human-motion retargeting → [BANK-331-034](#bank-331-034)
<a id="bank-331-006"></a>
- `BANK-331-006` — Vision under occlusion → [BANK-331-038](#bank-331-038)

<a id="catalog-331-03"></a>
### Deployment

<a id="bank-331-007"></a>
- `BANK-331-007` — Demonstration versus autonomous operation → [BANK-331-033](#bank-331-033)
<a id="bank-331-008"></a>
- `BANK-331-008` — Worker interaction → [BANK-331-039](#bank-331-039)
<a id="bank-331-009"></a>
- `BANK-331-009` — Battery endurance under real tasks → [BANK-331-035](#bank-331-035)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [330 Robotics](../330_robotics/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
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

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/331_humanoid_robots/NICHE_331_humanoid_robots.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
