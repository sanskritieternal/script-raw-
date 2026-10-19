"""Editorial question review for the cycling niche."""

from review_angle_plans import audit, revise_domain


CYCLING = """history_origins|How Cycling Entered a City|When did cycling become ordinary transport in one city?|Compare dated street plans, counts, rules, and firsthand accounts.
famous_examples|A Cycle Route Under Scrutiny|What made one widely cited route usable for different riders?|Trace design, junctions, maintenance, counts, and user experience.
hidden_stories|The People Who Keep a Route Open|Whose work keeps one cycling corridor safe and usable?|Follow cleaners, repair crews, planners, advocates, and riders with consent.
beginner_explainers|Choosing a Bicycle for a Real Trip|Which bicycle and equipment features serve one rider and route?|Specify trip, fit, load, terrain, service access, and budget.
advanced_concepts|Safety Beyond a Painted Lane|How do speeds, junctions, and separation shape risk on one corridor?|Compare design records, exposure, conflicts, and crash data limitations.
mysteries_unsolved_cases|Why a Bike Lane Goes Unused|Which barriers explain low use of one apparently complete route?|Test network gaps, surface, junctions, security, and trip destinations.
technology_innovation|An Electric Bicycle in Daily Use|Which problems does one e-bike design solve, and which remain?|Compare range, charging, weight, repair, cost, and local rules.
people_personalities|The Planner and the Rider|How did different users challenge one cycleway proposal?|Compare attributed planning records with consented rider perspectives.
major_events|A Road Redesign That Changed Cycling|What happened after one street changed its cycling layout?|Compare dated design, travel counts, safety outcomes, and nearby streets.
how_it_works|A Cycling Network, Not One Segment|What makes a route continuous from origin to destination?|Map crossings, detours, parking, transit links, and maintenance.
rise_fall|A Bike Share System's Turning Point|Why did one bike share system expand, shrink, or close?|Examine funding, coverage, upkeep, pricing, and ridership over time.
then_vs_now|The Same Trip by Bicycle Across Decades|How did one commute's time, exposure, and access change?|Use dated maps, street rules, traffic conditions, and comparable trips.
future_developments|A Proposed Cycling Network|Would one planned connection close a real access or safety gap?|Check current design, budget, intersections, predicted users, and alternatives.
myths_vs_facts|Do Cyclists Avoid Bike Lanes?|Does use of one route match a familiar claim about rider behavior?|Compare observation by time, trip purpose, route condition, and user group.
documentary_stories|One Journey Across a Fragmented Network|Where does a rider's trip become difficult and why?|Document the full route with consent and verify each infrastructure claim.
map_vs_ground|The Mapped Route and Its Surface|Does a mapped cycling route match conditions on the ground?|Check continuous access, surface, crossings, closures, and signage.
route_choices|Two Routes to the Same Destination|How do two bicycle routes differ for a defined rider?|Compare distance, junctions, traffic exposure, gradient, and arrival facilities.
seasonality|Cycling Through a Changing Year|Which seasonal conditions alter one route's usability?|Examine daylight, weather, drainage, maintenance, and travel counts.
local_voice|Who Benefits from a New Cycleway?|How do residents and regular users describe one route change?|Seek varied consented accounts and compare them with measured outcomes.
landscape_process|The Terrain Behind a Cycling Route|How do slope, water, or wind shape one path's design and use?|Relate mapped terrain to construction choices and documented conditions.
accessibility|Cycling With Different Mobility Needs|Which design details help or exclude users of adapted cycles?|Check widths, barriers, turning space, parking, and user testimony.
infrastructure|A Junction as the Critical Link|How does one intersection affect an otherwise connected cycle route?|Review signals, turning conflicts, sightlines, speeds, and observed use.
environmental_pressure|When a Popular Trail Wears Down|How does cycling use affect one shared path and its surroundings?|Measure erosion, crowding, maintenance, and alternatives without assuming cause.
safety_decision|A Safer Route Choice Under Uncertainty|What information helps compare risk across two routes?|Use current conditions, traffic exposure, junctions, and official guidance.
place_history|A Former Rail Line Becomes a Cycleway|How did one transport corridor change use and public access?|Trace ownership, construction, community decisions, and present constraints.
comparison_of_places|Why Cycling Works Differently in Two Cities|Which network and policy differences explain different outcomes?|Use comparable counts, definitions, land use, weather, and street design.
responsible_access|Sharing a Path Fairly|How are pedestrians, cyclists, and other users accommodated on one path?|Inspect width, speed rules, signage, conflicts, and accessibility.
field_training_method|Learning to Cycle in Traffic|What does one training program teach, and how is it evaluated?|Examine curriculum, instructor qualification, participation, and outcome measures.
field_equipment_design|A Helmet or Light's Real Protection|What can one safety product demonstrably do in its intended use?|Check applicable standards, fit or installation, test limits, and maintenance.
field_rules_and_fairness|Rules on a Shared Route|Are cycling rules clear and applied fairly to all route users?|Compare current local law, enforcement records, signage, and user accounts.
field_injury_prevention|Preventing Harm at a Known Conflict Point|Which design changes could reduce severe injury at one location?|Use crash patterns, exposure, speed, near misses, and qualified analysis.
field_event_logistics|A Mass Ride Through Public Streets|How does one organized cycling event manage access and safety?|Review permits, route design, marshals, emergency planning, and affected residents.
"""


if __name__ == "__main__":
    revise_domain("138", "138_bicycles_cycling", CYCLING,
                  "Cycling as transport and recreation through route networks, infrastructure, access, equipment, safety, maintenance, and diverse riders.",
                  "dated street plans and traffic counts, official crash and design records, equipment standards and tests, current local rules, and consented rider and resident accounts",
                  "Name place, route, rider, jurisdiction, and date. Distinguish exposure from crash counts, avoid unsafe riding instruction, and verify current road rules and route conditions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
