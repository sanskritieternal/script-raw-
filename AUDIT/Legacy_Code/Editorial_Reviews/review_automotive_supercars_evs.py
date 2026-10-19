"""Editorial question designs for vehicle engineering and use."""

from review_angle_plans import audit, revise_domain


AUTOMOTIVE = """history_origins|A Vehicle System's Design History|Which documented constraint drove an early design change?|Trace dated drawings, tests, and production versions.
famous_examples|A Widely Studied Vehicle|Which engineering choices explain a named model's reputation?|Compare measured outcomes with marketing and model-year changes.
hidden_stories|Workers behind a Vehicle|Which technician, supplier, or test team contribution is missing?|Use credits, oral histories, and dated production records.
beginner_explainers|Follow Energy through a Car|Where does energy enter, convert, dissipate, and reach the wheels?|Specify powertrain and driving condition.
advanced_concepts|Coupled Vehicle Tradeoffs|How does changing vehicle mass affect braking, handling, efficiency, and crash design?|Use one defined vehicle and engineering model.
mysteries_unsolved_cases|A Defect under Investigation|Which failure mechanism is supported by current evidence?|Separate complaints, investigation, and confirmed cause.
technology_innovation|A New Component Tested|What changed when one component entered a production vehicle?|Compare baseline and updated tests under matched conditions.
people_personalities|An Engineer's Decision|What evidence explains one named design choice?|Use contemporaneous records and distinguish team work.
major_events|A Recall and Redesign|What defect was identified, and what did the remedy address?|Trace official notice, affected models, and verification.
how_it_works|One Vehicle System End to End|How do sensors, controls, hardware, and driver interact?|Follow a bounded function through input and response.
rise_fall|A Design Retired|Which cost, safety, reliability, or regulatory pressures ended one design?|Compare documented versions and replacement.
then_vs_now|Two Generations Compared|Which measurements can be compared across model generations?|Control mass, tires, test cycle, and equipment.
future_developments|A Proposed Vehicle Feature|What proof would establish useful performance in production?|Define tests, failure criteria, and deployment context.
myths_vs_facts|A Headline Performance Number|Which test conditions make a quoted result comparable?|Check protocol, configuration, and independent replication.
documentary_stories|From Prototype to Road|Which test and manufacturing decisions changed one vehicle?|Follow dated prototype, homologation, and production evidence.
system_boundary|What Counts as the Car?|Which outcomes depend on vehicle, driver, road, fuel, or service network?|Define boundary before comparing performance.
input_output_trace|Driver Command to Motion|How does one command pass through control and actuation?|Record latency, feedback, and operating mode.
design_tradeoff|Safety, Mass, and Efficiency|What gains and losses followed a documented design compromise?|Compare matched measurements and constraints.
failure_mode|One Component Failure|What failed first and how did effects spread?|Use inspection, recall, or test evidence; avoid speculation.
testing_limits|Laboratory versus Road|Which dynamometer or track result fails to predict everyday use?|State cycle, weather, load, and driver behavior.
standards_interoperability|A Vehicle Requirement|Which standard applies to the selected model and market?|Check edition, jurisdiction, and certification scope.
security_threat_model|Connected Vehicle Exposure|Which interface could permit a documented misuse?|Bound software version, access, and tested mitigation.
maintenance_lifecycle|Part through Service Life|When does inspection, repair, or replacement become necessary?|Use service records and failure data by mileage and age.
infrastructure_dependencies|Vehicle and Road Network|Which road, fuel, repair, or data dependency shapes actual use?|Map availability and local conditions.
accessibility_usability|Controls for Different Drivers|Who can reach, understand, and operate a key function?|Use human-factors testing across users.
independent_replication|Repeat a Vehicle Test|Can another lab reproduce a claimed result?|Match configuration, protocol, instrumentation, and uncertainty.
responsible_deployment|Introducing a New Feature|What monitoring and remedy plan follows release?|Track incidents, updates, recalls, and owner communication.
field_route_capacity|A Road Route's Capacity|How do vehicle dimensions and traffic conditions affect a named route?|Separate vehicle limits from network capacity.
field_vehicle_design|Vehicle Layout in Context|How does a design serve one defined use case?|Compare packaging, visibility, protection, and service access.
field_maintenance_system|Service Network for a Model|Can a repair network diagnose and supply a critical part?|Check manuals, tools, parts lead time, and coverage.
field_safety_case|Evidence for Safe Operation|Which tests and real-use reports support a bounded safety claim?|Distinguish rating, compliance, and residual risk.
field_construction_impact|Building the Vehicle|Which material and factory choices create measurable impacts?|Define production boundary and supplier evidence.
"""

