# 062 Computer & PC: Detailed Topic-Bank Draft

**8 categories · 32 individually authored episode proposals.**

Individually authored episode questions and coverage boundaries for Computer & PC. The subject progression is organized by concrete content rather than a topic-by-angle multiplication.

[All-niche progress](../DEPTH_COMPLETION_STATUS.md) · [All-niche index](../ALL_NICHE_TOPIC_BANKS.md) · [Editable bank](./IN_DEPTH_TOPIC_BANK.json)

Every question below has its own coverage boundary. All remain proposed; sources and current niche angle scopes have not been verified. Learning levels organize documentary research rather than physical difficulty. The older initial proposals remain in the JSON's prior_initial_map archive and are not counted again.

## 01. Reading the computer as a system

**Level:** foundation. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-062-013 | What happens between pressing a PC's power button and seeing the login screen? | Trace firmware, device initialization, boot selection and operating-system startup using vendor diagrams; distinguish stages without giving firmware-flashing instructions. |
| BANK-062-014 | How do CPU cores, clock speed and instruction behavior jointly affect work? | Compare a documented processor workload with serial and parallel portions; reject rankings based on clock rate alone. |
| BANK-062-015 | Why do RAM capacity and storage capacity solve different problems? | Follow a large working dataset through memory, paging and persistent files; use operating-system counters instead of treating free memory as the only performance measure. |
| BANK-062-016 | How does a motherboard determine which upgrades can actually work? | Read socket, chipset, firmware, physical-clearance and memory-support documentation for a named board revision; avoid compatibility claims based only on matching connectors. |

## 02. Processors and graphics

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-062-017 | Why can a CPU with more cores finish a particular task more slowly? | Compare scheduling, thermal limits, per-core work and software scaling under controlled conditions; identify benchmark versions and avoid a universal brand verdict. |
| BANK-062-018 | How does integrated graphics share resources with the rest of a PC? | Trace system memory, display outputs and power budgets using actual architecture documentation; distinguish graphics capability from discrete video-memory labels. |
| BANK-062-019 | What does GPU utilization fail to reveal about a rendering bottleneck? | Compare compute activity, memory bandwidth, VRAM allocation, decoding and CPU feeding through a defined workload; do not infer capability from one dashboard percentage. |
| BANK-062-020 | Why do video-memory capacity and graphics speed need separate evaluation? | Contrast a workload that fits in memory with one that spills or fails; include precision and software support instead of comparing gigabytes alone. |

## 03. Storage and data protection

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-062-021 | When does an SSD interface become less important than its sustained workload behavior? | Inspect latency, caching, temperature and steady-state writes from reproducible tests; keep SATA, PCIe generation and device controller behavior distinct. |
| BANK-062-022 | Why is a second partition on the same drive not an independent backup? | Model device failure, deletion and recovery boundaries; consult backup documentation and demonstrate only with disposable files. |
| BANK-062-023 | How can a restore test reveal gaps in an apparently successful backup? | Specify selected files, application state, encryption keys and recovery time; compare restored content against a known baseline without using private user data. |
| BANK-062-024 | What do drive-health indicators establish about future reliability? | Read manufacturer definitions and error records; distinguish warning signals, uncertainty and recoverability without promising that any status predicts failure precisely. |

## 04. Cooling, power and physical design

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-062-025 | How can a cooling limit change a processor's sustained performance? | Compare temperatures, clock behavior and power under a repeatable workload; use vendor operating limits and avoid encouraging thermal-protection bypasses. |
| BANK-062-026 | Why does a power supply's wattage label not establish its complete suitability? | Examine connectors, documented protections, transient requirements and independent test methods; exclude opening power supplies or improvising electrical connections. |
| BANK-062-027 | How do case airflow and dust affect maintenance decisions? | Map intake, exhaust, filters and accessibility using manufacturer service guidance; keep electrical cleaning precautions and model-specific disassembly boundaries explicit. |
| BANK-062-028 | What makes a laptop upgrade different from a desktop upgrade? | Compare soldered parts, service manuals, battery access and chassis clearance for specific models; avoid assuming replaceability from the product family's name. |

## 05. Operating systems and troubleshooting

**Level:** intermediate. **Evidence direction:** Inspect the actual product version, official documentation, terms and privacy policies. Test claims under stated conditions and distinguish account permissions, data retention, measured functionality and marketing.

