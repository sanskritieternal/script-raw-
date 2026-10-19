"""Editorial question designs for niche 206, Deserts."""

from review_angle_plans import audit, revise_domain


DESERTS = """history_origins|How a Desert Landscape Formed|Which climate and geologic processes shaped one named desert?|Use stratigraphy, landforms, paleoclimate, and dating uncertainty.
famous_examples|An Iconic Desert Image Rechecked|What does a famous dune or cactus view omit about the wider desert?|Compare landforms, soils, water, species, and land use across the region.
hidden_stories|People Who Know a Dryland|Whose land knowledge and monitoring shape understanding of one desert?|Attribute Indigenous, local, field, and management accounts with consent.
beginner_explainers|What Makes a Desert?|Which water-balance conditions define one arid region?|Compare precipitation, evaporation demand, seasonality, and ecological response.
advanced_concepts|Small Rain, Large Response|Why can a brief rain event strongly alter one dryland system?|Trace infiltration, runoff, seeds, microbes, grazing, and time lags.
mysteries_unsolved_cases|A Patch That Changed Unexpectedly|Which factors explain a documented shift in desert vegetation?|Test rainfall, soil, grazing, invasive species, fire, and sampling.
technology_innovation|Remote Sensing in Drylands|Does satellite imagery accurately track one desert condition?|Compare spectral signal, sparse cover, soil background, calibration, and field plots.
people_personalities|A Dryland Stewardship Decision|How did one named community or manager alter desert land use?|Use plans, rights, participation, monitoring, and outcomes.
major_events|After an Unusual Desert Storm|What changed after one documented rainfall or flood event?|Compare runoff, erosion, plant response, infrastructure, and recovery.
how_it_works|Water at the Desert Surface|How do rain, soil crust, infiltration, and evaporation interact?|Specify soil, slope, vegetation, event size, and measured fluxes.
rise_fall|A Desert Plant Population's Trend|What supports increase or decline for one species?|Use repeat plots, recruitment, mortality, weather, and disturbance.
then_vs_now|One Desert Site Across Surveys|Which changes survive differences in field methods?|Match site, season, plots, species names, soil measures, and weather.
future_developments|Scenarios for One Dryland|Which plausible changes could reshape vegetation and water?|State heat, precipitation, land use, invasion, and management assumptions.
myths_vs_facts|Is a Desert Empty?|What do surveys reveal about life in one apparently bare site?|Include cryptic, nocturnal, seasonal, and soil organisms with sampling limits.
documentary_stories|A Dryland Monitoring Plot|What did repeated visits show through drought and rain?|Follow dated vegetation, soil, weather, and management records.
observation_to_explanation|A Green Desert After Rain|What can a sudden bloom establish?|Separate temporary annual plants from perennial cover and long-term recovery.
measurement_method|Measuring Sparse Vegetation|How does a field transect estimate desert plant and soil cover?|Specify line points, species, crust, bare ground, repeats, and error.
scale_and_timespan|One Wash Versus a Desert Region|At what scale is a dryland change claim valid?|Define landform, watershed, region, years, and sampling coverage.
field_vs_lab|A Desert Trait in Natural Conditions|Does a controlled drought response predict field survival?|Compare soil, heat, root depth, competitors, life stage, and long-term data.
natural_variation|Rainfall Pulses and Quiet Years|How much ecological change follows normal weather variation?|Use multi-year rainfall and vegetation series before trend claims.
mechanism_chain|From Soil Disturbance to Erosion|Which measured steps link trampling or land use to soil loss?|Trace crust damage, infiltration, runoff, sediment, and recovery.
extreme_case|An Exceptional Dryland Event|How was a record heat, rain, or bloom event verified?|Check station coverage, units, period, baseline, and ecological response.
classification_debate|Where Does the Desert Begin?|Why do climate and vegetation maps draw different boundaries?|Compare precipitation, water balance, soils, and transition zones.
interacting_systems|Plants, Crusts, Soil, and Water|How do biological soil crusts affect a named site?|Use measured stability, infiltration, plant response, and competing factors.
data_gap|What Desert Monitoring Misses|Which seasons, soils, or organisms are weakly sampled?|Map access, rare rain events, nocturnal species, and remote-sensing limits.
prediction_test|Did a Dryland Forecast Hold?|Did predicted vegetation response match later field plots?|Compare forecast date, weather assumptions, plot methods, and error.
human_impact|Living and Working in a Desert|How do water and land decisions affect local communities?|Compare rights, livelihoods, infrastructure, ecological outcomes, and consented accounts.
field_field_sampling|A Dryland Plot Designed Well|Which measurements answer one desert ecosystem question?|Choose landform, repeat timing, plant cover, soil crust, stability, and controls.
field_land_use|Grazing or Development in One Dryland|How did a documented use change affect soil and vegetation?|Compare intensity, weather, reference sites, rights, and recovery.
field_weather_variability|Separating Drought from Trend|How much of a site change follows rainfall or temperature variability?|Use comparable weather and plot records across multiple years.
field_habitat_change|A Desert Habitat Mosaic|Which dunes, washes, flats, or slopes changed?|Map landforms and compare field evidence, habitat quality, and species.
field_restoration_evidence|Did Dryland Restoration Last?|Which outcomes improved after one desert intervention?|Check native cover, soil stability, water, maintenance, controls, and time.
"""


if __name__ == "__main__":
    revise_domain("206", "206_deserts", DESERTS,
                  "Deserts through water balance, landforms, soil crusts, sparse vegetation, local livelihoods, and measured change.",
                  "long-term precipitation and temperature records, repeat vegetation and soil protocols, calibrated imagery, land-use records, restoration monitoring, and consented local accounts",
                  "Name desert, landform, season, measure, and time span. Distinguish a brief green-up from lasting recovery and sparse visible cover from low biodiversity; respect land rights and fragile soil crusts.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
