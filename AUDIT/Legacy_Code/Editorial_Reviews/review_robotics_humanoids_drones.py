"""Editorial question designs for robotics, humanoid robots, and drones."""

from review_angle_plans import audit, revise_domain


ROBOTICS = """history_origins|A Robot Enters a Workplace|Which task and constraint drove one early robot deployment?|Use dated design, safety, and production records.
famous_examples|A Famous Robot Demonstration Rechecked|Which tasks did it complete outside a staged demonstration?|Compare trials, conditions, and operator assistance.
hidden_stories|Technicians Behind Automation|Who installs, calibrates, repairs, and supervises the system?|Use consented worker accounts and maintenance records.
beginner_explainers|Sense, Plan, Act|How do sensor readings become a robot movement?|Trace one bounded task through control and actuation.
advanced_concepts|Precision Versus Robustness|Can a system handle changed objects and environments?|Measure repeatability across defined conditions.
mysteries_unsolved_cases|An Unexpected Robot Stop|Which sensor, software, power, or human condition explains an incident?|Use logs and public reports without unsafe troubleshooting steps.
technology_innovation|A New Gripper or Sensor|Did it improve a defined task and at what cost?|Compare matched objects, speed, errors, and safety.
people_personalities|A Robot Design Decision|Who set the task and safety requirements?|Trace decisions and affected workers.
major_events|A Robot Deployment Timeline|What happened from pilot to routine use?|Compare acceptance tests with operational outcomes.
how_it_works|A Robot Cell in Operation|How do controller, sensors, actuators, guards, and operator interact?|Map one application and its safe boundaries.
rise_fall|Why a Robot Was Retired|Which performance, maintenance, or task change drove retirement?|Use operating logs and alternatives.
then_vs_now|One Task Across Robot Generations|How did throughput, quality, safety, and labor change?|Compare matched tasks and environments.
future_developments|A Proposed Robot Capability|What test would demonstrate field reliability?|Define task, variation, intervention, and failure threshold.
myths_vs_facts|Autonomous Means No Humans?|Which setup, monitoring, and exception work remains?|Observe a complete workflow.
documentary_stories|A Shift with a Robot|How does one team use and recover the system day to day?|Use consented observation and logs.
system_boundary|What the Robot Controls|Where do machine, fixtures, software, operator, and facility responsibilities end?|Draw one deployed system boundary.
input_output_trace|A Pick-and-Place Cycle|What inputs and outputs shape a single safe cycle?|Trace sensors, decisions, movement, and stop conditions.
design_tradeoff|Speed and Contact Safety|How do performance goals interact with protection measures?|Use applicable standards and tested configuration.
failure_mode|A Failed Grasp|What conditions cause an object to be dropped or damaged?|Review tests and mitigation, not hazardous operating steps.
testing_limits|Lab Task Versus Working Floor|Which changes in lighting, objects, wear, and people alter results?|State trial conditions and sample size.
standards_interoperability|Connecting Robot Components|Which interfaces and safety assumptions must align?|Check versions and integration evidence.
security_threat_model|Trust in Robot Commands|Who can change programs or sensor data?|Map permissions, remote access, and safe failure defensively.
maintenance_lifecycle|Keeping a Robot Accurate|How do calibration, parts, software, and inspection affect performance?|Use service schedules and outcomes.
infrastructure_dependencies|Robot Beyond Its Arm|Which power, network, tooling, and material supply keep it working?|Map single points of failure.
accessibility_usability|An Operator's Control Interface|Can intended workers understand status and intervene?|Test language, reach, sensory access, and training.
independent_replication|Repeating a Robot Benchmark|Can another lab reproduce a capability claim?|Publish robot, firmware, task, fixtures, trials, and failures.
responsible_deployment|Automation and Workers|Who gains or loses tasks, control, and safety?|Compare documented outcomes and worker voice.
field_training_or_control_data|Data Behind Robot Behavior|Which examples or control rules cover the real task?|Check provenance, variation, and out-of-scope cases.
field_real_world_testing|Robot in Its Intended Setting|How does performance change outside the lab?|Measure task success, intervention, and incidents.
field_human_oversight|Who Can Stop the Robot?|What authority and information does a human supervisor have?|Test actual intervention under safe conditions.
field_failure_recovery|Recovering from a Robot Fault|Can work resume without hidden hazards or data loss?|Inspect documented procedure and drill outcomes.
field_hardware_dependency|Hardware Limits Behavior|Which sensors, actuators, batteries, or fixtures constrain claims?|Name versions and measured limits.
"""

