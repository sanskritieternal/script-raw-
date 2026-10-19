"""Editorial question designs for batteries, aircraft, and rockets."""

from review_angle_plans import audit, revise_domain


BATTERIES = """history_origins|A Battery Chemistry Reaches the Road|Which tested advantage let a cell chemistry enter a named vehicle?|Trace dated cell, pack, and production evidence.
famous_examples|A Battery Pack Examined|What does a well-documented pack show about architecture and performance?|State model year, cell chemistry, and configuration.
hidden_stories|Supply Chain behind a Cell|Whose extraction, processing, or assembly work is absent from the story?|Use traceable supplier and labor records.
beginner_explainers|Cell, Module, and Pack|Which functions and protections are added at each level?|Follow one documented vehicle design.
advanced_concepts|The Degradation Problem|How do time, temperature, and cycling interact in a tested battery?|Use capacity definitions and comparable cohorts.
mysteries_unsolved_cases|An Unexplained Pack Failure|What evidence distinguishes cell, cooling, control, and external damage?|Use teardown and diagnostic records.
technology_innovation|A New Cell Design|Which benefit survives pack-level and life-cycle testing?|Compare matched conditions and production status.
people_personalities|Battery Development Team|Who made one documented design choice and why?|Credit materials, integration, and test teams.
major_events|A Battery Recall|Which packs were affected and how was the defect bounded?|Read official notice, remedy, and follow-up.
how_it_works|Charge through a Pack|How do cells, sensors, controls, and cooling shape charge power?|Trace measurements across one session.
rise_fall|A Cell Chemistry Replaced|Which durability, cost, supply, or safety evidence drove change?|Compare versions and production dates.
then_vs_now|Two Pack Generations|What changed in usable energy, mass, charging, and serviceability?|Use aligned metrics and test cycles.
future_developments|A Proposed Battery Breakthrough|What production-scale evidence would confirm the claim?|Require durability, safety, cost, and yield data.
myths_vs_facts|Capacity Is Not Range|When does nominal pack capacity fail to predict vehicle range?|Include usable window, efficiency, and conditions.
documentary_stories|One Battery's Lifecycle|What records follow cells from materials to reuse or recycling?|Trace custody and measured recovery.
system_boundary|Where Is Battery Performance Measured?|Does a figure describe cell, module, pack, or vehicle?|Define energy, mass, and test temperature.
input_output_trace|Power into Stored Energy|Where does energy go during a measured charge?|Compare meter, pack, thermal, and auxiliary data.
design_tradeoff|Energy, Power, and Lifetime|What is gained and lost by changing cell or pack design?|Use controlled tests and vehicle use case.
failure_mode|A Battery Fault Chain|Which initiating event and safeguards are documented?|Use qualified incident and lab evidence.
testing_limits|Accelerated Aging Limits|Which lab stress fails to represent years of road use?|Compare protocol and observed field degradation.
standards_interoperability|Battery Test Definition|Which test standard and edition produced a published result?|State cell format and pass criterion.
security_threat_model|Battery Control Interface|What authenticated update or diagnostic path can alter limits?|Bound model, software version, and evidence.
maintenance_lifecycle|Pack Health in Service|Which measurement supports a repair or replacement decision?|State capacity method, uncertainty, and warranty terms.
infrastructure_dependencies|Materials and Power|Which supply and charging dependencies shape pack deployment?|Map source, grid, and service network.
accessibility_usability|Battery Information for Drivers|Can a user interpret state of charge and health accurately?|Test interface wording against actual limitations.
independent_replication|Repeat a Cell Result|Can another lab reproduce a reported lifetime?|Match chemistry, protocol, temperature, and statistics.
responsible_deployment|Pack after Vehicle Service|How are damaged and retired packs identified and handled?|Use manufacturer and authorized recycler procedures.
field_route_capacity|Battery on a Defined Route|What reserve is available after a specified trip?|Model grade, weather, speed, and charging stops.
field_vehicle_design|Pack in Vehicle Structure|How do enclosure, cooling, crash protection, and repair access interact?|Use production drawings and tests.
field_maintenance_system|Diagnosing a Pack|What tools and trained workers are available for one model?|Check service instructions and local availability.
field_safety_case|Battery Safety Evidence|Which abuse, crash, and field tests support a bounded claim?|Identify standard, configuration, and residual uncertainty.
field_construction_impact|Battery Production Footprint|Which mining and manufacturing impacts are measurable?|Set life-cycle boundary and material source.
"""

