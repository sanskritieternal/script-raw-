"""Editorial question designs for niche 213, Glaciers."""

from review_angle_plans import audit, revise_domain


GLACIERS = """history_origins|How One Glacier Formed|Which climate and terrain conditions allowed a named glacier to develop?|Use landforms, ice cores or sediments, maps, and dating uncertainty.
famous_examples|A Famous Retreat Rechecked|What does one glacier's retreat actually show?|Compare front position, area, thickness, mass balance, dates, and climate context.
hidden_stories|The People Behind Glacier Records|Whose field and data work sustains a glacier time series?|Trace surveyors, local observers, guides, analysts, and institutions.
beginner_explainers|A Glacier's Gains and Losses|How do snow accumulation and ice melt affect one glacier?|Define balance year, zones, flow, and measurement units.
advanced_concepts|Retreat Is Not Mass Balance|Why can the glacier front lag behind a change in mass?|Explain ice flow, geometry, response time, and different observations.
mysteries_unsolved_cases|An Unusual Glacier Year|Which factors explain a documented anomaly in one glacier?|Test snowfall, summer heat, debris cover, avalanches, and measurement.
technology_innovation|Remote Sensing a Glacier|Does imagery improve estimates of area or thickness?|Compare snowline, shadow, debris cover, resolution, and field validation.
people_personalities|A Glacier Monitoring Choice|How did one named researcher or community build a long record?|Use method history, funding, local knowledge, and revisions.
major_events|A Glacier Lake Outburst Examined|What happened in one documented outburst and what remains uncertain?|Trace lake level, trigger, flow, impact, and official investigation.
how_it_works|How Ice Moves Downhill|What measurements show glacier flow at one site?|Compare surface markers, slope, ice thickness, basal conditions, and season.
rise_fall|A Glacier's Mass Trend|What supports a long-term gain or loss?|Use comparable annual mass balance, density corrections, and uncertainty.
then_vs_now|One Glacier Across Two Surveys|Which changes are real across maps and methods?|Match dates, season, outline, elevation datum, and measurement technique.
future_developments|Scenarios for One Glacier|Which conditions could alter its future size and runoff?|State climate, snowfall, debris, geometry, and model assumptions.
myths_vs_facts|Did a Snowy Winter Save the Glacier?|How much can one winter offset several years of ice loss?|Compare annual mass balance, long series, and glacier geometry.
documentary_stories|One Glacier Field Season|What did a year's measurements reveal?|Trace stakes, snow pits, weather, data checks, and local observations.
observation_to_explanation|One Glacier Photograph's Limits|What can an image establish about change?|Separate viewpoint and seasonal snow from area, thickness, and mass trend.
measurement_method|Measuring Glacier Mass Balance|How do stakes, snow pits, and geodetic surveys estimate mass change?|Explain density, spatial extrapolation, timing, cross-checks, and error.
scale_and_timespan|One Glacier Versus a Region|At what scale is a glacier claim supported?|Define glacier, mountain range, measurement years, and representativeness.
field_vs_lab|Ice Behavior in Nature|Does a controlled ice-deformation result explain one glacier's flow?|Compare temperature, impurities, pressure, basal water, and field data.
natural_variation|Year-to-Year Glacier Change|How much mass balance varies with weather?|Use long records and avoid inferring a trend from one year.
mechanism_chain|From Temperature to Runoff|Which links connect warming to seasonal river flow?|Trace melt energy, snow, storage, ice area, and basin water use.
extreme_case|A Record Glacier Loss|How was an exceptional loss year verified?|Check balance-year dates, method, units, sampling, and uncertainty.
classification_debate|When Is Ice a Glacier?|Why do inventories disagree about small ice bodies?|Compare persistence, movement, area threshold, debris cover, and definitions.
interacting_systems|Glacier and Watershed|How do ice, snow, sediment, and downstream water interact?|Measure timing and distinguish glacier runoff from all basin flow.
data_gap|The Unmeasured Glaciers|Which elevations or regions lack repeated observations?|Map field access, imagery limits, debris, and model dependence.
prediction_test|Did a Glacier Model Hold?|How did a past projection compare with later measurements?|Match model version, climate assumptions, dates, mass or area metric, and error.
human_impact|Who Depends on Glacier Water?|How are seasonal water, hazards, tourism, and adaptation costs shared?|Use basin records, rights, local accounts, and uncertainty.
field_field_sampling|A Glacier Monitoring Design|Which measurements answer one glacier question?|Specify stakes, pits, timing, density, geodetic check, and safety approvals.
field_land_use|Land Use Below a Glacier|How do downstream decisions affect exposure to glacier-related change?|Compare settlement, water use, infrastructure, and hazard maps.
field_weather_variability|Snowfall Versus Long-Term Loss|How much of a mass-balance change follows one season's weather?|Use matched precipitation, temperature, and multi-year glacier records.
field_habitat_change|New Ground After Ice Retreat|Which habitats emerge and change as one glacier recedes?|Use repeat maps, soil and vegetation surveys, and time since exposure.
field_restoration_evidence|Can an Intervention Protect a Glacier?|Which measured outcome followed one local ice-preservation attempt?|Compare coverage, energy balance, cost, scale, and controls without claiming global reversal.
"""


if __name__ == "__main__":
    revise_domain("213", "213_glaciers", GLACIERS,
                  "Glaciers through mass balance, ice motion, front position, runoff, hazards, monitoring, and human dependence.",
                  "standardized glacier mass-balance records, geodetic surveys, dated imagery, weather and runoff gauges, hazard assessments, and consented local accounts",
                  "Name glacier, balance year, measure, method, and uncertainty. Distinguish front retreat, area, and mass loss; avoid judging long-term change from one snowy year or photograph.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
