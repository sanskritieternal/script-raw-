"""Editorial questions for software programming and personal computers."""

from review_angle_plans import audit, revise_domain


SOFTWARE = """history_origins|How a Software Practice Emerged|Which problem led to one programming language, tool, or method?|Trace dated design notes, code, release records, and competing approaches.
famous_examples|A Famous Program Reexamined|What did one influential program actually make possible?|Compare original version, platform, user tasks, and later claims.
hidden_stories|The Maintainers Behind the Release|Whose testing, documentation, localization, or maintenance work is overlooked?|Use credits, issue records, commits, and attributed accounts.
beginner_explainers|What a Program Does|How does one small program turn an input into an output?|Trace a reproducible example and explain each transformation.
advanced_concepts|Correctness Under Real Conditions|Which assumptions make one algorithm or system correct?|State inputs, invariants, failure cases, complexity, and test limits.
mysteries_unsolved_cases|A Bug With Multiple Causes|Which evidence distinguishes competing explanations for one documented failure?|Use issue history, logs, versions, reproductions, and fixes without exploit steps.
technology_innovation|A New Programming Tool in Use|Did one compiler, framework, or tool improve a measured outcome?|Compare like-for-like workloads, developer effort, reliability, and migration cost.
people_personalities|A Design Decision's Authors|Who proposed and challenged one consequential software choice?|Read design discussion, code review, and dated release decisions.
major_events|A Release Changes the Ecosystem|What changed for users and maintainers after one major software release?|Compare adoption, compatibility, performance, and reported defects.
how_it_works|From Source to Running Program|What roles do source code, build, dependencies, runtime, and operating system play?|Use one pinned version and a reproducible public example.
rise_fall|A Software Project's Trajectory|Why did one project grow, fork, decline, or end?|Compare maintainers, funding, compatibility, users, and documented decisions.
then_vs_now|One Programming Task Across Eras|How did tools and constraints change for a defined task?|Compare equivalent functionality, hardware, reliability, and developer time.
future_developments|A Proposed Software Direction|What evidence would justify adopting one planned language or platform change?|Specify compatibility, migration, security, performance, and user impact.
myths_vs_facts|Testing a Programming Slogan|Does a popular claim about speed, safety, or simplicity hold for a defined task?|Compare pinned versions, workloads, measurement methods, and exceptions.
documentary_stories|One Bug From Report to Fix|How did a documented issue move through triage, reproduction, patch, and release?|Build a dated public timeline without exploit-enabling detail.
system_boundary|Where the Program Ends|Which behavior belongs to application, library, operating system, and external service?|Map interfaces and ownership for one deployed version.
input_output_trace|Tracing One Request|How does one input become an output through a defined software path?|Use safe sample data, public architecture, and measured checkpoints.
design_tradeoff|A Software Architecture Choice|What did one design gain in speed, safety, simplicity, or flexibility?|Compare original requirements, benchmarks, maintenance, and alternatives.
failure_mode|When a Software Assumption Failed|Which documented condition caused one user-visible failure?|Use public postmortem and observed impact; omit exploitable procedure.
testing_limits|What the Test Suite Missed|Which conditions were covered and which escaped before one release?|Compare test plan, environment, defect report, and later regression checks.
standards_interoperability|Software Meets an Open Format|Did one implementation interoperate with independent products?|Use versioned specifications and conformance or cross-product tests.
security_threat_model|A Software Security Boundary|What assets and trust assumptions did one public design address?|Discuss high-level controls and published findings without attack instructions.
maintenance_lifecycle|Who Maintains a Dependency?|How did updates, support windows, and compatibility shape one product?|Read release policy, advisories, and migration records by date.
infrastructure_dependencies|Services Behind an App|Which hosting, identity, network, or data systems affect one feature?|Use public dependency and incident records without exposing live weak points.
accessibility_usability|A Feature for More Users|Did one interface work for people with different access needs?|Compare accessibility criteria with testing by affected users.
independent_replication|Reproducing a Performance Claim|Can a published benchmark be rerun fairly?|Pin source, compiler, hardware, dataset, flags, and measurement method.
responsible_deployment|Releasing a Change Safely|What staged rollout and monitoring accompanied one software change?|Compare release plan, user impact, rollback criteria, and actual outcomes.
field_software_architecture|A Module Boundary Under Review|How did one architectural split affect changeability and reliability?|Compare dependencies, interface contracts, defect history, and maintenance effort.
field_interface_design|An API or UI Decision|How did one interface choice affect errors and user work?|Read specification, usability evidence, and breaking-change history.
field_version_changes|What Changed Between Releases?|Which behavior changed in one version and who was affected?|Use release notes, code diff, migration guide, and reproducible checks.
field_open_standards|An Open Standard in Practice|Did independent implementations agree on one standard's behavior?|Name standard version and compare conformance and interoperability tests.
field_technical_debt|The Cost of an Earlier Shortcut|Which documented design shortcut later slowed or broke development?|Trace issue and change history with estimates separated from measurements."""