AIRCRAFT = """history_origins|A Design Requirement Takes Shape|Which route, payload, or safety requirement shaped one aircraft?|Use dated design and certification records.
famous_examples|A Famous Aircraft Reassessed|Which design choices explain a named aircraft's role?|Compare production versions and operating evidence.
hidden_stories|Workers behind Flight Test|Which test, maintenance, or manufacturing contribution is overlooked?|Use documented personnel and program records.
beginner_explainers|Lift, Thrust, and Control|How do these systems interact in one phase of flight?|Use a specified aircraft and conditions.
advanced_concepts|Aeroelastic Design Limit|What evidence sets an aircraft's safe operating envelope?|Read analysis, ground tests, and flight tests.
mysteries_unsolved_cases|An Unresolved Technical Event|Which evidence is missing from an aircraft investigation?|Separate preliminary report from final finding.
technology_innovation|A New Aircraft Material|Did a design material improve mass, durability, or maintainability?|Compare tests and in-service evidence.
people_personalities|A Design Decision in Context|Who proposed one aircraft solution and who tested it?|Use dated team and regulator records.
major_events|A Certification Milestone|What exactly did an approval permit at that date?|Check type, variant, operating limits, and jurisdiction.
how_it_works|Flight Control Chain|How does pilot input become an aerodynamic response?|Follow sensor, control law, actuator, and feedback.
rise_fall|An Aircraft Type Retired|Which economics, maintenance, or rule changes explain withdrawal?|Distinguish fleet and model-specific evidence.
then_vs_now|Two Aircraft Generations|Which efficiency and safety measures can be fairly compared?|Align payload, route, test basis, and period.
future_developments|A Proposed Aircraft Design|What ground and flight evidence would support deployment?|Treat certification and production as separate gates.
myths_vs_facts|A Claimed Fuel Saving|Does a published percentage hold for an actual mission?|State load, distance, weather, and baseline.
documentary_stories|Prototype to Service|How did test findings change one aircraft before delivery?|Follow dated test, redesign, approval, and service records.
system_boundary|Aircraft or Flight Operation?|Which performance depends on airframe, crew, weather, and airspace?|Define measurement boundary.
input_output_trace|Command to Surface|What happens after one flight-control command?|Trace redundancy, timing, and actuator response.
design_tradeoff|Wing Design Tradeoff|How does one wing choice affect drag, structure, and handling?|Use matched analyses and certified limits.
failure_mode|A Documented Component Failure|What fault path and mitigation were established?|Use investigation and airworthiness records.
testing_limits|Ground Test to Flight|Which assumptions must flight testing challenge?|Compare simulation, test conditions, and envelope.
standards_interoperability|Certification Basis|Which rules applied to a particular aircraft variant?|Name authority, amendment, and special conditions.
security_threat_model|Aircraft Data Interface|Which connectivity path has a documented risk and control?|Avoid speculative exploit instructions; bound version.
maintenance_lifecycle|Continued Airworthiness|How did in-service data change an inspection or repair?|Use directives, service bulletins, and operator records.
infrastructure_dependencies|Aircraft and Airport|Which runway, ground service, and navigation systems are needed?|Use one aircraft and route.
accessibility_usability|Cockpit and Cabin Use|How does a design serve crew and passengers with varied needs?|Use human-factors and access evidence.
independent_replication|Repeating a Flight Result|Can another team reproduce a performance figure?|Match mass, atmosphere, configuration, and method.
responsible_deployment|Introducing an Aircraft Type|What training, maintenance, and monitoring accompany service entry?|Trace approval and operator evidence.
field_route_capacity|Aircraft on a Route|Can a type meet payload and range for a particular city pair?|Include reserves, weather, runway, and rules.
field_vehicle_design|Airframe Layout|How do structure, propulsion, cabin, and systems share space?|Use drawings and approved configuration.
field_maintenance_system|Support for a Fleet|Are parts, tooling, and technicians available where aircraft operate?|Check operator and approved service records.
field_safety_case|Basis for Safe Flight|Which tests and compliance findings support one claim?|Distinguish design approval from every-use guarantee.
field_construction_impact|Making an Aircraft|Which materials, energy, and labor impacts can be documented?|Set production boundary and supplier chain.
"""

