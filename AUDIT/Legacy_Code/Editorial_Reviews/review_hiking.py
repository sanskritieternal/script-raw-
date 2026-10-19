"""Editorial question designs for niche 189, Hiking."""

from review_angle_plans import audit, revise_domain


HIKING = """history_origins|How a Walking Route Became a Trail|When was one path designated for recreation and whose earlier use shaped it?|Compare dated maps, land records, trail plans, and community accounts.
famous_examples|A Famous Hike Beyond the Photograph|What does a celebrated hike require from an ordinary visitor?|Check ascent, exposure, permits, transport, facilities, and access barriers.
hidden_stories|The People Who Maintain a Trail|Whose work keeps a hiking route open?|Trace crews, volunteers, land managers, local residents, and funding.
beginner_explainers|Choosing a First Hike|Which route details matter before a newcomer starts?|Define distance, ascent, surface, weather, daylight, facilities, and return options.
advanced_concepts|Trail Difficulty Is Multidimensional|Why do a route's distance and grade fail to describe its demands?|Compare terrain, exposure, altitude, weather, wayfinding, and group ability.
mysteries_unsolved_cases|A Sudden Trail Closure|Which evidence explains a closure that surprised hikers?|Check official alerts, inspection records, weather, maintenance, and uncertainty.
technology_innovation|Digital Navigation on Trail|Does one navigation tool improve decisions or create new dependence?|Compare map accuracy, battery, coverage, usability, and fallback skill.
people_personalities|A Trail Advocate's Decision|How did one organizer change the route or access rules?|Use proposals, meeting records, opposition, and observed outcome.
major_events|An Event That Changed a Trail|How did a storm, fire, protest, or new rule change one hiking route?|Distinguish immediate closure from lasting design or access change.
how_it_works|How a Trail Is Rated|Who assigns difficulty and what does the rating measure?|Compare agency criteria, site conditions, user needs, and update practices.
rise_fall|When a Trail Became Crowded|What caused a measured change in trail use?|Compare counts, publicity, transport, permits, weather, and recording methods.
then_vs_now|A Trail Across Two Decades|How have a route's condition and access changed?|Use comparable maps, maintenance logs, visitor counts, and dated images.
future_developments|A Trail Under Climate Pressure|What plausible changes could affect a route's safety and upkeep?|State assumptions about heat, rain, erosion, budgets, and use.
myths_vs_facts|The Shortcut That Saves Time?|Does a popular trail shortcut actually improve a hike?|Check legality, measured time, terrain, erosion, and hazard exposure.
documentary_stories|A Hike Reconstructed Carefully|What happened on one documented outing and why?|Use consented accounts, route records, weather, and time-stamped decisions.
map_vs_ground|The Trail Map's Blind Spots|Which current ground conditions are missing from a published route map?|Compare grade, surface, crossing, signage, shade, and closures.
route_choices|Why Hikers Choose a Junction|What factors explain decisions at one trail split?|Check signs, destination, crowding, skill, weather, and route information.
seasonality|One Trail in Different Seasons|How does season change a hike's feasibility?|Use current local alerts alongside historical weather and access patterns.
local_voice|Neighbors of a Popular Trail|How do nearby residents describe the effects of hikers?|Seek consented accounts and compare parking, work, noise, and benefit.
landscape_process|Why the Trail Keeps Eroding|Which physical process changes one trail segment?|Use slope, drainage, soil, vegetation, maintenance, and field measurements.
accessibility|Is This Hiking Route Usable?|Which documented barriers affect walkers with different needs?|Check grade, surface, rest points, transit, facilities, and user accounts.
infrastructure|What Supports a Safe Trail?|Which built and staffed systems make one hike possible?|Trace bridges, signs, water, toilets, inspections, and funding.
environmental_pressure|Footfall and Habitat|What ecological effects are measurable near one trail?|Compare use intensity with soil, vegetation, wildlife, and controls.
safety_decision|When to Turn Around|Which current conditions justify changing a hiking plan?|Check official alerts, weather, daylight, group condition, and exits.
place_history|Before the Hiking Trail|Whose routes, homes, or livelihoods preceded today's trail?|Use historical maps, land records, and community sources with attribution.
comparison_of_places|Two Hikes for One Group|Why is one route a better fit for a defined group's needs?|Compare surface, ascent, access, facilities, exposure, and duration.
responsible_access|A Reservation System's Consequences|Who gains and loses when entry to a trail is rationed?|Compare crowding, ecology, equity, displaced use, and administration.
field_trip_budget|The Full Cost of a Day Hike|Which costs are overlooked in a supposedly free hike?|Count transport, entry, gear, food, time, and accessibility needs.
field_route_reliability|Can a Trail Plan Survive Disruption?|How robust is one hike to closure, weather, or missed transport?|Check current notices, alternate routes, timing, and turnaround points.
field_local_etiquette|Etiquette on a Shared Trail|Which visitor practices matter to local users and land managers?|Use site rules and consented views; avoid presenting one custom as universal.
field_accessibility_check|An Access Audit from Door to Trail|At which stage does one hiker face the strongest barrier?|Check transport, booking, trailhead, surface, restrooms, and information.
field_environmental_footprint|The Impact of One Hiking Trip|Which stage of a visit produces the largest measured impact?|Set boundaries for transport, equipment, waste, and site damage.
"""


if __name__ == "__main__":
    revise_domain("189", "189_hiking", HIKING,
                  "Hiking through route conditions, access, trail work, navigation, visitor decisions, and ecological effects.",
                  "current land-manager notices, trail maps and inspections, visitor counts, weather records, accessibility details, ecological monitoring, and consented local accounts",
                  "Name the trail, jurisdiction, season, visitor profile, and date. Verify current conditions with the responsible land manager before practical route or safety guidance; avoid declaring any trail safe for every hiker.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