PC = """history_origins|How a Personal Computer Model Began|Which component, price, software, and distribution choices shaped one early PC?|Compare dated manuals, advertisements, engineering records, and user accounts.
famous_examples|A Landmark PC Reexamined|What did one celebrated computer make accessible, and to whom?|Compare launch configuration, price, software, sales, and user evidence.
hidden_stories|People Behind a PC|Whose component, assembly, repair, software, or support work is overlooked?|Use credits, service documents, worker records, and attributed accounts.
beginner_explainers|Inside a PC|How do processor, memory, storage, firmware, and peripherals cooperate?|Trace one ordinary task on a named configuration without repair instructions.
advanced_concepts|Where Performance Bottlenecks Form|Why does one workload strain memory, storage, processor, or cooling?|Compare measurements on a defined PC and workload with uncertainty.
mysteries_unsolved_cases|An Unexplained Hardware Failure|Which component or compatibility issue explains a documented PC fault?|Use official diagnostics, service notices, and controlled tests without unsafe procedures.
technology_innovation|A Component Generation in Use|Did one hardware change improve a defined user task?|Compare compatible systems, power, cost, reliability, and measured performance.
people_personalities|A PC Design Decision|Who chose a consequential component or platform rule?|Read dated design, procurement, and developer accounts.
major_events|A PC Platform Shift|What changed when one processor, connector, or operating system generation arrived?|Trace compatibility, pricing, software, service, and user adoption.
how_it_works|From Power-On to Application|How do firmware, hardware, operating system, drivers, and app connect?|Map public interface roles for a named platform, without bypass instructions.
rise_fall|A PC Model's Market Life|Why did one machine succeed, decline, or persist?|Compare price, software, distribution, repairability, rivals, and dates.
then_vs_now|One PC Task Across Eras|How did time, energy, cost, and access change for the same task?|Define workload and compare period-appropriate systems fairly.
future_developments|A Proposed PC Design|What evidence would establish a new architecture's benefit?|Specify workloads, compatibility, support, energy, repairability, and cost.
myths_vs_facts|A PC Specification Claim Checked|Does a headline processor, memory, or battery claim match observed use?|Match configuration, test settings, workload, and measurement method.
documentary_stories|One PC From Launch to Retirement|How did a model move through release, updates, repairs, and reuse?|Build a dated timeline from manuals, advisories, reviews, and owner accounts.
system_boundary|What Is the PC System?|Which behavior depends on board, firmware, operating system, peripheral, or network?|Define a named configuration and map public interfaces.
input_output_trace|A User Action Through Hardware|How do input, memory, computation, storage, and display produce one result?|Trace a safe illustrative task on a documented configuration.
design_tradeoff|A Portable PC Compromise|How did size, battery, performance, cooling, and repairability compete?|Compare design data and measured outcomes for one model.
failure_mode|A Documented PC Failure|Which conditions contributed to a known defect or reliability issue?|Use service and test records, avoiding hazardous troubleshooting steps.
testing_limits|A Hardware Benchmark's Limits|Which tasks and settings did one PC test represent?|Inspect sample size, configuration, firmware, thermal state, and workload.
standards_interoperability|PC Components Working Together|Did one firmware or connector standard deliver compatible operation?|Name version and compare conformance and independent device tests.
security_threat_model|Firmware and Device Trust|Which public protections address one PC trust boundary?|Discuss model and validation at high level without bypass or attack detail.
maintenance_lifecycle|Keeping a PC Useful|How do updates, parts availability, and repair policy affect service life?|Compare vendor support, repair records, costs, and reuse options.
infrastructure_dependencies|What a PC Needs Beyond the Box|Which power, network, account, or software services affect a defined task?|Map dependencies and outage evidence without live weak-point detail.
accessibility_usability|A PC Configuration for More Users|Which physical and software choices support different access needs?|Check device compatibility, input options, settings, and user testing.
independent_replication|Can a PC Benchmark Be Reproduced?|Do independent tests support a maker's performance claim?|Match model, memory, firmware, power mode, workload, and thermal conditions.
responsible_deployment|A PC Fleet Upgrade|How was one hardware change rolled out and supported in an organization?|Compare procurement, compatibility tests, training, repair, and e-waste outcomes.
field_software_architecture|Software Layers on a PC|How did firmware, drivers, OS, and apps divide responsibility on one platform?|Map versioned interfaces and observed compatibility consequences.
field_interface_design|Ports and Human Controls|How did one PC's connectors, keyboard, or settings affect everyday use?|Compare design requirements, accessibility, compatibility, and user evidence.
field_version_changes|A Hardware Revision's Effects|What changed between two revisions of one PC model?|Use service manuals, part numbers, firmware notes, and matched tests.
field_open_standards|An Interoperable PC Interface|How did a published hardware standard enable or limit component choice?|Compare specification version with independent device tests.
field_technical_debt|Legacy Compatibility Costs|Which earlier PC platform choice constrained later hardware or software?|Trace standards, support decisions, user dependence, and migration cost."""


if __name__ == "__main__":
    revise_domain("061", "061_software_programming", SOFTWARE,
                  "Software and programming through versioned design, code, tests, standards, maintenance, user impact, and reproducible claims.",
                  "versioned source code and design discussions, official specifications and release records, reproducible tests and benchmarks, public incident reports, and user and maintainer accounts",
                  "Name product, version, platform, and workload. Reproduce measurements under stated conditions, check current advisories, and omit exploitable security procedures and private user data.")
    revise_domain("062", "062_computer_pc", PC,
                  "Personal computers through hardware generations, firmware and software interfaces, performance, access, repair, support, and service life.",
                  "dated computer manuals and component specifications, firmware and interface standards, matched performance and power tests, service and support records, and owner and worker accounts",
                  "Name exact model, revision, configuration, workload, and date. Separate maker specifications from measured behavior; avoid unsafe repair or security bypass instructions and verify current support status.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
