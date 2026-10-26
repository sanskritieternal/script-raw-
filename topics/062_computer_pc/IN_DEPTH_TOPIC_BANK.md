# 062 — Computer & PC: main topic bank

Updated: 2026-10-24 · **48 active BANK proposals · 6 categories · 11 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Reading the computer as a system](#catalog-062-d01).
- **Intermediate:** [Processors and graphics](#catalog-062-d02) → [Storage and data protection](#catalog-062-d03) → [Cooling, power and physical design](#catalog-062-d04) → [Operating systems and troubleshooting](#catalog-062-d05) → [Networks and peripherals](#catalog-062-d06) → [Firmware, clocks and device identity](#catalog-062-r01) → [Working sets and memory transfer](#catalog-062-r02).
- **Advanced:** [Workload matching and buying evidence](#catalog-062-d07) → [Accessibility, repair and end of life](#catalog-062-d08) → [Version compatibility and recovery](#catalog-062-r03).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Computer systems, compute and storage](#domain-062-g01) | 5 | 13 | 0 |
| [Power, operating systems and connections](#domain-062-g02) | 0 | 15 | 0 |
| [Workloads, access and lifecycle](#domain-062-g03) | 0 | 0 | 10 |
| [PC interfaces](#domain-062-09) | 0 | 3 | 0 |
| [Computer performance](#domain-062-10) | 0 | 1 | 0 |
| [Computer firmware](#domain-062-11) | 0 | 0 | 1 |

<a id="domain-062-g01"></a>
## Category: Computer systems, compute and storage

<a id="catalog-062-d01"></a>
### Reading the computer as a system

Subcategory `CATALOG-062-D01` · foundation.

<a id="bank-062-013"></a>
#### BANK-062-013 — What happens between pressing a PC's power button and seeing the login screen?

**Individual coverage scope:** Trace firmware, device initialization, boot selection and operating-system startup using vendor diagrams; distinguish stages without giving firmware-flashing instructions.

<a id="bank-062-014"></a>
#### BANK-062-014 — How do CPU cores, clock speed and instruction behavior jointly affect work?

**Individual coverage scope:** Compare a documented processor workload with serial and parallel portions; reject rankings based on clock rate alone.

<a id="bank-062-015"></a>
#### BANK-062-015 — Why do RAM capacity and storage capacity solve different problems?

**Individual coverage scope:** Follow a large working dataset through memory, paging and persistent files; use operating-system counters instead of treating free memory as the only performance measure.

<a id="bank-062-016"></a>
#### BANK-062-016 — How does a motherboard determine which upgrades can actually work?

**Individual coverage scope:** Read socket, chipset, firmware, physical-clearance and memory-support documentation for a named board revision; avoid compatibility claims based only on matching connectors.

<a id="bank-062-053"></a>
#### BANK-062-053 — Which PCIe lanes are available to a device on one motherboard?

**Individual coverage scope:** Map CPU and chipset lanes, link generation and shared slots using a named board manual, then test actual link width and workload rather than quote raw bandwidth alone.

**Research follow-up:** [Bounded case and source-access note](SELECTED_SOURCE_NOTE.md). This does not change proposal or production status.

<a id="catalog-062-d02"></a>
### Processors and graphics

Subcategory `CATALOG-062-D02` · intermediate.

Prerequisites: [CATALOG-062-D01](#catalog-062-d01).

<a id="bank-062-017"></a>
#### BANK-062-017 — Why can a CPU with more cores finish a particular task more slowly?

**Individual coverage scope:** Compare scheduling, thermal limits, per-core work and software scaling under controlled conditions; identify benchmark versions and avoid a universal brand verdict.

<a id="bank-062-018"></a>
#### BANK-062-018 — How does integrated graphics share resources with the rest of a PC?

**Individual coverage scope:** Trace system memory, display outputs and power budgets using actual architecture documentation; distinguish graphics capability from discrete video-memory labels.

<a id="bank-062-019"></a>
#### BANK-062-019 — What does GPU utilization fail to reveal about a rendering bottleneck?

**Individual coverage scope:** Compare compute activity, memory bandwidth, VRAM allocation, decoding and CPU feeding through a defined workload; do not infer capability from one dashboard percentage.

<a id="bank-062-020"></a>
#### BANK-062-020 — Why do video-memory capacity and graphics speed need separate evaluation?

**Individual coverage scope:** Contrast a workload that fits in memory with one that spills or fails; include precision and software support instead of comparing gigabytes alone.

<a id="bank-062-051"></a>
#### BANK-062-051 — What limited Pentium 4 NetBurst clock scaling, and what changed afterward?

**Individual coverage scope:** Compare dated processor models, thermal guidance, power and instructions per clock; avoid a false hard 4 GHz barrier or a single-cause account of Intel?s architecture shift.

<a id="bank-062-054"></a>
#### BANK-062-054 — When does ray tracing improve a rendered scene enough to justify its PC cost?

**Individual coverage scope:** Compare the same game or renderer with rasterization and selected ray-traced effects, holding resolution, quality settings and hardware fixed.

<a id="bank-062-055"></a>
#### BANK-062-055 — What did Apple?s first M1 Mac change about PC architecture comparisons?

**Individual coverage scope:** Compare a named 2020 M1 Mac with a contemporary x86 system for workload, power, integrated memory and software compatibility; avoid architecture-wide winner claims.

**Research follow-up:** [Bounded case and source-access note](SELECTED_SOURCE_NOTE.md). This does not change proposal or production status.

<a id="bank-062-059"></a>
#### BANK-062-059 — Which workloads benefit from an AMD 3D V-Cache processor, and why?

**Individual coverage scope:** Compare named X3D and non-X3D models under matched memory, GPU and game settings; relate cache behavior to observed results without universal victory claims.

<a id="catalog-062-d03"></a>
### Storage and data protection

Subcategory `CATALOG-062-D03` · intermediate.

Prerequisites: [CATALOG-062-D01](#catalog-062-d01).

<a id="bank-062-021"></a>
#### BANK-062-021 — When does an SSD interface become less important than its sustained workload behavior?

**Individual coverage scope:** Inspect latency, caching, temperature and steady-state writes from reproducible tests; keep SATA, PCIe generation and device controller behavior distinct.

<a id="bank-062-022"></a>
#### BANK-062-022 — Why is a second partition on the same drive not an independent backup?

**Individual coverage scope:** Model device failure, deletion and recovery boundaries; consult backup documentation and demonstrate only with disposable files.

<a id="bank-062-023"></a>
#### BANK-062-023 — How can a restore test reveal gaps in an apparently successful backup?

**Individual coverage scope:** Specify selected files, application state, encryption keys and recovery time; compare restored content against a known baseline without using private user data.

<a id="bank-062-024"></a>
#### BANK-062-024 — What do drive-health indicators establish about future reliability?

**Individual coverage scope:** Read manufacturer definitions and error records; distinguish warning signals, uncertainty and recoverability without promising that any status predicts failure precisely.

<a id="bank-062-057"></a>
#### BANK-062-057 — When does an SSD slow after its write cache fills?

**Individual coverage scope:** Test a named NAND type, controller, capacity and firmware across sustained writes and recovery time; distinguish SLC caching from intrinsic QLC speed.


<a id="domain-062-g02"></a>
## Category: Power, operating systems and connections

<a id="catalog-062-d04"></a>
### Cooling, power and physical design

Subcategory `CATALOG-062-D04` · intermediate.

Prerequisites: [CATALOG-062-D01](#catalog-062-d01).

<a id="bank-062-025"></a>
#### BANK-062-025 — How can a cooling limit change a processor's sustained performance?

**Individual coverage scope:** Compare temperatures, clock behavior and power under a repeatable workload; use vendor operating limits and avoid encouraging thermal-protection bypasses.

<a id="bank-062-026"></a>
#### BANK-062-026 — Why does a power supply's wattage label not establish its complete suitability?

**Individual coverage scope:** Examine connectors, documented protections, transient requirements and independent test methods; exclude opening power supplies or improvising electrical connections.

<a id="bank-062-027"></a>
#### BANK-062-027 — How do case airflow and dust affect maintenance decisions?

**Individual coverage scope:** Map intake, exhaust, filters and accessibility using manufacturer service guidance; keep electrical cleaning precautions and model-specific disassembly boundaries explicit.

<a id="bank-062-028"></a>
#### BANK-062-028 — What makes a laptop upgrade different from a desktop upgrade?

**Individual coverage scope:** Compare soldered parts, service manuals, battery access and chassis clearance for specific models; avoid assuming replaceability from the product family's name.

<a id="bank-062-052"></a>
#### BANK-062-052 — How does a motherboard VRM support a specific CPU under changing load?

**Individual coverage scope:** Trace voltage conversion, phases, thermal limits and board power settings on one documented board; do not infer quality or safety from phase count alone.

<a id="bank-062-056"></a>
#### BANK-062-056 — Why can a PC power supply fail during a brief GPU load spike?

**Individual coverage scope:** Use a named GPU, PSU and ATX revision to compare sustained draw, excursions, connectors and protection behavior; distinguish shutdown evidence from a wattage-label anecdote.

**Research follow-up:** [Bounded case and source-access note](SELECTED_SOURCE_NOTE.md). This does not change proposal or production status.

<a id="catalog-062-d05"></a>
### Operating systems and troubleshooting

Subcategory `CATALOG-062-D05` · intermediate.

Prerequisites: [CATALOG-062-D01](#catalog-062-d01).

<a id="bank-062-029"></a>
#### BANK-062-029 — How can Task Manager or another system monitor mislead a performance diagnosis?

**Individual coverage scope:** Relate sampling intervals, per-process totals and resource categories to a controlled task; confirm tool definitions before interpreting a high or low percentage.

<a id="bank-062-030"></a>
#### BANK-062-030 — What separates a driver problem from an application or hardware problem?

**Individual coverage scope:** Design a reversible diagnosis using event records, version history and a known-good workload; exclude destructive resets as an unexplained first step.

<a id="bank-062-031"></a>
#### BANK-062-031 — Why can startup programs slow access to an otherwise fast PC?

**Individual coverage scope:** Measure login-to-ready time and background resource competition in an isolated account; distinguish startup impact labels from observed delay.

<a id="bank-062-032"></a>
#### BANK-062-032 — How should an operating-system reinstall be planned so recovery is possible?

**Individual coverage scope:** Inventory backups, application access, licenses, encryption recovery and official installation media; outline decision checkpoints rather than issuing a blanket erase procedure.

<a id="bank-062-058"></a>
#### BANK-062-058 — What did Intel identify in the 13th and 14th generation desktop Vmin instability issue?

**Individual coverage scope:** Trace Intel?s dated root-cause statements, affected desktop SKUs, board settings and BIOS microcode versions; distinguish prevention from repair of degraded processors.

**Research follow-up:** [Bounded case and source-access note](SELECTED_SOURCE_NOTE.md). This does not change proposal or production status.

<a id="catalog-062-d06"></a>
### Networks and peripherals

Subcategory `CATALOG-062-D06` · intermediate.

Prerequisites: [CATALOG-062-D01](#catalog-062-d01).

<a id="bank-062-033"></a>
#### BANK-062-033 — How can slow Wi-Fi be separated from a slow internet connection?

**Individual coverage scope:** Compare local transfer, signal conditions, router placement and wired baselines; state device capabilities and avoid unauthorized network scanning.

<a id="bank-062-034"></a>
#### BANK-062-034 — Why can a USB-C connector support different data, charging and display functions?

**Individual coverage scope:** Read host, cable and peripheral specifications together; distinguish connector shape, protocol support and power negotiation using verified documentation.

<a id="bank-062-035"></a>
#### BANK-062-035 — What changes when a display is used for text, color work or fast motion?

**Individual coverage scope:** Compare resolution, scaling, refresh behavior, calibration and viewing conditions; avoid reducing suitability to a single panel specification.

<a id="bank-062-036"></a>
#### BANK-062-036 — How can a keyboard, mouse or audio delay be isolated across a setup?

**Individual coverage scope:** Separate device, connection, driver and application stages with controlled substitution; report reproducible observations instead of attributing every delay to wireless technology.


<a id="domain-062-g03"></a>
## Category: Workloads, access and lifecycle

<a id="catalog-062-d07"></a>
### Workload matching and buying evidence

Subcategory `CATALOG-062-D07` · advanced.

Prerequisites: [CATALOG-062-D01](#catalog-062-d01).

<a id="bank-062-037"></a>
#### BANK-062-037 — How should a PC be evaluated for video editing rather than gaming alone?

**Individual coverage scope:** Define footage codec, resolution, effects, export path and application version; use representative project tests instead of transferring unrelated benchmark scores.

<a id="bank-062-038"></a>
#### BANK-062-038 — What hardware constraints matter when testing a local language model?

**Individual coverage scope:** Compare model size, precision, context memory, runtime support and measured speed; treat compatibility and acceptable responsiveness as different questions.

<a id="bank-062-039"></a>
#### BANK-062-039 — How can a used PC listing be checked for missing or misleading specifications?

**Individual coverage scope:** Compare exact component IDs, service history, support status and seller evidence; distinguish disclosed facts from claims that require inspection or return protection.

<a id="bank-062-040"></a>
#### BANK-062-040 — When does a small upgrade have better evidence than replacing an entire system?

**Individual coverage scope:** Identify the bottleneck, compatible alternatives, measured workload and total cost; leave prices and personal purchase choices for dated research.

<a id="bank-062-060"></a>
#### BANK-062-060 — When does enabling XMP or EXPO change an actual PC workload?

**Individual coverage scope:** Use a specified CPU, motherboard, BIOS and DDR profile; test stability and task time with the profile on and off, separating rated speed from achieved benefit.

**Research follow-up:** [Bounded case and source-access note](SELECTED_SOURCE_NOTE.md). This does not change proposal or production status.

<a id="catalog-062-d08"></a>
### Accessibility, repair and end of life

Subcategory `CATALOG-062-D08` · advanced.

Prerequisites: [CATALOG-062-D01](#catalog-062-d01).

<a id="bank-062-041"></a>
#### BANK-062-041 — What should accessible PC setup consider beyond larger text?

**Individual coverage scope:** Examine input alternatives, screen-reader support, audio cues and application compatibility with consented user testing; avoid assuming one setting serves all users.

<a id="bank-062-042"></a>
#### BANK-062-042 — How do service documentation and spare-part access change repair feasibility?

**Individual coverage scope:** Compare a named machine's procedures, diagnostics, part availability and local repair rules; keep warranty and legal statements jurisdiction-specific.

<a id="bank-062-043"></a>
#### BANK-062-043 — How can a computer be prepared for transfer without exposing the previous owner's data?

**Individual coverage scope:** Consult current vendor sanitization guidance for storage type and encryption state; distinguish account sign-out from verified erasure and keep demonstrations on spare media.

<a id="bank-062-044"></a>
#### BANK-062-044 — What happens to a computer after it enters an electronics recycling stream?

**Individual coverage scope:** Trace collection, reuse, material recovery and hazardous handling through authorized facilities; do not infer responsible disposal from a recycling logo alone.

<a id="bank-062-061"></a>
#### BANK-062-061 — Why did built-in optical drives disappear from many desktop PCs?

**Individual coverage scope:** Compare dated case designs, software distribution, media use and external-drive options; identify markets where discs remain relevant instead of declaring the format dead.


<a id="domain-062-09"></a>
## Category: PC interfaces

<a id="catalog-062-r01"></a>
### Firmware, clocks and device identity

Subcategory `CATALOG-062-R01` · intermediate.

<a id="bank-062-045"></a>
#### BANK-062-045 — What happens before an operating system begins to load?

**Individual coverage scope:** Trace firmware initialization, device discovery, boot selection and handoff conceptually; exclude bypassing security controls.

<a id="bank-062-047"></a>
#### BANK-062-047 — How does a computer keep time after it is turned off?

**Individual coverage scope:** Compare hardware clocks, firmware settings, network synchronization and operating-system interpretation.

<a id="bank-062-048"></a>
#### BANK-062-048 — What changes when a storage drive reports healthy status but files fail integrity checks?

**Individual coverage scope:** Separate hardware indicators, filesystem metadata, memory errors, application writes and backups without diagnosing a real device.


<a id="domain-062-10"></a>
## Category: Computer performance

<a id="catalog-062-r02"></a>
### Working sets and memory transfer

Subcategory `CATALOG-062-R02` · intermediate.

<a id="bank-062-049"></a>
#### BANK-062-049 — Why can a workload fit in RAM yet run slowly because of cache misses or limited memory bandwidth?

**Individual coverage scope:** Compare cache hierarchy, locality, working set, access patterns, latency and bandwidth using labeled benign benchmarks; distinguish capacity from the rate and pattern of moving data.


<a id="domain-062-11"></a>
## Category: Computer firmware

<a id="catalog-062-r03"></a>
### Version compatibility and recovery

Subcategory `CATALOG-062-R03` · advanced.

<a id="bank-062-050"></a>
#### BANK-062-050 — What should a firmware-update explanation establish about compatibility and recovery before describing a change?

**Individual coverage scope:** Compare exact model, supported version, release notes, configuration retention, recovery documentation and vendor responsibilities; exclude flashing instructions, bypasses or a guarantee that updating fixes an observed fault.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

### pending_topics/0 — Why Did Intel Fail to Break 4 GHz for 15 Years? The NetBurst Thermal Wall That Changed PC History

**Original question:** Why did Intel promise in 2000 that Pentium 4 would reach 10 GHz, only to hit a catastrophic 130-watt thermal meltdown at 3.8 GHz that forced an entire architectural surrender?

**Original planning scope:** 31-stage NetBurst execution pipeline, pipeline stall penalties, dynamic power dissipation scaling with frequency cubed (P = C*V^2*f), Israeli design team saving Intel with Core 2 Duo (Conroe).

**Editorial disposition:** authored_case. case added: NetBurst dated clock/heat comparison

**Scoped proposals:** [BANK-062-051](#bank-062-051).

### pending_topics/1 — How a CPU Actually Works: From Quartz Crystals and Clocks to Fetch-Decode-Execute

**Original question:** How does an electrical pulse from a vibrating quartz crystal coordinate billions of microscopic silicon transistors through the fetch, decode, execute, and writeback cycle 4 billion times a second?

**Original planning scope:** Program counter, instruction register and control unit decoding micro-ops, arithmetic logic unit (ALU), L1/L2 cache latency differences, branch prediction.

**Editorial disposition:** existing_scope. existing CPU execution scope

**Scoped proposals:** [BANK-062-014](#bank-062-014).

### pending_topics/2 — Motherboard VRMs: The 16-Phase Power Station Keeping Your $600 CPU from Burning

**Original question:** How does your motherboard cleanly step down 12 volts from the power supply to an ultra-precise 1.25 volts at 250 amperes without boiling its MOSFETs?

**Original planning scope:** Buck converter topology, high-side and low-side MOSFETs, ferrite chokes and solid capacitors, pulse-width modulation (PWM) multi-phase switching, Vdroop and Load-Line Calibration (LLC).

**Editorial disposition:** authored_case. case added: board VRM, not phase count alone

**Scoped proposals:** [BANK-062-052](#bank-062-052).

### pending_topics/3 — Thermal Paste vs Liquid Metal: The Microscopic Battle for Heat Transfer

**Original question:** Why does a 0.1-millimeter microscopic air gap trap heat like an oven, and how does gallium-indium liquid metal drop temperatures by 15°C while threatening to short-circuit motherboards?

**Original planning scope:** Surface roughness and microscopic air voids, thermal conductivity ratings (silicone paste 8 W/mK vs liquid metal 73 W/mK), CPU delidding, gallium galvanic corrosion of aluminum heat sinks.

**Editorial disposition:** existing_scope. cooling scope; model and paste conditions needed

**Scoped proposals:** [BANK-062-025](#bank-062-025).

### pending_topics/4 — PCIe Lanes and Chipsets: How Data Moves at 64 GB/s Across the Motherboard

**Original question:** What is the difference between lanes wired directly to the CPU and lanes routed through the motherboard chipset, and why do high-end NVMe drives share bandwidth with graphics cards?

**Original planning scope:** Differential signaling and NRZ vs PAM4 encoding in PCIe 5.0/6.0, direct CPU lanes vs DMI chipset multiplexing, slot bifurcation (x16 to x8/x8), latency implications.

**Editorial disposition:** authored_case. case added: board-specific PCIe lane map

**Scoped proposals:** [BANK-062-053](#bank-062-053).

### pending_topics/5 — Ray Tracing vs Rasterization: The 30-Year Battle for Photorealistic Gaming Graphics

**Original question:** Why did GPUs fake lighting with rasterized tricks for three decades, and how do dedicated RT cores calculate millions of bounding volume hierarchy (BVH) ray bounces in real time?

**Original planning scope:** Rasterization polygon projection and depth z-buffering, Bounding Volume Hierarchy (BVH) ray traversal, temporal anti-aliasing and AI denoising (DLSS), rendering physical light physics.

**Editorial disposition:** authored_case. case added: bounded graphics workload

**Scoped proposals:** [BANK-062-054](#bank-062-054).

### pending_topics/6 — x86 vs ARM: Why Apple Silicon M1 Shocked the Entire PC Industry

**Original question:** How did a mobile phone chip architecture humiliate 100-watt desktop Intel and AMD processors while using a tiny fan-less battery chassis?

**Original planning scope:** CISC variable-length decoding legacy overhead vs RISC fixed-length instructions, massive 8-wide decode engines, Unified Memory Architecture (UMA) on-package bandwidth, memory reordering.

**Editorial disposition:** authored_case. case added: dated M1 system comparison

**Scoped proposals:** [BANK-062-055](#bank-062-055).

### pending_topics/7 — Liquid Nitrogen Overclocking: Breaking 9 GHz at -196°C

**Original question:** What happens to silicon transistors when cooled to -196°C with bubbling liquid nitrogen, and why do chips suddenly stop working if they get too cold (the Cold Bug)?

**Original planning scope:** Carrier mobility increase at sub-zero temperatures, condensation insulation with kneaded eraser putty, the silicon 'Cold Bug' and 'Cold Boot Bug', pushing 2.0+ volts into flagship dies.

**Editorial disposition:** existing_scope. cooling scope; overclock record conditions needed

**Scoped proposals:** [BANK-062-025](#bank-062-025).

### pending_topics/8 — Nvidia CUDA: The Secret Software Moat That Created a $3 Trillion AI Monopoly

**Original question:** How did Jensen Huang spend hundreds of millions in 2006 to add non-gaming compute logic to every GeForce graphics card, laying the foundation for modern ChatGPT and AI dominance?

**Original planning scope:** General-Purpose computing on GPUs (GPGPU), SIMT (Single Instruction, Multiple Threads) parallel execution, PyTorch and TensorFlow deep integration, why AMD's ROCm struggled to catch up.

**Editorial disposition:** existing_scope. AI workload scope; market-cap claim unverified

**Scoped proposals:** [BANK-062-038](#bank-062-038).

### pending_topics/9 — GPU Power Transients: Why 450-Watt Graphics Cards Were Tripping 1,000-Watt Power Supplies

**Original question:** Why did modern RTX 30 and 40 series graphics cards shut down high-end power supplies in 10 microseconds, and why did new 12VHPWR power cables melt?

**Original planning scope:** Microsecond transient spikes exceeding 250% TDP, power supply overcurrent protection (OCP) tripping, ATX 3.0 specification revisions, terminal pin contact resistance in 12VHPWR connectors.

**Editorial disposition:** authored_case. case added: transient versus steady PSU load

**Scoped proposals:** [BANK-062-056](#bank-062-056).

### pending_topics/10 — The Evolution of Solid State Drives: From 2.5-Inch SATA to PCIe 5.0 Blowtorches

**Original question:** How did storage jump from 500 MB/s SATA bottlenecks to 14,000 MB/s NVMe drives, and why do the newest Gen 5 SSDs require active cooling fans?

**Original planning scope:** AHCI legacy spinning disk queue limits vs NVMe 64,000 deep parallel queues, 3D charge-trap NAND stacking (232+ layers), controller thermal throttling at 80°C.

**Editorial disposition:** existing_scope. SSD interface scope already covers transition

**Scoped proposals:** [BANK-062-021](#bank-062-021).

### pending_topics/11 — SLC, MLC, TLC, and QLC: Why Cheaper SSDs Slow Down to Hard Drive Speeds During Large Transfers

**Original question:** How does storing 4 bits of data in a single microscopic floating gate require distinguishing between 16 precise voltage levels, and what happens when the fast pseudo-SLC cache fills up?

**Original planning scope:** Voltage charge drift, write endurance cycles (TBW) collapsing from 10,000 to 300 cycles, SLC caching buffer tricks, sudden drop to 80 MB/s sustained write speeds.

**Editorial disposition:** authored_case. case added: sustained NAND/cache test

**Scoped proposals:** [BANK-062-057](#bank-062-057).

### pending_topics/12 — Electromigration: The Invisible Atomic River That Slowly Kills Overclocked CPUs

**Original question:** How does a flood of moving electrons physically knock copper atoms down microscopic wire traces until a $500 CPU develops voids, short circuits, and crashes?

**Original planning scope:** Black's Equation for Mean Time to Failure (MTTF), exponential acceleration by temperature and current density (J^2), the danger of manual fixed high Vcore overclocks.

**Editorial disposition:** existing_scope. cooling/reliability scope; voltage/temperature needed

**Scoped proposals:** [BANK-062-025](#bank-062-025).

### pending_topics/13 — RAM Sub-Timings: How Tuning 30 Secondary Numbers Gives Free Gaming Performance

**Original question:** Why does buying 6000 MHz RAM only give you half its potential performance unless you manually tighten obscure secondary numbers like tRFC and tREFI in BIOS?

**Original planning scope:** DRAM capacitor refresh cycles, CAS Latency (tCL) vs turnaround timings (tRFC), refreshing capacitor rows before charge drains, 1% low FPS stabilization in gaming.

**Editorial disposition:** existing_scope. memory behavior scope; free gain unverified

**Scoped proposals:** [BANK-062-049](#bank-062-049).

### pending_topics/14 — The Intel 13th and 14th Gen Instability Crisis: Microcode, Oxidation, and Elevated Voltages

**Original question:** Why were flagship Core i9 processors crashing in Unreal Engine games and game server farms across the globe throughout 2024?

**Original planning scope:** Elevated VID microcode requests during idle/low-load states, Vmin shift causing permanent ring bus silicon degradation, manufacturing via oxidation defects, warranty extensions.

**Editorial disposition:** authored_case. case added: Intel desktop Vmin and microcode

**Scoped proposals:** [BANK-062-058](#bank-062-058).

### pending_topics/15 — Quantum Computing Chips: Qubits Suspended in Gold Cryogenic Chandelier Fridges

**Original question:** How do IBM and Google cool niobium-aluminum superconducting chips to 15 millikelvin—colder than deep space—to manipulate quantum superposition and entanglement?

**Original planning scope:** Transmon qubits and Josephson junctions, microwave pulse quantum logic gates, dilution refrigerators using Helium-3/Helium-4 phase separation, quantum decoherence error rates.

**Editorial disposition:** existing_scope. external quantum processor primary home

**Scoped proposals:** [BANK-512-036](../512_quantum_computing/IN_DEPTH_TOPIC_BANK.md#bank-512-036).

### pending_topics/16 — Neuromorphic Chips: Silicon Brains That Process Information with Spiking Neurons

**Original question:** Why do traditional computers waste 90% of their power shuttling data between separate CPU and RAM chips, and how do neuromorphic chips merge memory and compute like real brain synapses?

**Original planning scope:** The Von Neumann bottleneck, Spiking Neural Networks (SNNs), Intel Loihi 2 and IBM TrueNorth chips, memristor analog weight storage, 1,000x energy efficiency for edge AI.

**Editorial disposition:** existing_scope. CPU comparison scope; select actual neuromorphic chip

**Scoped proposals:** [BANK-062-014](#bank-062-014).

### pending_topics/17 — Silicon Photonics: Replacing Copper Traces on Motherboards with Microscopic Laser Beams

**Original question:** When copper wires hit an electrical impedance wall at 100 GHz, how will microscopic glass waveguides etched directly into silicon dies transport data at the speed of light?

**Original planning scope:** Co-Packaged Optics (CPO), micro-ring resonators and optical modulators, eliminating electrical resistance heat loss, TSMC and Intel optical engine roadmaps.

**Editorial disposition:** existing_scope. board compatibility scope; replacement claim unverified

**Scoped proposals:** [BANK-062-016](#bank-062-016).

### pending_topics/18 — The Death of Moore's Law: 3D Chiplets, Gate-All-Around (GAA), and Backside Power

**Original question:** How are engineers keeping transistor scaling alive after hitting the limits of FinFETs by wrapping gates entirely around silicon ribbons and routing power from behind the wafer?

**Original planning scope:** Gate-All-Around (GAAFET / RibbonFET) nanosheets, Intel PowerVia and TSMC A16 backside power delivery networks, 3D V-Cache vertical silicon stacking, economic packaging costs.

**Editorial disposition:** existing_scope. external chiplet interface primary home

**Scoped proposals:** [BANK-511-041](../511_semiconductors/IN_DEPTH_TOPIC_BANK.md#bank-511-041).

### pending_topics/19 — The Personal Computer in 2040: What Replaces the Desktop Tower?

**Original question:** Will traditional desktop towers with fans and copper heatsinks exist in 2040, or will computing dissolve into decentralized ambient nodes and high-bandwidth optical wireless displays?

**Original planning scope:** Diamond wafer substrate thermal dissipation, localized AI accelerator nodes, high-bandwidth wireless mmWave display protocols, the eternal survival of enthusiast modular building.

**Editorial disposition:** existing_scope. upgrade versus replacement scenarios; no 2040 prediction

**Scoped proposals:** [BANK-062-040](#bank-062-040).

### trending_topics/0 — Why Buying Faster RAM Might Do Absolutely Nothing for Your PC (XMP / EXPO)

**Editorial disposition:** authored_case. case added: XMP/EXPO versioned workload test

**Scoped proposals:** [BANK-062-060](#bank-062-060).

### trending_topics/1 — The Intel 13th & 14th Gen Disaster: What Actually Caused the Crashes?

**Editorial disposition:** existing_scope. direct overlap with Intel desktop Vmin case

**Scoped proposals:** [BANK-062-058](#bank-062-058).

### trending_topics/2 — Why Your Graphics Card Needs a Support Bracket (GPU Sag Cracking Circuit Boards)

**Editorial disposition:** existing_scope. case support needs actual card and slot guidance

**Scoped proposals:** [BANK-062-027](#bank-062-027).

### trending_topics/3 — How to Clean Dust from a PC Without Damaging Fans (The Vacuum Myth)

**Editorial disposition:** existing_scope. dust maintenance already scoped; follow hardware guidance

**Scoped proposals:** [BANK-062-027](#bank-062-027).

### trending_topics/4 — Why Did AMD's 3D V-Cache Crush Intel in Gaming? The Cache Magic Explained

**Editorial disposition:** authored_case. case added: named X3D workload comparison

**Scoped proposals:** [BANK-062-059](#bank-062-059).

### trending_topics/5 — The $100 PC Case That Stole the Entire Market: The Lian Li O11 Dynamic Phenomenon

**Editorial disposition:** existing_scope. case design belongs to airflow/maintenance; sales claim unverified

**Scoped proposals:** [BANK-062-027](#bank-062-027).

### trending_topics/6 — Why Did We Stop Putting Optical CD/DVD Drives in Desktop PCs?

**Editorial disposition:** authored_case. case added: optical-drive form-factor history

**Scoped proposals:** [BANK-062-061](#bank-062-061).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-062-01"></a>
### PC architecture

<a id="bank-062-001"></a>
- `BANK-062-001` — CPU cache and memory hierarchy → [BANK-062-049](#bank-062-049)
<a id="bank-062-002"></a>
- `BANK-062-002` — RAM capacity versus bandwidth → [BANK-062-049](#bank-062-049)
<a id="bank-062-003"></a>
- `BANK-062-003` — GPU compute versus graphics workloads → [BANK-062-018](#bank-062-018), [BANK-062-019](#bank-062-019)
<a id="bank-062-004"></a>
- `BANK-062-004` — Storage latency and queue depth → [BANK-062-021](#bank-062-021)

<a id="catalog-062-02"></a>
### Build and maintenance

<a id="bank-062-005"></a>
- `BANK-062-005` — Power-supply sizing assumptions → [BANK-062-026](#bank-062-026)
<a id="bank-062-006"></a>
- `BANK-062-006` — Cooling airflow and dust → [BANK-062-027](#bank-062-027)
<a id="bank-062-007"></a>
- `BANK-062-007` — Firmware updates and recovery → [BANK-062-045](#bank-062-045), [BANK-062-050](#bank-062-050)
<a id="bank-062-008"></a>
- `BANK-062-008` — Diagnosing boot failures systematically → [BANK-062-013](#bank-062-013), [BANK-062-030](#bank-062-030)

<a id="catalog-062-03"></a>
### Evaluation

<a id="bank-062-009"></a>
- `BANK-062-009` — Reading benchmark methodology → [BANK-062-017](#bank-062-017)
<a id="bank-062-010"></a>
- `BANK-062-010` — VRAM limits in local AI → [BANK-062-038](#bank-062-038)
<a id="bank-062-011"></a>
- `BANK-062-011` — Laptop thermal throttling → [BANK-062-025](#bank-062-025)
<a id="bank-062-012"></a>
- `BANK-062-012` — Upgrade value over a system's lifespan → [BANK-062-040](#bank-062-040)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [321 Satellite Internet](../321_satellite_internet/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

### Retired overlaps and primary questions

<a id="bank-062-046"></a>
- `BANK-062-046` → [BANK-062-034](../062_computer_pc/IN_DEPTH_TOPIC_BANK.md#bank-062-034): The individual scopes describe substantially the same episode: Read host, cable and peripheral specifications together; distinguish connector shape, protocol support and power negotiation using verified documentation. / Compare connector shape, protocol, cable capability, host, device and power negotiation with version-specific verification deferred. Retain one primary question and preserve the other full record inactive with a referral.

  Preserved inactive question: Why can a fast USB-shaped connector deliver a slower connection than expected?

  Preserved inactive scope: Compare connector shape, protocol, cable capability, host, device and power negotiation with version-specific verification deferred.


## Editorial coverage review

All 20 pending and 7 trending archived pitches have explicit dispositions. Eleven distinct versioned or model-specific PC cases were added; 16 pitches route to existing active scopes or a shared new case. Selected primary sources and scope boundaries are in SELECTED_SOURCE_NOTE.md. Coverage remains open.


## Coverage remaining open

- **Further case and comparison depth:** Select distinct named cases, regional and language variants, overlooked participants, and contrary examples within Reading the computer as a system, Processors and graphics, Storage and data protection. Review actual scopes before adding an episode; these are coverage directions rather than a claim that present questions exhaust the niche.
- **Sources and readiness:** Inspect actual source access, dates, editions, versions, methods and competing evidence. No new source verification, research certification or production approval was performed.
- **Neighboring-niche boundary review:** Before producing an episode, compare related banks and assign one primary home. A lexical duplicate check does not establish semantic uniqueness across every pair.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/062_computer_pc/NICHE_062_computer_pc.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
