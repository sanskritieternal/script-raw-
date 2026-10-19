"""Editorial question designs for structures and construction work."""

from review_angle_plans import audit, revise_domain


BRIDGES = """history_origins|A Crossing Becomes a Bridge|Which geography and travel need shaped an early bridge?|Trace plans, funding, and prior routes.
famous_examples|A Notable Bridge Reexamined|What do its design and inspection records establish?|Specify original build, modifications, and current condition.
hidden_stories|Labor at a Crossing|Whose building and maintenance work is absent from the story?|Use contract, payroll, and oral-history evidence.
beginner_explainers|How a Bridge Carries Load|How do deck, supports, and foundations pass loads to ground?|Use one structural type and load case.
advanced_concepts|Scour and Foundation Risk|How does water action alter a bridge's support?|Compare hydraulic model, inspection, and flood history.
mysteries_unsolved_cases|Uncertain Bridge Damage|Which inspection and material evidence could distinguish causes?|Avoid diagnosing from appearance alone.
technology_innovation|A New Bridge Material|Did a material improve durability or construction speed?|Compare matched structures and long-term records.
people_personalities|A Bridge Design Decision|Who chose a structural scheme, and what alternatives were rejected?|Read dated drawings and committee records.
major_events|A Crossing Opens or Closes|How did travel and community access change?|Compare route and traffic evidence before and after.
how_it_works|Inspection to Repair|How does a finding become a load decision or repair order?|Follow one documented owner process.
rise_fall|A Bridge Replaced|Why did repair lose to replacement?|Compare condition, capacity, cost, and route needs.
then_vs_now|One Bridge over Time|Which components changed since construction?|Use dated inspection and rehabilitation records.
future_developments|A Proposed Bridge|What tests and approvals would support its planned capacity?|Treat cost and travel forecasts as uncertain.
myths_vs_facts|Poor Condition Means Collapse?|What does an official condition label actually measure?|Read component ratings and current restrictions.
documentary_stories|Crossing from Plan to Service|Which design and site findings changed the built bridge?|Trace drawings, change orders, and inspections.
system_boundary|Bridge versus Corridor|Which delays or risks belong to approaches and network connections?|Define segment and time period.
input_output_trace|Vehicle Load through Structure|How is load distributed to deck, members, and foundations?|Use design drawings and bounded load cases.
design_tradeoff|Span, Material, and Cost|What did a chosen span arrangement gain and cost?|Compare alternatives under same site constraints.
failure_mode|A Documented Bridge Failure|Which sequence did official investigation establish?|Distinguish initiating failure from contributing conditions.
testing_limits|Model versus Field Behavior|Which assumptions in a bridge model need field validation?|Compare sensor, load-test, and inspection evidence.
standards_interoperability|Applicable Bridge Criteria|Which design and inspection rules governed a named crossing?|Name owner, jurisdiction, and edition.
security_threat_model|Keeping a Crossing Available|Which publicly documented hazards and redundancies shape continuity?|Focus on governance, not attack steps.
maintenance_lifecycle|Condition through Decades|How do inspections trigger preservation or replacement?|Track components, dates, and traffic loading.
infrastructure_dependencies|Bridge and River or Road|Which waterway, utility, and approach systems affect service?|Use one crossing and seasonal conditions.
accessibility_usability|Crossing for All Users|Can pedestrians, cyclists, and mobility-device users cross safely?|Check ramps, width, barriers, and connections.
independent_replication|Checking a Condition Claim|Can an analyst reproduce a published bridge classification?|Use component ratings, inventory date, and coding rules.
responsible_deployment|Bridge Opening and Monitoring|What postconstruction inspection and traffic evidence is needed?|Compare design promises with first-year use.
field_route_capacity|A Crossing's Bottleneck|Is capacity set by bridge lanes or approaches?|Measure both directions and peak queues.
field_vehicle_design|Design Vehicle on a Bridge|Which vehicles and weights fit the posted crossing?|Use current load rating and restrictions.
field_maintenance_system|Access for Bridge Repair|Can crews inspect and replace vulnerable components?|Check access plan, closures, and owner records.
field_safety_case|Evidence behind a Load Posting|Which inspection and analysis support a current restriction?|Date the rating and distinguish condition from capacity.
field_construction_impact|Building a Crossing|Which water, habitat, land, and material impacts were monitored?|Compare assessment and observed results.
"""

