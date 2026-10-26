# 160 — Data Centers & Infrastructure: main topic bank

Updated: 2026-10-23 · **34 active BANK proposals · 7 categories · 8 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Original bounded cases and mechanisms](#catalog-160-r01) → [Compute, storage and networks](#catalog-160-r05).
- **Intermediate:** [Original bounded cases and mechanisms](#catalog-160-r02) → [Original bounded cases and mechanisms](#catalog-160-r03) → [Reliability and capacity](#catalog-160-r06).
- **Advanced:** [Original bounded cases and mechanisms](#catalog-160-r04) → [Siting and accountability](#catalog-160-r07) → [Dated rack and utility capacity cases](#catalog-160-r08).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Tier 1: Foundational Frameworks](#domain-160-01) | 5 | 0 | 0 |
| [Tier 2: Practical Mechanics & Channels](#domain-160-02) | 0 | 5 | 0 |
| [Tier 3: Advanced Methodologies & Frameworks](#domain-160-03) | 0 | 6 | 0 |
| [Tier 4: Enterprise Strategy & Deep Mastery](#domain-160-04) | 0 | 0 | 4 |
| [Infrastructure foundations](#domain-160-05) | 4 | 0 | 0 |
| [Infrastructure operation](#domain-160-06) | 0 | 4 | 0 |
| [Infrastructure choices](#domain-160-07) | 0 | 0 | 6 |

<a id="domain-160-01"></a>
## Category: Tier 1: Foundational Frameworks

<a id="catalog-160-r01"></a>
### Original bounded cases and mechanisms

Subcategory `CATALOG-160-R01` · foundation.

<a id="bank-160-010"></a>
#### BANK-160-010 — The Megawatt Facility: Anatomy of a 100-Megawatt Hyperscale Data Center

**Video question:** What does it take to build and operate a windowless facility that consumes as much electricity as a city of 100,000 homes to power the global cloud?

**Individual coverage scope:** High-voltage substation step-down transformers, rows of thousands of compute racks, industrial cooling towers, physical multi-factor biometric security, and 99.999% uptime engineering.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-011"></a>
#### BANK-160-011 — PUE Deconstructed: The Single Metric That Measures Data Center Efficiency

**Video question:** How did Google and hyperscalers drop Power Usage Effectiveness from a wasteful 2.0 down to a near-perfect 1.1?

**Individual coverage scope:** Total facility power vs IT equipment power math, parasitic cooling and lighting overhead, hot aisle vs cold aisle containment physics, and machine learning cooling optimization.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-012"></a>
#### BANK-160-012 — Uptime Tiers I to IV: What It Costs to Guarantee 99.999% 'Five Nines' Reliability

**Video question:** What is the difference between a facility that allows 28 hours of downtime a year and a fault-tolerant Tier IV facility that allows just 26 seconds?

**Individual coverage scope:** Uptime Institute standards, N+1 vs 2N+1 component redundancy, dual-powered server power supplies (PSUs), concurrent maintainability without taking loads offline, and CAPEX differences.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-013"></a>
#### BANK-160-013 — The Zero-Second Blackout: How UPS Systems Bridge the Gap Between Grid Failure and Diesel Generators

**Video question:** When lightning knocks out the regional electrical grid, how do millions of servers keep processing transactions without a single millisecond flicker?

**Individual coverage scope:** Double-conversion static battery UPS banks, rotary mechanical flywheel kinetic energy buffers, automatic transfer switches (ATS), and massive 2-megawatt diesel generators firing up in 10 seconds.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-014"></a>
#### BANK-160-014 — Hot Aisles vs Cold Aisles: The Aerodynamic Science of Not Baking Server Racks

**Video question:** Why does mixing exhaust air with intake air destroy data center efficiency, and how do physical plastic curtains save millions in electricity?

**Individual coverage scope:** Airflow short-circuiting and recirculation, blanking panel discipline, raised floor pressurized plenums vs overhead ducting, and computational fluid dynamics (CFD) thermal modeling.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-160-02"></a>
## Category: Tier 2: Practical Mechanics & Channels

<a id="catalog-160-r02"></a>
### Original bounded cases and mechanisms

Subcategory `CATALOG-160-R02` · intermediate.

<a id="bank-160-015"></a>
#### BANK-160-015 — Liquid Cooling Revolution: Why AI Compute Chips Are Drowning in Fluorochemicals and Water

**Video question:** When an AI server rack consumes 100 kilowatts of electricity, why does air cooling completely fail, forcing engineers to pump chilled fluid directly onto chips?

**Individual coverage scope:** Thermal conductivity of water (24x air), direct-to-chip copper cold plates, two-phase immersion cooling where dielectric fluids boil and condense, and manifold plumbing reliability.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-016"></a>
#### BANK-160-016 — Spine-Leaf Networks: The Non-Blocking Optical Fabric Inside Modern Cloud Clusters

**Video question:** How do thousands of servers communicate with each other with uniform microsecond latency without creating network chokepoints?

**Individual coverage scope:** Replacing traditional 3-tier hierarchical networks with 2-tier Clos topologies, Equal-Cost Multi-Path (ECMP) routing, Top-of-Rack (ToR) switches, 400G optical transceivers, and east-west traffic dominance.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-017"></a>
#### BANK-160-017 — Subsea Cables: The 800,000-Mile Fiber Optic Nervous System Under the Oceans

**Video question:** Why does 99% of all intercontinental internet traffic travel through garden-hose-sized glass fibers lying in the mud of the ocean floor rather than satellites?

**Individual coverage scope:** Optical fiber total internal reflection, erbium-doped fiber amplifiers (EDFAs) boosting signals every 60 km, armored cable laying ships, shark bite and anchor hazards, and landing stations.

**Neighboring scope:** [BANK-129-035](../129_internet_history/IN_DEPTH_TOPIC_BANK.md#bank-129-035) — Data-center infrastructure dependence differs from internet history of undersea access.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-018"></a>
#### BANK-160-018 — The Data Center Water Crisis: Millions of Gallons Evaporated for Cooling

**Video question:** Why do massive cloud data centers in drought-stricken Arizona and Utah consume millions of gallons of potable municipal drinking water every day?

**Individual coverage scope:** Evaporative cooling tower thermodynamics, Water Usage Effectiveness (WUE) metrics, adiabatic cooling economizers, community water utility backlash, and closed-loop dry cooler transitions.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-019"></a>
#### BANK-160-019 — Northern Virginia: Inside 'Data Center Alley' Where 70% of the World's Internet Flows

**Video question:** Why did Loudoun County, Virginia, become the digital capital of planet Earth, housing over 25 million square feet of operational server halls?

**Individual coverage scope:** Early MAE-East internet exchange hub, cheap commercial Dominion Energy power rates, dense dark fiber clustering, tax incentives, and the current electrical grid transmission capacity wall.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-160-03"></a>
## Category: Tier 3: Advanced Methodologies & Frameworks

<a id="catalog-160-r03"></a>
### Original bounded cases and mechanisms

Subcategory `CATALOG-160-R03` · intermediate.

<a id="bank-160-020"></a>
#### BANK-160-020 — The AI Power Shock: Why Artificial Intelligence is Breaking National Electrical Grids

**Video question:** Why are tech giants being told by electric utility companies that they must wait 7 years to get grid connections for new AI training facilities?

**Individual coverage scope:** NVIDIA H100/B200 cluster power spikes, a single ChatGPT prompt consuming 10x the power of a Google search, grid interconnection queues, keeping retiring coal plants alive, and transmission line shortages.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-021"></a>
#### BANK-160-021 — Small Modular Reactors (SMRs): Can Nuclear Power Solve the Hyperscale Energy Crunch?

**Video question:** Why are Microsoft, Amazon, and Google investing billions in nuclear startups and signing contracts to co-locate data centers directly next to nuclear reactors?

**Individual coverage scope:** Baseload 24/7 zero-carbon power requirements, factory-fabricated SMR designs, the Three Mile Island Unit 1 restart deal, regulatory licensing hurdles, and dedicated private microgrids.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTE_DATA_CENTER_CASES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-113-025](../113_energy_power/IN_DEPTH_TOPIC_BANK.md#bank-113-025) — The data-center scope concerns power procurement; energy covers SMR investment and generation claims.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-022"></a>
#### BANK-160-022 — Dark Fiber and High-Frequency Trading: The Race for Nanoseconds Between Chicago and New York

**Video question:** Why did financial firms spend hundreds of millions tunneling straight fiber through mountains and building laser towers just to shave 3 milliseconds off trading orders?

**Individual coverage scope:** Spread Networks' direct fiber path, microwave and millimeter-wave line-of-sight networks traveling at light speed in air vs glass (30% latency advantage), and algorithmic market making.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-023"></a>
#### BANK-160-023 — Project Natick: What Microsoft Learned Sinking a Data Center to the Bottom of the Ocean

**Video question:** Why did a pressurized steel capsule holding 864 servers submerged off the coast of Scotland experience one-eighth the hardware failure rate of land facilities?

**Individual coverage scope:** Free ocean water thermal cooling, dry pure nitrogen atmosphere eliminating oxygen corrosion, lack of human movement and vibrations, and rapid coastal city deployment potential.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-024"></a>
#### BANK-160-024 — Fire Suppression in Server Halls: Inergen Gas vs Water Mist Systems

**Video question:** How do you extinguish an electrical fire inside a room filled with tens of millions of dollars of live electronics without shorting them out or deafening the hard drives?

**Individual coverage scope:** Inert gas systems (Inergen, FM-200, Novec 1230) suffocating fire by lowering oxygen without suffocating humans, acoustic shockwave mufflers protecting hard drives, and double-interlock pre-action sprinklers.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-025"></a>
#### BANK-160-025 — Physical Security at the Edge: Mantraps, Biometrics, and Faraday Cages

**Video question:** What happens if a rogue actor attempts to physically break into an enterprise or government intelligence data center?

**Individual coverage scope:** K-rated anti-ram perimeter crash fences, dual-door mantraps with weight sensors, iris and biometric palm scanners, strict compartmentalized cage access, and TEMPEST-certified electromagnetic shielding.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-160-04"></a>
## Category: Tier 4: Enterprise Strategy & Deep Mastery

<a id="catalog-160-r04"></a>
### Original bounded cases and mechanisms

Subcategory `CATALOG-160-R04` · advanced.

<a id="bank-160-026"></a>
#### BANK-160-026 — Waste Heat Recovery: Using Cloud Servers to Warm Cities, Swimming Pools, and Greenhouses

**Video question:** Why let billions of BTUs of thermal heat evaporate into the atmosphere when it can be pumped into municipal district heating systems to warm homes?

**Individual coverage scope:** Low-grade heat exchange thermodynamics, European regulations mandating district heat reuse (Stockholm, Paris), warming municipal swimming pools, and circular energy economies.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-027"></a>
#### BANK-160-027 — Edge Data Centers: Why 5G and Autonomous Driving Demand Micro-Facilities Every 5 Miles

**Video question:** Why can't self-driving cars and robotic surgical arms wait 50 milliseconds to query a distant hyperscale data center 500 miles away?

**Individual coverage scope:** Speed-of-light latency physics, modular containerized edge data pods installed at cell towers, decentralized content delivery networks (CDNs), and distributed microgrid resilience.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-028"></a>
#### BANK-160-028 — The $1 Billion Facility: The CapEx and OpEx Breakdown of a 100 MW Campus

**Video question:** Where does $1 billion go when developing a cloud campus, and why does electricity account for 75% of operational lifetime costs?

**Individual coverage scope:** Shell construction vs MEP (Mechanical, Electrical, Plumbing) equipment split, generator and transformer procurement, server hardware 3-year refresh cycles, power tariff structures, and real estate leasing models.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.

<a id="bank-160-029"></a>
#### BANK-160-029 — The Masterclass on Data Center Engineering: Designing the Ultimate Cloud Campus

**Video question:** How does an infrastructure director design a resilient, sustainable, scalable 500-megawatt computing campus that will operate flawlessly for 30 years?

**Individual coverage scope:** Holistic integration of high-voltage utility interconnections, closed-loop liquid thermal topologies, modular scalable building blocks, automated DCIM (Data Center Infrastructure Management) telemetry, and future-proofing for next-generation silicon.

Source: preserved local roadmap proposal. Its original framing is not a verified finding.


<a id="domain-160-05"></a>
## Category: Infrastructure foundations

<a id="catalog-160-r05"></a>
### Compute, storage and networks

Subcategory `CATALOG-160-R05` · foundation.

<a id="bank-160-030"></a>
#### BANK-160-030 — What happens inside a data center when someone requests a web page?

**Individual coverage scope:** Trace network entry, compute, storage and response in a schematic system; distinguish the facility from the application.

<a id="bank-160-031"></a>
#### BANK-160-031 — Why does a server rack require more planning than stacking computers?

**Individual coverage scope:** Compare electrical supply, heat, cabling, airflow, weight and service access conceptually.

<a id="bank-160-032"></a>
#### BANK-160-032 — What is the difference between keeping data and keeping a service available?

**Individual coverage scope:** Separate storage durability, redundancy, backups, application dependencies and recovery.

<a id="bank-160-033"></a>
#### BANK-160-033 — How does a data center turn electricity consumption into a cooling requirement?

**Individual coverage scope:** Explain heat flows, airflow and cooling loops with a labeled energy balance.


<a id="domain-160-06"></a>
## Category: Infrastructure operation

<a id="catalog-160-r06"></a>
### Reliability and capacity

Subcategory `CATALOG-160-R06` · intermediate.

<a id="bank-160-034"></a>
#### BANK-160-034 — Why can redundant equipment still share a single point of failure?

**Individual coverage scope:** Trace dependencies on power, control, network, maintenance and human procedures through a hypothetical fault tree.

<a id="bank-160-035"></a>
#### BANK-160-035 — What does power usage effectiveness measure and what does it leave out?

**Individual coverage scope:** Separate facility overhead, IT demand, location, utilization, water and useful computing output.

<a id="bank-160-036"></a>
#### BANK-160-036 — How can software scheduling change a facility's physical resource use?

**Individual coverage scope:** Compare utilization, workload placement, peaks, cooling and latency constraints without assuming idle power is zero.

<a id="bank-160-037"></a>
#### BANK-160-037 — Why do backups need recovery tests to be meaningful?

**Individual coverage scope:** Explain restoration scope, dependencies, recovery point, recovery time and evidence of a successful drill.


<a id="domain-160-07"></a>
## Category: Infrastructure choices

<a id="catalog-160-r07"></a>
### Siting and accountability

Subcategory `CATALOG-160-R07` · advanced.

<a id="bank-160-038"></a>
#### BANK-160-038 — How should a data center's water use be compared across climates?

**Individual coverage scope:** Distinguish withdrawal, consumption, cooling design, water stress and seasonal demand.

**Neighboring scope:** [BANK-001-203](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-203) — Facility water comparison belongs here; the AI bank tests onsite versus indirect water accounting.

<a id="bank-160-039"></a>
#### BANK-160-039 — What can a community ask before a large data center is built nearby?

**Individual coverage scope:** Map grid upgrades, water, land, jobs, noise, taxes and public disclosure with dated local records.

<a id="bank-160-040"></a>
#### BANK-160-040 — How can an outage propagate across services hosted in different buildings?

**Individual coverage scope:** Trace identity, DNS, control planes, shared providers and configuration dependencies at a systems level.

<a id="bank-160-041"></a>
#### BANK-160-041 — What does a credible claim about carbon-free computing need to specify?

**Individual coverage scope:** Compare hourly versus annual matching, location, boundaries, embodied impacts and backup power.

<a id="catalog-160-r08"></a>
### Dated rack and utility capacity cases

Subcategory `CATALOG-160-R08` · advanced.

<a id="bank-160-042"></a>
#### BANK-160-042 — What does NVIDIA's GB200 NVL72 reference design require of a high-density rack?

**Individual coverage scope:** Read NVIDIA's 2024 OCP design description and current hardware guide for approximate rack power, hybrid liquid/air heat paths and facility interfaces; distinguish a particular reference configuration from every AI server rack.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTE_DATA_CENTER_CASES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-001-206](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-206) — The named rack design is a facility integration case; the AI bank explains general air and liquid heat transfer.

<a id="bank-160-043"></a>
#### BANK-160-043 — What did Dominion Energy report about Northern Virginia data-center connections in 2024?

**Individual coverage scope:** Use the utility's dated sustainability report to identify connected facilities and combined capacity, then separate completed connections from requested load, waiting time and forecasts for future grid constraints.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTE_DATA_CENTER_CASES.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-001-205](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-205) — Dominion?s connection record concerns regional utility capacity; the AI bank distinguishes nuclear agreements from delivered energy.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

### pending_topics/0 — The Megawatt Facility: Anatomy of a 100-Megawatt Hyperscale Data Center

**Original question:** What does it take to build and operate a windowless facility that consumes as much electricity as a city of 100,000 homes to power the global cloud?

**Original planning scope:** High-voltage substation step-down transformers, rows of thousands of compute racks, industrial cooling towers, physical multi-factor biometric security, and 99.999% uptime engineering.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-010](#bank-160-010).

### pending_topics/1 — PUE Deconstructed: The Single Metric That Measures Data Center Efficiency

**Original question:** How did Google and hyperscalers drop Power Usage Effectiveness from a wasteful 2.0 down to a near-perfect 1.1?

**Original planning scope:** Total facility power vs IT equipment power math, parasitic cooling and lighting overhead, hot aisle vs cold aisle containment physics, and machine learning cooling optimization.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-011](#bank-160-011), [BANK-160-035](#bank-160-035).

### pending_topics/2 — Uptime Tiers I to IV: What It Costs to Guarantee 99.999% 'Five Nines' Reliability

**Original question:** What is the difference between a facility that allows 28 hours of downtime a year and a fault-tolerant Tier IV facility that allows just 26 seconds?

**Original planning scope:** Uptime Institute standards, N+1 vs 2N+1 component redundancy, dual-powered server power supplies (PSUs), concurrent maintainability without taking loads offline, and CAPEX differences.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-012](#bank-160-012).

### pending_topics/3 — The Zero-Second Blackout: How UPS Systems Bridge the Gap Between Grid Failure and Diesel Generators

**Original question:** When lightning knocks out the regional electrical grid, how do millions of servers keep processing transactions without a single millisecond flicker?

**Original planning scope:** Double-conversion static battery UPS banks, rotary mechanical flywheel kinetic energy buffers, automatic transfer switches (ATS), and massive 2-megawatt diesel generators firing up in 10 seconds.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-013](#bank-160-013).

### pending_topics/4 — Hot Aisles vs Cold Aisles: The Aerodynamic Science of Not Baking Server Racks

**Original question:** Why does mixing exhaust air with intake air destroy data center efficiency, and how do physical plastic curtains save millions in electricity?

**Original planning scope:** Airflow short-circuiting and recirculation, blanking panel discipline, raised floor pressurized plenums vs overhead ducting, and computational fluid dynamics (CFD) thermal modeling.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-014](#bank-160-014).

### pending_topics/5 — Liquid Cooling Revolution: Why AI Compute Chips Are Drowning in Fluorochemicals and Water

**Original question:** When an AI server rack consumes 100 kilowatts of electricity, why does air cooling completely fail, forcing engineers to pump chilled fluid directly onto chips?

**Original planning scope:** Thermal conductivity of water (24x air), direct-to-chip copper cold plates, two-phase immersion cooling where dielectric fluids boil and condense, and manifold plumbing reliability.

**Editorial disposition:** existing_scope. General cooling is already scoped; the named NVL72 reference rack adds a specific load and heat-path case.

**Scoped proposals:** [BANK-160-015](#bank-160-015), [BANK-160-042](#bank-160-042).

### pending_topics/6 — Spine-Leaf Networks: The Non-Blocking Optical Fabric Inside Modern Cloud Clusters

**Original question:** How do thousands of servers communicate with each other with uniform microsecond latency without creating network chokepoints?

**Original planning scope:** Replacing traditional 3-tier hierarchical networks with 2-tier Clos topologies, Equal-Cost Multi-Path (ECMP) routing, Top-of-Rack (ToR) switches, 400G optical transceivers, and east-west traffic dominance.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-016](#bank-160-016).

### pending_topics/7 — Subsea Cables: The 800,000-Mile Fiber Optic Nervous System Under the Oceans

**Original question:** Why does 99% of all intercontinental internet traffic travel through garden-hose-sized glass fibers lying in the mud of the ocean floor rather than satellites?

**Original planning scope:** Optical fiber total internal reflection, erbium-doped fiber amplifiers (EDFAs) boosting signals every 60 km, armored cable laying ships, shark bite and anchor hazards, and landing stations.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-017](#bank-160-017).

### pending_topics/8 — The Data Center Water Crisis: Millions of Gallons Evaporated for Cooling

**Original question:** Why do massive cloud data centers in drought-stricken Arizona and Utah consume millions of gallons of potable municipal drinking water every day?

**Original planning scope:** Evaporative cooling tower thermodynamics, Water Usage Effectiveness (WUE) metrics, adiabatic cooling economizers, community water utility backlash, and closed-loop dry cooler transitions.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-018](#bank-160-018), [BANK-160-038](#bank-160-038).

### pending_topics/9 — Northern Virginia: Inside 'Data Center Alley' Where 70% of the World's Internet Flows

**Original question:** Why did Loudoun County, Virginia, become the digital capital of planet Earth, housing over 25 million square feet of operational server halls?

**Original planning scope:** Early MAE-East internet exchange hub, cheap commercial Dominion Energy power rates, dense dark fiber clustering, tax incentives, and the current electrical grid transmission capacity wall.

**Editorial disposition:** existing_scope. Northern Virginia siting exists; the utility's 2024 connection report adds a dated capacity record.

**Scoped proposals:** [BANK-160-019](#bank-160-019), [BANK-160-039](#bank-160-039), [BANK-160-043](#bank-160-043).

### pending_topics/10 — The AI Power Shock: Why Artificial Intelligence is Breaking National Electrical Grids

**Original question:** Why are tech giants being told by electric utility companies that they must wait 7 years to get grid connections for new AI training facilities?

**Original planning scope:** NVIDIA H100/B200 cluster power spikes, a single ChatGPT prompt consuming 10x the power of a Google search, grid interconnection queues, keeping retiring coal plants alive, and transmission line shortages.

**Editorial disposition:** existing_scope. Utility connection claims need a dated load boundary; the 2024 reported completions are distinct from predicted waits.

**Scoped proposals:** [BANK-160-020](#bank-160-020), [BANK-160-043](#bank-160-043).

### pending_topics/11 — Small Modular Reactors (SMRs): Can Nuclear Power Solve the Hyperscale Energy Crunch?

**Original question:** Why are Microsoft, Amazon, and Google investing billions in nuclear startups and signing contracts to co-locate data centers directly next to nuclear reactors?

**Original planning scope:** Baseload 24/7 zero-carbon power requirements, factory-fabricated SMR designs, the Three Mile Island Unit 1 restart deal, regulatory licensing hurdles, and dedicated private microgrids.

**Editorial disposition:** existing_scope. The data-center energy scope remains local; the AI bank already has the primary nuclear-agreement timing distinction.

**Scoped proposals:** [BANK-160-021](#bank-160-021), [BANK-001-205](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-205).

### pending_topics/12 — Dark Fiber and High-Frequency Trading: The Race for Nanoseconds Between Chicago and New York

**Original question:** Why did financial firms spend hundreds of millions tunneling straight fiber through mountains and building laser towers just to shave 3 milliseconds off trading orders?

**Original planning scope:** Spread Networks' direct fiber path, microwave and millimeter-wave line-of-sight networks traveling at light speed in air vs glass (30% latency advantage), and algorithmic market making.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-022](#bank-160-022).

### pending_topics/13 — Project Natick: What Microsoft Learned Sinking a Data Center to the Bottom of the Ocean

**Original question:** Why did a pressurized steel capsule holding 864 servers submerged off the coast of Scotland experience one-eighth the hardware failure rate of land facilities?

**Original planning scope:** Free ocean water thermal cooling, dry pure nitrogen atmosphere eliminating oxygen corrosion, lack of human movement and vibrations, and rapid coastal city deployment potential.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-023](#bank-160-023), [BANK-160-037](#bank-160-037).

### pending_topics/14 — Fire Suppression in Server Halls: Inergen Gas vs Water Mist Systems

**Original question:** How do you extinguish an electrical fire inside a room filled with tens of millions of dollars of live electronics without shorting them out or deafening the hard drives?

**Original planning scope:** Inert gas systems (Inergen, FM-200, Novec 1230) suffocating fire by lowering oxygen without suffocating humans, acoustic shockwave mufflers protecting hard drives, and double-interlock pre-action sprinklers.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-024](#bank-160-024).

### pending_topics/15 — Physical Security at the Edge: Mantraps, Biometrics, and Faraday Cages

**Original question:** What happens if a rogue actor attempts to physically break into an enterprise or government intelligence data center?

**Original planning scope:** K-rated anti-ram perimeter crash fences, dual-door mantraps with weight sensors, iris and biometric palm scanners, strict compartmentalized cage access, and TEMPEST-certified electromagnetic shielding.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-025](#bank-160-025).

### pending_topics/16 — Waste Heat Recovery: Using Cloud Servers to Warm Cities, Swimming Pools, and Greenhouses

**Original question:** Why let billions of BTUs of thermal heat evaporate into the atmosphere when it can be pumped into municipal district heating systems to warm homes?

**Original planning scope:** Low-grade heat exchange thermodynamics, European regulations mandating district heat reuse (Stockholm, Paris), warming municipal swimming pools, and circular energy economies.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-026](#bank-160-026).

### pending_topics/17 — Edge Data Centers: Why 5G and Autonomous Driving Demand Micro-Facilities Every 5 Miles

**Original question:** Why can't self-driving cars and robotic surgical arms wait 50 milliseconds to query a distant hyperscale data center 500 miles away?

**Original planning scope:** Speed-of-light latency physics, modular containerized edge data pods installed at cell towers, decentralized content delivery networks (CDNs), and distributed microgrid resilience.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-027](#bank-160-027).

### pending_topics/18 — The $1 Billion Facility: The CapEx and OpEx Breakdown of a 100 MW Campus

**Original question:** Where does $1 billion go when developing a cloud campus, and why does electricity account for 75% of operational lifetime costs?

**Original planning scope:** Shell construction vs MEP (Mechanical, Electrical, Plumbing) equipment split, generator and transformer procurement, server hardware 3-year refresh cycles, power tariff structures, and real estate leasing models.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-028](#bank-160-028).

### pending_topics/19 — The Masterclass on Data Center Engineering: Designing the Ultimate Cloud Campus

**Original question:** How does an infrastructure director design a resilient, sustainable, scalable 500-megawatt computing campus that will operate flawlessly for 30 years?

**Original planning scope:** Holistic integration of high-voltage utility interconnections, closed-loop liquid thermal topologies, modular scalable building blocks, automated DCIM (Data Center Infrastructure Management) telemetry, and future-proofing for next-generation silicon.

**Editorial disposition:** existing_scope. Existing original BANK question is the primary home; numerical scale and performance claims require dated source checks.

**Scoped proposals:** [BANK-160-029](#bank-160-029), [BANK-160-034](#bank-160-034), [BANK-160-041](#bank-160-041).

### trending_topics/0 — The Three Mile Island Nuclear Restart: Constellation and Microsoft's 20-Year Power Deal

**Editorial disposition:** existing_scope. Power procurement is local, while BANK-001-205 covers why the Constellation-Microsoft agreement does not prove delivery timing.

**Scoped proposals:** [BANK-160-021](#bank-160-021), [BANK-001-205](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md#bank-001-205).

### trending_topics/1 — The 100 kW Server Rack: How NVIDIA's Blackwell NVL72 is Breaking Data Center Cooling

**Editorial disposition:** new_case. General liquid cooling plus the named GB200 NVL72 rack cover the 100-kW trend; exact loads depend on configuration.

**Scoped proposals:** [BANK-160-015](#bank-160-015), [BANK-160-042](#bank-160-042).

### trending_topics/2 — Northern Virginia at the Brink: Dominion Energy's Power Grid Capacity Bottleneck

**Editorial disposition:** new_case. Northern Virginia siting and interconnection scopes plus Dominion?s 2024 connected-load record cover this trend.

**Scoped proposals:** [BANK-160-019](#bank-160-019), [BANK-160-020](#bank-160-020), [BANK-160-043](#bank-160-043).

### trending_topics/3 — Subsea Data Centers Go Commercial: Can Ocean Cooling Solve the AI Heat Problem?

**Editorial disposition:** existing_scope. Project Natick is already the original named subsea-facility case; commercialization is not verified.

**Scoped proposals:** [BANK-160-023](#bank-160-023).

### trending_topics/4 — The Subsea Cable Cut Crisis: How Anchor Drags in the Red Sea Disrupted Global Internet

**Editorial disposition:** existing_scope. Subsea cables are already scoped as infrastructure; Red Sea cuts need operator-specific outage evidence before a separate case.

**Scoped proposals:** [BANK-160-017](#bank-160-017).

### trending_topics/5 — Direct-to-Chip vs Immersion Cooling: The War Inside High-Density Server Halls

**Editorial disposition:** existing_scope. Direct-liquid and air pathways are covered; an immersion comparison needs specified system designs.

**Scoped proposals:** [BANK-160-015](#bank-160-015), [BANK-160-042](#bank-160-042).

### trending_topics/6 — The $10 Billion Campus: Inside the Largest AI Data Center Projects on Earth

**Editorial disposition:** existing_scope. Facility costs and community questions are existing scopes; the $10 billion superlative needs a named audited project.

**Scoped proposals:** [BANK-160-028](#bank-160-028), [BANK-160-039](#bank-160-039).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-160-01"></a>
### Facility systems

<a id="bank-160-001"></a>
- `BANK-160-001` — Server rack power density → [BANK-160-031](#bank-160-031)
<a id="bank-160-002"></a>
- `BANK-160-002` — Cooling architectures → [BANK-160-033](#bank-160-033)
<a id="bank-160-003"></a>
- `BANK-160-003` — Uninterruptible power systems → [BANK-160-013](#bank-160-013)

<a id="catalog-160-02"></a>
### Network and storage

<a id="bank-160-004"></a>
- `BANK-160-004` — East-west data traffic → [BANK-160-016](#bank-160-016)
<a id="bank-160-005"></a>
- `BANK-160-005` — Storage redundancy → [BANK-160-032](#bank-160-032)
<a id="bank-160-006"></a>
- `BANK-160-006` — Disaster recovery objectives → [BANK-160-037](#bank-160-037)

<a id="catalog-160-03"></a>
### Environmental accounting

<a id="bank-160-007"></a>
- `BANK-160-007` — PUE interpretation → [BANK-160-035](#bank-160-035)
<a id="bank-160-008"></a>
- `BANK-160-008` — Water-use metrics → [BANK-160-038](#bank-160-038)
<a id="bank-160-009"></a>
- `BANK-160-009` — Location and grid-emissions differences → [BANK-160-041](#bank-160-041)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [113 Energy & Power](../113_energy_power/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [114 Water](../114_water/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [157 Materials Science](../157_materials_science/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [158 Batteries & Energy Storage](../158_batteries_energy_storage/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [161 Electricity & Electronics](../161_electricity_electronics/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [357 Gemology](../357_gemology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- **Case and source readiness:** Select dated jurisdictions, editions, named sites, populations or product versions for the active proposals. Inspect actual sources before making factual claims; no research or production readiness was certified.
- **Reviewed starter branches and primary-home boundaries:** All original starter concepts now have explicit individual-scope targets. See the starter crosswalk below and Scripts/editorial_review_002_184.json for scope evidence and semantic pair decisions; follow the primary-home referrals after consolidation.
- **Regional and participant variation:** Compare less-visible regions, languages, participants and contrary cases within this niche; record substantive distinctions before adding another proposal.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/160_data_centers_infrastructure/NICHE_160_data_centers_infrastructure.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
