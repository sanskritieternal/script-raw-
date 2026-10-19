"""Editorial question designs for maritime and surface transport."""

from review_angle_plans import audit, revise_domain


SHIPS = """history_origins|A Ship Design Changes|Which cargo, route, or safety need drove one design revision?|Trace dated plans, trials, and operating records.
famous_examples|A Famous Vessel Reassessed|What do plans and service records show about a named ship?|Specify build date, refits, and route.
hidden_stories|Shipyard Labor|Whose fabrication or outfitting work is missing from a vessel's history?|Use yard records and attributed worker accounts.
beginner_explainers|Hull, Stability, and Load|How do hull form and cargo placement affect a ship's behavior?|Use one vessel type and loading condition.
advanced_concepts|Damage Stability|How does compartment design limit flooding in a specified case?|Use approved calculations and test assumptions.
mysteries_unsolved_cases|An Unexplained Vessel Loss|Which physical and voyage evidence remains unresolved?|Separate investigation findings from hypotheses.
technology_innovation|A New Shipyard Method|Did a construction method improve quality, time, or repairability?|Compare documented builds and defects.
people_personalities|A Naval Architect's Choice|Who argued for a design decision and who evaluated it?|Use dated drawings and team records.
major_events|Launch and Sea Trials|What did a vessel's trials demonstrate before delivery?|Compare test objectives and later service.
how_it_works|Building a Hull|How do design, material preparation, assembly, and inspection connect?|Follow one documented yard program.
rise_fall|A Vessel Type Retires|Which changes in trade, rules, or operating cost explain decline?|Use fleet and route evidence.
then_vs_now|Two Shipbuilding Eras|Which capacity, efficiency, and labor measures can be compared?|Align vessel type, route, and accounting boundary.
future_developments|A Proposed Low-Emission Ship|Which trials would verify claimed performance?|Specify fuel supply, route, and lifecycle boundary.
myths_vs_facts|Unsinkable Claim|Which flooding conditions did a design actually address?|Check approved stability basis and damage cases.
documentary_stories|Design to First Voyage|Which changes occurred between drawing, build, trial, and operation?|Build a dated evidence trail.
system_boundary|Ship versus Voyage|Which outcomes depend on hull, crew, weather, cargo, and port?|Define system and operating condition.
input_output_trace|Helm to Course Change|How do command, steering machinery, hull, and sea state interact?|Use recorded maneuvering trials.
design_tradeoff|Capacity and Stability|How did a cargo or deck choice affect stability and access?|Compare approved loading scenarios.
failure_mode|A Documented Structural Failure|What initiated damage and how was it contained?|Use official investigation and survey evidence.
testing_limits|Model Basin and Sea Trial|Which effects are absent from scale testing?|Compare model, full-size trial, and service records.
standards_interoperability|Ship Rules in Force|Which flag, class, and convention rules applied at delivery?|Name vessel type, date, and jurisdiction.
security_threat_model|Shipboard Control Networks|Which documented interfaces deserve protection?|Bound system and mitigation without exploit steps.
maintenance_lifecycle|Hull through Service Life|What inspection and repair history reveals deterioration?|Use surveys, dry-dock records, and age.
infrastructure_dependencies|Port and Ship Fit|Which depth, berth, cargo, and shore services constrain a vessel?|Check named ports and tides.
accessibility_usability|Life aboard for Different Users|How do boarding and spaces serve crew or passengers?|Use vessel layout and access assessments.
independent_replication|Repeat a Sea-Trial Result|Can another team match an efficiency or speed claim?|Align load, sea state, draft, and instrumentation.
responsible_deployment|Entering Maritime Service|What training, inspection, and pollution controls are required?|Follow actual operator and regulator records.
field_route_capacity|Ship on a Trade Route|Can vessel capacity and port limits serve a specific route?|Include draft, schedule, and seasonal conditions.
field_vehicle_design|Hull and Superstructure|How do cargo, propulsion, crew spaces, and stability share the vessel?|Use approved arrangement drawings.
field_maintenance_system|Repair Network|Where can a ship obtain suitable inspection, parts, and dry dock?|Map dated port availability.
field_safety_case|Evidence for a Safe Voyage|Which design approval, trials, and operating controls support a claim?|State applicable voyage and residual limits.
field_construction_impact|Shipyard Footprint|Which material, energy, waste, and labor impacts can be measured?|Set build and supplier boundaries.
"""

