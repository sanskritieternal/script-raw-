# 332 — Drones: main topic bank

Updated: 2026-10-23 · **12 active BANK proposals · 6 categories · 10 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Multirotors](#catalog-332-r01).
- **Intermediate:** [Navigation](#catalog-332-r02) → [Mapping](#catalog-332-r03) → [Inspection](#catalog-332-r05) → [Visual-inertial estimation](#catalog-332-r07).
- **Advanced:** [Airspace integration](#catalog-332-r04) → [Payload tradeoffs](#catalog-332-r06) → [Disaster surveys](#catalog-332-r08) → [Flight permissions](#catalog-332-r09) → [Flight privacy](#catalog-332-r10).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Flight](#domain-332-01) | 1 | 0 | 0 |
| [Sensing](#domain-332-02) | 0 | 1 | 0 |
| [Applications](#domain-332-03) | 0 | 3 | 1 |
| [Governance](#domain-332-04) | 0 | 0 | 4 |
| [Operations](#domain-332-05) | 0 | 0 | 1 |
| [Navigation](#domain-332-06) | 0 | 1 | 0 |

<a id="domain-332-01"></a>
## Category: Flight

<a id="catalog-332-r01"></a>
### Multirotors

Subcategory `CATALOG-332-R01` · foundation.

<a id="bank-332-030"></a>
#### BANK-332-030 — How does a quadcopter steer without changing the angle of fixed wings?

**Individual coverage scope:** Explain differential thrust, torque and feedback conceptually; exclude hazardous modification instructions.


<a id="domain-332-02"></a>
## Category: Sensing

<a id="catalog-332-r02"></a>
### Navigation

Subcategory `CATALOG-332-R02` · intermediate.

<a id="bank-332-031"></a>
#### BANK-332-031 — Why can a drone lose reliable positioning even with visible satellites?

**Individual coverage scope:** Compare geometry, multipath, interference, sensors and estimation; avoid bypassing geofences or restrictions.


<a id="domain-332-03"></a>
## Category: Applications

<a id="catalog-332-r03"></a>
### Mapping

Subcategory `CATALOG-332-R03` · intermediate.

<a id="bank-332-032"></a>
#### BANK-332-032 — How do overlapping drone photographs become a terrain model?

**Individual coverage scope:** Trace feature matching, camera geometry, ground reference and reconstruction error; distinguish surface from bare-earth models.

<a id="catalog-332-r05"></a>
### Inspection

Subcategory `CATALOG-332-R05` · intermediate.

<a id="bank-332-034"></a>
#### BANK-332-034 — What can drone imagery reveal about infrastructure and what still needs physical inspection?

**Individual coverage scope:** Compare visible defects, occlusion, resolution, measurement and specialist judgment without certifying a structure.

<a id="bank-332-040"></a>
#### BANK-332-040 — How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data?

**Individual coverage scope:** Follow the USGS account of coordinated airspace, sensors, repeat imagery, elevation models and situational products during one eruption; avoid a flight procedure or claim that imagery alone determined rescue or hazard decisions.

**Research follow-up:** [Bounded case and source-access note](332_DRONES_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-332-034](#bank-332-034) — Named 2018 eruption data products versus generic infrastructure imagery.

**Neighboring scope:** [BANK-152-011](../152_volcanoes/IN_DEPTH_TOPIC_BANK.md#bank-152-011) — Drone sensing and data products versus eruption behavior and tourist hazard framing.

<a id="catalog-332-r08"></a>
### Disaster surveys

Subcategory `CATALOG-332-R08` · advanced.

<a id="bank-332-037"></a>
#### BANK-332-037 — Why do drone damage maps require ground context before recovery decisions are made?

**Individual coverage scope:** Compare occlusion, image timing, geolocation, hidden damage, access and local reports without certifying buildings.


<a id="domain-332-04"></a>
## Category: Governance

<a id="catalog-332-r04"></a>
### Airspace integration

Subcategory `CATALOG-332-R04` · advanced.

<a id="bank-332-033"></a>
#### BANK-332-033 — What information must systems share before many drones can operate together?

**Individual coverage scope:** Compare location, intent, separation, failure procedures and authority; reserve current legal requirements for official research.

<a id="bank-332-041"></a>
#### BANK-332-041 — What did NASA's 2019 UTM Technical Capability Level 4 flight demonstration test about coordinating multiple drones?

**Individual coverage scope:** Examine the NASA/FAA test-site demonstration's traffic-management concept and reported gaps; separate research-flight evidence from routine permission for urban or beyond-visual-line-of-sight operations.

**Research follow-up:** [Bounded case and source-access note](332_DRONES_PRIMARY_SOURCE_NOTES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-332-033](#bank-332-033) — Named NASA multi-operator demonstration versus general information-sharing requirements.

**Neighboring scope:** [BANK-330-033](../330_robotics/IN_DEPTH_TOPIC_BANK.md#bank-330-033) — Airspace coordination trial versus robot demonstration reliability generally.

<a id="catalog-332-r09"></a>
### Flight permissions

Subcategory `CATALOG-332-R09` · advanced.

<a id="bank-332-038"></a>
#### BANK-332-038 — Why do beyond-visual-line-of-sight missions require different coordination from a nearby recreational flight?

**Individual coverage scope:** Compare monitoring, communications, airspace, contingency and privacy; require current official requirements before proposing a real operation.

<a id="catalog-332-r10"></a>
### Flight privacy

Subcategory `CATALOG-332-R10` · advanced.

<a id="bank-332-039"></a>
#### BANK-332-039 — How can a drone survey collect useful site information while avoiding unnecessary personal data?

**Individual coverage scope:** Compare task boundaries, camera angle, bystanders, identifiable details, retention, access and disclosure; actual privacy law and flight permission require separate current verification.


<a id="domain-332-05"></a>
## Category: Operations

<a id="catalog-332-r06"></a>
### Payload tradeoffs

Subcategory `CATALOG-332-R06` · advanced.

<a id="bank-332-035"></a>
#### BANK-332-035 — How does carrying an extra sensor change a drone mission's endurance and data quality?

**Individual coverage scope:** Compare mass, power, vibration, flight time and coverage with hypothetical parameters; exclude flight authorization claims.


<a id="domain-332-06"></a>
## Category: Navigation

<a id="catalog-332-r07"></a>
### Visual-inertial estimation

Subcategory `CATALOG-332-R07` · intermediate.

<a id="bank-332-036"></a>
#### BANK-332-036 — Why can combining cameras and inertial sensors help a drone estimate motion without perfect GPS?

**Individual coverage scope:** Trace feature tracking, acceleration, bias, scale and failure conditions conceptually.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-332-010"></a>
### pending_topics/0 — The Architecture of Drones: A Drone Task Takes Flight

**Original question:** Which need and technology made one civilian use feasible?

**Original planning scope:** Use dated operator, regulator, and design records. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 1 (The Architecture of Drones: A Drone Task Takes Flight) through: How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-040](#bank-332-040).

<a id="bank-332-011"></a>
### pending_topics/1 — Drones: A Celebrated Drone Mission Rechecked

**Original question:** What did the aircraft accomplish versus its support crew?

**Original planning scope:** Compare footage, logs, conditions, and ground work. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 2 (Drones: A Celebrated Drone Mission Rechecked) through: How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-040](#bank-332-040).

<a id="bank-332-012"></a>
### pending_topics/2 — Drones: The Ground Crew of a Flight

**Original question:** Who plans, checks, observes, maintains, and processes data?

**Original planning scope:** Credit operators and affected communities. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 3 (Drones: The Ground Crew of a Flight) through: How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-040](#bank-332-040).

<a id="bank-332-013"></a>
### pending_topics/3 — Drones: What Keeps a Drone Flying?

**Original question:** How do sensors, control, motors, battery, and pilot interact?

**Original planning scope:** Trace a lawful mission at a high level. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 4 (Drones: What Keeps a Drone Flying?) through: How does a quadcopter steer without changing the angle of fixed wings? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-030](#bank-332-030).

<a id="bank-332-014"></a>
### pending_topics/4 — Drones: Payload, Range, and Endurance

**Original question:** How does a useful payload change flight performance?

**Original planning scope:** Use measured trials for a named aircraft. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 5 (Drones: Payload, Range, and Endurance) through: How does carrying an extra sensor change a drone mission's endurance and data quality? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-035](#bank-332-035).

<a id="bank-332-015"></a>
### pending_topics/5 — Drones: A Lost Connection Investigated

**Original question:** Which public evidence explains a documented disruption?

**Original planning scope:** Compare signal, environment, power, and flight logs. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 6 (Drones: A Lost Connection Investigated) through: Why can a drone lose reliable positioning even with visible satellites? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-031](#bank-332-031).

<a id="bank-332-016"></a>
### pending_topics/6 — Drones: A New Drone Sensor

**Original question:** Did it improve a defined survey or inspection outcome?

**Original planning scope:** Compare resolution, ground truth, cost, and privacy. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 7 (Drones: A New Drone Sensor) through: How does carrying an extra sensor change a drone mission's endurance and data quality? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-035](#bank-332-035).

<a id="bank-332-017"></a>
### pending_topics/7 — Drones: A Drone Operation Decision

**Original question:** Who authorized a mission and consulted those below?

**Original planning scope:** Trace operator, regulator, client, and local voices. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 8 (Drones: A Drone Operation Decision) through: What did NASA's 2019 UTM Technical Capability Level 4 flight demonstration test about coordinating multiple drones? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-041](#bank-332-041).

<a id="bank-332-018"></a>
### pending_topics/8 — Drones: A Regulatory or Deployment Change

**Original question:** How did one dated decision affect actual flights?

**Original planning scope:** Name jurisdiction, aircraft class, and use. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 9 (Drones: A Regulatory or Deployment Change) through: What did NASA's 2019 UTM Technical Capability Level 4 flight demonstration test about coordinating multiple drones? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-041](#bank-332-041).

<a id="bank-332-019"></a>
### pending_topics/9 — Drones: From Flight Plan to Data Product

**Original question:** What happens between takeoff, sensing, processing, and delivery?

**Original planning scope:** Map one authorized civilian task. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 10 (Drones: From Flight Plan to Data Product) through: How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-040](#bank-332-040).

<a id="bank-332-020"></a>
### pending_topics/10 — Drones: A Drone Service Retired

**Original question:** Which operating, safety, or cost constraint changed viability?

**Original planning scope:** Compare logs and alternatives. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 11 (Drones: A Drone Service Retired) through: Why do beyond-visual-line-of-sight missions require different coordination from a nearby recreational flight? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-038](#bank-332-038).

<a id="bank-332-021"></a>
### pending_topics/11 — Drones: One Aerial Task Across Platforms

**Original question:** Did drones improve time, quality, cost, or risk?

**Original planning scope:** Match weather, area, crew, and output standard. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 12 (Drones: One Aerial Task Across Platforms) through: How does carrying an extra sensor change a drone mission's endurance and data quality? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-035](#bank-332-035).

<a id="bank-332-022"></a>
### pending_topics/12 — Drones: A Proposed Drone Service

**Original question:** What approvals and field evidence are needed before rollout?

**Original planning scope:** Separate trial, waiver, and general availability. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 13 (Drones: A Proposed Drone Service) through: What did NASA's 2019 UTM Technical Capability Level 4 flight demonstration test about coordinating multiple drones? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-041](#bank-332-041).

<a id="bank-332-023"></a>
### pending_topics/13 — Drones: Autonomous Flight Needs No Pilot?

**Original question:** Which supervision and airspace duties still apply?

**Original planning scope:** Check current local rules and actual operation. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 14 (Drones: Autonomous Flight Needs No Pilot?) through: What did NASA's 2019 UTM Technical Capability Level 4 flight demonstration test about coordinating multiple drones? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-041](#bank-332-041).

<a id="bank-332-024"></a>
### pending_topics/14 — Drones: One Authorized Drone Mission

**Original question:** What happened from briefing to delivered result?

**Original planning scope:** Follow consented operator and community accounts. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 15 (Drones: One Authorized Drone Mission) through: How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-040](#bank-332-040).

<a id="bank-332-025"></a>
### pending_topics/15 — Drones: Aircraft and Ground System

**Original question:** Which functions rely on pilot, controller, network, and cloud?

**Original planning scope:** Draw command and data paths. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 16 (Drones: Aircraft and Ground System) through: What did NASA's 2019 UTM Technical Capability Level 4 flight demonstration test about coordinating multiple drones? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-041](#bank-332-041).

<a id="bank-332-026"></a>
### pending_topics/16 — Drones: A Survey Image to Map

**Original question:** Which inputs and processing create a final measurement?

**Original planning scope:** Trace calibration, geolocation, validation, and uncertainty. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 17 (Drones: A Survey Image to Map) through: How do overlapping drone photographs become a terrain model? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-032](#bank-332-032).

<a id="bank-332-027"></a>
### pending_topics/17 — Drones: Flight Time Versus Payload

**Original question:** Which mission outcome improves or degrades with added equipment?

**Original planning scope:** Compare named batteries, aircraft, and conditions. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 18 (Drones: Flight Time Versus Payload) through: How does carrying an extra sensor change a drone mission's endurance and data quality? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-035](#bank-332-035).

<a id="bank-332-028"></a>
### pending_topics/18 — Drones: A Flight Abort

**Original question:** What triggered one documented safe termination?

**Original planning scope:** Use incident report and avoid operational evasion detail. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** merge_existing. Existing question covers archived pitch 19 (Drones: A Flight Abort) through: Why do beyond-visual-line-of-sight missions require different coordination from a nearby recreational flight? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-038](#bank-332-038).

<a id="bank-332-029"></a>
### pending_topics/19 — Drones: A Perfect-Weather Trial

**Original question:** What weather, terrain, light, and signal conditions were excluded?

**Original planning scope:** State test envelope and safety margins. Evidence base: current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts.

**Editorial disposition:** new_case. Named sourced case covers archived pitch 20 (Drones: A Perfect-Weather Trial) through: How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-040](#bank-332-040).

### trending_topics/0 — Drones: Record Extremes & Superlatives

**Editorial disposition:** new_case. Named sourced case covers archived pitch 21 (Drones: Record Extremes & Superlatives) through: How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-040](#bank-332-040).

### trending_topics/1 — Drones: A Lost Connection Investigated

**Editorial disposition:** merge_existing. Existing question covers archived pitch 22 (Drones: A Lost Connection Investigated) through: Why can a drone lose reliable positioning even with visible satellites? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-031](#bank-332-031).

### trending_topics/2 — Drones: A New Drone Sensor

**Editorial disposition:** merge_existing. Existing question covers archived pitch 23 (Drones: A New Drone Sensor) through: How does carrying an extra sensor change a drone mission's endurance and data quality? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-035](#bank-332-035).

### trending_topics/3 — Drones: Autonomous Flight Needs No Pilot?

**Editorial disposition:** new_case. Named sourced case covers archived pitch 24 (Drones: Autonomous Flight Needs No Pilot?) through: What did NASA's 2019 UTM Technical Capability Level 4 flight demonstration test about coordinating multiple drones? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-041](#bank-332-041).

### trending_topics/4 — Drones: A Regulatory or Deployment Change

**Editorial disposition:** new_case. Named sourced case covers archived pitch 25 (Drones: A Regulatory or Deployment Change) through: What did NASA's 2019 UTM Technical Capability Level 4 flight demonstration test about coordinating multiple drones? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-041](#bank-332-041).

### trending_topics/5 — Drones: The Ground Crew of a Flight

**Editorial disposition:** new_case. Named sourced case covers archived pitch 26 (Drones: The Ground Crew of a Flight) through: How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-040](#bank-332-040).

### trending_topics/6 — Drones: One Authorized Drone Mission

**Editorial disposition:** new_case. Named sourced case covers archived pitch 27 (Drones: One Authorized Drone Mission) through: How did USGS drone surveys turn Kīlauea's 2018 eruption imagery into scientific and response data? The original archive wording remains in topics_status.json and does not establish a superlative, safety finding or production readiness.

**Scoped proposals:** [BANK-332-040](#bank-332-040).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-332-01"></a>
### Flight systems

<a id="bank-332-001"></a>
- `BANK-332-001` — Multirotor control → [BANK-332-030](#bank-332-030)
<a id="bank-332-002"></a>
- `BANK-332-002` — Visual-inertial navigation → [BANK-332-036](#bank-332-036)
<a id="bank-332-003"></a>
- `BANK-332-003` — Payload endurance tradeoffs → [BANK-332-035](#bank-332-035)

<a id="catalog-332-02"></a>
### Uses

<a id="bank-332-004"></a>
- `BANK-332-004` — Crop mapping → [BANK-332-032](#bank-332-032)
<a id="bank-332-005"></a>
- `BANK-332-005` — Infrastructure inspection → [BANK-332-034](#bank-332-034)
<a id="bank-332-006"></a>
- `BANK-332-006` — Disaster damage surveys → [BANK-332-037](#bank-332-037)

<a id="catalog-332-03"></a>
### Governance

<a id="bank-332-007"></a>
- `BANK-332-007` — Airspace permissions → [BANK-332-038](#bank-332-038)
<a id="bank-332-008"></a>
- `BANK-332-008` — Flight privacy → [BANK-332-039](#bank-332-039)
<a id="bank-332-009"></a>
- `BANK-332-009` — Beyond-visual-line-of-sight requirements → [BANK-332-038](#bank-332-038)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [330 Robotics](../330_robotics/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [331 Humanoid Robots](../331_humanoid_robots/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [333 Brain-Computer Interfaces](../333_brain-computer_interfaces/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [334 Virtual Worlds](../334_virtual_worlds/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [335 Digital Humans](../335_digital_humans/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [342 AI Filmmaking](../342_ai_filmmaking/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Coverage remaining open

- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.
- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.
- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/332_drones/NICHE_332_drones.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
