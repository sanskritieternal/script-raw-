"""Editorial question designs for resorts, travel hacks, and travel systems."""

from review_angle_plans import audit, revise_domain


RESORTS = """history_origins|How a Resort Site Was Chosen|Which land, transport, and financing decisions created one resort?|Use dated land, planning, and ownership records.
famous_examples|A Celebrated Resort Rechecked|What does the property actually offer in a specified season?|Compare current services, total price, access, and promotional claims.
hidden_stories|The Workforce Behind Leisure|Whose labor keeps one resort running?|Trace housekeeping, grounds, food, transport, maintenance, and subcontractors.
beginner_explainers|Reading a Resort Offer|What is included in the quoted stay and what costs extra?|Check property, dates, room, meals, activities, fees, and cancellation terms.
advanced_concepts|Capacity and Service Trade-offs|How do occupancy peaks affect staffing and guest experience?|Compare room nights, queues, service hours, and worker schedules.
mysteries_unsolved_cases|Why a Resort Failed|Which documented factors explain a stalled or closed development?|Test finance, demand, access, water, regulation, and incomplete records.
technology_innovation|A Resort Service Tool Tested|Did one booking or room system improve service?|Compare errors, staff workload, accessibility, privacy, and recovery.
people_personalities|A Resort Development Decision|Who authorized a consequential land or design choice?|Use proposals, consent records, objections, and outcomes.
major_events|A Resort During Disruption|How did one event alter guest and worker arrangements?|Use dated property notices, payroll evidence, and local records.
how_it_works|From Reservation to Departure|Which handoffs produce a complete resort stay?|Map booking, transfer, check-in, meals, activities, and checkout.
rise_fall|A Resort's Changing Occupancy|What explains a documented rise or fall in use?|Check seasonality, prices, transport, room supply, and counting.
then_vs_now|One Resort Across Two Periods|How did its scale, labor, amenities, and local effects change?|Use comparable plans, rates, employment, and resource measures.
future_developments|A Resort's Conditional Future|Which factors could alter its operating model?|State climate, water, labor, financing, and demand assumptions.
myths_vs_facts|Is All-Inclusive All-In?|Which exclusions materially change the guest's cost?|Check dated contract for taxes, activities, drinks, transfers, and tips.
documentary_stories|A Day at One Resort|What work and decisions shape a guest day?|Use consented observation without exposing private guest or worker data.
map_vs_ground|Beyond the Resort Map|Which paths, barriers, or nearby places does the site map omit?|Check actual mobility routes, shore or land access, and season.
route_choices|Reaching a Remote Resort|Which transfer option works for a defined traveler?|Compare timetable, full cost, reliability, luggage, and accessibility.
seasonality|The Resort in Two Seasons|What changes in services, price, staffing, and risk?|Use dated offers, weather data, and operating schedules.
local_voice|Neighbors of the Resort|How do residents describe benefits and burdens?|Seek varied accounts and data on jobs, water, roads, and land.
landscape_process|Why This Resort Sits Here|Which coast, slope, water, or habitat conditions shaped its site?|Use physical maps, planning assessments, and dated observations.
accessibility|Can a Guest Use the Whole Resort?|Where do booking, transfer, rooms, dining, and activities pose barriers?|Verify features for a defined guest and date.
infrastructure|Utilities Behind a Resort|What water, power, wastewater, and transport systems sustain it?|Trace supply, demand peaks, maintenance, and local sharing.
environmental_pressure|A Resort's Resource Claims|How can water, waste, and energy claims be tested?|Require period, occupancy denominator, geographic boundary, and data.
safety_decision|A Changing Activity Offer|Which current conditions alter an activity plan?|Check operator, site authority, weather, access, and alternatives.
place_history|Land Before the Resort|Who used or held the site before development?|Use land records, historical maps, and affected community accounts.
comparison_of_places|Two Resorts, Different Local Effects|Why do similar properties affect host communities differently?|Compare procurement, jobs, land, water, access, and ownership.
responsible_access|Shared Shores and Trails|Which resort practices affect public access?|Check legal rights, signage, ecological limits, and local priorities.
field_service_handoff|When a Guest Request Moves Teams|Where do booking, front desk, and activity staff lose information?|Trace a consented case and protect personal data.
field_visitor_flow|The Peak-Hour Bottleneck|Which queue or transfer constrains one resort?|Measure arrivals, staff, capacity, accessibility, and contingency.
field_staff_labor|One Resort Job's Real Conditions|How do hours, housing, and workload compare with the role description?|Use consented accounts, schedules, and applicable labor records.
field_access_and_cost|A Usable Stay's Full Price|What would a defined guest pay and be able to use?|Verify room, transfer, meals, mandatory fees, and activity access.
field_local_impact|Who Captures Resort Spending|How much guest spending stays in the host community?|Trace ownership, purchasing, wages, taxes, and measured burden.
"""

