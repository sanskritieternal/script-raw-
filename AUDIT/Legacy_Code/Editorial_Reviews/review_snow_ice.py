"""Editorial question designs for niche 214, Snow & Ice."""

from review_angle_plans import audit, revise_domain


SNOW_ICE = """history_origins|How Snow and Ice Records Began|Which instruments first documented one region's snow or ice?|Compare historical logs, sites, methods, and coverage.
famous_examples|A Famous Ice Minimum Rechecked|What does one widely cited minimum measure?|Define ice type, extent or area, region, season, sensor, and baseline.
hidden_stories|Who Maintains Snow Observations?|Whose field and data work keeps a snow record reliable?|Trace station crews, observers, calibrators, analysts, and local knowledge.
beginner_explainers|Snow, Sea Ice, and Land Ice|How do these forms of frozen water differ?|Compare origin, location, movement, seasonality, and sea-level relevance.
advanced_concepts|Extent, Area, and Water Stored|Why can snow cover and snow water equivalent tell different stories?|Compare surface footprint, depth, density, and water content.
mysteries_unsolved_cases|A Snowpack That Melted Early|Which factors explain an unusual melt season?|Test temperature, rain-on-snow, dust, wind, shade, and sensors.
technology_innovation|Snow and Ice from Space|What can one satellite sensor measure and miss?|Compare resolution, cloud or canopy, melt ponds, concentration, and ground checks.
people_personalities|A Cryosphere Monitoring Decision|How did one named team change a snow or ice data series?|Trace instrument changes, calibration, publication, and review.
major_events|A Rapid Snow or Ice Event|What happened during one documented thaw, freeze, or breakup?|Use dated observations, weather, impacts, and uncertainty.
how_it_works|Snow Becomes Stored Water|How do snowfall, compaction, melt, and refreezing change a snowpack?|Use measured depth, density, SWE, and season.
rise_fall|A Regional Snow Trend|What supports a sustained change in snow cover or SWE?|Compare consistent time series, elevation, station coverage, and uncertainty.
then_vs_now|Two Snow Seasons Compared|Which differences remain after matching dates and measures?|Compare snow depth, SWE, extent, storm timing, and sensor method.
future_developments|Scenarios for a Snow Region|Which plausible conditions could reshape snow duration?|State temperature, precipitation phase, elevation, and model assumptions.
myths_vs_facts|Does More Snow Mean More Water?|When does a deeper snowpack contain less water?|Compare density, depth, SWE, and melt history.
documentary_stories|One Winter's Snowpack|What did repeated observations reveal about a particular season?|Trace storms, gauges, manual surveys, melt, and forecast revisions.
observation_to_explanation|One Snowy Day in Context|What can a single snowfall establish?|Separate event weather from seasonal water storage and climate trend.
measurement_method|Measuring Snow Water Equivalent|How do snow pillows and manual cores estimate stored water?|Explain calibration, location bias, density, gaps, and uncertainty.
scale_and_timespan|A Station Versus a Snow Basin|At what scale is a snow or ice claim supported?|Define elevation, basin, region, season, years, and sensor reach.
field_vs_lab|Ice Reflectance in Nature|Does a controlled albedo result predict a real snow surface?|Compare grain size, dust, canopy, sunlight, and field measurements.
natural_variation|Snow Year to Snow Year|How much variation follows normal storm timing?|Use long comparable series and elevation context.
mechanism_chain|From Snowpack to Spring Flow|Which measured steps link winter snow to river discharge?|Trace SWE, melt timing, rain, soil, reservoirs, and withdrawals.
extreme_case|A Record Snow or Ice Claim|How was one exceptional measurement verified?|Check station or grid, instrument, dates, category, and independent review.
classification_debate|What Counts as Ice Covered?|How do thresholds change reported sea-ice extent?|Compare concentration, area, extent, spatial resolution, and convention.
interacting_systems|Snow, Ground, and Air|How does snow cover alter one land surface's energy and water balance?|Use measured albedo, insulation, melt, and soil conditions.
data_gap|What Snow Maps Cannot See|Which canopy, cloud, elevation, or station gaps weaken a claim?|Map retrieval limits and model-filled observations.
prediction_test|Did a Snow Forecast Hold?|How did a projected melt or SWE compare with later measurements?|Match forecast date, model, station coverage, observed units, and error.
human_impact|Who Uses Snow and Ice Data?|How do water managers, residents, and travelers act on one measure?|Compare decisions, access, costs, and uncertainty without route safety claims.
field_field_sampling|A Snow Survey Designed Well|Which observations answer a snowpack question?|Specify transects, depth, density, SWE, timing, terrain, and safety approvals.
field_land_use|Land Cover and Snowpack|How did one land-use change alter snow retention or melt?|Compare canopy, wind, ground data, weather, and controls.
field_weather_variability|Storm Pattern Versus Trend|How much of a cryosphere change follows a short weather anomaly?|Use multi-year observations and consistent seasonal dates.
field_habitat_change|Snow Duration and Habitat|Which ecological condition changed with snow timing?|Use paired snow and species records, habitat context, and lag.
field_restoration_evidence|Did Snow Retention Work?|Which measurable outcome followed one local intervention?|Compare SWE, melt timing, water yield, cost, and controls.
"""


if __name__ == "__main__":
    revise_domain("214", "214_snow_ice", SNOW_ICE,
                  "Snow and ice through distinct frozen-water types, measurement definitions, seasonal storage, reflectance, runoff, and observed trends.",
                  "versioned snow and sea-ice datasets, station and snow-course records, satellite methods, weather observations, water gauges, and documented uncertainty",
                  "Name snow or ice type, measure, region, elevation, season, and date. Distinguish sea-ice extent from area and snow depth from SWE; use current official sources for travel or ice safety.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