ROCKETS = """history_origins|A Launch Vehicle Requirement|Which payload and mission need drove one rocket design?|Trace dated specifications and program decisions.
famous_examples|A Launch Vehicle Case|What do test and mission records show about a celebrated rocket?|Specify variant, flight, and outcome.
hidden_stories|People behind the Launch|Which test operators or manufacturing workers are omitted?|Use credited, dated program records.
beginner_explainers|Propulsion and Staging|Why might a rocket use multiple stages for one mission?|Explain mass flow and mission constraints without build instructions.
advanced_concepts|Guidance under Changing Conditions|How does a launch vehicle stay within its planned trajectory?|Use public control and flight-data descriptions.
mysteries_unsolved_cases|An Unresolved Anomaly|Which telemetry or physical evidence is needed to identify cause?|Distinguish preliminary hypotheses from final review.
technology_innovation|A New Engine Feature|What changed in tested thrust, reliability, or reuse?|Compare test campaigns and flight conditions.
people_personalities|A Program Decision|How did a named team choose among design alternatives?|Use dated decisions and shared credit.
major_events|A Flight Test Milestone|What did one flight demonstrate and leave unproven?|Read mission objectives and postflight findings.
how_it_works|Launch Sequence at System Level|How do ground, propulsion, guidance, and staging interact?|Use public sequence and outcome data; omit operational procedures.
rise_fall|A Vehicle Program Ends|Which documented cost, technical, or mission factors mattered?|Compare program records and successor plans.
then_vs_now|Two Rocket Generations|Which payload and reliability metrics can be compared?|Align orbit, configuration, sample size, and era.
future_developments|A Proposed Launch Capability|What tests and flights would validate its advertised use?|Mark projections and uncompleted milestones.
myths_vs_facts|A Payload Headline|Is a published payload figure tied to a specific orbit and variant?|Check mission profile and source.
documentary_stories|From Engine Test to Flight|How did one test finding change a launch program?|Trace dated reports, redesign, and mission results.
system_boundary|Rocket or Launch System?|Which outcome includes ground facilities, upper stage, or payload?|Define boundary and mission.
input_output_trace|Command to Vehicle Response|How do guidance commands and vehicle sensors produce a recorded response?|Use public data, not operational settings.
design_tradeoff|Payload and Margin|How does a design trade payload against margin or reuse?|Use public mission-level comparison.
failure_mode|An Officially Investigated Anomaly|What sequence and causal finding does the record support?|Use public investigation; avoid actionable failure detail.
testing_limits|Ground Test and Flight|Which flight conditions cannot be reproduced in a static engine test?|Compare environments and integration evidence.
standards_interoperability|Launch Interfaces|Which published interface and approval constraints apply to a payload?|Name operator, vehicle version, and date.
security_threat_model|Mission Assurance Boundaries|What public controls protect command integrity?|Discuss governance and verification at a high level.
maintenance_lifecycle|Reusable Hardware Inspection|What evidence supports another flight of one component?|Use public inspection and refurbishment findings.
infrastructure_dependencies|Launch Site Dependence|Which facilities and range approvals constrain one mission?|Name jurisdiction and site without operational detail.
accessibility_usability|Public Mission Data|Can non-specialists understand a mission outcome from available records?|Test definitions, units, and uncertainty.
independent_replication|Checking a Performance Claim|Can independent analysts reproduce a trajectory-level result?|Use public mission data and stated assumptions.
responsible_deployment|Launch Impact Review|Which community and environmental concerns were evaluated?|Use agency review and monitoring records.
field_route_capacity|Access to a Target Orbit|What payload can a version carry to a specified orbit?|State altitude, inclination, margin, and source.
field_vehicle_design|Vehicle Architecture|How do stages, fairing, and payload interfaces serve a mission?|Use public drawings and performance bounds.
field_maintenance_system|Launch Hardware Turnaround|Which inspections and facilities govern reuse?|Use public program evidence only.
field_safety_case|Evidence before Flight|Which qualification tests and range approvals support a mission?|Avoid claiming a launch is risk-free.
field_construction_impact|Building a Launch Vehicle|Which material and site impacts can be measured?|Bound production, testing, and launch phases.
"""


if __name__ == "__main__":
    revise_domain("421", "421_ev_battery_technology", BATTERIES,
                  "EV batteries through cell and pack evidence, lifecycle measurement, service, safety, and material provenance.",
                  "DOE battery test guidance, cell and pack measurements, official recalls, service records, supply-chain documents, and peer-reviewed lifecycle analyses",
                  "State chemistry, vehicle and pack version, test protocol, temperature, and lifecycle boundary. Never infer vehicle range from cell capacity alone.")
    revise_domain("422", "422_aircraft_engineering", AIRCRAFT,
                  "Aircraft engineering through design and production variants, certification basis, flight tests, operation, and continued airworthiness.",
                  "FAA certification and airworthiness records, dated design documents, ground and flight tests, accident investigations, operator manuals, and service records",
                  "Name aircraft variant, authority, rule edition, flight conditions, and report status. A test or certificate is bounded evidence, not a universal safety promise.")
    revise_domain("423", "423_rocket_engineering", ROCKETS,
                  "Rocket engineering through documented mission requirements, public test evidence, launch outcomes, program decisions, and societal effects.",
                  "NASA propulsion-test reports, public mission and flight records, launch approvals, official investigations, and environmental reviews",
                  "Name vehicle version, mission, orbit, date, and data source. Keep discussion at the system and public-evidence level, without operational construction or launch instructions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