METROS = """history_origins|A Metro Line's Purpose|Which travel demand and land-use assumptions justified one line?|Read original plan and later ridership.
famous_examples|A Metro System in Context|What does one widely cited network demonstrate?|Compare service, funding, and city form.
hidden_stories|Workers and Displaced Residents|Who built the line and who lost access or land?|Use construction, compensation, and community records.
beginner_explainers|How a Metro Moves People|How do train frequency, dwell time, and transfer design set capacity?|Use one line and time period.
advanced_concepts|Reliability at High Frequency|How do signals and dwell variability propagate delays?|Compare actual headways and operating logs.
mysteries_unsolved_cases|An Unexplained Delay Pattern|Which data could distinguish equipment, staffing, and crowding causes?|Use incidents and service logs.
technology_innovation|An Automated Operation Change|Did automation improve service or shift work and risk?|Compare before and after on one line.
people_personalities|Planning a Line|Who decided alignment and who challenged it?|Trace hearings, alternatives, and affected groups.
major_events|A Line Opens|Which promised service and ridership materialized after opening?|Compare forecast, timetable, and observed use.
how_it_works|Train Dispatch to Platform|How are signals, vehicles, operators, and station staff coordinated?|Trace a service period with operational data.
rise_fall|A Metro Service Reduced|Which funding, demand, or maintenance factors explain the change?|Compare dated plans and service data.
then_vs_now|A Line over Two Decades|How did frequency, accessibility, and travel time change?|Hold route and measurement basis steady.
future_developments|A Proposed Extension|What demand, cost, and community evidence would support it?|Treat projections as scenarios.
myths_vs_facts|Capacity Claim|Does a quoted passengers-per-hour figure match delivered service?|Check train length, frequency, occupancy, and direction.
documentary_stories|From Alignment to Opening|How did design, construction, testing, and service evolve?|Build a dated project timeline.
system_boundary|Line versus Network|Which trip benefits depend on transfers, buses, walking, and fares?|Define door-to-door or station-to-station outcome.
input_output_trace|Train Command to Stop|How do signaling, braking, platform, and operator actions interact?|Use published system descriptions and incident records.
design_tradeoff|Speed versus Station Access|What did wider station spacing gain and cost?|Compare travel times and access by neighborhood.
failure_mode|A Service Disruption|Which equipment or process failed and how did it spread?|Use official investigation and recovery logs.
testing_limits|Trial Service versus Daily Operations|What did preopening tests miss about crowding and reliability?|Compare trial and first-year data.
standards_interoperability|Connecting Two Rail Systems|Which platform, power, signal, and fare interfaces matter?|Name systems and dates.
security_threat_model|Metro Control Resilience|Which public security measures protect service continuity?|Discuss oversight and recovery, not exploitable details.
maintenance_lifecycle|Track and Fleet Renewal|What deterioration evidence determines replacement timing?|Use inspection, backlog, and outage data.
infrastructure_dependencies|Power and City Services|Which external systems must work for this metro line?|Map power, drainage, telecom, and access.
accessibility_usability|A Journey with Mobility Needs|Can riders reach, board, transfer, and exit on a real route?|Check lift uptime, gaps, signage, and alternatives.
independent_replication|Recheck a Ridership Claim|Can published counts be reproduced from source data?|Match period, stations, transfer handling, and method.
responsible_deployment|New Metro Service|What training, safety oversight, and community monitoring precede opening?|Use local authority records.
field_route_capacity|A Corridor at Peak Hour|How many passengers can a line actually move?|Use observed headways, train capacity, and constraints.
field_vehicle_design|Train and Station Fit|How do door layout, platform length, and circulation interact?|Use vehicle and station drawings.
field_maintenance_system|Keeping Trains Available|Do depots, spares, and technicians match service needs?|Compare fleet and maintenance records.
field_safety_case|Rail Transit Safety Evidence|Which hazard analyses, inspections, and oversight findings apply?|Name line, agency, and period.
field_construction_impact|Building a Metro Corridor|Which excavation, emissions, business, and displacement impacts occurred?|Compare assessment with monitored outcome.
"""

