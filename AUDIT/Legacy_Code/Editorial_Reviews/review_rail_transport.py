"""Niche-specific rail and multimodal transport editorial reviews."""

from review_angle_plans import audit, revise_domain


RAIL = """history_origins|Why This Railway Was Built|Which needs and interests shaped one rail line's original route?|Compare plans, finance, land acquisition, and affected communities.
famous_examples|A Celebrated Rail System Tested|Which measurable outcomes make one railway a model?|Compare capacity, reliability, access, cost, and safety on equal terms.
hidden_stories|Who Maintains the Railway?|Whose inspection, cleaning, dispatch, and repair work is absent from travel stories?|Use role descriptions, staffing data, and attributed worker accounts.
beginner_explainers|A Train's Trip Through the Network|What must happen before and during one scheduled train movement?|Map track availability, signaling, power, stations, crew, and control at a high level.
advanced_concepts|Capacity Versus Reliability|Why can adding a train reduce schedule resilience on a busy corridor?|Compare headways, dwell times, junction conflicts, and recovery margin.
mysteries_unsolved_cases|Why Did the Timetable Fail?|Which evidence best explains repeated delay on one line?|Compare actual movement logs, infrastructure, rolling stock, and weather.
technology_innovation|A Signaling Upgrade in Practice|Did a new signaling system improve capacity or reliability?|Compare before-and-after results, transition costs, and operating constraints.
people_personalities|A Railway Decision Maker|Who chose one route, station, or service pattern, and who opposed it?|Use dated decisions and affected passenger and landholder accounts.
major_events|After a Rail Disruption|What changed in operations and oversight after one documented incident?|Trace official investigation, recommendations, implementation, and remaining gaps.
how_it_works|How a Railway Stays Safe|Which layers prevent one identified operational hazard?|Explain governance, training, equipment, inspection, and response without exploitable detail.
rise_fall|A Line's Closure or Return|Why did one passenger or freight service end or reopen?|Compare demand, finances, policy, maintenance, and community effects.
then_vs_now|One Corridor Across Eras|How did journey time, frequency, access, and cost change?|Use comparable endpoints, published timetables, and price basis.
future_developments|A Proposed Rail Extension|What evidence would justify extending service to one place?|Assess demand, capital and operating costs, land effects, access, and alternatives.
myths_vs_facts|The Fastest Train Claim|Does a speed headline describe typical end-to-end passenger travel?|Compare scheduled time, stops, transfers, reliability, and measurement date.
documentary_stories|From Rail Proposal to Opening|How did one project change from initial case to actual service?|Build a timeline of design, approvals, costs, construction, and outcomes.
system_boundary|What Counts as Rail Performance?|Does a line-level metric include stations, transfers, and access?|Set system boundary from home-to-destination, not train motion alone.
input_output_trace|Where the Delay Accumulated|At which part of a journey did actual time depart from the timetable?|Use timestamped dispatch and passenger evidence without exposing sensitive systems.
design_tradeoff|Frequent Stops or Faster Trips|How did one stopping pattern trade local access against through-travel time?|Compare riders, dwell, capacity, and alternative service patterns.
failure_mode|A Known Fault and Its Safeguards|What public investigation shows how a railway failure was contained?|Use official findings at a non-operational level and avoid bypass instructions.
testing_limits|The Trial Run Versus Daily Service|What did a rail test prove, and what remained untested?|Compare conditions, duration, passenger load, and safety approval.
standards_interoperability|Crossing a Network Boundary|What prevents a train or ticket from working on another network?|Compare track, signaling, power, platform, and fare standards.
security_threat_model|Protecting Rail Service|How does an operator balance open public access with system security?|Use public policy and outcome data without mapping vulnerabilities.
maintenance_lifecycle|Keeping Track Fit for Service|How do inspection and renewal decisions affect outages and safety?|Examine public maintenance plans, backlogs, work windows, and trends.
infrastructure_dependencies|When Rail Depends on Other Systems|How do power, roads, drainage, and telecoms affect one service?|Trace a documented interruption and the responsible interfaces.
accessibility_usability|Can Everyone Make the Transfer?|Where does one passenger route fail a defined accessibility need?|Audit signage, step-free paths, timing, information, and user experience.
independent_replication|Can Another City Copy the Line?|Which local conditions limit transfer of one railway success?|Compare density, geography, costs, governance, and demand.
responsible_deployment|Opening a New Rail Service|What evidence shows operational readiness before public launch?|Review independent assessment, training, emergency planning, and monitoring.
field_route_capacity|A Junction as Bottleneck|How does a public timetable reveal capacity constraints at one junction?|Compare scheduled movements and delays without operationally sensitive detail.
field_vehicle_design|Train Design and Passenger Use|How does one vehicle layout affect boarding, capacity, and accessibility?|Compare measured dwell, seating, mobility access, and user reports.
field_maintenance_system|A Renewal Program's Results|Did a track or fleet renewal reduce failures over time?|Compare assets, faults, spending, and service disruption.
field_safety_case|Reading a Rail Safety Decision|What evidence supported approval of one infrastructure change?|Use public risk assessment and regulator records, noting withheld details.
field_construction_impact|The Line Through a Community|Who bore land, noise, or access costs of one rail project?|Compare impact assessment, mitigation, and observed local effects."""


