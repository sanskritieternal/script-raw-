"""Editorial questions for islands."""

from review_angle_plans import audit, revise_domain


ISLANDS = """history_origins|How an Island Took Shape|Which geological or ecological processes formed one island?|Use maps, dated samples, and qualified local research.
famous_examples|An Island Beyond Its Postcard|What does a celebrated island image leave out of daily life?|Compare visitor promotion, residents' needs, services, and land use.
hidden_stories|The Work That Connects an Island|Whose ferry, fishing, repair, care, and supply work sustains residents?|Follow consented workers and trace seasonal dependence.
beginner_explainers|What Counts as an Island?|Which physical and political boundaries define one island in this story?|Name tidal conditions, jurisdiction, linked islets, and data definitions.
advanced_concepts|Isolation as a Measured Claim|How connected is one island for people, goods, information, and ecosystems?|Compare routes, costs, frequency, communications, and migration.
mysteries_unsolved_cases|A Changing Shoreline|Which causes explain an observed coastal change?|Compare maps, tide levels, storms, sediment, works, and uncertainty.
technology_innovation|An Island Utility Solution|Did one energy, water, or connectivity project meet local needs?|Compare reliability, costs, maintenance, governance, and alternatives.
people_personalities|A Resident's Island Decisions|How does one household balance work, travel, and staying?|Use voluntary account and situate it among varied island experiences.
major_events|A Storm and Its Aftermath|How did one documented event affect access and recovery?|Trace warnings, damage, services, local response, and reconstruction.
how_it_works|Supplying an Island|How do essential goods reach one settlement?|Map ports, vessels, schedules, storage, prices, and disruptions.
rise_fall|A Changing Island Population|Which factors explain population change in one period?|Compare census definitions, births, migration, jobs, housing, and policy.
then_vs_now|A Ferry Crossing Across Generations|How did one route's time, cost, and reliability change?|Use dated schedules, fares, weather disruption, and traveler accounts.
future_developments|An Island Adaptation Plan|Would one proposed project address risks residents prioritize?|Check hazard maps, cost, access, ecology, maintenance, and consultation.
myths_vs_facts|The Self-Sufficient Island Claim|How much does one island depend on outside materials and services?|Trace food, energy, health care, trade, and local production.
documentary_stories|A Week Between Arrivals|What happens when transport is delayed to one island?|Follow consented residents and workers; verify cause and duration.
map_vs_ground|An Island Trail on the Map|Does a mapped path remain open and safe today?|Check permissions, erosion, seasonal closure, terrain, and local advice.
route_choices|Two Ways to Reach the Island|How do routes differ for residents and visitors?|Compare fare, frequency, accessibility, weather, cargo, and time.
seasonality|An Island Through the Year|How do seasonal conditions reshape work and services?|Use weather, visitor, fishing, transport, and school records.
local_voice|Who Defines the Island's Future?|How do residents with different livelihoods view one development?|Use attributed consultation and document disagreement.
landscape_process|Reef, Cliff, or Mangrove Shore|How does one coastal feature change and protect the island?|Use site-specific monitoring and separate natural from built effects.
accessibility|Getting Around Without Easy Transport|Which barriers do disabled and older residents face?|Check ferry, dock, paths, care access, and consented experiences.
infrastructure|Water on an Island|How does one settlement obtain and manage freshwater?|Trace source, quality testing, storage, energy, costs, and drought plans.
environmental_pressure|Visitor Pressure on a Small Island|Which impacts are measured and who bears their costs?|Compare waste, water, housing, habitat, income, and seasonal peaks.
safety_decision|A Crossing Under Changing Conditions|What information informs a ferry or trip decision?|Use official warnings, operator rules, vessel limits, and alternatives.
place_history|The Island's Land and People|How did settlement, ownership, and access change?|Use local accounts, land records, maps, and colonial context where relevant.
comparison_of_places|Two Islands, Different Constraints|Why do similarly sized islands have different services?|Compare population, governance, routes, ecology, and funding.
responsible_access|Visiting Without Displacing|What do residents ask visitors to respect?|Check locally defined access rules, habitat limits, costs, and benefits.
field_map_accuracy|Testing an Island Map|Which coastline or route details are outdated?|Compare map date, field observation, tides, and authoritative updates.
field_place_names|The Names Around an Island|What histories do local and official place names reveal?|Use language authorities and community-preferred names.
field_local_history|An Island's Shared Archive|Which records and memories tell different parts of its past?|Compare photographs, port records, oral histories, and gaps.
field_visitor_access|A Day Visitor's Real Options|Can a visitor access a site without straining resident services?|Check transport, facilities, permissions, capacity, and local guidance.
field_landscape_change|A Shoreline Measured Over Time|How has one section of coast changed and why?|Use comparable imagery, tide datum, survey methods, and uncertainty.
"""


if __name__ == "__main__":
    revise_domain("151", "151_islands", ISLANDS,
                  "Islands as lived places and connected environments through geology, transport, services, governance, access, and ecological change.",
                  "dated charts and maps, local records and consented resident accounts, transport and service data, ecological monitoring, current weather and access rules, and comparable shoreline surveys",
                  "Name island, jurisdiction, period, and community. Avoid treating islands as isolated or interchangeable, check current route and weather conditions, and separate measured environmental change from assumed causes.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
