"""Editorial question designs for niche 223, Pilgrimage Travel."""

from review_angle_plans import audit, revise_domain


PILGRIMAGE = """history_origins|How One Pilgrimage Route Emerged|Which texts, practices, roads, and institutions shaped a route?|Date sources and distinguish tradition from documented travel history.
famous_examples|A Celebrated Pilgrimage Rechecked|What does one famous journey show about practice and logistics?|Specify tradition, route, period, participant, and source limits.
hidden_stories|Labor Along the Pilgrim Route|Whose work makes the journey possible?|Trace hosts, porters, drivers, sanitation crews, volunteers, and officials.
beginner_explainers|Planning a Pilgrimage Respectfully|Which route, registration, ritual, health, and access facts need confirmation?|Use current site-specific authorities and participant-defined purpose.
advanced_concepts|Devotion, Capacity, and Rights|How can a route balance worship, safety, conservation, and local life?|Compare demand, infrastructure, rules, equity, and custodial views.
mysteries_unsolved_cases|A Route History in Dispute|Which evidence supports different accounts of one pilgrimage path?|Attribute texts, inscriptions, maps, oral traditions, and uncertainty.
technology_innovation|Digital Registration on a Route|Did one platform improve access or crowd management?|Compare uptake, outages, privacy, exclusion, and alternative channels.
people_personalities|A Route Organizer's Choice|How did one named custodian or official change pilgrimage practice?|Use dated decisions, participant input, objections, and results.
major_events|A Season Interrupted|How did one documented closure or hazard alter a pilgrimage?|Track notices, alternate arrangements, local effects, and reopening.
how_it_works|One Pilgrimage's Practical Path|How do stages, permissions, lodging, ritual timing, and return fit together?|Map current official requirements without prescribing devotion.
rise_fall|A Route's Pilgrim Counts|What explains a measured change in participation?|Check counting method, transport, calendar, rules, and weather.
then_vs_now|One Route Across Generations|How have travel, costs, rituals, and access changed?|Use comparable dated records and participants' own accounts.
future_developments|Scenarios for a Pilgrim Corridor|Which conditions could reshape one route?|State climate, crowding, transport, custodial rules, and local priorities.
myths_vs_facts|A Pilgrimage Origin Claim|Which parts of a popular origin story are historical, devotional, or uncertain?|Attribute each claim to its source and tradition.
documentary_stories|One Pilgrim Season Reconstructed|What happened along a route during a documented season?|Use official dates and consented participant and resident accounts.
map_vs_ground|A Pilgrim Map's Blind Spots|Which current barriers or ritual stops are absent from a map?|Verify route, surface, permissions, facilities, and local names.
route_choices|Why Pilgrims Use Different Paths|How do practice, ability, time, cost, and access shape route choice?|Present alternatives without ranking religious legitimacy.
seasonality|The Pilgrimage Calendar|How do ritual dates and weather change one journey?|Specify tradition, year, route opening, and current notices.
local_voice|Host Communities' Experiences|How do residents and workers describe peak pilgrim periods?|Seek varied consented views on income, services, crowding, and care.
landscape_process|Terrain Along the Route|How do slope, river, coast, or desert affect travel?|Use site-specific physical and hazard records.
accessibility|Who Can Complete the Journey?|Which physical, cost, information, or rule barriers matter?|Define participant needs and verify current accommodations.
infrastructure|What Carries a Pilgrimage Season?|Which transport, water, sanitation, lodging, and emergency systems are needed?|Compare capacity, maintenance, peak demand, and funding.
environmental_pressure|The Route's Ecological Cost|Which measurable waste, water, or habitat pressures arise?|Compare season, volume, mitigation, and local needs.
safety_decision|Current Route Information|Which official conditions must be checked before one journey?|Use live weather, road or trail status, registration, health advisories, and custodian notices.
place_history|Before the Modern Pilgrim Route|What earlier settlement, land use, and ritual practice shaped a corridor?|Attribute archives, texts, archaeology, and living memory.
comparison_of_places|Two Pilgrimage Routes Compared|How do two routes differ in logistics and governance?|Define tradition, season, distance, access, custodians, and data year.
responsible_access|Visitor Limits on a Sacred Route|Who gains and loses when a route limits entry?|Consider worship rights, safety, equity, ecology, and local livelihoods.
field_map_accuracy|Verifying a Pilgrim Route Map|Does a published map match the current permitted path?|Check edition, closures, stage distances, place names, and authority.
field_place_names|Names Along a Sacred Route|Which official, local, and devotional names coexist?|Record language, tradition, community use, and attribution.
field_local_history|One Stop's Layered Past|How did a route stop become important?|Compare dated sources with participants' interpretations.
field_visitor_access|A Pilgrim Journey Access Audit|At which stage does a defined participant face a barrier?|Check registration, transport, lodging, route, ritual area, and return.
field_landscape_change|A Route in a Changing Landscape|How has one road, path, river, or settlement edge changed?|Use comparable maps, hazard records, and local accounts.
"""


if __name__ == "__main__":
    revise_domain("223", "223_pilgrimage_travel", PILGRIMAGE,
                  "Pilgrimage travel through religious purpose, route history, custodial rules, participant access, host communities, and changing conditions.",
                  "current custodial and government route notices, dated maps and archival sources, visitor and service records, and consented pilgrim, worker, and resident accounts",
                  "Name tradition, route, custodian, jurisdiction, season, and date. Attribute devotional claims respectfully; do not generalize one faith's practice, publish private rituals without consent, or use historic route descriptions as current travel guidance.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
