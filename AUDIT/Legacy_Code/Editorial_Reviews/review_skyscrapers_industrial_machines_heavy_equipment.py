"""Editorial question designs for tall buildings and industrial equipment."""

from review_angle_plans import audit, revise_domain


SKYSCRAPERS = """history_origins|Why Build High Here?|Which land, technology, and planning constraints shaped one tower?|Use dated plans, land records, and building rules.
famous_examples|A Famous Tower Reexamined|What did its structural and circulation design actually achieve?|Specify building version and occupancy period.
hidden_stories|Workers behind the Skyline|Whose construction, cleaning, and maintenance work is overlooked?|Use contracts, site records, and worker accounts.
beginner_explainers|How a Tall Building Stands|How do loads travel through floors, frame, and foundations?|Use one documented structural scheme.
advanced_concepts|Wind and Occupant Comfort|How do wind forces and motion limits shape a tall tower?|Compare wind study, structural model, and monitoring.
mysteries_unsolved_cases|A Tower Defect under Review|Which evidence could distinguish design, material, and upkeep causes?|Separate inspection findings from explanation.
technology_innovation|A New Structural System|Which measurable problem did a tower innovation solve?|Compare alternatives and built performance.
people_personalities|Designers and Decision Makers|Who chose a tower's form, systems, and budget?|Use dated drawings and team credit.
major_events|A Tower Opens|Did delivered occupancy and services match the original plan?|Compare approval, completion, and use data.
how_it_works|Vertical City Systems|How do lifts, stairs, water, power, and fire systems interact?|Trace one building's service scheme.
rise_fall|A Tower Changes Use|Which market, code, or maintenance forces drove conversion?|Compare original and later approved plans.
then_vs_now|A Tower through Renovation|What changed in façade, systems, access, and energy use?|Use dated baselines and metered results.
future_developments|A Proposed Super-Tall Tower|Which design, finance, and evacuation evidence remains needed?|Treat renderings and forecasts as conditional.
myths_vs_facts|Tallest by Which Measure?|How does the ranking change with height definition?|State occupied floor, architectural top, and date.
documentary_stories|A Tower from Permit to Use|Which site and approval decisions changed the built project?|Trace change orders and occupancy records.
system_boundary|Building or District?|Which transport, energy, and land impacts extend beyond the tower?|Define site and time boundary.
input_output_trace|Occupant to Safe Exit|How do alarm, stairs, lifts, and management interact?|Use approved egress design and drill evidence.
design_tradeoff|Height, Floor Area, and Structure|What was lost or gained by adding floors?|Compare core ratio, loads, cost, and access.
failure_mode|A Documented Building-System Failure|Which subsystem failed and how did occupants respond?|Use official investigation and maintenance record.
testing_limits|Wind-Tunnel to Occupied Tower|Which modeled effects need post-occupancy measurement?|Compare test configuration and actual motion.
standards_interoperability|Codes Governing a Tower|Which adopted structural, fire, and accessibility rules applied?|Name jurisdiction, permit date, and building use.
security_threat_model|Continuity of Building Services|Which public planning controls address loss of power or access?|Keep discussion at resilience and governance level.
maintenance_lifecycle|Façade and Systems over Time|Which inspections reveal repair needs?|Trace dated components, defects, and remedies.
infrastructure_dependencies|Tower and City Utilities|Which power, water, sewer, and transit limits shape operation?|Use capacity and service records.
accessibility_usability|Navigating a High-Rise|Can varied users enter, circulate, and evacuate under the approved plan?|Check actual lift, refuge, and route conditions.
independent_replication|Recheck an Energy Claim|Can another analyst reproduce a tower efficiency figure?|Match occupied area, weather, use, and meter boundary.
responsible_deployment|Handover of a Tall Building|What commissioning and training happened before occupancy?|Use test reports and operator records.
field_route_capacity|People Reaching a Tower|Can streets, transit, and entrances serve peak use?|Model arrivals, queues, and accessible routes.
field_vehicle_design|Service Vehicles and Loading|Which deliveries and emergency vehicles fit the site?|Use approved access plan and actual constraints.
field_maintenance_system|Keeping a Tower Operable|Are parts, access equipment, and staff available for critical systems?|Check owner records and redundancy.
field_safety_case|Evidence for Occupancy|Which inspections, approvals, and drills support a bounded claim?|Distinguish code approval from risk-free use.
field_construction_impact|Building Upward|Which materials, energy, noise, and neighborhood changes were measured?|Compare assessment with construction monitoring.
"""

