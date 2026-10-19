"""Editorial question designs for niche 220, Indian Cities."""

from review_angle_plans import audit, revise_domain


INDIAN_CITIES = """history_origins|How One Indian City Took Shape|Which trade, governance, migration, and land decisions shaped it?|Use dated maps, municipal records, archives, and local accounts.
famous_examples|A Celebrated City Project Rechecked|Did one widely praised urban project meet its stated goals?|Compare plan, budget, delivery, maintenance, access, and affected residents.
hidden_stories|The Labor Behind City Life|Whose work keeps an Indian city operating?|Trace sanitation, transport, care, vending, utilities, and contracted workers.
beginner_explainers|Which City Boundary?|How do municipal, census, district, and metropolitan boundaries differ?|Choose one city and date; map who is included.
advanced_concepts|Service Coverage Versus Usable Service|Does a listed urban service reach residents reliably?|Compare connection, quality, hours, affordability, and neighborhood.
mysteries_unsolved_cases|Why One Neighborhood Floods|Which factors explain recurring flooding at a named site?|Test rainfall, drains, topography, construction, water bodies, and maintenance.
technology_innovation|A City Technology Evaluated|Did one digital tool improve a defined public service?|Compare baseline, uptake, errors, cost, privacy, and excluded residents.
people_personalities|A City Planning Decision|How did one named official or community group shape a project?|Use plans, hearings, objections, budgets, and outcomes.
major_events|A City After a Shock|How did a flood, heatwave, closure, or policy event change services?|Trace timeline, affected wards, response, and lasting changes.
how_it_works|How a City Service Reaches Homes|Who plans, funds, delivers, and monitors one service?|Follow municipal, state, contractor, and resident roles.
rise_fall|A City's Population Figure|What explains a reported rise or fall?|Check city boundary, census year, migration, households, and estimate method.
then_vs_now|One Ward Across Two Decades|How have land use, services, and residents' access changed?|Compare same boundary, maps, census dates, and local testimony.
future_developments|Scenarios for One Indian City|Which conditions could alter housing, transport, and climate risk?|State assumptions, jurisdiction, funding, and population definition.
myths_vs_facts|The City Ranking Claim|What does one best or largest city list measure?|Inspect boundary, population year, indicators, weights, and missing data.
documentary_stories|One Urban Decision Reconstructed|What happened from proposal to everyday use of one project?|Trace documents, construction, residents' accounts, and maintenance.
map_vs_ground|A Ward Map's Blind Spots|Which paths, services, or settlements are absent from official layers?|Compare map date, field observation, and resident knowledge with care.
route_choices|How Residents Cross the City|Why do people choose one route or mode?|Compare time, fare, safety, accessibility, reliability, and trip purpose.
seasonality|A City Across Seasons|How do heat, monsoon, air conditions, or festivals change service needs?|Use local data and distinguish temporary peaks from long trends.
local_voice|Residents' Description of a Ward|How do different groups describe the same place?|Seek consented accounts across tenure, age, livelihood, and ability.
landscape_process|The Terrain Under a City|How do slope, coast, river, or former wetlands shape urban form?|Compare topography, drainage, land conversion, and planning.
accessibility|Can Everyone Use This City Service?|Which barriers affect a defined group?|Audit distance, cost, design, information, hours, and actual use.
infrastructure|The Maintenance Behind a City|Which assets and staff keep one service reliable?|Trace networks, inspections, breakdowns, budgets, and accountability.
environmental_pressure|A City's Unequal Exposure|Where does one pollution, heat, or flood burden fall?|Map exposure and population using comparable data and privacy safeguards.
safety_decision|Current Information for City Travel|Which official and local updates affect one urban trip?|Check service notices, weather, route access, and current conditions.
place_history|Before the Current Neighborhood|Whose homes, work, and land uses preceded redevelopment?|Use maps, land and court records, and consented community memory.
comparison_of_places|Two Wards, One Service Measure|Why do neighborhoods differ in access or outcomes?|Match population need, boundary, service standard, and data year.
responsible_access|Opening a City Space|Who benefits and who may be displaced by a new public space?|Compare tenure, vendors, accessibility, ecology, and upkeep.
field_map_accuracy|Checking a Municipal Map|Which boundaries and service locations are current?|Compare official version, ground checks, coordinate reference, and date.
field_place_names|A City's Multiple Names|How do official, historic, and locally used names coexist?|Attribute language, authority, community use, and date.
field_local_history|One Ward's Layered History|What explains its current street and settlement pattern?|Compare maps, planning records, oral histories, and land rights.
field_visitor_access|A City Destination Access Audit|What barriers arise from home to destination?|Check mode, time, fare, last mile, signage, facilities, and safety.
field_landscape_change|Measuring Urban Expansion|How did a built-up edge or water body change?|Use comparable imagery, boundary definitions, field checks, and land records.
"""


if __name__ == "__main__":
    revise_domain("220", "220_indian_cities", INDIAN_CITIES,
                  "Indian cities through changing boundaries, neighborhoods, public services, infrastructure, mobility, environmental exposure, and resident perspectives.",
                  "dated municipal and census records with definitions, city plans and budgets, service-performance data, validated maps, land records, and consented resident and worker accounts",
                  "Name city, ward or metro boundary, jurisdiction, population source, and date. Do not compare city rankings or growth with incompatible boundaries or years; protect residents' privacy and rights.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
