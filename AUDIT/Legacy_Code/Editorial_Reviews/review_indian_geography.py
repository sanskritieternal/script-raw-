"""Editorial question designs for niche 219, Indian Geography."""

from review_angle_plans import audit, revise_domain


INDIAN_GEOGRAPHY = """history_origins|How an Indian Landscape Was Mapped|Which surveys and local knowledge shaped a named regional map?|Compare dated sheets, methods, names, and land records.
famous_examples|A Familiar India Map Rechecked|What does one widely used physical or political map show and omit?|Specify edition, scale, boundaries, projection, and terrain detail.
hidden_stories|The People Behind a Map|Whose fieldwork and place knowledge contributed to one geographic account?|Trace survey crews, local guides, community historians, and data editors.
beginner_explainers|India Across Physical Regions|How do landform, climate, water, and settlement interact in one region?|Define region and avoid treating it as representative of the country.
advanced_concepts|A Region Has Many Boundaries|Why do watershed, ecological, linguistic, and administrative maps differ?|Compare one area and date with attributed sources.
mysteries_unsolved_cases|Two Indian Maps Disagree|Which date, scale, datum, or naming decision explains a mismatch?|Check official editions, field evidence, and uncertainty.
technology_innovation|Mapping Change in an Indian Landscape|Does one satellite layer detect the intended change?|Compare resolution, classification, season, cloud, and ground truth.
people_personalities|A Place-Name or Mapping Decision|How did one named authority or community affect a map label?|Use dated records, language, objections, and current use.
major_events|A River or Coast Changed Course|What changed after one documented geographic event?|Separate physical shift, administration, settlement, and map update.
how_it_works|From Survey to Regional Map|How are elevation, waterways, roads, and names compiled?|Trace source dates, scale, checks, and revision.
rise_fall|A Landscape Feature's Changing Extent|What supports expansion or contraction of one mapped feature?|Compare consistent definitions, maps, field data, and years.
then_vs_now|One Indian Region Across Maps|Which changes reflect the ground rather than mapping methods?|Match scale, season, boundary, and source dates.
future_developments|Scenarios for One Region|Which plausible changes could reshape its geography?|State climate, water use, land conversion, infrastructure, and uncertainty.
myths_vs_facts|A Geographic Superlative Tested|How is a claim about India's largest or highest feature defined?|Check metric, datum, administrative boundary, and current source.
documentary_stories|One Place Through Maps and Voices|How did a named landscape change over time?|Build a dated record from maps, land documents, and consented local accounts.
map_vs_ground|What an Official Map Misses|Which seasonal or local feature is absent from one map?|Compare edition, field observation, community use, and update cycle.
route_choices|Why One Corridor Matters|How do terrain, waterways, rights, and infrastructure shape travel?|Compare alternatives using dated maps and local sources.
seasonality|A Region Across the Year|How do monsoon, snow, heat, or dry season change access and land use?|Specify region and use seasonal records.
local_voice|How Residents Describe a Landscape|Which locally used names or boundaries differ from a map?|Attribute language, speaker, consent, and context.
landscape_process|What Shaped This Landform?|Which geologic or hydrologic process explains one feature?|Use field studies, maps, and time scale.
accessibility|Who Can Reach a Place?|Which transport, terrain, cost, or legal barriers matter?|Define user needs, season, and current conditions.
infrastructure|The Network Beneath a Map|How do roads, water, energy, and communications connect one region?|Check coverage, reliability, and unequal access.
environmental_pressure|One Landscape Under Stress|Which measured pressure changes land or water in a defined area?|Compare exposure, response, policy, and alternative causes.
safety_decision|Using Current Geographic Information|Which dated facts matter for a visit or field trip?|Check official access, weather, route status, local guidance, and limits.
place_history|Before the Current Place Label|Whose land use and names preceded a map's present depiction?|Use archives and consented Indigenous or local accounts.
comparison_of_places|Two Regions on Equal Terms|How do two Indian regions differ under one measure?|Match definitions, area, time, elevation, season, and source.
responsible_access|Opening a Sensitive Place|Who benefits and who bears costs when visitor access expands?|Compare rights, ecological limits, infrastructure, and local views.
field_map_accuracy|Checking an Indian Map Feature|How accurate is one feature at its published scale?|Compare datum, source edition, field control, date, and uncertainty.
field_place_names|One Feature, Multiple Names|How should an account present official and locally used names?|Record language, authority, source date, and contested status.
field_local_history|A Landscape's Layered Record|Which maps and community sources explain a place's current form?|Compare land records, oral accounts, and physical evidence.
field_visitor_access|A Door-to-Place Access Audit|Which step prevents a defined visitor from reaching a place?|Check booking, transport, route, facilities, cost, and current rules.
field_landscape_change|Measuring an Indian Landscape Shift|How did one riverbank, coastline, or land-cover edge move?|Use comparable georeferenced maps, field checks, dates, and uncertainty.
"""


if __name__ == "__main__":
    revise_domain("219", "219_indian_geography", INDIAN_GEOGRAPHY,
                  "Indian geography through regional physical processes, map sources and scale, place names, access, local histories, and measured landscape change.",
                  "dated Survey of India maps and metadata, relevant state and district records, georeferenced imagery with field checks, physical studies, and consented local accounts",
                  "Name region, jurisdiction, map edition, scale, measure, and date. Attribute disputed boundaries and local names; avoid treating one region or season as representative of all India.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