MACHINES = """history_origins|A Machine Enters Production|Which task and labor conditions led to one machine design?|Trace patents, factory records, and early tests.
famous_examples|A Defining Industrial Machine|What output and constraints made a model influential?|Use dated specifications and factory data.
hidden_stories|Operators and Maintainers|Which workers' adaptations made a machine productive?|Use documented practice and attributed testimony.
beginner_explainers|Input, Motion, and Output|How does one machine transform material or energy?|Follow a specific production cycle.
advanced_concepts|Precision under Wear|How do tolerances, heat, and wear affect repeatability?|Use calibration and inspection data.
mysteries_unsolved_cases|An Intermittent Machine Fault|Which logs could distinguish sensor, drive, and material causes?|Separate observed symptoms from diagnosis.
technology_innovation|An Automation Upgrade|Did throughput rise without increasing rejects or hazards?|Compare matched runs and workforce impact.
people_personalities|An Inventor and the Shop Floor|Who proposed, tested, and modified one mechanism?|Use dated designs and team records.
major_events|A Machine Incident|What did an official investigation identify and change?|Trace finding, remedy, and later monitoring.
how_it_works|One Production Cell|How do feed, operation, inspection, and unload connect?|Map one machine and operator workflow.
rise_fall|A Machine Type Retired|Which energy, cost, quality, or safety factors explain replacement?|Compare actual factory use.
then_vs_now|Two Generations of Machines|Which productivity measures are comparable?|Align product, quality threshold, labor, and downtime.
future_developments|A Proposed Machine Feature|What prototype and production tests would support adoption?|Define reliability, safety, and maintenance gates.
myths_vs_facts|Automation Means No Labor?|Which setup, supervision, and repair tasks remain?|Observe one actual shift and records.
documentary_stories|Prototype to Factory Floor|How did tests alter a machine before routine use?|Follow drawings, trials, and commissioning.
system_boundary|Machine or Production Line?|Which throughput depends on supply, inspection, and downstream steps?|Define bottleneck and denominator.
input_output_trace|Signal to Tool Motion|How do controller, drive, transmission, and tool respond?|Use a bounded mode and measured timing.
design_tradeoff|Speed and Precision|What quality or wear cost followed higher cycle rate?|Compare matched inputs and inspection outcomes.
failure_mode|A Guard or Interlock Event|What sequence did inspection establish?|Use official record and avoid bypass instructions.
testing_limits|Bench Test versus Production|Which loads, materials, or shifts reveal new failures?|Compare trial and service data.
standards_interoperability|Machine and Factory Interface|Which guarding, electrical, and data requirements apply?|Name machine version, site, and rule edition.
security_threat_model|Machine Control Access|Which authenticated service path could alter operation?|Bound version and documented controls without exploit details.
maintenance_lifecycle|Wear Part over Time|Which inspections and failure data determine replacement?|Use service history and production load.
infrastructure_dependencies|Machine and Factory Utilities|Which power, air, coolant, or network service is essential?|Map downtime and backups.
accessibility_usability|Operator at the Machine|Can varied workers reach, read, and control it?|Use ergonomic assessment and user observation.
independent_replication|Recheck a Throughput Claim|Can an independent team reproduce units per hour?|Match product mix, rejects, setup, and stoppages.
responsible_deployment|Commissioning a Machine|What training, guarding, and validation precede use?|Use site acceptance records and worker feedback.
field_prototype_testing|Prototype under Real Load|Which duty cycle exposes a claimed improvement?|Specify materials, duration, and failure criteria.
field_design_tolerance|Tolerance Stack|Which component variation reaches the final product?|Use drawings and measured distributions.
field_manufacturing_method|How the Machine Is Made|Which fabrication method determines alignment and durability?|Trace process and inspection evidence.
field_failure_investigation|A Failed Component|What physical and maintenance evidence identifies cause?|Keep hypothesis separate from finding.
field_repair_path|Returning to Service|Which approved repair and test restore performance?|Use maintenance records, not procedural instructions.
"""

