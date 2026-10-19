"""Niche-specific editorial questions for programming, software engineering, and cybersecurity."""

from review_angle_plans import audit, revise_domain


PROGRAMMING = """history_origins|A Language Feature's Origin|What problem did a named language feature originally solve?|Use dated proposals, specifications, and early programs.
famous_examples|A Program Reconsidered|Why is one example taught so often and what does it omit?|Run it with a named language version and examine its limits.
hidden_stories|The Maintainers Behind a Library|Who reviews changes, answers issues, and keeps compatibility?|Use public project records and attributed accounts.
beginner_explainers|A Program from Input to Output|How does a short program transform one input?|Trace variables, control flow, errors, and output.
advanced_concepts|What an Abstraction Costs|When does a useful abstraction add time, memory, or complexity?|Compare equivalent programs on a bounded task.
mysteries_unsolved_cases|A Bug That Appears Only Sometimes|Which runtime conditions explain a documented intermittent error?|Reproduce safely with version, input, and environment.
technology_innovation|A New Language Feature Tested|Did it improve a particular programming task?|Compare readability, correctness, compatibility, and runtime.
people_personalities|A Language Design Debate|Who argued for competing semantics and why?|Read dated proposals and decisions, credit contributors.
major_events|A Breaking Language Release|Which programs changed behavior after one release?|Test documented examples across exact versions.
how_it_works|Parsing to Execution|What happens between source text and a result?|Trace parser, representation, runtime, and system calls for one implementation.
rise_fall|Why a Language Gained Users|Which tasks, tools, institutions, and measures explain adoption?|Separate surveys, code counts, and real use.
then_vs_now|One Task Across Versions|How did syntax, safety, and performance change?|Use matched code and versioned documentation.
future_developments|A Proposed Language Change|What compatibility and implementation questions remain?|Distinguish proposal from accepted specification and deployed compiler.
myths_vs_facts|Shorter Code Is Better?|When does brevity help or hide a defect?|Compare comprehension and tests for a defined audience.
documentary_stories|A Bug Fix from Report to Release|How did a real issue become a tested change?|Follow issue, patch, review, release, and user impact.
system_boundary|Where Code Meets Its Environment|Which behavior comes from language, library, OS, or service?|Name implementation and version for one program.
input_output_trace|A Function's Actual Contract|What inputs, exceptions, side effects, and outputs does it have?|Use tests and documentation on one version.
design_tradeoff|Mutable or Immutable State|How do two designs affect clarity, performance, and mistakes?|Compare matched tasks and measured outcomes.
failure_mode|An Error Path Nobody Tested|What input exposed a failure and how was it handled?|Use a harmless reproduction and avoid exploit instructions.
testing_limits|Passing Tests and Missing Bugs|Which cases remain outside a program's test suite?|Inspect boundaries, properties, platforms, and dependencies.
standards_interoperability|Code Across Implementations|Which specified behavior is portable and which is implementation-specific?|Run conformance examples across named versions.
security_threat_model|Trusting Program Input|What can an untrusted input influence?|Trace validation, parsing, permissions, and safe failure without payloads.
maintenance_lifecycle|Keeping Code Usable|How do dependencies, deprecations, and documentation affect maintenance?|Follow one project and its release policy.
infrastructure_dependencies|A Program Needs a Runtime|Which compiler, package source, OS, and service must work?|Map dependencies and outage effects.
accessibility_usability|Programming Tools for Learners|Can intended users understand errors and navigate an editor?|Test documentation, language support, and assistive tools.
independent_replication|Reproducing a Code Claim|Can another developer obtain the same output?|Publish code, inputs, versions, environment, and test command.
responsible_deployment|When Code Reaches Users|Who may be harmed by an untested assumption?|Check privacy, accessibility, error handling, and rollback.
field_software_architecture|Modules Around One Task|How are responsibilities divided among functions and packages?|Draw calls and data flow for a bounded program.
field_interface_design|A Developer API's Clarity|Can a caller infer valid input and failure behavior?|Test naming, types, examples, and errors.
field_version_changes|A Dependency Update|Which behavior changed and which callers must adapt?|Read changelog and run focused regression tests.
field_open_standards|A Portable Language Claim|Does a public specification enable independent implementations?|Check conformance and platform differences.
field_technical_debt|A Workaround That Stayed|Which earlier constraint created a fragile code path?|Trace issue history, current cost, and migration tests.
"""

