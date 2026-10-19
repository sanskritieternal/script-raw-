"""Editorial question review for the motorcycle niche."""

from review_angle_plans import audit, revise_domain


MOTORCYCLES = """history_origins|Motorcycles as Everyday Transport|How did motorcycles become a common way to travel in one place?|Use dated registration, price, road, and transit records.
famous_examples|A Motorcycle Design That Spread|Which feature of one influential model was adopted elsewhere?|Compare dated specifications, patents, production, and user needs.
hidden_stories|The Mechanics Behind a Riding Culture|Whose repair and maintenance work keeps a motorcycle community moving?|Follow shops, training, parts access, and attributed worker accounts.
beginner_explainers|What Makes a Motorcycle Roadworthy?|Which documented checks and legal requirements apply to one model?|Identify jurisdiction, model, service guidance, and qualified inspection.
advanced_concepts|Risk per Trip or per Distance?|How does exposure change a comparison of motorcycle crash risk?|Distinguish trips, distance, riders, road types, and reporting gaps.
mysteries_unsolved_cases|Why a Crash Pattern Persists|Which causes of repeated crashes at one location are supported by evidence?|Examine traffic exposure, road design, records, and uncertainty.
technology_innovation|A Rider Assistance Feature Tested|What does one motorcycle safety feature do in real conditions?|Compare design intent, controlled testing, failure limits, and uptake.
people_personalities|A Rider's Daily Work|How do a delivery rider's schedules and pay shape road exposure?|Use consented interviews, platform terms, routes, and safety records.
major_events|A Helmet Rule and Its Aftermath|What changed after a documented helmet policy in one jurisdiction?|Compare implementation, compliance, injury data, and other changes.
how_it_works|From Throttle to Rear Wheel|How does one motorcycle powertrain deliver controlled motion?|Use one model's service diagram and avoid hands-on hazardous procedures.
rise_fall|Why a Motorcycle Model Left the Market|Which factors ended one model's production or sales?|Compare demand, emissions rules, service costs, and replacements.
then_vs_now|One Commute on Two Wheels Across Time|How did cost, road conditions, and protective equipment change?|Use comparable routes, dated vehicle records, rules, and prices.
future_developments|An Electric Motorcycle in Daily Service|Which use cases can one electric model meet today?|Test range, charging, payload, lifecycle cost, and repair access.
myths_vs_facts|A Common Helmet Claim Checked|What does a named safety claim about helmets actually show?|Use applicable standards, crash evidence, and stated limits.
documentary_stories|A Trip Through a Motorcycle City|What does one regular journey reveal about access and road risk?|Document route, rider choices, traffic mix, and consented experience.
map_vs_ground|The Road Map and the Riding Surface|Does a mapped motorcycle route match its real condition?|Verify pavement, junctions, closures, fuel or charging, and current restrictions.
route_choices|Two Routes for One Motorcycle Trip|How do two legal routes compare for a defined rider?|Compare time, road type, exposure, surface, services, and weather.
seasonality|Riding Through the Rainy Season|Which seasonal changes alter motorcycle travel in one region?|Check weather records, drainage, visibility, crash data, and alternatives.
local_voice|Who Shapes Motorcycle Policy?|How do riders, residents, and road officials describe one proposed rule?|Compare public consultation, diverse attributed accounts, and evidence.
landscape_process|A Mountain Road on Two Wheels|How do terrain and weather shape road design and motorcycle use?|Study mapped gradient, drainage, maintenance, and incident records.
accessibility|Who Can Use a Motorcycle Transport Service?|Which physical, cost, and service barriers affect different travelers?|Interview consenting users and examine vehicle, booking, and safety requirements.
infrastructure|A Junction Used by Many Motorcycles|Which design features create or reduce conflicts at one intersection?|Review speeds, sightlines, turning flows, traffic mix, and crashes.
environmental_pressure|A Motorcycle's Full Emissions Picture|How do fuel, electricity, manufacture, and use affect one comparison?|Choose a defined model, use pattern, grid, and lifecycle boundary.
safety_decision|A Route Decision Before Departure|Which current conditions should change a planned motorcycle journey?|Compare weather, road condition, legal access, and safer travel options.
place_history|A Workshop District's Motorcycle History|How did a local repair and parts economy develop?|Trace business records, land use, apprenticeships, and worker accounts.
comparison_of_places|Motorcycles in Two Transport Systems|Why do powered two-wheelers serve different roles in two cities?|Compare affordability, transit, road design, trip length, and data definitions.
responsible_access|Riding Near Homes and Shared Spaces|How are noise, speed, parking, and access managed in one area?|Check current local rules, enforcement, resident impacts, and rider needs.
field_training_method|What a Rider Course Can Demonstrate|How is one training program designed and evaluated?|Review curriculum, qualifications, access, outcomes, and evidence limits.
field_equipment_design|How a Helmet Is Evaluated|What does one applicable helmet standard test and leave untested?|Check current jurisdictional standard, fit, certification, and test scope.
field_rules_and_fairness|Who Can Legally Ride?|How do licensing and vehicle rules affect different riders?|Use current local law, fees, training access, enforcement, and exemptions.
field_injury_prevention|A System Response to Rider Injury|Which road and vehicle changes could reduce severe harm in one setting?|Use crash exposure, speed, helmet use, road design, and emergency care evidence.
field_event_logistics|A Motorcycle Gathering's Road Footprint|How is a large ride managed for participants and other road users?|Review permits, route, marshals, emergency plans, and local impacts.
"""


if __name__ == "__main__":
    revise_domain("139", "139_motorcycles", MOTORCYCLES,
                  "Motorcycles as vehicles and transport systems through design, work, cost, infrastructure, access, and road safety.",
                  "dated vehicle and service specifications, registration and traffic exposure data, official crash and road records, current local law, safety standards, and consented rider and worker accounts",
                  "Name vehicle class, model, place, jurisdiction, and date. Keep riding and mechanical hazards at documentary level, use qualified safety sources, and distinguish exposure-adjusted risk from raw crash totals.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