SUPERCARS = """history_origins|A Supercar Lineage|Which design and market changes shaped one named lineage?|Use dated model specifications and contemporary accounts.
famous_examples|A Celebrated Supercar Rechecked|What do independent tests establish about a famous model?|State year, trim, tires, surface, and test conditions.
hidden_stories|Specialist Work behind the Badge|Which supplier or craft team built a defining system?|Trace component provenance and production records.
beginner_explainers|What Makes a Supercar?|Which measurable traits and cultural claims define a chosen comparison set?|Make inclusion rules explicit.
advanced_concepts|Performance under Thermal Load|How does repeated hard use change brakes, tires, and power delivery?|Use instrumented sessions and temperature data.
mysteries_unsolved_cases|A Disputed Record|Which missing measurements prevent validation of a claimed speed or lap?|Audit timing, route, configuration, and witnesses.
technology_innovation|A Performance Device|Did one aero, chassis, or powertrain feature improve a measured outcome?|Compare matched runs and tradeoffs.
people_personalities|Designer and Development Team|What did a named designer propose and what did others change?|Use interviews alongside dated drawings.
major_events|A Model Launch Claim|Which promised capability survived independent testing?|Separate launch presentation from delivered specification.
how_it_works|Grip through a Fast Corner|How do tire, suspension, aero, and driver inputs interact?|Use speed and load data for a defined turn.
rise_fall|A Supercar Program Ends|Which cost, regulation, or demand factors are documented?|Check company filings and production history.
then_vs_now|Two Eras on Comparable Terms|How do older and newer supercars differ under matched tests?|Account for tires, track, weather, and safety rules.
future_developments|A Proposed Supercar Technology|What test would justify its performance promise?|Set measurable outcome and repeatability threshold.
myths_vs_facts|Top-Speed Headline|Was the quoted speed independently measured and repeatable?|Check run direction, instrumentation, and production configuration.
documentary_stories|One Car's Development|How did prototype tests change the delivered car?|Trace dated prototypes, homologation, and owner reports.
system_boundary|Car or Test Package?|Which parts of a lap result belong to driver, tires, track, and car?|Define allowed modifications and conditions.
input_output_trace|Throttle to Acceleration|How do driver request, traction control, powertrain, and tires interact?|Record mode and launch conditions.
design_tradeoff|Downforce and Drag|What did added aerodynamic load cost in speed, efficiency, or comfort?|Compare matched configurations and measured force.
failure_mode|Track-Day Failure|Which component reached a limit during repeated laps?|Use inspection and logs; distinguish wear from defect.
testing_limits|One Fast Lap|How representative is a single lap time?|Check repeat runs, weather, tire state, and timing method.
standards_interoperability|Road-Legal Performance|Which market and model-year rules shaped the delivered specification?|Use official approval and vehicle records.
security_threat_model|Connected Performance Systems|What access or update path could affect a vehicle mode?|Bound software version and documented threat.
maintenance_lifecycle|Cost of Keeping Performance|Which service operations and consumables dominate use?|Use manuals, invoices, and mileage without price generalization.
infrastructure_dependencies|Where Can It Be Used?|Which roads, tracks, fuel, and service access support a model?|State location and legal operating conditions.
accessibility_usability|Entering and Driving the Car|Which cockpit and control choices exclude some users?|Assess reach, visibility, ingress, and feedback.
independent_replication|Rechecking a Performance Claim|Can an independent team match a reported result?|Specify car, tire, driver, venue, weather, and timing.
responsible_deployment|Marketing a Speed Claim|What evidence and qualification should accompany it?|Separate controlled test from public-road capability.
field_route_capacity|Route Fit for a Supercar|How do clearance, width, traffic, and speed limits constrain a route?|Use legal and measured route data.
field_vehicle_design|Packaging for Performance|How do engine, cabin, cooling, and crash structure share limited space?|Use drawings and physical measurements.
field_maintenance_system|Specialist Service Capacity|Can owners access qualified diagnostics and parts?|Check actual coverage and wait times.
field_safety_case|High-Speed Safety Claim|Which crash, braking, and stability evidence applies?|Name tested version and avoid universal safety claims.
field_construction_impact|Low-Volume Production|What material, tooling, and labor impacts can be documented?|Define unit and production boundary.
"""