ENGINEERING = """history_origins|A Software Process Emerges|Which project problem prompted one engineering practice?|Use dated reports and distinguish origin from later adoption.
famous_examples|A Project Postmortem Rechecked|What does one celebrated success or failure actually show?|Compare stated goals, delivery evidence, and user outcomes.
hidden_stories|Invisible Engineering Work|Who maintains tests, documentation, operations, and accessibility?|Use team records and consented accounts.
beginner_explainers|From Requirement to Release|How does a user need become a shipped change?|Trace requirement, design, code, test, deployment, and feedback.
advanced_concepts|Reliability as a Measured Property|Which design and operating choices support a target level?|Define service, failure, time window, and measurement.
mysteries_unsolved_cases|A Regression That Escaped Review|Which assumption let a fault reach users?|Use issue timeline and safe reproduction evidence.
technology_innovation|A New Engineering Tool|Did one tool shorten feedback or improve defect discovery?|Compare matched teams, tasks, and costs.
people_personalities|A Design Decision in Context|Who had authority and whose needs were represented?|Review design records and stakeholder feedback.
major_events|A Release and Rollback|What triggered rollback and how was impact limited?|Use dated deployment, monitoring, and incident records.
how_it_works|A Change Through a Pipeline|Which checks run before and after deployment?|Trace source, review, build, tests, artifact, and monitoring.
rise_fall|Why a Development Method Spread|What problems did adopters seek to solve?|Separate marketing, measured outcomes, and context.
then_vs_now|One Team Before and After a Practice|Did delivery quality and workload change?|Match release size, team, users, and measurement period.
future_developments|An Engineering Practice Proposal|What evidence would justify adoption?|Specify expected outcome, costs, trial, and stop criteria.
myths_vs_facts|More Tests Mean Quality?|Which defects can tests detect and which needs require user evidence?|Check coverage, assertions, environments, and acceptance.
documentary_stories|An Incident and Its Fix|How did a team learn from a production failure?|Follow detection, response, root-cause evidence, and follow-up.
system_boundary|Who Owns a Software Outcome?|Where do product, development, operations, vendor, and users intersect?|Map responsibilities for one service.
input_output_trace|A Requirement to Observable Behavior|What evidence shows a promised feature works?|Link acceptance criterion, test, telemetry, and user task.
design_tradeoff|Speed of Delivery Versus Change Risk|How do batch size and review affect outcomes?|Compare matched releases and failure rates.
failure_mode|A Dependency Change Breaks Service|Why did checks miss an incompatible version?|Trace lockfile, build, staging, and recovery.
testing_limits|What Staging Cannot Prove|Which production load or user condition is absent?|List test assumptions and monitoring safeguards.
standards_interoperability|An API Contract Across Teams|Which schema and version promises allow integration?|Run consumer and provider tests.
security_threat_model|Security in the Delivery Chain|Who can modify source, builds, dependencies, or releases?|Use a bounded threat model and defensive controls.
maintenance_lifecycle|Support After Launch|How are bugs, updates, end-of-life, and ownership handled?|Read service policy and observed backlog.
infrastructure_dependencies|Software Needs Operations|Which registry, build service, network, and runtime can block delivery?|Map failure and recovery dependencies.
accessibility_usability|A Feature's Real Acceptance|Can intended users complete the task with assistive tools?|Test representative flows and document barriers.
independent_replication|Repeating an Engineering Metric|Can another analyst derive the reported delivery measure?|Publish definitions, time window, exclusions, and raw events.
responsible_deployment|Shipping with Consequences|Who is affected by a change and what rollback exists?|Check privacy, access, support, and staged rollout.
field_software_architecture|A Service's Component Boundaries|Which modules and dependencies explain behavior?|Draw actual data flow and failure ownership.
field_interface_design|A Product Flow Under Test|Where do users misunderstand or abandon a task?|Use observed sessions and accessible prototypes.
field_version_changes|Compatibility During Migration|Which clients and data formats must continue to work?|Test old and new versions with rollback plan.
field_open_standards|Standards in a Product|Does conformance enable another system to connect?|Check spec version, optional features, and integration test.
field_technical_debt|Debt with a Measured Cost|Which shortcut now slows changes or increases incidents?|Trace original decision, impact, and proposed remediation.
"""

