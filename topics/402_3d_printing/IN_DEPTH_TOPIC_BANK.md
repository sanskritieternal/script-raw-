# 402 — 3D Printing: main topic bank

Updated: 2026-10-23 · **14 active BANK proposals · 5 categories · 10 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Printing foundations](#catalog-402-r01) → [Print-process choices](#catalog-402-r04) → [Slicer infill strategies](#catalog-402-r07).
- **Intermediate:** [Print preparation](#catalog-402-r02) → [Print-process choices](#catalog-402-r05) → [Multi-material printing](#catalog-402-r08) → [Digital fabrication tolerances](#catalog-402-r09).
- **Advanced:** [Quality and decisions](#catalog-402-r03) → [Print-process choices](#catalog-402-r06) → [Print-farm operations](#catalog-402-r10).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-402-01) | 3 | 0 | 0 |
| [Methods and applications](#domain-402-02) | 0 | 3 | 0 |
| [Systems and interpretation](#domain-402-03) | 0 | 0 | 4 |
| [Print planning](#domain-402-04) | 1 | 1 | 0 |
| [Fabrication systems](#domain-402-05) | 0 | 1 | 1 |

<a id="domain-402-01"></a>
## Category: Foundations

<a id="catalog-402-r01"></a>
### Printing foundations

Subcategory `CATALOG-402-R01` · foundation.

<a id="bank-402-030"></a>
#### BANK-402-030 — Why can a watertight-looking 3D model fail to slice?

**Individual coverage scope:** Inspect nonmanifold geometry, normals and thin walls.

<a id="bank-402-031"></a>
#### BANK-402-031 — How does nozzle width constrain the detail an FDM printer can reproduce?

**Individual coverage scope:** Compare line width, wall count and intended geometry.

<a id="catalog-402-r04"></a>
### Print-process choices

Subcategory `CATALOG-402-R04` · foundation.

<a id="bank-402-036"></a>
#### BANK-402-036 — How do extrusion, resin curing and powder-bed fusion build layers differently?

**Individual coverage scope:** Compare process families and resulting constraints.


<a id="domain-402-02"></a>
## Category: Methods and applications

<a id="catalog-402-r02"></a>
### Print preparation

Subcategory `CATALOG-402-R02` · intermediate.

<a id="bank-402-032"></a>
#### BANK-402-032 — When should a model be split into several printed parts?

**Individual coverage scope:** Compare orientation, assembly, support and seam placement.

<a id="bank-402-033"></a>
#### BANK-402-033 — How do clearances differ between a static fit and a moving joint?

**Individual coverage scope:** Use a calibration specimen and document machine-specific results.

<a id="catalog-402-r05"></a>
### Print-process choices

Subcategory `CATALOG-402-R05` · intermediate.

<a id="bank-402-037"></a>
#### BANK-402-037 — How do layer orientation and supports change strength and surface quality?

**Individual coverage scope:** Separate anisotropy, removal and dimensional compensation.


<a id="domain-402-03"></a>
## Category: Systems and interpretation

<a id="catalog-402-r03"></a>
### Quality and decisions

Subcategory `CATALOG-402-R03` · advanced.

<a id="bank-402-034"></a>
#### BANK-402-034 — How can a printer fault be separated from a wet-filament problem?

**Individual coverage scope:** Design controlled comparisons without changing every setting at once.

<a id="bank-402-035"></a>
#### BANK-402-035 — What evidence is needed before using a printed part in a critical application?

**Individual coverage scope:** Distinguish hobby prototypes from qualified materials and validated manufacturing.

<a id="bank-402-043"></a>
#### BANK-402-043 — What does NIST?s AMB2018-03 printed polycarbonate coupon make testable about layer orientation and part quality?

**Individual coverage scope:** Use the benchmark description to connect raster direction, cut coupon geometry and specified mass, thickness, void and tensile comparisons. Distinguish prescribed test metrics from measured results or qualification of an end-use part.

**Research follow-up:** [Bounded case and source-access note](402_3D_PRINTING_SOURCE_NOTE.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-402-037](#bank-402-037) — NIST?s named polymer-coupon geometry and benchmark outcomes versus general orientation/support tradeoffs.

**Neighboring scope:** [BANK-402-035](#bank-402-035) — A benchmark test definition versus evidence required to qualify any critical application.

**Neighboring scope:** [BANK-401-035](../401_metalworking/IN_DEPTH_TOPIC_BANK.md#bank-401-035) — Printed polymer-coupon comparisons versus general metal-part inspection reporting.

<a id="catalog-402-r06"></a>
### Print-process choices

Subcategory `CATALOG-402-R06` · advanced.

<a id="bank-402-038"></a>
#### BANK-402-038 — How can printer calibration and ventilation planning address different forms of print failure?

**Individual coverage scope:** Distinguish geometry quality and material-emission controls.


<a id="domain-402-04"></a>
## Category: Print planning

<a id="catalog-402-r07"></a>
### Slicer infill strategies

Subcategory `CATALOG-402-R07` · foundation.

<a id="bank-402-039"></a>
#### BANK-402-039 — How does infill change print time without guaranteeing part strength?

**Individual coverage scope:** Compare geometry, load direction and wall contributions.

<a id="catalog-402-r08"></a>
### Multi-material printing

Subcategory `CATALOG-402-R08` · intermediate.

<a id="bank-402-040"></a>
#### BANK-402-040 — Why can two printable materials fail at their shared boundary?

**Individual coverage scope:** Compare adhesion, temperature compatibility and differential shrinkage.


<a id="domain-402-05"></a>
## Category: Fabrication systems

<a id="catalog-402-r09"></a>
### Digital fabrication tolerances

Subcategory `CATALOG-402-R09` · intermediate.

<a id="bank-402-041"></a>
#### BANK-402-041 — How should a printed part's tolerances change when it must fit a laser-cut or machined component?

**Individual coverage scope:** Trace process variation through one assembly.

<a id="catalog-402-r10"></a>
### Print-farm operations

Subcategory `CATALOG-402-R10` · advanced.

<a id="bank-402-042"></a>
#### BANK-402-042 — How can a print farm detect recurring failure without treating every printer as identical?

**Individual coverage scope:** Track machine configuration, batches and maintenance evidence.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-402-010"></a>
### pending_topics/0 — The Architecture of 3D Printing: An Additive Process Emerges

**Original question:** Which dated patent or machine changed a specific printing process?

**Original planning scope:** Distinguish prototype, commercialization, and later variants. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 0 (original ID 1, title ?The Architecture of 3D Printing: An Additive Process Emerges?) to: How do extrusion, resin curing and powder-bed fusion build layers differently? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-036](#bank-402-036).

<a id="bank-402-011"></a>
### pending_topics/1 — 3D Printing: A Printed Part under Test

**Original question:** What does a named printed object's documented test prove?

**Original planning scope:** Specify material, orientation, machine, process, and load. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** new_case. Named primary-source case routes archived pending_topics position 1 (original ID 2, title ?3D Printing: A Printed Part under Test?) to: What does NIST?s AMB2018-03 printed polycarbonate coupon make testable about layer orientation and part quality? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-043](#bank-402-043).

<a id="bank-402-012"></a>
### pending_topics/2 — 3D Printing: Work behind a Printed Object

**Original question:** Who modeled, prepared, operated, postprocessed, and inspected it?

**Original planning scope:** Use credits and process logs. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 2 (original ID 3, title ?3D Printing: Work behind a Printed Object?) to: How can printer calibration and ventilation planning address different forms of print failure? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-038](#bank-402-038).

<a id="bank-402-013"></a>
### pending_topics/3 — 3D Printing: From Model to Part

**Original question:** How do geometry, slicing, build, postprocessing, and inspection connect?

**Original planning scope:** Follow one documented part and record versions. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 3 (original ID 4, title ?3D Printing: From Model to Part?) to: Why can a watertight-looking 3D model fail to slice? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-030](#bank-402-030).

<a id="bank-402-014"></a>
### pending_topics/4 — 3D Printing: Anisotropy in a Print

**Original question:** How can build orientation change measured properties?

**Original planning scope:** Compare controlled specimens and test methods. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** new_case. Named primary-source case routes archived pending_topics position 4 (original ID 5, title ?3D Printing: Anisotropy in a Print?) to: What does NIST?s AMB2018-03 printed polycarbonate coupon make testable about layer orientation and part quality? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-043](#bank-402-043).

<a id="bank-402-015"></a>
### pending_topics/5 — 3D Printing: Why Did a Print Fail?

**Original question:** Which data distinguish feedstock, geometry, process, and handling causes?

**Original planning scope:** Review machine log and material test; avoid diagnosis from a photo. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 5 (original ID 6, title ?3D Printing: Why Did a Print Fail??) to: How can a printer fault be separated from a wet-filament problem? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-034](#bank-402-034).

<a id="bank-402-016"></a>
### pending_topics/6 — 3D Printing: A New Printing Method

**Original question:** Which measurable limit did a particular process improve?

**Original planning scope:** Compare accuracy, throughput, material, and repeatability. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 6 (original ID 7, title ?3D Printing: A New Printing Method?) to: How do extrusion, resin curing and powder-bed fusion build layers differently? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-036](#bank-402-036).

<a id="bank-402-017"></a>
### pending_topics/7 — 3D Printing: A Designer Revises a Part

**Original question:** What test result led to a documented redesign?

**Original planning scope:** Use model versions and inspection reports. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 7 (original ID 8, title ?3D Printing: A Designer Revises a Part?) to: When should a model be split into several printed parts? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-032](#bank-402-032).

<a id="bank-402-018"></a>
### pending_topics/8 — 3D Printing: A Standard Changes Qualification

**Original question:** How did a dated test or standard alter a specified application?

**Original planning scope:** Check edition, jurisdiction, and actual adoption. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 8 (original ID 9, title ?3D Printing: A Standard Changes Qualification?) to: What evidence is needed before using a printed part in a critical application? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-035](#bank-402-035).

<a id="bank-402-019"></a>
### pending_topics/9 — 3D Printing: Building Layer by Layer

**Original question:** Which process variables affect one part's geometry and properties?

**Original planning scope:** Describe principle and measured parameters, not unsafe machine operation. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 9 (original ID 10, title ?3D Printing: Building Layer by Layer?) to: How do extrusion, resin curing and powder-bed fusion build layers differently? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-036](#bank-402-036).

<a id="bank-402-020"></a>
### pending_topics/10 — 3D Printing: A Printed Prototype Replaced

**Original question:** Why was a print abandoned for another process?

**Original planning scope:** Compare documented cost, quality, and function. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 10 (original ID 11, title ?3D Printing: A Printed Prototype Replaced?) to: What evidence is needed before using a printed part in a critical application? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-035](#bank-402-035).

<a id="bank-402-021"></a>
### pending_topics/11 — 3D Printing: A Part across Machine Versions

**Original question:** Which properties changed after hardware or software update?

**Original planning scope:** Use same material and test where possible. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 11 (original ID 12, title ?3D Printing: A Part across Machine Versions?) to: How can printer calibration and ventilation planning address different forms of print failure? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-038](#bank-402-038).

<a id="bank-402-022"></a>
### pending_topics/12 — 3D Printing: A Proposed Printed Application

**Original question:** What qualification evidence is missing for intended use?

**Original planning scope:** Identify tests and regulatory path without prediction. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 12 (original ID 13, title ?3D Printing: A Proposed Printed Application?) to: What evidence is needed before using a printed part in a critical application? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-035](#bank-402-035).

<a id="bank-402-023"></a>
### pending_topics/13 — 3D Printing: Can Print Anything?

**Original question:** Which size, material, finish, and strength limits matter for a named use?

**Original planning scope:** Use actual machine specification and test. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 13 (original ID 14, title ?3D Printing: Can Print Anything??) to: What evidence is needed before using a printed part in a critical application? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-035](#bank-402-035).

<a id="bank-402-024"></a>
### pending_topics/14 — 3D Printing: One Part's Digital Thread

**Original question:** How did CAD revision, print log, and test produce the final object?

**Original planning scope:** Follow provenance and accountable approvals. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** new_case. Named primary-source case routes archived pending_topics position 14 (original ID 15, title ?3D Printing: One Part's Digital Thread?) to: What does NIST?s AMB2018-03 printed polycarbonate coupon make testable about layer orientation and part quality? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-043](#bank-402-043).

<a id="bank-402-025"></a>
### pending_topics/15 — 3D Printing: What the Part Must Do

**Original question:** Which fit, load, surface, and service-life requirements were specified?

**Original planning scope:** Compare brief with measured output. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 15 (original ID 16, title ?3D Printing: What the Part Must Do?) to: What evidence is needed before using a printed part in a critical application? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-035](#bank-402-035).

<a id="bank-402-026"></a>
### pending_topics/16 — 3D Printing: Feedstock and Machine Match

**Original question:** What do material batch and machine condition contribute?

**Original planning scope:** Use certificates, logs, and process notes. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 16 (original ID 17, title ?3D Printing: Feedstock and Machine Match?) to: Why can two printable materials fail at their shared boundary? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-040](#bank-402-040).

<a id="bank-402-027"></a>
### pending_topics/17 — 3D Printing: A Test Print's Lessons

**Original question:** Which measured deviation changed the model or settings?

**Original planning scope:** Compare build, inspection, and revision record. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** new_case. Named primary-source case routes archived pending_topics position 17 (original ID 18, title ?3D Printing: A Test Print's Lessons?) to: What does NIST?s AMB2018-03 printed polycarbonate coupon make testable about layer orientation and part quality? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-043](#bank-402-043).

<a id="bank-402-028"></a>
### pending_topics/18 — 3D Printing: Form Enabled by Printing

**Original question:** Which geometry could be made more simply or differently?

**Original planning scope:** Compare with alternative fabrication and function. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 18 (original ID 19, title ?3D Printing: Form Enabled by Printing?) to: When should a model be split into several printed parts? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-032](#bank-402-032).

<a id="bank-402-029"></a>
### pending_topics/19 — 3D Printing: A Printed Part's Makers

**Original question:** Who designed, prepared, printed, finished, and qualified it?

**Original planning scope:** Use revision history and credits. Evidence base: CAD and slicer versions, machine logs, feedstock batches, material characterization, part inspection and test records, NIST measurement research, and NIOSH emissions guidance.

**Editorial disposition:** merge_existing. Existing scoped question routes archived pending_topics position 19 (original ID 20, title ?3D Printing: A Printed Part's Makers?) to: How can a print farm detect recurring failure without treating every printer as identical? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-042](#bank-402-042).

### trending_topics/0 — 3D Printing: Record Extremes & Superlatives

**Editorial disposition:** reject_unsubstantiated_superlative. Archived trending_topics position 0 (original ID 21, title ?3D Printing: Record Extremes & Superlatives?) asserts an unspecified record or superlative without a defined measure, source, date or comparison set. Original record/status remain preserved; no active proposal adopts the claim.

### trending_topics/1 — 3D Printing: Why Did a Print Fail?

**Editorial disposition:** merge_existing. Existing scoped question routes archived trending_topics position 1 (original ID 22, title ?3D Printing: Why Did a Print Fail??) to: How can a printer fault be separated from a wet-filament problem? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-034](#bank-402-034).

### trending_topics/2 — 3D Printing: A New Printing Method

**Editorial disposition:** merge_existing. Existing scoped question routes archived trending_topics position 2 (original ID 23, title ?3D Printing: A New Printing Method?) to: How do extrusion, resin curing and powder-bed fusion build layers differently? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-036](#bank-402-036).

### trending_topics/3 — 3D Printing: Can Print Anything?

**Editorial disposition:** merge_existing. Existing scoped question routes archived trending_topics position 3 (original ID 24, title ?3D Printing: Can Print Anything??) to: What evidence is needed before using a printed part in a critical application? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-035](#bank-402-035).

### trending_topics/4 — 3D Printing: A Standard Changes Qualification

**Editorial disposition:** merge_existing. Existing scoped question routes archived trending_topics position 4 (original ID 25, title ?3D Printing: A Standard Changes Qualification?) to: What evidence is needed before using a printed part in a critical application? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-035](#bank-402-035).

### trending_topics/5 — 3D Printing: Work behind a Printed Object

**Editorial disposition:** merge_existing. Existing scoped question routes archived trending_topics position 5 (original ID 26, title ?3D Printing: Work behind a Printed Object?) to: How can printer calibration and ventilation planning address different forms of print failure? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-038](#bank-402-038).

### trending_topics/6 — 3D Printing: One Part's Digital Thread

**Editorial disposition:** new_case. Named primary-source case routes archived trending_topics position 6 (original ID 27, title ?3D Printing: One Part's Digital Thread?) to: What does NIST?s AMB2018-03 printed polycarbonate coupon make testable about layer orientation and part quality? Original archive wording/status remain preserved; the route is not verification of results, historical claims or production readiness.

**Scoped proposals:** [BANK-402-043](#bank-402-043).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-402-01"></a>
### Printing processes

<a id="bank-402-001"></a>
- `BANK-402-001` — FDM extrusion → [BANK-402-036](#bank-402-036)
<a id="bank-402-002"></a>
- `BANK-402-002` — Resin curing → [BANK-402-036](#bank-402-036)
<a id="bank-402-003"></a>
- `BANK-402-003` — Powder-bed fusion → [BANK-402-036](#bank-402-036)

<a id="catalog-402-02"></a>
### Design for printing

<a id="bank-402-004"></a>
- `BANK-402-004` — Layer orientation → [BANK-402-037](#bank-402-037)
<a id="bank-402-005"></a>
- `BANK-402-005` — Support removal → [BANK-402-037](#bank-402-037)
<a id="bank-402-006"></a>
- `BANK-402-006` — Dimensional compensation → [BANK-402-037](#bank-402-037)

<a id="catalog-402-03"></a>
### Quality

<a id="bank-402-007"></a>
- `BANK-402-007` — Strength anisotropy → [BANK-402-037](#bank-402-037)
<a id="bank-402-008"></a>
- `BANK-402-008` — Printer calibration → [BANK-402-038](#bank-402-038)
<a id="bank-402-009"></a>
- `BANK-402-009` — Material emissions and ventilation → [BANK-402-038](#bank-402-038)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [064 Home & Lifestyle](../064_home_lifestyle/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [085 DIY & Making](../085_diy_making/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [086 Restoration](../086_restoration/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [087 How Things Work](../087_how_things_work/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [088 How It's Made](../088_how_its_made/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [089 Inventions & Inventors](../089_inventions_inventors/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- **Concrete case selection for Slicer infill strategies:** Compare geometry, load direction and wall contributions. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Multi-material printing:** Compare adhesion, temperature compatibility and differential shrinkage. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Digital fabrication tolerances:** Trace process variation through one assembly. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Print-farm operations:** Track machine configuration, batches and maintenance evidence. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/402_3d_printing/NICHE_402_3d_printing.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
