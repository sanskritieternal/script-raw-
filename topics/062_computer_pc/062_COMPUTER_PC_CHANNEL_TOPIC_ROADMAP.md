# Computer & PC Channel Master Topic Roadmap (Scratch to Advanced)
**Niche:** 062 Computer & PC (Computing_Software)  
**Channel Language:** English (YouTube)  
**Target Audience:** PC Builders, Hardware Enthusiasts, Overclockers, System Architects, Retro-Computing Geeks (Global)  
**Production Format:** 10-Minute Documentary Explainer Episodes (600s, 75 Fixed 8s Scenes)  
**Execution & Sync Report:** [topics/062_computer_pc/TOPICS_COVERED_REPORT.md](./TOPICS_COVERED_REPORT.md)  

---

## 1. Channel Progression Strategy

This curriculum organizes the core disciplines of Computer & PC across four progressive tiers:
- **Tier 1: Silicon Architecture, Motherboard Buses & Power Delivery (Scratch / Beginner)** — CPU die layout, PCIe 5.0 lanes, VRM power phases, BIOS/UEFI firmware handoffs, and thermal interface material (TIM) heat transfer.
- **Tier 2: The GPU Revolution, Clock Cycles & Extreme Overclocking (Intermediate)** — Rasterization pipelines vs ray tracing RT cores, CUDA matrix streaming, liquid nitrogen sub-zero benching, and x86 CISC vs ARM RISC microcode.
- **Tier 3: Storage Evolution, Silicon Degradation & Memory Timings (Upper Intermediate)** — Spinning platters to 3D TLC/QLC NAND flash, CAS latency sub-timings, electromigration atomic drift, and transient load line power spikes.
- **Tier 4: Quantum Computing Chips, Neuromorphic Hardware & The Optical Bus (Advanced / Expert)** — Superconducting transmon qubits, dilution refrigerators at 15 millikelvin, memristor neuromorphic processing, and silicon photonics optical interconnects.

---

## 2. Topic Styles & Narrative Angles (32 Curated Formats)