TRAVEL_HACKS = """history_origins|Where a Travel Tip Came From|When and why did one common tactic become popular?|Trace original terms, dated advice, and later rule changes.
famous_examples|A Viral Travel Hack Tested|Does a widely shared tip work for a defined itinerary?|Compare total cost, restrictions, failure risk, and source date.
hidden_stories|The Cost Shift Behind a Tip|Who bears work or loss when a traveler saves money?|Trace staff, provider, local business, and other customers.
beginner_explainers|Checking a Travel Tip|What must a traveler verify before trying a tactic?|Name jurisdiction, provider, date, contract, accessibility, and backup.
advanced_concepts|Expected Value of a Booking Tactic|When does an apparent saving survive risk and fees?|Model probability, penalties, time, changes, and traveler preferences.
mysteries_unsolved_cases|Why a Tip Sometimes Fails|Which terms or data gaps explain mixed outcomes?|Compare provider policy, inventory, dates, and anecdotal selection bias.
technology_innovation|A Fare Alert Audited|Does an alert find usable savings for a specific trip?|Compare all-in fares, timing, data coverage, privacy, and false alerts.
people_personalities|The Source of a Travel Tip|How did one advisor or company popularize a tactic?|Trace dated claims, incentives, corrections, and outcomes.
major_events|When a Rule Changed a Hack|How did one documented policy change affect a tactic?|Compare rule text and applicable travel dates before and after.
how_it_works|From Tip to Completed Trip|What steps must work for a booking tactic to succeed?|Trace search, purchase, documentation, journey, and remedies.
rise_fall|Why a Tip Lost Value|What market or rule change made a tactic less useful?|Check price dispersion, fees, inventory, and provider terms.
then_vs_now|One Tip Across Two Booking Eras|Does an older saving still exist?|Compare all-in offers and rules using matched trips and dates.
future_developments|A Tactic Under New Conditions|What changes would make it useful or obsolete?|State pricing, distribution, regulation, and traveler assumptions.
myths_vs_facts|Always Book on One Day?|Is a simple timing rule supported for a defined market?|Test comparable routes, booking windows, total prices, and variability.
documentary_stories|A Tip Tried End to End|What happened when a consented traveler used a tactic?|Keep dated screenshots, terms, costs, and outcome without extrapolation.
map_vs_ground|Shortcut Versus Actual Journey|Does a mapped shortcut reduce door-to-door time?|Include transfers, queues, opening hours, access, and walking.
route_choices|Cheap Fare, Expensive Connection|When is a lower fare a worse complete itinerary?|Compare total price, delay exposure, protected connections, and needs.
seasonality|A Tip by Travel Season|Does it work during peaks and off-peaks alike?|Match destination, lead time, inventory, and service schedule.
local_voice|Local Costs of a Visitor Tip|How do residents and workers view a popular shortcut?|Seek consented accounts and measurable traffic or service effects.
landscape_process|Terrain Limits a Shortcut|Which physical barrier defeats an apparent route hack?|Check grades, water, weather, and actual legal access.
accessibility|Can a Traveler Use This Hack?|Does the tactic preserve required assistance and facilities?|Check each provider and connection for a defined need.
infrastructure|Hidden Dependency in a Tip|Which platform, transfer, or payment system must work?|Map failure points, offline alternatives, and support.
environmental_pressure|Savings Versus Extra Travel|Does a cheaper tactic add emissions or resource use?|Compare complete routes, occupancy, and repeated trips.
safety_decision|When to Reject a Shortcut|Which current condition makes a tactic unsuitable?|Check official notices, provider terms, daylight, and alternatives.
place_history|Why This Shortcut Exists|Which old road or service pattern created the option?|Use maps, planning records, and community history.
comparison_of_places|A Tip in Two Destinations|Why does the same tactic differ across places?|Compare rules, prices, transit, access, and local impacts.
responsible_access|An Ethical Travel Saving|Can the saving respect legal access and local services?|Check property rights, provider terms, worker burden, and resident priorities.
field_trip_budget|The Net Saving|How much remains after every required expense?|Include fees, transfers, time, baggage, changes, and failure contingency.
field_route_reliability|Probability of Making the Plan|What evidence supports a claimed connection or shortcut?|Use dated performance, buffers, and fallback cost.
field_local_etiquette|A Tip Meets Local Norms|Which provider or community practices should a visitor check?|Use current posted rules and local voices without stereotyping.
field_accessibility_check|The Hack's Access Chain|Where might an accessible itinerary break?|Check booking, vehicles, transfers, entrances, and recovery.
field_environmental_footprint|Total Impact of a Saving|Does a cheaper itinerary shift environmental burden?|Match destinations and passengers; include extra legs and lodging.
"""