EQUIPMENT = """history_origins|A Machine for Heavy Work|Which site problem prompted one equipment type?|Use early design and project records.
famous_examples|A Workhorse Machine Examined|What measurable work can a named model perform?|State attachment, ground, load, and duty cycle.
hidden_stories|Operators and Ground Crews|Whose coordination is missing from productivity claims?|Use site logs and worker accounts.
beginner_explainers|How Heavy Equipment Moves Work|How do engine, hydraulics, attachment, and ground interact?|Follow one defined task.
advanced_concepts|Stability on Real Ground|How do slope, load, reach, and surface change safe limits?|Use rated charts and site assessment.
mysteries_unsolved_cases|Unexpected Machine Downtime|Which diagnostic and site records could separate causes?|Compare fault codes with inspection.
technology_innovation|Visibility or Control Aid|Did a new aid change blind-area risk or workflow?|Use field observations and controlled comparison.
people_personalities|A Machine Design Choice|Who specified a feature and which site need did it answer?|Use design and operator feedback.
major_events|A Site Equipment Incident|Which factors did official review establish?|Trace equipment, ground, traffic plan, and remedy.
how_it_works|One Earthmoving Cycle|How do loading, travel, dumping, and return determine output?|Measure cycle and queue times.
rise_fall|A Machine Fleet Replaced|Which uptime, fuel, labor, or safety evidence drove change?|Use comparable site and cost data.
then_vs_now|Older and Newer Machines|What changed in output, emissions, visibility, and repair?|Hold attachment and task constant.
future_developments|A Proposed Autonomous Machine|What site and worker evidence is needed before deployment?|Define operating domain and oversight.
myths_vs_facts|Rated Capacity on Every Site?|When does ground or reach invalidate a headline rating?|Read configuration-specific chart.
documentary_stories|Machine from Factory to Site|How did delivery, setup, use, and repair affect a project?|Follow dated asset and site records.
system_boundary|Machine or Crew System?|Which production depends on traffic flow, materials, and spotters?|Define site boundary and time.
input_output_trace|Operator Command to Attachment|How does a control signal move through hydraulics to load?|Use measured response and configuration.
design_tradeoff|Power, Mass, and Reach|What stability or transport cost follows more reach?|Compare like tasks and site conditions.
failure_mode|A Documented Equipment Failure|What failed and which safeguards worked?|Use official investigation and maintenance evidence.
testing_limits|Test Ground versus Work Site|Which soil, slope, and visibility conditions change performance?|Compare test and field records.
standards_interoperability|Attachment and Machine Fit|Which rated interfaces and site rules apply?|Name model, attachment, jurisdiction, and date.
security_threat_model|Remote Equipment Controls|Which public controls protect command and stop functions?|Discuss governance, not bypass methods.
maintenance_lifecycle|Wear in a Hard Duty Cycle|Which components need inspection under a specific workload?|Use service records and condition monitoring.
infrastructure_dependencies|Fuel, Haul, and Ground|Which access, support, and supply systems govern uptime?|Map one site's logistics.
accessibility_usability|Cab Visibility and Controls|What can the operator see, reach, and understand?|Use NIOSH blind-area data and cab assessment.
independent_replication|Repeat a Productivity Result|Can a second site match units per hour?|Control material, haul distance, crew, and delay.
responsible_deployment|Equipment on a Live Site|What training, traffic separation, and monitoring are documented?|Use site-specific safety records.
field_prototype_testing|Trial under Site Conditions|What prototype test reflects real load and terrain?|Define task, surface, weather, and stop rules.
field_design_tolerance|Fit and Alignment under Load|Which manufacturing variation affects attachment performance?|Use inspections and controlled test.
field_manufacturing_method|Making a Heavy Component|How do weld, casting, machining, and inspection affect durability?|Trace an identified component.
field_failure_investigation|Equipment Incident Evidence|Which physical, operator, and maintenance records support cause?|Avoid attributing blame from one account.
field_repair_path|Repair and Return|What approved checks establish readiness after repair?|Use service and acceptance records.
"""


if __name__ == "__main__":
    revise_domain("430", "430_skyscrapers", SKYSCRAPERS,
                  "Skyscrapers through site decisions, structural systems, vertical services, worker labor, occupant access, and operation.",
                  "dated planning and as-built drawings, adopted codes and permits, wind and fire studies, commissioning and maintenance records, occupancy data, and worker accounts",
                  "Name building, jurisdiction, permit date, occupied use, and measurement boundary. Height rankings and energy claims depend on definitions; approval is not a universal safety guarantee.")
    revise_domain("431", "431_industrial_machines", MACHINES,
                  "Industrial machines through production tasks, controls and tolerances, safeguarding, operator work, maintenance, and measured output.",
                  "dated machine drawings and manuals, factory production and quality records, OSHA machine-guarding and hazardous-energy guidance, incident reports, and worker testimony",
                  "Name machine model, task, configuration, site, and rule jurisdiction. Questions do not instruct guard removal or servicing around hazardous energy.")
    revise_domain("432", "432_heavy_equipment", EQUIPMENT,
                  "Heavy equipment through bounded site tasks, load and ground conditions, visibility, operator coordination, uptime, and repair.",
                  "configuration-specific ratings, NIOSH visibility studies, site logs, manufacturer service records, incident investigations, and operator accounts",
                  "Name machine, attachment, load, reach, terrain, site, and date. A rated capacity or visibility diagram does not establish safety at every location.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
