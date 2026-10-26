# 512 — Quantum Computing: main topic bank

Updated: 2026-10-23 · **14 active BANK proposals · 7 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Quantum foundations](#catalog-512-r01) → [Quantum information](#catalog-512-r04) → [Quantum networking distinctions](#catalog-512-r07).
- **Intermediate:** [Computation methods](#catalog-512-r02) → [Quantum information](#catalog-512-r05) → [Control electronics](#catalog-512-r09) → [Error-correction overhead](#catalog-512-r11).
- **Advanced:** [Evaluating performance](#catalog-512-r03) → [Quantum information](#catalog-512-r06) → [Algorithm-specific resource estimates](#catalog-512-r08) → [Reproducibility of benchmark claims](#catalog-512-r10).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Foundations](#domain-512-01) | 2 | 0 | 0 |
| [Methods and applications](#domain-512-02) | 0 | 3 | 0 |
| [Systems and interpretation](#domain-512-03) | 0 | 0 | 3 |
| [Quantum systems](#domain-512-04) | 1 | 0 | 0 |
| [Quantum applications](#domain-512-05) | 0 | 0 | 1 |
| [Quantum engineering](#domain-512-06) | 0 | 3 | 0 |
| [Quantum evidence](#domain-512-07) | 0 | 0 | 1 |

<a id="domain-512-01"></a>
## Category: Foundations

<a id="catalog-512-r01"></a>
### Quantum foundations

Subcategory `CATALOG-512-R01` · foundation.

<a id="bank-512-030"></a>
#### BANK-512-030 — How does measuring a qubit differ from reading an ordinary stored bit?

**Individual coverage scope:** Separate superposition, probabilities and repeated trials.

<a id="catalog-512-r04"></a>
### Quantum information

Subcategory `CATALOG-512-R04` · foundation.

<a id="bank-512-036"></a>
#### BANK-512-036 — How do gates and entanglement transform a small quantum state before measurement?

**Individual coverage scope:** Use conceptual circuits and probabilistic outcomes.


<a id="domain-512-02"></a>
## Category: Methods and applications

<a id="catalog-512-r02"></a>
### Computation methods

Subcategory `CATALOG-512-R02` · intermediate.

<a id="bank-512-032"></a>
#### BANK-512-032 — How can quantum interference amplify useful outcomes in an algorithm?

**Individual coverage scope:** Use a small conceptual circuit with measurement limits.

<a id="bank-512-033"></a>
#### BANK-512-033 — Why does useful quantum error correction require many physical qubits?

**Individual coverage scope:** Explain noise, logical encoding and overhead conceptually.

<a id="catalog-512-r05"></a>
### Quantum information

Subcategory `CATALOG-512-R05` · intermediate.

<a id="bank-512-037"></a>
#### BANK-512-037 — How do decoherence and readout errors create different barriers to reliable quantum computation?

**Individual coverage scope:** Compare noise sources and error correction overhead.


<a id="domain-512-03"></a>
## Category: Systems and interpretation

<a id="catalog-512-r03"></a>
### Evaluating performance

Subcategory `CATALOG-512-R03` · advanced.

<a id="bank-512-034"></a>
#### BANK-512-034 — What makes a quantum benchmark vulnerable to an unfair classical comparison?

**Individual coverage scope:** Compare task definitions, resources and updated algorithms.

<a id="bank-512-035"></a>
#### BANK-512-035 — Which parts of a practical workload remain classical around a quantum processor?

**Individual coverage scope:** Map preparation, control, decoding and output analysis.

<a id="catalog-512-r06"></a>
### Quantum information

Subcategory `CATALOG-512-R06` · advanced.

<a id="bank-512-038"></a>
#### BANK-512-038 — Why must input preparation and output extraction be included in quantum-advantage claims?

**Individual coverage scope:** Compare end-to-end workload and classical baselines.


<a id="domain-512-04"></a>
## Category: Quantum systems

<a id="catalog-512-r07"></a>
### Quantum networking distinctions

Subcategory `CATALOG-512-R07` · foundation.

<a id="bank-512-039"></a>
#### BANK-512-039 — How does quantum networking differ from sending ordinary data between quantum computers?

**Individual coverage scope:** Separate entanglement distribution and classical communication.


<a id="domain-512-05"></a>
## Category: Quantum applications

<a id="catalog-512-r08"></a>
### Algorithm-specific resource estimates

Subcategory `CATALOG-512-R08` · advanced.

<a id="bank-512-040"></a>
#### BANK-512-040 — What must a useful quantum-algorithm resource estimate include beyond logical qubit count?

**Individual coverage scope:** Include error correction, depth and input-output work.


<a id="domain-512-06"></a>
## Category: Quantum engineering

<a id="catalog-512-r09"></a>
### Control electronics

Subcategory `CATALOG-512-R09` · intermediate.

<a id="bank-512-041"></a>
#### BANK-512-041 — How can classical control hardware limit a quantum processor's scale?

**Individual coverage scope:** Map wiring, timing, heat and calibration.

<a id="catalog-512-r11"></a>
### Error-correction overhead

Subcategory `CATALOG-512-R11` · intermediate.

<a id="bank-512-043"></a>
#### BANK-512-043 — Why can adding physical qubits fail to improve a logical qubit's reliability?

**Individual coverage scope:** Separate encoding overhead, error correlations, control quality and decoding assumptions without claiming a particular implementation has achieved a threshold.

<a id="bank-512-044"></a>
#### BANK-512-044 — What did Google's 2023 surface-code experiment establish about scaling one logical qubit?

**Individual coverage scope:** Compare distance-3 and distance-5 logical error measurements over repeated cycles in the named superconducting-device experiment; distinguish modest error suppression from a fault-tolerant general-purpose computer.

**Research follow-up:** [Bounded case and source-access note](512_QUANTUM_COMPUTING_SOURCE_NOTE.md). This does not change proposal or production status.

**Neighboring scope:** [BANK-512-043](#bank-512-043) — Named 2023 distance-3 versus distance-5 result versus general principle that more qubits need not improve reliability.

**Neighboring scope:** [BANK-512-034](#bank-512-034) — Logical-error experiment versus quantum/classical benchmark fairness.

**Neighboring scope:** [BANK-512-040](#bank-512-040) — One encoded-qubit experiment versus algorithm-level resource estimates.


<a id="domain-512-07"></a>
## Category: Quantum evidence

<a id="catalog-512-r10"></a>
### Reproducibility of benchmark claims

Subcategory `CATALOG-512-R10` · advanced.

<a id="bank-512-042"></a>
#### BANK-512-042 — What must be published to reproduce a quantum performance comparison?

**Individual coverage scope:** Record tasks, noise, sampling and classical baselines.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

<a id="bank-512-010"></a>
### pending_topics/0 — The Architecture of Quantum Computing: How Quantum Computing Developed

**Original question:** How did a quantum-computing proposal become a documented experiment?

**Original planning scope:** Trace one quantum-computing idea from its theoretical task through a documented experiment; distinguish the original proposal from later hardware claims. Evidence base: Trace dated origin records and subsequent interpretations. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/0 (original ID 1, title The Architecture of Quantum Computing: How Quantum Computing Developed) remains in the original snapshot. The bounded active question BANK-512-033 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-033](#bank-512-033).

<a id="bank-512-011"></a>
### pending_topics/1 — Quantum Computing: A Documented Quantum Computing Case

**Original question:** What did a widely cited quantum demonstration actually establish?

**Original planning scope:** Examine one widely cited quantum demonstration using its task, device, comparison method and uncertainty; state what practical use it did not establish. Evidence base: Read the original evaluation and its population, comparator, outcomes and limitations. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** new_case. Archived pending_topics/1 (original ID 2, title Quantum Computing: A Documented Quantum Computing Case) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

<a id="bank-512-012"></a>
### pending_topics/2 — Quantum Computing: People behind Quantum Computing

**Original question:** Whose calibration, control or verification work enabled a quantum result?

**Original planning scope:** Document overlooked calibration, control or verification work in one experiment; credit contributors through publications and attributed accounts. Evidence base: Use attributable contribution records and consented participant accounts. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/2 (original ID 3, title Quantum Computing: People behind Quantum Computing) remains in the original snapshot. The bounded active question BANK-512-033 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-033](#bank-512-033).

<a id="bank-512-013"></a>
### pending_topics/3 — Quantum Computing: Understanding Quantum Computing

**Original question:** How do preparation, operations and measurement answer one quantum task?

**Original planning scope:** Explain qubits, operations, measurement and error through one defined experiment; distinguish quantum computing from ordinary parallel processing. Evidence base: Use primary definitions and a documented end-to-end example. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/3 (original ID 4, title Quantum Computing: Understanding Quantum Computing) remains in the original snapshot. The bounded active question BANK-512-030 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-030](#bank-512-030).

<a id="bank-512-014"></a>
### pending_topics/4 — Quantum Computing: Tradeoffs in Quantum Computing

**Original question:** Which physical and logical resources determine the cost of a quantum task?

**Original planning scope:** Compare resource and error estimates for one quantum task; separate physical qubits, logical qubits, circuit depth and classical verification costs. Evidence base: Compare original methods, assumptions, measures and uncertainty. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/4 (original ID 5, title Quantum Computing: Tradeoffs in Quantum Computing) remains in the original snapshot. The bounded active question BANK-512-043 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-043](#bank-512-043).

<a id="bank-512-015"></a>
### pending_topics/5 — Quantum Computing: An Open Quantum Computing Question

**Original question:** Which experiment could distinguish explanations for a disputed quantum result?

**Original planning scope:** Investigate one unresolved result or scalability question using published experiments and competing interpretations; identify a test that could resolve it. Evidence base: Compare competing explanations and specify missing discriminating evidence. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/5 (original ID 6, title Quantum Computing: An Open Quantum Computing Question) remains in the original snapshot. The bounded active question BANK-512-040 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-040](#bank-512-040).

<a id="bank-512-016"></a>
### pending_topics/6 — Quantum Computing: A Tool for Quantum Computing

**Original question:** Does a component advance improve the full computation being proposed?

**Original planning scope:** Evaluate one new quantum hardware or control method against a defined baseline; distinguish component improvement from useful computational advantage. Evidence base: Compare validation, deployment and follow-up against a stated baseline. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/6 (original ID 7, title Quantum Computing: A Tool for Quantum Computing) remains in the original snapshot. The bounded active question BANK-512-041 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-041](#bank-512-041).

<a id="bank-512-017"></a>
### pending_topics/7 — Quantum Computing: Decisions in Quantum Computing

**Original question:** Which recorded research decisions shaped a quantum experiment's design?

**Original planning scope:** Reconstruct one research or engineering decision through papers, funding records and attributed accounts; distinguish stated goals from achieved milestones. Evidence base: Use decision records, assigned authority and attributed accounts. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/7 (original ID 8, title Quantum Computing: Decisions in Quantum Computing) remains in the original snapshot. The bounded active question BANK-512-040 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-040](#bank-512-040).

<a id="bank-512-018"></a>
### pending_topics/8 — Quantum Computing: A Turning Point in Quantum Computing

**Original question:** How did replication or criticism change a quantum milestone's interpretation?

**Original planning scope:** Follow a dated quantum milestone through its original publication, replication and later interpretation; avoid turning announcements into settled outcomes. Evidence base: Build a dated before-and-after record without assuming causation. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** new_case. Archived pending_topics/8 (original ID 9, title Quantum Computing: A Turning Point in Quantum Computing) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

<a id="bank-512-019"></a>
### pending_topics/9 — Quantum Computing: How Quantum Computing Works

**Original question:** Where do error and validation enter a quantum experiment?

**Original planning scope:** Map preparation, control, execution and readout in one quantum experiment; identify where errors and validation enter the process. Evidence base: Trace the process, custody transfers and assigned responsibilities. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/9 (original ID 10, title Quantum Computing: How Quantum Computing Works) remains in the original snapshot. The bounded active question BANK-512-037 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-037](#bank-512-037).

<a id="bank-512-020"></a>
### pending_topics/10 — Quantum Computing: When a Quantum Computing Approach Faltered

**Original question:** Why did confidence in a quantum approach increase or decline?

**Original planning scope:** Explain changing support for one quantum approach using measured performance, resource needs and independent results rather than publicity volume. Evidence base: Compare a dated series with competing explanations for change. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** new_case. Archived pending_topics/10 (original ID 11, title Quantum Computing: When a Quantum Computing Approach Faltered) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

<a id="bank-512-021"></a>
### pending_topics/11 — Quantum Computing: across Two Periods

**Original question:** How do two demonstrations compare using the same task and resource definitions?

**Original planning scope:** Compare two dated demonstrations using consistent task, error and resource definitions; describe where the devices cannot be directly compared. Evidence base: Align definitions, samples, versions and measurement conditions. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/11 (original ID 12, title Quantum Computing: across Two Periods) remains in the original snapshot. The bounded active question BANK-512-033 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-033](#bank-512-033).

<a id="bank-512-022"></a>
### pending_topics/12 — Quantum Computing: Possible Next Steps in Quantum Computing

**Original question:** What assumptions stand between a quantum algorithm and its proposed application?

**Original planning scope:** Assess a proposed quantum application through algorithm, error correction, hardware and input-output requirements; label untested assumptions. Evidence base: Read the actual proposal and distinguish required conditions from achieved results. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/12 (original ID 13, title Quantum Computing: Possible Next Steps in Quantum Computing) remains in the original snapshot. The bounded active question BANK-512-040 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-040](#bank-512-040).

<a id="bank-512-023"></a>
### pending_topics/13 — Quantum Computing: Testing a Quantum Computing Claim

**Original question:** Does a quantum-advantage claim use a defensible classical comparison?

**Original planning scope:** Test one quantum-advantage claim against its original task and classical comparison; distinguish theoretical speedup from measured end-to-end usefulness. Evidence base: Trace the public claim to original evidence and retain its qualifications. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** new_case. Archived pending_topics/13 (original ID 14, title Quantum Computing: Testing a Quantum Computing Claim) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

<a id="bank-512-024"></a>
### pending_topics/14 — Quantum Computing: One Quantum Computing Evidence Trail

**Original question:** How did a quantum result move from proposal through verification and debate?

**Original planning scope:** Build a sourced sequence from one proposed quantum experiment through execution, analysis and criticism; include unresolved verification questions. Evidence base: Build a dated evidence trail including dissent and unresolved findings. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** new_case. Archived pending_topics/14 (original ID 15, title Quantum Computing: One Quantum Computing Evidence Trail) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

<a id="bank-512-025"></a>
### pending_topics/15 — Quantum Computing: Qubit Platforms

**Original question:** How do qubit platforms compare on the same experimental criteria?

**Original planning scope:** Compare qubit platforms on the same stated experimental criteria; examine control, connectivity, coherence and measurement without declaring a universal winner. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/15 (original ID 16, title Quantum Computing: Qubit Platforms) remains in the original snapshot. The bounded active question BANK-512-037 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-037](#bank-512-037).

<a id="bank-512-026"></a>
### pending_topics/16 — Quantum Computing: Error Correction

**Original question:** What did an error-correction experiment establish about logical errors?

**Original planning scope:** Examine one error-correction experiment using code, logical error rate and resource overhead; distinguish error detection from sustained fault-tolerant computation. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** new_case. Archived pending_topics/16 (original ID 17, title Quantum Computing: Error Correction) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

<a id="bank-512-027"></a>
### pending_topics/17 — Quantum Computing: Benchmark Design

**Original question:** Does a quantum benchmark measure the advantage being claimed?

**Original planning scope:** Audit one benchmark's task selection, sampling, baseline and verification; identify whether its performance measure matches the public claim. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/17 (original ID 18, title Quantum Computing: Benchmark Design) remains in the original snapshot. The bounded active question BANK-512-034 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-034](#bank-512-034).

<a id="bank-512-028"></a>
### pending_topics/18 — Quantum Computing: Algorithm Limits

**Original question:** Which resources would a quantum algorithm need for its proposed task?

**Original planning scope:** Evaluate the assumptions and resource requirements of one quantum algorithm for a named problem; include data preparation and classical alternatives. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** merge_existing. Archived pending_topics/18 (original ID 19, title Quantum Computing: Algorithm Limits) remains in the original snapshot. The bounded active question BANK-512-040 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-040](#bank-512-040).

<a id="bank-512-029"></a>
### pending_topics/19 — Quantum Computing: Hardware Scaling

**Original question:** Which control and error constraints limit a hardware design's scaling?

**Original planning scope:** Trace scaling constraints in one hardware design through control, calibration, interconnects and error; distinguish component counts from usable computational capacity. Evidence base: Use the selected field lens's underlying records, measurement definitions and attributed accounts. Case records: original experiments, benchmark definitions, error estimates and reproducible classical comparisons. Starting framework: NIST quantum information science (https://www.nist.gov/quantum-information-science). Select and verify the dated underlying case sources before scripting..

**Editorial disposition:** new_case. Archived pending_topics/19 (original ID 20, title Quantum Computing: Hardware Scaling) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

### trending_topics/0 — Quantum Computing: Record Extremes & Superlatives

**Editorial disposition:** reject_unsubstantiated_superlative. Archived trending_topics/0 (original ID 21, title Quantum Computing: Record Extremes & Superlatives) remains in the original snapshot. The unspecified record/superlative lacks a defined metric, date and fair comparator; no unsupported claim is promoted.

### trending_topics/1 — Quantum Computing: An Open Quantum Computing Question

**Editorial disposition:** merge_existing. Archived trending_topics/1 (original ID 22, title Quantum Computing: An Open Quantum Computing Question) remains in the original snapshot. The bounded active question BANK-512-040 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-040](#bank-512-040).

### trending_topics/2 — Quantum Computing: A Tool for Quantum Computing

**Editorial disposition:** merge_existing. Archived trending_topics/2 (original ID 23, title Quantum Computing: A Tool for Quantum Computing) remains in the original snapshot. The bounded active question BANK-512-041 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-041](#bank-512-041).

### trending_topics/3 — Quantum Computing: Testing a Quantum Computing Claim

**Editorial disposition:** new_case. Archived trending_topics/3 (original ID 24, title Quantum Computing: Testing a Quantum Computing Claim) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

### trending_topics/4 — Quantum Computing: A Turning Point in Quantum Computing

**Editorial disposition:** new_case. Archived trending_topics/4 (original ID 25, title Quantum Computing: A Turning Point in Quantum Computing) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

### trending_topics/5 — Quantum Computing: People behind Quantum Computing

**Editorial disposition:** merge_existing. Archived trending_topics/5 (original ID 26, title Quantum Computing: People behind Quantum Computing) remains in the original snapshot. The bounded active question BANK-512-033 covers the premise without a duplicate BANK topic.

**Scoped proposals:** [BANK-512-033](#bank-512-033).

### trending_topics/6 — Quantum Computing: One Quantum Computing Evidence Trail

**Editorial disposition:** new_case. Archived trending_topics/6 (original ID 27, title Quantum Computing: One Quantum Computing Evidence Trail) remains in the original snapshot. This named primary-study case routes to BANK-512-044; it remains proposed with empty verified_sources and limits in 512_QUANTUM_COMPUTING_SOURCE_NOTE.md.

**Scoped proposals:** [BANK-512-044](#bank-512-044).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-512-01"></a>
### Quantum information

<a id="bank-512-001"></a>
- `BANK-512-001` — Qubits → [BANK-512-030](#bank-512-030)
<a id="bank-512-002"></a>
- `BANK-512-002` — Entanglement → [BANK-055-027](../055_time_reality/IN_DEPTH_TOPIC_BANK.md#bank-055-027)
<a id="bank-512-003"></a>
- `BANK-512-003` — Quantum gates → [BANK-512-036](#bank-512-036)

<a id="catalog-512-02"></a>
### Engineering

<a id="bank-512-004"></a>
- `BANK-512-004` — Error correction overhead → [BANK-512-043](#bank-512-043)
<a id="bank-512-005"></a>
- `BANK-512-005` — Decoherence → [BANK-512-037](#bank-512-037)
<a id="bank-512-006"></a>
- `BANK-512-006` — Qubit readout → [BANK-512-037](#bank-512-037)

<a id="catalog-512-03"></a>
### Evaluation

<a id="bank-512-007"></a>
- `BANK-512-007` — Quantum advantage claims → [BANK-512-038](#bank-512-038)
<a id="bank-512-008"></a>
- `BANK-512-008` — Algorithm input-output costs → [BANK-512-038](#bank-512-038)
<a id="bank-512-009"></a>
- `BANK-512-009` — Comparing classical baselines fairly → [BANK-512-038](#bank-512-038)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [062 Computer & PC](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

### Retired overlaps and primary questions

<a id="bank-512-031"></a>
- `BANK-512-031` → [BANK-055-027](../055_time_reality/IN_DEPTH_TOPIC_BANK.md#bank-055-027): The individual scopes describe substantially the same episode: Explain correlations, measurement outcomes and communication requirements without mystical inference. / Distinguish correlated outcomes and controllable signals. Retain one primary question and preserve the other full record inactive with a referral.

  Preserved inactive question: Why does entanglement not enable faster-than-light communication?

  Preserved inactive scope: Distinguish correlated outcomes and controllable signals.


## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- **Concrete case selection for Quantum networking distinctions:** Separate entanglement distribution and classical communication. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Algorithm-specific resource estimates:** Include error correction, depth and input-output work. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Control electronics:** Map wiring, timing, heat and calibration. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Reproducibility of benchmark claims:** Record tasks, noise, sampling and classical baselines. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.
- **Concrete case selection for Error-correction overhead:** Separate encoding overhead, error correlations, control quality and decoding assumptions without claiming a particular implementation has achieved a threshold. Select the actual case, documents or original demonstration before research; the proposal itself is scoped here.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/512_quantum_computing/NICHE_512_quantum_computing.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
