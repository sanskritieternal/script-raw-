"""Editorial question designs for niche 208, Wetlands."""

from review_angle_plans import audit, revise_domain


WETLANDS = """history_origins|How One Wetland Formed|Which water, sediment, and land-use processes created a named wetland?|Use cores, hydrologic records, maps, and dating uncertainty.
famous_examples|A Famous Wetland Restoration Rechecked|Which measured outcomes improved after one project?|Compare baseline, water regime, native species, costs, and reference sites.
hidden_stories|The People Who Know Wetland Water|Whose monitoring and use sustain knowledge of one wetland?|Attribute local stewards, Indigenous knowledge, field crews, and analysts with consent.
beginner_explainers|What Makes a Wetland?|Which water, soil, and vegetation traits identify one wetland?|Explain seasonal flooding and site-specific classification.
advanced_concepts|Ecological Character Beyond Area|Why can a wetland's mapped extent remain while its function changes?|Compare hydroperiod, water quality, soils, species, and connectivity.
mysteries_unsolved_cases|A Wetland That Dried Unexpectedly|Which factors explain a documented water-level change?|Test precipitation, diversions, drainage, groundwater, and measurement.
technology_innovation|Wetland Mapping from Space|Does one remote-sensing method capture seasonal inundation?|Compare resolution, cloud or canopy limits, timing, and ground validation.
people_personalities|A Wetland Management Decision|How did one named community or manager alter water or access?|Use rights, plans, implementation, objections, and ecological outcomes.
major_events|After a Flood or Drainage Change|What changed in one wetland after a documented event?|Compare water levels, sediment, vegetation, species, and recovery.
how_it_works|A Wetland's Water Balance|How do inflow, groundwater, rain, evaporation, and outflow interact?|Use measured flows, boundary, season, and uncertainty.
rise_fall|Wetland Extent Across Years|What supports a change in one wetland's size or condition?|Match seasonal timing, maps, water data, and classification.
then_vs_now|One Wetland Across Surveys|Which differences reflect true change?|Match hydroperiod, boundary, species protocol, imagery, and season.
future_developments|Scenarios for One Wetland|Which plausible changes could alter its water and ecology?|State climate, extraction, land use, policy, and restoration assumptions.
myths_vs_facts|Is Standing Water Always a Wetland?|How do wetland definitions handle seasonal or hidden water?|Compare hydrology, soils, vegetation, and jurisdiction without legal advice.
documentary_stories|A Wetland Water Decision Reconstructed|How did a documented allocation or drainage decision unfold?|Follow maps, permits, measured flows, public input, and consequences.
observation_to_explanation|One Dry Season's Meaning|What can a low-water observation establish?|Separate seasonal exposure from chronic drainage or ecological loss.
measurement_method|Monitoring Wetland Condition|How do field indicators and sensors measure ecological character?|Specify sites, frequency, water, soil, vegetation, calibration, and gaps.
scale_and_timespan|A Pool Versus a Watershed|At what scale does a wetland claim hold?|Define wetland boundary, catchment, seasons, years, and data coverage.
field_vs_lab|A Wetland Process in the Field|Does a controlled nutrient or soil result predict site behavior?|Compare flow, microbes, plants, season, and field validation.
natural_variation|Normal Flood and Dry Cycles|How much wetland variation is expected?|Use long hydrologic records and weather context.
mechanism_chain|From Drainage to Species Change|Which measured steps link a water intervention to ecological outcome?|Trace hydroperiod, soil, vegetation, habitat, and species response.
extreme_case|An Exceptional Wetland Event|How was a record flood, drought, or bird count verified?|Check gauges, survey effort, historical baseline, and uncertainty.
classification_debate|Where Does the Wetland End?|Why do ecological and administrative maps disagree?|Compare water regime, soils, vegetation, scale, and rule date.
interacting_systems|Wetland and Watershed|How do upstream land use and downstream waters shape one wetland?|Measure sediment, nutrients, flow, and habitat connections.
data_gap|What Wetland Inventories Miss|Which temporary or forested wetlands are undercounted?|Map season, canopy, imagery resolution, field access, and definitions.
prediction_test|Did a Water-Level Forecast Hold?|Did a projected wetland response match later measurements?|Compare model version, rainfall, water management, date, and gauges.
human_impact|Who Uses and Protects a Wetland?|How are fishing, water, flood risk, access, and conservation costs shared?|Use rights, livelihoods, local testimony, and measured outcomes.
field_field_sampling|A Wetland Baseline Survey|Which field measurements would document condition?|Choose hydroperiod, soil, water quality, plants, animals, season, and controls.
field_land_use|A Wetland's Surrounding Land|How did one land-use change affect wetland water or habitat?|Compare before and after records, weather, reference sites, and mechanisms.
field_weather_variability|Rainfall Versus Drainage|How much of a wetland change follows weather rather than management?|Use matched rainfall, flow, groundwater, and site records.
field_habitat_change|A Mosaic of Wetland Habitats|Which open water, marsh, or wooded patches changed?|Compare mapped extent, vegetation, water regime, and field checks.
field_restoration_evidence|Did Wetland Restoration Last?|Which predefined functions improved and persisted?|Measure hydroperiod, native habitat, water quality, costs, and controls.
"""


if __name__ == "__main__":
    revise_domain("208", "208_wetlands", WETLANDS,
                  "Wetlands through hydrology, ecological character, seasonal variability, watershed connections, local use, and restoration evidence.",
                  "site management and inventory records, measured water levels and flows, mapped soils and vegetation, repeat biological surveys, land-use records, and consented local accounts",
                  "Name wetland, boundary, jurisdiction, season, and measure. Distinguish a dry season from long-term loss and mapped area from ecological function; use current local sources for legal classifications.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
