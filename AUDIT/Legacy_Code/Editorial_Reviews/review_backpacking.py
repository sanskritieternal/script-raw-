"""Editorial question designs for niche 188, Backpacking."""

from review_angle_plans import audit, revise_domain


BACKPACKING = """history_origins|How Backpacking Became an Itinerary|When did carrying one's own kit become a recognizable travel practice?|Compare dated guidebooks, transport networks, equipment, and local work.
famous_examples|A Celebrated Long Route Rechecked|What does one famous backpacking route demand in practice?|Compare publicity with distance, services, access rules, cost, and local accounts.
hidden_stories|The People Supporting Independent Travel|Whose work enables a low-cost backpacking trip?|Trace hosts, transport workers, maintainers, guides, and waste crews.
beginner_explainers|Building a Feasible First Trip|Which constraints should a first-time backpacker resolve before choosing a route?|Bound trip length, budget, permits, weather, skills, transport, and return plan.
advanced_concepts|Weight Versus Resilience|When does a lighter pack reduce safety or increase dependence on services?|Compare equipment function, route exposure, experience, and contingency plans.
mysteries_unsolved_cases|An Itinerary That Failed|Which documented factors caused a planned trip to break down?|Reconstruct decisions, conditions, service availability, and reporting gaps.
technology_innovation|A Gear Change Under Scrutiny|Did one new backpacking product improve performance on a defined trip?|Compare weight, durability, price, repairability, and field evidence.
people_personalities|A Route Builder's Choices|How did one route designer or advocate shape access?|Use dated proposals, land negotiations, design changes, and objections.
major_events|A Closure That Rewrote a Trip|How did one documented closure alter backpackers' routes?|Track official notice, alternatives, local effects, and reopening.
how_it_works|The Logistics of a Multi-day Route|How do food, water, shelter, permits, and transport fit together on one route?|Map each leg and identify services that must be confirmed locally.
rise_fall|The Boom in a Backpacking Corridor|Why did one corridor grow or decline in popularity?|Compare visitor counts, transport, prices, publicity, rules, and survey methods.
then_vs_now|The Same Route in Two Eras|How did the cost and feasibility of one route change?|Compare dated prices, access rules, services, equipment, and visitor mix.
future_developments|Future of One Trail Corridor|Which conditions could reshape a backpacking route?|Test scenarios for climate, maintenance funding, land use, and transport.
myths_vs_facts|Is Ultralight Always Better?|For which trip conditions does lower pack weight help or hurt?|Define terrain, season, equipment reliability, ability, and evidence quality.
documentary_stories|A Trip Reconstructed from Records|What did travelers actually encounter on one documented journey?|Use itinerary, permits, dated weather, maps, and consented accounts.
map_vs_ground|Distance Is Not Difficulty|Which ground conditions make a mapped backpacking leg harder?|Compare ascent, surface, exposure, water, shelter, and current closures.
route_choices|The Detour Decision|Why might travelers choose one alternative route?|Compare verified conditions, permits, transport links, skill demands, and time.
seasonality|The Short Safe Window|How does season change the feasibility of one backpacking route?|Check current local conditions, daylight, water, weather, and access dates.
local_voice|A Host Community's Perspective|How do residents experience backpackers on one corridor?|Seek consented accounts and compare spending, crowding, waste, and work.
landscape_process|Why the Route Crosses This Terrain|Which landform or water system shapes one backpacking itinerary?|Use topographic and geologic records alongside field observations.
accessibility|Who Can Backpack This Route?|Which route or service barriers limit participation?|Check transport, trail surface, facilities, equipment cost, and user accounts.
infrastructure|The Services Behind Self-Sufficiency|Which maintained services does an independent trip rely on?|Trace signage, water, shelters, communications, rescue access, and funding.
environmental_pressure|The Footprint of an Overnight Stop|What impacts arise where backpackers camp or lodge?|Measure soil, vegetation, waste, water, and energy use at one site.
safety_decision|When to Cancel a Backpacking Leg|Which current facts should trigger a route change or turnaround?|Use official alerts, weather, daylight, water, group ability, and exit options.
place_history|Before the Backpacking Route|Whose paths or land uses preceded the itinerary?|Use land records, oral histories with consent, and Indigenous sources where relevant.
comparison_of_places|Two Routes, One Traveler Profile|Why is one route feasible for a defined traveler while another is not?|Compare total cost, access, terrain, permits, services, and season.
responsible_access|Visitor Limits on a Popular Route|How do permit limits affect ecosystems and nearby communities?|Compare monitoring, displaced use, equity, and local business effects.
field_trip_budget|The True Cost of One Itinerary|Where do planned and actual backpacking costs diverge?|Include transport, permits, food, accommodation, equipment, and contingency.
field_route_reliability|Can This Itinerary Hold?|Which legs fail most often under real operating conditions?|Check closure history, transport schedules, water reports, and alternatives.
field_local_etiquette|Travel Customs Along One Route|Which visitor behavior do local hosts ask travelers to change?|Use published rules and consented local perspectives without generalizing a culture.
field_accessibility_check|An Access Audit of One Trip|Which stage creates the strongest barrier for a defined traveler?|Check booking, transport, route, lodging, sanitation, and emergency support.
field_environmental_footprint|Counting a Trip's Impacts|Which part of one itinerary drives its measured environmental footprint?|Set system boundaries across transport, lodging, food, gear, and site damage.
"""


if __name__ == "__main__":
    revise_domain("188", "188_backpacking", BACKPACKING,
                  "Backpacking through itinerary design, real costs, route reliability, host communities, access, and ecological impact.",
                  "current land-manager alerts and permit rules, trail and transport records, dated costs, site monitoring, and consented traveler and resident accounts",
                  "Name route, jurisdiction, season, traveler profile, and date. Verify conditions locally before practical travel advice; do not imply a route is safe from historical descriptions or encourage unauthorized access.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