TRANSPORT = """history_origins|Why a Transport Route Emerged|Which travel needs and power relations shaped one road, waterway, or service?|Compare dated plans, land use, costs, and community accounts.
famous_examples|A Model Mobility Project Tested|Does a celebrated transport project improve access for intended users?|Compare door-to-door time, cost, safety, and affected groups.
hidden_stories|Workers Behind Everyday Mobility|Whose driving, repair, dispatch, cleaning, and care work makes trips possible?|Use staffing data and attributed worker accounts across modes.
beginner_explainers|From Origin to Destination|What stages make up one person's real trip?|Include walking, waiting, payment, transfers, and last-mile access.
advanced_concepts|Mobility Versus Accessibility|Does moving vehicles faster help people reach jobs and services?|Compare destinations reachable within time and cost limits.
mysteries_unsolved_cases|Why Did Travel Time Rise?|Which causes explain congestion or delay on one corridor?|Compare demand, incidents, road works, weather, and measurement changes.
technology_innovation|A New Mobility App|Did an app improve access or simply shift costs and data risk?|Compare actual trip outcomes, exclusion, privacy, and worker effects.
people_personalities|The People Who Designed a Route|Who shaped one transport decision, and whose needs were overlooked?|Use planning records and affected traveler testimony.
major_events|Transport During a Shock|How did one flood, strike, or closure change access to essential destinations?|Track service alternatives, costs, safety, and recovery by group.
how_it_works|Who Coordinates a Transport Network?|How do operators, infrastructure owners, regulators, and users interact?|Map one journey's responsibilities and points of failure.
rise_fall|A Service That Disappeared|Why did one route or mode lose service?|Compare ridership, funding, land use, regulation, and alternatives.
then_vs_now|One Commute Across Time|How did duration, cost, reliability, and safety change?|Use matched origins, destinations, times, and traveler groups.
future_developments|Choosing a New Mobility Investment|What evidence should decide among road, transit, walking, and cycling options?|Compare access, safety, cost, emissions, and maintenance over a defined horizon.
myths_vs_facts|Does a New Lane End Congestion?|Did a road expansion deliver the promised time savings?|Compare traffic, induced trips, travel-time distribution, and alternatives.
documentary_stories|A Transport Plan's Real Outcome|How did one project move from forecast to daily use?|Track funding, design revisions, opening, measured access, and complaints.
system_boundary|What Is a Successful Trip?|Does a transport metric include access, waiting, and transfer time?|Define the whole journey and relevant travelers before comparison.
input_output_trace|Where Time Is Spent|Which trip stage accounts for delay or unreliability?|Use timestamped journeys and clear sampling across users.
design_tradeoff|Road Space for Competing Needs|How does one street design balance buses, freight, walking, cycling, and cars?|Compare throughput, safety, access, and local business effects.
failure_mode|When a Service Breaks Down|How did a documented transport disruption affect different travelers?|Use public incident reports and recovery evidence, not exploitable details.
testing_limits|A Pilot Is Not a Citywide Result|What did one transport pilot actually measure?|Check duration, season, sample, selection, and displaced trips.
standards_interoperability|One Ticket, Several Systems|What prevents a traveler from making a seamless multimodal trip?|Compare fares, schedules, physical transfer, payment, and information.
security_threat_model|Safe and Open Mobility|How do operators protect travelers while keeping services accessible?|Use public policy, privacy safeguards, and aggregate outcomes.
maintenance_lifecycle|The Cost of Keeping Routes Open|How do upkeep choices affect reliability, access, and long-term cost?|Compare public budgets, asset condition, outages, and deferred work.
infrastructure_dependencies|A Journey Depends on More Than Vehicles|Which crossings, sidewalks, power, or drainage make one route usable?|Trace a real trip and a documented infrastructure gap.
accessibility_usability|A Journey With Access Needs|Can a defined traveler complete one trip independently?|Audit vehicles, stops, information, transfers, and fallback options with users.
independent_replication|Can a Transport Fix Travel?|Which local conditions affect whether another city can copy a success?|Compare density, street layout, governance, budget, and needs.
responsible_deployment|Launching a Mobility Service|What should be measured before and after a new service opens?|Set safety, access, worker, equity, and performance indicators.
field_route_capacity|A Corridor's Real Capacity|How many people, not vehicles, can one route move reliably?|Compare modes, occupancy, peak timing, and bottlenecks.
field_vehicle_design|Design for Boarding and Use|How does vehicle design affect safety, dwell, comfort, and access?|Compare actual users and service conditions across vehicle types.
field_maintenance_system|A Maintenance Backlog's Effects|Did delayed repairs change service or safety outcomes?|Compare asset condition, work orders, outages, and public reports.
field_safety_case|A Street Safety Intervention|What evidence supports one safety redesign?|Compare crashes, exposure, speeds, and near misses with time context.
field_construction_impact|Who Bears a Transport Project?|Which households and businesses experienced construction burdens?|Compare plans, disruption, compensation, and observed recovery."""


if __name__ == "__main__":
    revise_domain("109", "109_railways_trains", RAIL,
                  "Railway operations, infrastructure, vehicles, passengers, workers, safety governance, and community impacts through named corridors.",
                  "dated timetables and movement data, public regulator and incident reports, engineering and maintenance records, project appraisals, and attributed passenger and worker accounts",
                  "Name railway, corridor, operator, jurisdiction, and date. Verify current safety standards and avoid publishing exploitable operational details or unverified incident causes.")
    revise_domain("110", "110_transportation", TRANSPORT,
                  "Transport across modes as access to destinations, including time, cost, reliability, safety, accessibility, labor, and maintenance.",
                  "dated travel surveys and trip observations, planning and budget records, safety data, current accessibility standards, and attributed traveler and worker accounts",
                  "Name route, traveler group, jurisdiction, and date. Compare door-to-door journeys and safety exposure on equal terms; verify current rules and avoid sensitive vulnerabilities.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
