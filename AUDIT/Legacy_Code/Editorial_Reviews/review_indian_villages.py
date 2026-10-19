"""Editorial question designs for niche 221, Indian Villages."""

from review_angle_plans import audit, revise_domain


INDIAN_VILLAGES = """history_origins|How One Village Took Shape|Which land, water, migration, and governance changes shaped a named settlement?|Use land records, maps, census directories, and consented accounts.
famous_examples|A Celebrated Village Model Rechecked|Did one widely cited village project deliver its claimed results?|Compare baseline, funds, maintenance, participation, and unequal effects.
hidden_stories|Work Behind Village Life|Whose paid and unpaid labor is missing from a village account?|Trace farming, care, water, craft, service, and seasonal migration.
beginner_explainers|What Does Village Mean Here?|How do census village, revenue village, habitation, and gram panchayat differ?|Use one locality and date with official definitions.
advanced_concepts|A Listed Amenity Versus Access|Does an official village amenity translate into usable service?|Check distance, hours, quality, affordability, and households served.
mysteries_unsolved_cases|Why a Village Service Fails|Which factors explain a documented water, road, or school gap?|Test geography, staffing, funding, maintenance, eligibility, and season.
technology_innovation|A Rural Tool Evaluated|Did one digital or physical technology improve a defined task?|Compare baseline, adoption, cost, repair, connectivity, and excluded users.
people_personalities|A Local Governance Choice|How did one named community body or official shape a decision?|Use meeting minutes, budget, dissent, implementation, and outcomes.
major_events|A Village Through a Disruption|How did a flood, drought, migration surge, or policy event affect one place?|Trace timeline, households, services, response, and recovery.
how_it_works|From Panchayat Plan to Service|How does one local public service get decided, funded, and maintained?|Map gram panchayat, block, district, state, and resident roles.
rise_fall|A Village Population Change|What explains a recorded increase or decrease?|Check census boundary, year, migration, household count, and measurement.
then_vs_now|One Village Across Two Censuses|What changed in livelihoods, services, and settlement?|Use comparable village codes, boundaries, definitions, and local accounts.
future_developments|Scenarios for One Village|Which conditions could alter water, work, and access?|State climate, migration, infrastructure, land, and governance assumptions.
myths_vs_facts|The Self-Sufficient Village Claim|What goods, services, labor, and money flow beyond one village?|Trace markets, commuting, remittances, public services, and season.
documentary_stories|One Local Project Reconstructed|What happened between a village proposal and daily use?|Follow documents, procurement, field condition, residents, and maintenance.
map_vs_ground|A Village Missing from a Map|Which habitation, path, or seasonal use is absent from official data?|Compare map edition, ground evidence, and resident knowledge with consent.
route_choices|How Residents Reach Essential Services|Why is one route or mode used for school, care, or markets?|Compare season, cost, time, accessibility, and reliability.
seasonality|Village Life Through the Year|How do monsoon, harvest, heat, and migration alter activities?|Use a named location and repeated observations.
local_voice|Whose Village Account Is Heard?|How do residents with different livelihoods and social positions describe change?|Seek consent and avoid presenting one speaker as the whole village.
landscape_process|Land and Water Under the Settlement|How do terrain, soil, and drainage shape one village?|Use maps, wells, fields, weather, and land-use records.
accessibility|Who Can Use a Village Facility?|Which barriers affect a defined group?|Check distance, design, timing, cost, information, and social access.
infrastructure|Keeping a Village Network Working|Which assets and workers sustain water, roads, power, or connectivity?|Trace coverage, outage, maintenance, funds, and accountability.
environmental_pressure|A Local Resource Under Stress|Which measured pressure affects land or water?|Compare extraction, pollution, weather, policy, and household impacts.
safety_decision|Current Information for Visiting a Rural Site|Which official and local updates matter for access?|Check road, weather, permissions, service status, and community norms.
place_history|Before Today's Administrative Name|Which older settlement, land, and language histories remain?|Use land records, maps, archives, and consented oral history.
comparison_of_places|Two Villages on Comparable Terms|Why do services or livelihoods differ?|Match district context, population, geography, year, and definitions.
responsible_access|A Visitor Economy in One Village|Who benefits and who bears costs from expanded visits?|Compare consent, livelihoods, privacy, waste, and local governance.
field_map_accuracy|Checking a Village Boundary|Does one mapped code match the settlement and administrative unit?|Compare official directory, survey map, field evidence, and date.
field_place_names|Names Residents Actually Use|How do official and locally used village or hamlet names differ?|Record language, source, authority, context, and consent.
field_local_history|One Village's Documented Past|Which land, family, work, and migration records explain change?|Compare archival sources and consented memories, protecting living people.
field_visitor_access|A Rural Access Audit|Where does travel to one service or destination break down?|Check transport, road, season, cost, timing, facilities, and rights.
field_landscape_change|Fields and Settlement Over Time|How did one village landscape change?|Use comparable maps, land records, imagery, field checks, and resident accounts.
"""


if __name__ == "__main__":
    revise_domain("221", "221_indian_villages", INDIAN_VILLAGES,
                  "Indian villages through administrative definitions, local governance, livelihoods, service usability, migration, land and water, and resident perspectives.",
                  "dated census village and amenity definitions, local government directory entries, gram panchayat and district records, land and service data, validated maps, and consented resident accounts",
                  "Name village code or unit, gram panchayat, district, state, source year, and season. Do not equate a listed amenity with usable access or present one resident as representative; protect privacy and sensitive social identities.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