**Source types to locate:** official versioned documentation and release notes; dated privacy policies and service terms; reproducible product tests and original validation reports. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-062-029 | How can Task Manager or another system monitor mislead a performance diagnosis? | Relate sampling intervals, per-process totals and resource categories to a controlled task; confirm tool definitions before interpreting a high or low percentage. |
| BANK-062-030 | What separates a driver problem from an application or hardware problem? | Design a reversible diagnosis using event records, version history and a known-good workload; exclude destructive resets as an unexplained first step. |
| BANK-062-031 | Why can startup programs slow access to an otherwise fast PC? | Measure login-to-ready time and background resource competition in an isolated account; distinguish startup impact labels from observed delay. |
| BANK-062-032 | How should an operating-system reinstall be planned so recovery is possible? | Inventory backups, application access, licenses, encryption recovery and official installation media; outline decision checkpoints rather than issuing a blanket erase procedure. |

## 06. Networks and peripherals

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-062-033 | How can slow Wi-Fi be separated from a slow internet connection? | Compare local transfer, signal conditions, router placement and wired baselines; state device capabilities and avoid unauthorized network scanning. |
| BANK-062-034 | Why can a USB-C connector support different data, charging and display functions? | Read host, cable and peripheral specifications together; distinguish connector shape, protocol support and power negotiation using verified documentation. |
| BANK-062-035 | What changes when a display is used for text, color work or fast motion? | Compare resolution, scaling, refresh behavior, calibration and viewing conditions; avoid reducing suitability to a single panel specification. |
| BANK-062-036 | How can a keyboard, mouse or audio delay be isolated across a setup? | Separate device, connection, driver and application stages with controlled substitution; report reproducible observations instead of attributing every delay to wireless technology. |

## 07. Workload matching and buying evidence

**Level:** advanced. **Evidence direction:** Define the rival claims and their evidence standards. Compare sources on equal terms, separate empirical findings from values or interpretations and do not imply that all positions have equal evidential support.

**Source types to locate:** the original sources behind the compared claims; explicit definitions and measurement methods; independent critiques with traceable evidence. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-062-037 | How should a PC be evaluated for video editing rather than gaming alone? | Define footage codec, resolution, effects, export path and application version; use representative project tests instead of transferring unrelated benchmark scores. |
| BANK-062-038 | What hardware constraints matter when testing a local language model? | Compare model size, precision, context memory, runtime support and measured speed; treat compatibility and acceptable responsiveness as different questions. |
| BANK-062-039 | How can a used PC listing be checked for missing or misleading specifications? | Compare exact component IDs, service history, support status and seller evidence; distinguish disclosed facts from claims that require inspection or return protection. |
| BANK-062-040 | When does a small upgrade have better evidence than replacing an entire system? | Identify the bottleneck, compatible alternatives, measured workload and total cost; leave prices and personal purchase choices for dated research. |

## 08. Accessibility, repair and end of life

**Level:** advanced. **Evidence direction:** Use the current official legal text, policy, procedure or public dataset for a specific jurisdiction and date. Distinguish written rules, implementation and lived access; give no personal legal or financial conclusion.

**Source types to locate:** official laws, rules and administrative guidance; audits, judgments and public service records; consented accounts from affected people and qualified specialists. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-062-041 | What should accessible PC setup consider beyond larger text? | Examine input alternatives, screen-reader support, audio cues and application compatibility with consented user testing; avoid assuming one setting serves all users. |
| BANK-062-042 | How do service documentation and spare-part access change repair feasibility? | Compare a named machine's procedures, diagnostics, part availability and local repair rules; keep warranty and legal statements jurisdiction-specific. |
| BANK-062-043 | How can a computer be prepared for transfer without exposing the previous owner's data? | Consult current vendor sanitization guidance for storage type and encryption state; distinguish account sign-out from verified erasure and keep demonstrations on spare media. |
| BANK-062-044 | What happens to a computer after it enters an electronics recycling stream? | Trace collection, reuse, material recovery and hazardous handling through authorized facilities; do not infer responsible disposal from a recycling logo alone. |

## Coverage limits and next step

This is an expanded topic-bank draft, not exhaustive scholarship or a researched episode package. Each question has an individually written boundary. Source access, claim verification, current angle-scope review and publication approval remain pending. Add new branches and cases when they fill a real gap; no numeric topic cap applies.

Select an exact case, edition, population, jurisdiction or product version, inspect sources and refine the question before using the existing registry idea/depth planning workflow. These BANK IDs are catalog identities, not approved IDEA IDs. Existing Q1-Q42 defaults, production queues and approval gates are unchanged.

## Related niche homes

- [061 Software & Programming](../061_software_programming/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [063 Consumer Technology](../063_consumer_technology/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [318 Internet](../318_internet/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [319 Mobile Technology](../319_mobile_technology/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [320 5G / 6G](../320_5g_6g/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [321 Satellite Internet](../321_satellite_internet/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
