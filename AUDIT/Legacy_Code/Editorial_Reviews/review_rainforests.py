"""Editorial question designs for niche 207, Rainforests."""

from review_angle_plans import audit, revise_domain


RAINFORESTS = """history_origins|How One Rainforest Took Shape|Which climate, geology, and species histories formed a named rainforest?|Use dated paleoecology, soils, maps, and uncertainty.
famous_examples|A Famous Rainforest Claim Tested|What does one widely cited forest case actually show?|Define forest type, boundary, years, measure, and local context.
hidden_stories|People Behind Rainforest Knowledge|Whose stewardship and fieldwork produced a forest account?|Attribute Indigenous knowledge, local teams, plot crews, and data curators with consent.
beginner_explainers|Rainforest Is Not One Habitat|How do canopy, understory, soil, and waterways differ at one site?|Use measured light, water, species, and microhabitats.
advanced_concepts|Forest Cover Versus Forest Integrity|Why can tree cover remain while ecological condition changes?|Compare fragmentation, species mix, canopy structure, hunting, and regeneration.
mysteries_unsolved_cases|An Unexpected Forest Decline|Which factors explain a documented change in one forest plot?|Test drought, land use, fire, pests, edge effects, and sampling.
technology_innovation|Mapping Rainforest Change|Does one satellite or lidar method detect the change of interest?|Compare cloud cover, canopy height, disturbance, field calibration, and error.
people_personalities|A Forest Governance Choice|How did one named community or manager change land stewardship?|Use tenure records, participation, plans, opposition, and measured outcomes.
major_events|After a Forest Disturbance|What changed following a documented storm, fire, or clearing?|Compare pre-event plots, severity, recovery, land use, and reference sites.
how_it_works|Water and Carbon in One Rainforest|How do canopy, soil, rainfall, and vegetation exchange resources?|Use measured fluxes and state site and season.
rise_fall|A Rainforest Area Trend|What supports a change in extent or condition?|Match forest definitions, maps, field plots, years, and uncertainty.
then_vs_now|The Same Forest Across Surveys|Which changes survive different mapping and field methods?|Compare boundaries, resolution, season, plot design, and taxonomy.
future_developments|Scenarios for One Rainforest|Which plausible drivers could reshape it?|State climate, tenure, roads, fire, policy, and adaptation assumptions.
myths_vs_facts|Is Reforestation the Same as Recovery?|When does tree regrowth restore rainforest functions?|Compare species, age, soil, fauna, connectivity, and time.
documentary_stories|A Forest Boundary Decision|How did one documented boundary or tenure decision affect people and forest?|Trace maps, rights, enforcement, land cover, and consented accounts.
observation_to_explanation|One Cleared Patch's Meaning|What can a single satellite image establish?|Separate event, legality, area trend, degradation, and causes.
measurement_method|Counting Forest Change|How do maps and ground plots estimate rainforest extent or condition?|Check classification, sample design, validation, confidence, and revision.
scale_and_timespan|A Plot Versus a Forest Region|At what scale is a rainforest claim supported?|Define site, landscape, country, time, and data coverage.
field_vs_lab|A Tree Trait in a Forest|Does a controlled drought or growth result hold under canopy competition?|Compare species, roots, soil, light, and field validation.
natural_variation|Wet and Dry Years in Rainforest|How much canopy or growth change reflects weather variability?|Use long-term plots and rainfall records.
mechanism_chain|From Road to Forest Change|Which evidence links a new access route to ecological effects?|Trace land rights, clearing, edge, species response, and alternatives.
extreme_case|An Exceptional Forest Record|How was a record tree density, biomass, or diversity claim verified?|Check sampling area, taxonomy, units, method, and uncertainty.
classification_debate|What Counts as Rainforest?|Why do maps disagree over one forest boundary?|Compare climate, canopy, land-use, and ecological definitions.
interacting_systems|Forest, Rivers, and Climate|How does one rainforest exchange water or organisms with neighbors?|Use measured flows and avoid treating the site as closed.
data_gap|Blind Spots Beneath the Canopy|Which species, soils, or land uses are missed by existing data?|Map cloud cover, plot locations, taxonomic gaps, and tenure records.
prediction_test|Did a Forest Change Forecast Hold?|Did a projected loss or regrowth appear later?|Compare model assumptions, boundary, date, observed maps, and field checks.
human_impact|Who Holds the Forest's Benefits?|How are forest use, protection costs, and rights distributed?|Study tenure, livelihoods, access, conservation results, and consented views.
field_field_sampling|A Rainforest Plot Designed Well|What plot and biodiversity measures answer one question?|Choose stratification, permanent markers, season, taxa, and ethics.
field_land_use|One Land-Use Conversion|How did a specific conversion change rainforest structure?|Compare prior use, surrounding controls, species, soil, and social effects.
field_weather_variability|Rainfall Versus Long-Term Change|How much of an observed forest response follows unusual weather?|Use matched weather and plot series across years.
field_habitat_change|Fragmentation at a Named Site|What changed in patch size, edges, and connectivity?|Compare validated maps, field species data, and land rights.
field_restoration_evidence|Did Rainforest Restoration Work?|Which outcomes improved after one intervention?|Measure native regeneration, soil, fauna, costs, controls, and longevity.
"""


if __name__ == "__main__":
    revise_domain("207", "207_rainforests", RAINFORESTS,
                  "Rainforests through defined forest types, land rights, canopy and ground evidence, fragmentation, disturbance, and regeneration.",
                  "official forest assessments and methods, validated imagery, permanent field plots, land-tenure records, biodiversity surveys, and consented local and Indigenous accounts",
                  "Name forest type, boundary, jurisdiction, measure, and date. Distinguish tree cover from ecological integrity and reforestation from recovery; respect rights and protect sensitive locations.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
