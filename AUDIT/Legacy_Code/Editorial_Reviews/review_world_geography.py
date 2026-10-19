"""Editorial question designs for niche 218, World Geography."""

from review_angle_plans import audit, revise_domain


GEOGRAPHY = """history_origins|How a Place Became Mapped|Which survey and political decisions shaped one map feature?|Compare dated maps, methods, local names, and boundary records.
famous_examples|A Famous Map Claim Rechecked|What does one widely shared geographic ranking actually measure?|Define feature, extent, datum, projection, source, and date.
hidden_stories|Who Made the Map?|Whose fieldwork and local knowledge appear or disappear in one map?|Trace surveyors, Indigenous and local contributors, editors, and data sources.
beginner_explainers|Reading a World Map Critically|What do projection, scale, legend, and date change?|Use one map and compare with ground or official data.
advanced_concepts|Boundaries Are Not One Thing|How do physical, administrative, and cultural regions differ?|Choose one place and attribute each boundary to its source.
mysteries_unsolved_cases|Two Maps Disagree|Which technical or political choices explain a geographic mismatch?|Check datum, projection, date, source, resolution, and contested claims.
technology_innovation|A New Geospatial Layer Tested|Does one satellite or crowdsourced layer improve a place description?|Compare accuracy, update cycle, bias, licensing, and field verification.
people_personalities|A Place-Name Decision|How did one named authority or community change a geographic label?|Use dated records, language, objections, adoption, and continued local use.
major_events|A Boundary or Landscape Change|What changed on maps after one documented event?|Separate legal change, physical change, naming, and map updates.
how_it_works|How Coordinates Locate a Place|What do latitude, longitude, datum, and precision tell us?|Show one location across systems and quantify uncertainty.
rise_fall|A Place's Changing Footprint|Why did a mapped settlement or habitat expand or shrink?|Compare classification, land use, population, imagery, and date.
then_vs_now|One Place Across Maps|Which changes reflect the ground rather than cartographic method?|Match scale, projection, feature definitions, and sources.
future_developments|Scenarios for a Changing Place|Which plausible processes could alter its geography?|State land use, coast or river dynamics, governance, and uncertainty.
myths_vs_facts|A Map Is Neutral?|Which choices shape what one map emphasizes or omits?|Compare projection, classification, names, scale, and intended audience.
documentary_stories|A Place Through Its Maps|How do maps and local accounts record one landscape's change?|Build a dated sequence and attribute contested interpretations.
map_vs_ground|When a Map Misses a Place|Which important route, hazard, or use is absent from a map?|Compare field observation, community account, source date, and access.
route_choices|Why Routes Follow This Corridor|How do terrain, rights, transport, and cost shape one route?|Compare alternatives using dated maps and local testimony.
seasonality|One Place Across Seasons|How do access, water, vegetation, or settlement activities vary?|Use seasonal data and avoid a year-round claim from one visit.
local_voice|Names Used by Local People|Which locally used names coexist with official labels?|Attribute language, speakers, context, consent, and naming authority.
landscape_process|What Shaped This Landform?|Which physical process explains one mapped feature?|Use geology, hydrology, climate, and measured change.
accessibility|Who Can Actually Reach This Place?|Which physical, legal, cost, or information barriers matter?|Define traveler or resident needs and verify current conditions.
infrastructure|What Connects This Region?|How do roads, water, energy, and communications shape settlement?|Map coverage, condition, costs, and who lacks service.
environmental_pressure|One Place Under Pressure|Which land or water change affects a defined landscape?|Measure exposure, ecosystem response, and human use.
safety_decision|Using Current Place Information|Which dated facts matter before travel to one area?|Check official access, weather, terrain, route status, and local guidance.
place_history|Earlier Uses of a Named Place|Whose homes, rights, and land use preceded the current map label?|Use archives and consented local and Indigenous sources.
comparison_of_places|Two Places on Comparable Terms|How do two places differ under the same geographic measure?|Match area, population, elevation, season, source, and boundary.
responsible_access|Opening a Place to Visitors|Who benefits and who bears costs when access expands?|Compare rights, infrastructure, environment, revenue, and local views.
field_map_accuracy|An Accuracy Check on One Map|How far do mapped features deviate from verified positions?|Define datum, reference data, sampling, date, and uncertainty.
field_place_names|One Place, Multiple Names|How should a map represent official and locally used names?|Record language, source, authority, history, and disputed status.
field_local_history|A Landscape's Layered History|Which documents and community accounts explain a place's present form?|Compare maps, land records, oral histories, and attribution.
field_visitor_access|A Door-to-Place Access Audit|At which step does a defined visitor face the strongest barrier?|Check transport, booking, cost, route, facilities, and rights.
field_landscape_change|Measuring a Moving Boundary|How did one coast, river, or settlement edge shift?|Use comparable maps, field checks, dates, and uncertainty.
"""


if __name__ == "__main__":
    revise_domain("218", "218_world_geography", GEOGRAPHY,
                  "World geography through physical and political boundaries, map methods, place names, access, landscape change, and local knowledge.",
                  "dated authoritative maps and gazetteers, geodetic metadata, satellite imagery with field checks, land and boundary records, and consented local and Indigenous accounts",
                  "Name place, source, date, map scale, and boundary or naming authority. Attribute contested territorial claims and local names; do not treat one projection or official label as the only perspective.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