ROADS = """history_origins|A Highway Alignment Chosen|Which travel and political assumptions drove one route?|Trace maps, alternatives, and decision records.
famous_examples|A Widely Cited Road Project|Which measured outcomes followed opening?|Compare promised congestion, safety, and access effects.
hidden_stories|Communities in the Right of Way|Whose homes, businesses, or lands were affected?|Use acquisition records and local accounts.
beginner_explainers|What Makes a Road Work?|How do geometry, pavement, drainage, and operations interact?|Follow one bounded road segment.
advanced_concepts|Safety and Capacity Tradeoffs|How does a design change affect crash severity and throughput?|Use site-calibrated evidence and multiple modes.
mysteries_unsolved_cases|A Crash Pattern without Clear Cause|Which road, traffic, and reporting data would distinguish explanations?|Avoid attributing causation from a map alone.
technology_innovation|A New Pavement or Control System|Did it improve durability, safety, or travel time?|Compare similar sites and maintenance costs.
people_personalities|A Route Decision|Who selected one alternative, and who opposed it?|Use hearings and agency records.
major_events|A Road Opens or Closes|What changes in traffic and access followed?|Use before-and-after counts and diverted routes.
how_it_works|Road from Design to Maintenance|How do traffic estimates, geotechnics, drainage, and upkeep connect?|Follow a project file.
rise_fall|A Highway Replaced|Why was a road removed, bypassed, or rebuilt?|Compare condition, costs, and community effects.
then_vs_now|One Corridor across Time|How did crashes, traffic, and nearby land use change?|Control boundaries, exposure, and reporting changes.
future_developments|A Proposed Road Expansion|What evidence would test its claimed benefits?|Compare alternatives and induced-demand scenarios.
myths_vs_facts|More Lanes End Congestion?|What happened after capacity increased in one corridor?|Measure peak trips and network effects over time.
documentary_stories|A Road Project's Public Record|How did alternatives become the built alignment?|Trace assessment, consultation, contracts, and operation.
system_boundary|Segment or Network?|Which effects move to parallel roads and nearby streets?|Define the network and time period.
input_output_trace|Storm to Road Closure|How does rainfall pass through drainage and affect access?|Use design storm and observed incidents.
design_tradeoff|Speed and Street Access|What did wider lanes or fewer crossings change?|Compare travel, crash severity, and pedestrian access.
failure_mode|A Pavement or Drainage Failure|What evidence explains a documented closure?|Use inspection, weather, and repair records.
testing_limits|Model versus Traffic after Opening|Which demand assumptions failed in real use?|Compare forecast and observed trips by mode.
standards_interoperability|Design Criteria for a Route|Which jurisdictional rules governed one road segment?|Name date, road class, and approved exceptions.
security_threat_model|Road Operations Resilience|Which disruptions are addressed by plans and redundancy?|Discuss public continuity and response evidence.
maintenance_lifecycle|Pavement through Renewal|When did condition data trigger repair or resurfacing?|Use inspections, traffic loading, and cost.
infrastructure_dependencies|Road and Other Utilities|Which drainage, power, signal, and bridge systems constrain operation?|Map a bounded corridor.
accessibility_usability|Crossing the Corridor|Can people with varied mobility reach destinations safely?|Use crossings, bus stops, slopes, and observed behavior.
independent_replication|Recheck a Safety Result|Can an analyst reproduce a reported crash reduction?|Match exposure, period, site selection, and regression effects.
responsible_deployment|Opening a New Road|What monitoring and mitigation followed construction?|Track crashes, noise, air, and access.
field_route_capacity|Corridor at Peak Demand|What bottleneck determines actual throughput?|Use observed flows, intersections, and spillback.
field_vehicle_design|Road Design for Actual Users|Which vehicles and nonmotor users can fit the geometry?|Check design vehicle, turns, and safe crossings.
field_maintenance_system|Maintaining a Highway|Do crews, materials, and closures support required upkeep?|Use agency service and condition records.
field_safety_case|Safety Claim for a Road Change|What data support expected and observed crash outcomes?|Use calibrated methods and severity, not counts alone.
field_construction_impact|Road Project Footprint|Which land, materials, emissions, and neighborhood effects occurred?|Set build and operating boundaries.
"""


if __name__ == "__main__":
    revise_domain("424", "424_shipbuilding", SHIPS,
                  "Shipbuilding through design, yard labor, construction, stability, sea trials, service, and port dependence.",
                  "dated vessel plans, yard and survey records, IMO instruments, class and flag documentation, sea-trial data, and official investigations",
                  "Name ship type, build or refit date, flag, route, and loading condition. Approval and trials apply to defined conditions, not every voyage.")
    revise_domain("425", "425_metro_systems", METROS,
                  "Metro systems through corridor planning, vehicle and station design, actual service, safety oversight, access, and community effects.",
                  "authority plans and timetables, observed headways and ridership, station access audits, maintenance records, safety-oversight findings, and community testimony",
                  "Name line, agency, city, and period. Separate forecast capacity from delivered service and document whose journeys are included.")
    revise_domain("426", "426_roads_highways", ROADS,
                  "Roads and highways through route decisions, observed safety and access, pavement and drainage, maintenance, and network effects.",
                  "dated agency designs and assessments, traffic and crash data, FHWA safety methods, pavement inspections, contracts, and affected-community accounts",
                  "Name corridor, jurisdiction, design year, exposure, and comparison period. A model prediction is not an observed crash or travel outcome.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