TUNNELS = """history_origins|Why a Tunnel Here?|Which terrain, density, or water crossing motivated one tunnel?|Compare dated surface and tunnel alternatives.
famous_examples|A Well-Known Tunnel Examined|What do build and operating records actually show?|Specify bore, purpose, and refurbishment history.
hidden_stories|Labor Underground|Whose hazardous work and displacement are omitted?|Use worker, contract, and local records.
beginner_explainers|Parts of a Transport Tunnel|How do excavation, lining, drainage, ventilation, and exits connect?|Use one road or rail tunnel.
advanced_concepts|Ground and Lining Interaction|How do soil or rock conditions influence support design?|Compare site investigation and observed movement.
mysteries_unsolved_cases|Unexplained Water Ingress|Which measurements could separate ground, joint, and drainage causes?|Use inspections and monitoring over time.
technology_innovation|A Tunneling Method|Did a new method improve settlement, speed, or safety?|Compare similar sites and ground conditions.
people_personalities|A Route and Method Choice|Who selected the alignment or excavation method, and why?|Read alternatives and review records.
major_events|A Tunnel Enters Service|What did opening change in route time and surface access?|Compare actual service with forecasts.
how_it_works|From Survey to Lining|How do ground investigation, excavation, support, and monitoring interact?|Trace a documented project stage.
rise_fall|A Tunnel Closes or Rebuilds|Which condition or service limit drove the decision?|Use inspection, outage, and cost records.
then_vs_now|A Tunnel through Refits|How did ventilation, lighting, exits, and use change?|Compare dated plans and inspections.
future_developments|A Proposed Tunnel Link|What evidence would test its cost and route benefit?|Compare alternatives and uncertain ground risk.
myths_vs_facts|Deep Means Safe?|Which risks remain despite depth?|Check ground, water, fire, ventilation, and egress evidence.
documentary_stories|One Tunnel Project's Record|Which unexpected ground conditions changed design or schedule?|Use dated logs and change orders.
system_boundary|Tunnel versus Network|Which outcomes depend on portals, stations, approaches, and diversions?|Define door-to-door or portal-to-portal scope.
input_output_trace|Water to Drainage System|How does seepage reach drains, pumps, and discharge?|Use design and inspection records.
design_tradeoff|Bore Size and Evacuation|How did space allocation affect cost, capacity, and emergency access?|Use approved alternatives.
failure_mode|A Documented Tunnel Incident|What systems failed and which worked?|Use official investigation and response review.
testing_limits|Ground Model versus Excavation|Which assumptions required correction as work advanced?|Compare bore logs, settlement, and monitoring.
standards_interoperability|Inspection and Fire Rules|Which requirements applied to one tunnel?|Name use, jurisdiction, date, and editions.
security_threat_model|Tunnel Service Continuity|Which public controls address disruption and recovery?|Discuss resilience without operational vulnerabilities.
maintenance_lifecycle|Lining and Equipment Aging|Which inspection findings drive repair?|Track structure, drainage, power, and ventilation separately.
infrastructure_dependencies|Tunnel Systems|Which power, pumps, control, and surface links are essential?|Map dependencies and backup evidence.
accessibility_usability|A Tunnel Journey|Can users find routes and exits with varied mobility needs?|Check signage, gradients, lifts, and alternatives.
independent_replication|Recheck a Settlement Claim|Can measured ground movement be reproduced from monitoring data?|Match sensors, baseline, time, and location.
responsible_deployment|Opening a Tunnel|What commissioning, training, and monitoring preceded service?|Use operator and regulator records.
field_route_capacity|Tunnel at Peak Use|Is throughput limited by bore, portals, or downstream links?|Use observed flows and restrictions.
field_vehicle_design|Vehicle Envelope|Which rail cars or road vehicles fit the built clearances?|Use drawings and current operating rules.
field_maintenance_system|Keeping a Tunnel Open|How are inspections and repairs scheduled without losing access?|Examine closures, spare equipment, and crews.
field_safety_case|Tunnel Safety Evidence|Which inspections, drills, and equipment tests support operation?|Name tunnel and period; avoid blanket guarantees.
field_construction_impact|Excavation Footprint|What spoil, settlement, water, and neighborhood effects occurred?|Compare assessment and monitoring.
"""