Every episode is produced using one of the 32 niche angle presets defined in [`REGISTRY/Niches/062_computer_pc/ANGLE_PLAN.json`](file:///h:/script-raw-/REGISTRY/Niches/062_computer_pc/ANGLE_PLAN.json):

| # | Angle Slug / Style | Primary Angle Focus | Core Story Question Formulated |
|---|---|---|---|
| 1 | `history_origins` | **How a Personal Computer Model Began** | *Which component, price, software, and distribution choices shaped one early PC?* |
| 2 | `famous_examples` | **A Landmark PC Reexamined** | *What did one celebrated computer make accessible, and to whom?* |
| 3 | `hidden_stories` | **People Behind a PC** | *Whose component, assembly, repair, software, or support work is overlooked?* |
| 4 | `beginner_explainers` | **Inside a PC** | *How do processor, memory, storage, firmware, and peripherals cooperate?* |
| 5 | `advanced_concepts` | **Where Performance Bottlenecks Form** | *Why does one workload strain memory, storage, processor, or cooling?* |
| 6 | `mysteries_unsolved_cases` | **An Unexplained Hardware Failure** | *Which component or compatibility issue explains a documented PC fault?* |
| 7 | `technology_innovation` | **A Component Generation in Use** | *Did one hardware change improve a defined user task?* |
| 8 | `people_personalities` | **A PC Design Decision** | *Who chose a consequential component or platform rule?* |
| 9 | `major_events` | **A PC Platform Shift** | *What changed when one processor, connector, or operating system generation arrived?* |
| 10 | `how_it_works` | **From Power-On to Application** | *How do firmware, hardware, operating system, drivers, and app connect?* |
| 11 | `rise_fall` | **A PC Model's Market Life** | *Why did one machine succeed, decline, or persist?* |
| 12 | `then_vs_now` | **One PC Task Across Eras** | *How did time, energy, cost, and access change for the same task?* |
| 13 | `future_developments` | **A Proposed PC Design** | *What evidence would establish a new architecture's benefit?* |
| 14 | `myths_vs_facts` | **A PC Specification Claim Checked** | *Does a headline processor, memory, or battery claim match observed use?* |
| 15 | `documentary_stories` | **One PC From Launch to Retirement** | *How did a model move through release, updates, repairs, and reuse?* |
| 16 | `system_boundary` | **What Is the PC System?** | *Which behavior depends on board, firmware, operating system, peripheral, or network?* |
| 17 | `input_output_trace` | **A User Action Through Hardware** | *How do input, memory, computation, storage, and display produce one result?* |
| 18 | `design_tradeoff` | **A Portable PC Compromise** | *How did size, battery, performance, cooling, and repairability compete?* |
| 19 | `failure_mode` | **A Documented PC Failure** | *Which conditions contributed to a known defect or reliability issue?* |
| 20 | `testing_limits` | **A Hardware Benchmark's Limits** | *Which tasks and settings did one PC test represent?* |
| 21 | `standards_interoperability` | **PC Components Working Together** | *Did one firmware or connector standard deliver compatible operation?* |
| 22 | `security_threat_model` | **Firmware and Device Trust** | *Which public protections address one PC trust boundary?* |
| 23 | `maintenance_lifecycle` | **Keeping a PC Useful** | *How do updates, parts availability, and repair policy affect service life?* |
| 24 | `infrastructure_dependencies` | **What a PC Needs Beyond the Box** | *Which power, network, account, or software services affect a defined task?* |
| 25 | `accessibility_usability` | **A PC Configuration for More Users** | *Which physical and software choices support different access needs?* |
| 26 | `independent_replication` | **Can a PC Benchmark Be Reproduced?** | *Do independent tests support a maker's performance claim?* |
| 27 | `responsible_deployment` | **A PC Fleet Upgrade** | *How was one hardware change rolled out and supported in an organization?* |
| 28 | `field_software_architecture` | **Software Layers on a PC** | *How did firmware, drivers, OS, and apps divide responsibility on one platform?* |
| 29 | `field_interface_design` | **Ports and Human Controls** | *How did one PC's connectors, keyboard, or settings affect everyday use?* |
| 30 | `field_version_changes` | **A Hardware Revision's Effects** | *What changed between two revisions of one PC model?* |
| 31 | `field_open_standards` | **An Interoperable PC Interface** | *How did a published hardware standard enable or limit component choice?* |
| 32 | `field_technical_debt` | **Legacy Compatibility Costs** | *Which earlier PC platform choice constrained later hardware or software?* |

---

## 3. Topic Catalog (Scratch to Advanced Curriculum)

### Tier 1: Silicon Architecture & Power Delivery
1. **Why Did Intel Fail to Break 4 GHz for 15 Years? The NetBurst Thermal Wall That Changed PC History**
   - *Question:* Why did Intel promise in 2000 that Pentium 4 would reach 10 GHz, only to hit a catastrophic 130-watt thermal meltdown at 3.8 GHz that forced an entire architectural surrender?
   - *Key Focus:* 31-stage NetBurst execution pipeline, pipeline stall penalties, dynamic power dissipation scaling with frequency cubed (P = C*V^2*f), Israeli design team saving Intel with Core 2 Duo (Conroe).
2. **How a CPU Actually Works: From Quartz Crystals and Clocks to Fetch-Decode-Execute**
   - *Question:* How does an electrical pulse from a vibrating quartz crystal coordinate billions of microscopic silicon transistors through the fetch, decode, execute, and writeback cycle 4 billion times a second?
   - *Key Focus:* Program counter, instruction register and control unit decoding micro-ops, arithmetic logic unit (ALU), L1/L2 cache latency differences, branch prediction.
3. **Motherboard VRMs: The 16-Phase Power Station Keeping Your $600 CPU from Burning**
   - *Question:* How does your motherboard cleanly step down 12 volts from the power supply to an ultra-precise 1.25 volts at 250 amperes without boiling its MOSFETs?
   - *Key Focus:* Buck converter topology, high-side and low-side MOSFETs, ferrite chokes and solid capacitors, pulse-width modulation (PWM) multi-phase switching, Vdroop and Load-Line Calibration (LLC).
4. **Thermal Paste vs Liquid Metal: The Microscopic Battle for Heat Transfer**
   - *Question:* Why does a 0.1-millimeter microscopic air gap trap heat like an oven, and how does gallium-indium liquid metal drop temperatures by 15°C while threatening to short-circuit motherboards?
   - *Key Focus:* Surface roughness and microscopic air voids, thermal conductivity ratings (silicone paste 8 W/mK vs liquid metal 73 W/mK), CPU delidding, gallium galvanic corrosion of aluminum heat sinks.
5. **PCIe Lanes and Chipsets: How Data Moves at 64 GB/s Across the Motherboard**
   - *Question:* What is the difference between lanes wired directly to the CPU and lanes routed through the motherboard chipset, and why do high-end NVMe drives share bandwidth with graphics cards?
   - *Key Focus:* Differential signaling and NRZ vs PAM4 encoding in PCIe 5.0/6.0, direct CPU lanes vs DMI chipset multiplexing, slot bifurcation (x16 to x8/x8), latency implications.
### Tier 2: The GPU Revolution & Overclocking
6. **Ray Tracing vs Rasterization: The 30-Year Battle for Photorealistic Gaming Graphics**
   - *Question:* Why did GPUs fake lighting with rasterized tricks for three decades, and how do dedicated RT cores calculate millions of bounding volume hierarchy (BVH) ray bounces in real time?
   - *Key Focus:* Rasterization polygon projection and depth z-buffering, Bounding Volume Hierarchy (BVH) ray traversal, temporal anti-aliasing and AI denoising (DLSS), rendering physical light physics.
7. **x86 vs ARM: Why Apple Silicon M1 Shocked the Entire PC Industry**
   - *Question:* How did a mobile phone chip architecture humiliate 100-watt desktop Intel and AMD processors while using a tiny fan-less battery chassis?
   - *Key Focus:* CISC variable-length decoding legacy overhead vs RISC fixed-length instructions, massive 8-wide decode engines, Unified Memory Architecture (UMA) on-package bandwidth, memory reordering.
8. **Liquid Nitrogen Overclocking: Breaking 9 GHz at -196°C**
   - *Question:* What happens to silicon transistors when cooled to -196°C with bubbling liquid nitrogen, and why do chips suddenly stop working if they get too cold (the Cold Bug)?
   - *Key Focus:* Carrier mobility increase at sub-zero temperatures, condensation insulation with kneaded eraser putty, the silicon 'Cold Bug' and 'Cold Boot Bug', pushing 2.0+ volts into flagship dies.
9. **Nvidia CUDA: The Secret Software Moat That Created a $3 Trillion AI Monopoly**
   - *Question:* How did Jensen Huang spend hundreds of millions in 2006 to add non-gaming compute logic to every GeForce graphics card, laying the foundation for modern ChatGPT and AI dominance?
   - *Key Focus:* General-Purpose computing on GPUs (GPGPU), SIMT (Single Instruction, Multiple Threads) parallel execution, PyTorch and TensorFlow deep integration, why AMD's ROCm struggled to catch up.
10. **GPU Power Transients: Why 450-Watt Graphics Cards Were Tripping 1,000-Watt Power Supplies**
   - *Question:* Why did modern RTX 30 and 40 series graphics cards shut down high-end power supplies in 10 microseconds, and why did new 12VHPWR power cables melt?
   - *Key Focus:* Microsecond transient spikes exceeding 250% TDP, power supply overcurrent protection (OCP) tripping, ATX 3.0 specification revisions, terminal pin contact resistance in 12VHPWR connectors.
### Tier 3: Storage Evolution & Silicon Degradation
11. **The Evolution of Solid State Drives: From 2.5-Inch SATA to PCIe 5.0 Blowtorches**
   - *Question:* How did storage jump from 500 MB/s SATA bottlenecks to 14,000 MB/s NVMe drives, and why do the newest Gen 5 SSDs require active cooling fans?
   - *Key Focus:* AHCI legacy spinning disk queue limits vs NVMe 64,000 deep parallel queues, 3D charge-trap NAND stacking (232+ layers), controller thermal throttling at 80°C.
12. **SLC, MLC, TLC, and QLC: Why Cheaper SSDs Slow Down to Hard Drive Speeds During Large Transfers**
   - *Question:* How does storing 4 bits of data in a single microscopic floating gate require distinguishing between 16 precise voltage levels, and what happens when the fast pseudo-SLC cache fills up?
   - *Key Focus:* Voltage charge drift, write endurance cycles (TBW) collapsing from 10,000 to 300 cycles, SLC caching buffer tricks, sudden drop to 80 MB/s sustained write speeds.
13. **Electromigration: The Invisible Atomic River That Slowly Kills Overclocked CPUs**
   - *Question:* How does a flood of moving electrons physically knock copper atoms down microscopic wire traces until a $500 CPU develops voids, short circuits, and crashes?
   - *Key Focus:* Black's Equation for Mean Time to Failure (MTTF), exponential acceleration by temperature and current density (J^2), the danger of manual fixed high Vcore overclocks.
14. **RAM Sub-Timings: How Tuning 30 Secondary Numbers Gives Free Gaming Performance**
   - *Question:* Why does buying 6000 MHz RAM only give you half its potential performance unless you manually tighten obscure secondary numbers like tRFC and tREFI in BIOS?
   - *Key Focus:* DRAM capacitor refresh cycles, CAS Latency (tCL) vs turnaround timings (tRFC), refreshing capacitor rows before charge drains, 1% low FPS stabilization in gaming.
15. **The Intel 13th and 14th Gen Instability Crisis: Microcode, Oxidation, and Elevated Voltages**
   - *Question:* Why were flagship Core i9 processors crashing in Unreal Engine games and game server farms across the globe throughout 2024?
   - *Key Focus:* Elevated VID microcode requests during idle/low-load states, Vmin shift causing permanent ring bus silicon degradation, manufacturing via oxidation defects, warranty extensions.
### Tier 4: Quantum Chips, Neuromorphic & Optical Buses
16. **Quantum Computing Chips: Qubits Suspended in Gold Cryogenic Chandelier Fridges**
   - *Question:* How do IBM and Google cool niobium-aluminum superconducting chips to 15 millikelvin—colder than deep space—to manipulate quantum superposition and entanglement?
   - *Key Focus:* Transmon qubits and Josephson junctions, microwave pulse quantum logic gates, dilution refrigerators using Helium-3/Helium-4 phase separation, quantum decoherence error rates.
17. **Neuromorphic Chips: Silicon Brains That Process Information with Spiking Neurons**
   - *Question:* Why do traditional computers waste 90% of their power shuttling data between separate CPU and RAM chips, and how do neuromorphic chips merge memory and compute like real brain synapses?
   - *Key Focus:* The Von Neumann bottleneck, Spiking Neural Networks (SNNs), Intel Loihi 2 and IBM TrueNorth chips, memristor analog weight storage, 1,000x energy efficiency for edge AI.
18. **Silicon Photonics: Replacing Copper Traces on Motherboards with Microscopic Laser Beams**
   - *Question:* When copper wires hit an electrical impedance wall at 100 GHz, how will microscopic glass waveguides etched directly into silicon dies transport data at the speed of light?
   - *Key Focus:* Co-Packaged Optics (CPO), micro-ring resonators and optical modulators, eliminating electrical resistance heat loss, TSMC and Intel optical engine roadmaps.
19. **The Death of Moore's Law: 3D Chiplets, Gate-All-Around (GAA), and Backside Power**
   - *Question:* How are engineers keeping transistor scaling alive after hitting the limits of FinFETs by wrapping gates entirely around silicon ribbons and routing power from behind the wafer?
   - *Key Focus:* Gate-All-Around (GAAFET / RibbonFET) nanosheets, Intel PowerVia and TSMC A16 backside power delivery networks, 3D V-Cache vertical silicon stacking, economic packaging costs.
20. **The Personal Computer in 2040: What Replaces the Desktop Tower?**
   - *Question:* Will traditional desktop towers with fans and copper heatsinks exist in 2040, or will computing dissolve into decentralized ambient nodes and high-bandwidth optical wireless displays?
   - *Key Focus:* Diamond wafer substrate thermal dissipation, localized AI accelerator nodes, high-bandwidth wireless mmWave display protocols, the eternal survival of enthusiast modular building.

---

## 4. Flagship Launch Episode
- **Niche ID:** 062 (Computer & PC)
- **Angle Preset:** `beginner_explainers`
- **Episode Title:** *Why Did Intel Fail to Break 4 GHz for 15 Years? The NetBurst Thermal Wall That Changed PC History*
- **Episode Slug:** `062_computer_pc_beginner_explainers_the_netburst_thermal_wall`
- **Duration:** 10 Minutes (600 Seconds / 75 Scenes @ 8s fixed)
- **Execution:** Full Phases 0–5 Autonomous Production Package inside `OUTPUT/062_computer_pc/`.