CYBERSECURITY = """history_origins|A Security Practice Takes Shape|Which documented incident or need changed one defensive practice?|Use dated standards and incident records.
famous_examples|A Widely Cited Breach Revisited|Which failures are supported by public evidence?|Separate investigation findings from speculation.
hidden_stories|Security Work After Headlines|Who restores service, supports victims, and fixes controls?|Use public records and consented accounts.
beginner_explainers|What a Security Control Protects|What asset and failure does one control address?|Define threat, user, boundary, and expected outcome.
advanced_concepts|Defense in Depth Tested|Do multiple controls fail independently in a defined scenario?|Map dependencies and validation evidence.
mysteries_unsolved_cases|An Incident's Unknown Cause|Which facts are established and what remains uncertain?|Compare official timeline, logs, and plausible alternatives.
technology_innovation|A New Defensive Product|Did it reduce a defined risk without unacceptable costs?|Compare detection quality, false alarms, coverage, and operations.
people_personalities|A Risk Decision|Who accepted a residual risk and with what information?|Trace governance records and affected groups.
major_events|A Public Incident Timeline|What happened from detection through recovery?|Use dated notices and postmortem; avoid operational attack steps.
how_it_works|From Alert to Response|How does a team validate and triage a signal?|Describe roles, evidence preservation, and escalation at a safe level.
rise_fall|Changing Threat Reports|Is an apparent increase a change in attacks or reporting?|Check definitions, detection, population, and time window.
then_vs_now|A Control Before and After Deployment|Did exposure and response improve?|Match assets, measurement, and threat context.
future_developments|An Emerging Security Claim|What evidence would show a proposed defense works?|Define adversary capability, deployment limits, and independent test.
myths_vs_facts|One Tool Makes a System Secure?|Which risks lie outside a tool's scope?|Map assets, people, process, and dependencies.
documentary_stories|Recovery After an Incident|How did an organization restore trusted service?|Use public timeline, impacted users, and documented lessons.
system_boundary|Who Secures a Shared Service?|Which duties belong to provider, customer, vendor, and user?|Use named architecture and contractual responsibility.
input_output_trace|A Security Alert's Evidence|What data triggers an alert and what does it actually prove?|Trace logging, detection rule, context, and false positives.
design_tradeoff|Stronger Control and User Friction|How does a control affect security and access?|Test intended users, bypass pressure, and recovery.
failure_mode|A Defensive Control Fails|Why did a control miss or misclassify an event?|Analyze public incident and avoid reproduction instructions.
testing_limits|What a Security Exercise Misses|Which actors or conditions were outside the test?|State scope, authorization, environment, and uncertainty.
standards_interoperability|Security Controls Across Vendors|Which protocol and version details permit safe integration?|Check published standards and conformance evidence.
security_threat_model|A Named Threat Model|Which assets, trust boundaries, and adversary capabilities matter?|Use defensive modeling without actionable intrusion detail.
maintenance_lifecycle|Patching as a Process|How are assets found, fixes tested, and exceptions tracked?|Use dated policy and measured remediation evidence.
infrastructure_dependencies|Security's Shared Dependencies|Which identity, logging, backups, and network services must survive?|Map correlated failure and recovery.
accessibility_usability|Security for Every User|Can users authenticate and recover access with disabilities or limited connectivity?|Test options, support, and real completion rates.
independent_replication|Checking a Risk Reduction Claim|Can another analyst repeat the measure?|Publish scope, detection definitions, baseline, and limits.
responsible_deployment|A Control's Human Effects|Who bears monitoring, exclusion, or error costs?|Assess privacy, redress, accessibility, and governance.
field_attack_surface|A Service's Exposed Boundaries|Which public interfaces and dependencies need defensive review?|Inventory assets and trust boundaries without exploit detail.
field_data_protection|A Sensitive Record's Path|Where is data collected, stored, shared, and deleted?|Trace authorized access, encryption boundaries, and retention.
field_incident_response|A Response Plan Under Test|Can a team detect, contain, communicate, and recover from a bounded event?|Use an authorized exercise and record gaps without attack recipes.
field_identity_controls|Identity and Privilege|Which roles can perform a consequential action?|Review authentication, authorization, recovery, and audit evidence.
field_security_usability|A Safe Action Users Can Complete|Does a security control work for intended users?|Test comprehension, accessibility, support, and false-alarm burden.
"""


if __name__ == "__main__":
    revise_domain("324", "324_programming", PROGRAMMING,
                  "Programming as the act of specifying executable behavior, debugging, reasoning about code, and maintaining language and library compatibility.",
                  "language specifications and proposals, versioned documentation, source and issue histories, reproducible programs, and tests",
                  "Name language, implementation, version, input, and environment. Distinguish specification from implementation and avoid exposing production data.")
    revise_domain("325", "325_software_engineering", ENGINEERING,
                  "Software engineering as requirements, design, delivery, testing, operations, maintenance, and user outcomes across a software lifecycle.",
                  "project requirements and design records, versioned artifacts, test and deployment data, incident reports, and user research",
                  "Name system, team context, time period, and metric definition. Do not infer causality from a single project or a passing test suite.")
    revise_domain("326", "326_cybersecurity", CYBERSECURITY,
                  "Cybersecurity as governance and management of defined risks across assets, prevention, detection, response, recovery, and affected users.",
                  "NIST frameworks, public incident reports, system inventories, control tests, measurements, and consented user accounts",
                  "Describe defenses and evidence at a safe level. Do not provide operational intrusion instructions or treat a framework as proof of security.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