CONSTRUCTION = """history_origins|A Building Method Adopted|Which site and labor constraints led to a method's use?|Trace dated projects and technical records.
famous_examples|A Project beyond Its Image|What do contracts, inspections, and occupancy show?|Compare design intent with as-built records.
hidden_stories|Workers and Subcontractors|Whose tasks and exposure are missing from a project's story?|Use contracts, site logs, and worker accounts.
beginner_explainers|Project from Ground to Handover|How do design, permits, procurement, build, and inspection connect?|Follow one bounded project.
advanced_concepts|Managing Interface Risk|Where do structure, envelope, mechanical systems, and trades conflict?|Use clash, change, and defect records.
mysteries_unsolved_cases|A Defect with Several Causes|Which records distinguish design, materials, installation, and maintenance?|Avoid blame without investigation.
technology_innovation|A New Construction Method|Did it improve measured time, quality, or safety?|Compare similar projects and adoption costs.
people_personalities|A Site Decision|Who approved a key change, and what constraints mattered?|Use dated request and approval records.
major_events|A Construction Stoppage|What triggered it, and what changed before work resumed?|Read official order, schedule, and remedy.
how_it_works|Drawing to Installed Work|How does a specification become a verified built element?|Trace procurement, installation, test, and sign-off.
rise_fall|A Method Discontinued|Which cost, defect, or rule evidence drove replacement?|Compare period and project types.
then_vs_now|Construction across Eras|How did labor, materials, quality checks, and site conditions change?|Use comparable project measures.
future_developments|A Proposed Construction System|What trials and code review would justify use?|Treat productivity and carbon forecasts as conditional.
myths_vs_facts|On Time and on Budget?|Which baseline and scope changes shape a project claim?|Compare original and approved revisions.
documentary_stories|One Project's Change Orders|How did field conditions alter design and cost?|Build a dated contract and inspection timeline.
system_boundary|What Is in the Project?|Which off-site supply, utilities, and later operation belong to a claimed outcome?|Define cost and impact boundaries.
input_output_trace|Material to Installed Component|How are batch, delivery, inspection, and acceptance linked?|Follow traceable records for one component.
design_tradeoff|Speed, Cost, and Quality|Which measured gains or losses followed a schedule change?|Use matched scope and defect data.
failure_mode|A Construction Incident|Which causal and organizational factors were officially established?|Use investigation findings, not speculation.
testing_limits|Mockup versus Finished Building|Which site conditions change performance?|Compare mockup, field tests, and occupancy data.
standards_interoperability|Codes and Specifications|Which adopted code and contract edition governed a project?|Name jurisdiction, permit date, and approved changes.
security_threat_model|Site Access and Records|Which public governance controls protect workers and project data?|Avoid operational bypass details.
maintenance_lifecycle|Built Asset after Handover|Which defects and upkeep needs appeared during use?|Read warranties, inspections, and owner records.
infrastructure_dependencies|Project and Utility Connections|Which power, water, road, and permits determine completion?|Trace dated coordination.
accessibility_usability|Using the Finished Space|Does the built result meet diverse users' needs?|Compare approved design, field measurements, and user experience.
independent_replication|Verify a Productivity Claim|Can another analyst calculate labor hours per completed unit?|Use scope, schedule, quality, and denominator.
responsible_deployment|Handover with Evidence|What tests, training, and documents were delivered to operators?|Audit commissioning and punch list.
field_route_capacity|Construction Logistics|Can deliveries and workers reach a constrained site?|Model access windows and neighborhood effects.
field_vehicle_design|Equipment on Site|Which equipment fits ground, reach, and access constraints?|Use approved site plan and load limits.
field_maintenance_system|Maintaining Built Work|Was repair access designed and documented?|Examine as-builts, manuals, and physical access.
field_safety_case|Evidence for Site Safety|What inspections and controls address a defined hazard?|Use site-specific plan and incident data.
field_construction_impact|Project Footprint|Which waste, emissions, land, and community effects were measured?|Set construction phase and compare baseline.
"""


if __name__ == "__main__":
    revise_domain("427", "427_bridges", BRIDGES,
                  "Bridges through crossing decisions, structural load paths, inspection, condition ratings, maintenance, and access.",
                  "dated design and as-built drawings, FHWA bridge inventory and inspection records, owner load ratings, repair records, official investigations, and community testimony",
                  "Name bridge, owner, inventory date, jurisdiction, and load case. A condition label is not by itself a collapse forecast or load rating.")
    revise_domain("428", "428_tunnels", TUNNELS,
                  "Transport tunnels through route alternatives, ground investigation, excavation, lining, ventilation, operation, and inspection.",
                  "project ground and construction logs, FHWA tunnel inspection guidance, owner inventory and monitoring data, emergency reviews, and environmental assessments",
                  "Name tunnel use, bore, operator, date, and ground context. Keep safety and security discussion at public-evidence level.")
    revise_domain("429", "429_construction", CONSTRUCTION,
                  "Construction through project decisions, labor, contracts, quality control, site safety, handover, and actual performance.",
                  "dated contracts and change orders, approved plans, site and inspection logs, OSHA materials, commissioning records, incident investigations, and user accounts",
                  "Name project, jurisdiction, permit and code edition, and scope baseline. Do not turn research questions into site instructions or compliance claims.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