HUMANOIDS = """history_origins|Why Give a Robot Human Form?|Which intended task justified one humanoid design?|Use dated research goals and deployment evidence.
famous_examples|A Humanoid Demo Rechecked|What was autonomous, scripted, or remotely assisted?|Review disclosed setup and repeated trials.
hidden_stories|Operators Behind the Humanoid|Who teleoperates, labels data, repairs hardware, and keeps it balanced?|Use consented worker accounts and documentation.
beginner_explainers|Balance and Manipulation|How does a humanoid coordinate sensors, joints, and contact?|Explain one bounded movement and its limits.
advanced_concepts|General-Purpose Claims Tested|How many tasks transfer without rebuilding the setup?|Compare task diversity, interventions, and repeatability.
mysteries_unsolved_cases|A Fall in a Demonstration|Which conditions could explain a documented loss of balance?|Use video limits, telemetry, and operator account.
technology_innovation|A New Humanoid Hand|Does dexterity improve useful work rather than appearance?|Measure objects handled, force, failures, and time.
people_personalities|Choosing the Human Shape|Who argued for that form and which users were consulted?|Trace design records and alternatives.
major_events|A Humanoid Pilot in Practice|What changed between announcement and actual deployment?|Build dated task and safety timeline.
how_it_works|A Humanoid Completes a Task|How do perception, locomotion, grasping, and supervision combine?|Follow one real workflow.
rise_fall|A Humanoid Program Changes Direction|What technical or market evidence drove redesign?|Compare goals, trials, cost, and customer needs.
then_vs_now|Two Humanoid Generations|Did endurance, manipulation, safety, or intervention improve?|Use matched tasks and test conditions.
future_developments|A Humanoid Work Claim|Which field evidence would justify scale-up?|Require task rate, safety, maintenance, and economics.
myths_vs_facts|Human Shape Means Human Ability?|Which physical and cognitive tasks remain unproven?|Separate appearance from measured capabilities.
documentary_stories|One Shift with a Humanoid Pilot|What work did it complete and what did humans rescue?|Use consented observation and full task accounting.
system_boundary|Autonomy Versus Remote Help|Which decisions came from onboard system, cloud, or operator?|Draw control and disclosure boundary.
input_output_trace|A Humanoid Picking an Object|What observations and commands precede a safe grasp?|Trace system states without hazardous directions.
design_tradeoff|Bipedal Form or Stable Base|When does walking justify its energy and stability cost?|Compare a matched task and environment.
failure_mode|A Failed Balance Recovery|How does the system limit harm after a loss of stability?|Use safe trials and protective design evidence.
testing_limits|Demo Choreography Versus Routine Work|Which props, resets, and human interventions change the result?|Request full trial denominator.
standards_interoperability|Humanoid in a Shared Space|Which robot and workplace safety requirements apply?|Identify jurisdiction, task, and integration design.
security_threat_model|Control of a Mobile Humanoid|Who can issue commands or access cameras?|Map identity, update, and privacy boundaries defensively.
maintenance_lifecycle|Wear in a Human-Form Robot|How do joints, batteries, calibration, and software age?|Use service and uptime records.
infrastructure_dependencies|A Humanoid Needs a Workplace|Which floor, power, wireless, tools, and supervision are required?|Map preparation hidden by a demo.
accessibility_usability|Working Beside a Humanoid|Can people predict movement and request help?|Test communication, disability access, and worker control.
independent_replication|Repeat a Humanoid Task Claim|Can another team achieve the result?|Publish setup, hardware, software, trials, interventions, and failures.
responsible_deployment|Humanoid Work and Human Agency|Who controls deployment, surveillance, and job changes?|Consult workers and affected users.
field_training_or_control_data|Data Behind a Humanoid Task|Which human demonstrations or rules shaped behavior?|Check consent, task coverage, and generalization limits.
field_real_world_testing|Humanoid in an Actual Facility|Does it complete tasks under ordinary variation?|Measure uptime, assistance, safety, and throughput.
field_human_oversight|Remote Operator or Supervisor?|What does a human actually control in a claimed autonomous run?|Disclose intervention timing and decision authority.
field_failure_recovery|After a Humanoid Stumbles|Can people and system recover safely?|Review incident protocol and observed drills.
field_hardware_dependency|Body Limits Capability|Which joints, hands, sensors, and battery define the feasible task?|Measure limits on the named model.
"""

