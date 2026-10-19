"""Editorial question designs for niche 190, Camping."""

from review_angle_plans import audit, revise_domain


CAMPING = """history_origins|How a Campground Was Established|Which policy and land-use change created one campground?|Compare land records, site plans, local objections, and early rules.
famous_examples|A Celebrated Campsite Examined|What does a famous campsite offer and whom can it serve?|Check booking, price, facilities, season, access, and ecological capacity.
hidden_stories|The Labor Behind an Overnight Stay|Whose work makes a campground usable?|Trace hosts, cleaners, maintenance workers, waste teams, and rangers.
beginner_explainers|Planning a First Night Outdoors|Which choices must a first-time camper settle before booking?|Bound site type, weather, shelter, food storage, facilities, and local rules.
advanced_concepts|Campground Capacity and Impact|How can a manager decide how many overnight stays a site can support?|Compare water, toilets, habitat monitoring, staffing, and visitor experience.
mysteries_unsolved_cases|Why a Campground Closed|Which documented causes explain a site closure?|Check hazards, infrastructure, permits, ecological findings, and funding.
technology_innovation|A New Shelter or Stove Tested|Did one camping product improve a defined need?|Compare performance, failure modes, cost, repairability, and conditions.
people_personalities|A Campground Manager's Choice|How did one manager change a site's design or rules?|Use dated plans, public comments, budgets, and results.
major_events|A Fire Season's Effect on Camping|How did a documented fire event change one campground?|Separate temporary restrictions from rebuilding and lasting policy.
how_it_works|How Campsites Are Allocated|How do bookings, permits, and on-site assignment work at one campground?|Track published rules, actual availability, fees, and exceptions.
rise_fall|The Boom in Overnight Stays|Why did one campground's use change over time?|Compare occupancy, pricing, transport, promotion, closure, and data methods.
then_vs_now|Camping at One Site Across Generations|How have facilities, costs, and rules changed at one campground?|Use dated fee schedules, plans, visitor data, and site records.
future_developments|A Campground's Climate Choices|Which site changes might reduce future heat, flood, or fire exposure?|Specify hazard assumptions, costs, accessibility, and ecological trade-offs.
myths_vs_facts|Is a Campfire Always Part of Camping?|How do fire rules and impacts differ across camping sites?|Check local restrictions, fuel demand, air quality, wildfire risk, and alternatives.
documentary_stories|A Campsite Decision Reconstructed|What happened when one documented camp had to change plans?|Use official alerts and consented accounts with dated decisions.
map_vs_ground|A Campground Map Versus Reality|Which physical barriers or services are missing from a booking map?|Check site grade, distance to facilities, shade, drainage, and actual access.
route_choices|Getting to the Campsite|Why does one access route work better for a defined camper?|Compare transport, road or trail conditions, luggage, time, and alternatives.
seasonality|When a Campsite Is Actually Available|How do season and weather affect usable camping days?|Compare opening dates, closures, temperature, water, and daylight.
local_voice|Neighbors of a Campground|How do residents describe overnight visitor activity?|Seek consented accounts and compare employment, traffic, noise, and resource use.
landscape_process|Why This Site Floods or Dries|Which landscape process shapes a campground's risks?|Use drainage, soil, vegetation, water records, and site design.
accessibility|Can Different Campers Use This Site?|Where are the barriers from booking to sleeping?|Check information, transport, parking, surface, toilets, and campsite layout.
infrastructure|What an Overnight Site Needs|How are water, sanitation, waste, power, and maintenance provided?|Trace design capacity, operating costs, inspection, and failures.
environmental_pressure|An Overnight Stay's Site Impact|Which camping practices cause measurable local damage?|Compare soil compaction, waste, wildlife attraction, water, and mitigations.
safety_decision|When to Change a Camping Plan|Which current conditions warrant a different site or date?|Check local alerts, weather, fire rules, food storage requirements, and exits.
place_history|Before the Campground|Whose land and uses preceded a campsite's creation?|Use land records and community sources, including Indigenous accounts where relevant.
comparison_of_places|Two Sites for One Camping Group|Why is one campground more suitable for a defined group's needs?|Compare total cost, access, facilities, rules, hazards, and season.
responsible_access|A Campsite Booking Rule's Effects|Who benefits and who is excluded by one allocation system?|Compare demand, cancellation, cost, equity, and site impacts.
field_trip_budget|The Cost of One Night|What does a camping trip cost beyond the campsite fee?|Include transport, equipment, food, fuel, permits, and contingency.
field_route_reliability|Will Camp Access Hold?|What can interrupt travel from home to a booked site?|Check roads, transport, booking status, weather, closures, and fallback.
field_local_etiquette|Shared Space at a Campground|Which behaviors affect neighbors, workers, and wildlife?|Use posted rules, host accounts, noise data, food storage, and waste practices.
field_accessibility_check|Auditing a Campsite Journey|At which step does a defined camper lose usable access?|Check reservation, arrival, site surface, amenities, and emergency information.
field_environmental_footprint|The Footprint of an Overnight Trip|Where do the largest measured impacts arise?|Set boundaries for travel, equipment, energy, water, waste, and habitat.
"""


if __name__ == "__main__":
    revise_domain("190", "190_camping", CAMPING,
                  "Camping through overnight logistics, site design, public access, worker effort, safety, and ecological capacity.",
                  "current campsite rules and alerts, booking and fee records, accessibility and facility information, land and ecological monitoring, and consented host and camper accounts",
                  "Name the site, jurisdiction, season, group needs, and date. Check current fire, food-storage, weather, and access rules locally; avoid implying historic conditions make a campsite safe today.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