EVS = """history_origins|One EV Program's Path|Which battery, policy, and market constraints shaped a named model?|Trace dated prototypes and production records.
famous_examples|An EV Range Claim Examined|What does the official range test establish for a selected model?|Name test cycle, version, and weather limitation.
hidden_stories|Materials and Labor behind an EV|Which supplier, worker, or community experience is missing?|Trace verifiable supply-chain records and testimony.
beginner_explainers|Energy from Outlet to Wheel|Where are charging, storage, conversion, and driving losses?|Define boundary and use measured energy.
advanced_concepts|Battery Thermal Management|How do temperature and power demand affect charge and discharge?|Use pack limits and controlled measurements.
mysteries_unsolved_cases|A Range Shortfall|Which factors could explain a documented trip's lower range?|Check speed, weather, load, terrain, and battery state.
technology_innovation|A New Cell or Charging Feature|What improved in production use and under which conditions?|Compare matched tests and degradation evidence.
people_personalities|An EV Design Decision|Who argued for one architecture and why?|Use dated records and team attribution.
major_events|An EV Recall|Which defect and models did an official recall identify?|Trace remedy, dates, and post-remedy evidence.
how_it_works|A DC Charging Session|How do charger, vehicle, battery, and grid coordinate power?|Follow handshake, taper, and measured energy.
rise_fall|An EV Model Discontinued|Which documented factors explain its end?|Compare sales, costs, compliance, and replacement.
then_vs_now|Two EV Generations|How have usable energy, efficiency, and charging changed?|Compare like test cycles and equipment.
future_developments|A Battery Promise|What would validate a claimed future improvement?|Specify production scale, durability, and test protocol.
myths_vs_facts|Zero Emissions?|Which emissions disappear at the tailpipe and which remain elsewhere?|Define electricity, manufacturing, and use boundaries.
documentary_stories|One EV Trip's Evidence|How did route, charger uptime, and weather shape the trip?|Use dated logs; avoid universalizing one journey.
system_boundary|Where Does EV Efficiency Begin?|Does the claim measure pack, plug, generation, or full lifecycle?|State energy and emissions boundaries.
input_output_trace|Plug to Stored Energy|Where did metered electricity go during one charge?|Compare station meter, vehicle report, and battery estimate.
design_tradeoff|Battery Size and Mass|How did added capacity alter range, cost, load, and charging?|Use a defined platform and matched cycle.
failure_mode|Charging Failure Diagnosis|Was a failed session caused by car, plug, station, network, or payment?|Check logs and repeated tests.
testing_limits|Rated versus Trip Range|Which official cycle assumptions differ from one journey?|Name speed, weather, climate use, and vehicle condition.
standards_interoperability|Connector Compatibility|Can a selected car charge at a selected station today?|Verify hardware, protocol, adapter, software, and date.
security_threat_model|Charger Account Exposure|Which data and control paths create a documented risk?|Bound operator, app, and software version.
maintenance_lifecycle|Battery and Vehicle Aging|What evidence shows capacity and repair needs over time?|Use cohorts, measurement method, and warranty terms.
infrastructure_dependencies|Charging Access|Which home, workplace, public, and grid conditions determine usefulness?|Map access and reliable uptime by place.
accessibility_usability|Using a Public Charger|Can drivers reach, handle, pay for, and understand the equipment?|Observe varied users and site layout.
independent_replication|Repeat an EV Efficiency Test|Can another team reproduce a consumption figure?|Match cycle, temperature, tires, and charge state.
responsible_deployment|EV Rollout and Support|What repair, charging, and recall support is needed after sale?|Track uptime and owner outcomes.
field_route_capacity|Charging along a Route|Can available stalls serve the expected vehicles and dwell times?|Model queue, uptime, arrival rate, and alternatives.
field_vehicle_design|EV Packaging Choices|How do pack position, cooling, crash structure, and cabin space interact?|Use production drawings and test evidence.
field_maintenance_system|EV Service Capability|Which repairs need specialist tools, parts, and training?|Check local coverage and documented procedures.
field_safety_case|Battery and Road Safety|Which tests support a specific EV safety claim?|Separate crash rating, battery abuse test, and real-world data.
field_construction_impact|Building Chargers and Batteries|Which materials, energy, land, and labor impacts are measurable?|Set lifecycle boundary and avoid double counting.
"""


if __name__ == "__main__":
    revise_domain("418", "418_automotive_engineering", AUTOMOTIVE,
                  "Automotive engineering through bounded vehicle systems, test conditions, production variants, service, and road use.",
                  "dated design and service documents, official test protocols and recalls, instrumented measurements, production records, and independent replication",
                  "Name model, year, configuration, jurisdiction, and test conditions. A rating, certification, or demonstration applies only within its defined scope.")
    revise_domain("419", "419_supercars", SUPERCARS,
                  "Supercars through verifiable design choices, repeatable performance, specialist production, ownership, and lawful use.",
                  "dated factory specifications and drawings, independent instrumented tests, track logs, official approval records, service documentation, and production records",
                  "Define the comparison set, car version, tires, driver, venue, and weather. Do not treat marketing records or track performance as public-road guidance.")
    revise_domain("420", "420_electric_vehicles", EVS,
                  "Electric vehicles through measured energy flow, range and charging conditions, lifecycle boundaries, and user access.",
                  "official range protocols and labels, metered charge and trip logs, battery and service records, station reliability data, recall notices, and lifecycle methods",
                  "Name vehicle version, test cycle, temperature, charger configuration, place, and date. Separate tailpipe, electricity, and manufacturing boundaries.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
