"""Editorial questions for personal travel."""

from review_angle_plans import audit, revise_domain


TRAVEL = """history_origins|How a Travel Route Became Popular|Which transport, lodging, and policy changes opened one route to visitors?|Compare dated timetables, prices, local records, and traveler accounts.
famous_examples|A Famous Destination Reexamined|What does one celebrated itinerary offer and what does it omit?|Compare actual access, cost, crowding, resident views, and promotional claims.
hidden_stories|People Who Make Travel Possible|Whose transport, cleaning, guiding, or care work is absent from a trip story?|Use attributed worker accounts and local employment evidence.
beginner_explainers|Planning a Trip as a System|Which dates, documents, transport links, costs, and access needs shape one itinerary?|Use a named route and clearly dated official sources.
advanced_concepts|The Real Cost of a Trip|How do fares, lodging, transfers, fees, time, and contingency affect total cost?|Compare transparent scenarios for a fixed traveler group and travel dates.
mysteries_unsolved_cases|Why a Route Failed in Practice|Which evidence explains a gap between published and actual journey times?|Compare dated schedules, disruption notices, traveler records, and weather.
technology_innovation|A Travel Tool Under Test|Did one booking or navigation tool improve reliability or access?|Compare actual journeys, offline limits, accessibility, privacy, and fees.
people_personalities|A Traveler or Local Guide's Perspective|What can one consented account show about a route?|Pair the narrative with official and local evidence without generalizing.
major_events|A Travel Rule Changes|What changed for visitors and residents after one dated policy or transport event?|Compare official rule, implementation, prices, and local response.
how_it_works|One Journey Door to Door|How do transfers, check-in, border rules, last-mile access, and delays interact?|Map a dated itinerary using official operators and accessible alternatives.
rise_fall|A Destination's Visitor Pattern|Why did visitation to one place rise or fall?|Compare access, prices, policy, marketing, local capacity, and season.
then_vs_now|A Route Across Two Periods|How did travel time, cost, access, and local impact change?|Use equivalent origin, destination, and measures in both periods.
future_developments|A Proposed Travel Link|What evidence would show whether one planned route helps travelers and residents?|Specify demand, affordability, accessibility, emissions, and local costs.
myths_vs_facts|A Travel Tip Checked|Does a viral claim about cheapest time or easiest route hold for defined dates?|Compare official terms and observed prices without a universal promise.
documentary_stories|One Trip Through Its Records|How did a real journey unfold from plan through return?|Use consented account, dated bookings, notices, costs, and changes.
map_vs_ground|A Map and Actual Access|Do mapped distances and routes match what a traveler can use?|Compare current schedules, terrain, closures, and accessibility evidence.
route_choices|Two Ways to Reach One Place|Which route better fits a defined traveler and dates?|Compare full time, cost, reliability, access, and environmental impact.
seasonality|A Destination Across Seasons|How do weather, daylight, services, and crowding change a visit?|Use local climate and operator records for named months.
local_voice|Residents on Visitor Impacts|How do residents describe tourism's benefits and burdens?|Use attributed voices alongside housing, work, and public-service measures.
landscape_process|Why the Route Changes|How do tides, snow, erosion, or heat affect a travel corridor?|Use current official hazard and closure data, not an assumed stable map.
accessibility|A Trip for Different Mobility Needs|Which journey segments create barriers for a defined traveler group?|Verify current operator facilities and first-hand accessibility reports.
infrastructure|What Supports the Visit|Which stations, paths, water, waste, or health services handle visitors?|Compare public capacity and maintenance records without exposing vulnerabilities.
environmental_pressure|A Trip's Measurable Footprint|Which transport and local resource demands arise from one itinerary?|Define system boundary and compare mode, distance, occupancy, and local impacts.
safety_decision|When Plans Need to Change|Which official notices should cause an itinerary to be reconsidered?|Use dated operator and authority updates; avoid situational emergency instructions.
place_history|Before the Destination Brand|What communities and land uses preceded a place's tourism image?|Use local history, land records, and resident voices.
comparison_of_places|Two Destinations Under One Budget|How do two places compare for cost, access, and resident impact?|Use matching dates, traveler needs, exchange assumptions, and sources.
responsible_access|Visiting Without Displacing|Which visitor rules protect a site's meaning and local access?|Check community guidance, permits, capacity, and observed enforcement.
field_trip_budget|A Transparent Trip Budget|What would one dated itinerary cost for a defined traveler group?|List all transport, lodging, fees, taxes, meals, and uncertainty in local currency.
field_route_reliability|A Route's Published Versus Actual Service|How often did one route operate as scheduled in a defined season?|Compare timetable, cancellation, delay, and alternate-service records.
field_local_etiquette|What Hosts Ask of Visitors|Which local expectations are documented by communities and authorities?|Attribute guidance and avoid treating one person's view as universal.
field_accessibility_check|Testing a Travel Claim for Access|Does a claimed accessible itinerary work end to end?|Check each segment, current facilities, booking rules, and affected travelers' reports.
field_environmental_footprint|Comparing Two Trip Options|How do two routes differ in travel emissions and destination pressures?|Match dates, distance, occupancy, methods, and local context."""


if __name__ == "__main__":
    revise_domain("074", "074_personal_travel", TRAVEL,
                  "Personal travel through dated itineraries, full trip cost, service reliability, accessibility, safety notices, environmental effects, and local resident perspectives.",
                  "current official operator schedules and terms, border and health authority notices, dated prices, accessibility audits, local capacity and environmental data, and attributed traveler and resident accounts",
                  "Name traveler needs, route, jurisdiction, and travel dates. Verify current entry, health, weather, and operator rules before production; avoid guaranteed prices or safety and respect local visitor restrictions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