DRONES = """history_origins|A Drone Task Takes Flight|Which need and technology made one civilian use feasible?|Use dated operator, regulator, and design records.
famous_examples|A Celebrated Drone Mission Rechecked|What did the aircraft accomplish versus its support crew?|Compare footage, logs, conditions, and ground work.
hidden_stories|The Ground Crew of a Flight|Who plans, checks, observes, maintains, and processes data?|Credit operators and affected communities.
beginner_explainers|What Keeps a Drone Flying?|How do sensors, control, motors, battery, and pilot interact?|Trace a lawful mission at a high level.
advanced_concepts|Payload, Range, and Endurance|How does a useful payload change flight performance?|Use measured trials for a named aircraft.
mysteries_unsolved_cases|A Lost Connection Investigated|Which public evidence explains a documented disruption?|Compare signal, environment, power, and flight logs.
technology_innovation|A New Drone Sensor|Did it improve a defined survey or inspection outcome?|Compare resolution, ground truth, cost, and privacy.
people_personalities|A Drone Operation Decision|Who authorized a mission and consulted those below?|Trace operator, regulator, client, and local voices.
major_events|A Regulatory or Deployment Change|How did one dated decision affect actual flights?|Name jurisdiction, aircraft class, and use.
how_it_works|From Flight Plan to Data Product|What happens between takeoff, sensing, processing, and delivery?|Map one authorized civilian task.
rise_fall|A Drone Service Retired|Which operating, safety, or cost constraint changed viability?|Compare logs and alternatives.
then_vs_now|One Aerial Task Across Platforms|Did drones improve time, quality, cost, or risk?|Match weather, area, crew, and output standard.
future_developments|A Proposed Drone Service|What approvals and field evidence are needed before rollout?|Separate trial, waiver, and general availability.
myths_vs_facts|Autonomous Flight Needs No Pilot?|Which supervision and airspace duties still apply?|Check current local rules and actual operation.
documentary_stories|One Authorized Drone Mission|What happened from briefing to delivered result?|Follow consented operator and community accounts.
system_boundary|Aircraft and Ground System|Which functions rely on pilot, controller, network, and cloud?|Draw command and data paths.
input_output_trace|A Survey Image to Map|Which inputs and processing create a final measurement?|Trace calibration, geolocation, validation, and uncertainty.
design_tradeoff|Flight Time Versus Payload|Which mission outcome improves or degrades with added equipment?|Compare named batteries, aircraft, and conditions.
failure_mode|A Flight Abort|What triggered one documented safe termination?|Use incident report and avoid operational evasion detail.
testing_limits|A Perfect-Weather Trial|What weather, terrain, light, and signal conditions were excluded?|State test envelope and safety margins.
standards_interoperability|Drone in Managed Airspace|Which identification and communication requirements apply?|Name jurisdiction and current aircraft class.
security_threat_model|Trust in Drone Commands and Images|Who can access controls or collected footage?|Map permissions, storage, and defensive safeguards.
maintenance_lifecycle|Keeping an Aircraft Airworthy|How do batteries, propellers, sensors, and software age?|Read inspection records and versioned guidance.
infrastructure_dependencies|Flight Needs More Than Aircraft|Which airspace information, charging, positioning, and data systems matter?|Map mission failure dependencies.
accessibility_usability|An Operator's Ground Control|Can intended pilots understand status and warnings?|Test display, language, sensory access, and workload.
independent_replication|Repeating a Drone Accuracy Claim|Can another crew produce the same result?|Publish platform, sensor, weather, ground truth, and method.
responsible_deployment|Drones Above Communities|Who experiences noise, surveillance, or access effects?|Consult affected residents and document safeguards.
field_training_or_control_data|Data Behind Automated Flight|Which maps or examples inform a flight feature?|Check provenance, coverage, and outdated assumptions.
field_real_world_testing|Drone Under Operational Conditions|Does it perform across expected wind, light, and terrain?|Use authorized field trials and complete failure counts.
field_human_oversight|Pilot Authority During Automation|Can an operator understand and override decisions?|Test lawful intervention and attention demands.
field_failure_recovery|When a Mission Cannot Continue|How is a flight ended and data secured?|Review approved procedures and incident outcomes.
field_hardware_dependency|Aircraft and Payload Limits|Which battery, sensor, link, and structure constrain a claim?|Name model, configuration, and measured envelope.
"""


if __name__ == "__main__":
    revise_domain("330", "330_robotics", ROBOTICS,
                  "Robotics as task-specific sensing, control, physical action, integration, maintenance, safety, and work outcomes.",
                  "NIST robot test methods, applicable standards, dated design and service records, controlled trials, and consented worker accounts",
                  "Name robot, task, environment, software and hardware versions, and trial count. Separate demonstrations from routine performance and use safe, authorized tests.")
    revise_domain("331", "331_humanoid_robots", HUMANOIDS,
                  "Humanoid robots as human-form machines whose locomotion, manipulation, autonomy, supervision, safety, and operating cost require separate evidence.",
                  "dated product specifications, disclosed demos, independent task trials, safety documentation, maintenance records, and worker accounts",
                  "Name model, task, setting, version, and human intervention. Distinguish visual resemblance from general capability and disclose teleoperation.")
    revise_domain("332", "332_drones", DRONES,
                  "Drones as aircraft systems used for defined civilian tasks with pilots, airspace rules, payloads, data processing, and community effects.",
                  "current aviation authority guidance, aircraft specifications, authorized flight records, field measurements, and consented local accounts",
                  "Name jurisdiction, aircraft class, operation, date, and authorization. Verify current local rules; avoid flight or restriction-evasion instructions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