TRAVEL_SYSTEMS = """history_origins|How a Travel Network Formed|Which decisions connected transport, lodging, and booking in one region?|Use dated plans, contracts, and service maps.
famous_examples|A Network That Seems Seamless|Where does a celebrated travel system still require handoffs?|Test booking, transfers, payments, access, and disruption.
hidden_stories|Workers in the Handoffs|Whose labor repairs gaps between providers?|Trace dispatch, station, call center, cleaning, and frontline roles.
beginner_explainers|A Trip as a System|Which organizations must coordinate for a complete journey?|Map booking, transport, border, lodging, and destination services.
advanced_concepts|Cascading Delay|How does one failed leg affect the rest of an itinerary?|Model timetable, buffer, liability, inventory, and alternatives.
mysteries_unsolved_cases|Why an Integration Failed|Which documented technical or institutional gap blocked coordination?|Compare data formats, incentives, funding, and governance.
technology_innovation|One Travel Platform Tested|Did integration reduce traveler effort or merely move it?|Measure errors, time, support burden, access, and privacy.
people_personalities|A Network Coordination Decision|Who set the rules for one cross-provider service?|Use board records, contracts, public input, and outcomes.
major_events|System Stress During Disruption|How did one documented event expose network dependencies?|Trace dated outages, responses, and traveler effects.
how_it_works|From Search to Return|How do reservation, ticket, transfer, stay, and refund systems interact?|Draw one real journey with provider boundaries.
rise_fall|A System's Use Over Time|What explains measured growth or decline?|Separate passengers, trips, bookings, and changing definitions.
then_vs_now|Before and After Integration|Did a new common ticket or platform improve a journey?|Compare matched trips, costs, time, and failure handling.
future_developments|Possible Travel Network Changes|Which assumptions would improve or weaken integration?|State investment, interoperability, labor, and policy conditions.
myths_vs_facts|Is One-Click Travel Seamless?|Which obligations still fall on the traveler?|Check separate contracts, transfers, bags, visas, and refunds.
documentary_stories|One Journey Across Providers|What happened at each handoff of a documented trip?|Use consented records and dated provider messages.
map_vs_ground|Network Diagram Versus Walkable Route|What physical transfer does a schematic hide?|Check actual distance, steps, wayfinding, and time.
route_choices|Two Network Paths|Which complete itinerary works for a defined traveler?|Compare total cost, reliability, rights, and access.
seasonality|Seasonal Stress on a Network|Which connection fails or changes at peak demand?|Use dated schedules, occupancy, and disruption data.
local_voice|People Living with the Network|How do residents and workers experience visitor flows?|Compare access, jobs, crowding, and public cost.
landscape_process|Geography of a Network Gap|Which terrain or climate feature shapes a missing link?|Use physical maps and infrastructure history.
accessibility|End-to-End System Access|Where does a nominally accessible leg fail as a whole?|Test booking, transfers, vehicles, rooms, and assistance.
infrastructure|The Shared Backbone|Which power, data, station, road, or payment systems connect providers?|Trace ownership, capacity, maintenance, and outages.
environmental_pressure|Whole-Journey Impacts|Where does a network shift environmental burden?|Use complete itinerary, occupancy, energy, and infrastructure boundary.
safety_decision|Current Network Disruption|Which live sources inform a changed itinerary?|Check official operator and authority notices by date and route.
place_history|Earlier Routes and Networks|What path or service preceded today's travel system?|Use maps, timetables, land records, and community accounts.
comparison_of_places|Two Regions' Travel Integration|Why can one region offer easier transfers?|Compare governance, funding, density, access, and pricing.
responsible_access|Visitors and Resident Services|When does tourism demand strain a shared network?|Test service capacity, local access, cost, and policy choices.
field_service_handoff|A Booking Across Providers|Where can customer information or responsibility be lost?|Trace one consented case and contract boundaries.
field_visitor_flow|The Transfer Bottleneck|What limits throughput at one node?|Measure arrivals, queue, staffing, capacity, and accessible routes.
field_staff_labor|The Human Backup System|How do workers manage exceptions when systems fail?|Use consented accounts, staffing, training, and escalation rules.
field_access_and_cost|The Complete Journey's Price|What must a defined traveler pay for usable access?|Include mandatory fees, transfers, assistance, changes, and lodging.
field_local_impact|Network Benefits and Burdens|Who gains from visitor movement and who pays for it?|Trace revenue, employment, crowding, public costs, and resident access.
"""


if __name__ == "__main__":
    revise_domain("231", "231_resorts", RESORTS,
                  "Named resort properties as land, labor, service, and resource systems across seasons.",
                  "dated property offers and contracts, land and planning records, measured resource use, and consented guest, worker, and resident accounts",
                  "Name property, jurisdiction, and season. Verify current price, access, activity conditions, and legal rights; protect guest and worker privacy.")
    revise_domain("232", "232_travel_hacks", TRAVEL_HACKS,
                  "Specific travel tactics tested against complete trip costs, provider terms, failure risk, access, and local effects.",
                  "dated provider terms and all-in offers, official consumer guidance, matched itinerary comparisons, performance data, and consented traveler accounts",
                  "Name provider, jurisdiction, booking and travel dates, and traveler needs. A tactic is a research candidate, not a current saving or entitlement.")
    revise_domain("233", "233_travel_systems", TRAVEL_SYSTEMS,
                  "Complete journeys across provider, infrastructure, booking, payment, and service handoffs.",
                  "dated schedules and service maps, provider contracts, accessibility information, disruption records, governance documents, and consented traveler and worker accounts",
                  "Name network, route, date, and traveler needs. Verify live service and each provider's terms before describing usable connections or rights.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
