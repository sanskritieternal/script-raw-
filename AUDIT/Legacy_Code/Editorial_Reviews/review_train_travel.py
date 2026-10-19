"""Editorial question designs for niche 227, Train Travel."""

from review_angle_plans import audit, revise_domain


TRAIN_TRAVEL = """history_origins|How One Rail Journey Emerged|Which infrastructure and service decisions created a route?|Use dated timetables, route maps, plans, and community records.
famous_examples|A Celebrated Train Journey Rechecked|What does a famous rail itinerary actually offer?|Compare current schedule, fare, access, connections, scenery, and disruption.
hidden_stories|The Workers Behind a Train Trip|Whose work keeps one journey running?|Trace drivers, dispatchers, station staff, maintenance, cleaning, and catering.
beginner_explainers|Planning a Complete Rail Trip|Which booking and connection details matter first?|Check operator, date, ticket terms, transfers, accessibility, and last mile.
advanced_concepts|Reliability of a Multi-Leg Trip|How do delays and connection rules affect arrival probability?|Use observed punctuality, buffer times, missed connections, and assistance.
mysteries_unsolved_cases|Why a Route Was Delayed|Which documented factors explain recurring disruption?|Test timetable, infrastructure, weather, rolling stock, and data definitions.
technology_innovation|A Rail Travel Tool Evaluated|Did one app or ticket system improve a defined journey?|Compare accessibility, price transparency, errors, privacy, and offline options.
people_personalities|A Service Decision|How did one named operator or community campaign change a train route?|Use proposals, public input, schedules, costs, and outcomes.
major_events|A Closure That Changed Travel|How did one documented line closure affect passengers and towns?|Trace replacement services, travel time, cost, access, and reopening.
how_it_works|From Booking to Arrival|How do ticket, station, platform, train, connection, and last mile fit together?|Map one itinerary with current operator rules.
rise_fall|A Route's Passenger Trend|What explains a measured change in ridership?|Check service frequency, fares, population, disruptions, and counting.
then_vs_now|One Rail Corridor Across Eras|How did journey time, fare, access, and service change?|Use comparable timetables, currency context, stations, and boundaries.
future_developments|Scenarios for a Rail Route|Which conditions could alter service?|State infrastructure, energy, demand, funding, and timetable assumptions.
myths_vs_facts|Train Is Always the Cheapest?|When does a full rail itinerary cost more or less?|Include fare, booking time, transfers, last mile, luggage, and delays.
documentary_stories|A Journey Through One Disruption|What happened when a documented train trip was interrupted?|Use operator notices, passenger consent, and time-stamped records.
map_vs_ground|A Network Map's Blind Spots|Which transfer, step, outage, or walking distance is omitted?|Check current station and platform information on site.
route_choices|Two Rail Itineraries Compared|Why might a traveler choose a slower or longer route?|Compare full door-to-door time, cost, reliability, accessibility, and preferences.
seasonality|Rail Travel Across Seasons|How do holidays, weather, and maintenance change one route?|Use current timetables and dated service data.
local_voice|Towns Along the Line|How do residents and workers describe a rail service change?|Seek varied consented accounts and compare access and livelihood effects.
landscape_process|Why the Railway Follows This Terrain|Which river, pass, coast, or geology shaped the alignment?|Use engineering maps and physical geography.
accessibility|Can a Defined Traveler Complete This Trip?|Which barriers appear at booking, stations, transfers, and arrival?|Verify actual assistance, lifts, platform gap, information, and alternatives.
infrastructure|What Keeps a Line Running?|Which track, signaling, power, station, and workforce systems matter?|Trace maintenance, failures, capacity, and funding.
environmental_pressure|The Footprint of One Rail Trip|What emissions and land impacts belong in a comparison?|Set boundary for electricity source, occupancy, access trips, and infrastructure.
safety_decision|Current Rail Travel Information|Which operator updates matter before and during a trip?|Check disruption, platform, weather, assistance, and connection protections.
place_history|Before the Railway Station|What settlement and land use preceded a line?|Use maps, land records, and local history including displacement.
comparison_of_places|Two Towns, Different Rail Access|Why does service benefit them differently?|Compare frequency, fares, station distance, accessibility, and population need.
responsible_access|A New Rail Service's Trade-offs|Who gains and loses from a route or station change?|Compare access, noise, land take, cost, housing, and environment.
field_trip_budget|The True Cost of One Train Journey|Where do advertised and actual costs diverge?|Include fees, local transport, meals, baggage, changes, and missed connections.
field_route_reliability|Can This Connection Be Trusted?|How often would a defined transfer work?|Use observed arrival data, timetable buffer, station layout, and alternatives.
field_local_etiquette|Shared Space on One Rail System|Which passenger practices do operators and local users expect?|Use current rules and consented perspectives without cultural generalization.
field_accessibility_check|An End-to-End Rail Access Audit|At which stage does an assistance plan fail or succeed?|Check booking, station arrival, boarding, transfer, alighting, and last mile.
field_environmental_footprint|Comparing Rail with Another Mode|How does one trip's footprint change with assumptions?|Use matched route, occupancy, power mix, access travel, and system boundary.
"""


if __name__ == "__main__":
    revise_domain("227", "227_train_travel", TRAIN_TRAVEL,
                  "Train travel through complete itineraries, timetable reliability, true cost, station access, workforce, and environmental comparisons.",
                  "current operator timetables and fare rules, dated punctuality and ridership data, station accessibility and assistance reports, infrastructure records, and consented passenger and worker accounts",
                  "Name route, operator, travel date, passenger needs, and currency. Verify current timetable and assistance with the operator; do not infer an accessible complete trip from one accessible train or station.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
