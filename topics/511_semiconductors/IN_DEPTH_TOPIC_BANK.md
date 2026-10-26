# 511 — Semiconductors: main topic bank

Updated: 2026-10-23 · **15 active BANK proposals · 8 categories · 12 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Chip foundations](#catalog-511-r01) → [Semiconductor devices](#catalog-511-r04) → [Power semiconductors](#catalog-511-r08).
- **Intermediate:** [Manufacturing systems](#catalog-511-r02) → [Semiconductor devices](#catalog-511-r05) → [Memory architectures](#catalog-511-r07).
- **Advanced:** [Industry constraints](#catalog-511-r03) → [Chip industry](#catalog-511-r06) → [Chiplets](#catalog-511-r09) → [Semiconductor metrology](#catalog-511-r10) → [Memory architectures](#catalog-511-r11) → [Yield management](#catalog-511-r12).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-511-01) | 2 | 0 | 0 |
| [Methods and applications](#domain-511-02) | 0 | 3 | 0 |
| [Systems and interpretation](#domain-511-03) | 0 | 0 | 3 |
| [Chip systems](#domain-511-04) | 0 | 1 | 1 |
| [Chip applications](#domain-511-05) | 1 | 0 | 0 |
| [Chip integration](#domain-511-06) | 0 | 0 | 1 |
| [Manufacturing evidence](#domain-511-07) | 0 | 0 | 2 |
| [Semiconductor manufacturing evidence](#domain-511-08) | 0 | 0 | 1 |

<a id="domain-511-01"></a>
## Category: Foundations

<a id="catalog-511-r01"></a>
### Chip foundations

Subcategory `CATALOG-511-R01` · foundation.

<a id="bank-511-030"></a>
#### BANK-511-030 — Why does a transistor need a controllable channel rather than merely conductive material?

**Individual coverage scope:** Explain switching and leakage conceptually.

<a id="catalog-511-r04"></a>
### Semiconductor devices

Subcategory `CATALOG-511-R04` · foundation.

<a id="bank-511-036"></a>
#### BANK-511-036 — How do PN junctions and MOSFETs use carrier behavior differently?

**Individual coverage scope:** Compare rectification and controlled conduction conceptually.


<a id="domain-511-02"></a>
## Category: Methods and applications

<a id="catalog-511-r02"></a>
### Manufacturing systems

Subcategory `CATALOG-511-R02` · intermediate.

<a id="bank-511-032"></a>
#### BANK-511-032 — Why can a tiny manufacturing defect disable a large chip?

**Individual coverage scope:** Compare defect density, die area and redundancy.

<a id="bank-511-033"></a>
#### BANK-511-033 — How do chip design rules translate manufacturing limits into layout constraints?

**Individual coverage scope:** Explain spacing and process variation without proprietary parameters.

<a id="catalog-511-r05"></a>
### Semiconductor devices

Subcategory `CATALOG-511-R05` · intermediate.

<a id="bank-511-037"></a>
#### BANK-511-037 — How do lithography, deposition and etching combine into a repeated fabrication sequence?

**Individual coverage scope:** Map functions and yield constraints without proprietary process recipes.


<a id="domain-511-03"></a>
## Category: Systems and interpretation

<a id="catalog-511-r03"></a>
### Industry constraints

Subcategory `CATALOG-511-R03` · advanced.

<a id="bank-511-034"></a>
#### BANK-511-034 — What does advanced packaging change when transistor scaling becomes harder?

**Individual coverage scope:** Compare interconnects, thermal limits and system integration.

<a id="bank-511-035"></a>
#### BANK-511-035 — How can water, power and skilled labor constrain a new semiconductor fab?

**Individual coverage scope:** Map infrastructure dependencies and ramp-up assumptions.

<a id="catalog-511-r06"></a>
### Chip industry

Subcategory `CATALOG-511-R06` · advanced.

<a id="bank-511-038"></a>
#### BANK-511-038 — How do foundry models and packaging bottlenecks shape supply-chain concentration?

**Individual coverage scope:** Separate design ownership, fabrication and integration.


<a id="domain-511-04"></a>
## Category: Chip systems

<a id="catalog-511-r07"></a>
### Memory architectures

Subcategory `CATALOG-511-R07` · intermediate.

<a id="bank-511-039"></a>
#### BANK-511-039 — How do SRAM and DRAM trade density, speed and refresh requirements?

**Individual coverage scope:** Connect device structure and system use conceptually.

<a id="catalog-511-r11"></a>
### Memory architectures

Subcategory `CATALOG-511-R11` · advanced.

<a id="bank-511-043"></a>
#### BANK-511-043 — Why can moving data between memory and compute dominate a chip system's energy?

**Individual coverage scope:** Compare architecture and workload rather than transistor count.


<a id="domain-511-05"></a>
## Category: Chip applications

<a id="catalog-511-r08"></a>
### Power semiconductors

Subcategory `CATALOG-511-R08` · foundation.

<a id="bank-511-040"></a>
#### BANK-511-040 — Why do power switches face different design goals from logic transistors?

**Individual coverage scope:** Compare voltage, current, heat and switching loss.


<a id="domain-511-06"></a>
## Category: Chip integration

<a id="catalog-511-r09"></a>
### Chiplets

Subcategory `CATALOG-511-R09` · advanced.

<a id="bank-511-041"></a>
#### BANK-511-041 — How can chiplets reduce some manufacturing risks while adding interface challenges?

**Individual coverage scope:** Trace yields, communication and package integration.


<a id="domain-511-07"></a>
## Category: Manufacturing evidence

<a id="catalog-511-r10"></a>
### Semiconductor metrology

Subcategory `CATALOG-511-R10` · advanced.

<a id="bank-511-042"></a>
#### BANK-511-042 — How can fabrication measurements detect variation smaller than a finished chip feature?

**Individual coverage scope:** Discuss indirect measurement, calibration and uncertainty.

<a id="bank-511-045"></a>
#### BANK-511-045 — What did NIST's SRM 2541–2547 silicon wafers make comparable in four-point-probe measurements?

**Individual coverage scope:** Use NIST's 2006 certification report for the wafer resistivity and sheet-resistance reference family, its dual-configuration probe method and uncertainty analysis; distinguish a calibration reference from evidence about chip yield or today's fab process.

**Research follow-up:** [Bounded case and source-access note](CASE_SOURCE_NOTES.md). This does not change proposal or production status.


<a id="domain-511-08"></a>
## Category: Semiconductor manufacturing evidence

<a id="catalog-511-r12"></a>
### Yield management

Subcategory `CATALOG-511-R12` · advanced.

<a id="bank-511-044"></a>
#### BANK-511-044 — How can a fabrication yield problem be localized when several process steps contribute variation?

**Individual coverage scope:** Compare wafer maps, process measurements and test limits conceptually rather than provide a fabrication recipe.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-511-010"></a>
### pending_topics/0 — The Architecture of Semiconductors: How Semiconductors Developed

**Original question:** Which engineering problem drove a semiconductor device or process change?

**Original planning scope:** Trace one semiconductor device or fabrication method from its original engineering problem through documented demonstrations and production changes. Evidence base: Trace dated origin records and subsequent interpretations. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. A broad semiconductor history needs a bounded period and source edition.

<a id="bank-511-011"></a>
### pending_topics/1 — Semiconductors: A Documented Semiconductors Case

**Original question:** What does a landmark chip's benchmark establish for its intended workload?

**Original planning scope:** Examine one influential chip using its intended workload, architecture, manufacturing context and measured performance; avoid treating one benchmark as universal. Evidence base: Read the original evaluation and its population, comparator, outcomes and limitations. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Distinct bounded case proposed.. The 2006 NIST report documents a named wafer-reference-material case.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

<a id="bank-511-012"></a>
### pending_topics/2 — Semiconductors: People behind Semiconductors

**Original question:** Whose fabrication, testing or packaging contribution was overlooked?

**Original planning scope:** Document overlooked fabrication, testing or packaging contributions within one chip program; use attributed technical records and worker accounts. Evidence base: Use attributable contribution records and consented participant accounts. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. A people-focused account requires attributed inventor or worker records, beyond this technical report.

<a id="bank-511-013"></a>
### pending_topics/3 — Semiconductors: Understanding Semiconductors

**Original question:** How does a chip design become a fabricated, packaged and tested device?

**Original planning scope:** Explain design, fabrication, packaging and testing through one device type; distinguish a chip design from a manufacturing process node. Evidence base: Use primary definitions and a documented end-to-end example. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal explains transistor-channel control.

**Scoped proposals:** [BANK-511-030](#bank-511-030).

<a id="bank-511-014"></a>
### pending_topics/4 — Semiconductors: Tradeoffs in Semiconductors

**Original question:** Which power, performance, area and yield tradeoffs shape a chip comparison?

**Original planning scope:** Compare one architectural or process tradeoff using power, performance, area and yield measurements under explicitly matched conditions. Evidence base: Compare original methods, assumptions, measures and uncertainty. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal bounds advanced-packaging tradeoffs.

**Scoped proposals:** [BANK-511-034](#bank-511-034).

<a id="bank-511-015"></a>
### pending_topics/5 — Semiconductors: An Open Semiconductors Question

**Original question:** Why did measured device behavior differ from its published expectation?

**Original planning scope:** Investigate a documented gap between expected and measured device behavior; compare test conditions and published explanations without inventing proprietary details. Evidence base: Compare competing explanations and specify missing discriminating evidence. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal leaves open multi-step yield localization.

**Scoped proposals:** [BANK-511-044](#bank-511-044).

<a id="bank-511-016"></a>
### pending_topics/6 — Semiconductors: A Tool for Semiconductors

**Original question:** What separates a semiconductor laboratory advance from qualified production?

**Original planning scope:** Evaluate one semiconductor innovation against a stated baseline and workload; distinguish laboratory demonstration, qualification and production availability. Evidence base: Compare validation, deployment and follow-up against a stated baseline. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Distinct bounded case proposed.. NIST's SRM family is a specific comparison tool with certified uncertainty.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

<a id="bank-511-017"></a>
### pending_topics/7 — Semiconductors: Decisions in Semiconductors

**Original question:** Which documented constraints shaped a chip or fabrication investment decision?

**Original planning scope:** Reconstruct one chip-design or manufacturing-investment decision using public technical and business records; attribute the constraints described by participants. Evidence base: Use decision records, assigned authority and attributed accounts. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Distinct bounded case proposed.. The NIST report documents a reference-material design and certification choice.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

<a id="bank-511-018"></a>
### pending_topics/8 — Semiconductors: A Turning Point in Semiconductors

**Original question:** How did a dated supply or policy event affect a specific chip chain?

**Original planning scope:** Examine a dated fabrication milestone, supply disruption or policy decision through its effects on a specific device or production chain. Evidence base: Build a dated before-and-after record without assuming causation. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Distinct bounded case proposed.. The 2006 revision is a dated metrology milestone, not an industry-wide turning point.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

<a id="bank-511-019"></a>
### pending_topics/9 — Semiconductors: How Semiconductors Works

**Original question:** Where are quality and responsibility checked between chip design and shipment?

**Original planning scope:** Map one chip from design files through fabrication, packaging and test; identify the role and evidence available at each stage. Evidence base: Trace the process, custody transfers and assigned responsibilities. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal traces repeated fabrication steps.

**Scoped proposals:** [BANK-511-037](#bank-511-037).

<a id="bank-511-020"></a>
### pending_topics/10 — Semiconductors: When a Semiconductors Approach Faltered

**Original question:** Why did a device architecture gain or lose support for a workload?

**Original planning scope:** Explain the adoption or decline of one device architecture using workload, cost, manufacturing and software-support evidence. Evidence base: Compare a dated series with competing explanations for change. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal addresses yield investigation without inventing a named failure.

**Scoped proposals:** [BANK-511-044](#bank-511-044).

<a id="bank-511-021"></a>
### pending_topics/11 — Semiconductors: across Two Periods

**Original question:** How do chip generations compare under equivalent system and test conditions?

**Original planning scope:** Compare two chip generations on equivalent workloads and measurement conditions; account for manufacturing, memory and system-level differences. Evidence base: Align definitions, samples, versions and measurement conditions. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Distinct bounded case proposed.. NIST compares 100 mm SRMs with earlier 50.8 mm sets within its certification history.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

<a id="bank-511-022"></a>
### pending_topics/12 — Semiconductors: Possible Next Steps in Semiconductors

**Original question:** What measurements and production steps remain before a proposed chip advance scales?

**Original planning scope:** Assess a proposed semiconductor advance through required materials, tools, validation and production scale; distinguish targets from achieved results. Evidence base: Read the actual proposal and distinguish required conditions from achieved results. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. A next-steps claim needs a dated, named semiconductor proposal, not an extrapolation from the 2006 report.

<a id="bank-511-023"></a>
### pending_topics/13 — Semiconductors: Testing a Semiconductors Claim

**Original question:** Does a semiconductor claim compare measured properties or marketing labels?

**Original planning scope:** Test one chip-performance or process-node claim against its definitions and benchmark setup; separate marketing labels from measured device properties. Evidence base: Trace the public claim to original evidence and retain its qualifications. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Distinct bounded case proposed.. The certified values and uncertainty method bound a test of measurement comparability.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

<a id="bank-511-024"></a>
### pending_topics/14 — Semiconductors: One Semiconductors Evidence Trail

**Original question:** How did a chip move from design through qualification and deployment?

**Original planning scope:** Build a sourced account of one chip's development, qualification and deployment; identify which production or performance claims remain unverified. Evidence base: Build a dated evidence trail including dissent and unresolved findings. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Distinct bounded case proposed.. NIST's technical report supplies the certification evidence trail.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

<a id="bank-511-025"></a>
### pending_topics/15 — Semiconductors: Chip Architecture

**Original question:** How does one chip architecture change performance on a defined workload?

**Original planning scope:** Examine how one architectural choice changes execution on a defined workload; compare memory access, parallelism, power and baseline implementation. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal covers chiplet architecture and interface tradeoffs.

**Scoped proposals:** [BANK-511-041](#bank-511-041).

<a id="bank-511-026"></a>
### pending_topics/16 — Semiconductors: Fabrication Steps

**Original question:** Where do process controls and inspection enter chip fabrication?

**Original planning scope:** Follow one published fabrication process at an explanatory level; identify inputs, process control and inspection without presenting proprietary operating recipes. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal covers repeated fabrication steps; SRMs concern measurement, not a process sequence.

**Scoped proposals:** [BANK-511-037](#bank-511-037).

<a id="bank-511-027"></a>
### pending_topics/17 — Semiconductors: Yield Loss

**Original question:** What do reported yield figures include and exclude?

**Original planning scope:** Analyze yield measurements for a defined product and production stage; distinguish defect mechanisms, test rejection and assumptions about economic viability. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal concerns localization of yield loss; SRM certification does not report yield.

**Scoped proposals:** [BANK-511-044](#bank-511-044).

<a id="bank-511-028"></a>
### pending_topics/18 — Semiconductors: Packaging

**Original question:** Which packaging tradeoffs matter for a specified device?

**Original planning scope:** Compare packaging approaches for a specified device or system; examine thermal, interconnect, reliability and testing tradeoffs. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal addresses packaging constraints.

**Scoped proposals:** [BANK-511-034](#bank-511-034).

<a id="bank-511-029"></a>
### pending_topics/19 — Semiconductors: Critical Supply

**Original question:** Which input dependencies constrain a defined chip supply chain?

**Original planning scope:** Trace a critical material or production input through a defined chip supply chain; use dated capacity and dependency evidence without assuming global substitutability. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original device papers, measurement conditions, process qualification and dated production disclosures. Starting framework: NIST semiconductor metrology program (https://www.nist.gov/chips/research-development-programs/metrology-program). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal considers fab resource constraints; the NIST report does not measure supply risk.

**Scoped proposals:** [BANK-511-035](#bank-511-035).

### trending_topics/0 — Semiconductors: Record Extremes & Superlatives

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. A record superlative needs a comparable chip metric, device class and date.

### trending_topics/1 — Semiconductors: An Open Semiconductors Question

**Editorial disposition:** Routed to existing scoped BANK proposal.. The existing proposal bounds open yield-localization questions.

**Scoped proposals:** [BANK-511-044](#bank-511-044).

### trending_topics/2 — Semiconductors: A Tool for Semiconductors

**Editorial disposition:** Distinct bounded case proposed.. The NIST SRM family is a named measurement-comparison tool.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

### trending_topics/3 — Semiconductors: Testing a Semiconductors Claim

**Editorial disposition:** Distinct bounded case proposed.. The certificate and uncertainty analysis bound a comparability claim.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

### trending_topics/4 — Semiconductors: A Turning Point in Semiconductors

**Editorial disposition:** Distinct bounded case proposed.. The 2006 revision is a dated certification milestone, not an industry-wide turning point.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

### trending_topics/5 — Semiconductors: People behind Semiconductors

**Editorial disposition:** Documented cross-bank overlap or out of scope pending bounded evidence.. A people-focused pitch needs independently attributed records.

### trending_topics/6 — Semiconductors: One Semiconductors Evidence Trail

**Editorial disposition:** Distinct bounded case proposed.. The NIST report is a traceable technical evidence trail.

**Scoped proposals:** [BANK-511-045](#bank-511-045).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-511-01"></a>
### Device physics

<a id="bank-511-001"></a>
- `BANK-511-001` — PN junctions → [BANK-511-036](#bank-511-036)
<a id="bank-511-002"></a>
- `BANK-511-002` — MOSFET operation → [BANK-511-036](#bank-511-036)
<a id="bank-511-003"></a>
- `BANK-511-003` — Carrier mobility → [BANK-511-036](#bank-511-036)

<a id="catalog-511-02"></a>
### Fabrication

<a id="bank-511-004"></a>
- `BANK-511-004` — Photolithography → [BANK-511-037](#bank-511-037)
<a id="bank-511-005"></a>
- `BANK-511-005` — Etching and deposition → [BANK-511-037](#bank-511-037)
<a id="bank-511-006"></a>
- `BANK-511-006` — Yield management → [BANK-511-044](#bank-511-044)

<a id="catalog-511-03"></a>
### Industry

<a id="bank-511-007"></a>
- `BANK-511-007` — Foundry versus integrated models → [BANK-511-038](#bank-511-038)
<a id="bank-511-008"></a>
- `BANK-511-008` — Packaging bottlenecks → [BANK-511-038](#bank-511-038)
<a id="bank-511-009"></a>
- `BANK-511-009` — Chip supply-chain concentration → [BANK-511-038](#bank-511-038)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

### Retired overlaps and primary questions

<a id="bank-511-031"></a>
- `BANK-511-031` → [BANK-088-029](../088_how_its_made/IN_DEPTH_TOPIC_BANK.md#bank-088-029): The individual scopes describe substantially the same episode: Explain documented fabrication, probing, dicing, packaging and testing at a bounded level; distinguish a simplified flow from a reproducible fabrication recipe. / Map fabrication, testing, dicing and packaging. Retain one primary question and preserve the other full record inactive with a referral.

  Preserved inactive question: How does a wafer become many separately packaged chips?

  Preserved inactive scope: Map fabrication, testing, dicing and packaging.


## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- **Concrete case selection for Memory architectures:** Connect device structure and system use conceptually. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Power semiconductors:** Compare voltage, current, heat and switching loss. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Chiplets:** Trace yields, communication and package integration. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Semiconductor metrology:** Discuss indirect measurement, calibration and uncertainty. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Yield management:** Compare wafer maps, process measurements and test limits conceptually rather than provide a fabrication recipe. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/511_semiconductors/NICHE_511_semiconductors.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
