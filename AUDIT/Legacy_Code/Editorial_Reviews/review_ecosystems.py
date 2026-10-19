"""Editorial question designs for niche 205, Ecosystems."""

from review_angle_plans import audit, revise_domain


ECOSYSTEMS = """history_origins|How One Ecosystem Was Defined|Which boundary and interactions led researchers to treat a place as one system?|Trace maps, field observations, and changing definitions.
famous_examples|A Famous Ecosystem Case Rechecked|Which mechanism is supported by a well-known ecological story?|Compare original data, later monitoring, alternative drivers, and scale.
hidden_stories|The Work Behind Long-Term Monitoring|Whose repeated sampling makes ecosystem claims possible?|Trace field staff, local knowledge holders, data curators, and analysts.
beginner_explainers|What Is in an Ecosystem?|How do living organisms and physical conditions interact at one site?|Define boundary, time period, flows, and representative components.
advanced_concepts|A System with Feedback|Which measured feedback helps maintain or change one ecosystem?|Map causal links, delays, thresholds, and competing explanations.
mysteries_unsolved_cases|A Sudden Shift in One Habitat|Which factors could explain an unexpected system change?|Test weather, land use, species interactions, disturbance, and sampling.
technology_innovation|Sensors in Ecosystem Science|Does one monitoring tool improve a chosen ecosystem measure?|Compare calibration, spatial reach, time resolution, missing data, and field checks.
people_personalities|An Ecological Management Choice|How did one named team or steward alter a system?|Use management records, public objections, monitoring, and outcomes.
major_events|An Ecosystem After Disturbance|What changed after one fire, flood, drought, or spill?|Compare baseline, exposure, recovery sequence, and unaffected references.
how_it_works|Tracing Energy or Nutrients|How does one resource move through a defined ecosystem?|Use measured producers, consumers, decomposition, losses, and timescale.
rise_fall|A Changing Ecosystem Metric|Why did one indicator rise or fall?|Check method, season, weather, land use, species, and uncertainty.
then_vs_now|One Place Across Two Surveys|Which ecosystem changes survive differences in measurement?|Match boundaries, season, protocols, indicators, and missing records.
future_developments|Scenarios for a Named Ecosystem|Which plausible pressures could alter the system?|State climate, land-use, species, policy, and response assumptions.
myths_vs_facts|Does More Species Mean Healthier?|When does a biodiversity metric reflect function or resilience?|Define taxa, scale, baseline, functional roles, and disturbance.
documentary_stories|An Ecosystem Decision Reconstructed|What happened when managers changed one practice?|Follow dated plan, implementation, monitoring, local accounts, and revision.
observation_to_explanation|One Dry Season's Meaning|What can a short-lived ecosystem observation establish?|Separate event response from persistent shift and long-term trend.
measurement_method|Sampling an Ecosystem|How do plots, sensors, and surveys estimate one condition?|Specify spatial design, frequency, detection, calibration, and uncertainty.
scale_and_timespan|A Plot Versus a Landscape|At what scale does one ecosystem inference hold?|Define boundary, connectivity, years, and sampling representativeness.
field_vs_lab|A Mechanism in Natural Conditions|Does a controlled interaction matter at ecosystem scale?|Compare lab controls, field confounders, time lags, and validation.
natural_variation|Normal Variability or Regime Shift?|How do researchers distinguish recurring swings from persistent change?|Use long series, reference sites, thresholds, and uncertainty.
mechanism_chain|From Land Use to System Change|Which measured links connect one human activity to an ecological outcome?|Trace exposure, habitat, species response, feedback, and alternatives.
extreme_case|An Ecosystem Beyond Its Baseline|How was an exceptional ecological event verified?|Check measure, historical range, instrumentation, site coverage, and date.
classification_debate|Where Does One Ecosystem End?|Why do boundary choices change the conclusion?|Compare watershed, habitat, jurisdiction, and species movement definitions.
interacting_systems|When Two Ecosystems Connect|How do water, organisms, or nutrients cross a boundary?|Measure exchanges and avoid treating sites as isolated.
data_gap|The Missing Ecosystem Measurements|Which unobserved places or processes weaken a claim?|Map seasonal gaps, taxa, soil and water data, and method changes.
prediction_test|Did an Ecosystem Forecast Hold?|How did a prior projection compare with later measurements?|Match model version, assumptions, location, horizon, and indicators.
human_impact|Who Depends on This Ecosystem?|How are benefits and environmental costs distributed?|Compare water, food, risk, access, land rights, and local accounts.
field_field_sampling|A Repeatable Field Protocol|Which observations would answer one ecosystem question?|Choose plots, controls, timing, taxa, variables, and data quality checks.
field_land_use|A Land-Use Change Examined|How did one conversion alter ecosystem structure and function?|Compare prechange records, reference sites, policy, and measured response.
field_weather_variability|Weather Versus Lasting Change|How much of an observed ecological shift follows weather?|Compare multi-year climate and matched ecological series.
field_habitat_change|A Habitat Mosaic in Motion|Which habitat patches changed and what species responded?|Use repeat maps and field surveys with consistent classifications.
field_restoration_evidence|Did Restoration Work?|Which predeclared outcomes improved after one restoration project?|Compare baseline, controls, costs, maintenance, and long-term monitoring.
"""


if __name__ == "__main__":
    revise_domain("205", "205_ecosystems", ECOSYSTEMS,
                  "Ecosystems through defined boundaries, interactions, standardized field measurement, disturbance, land use, and restoration evidence.",
                  "dated ecosystem maps and land-use records, repeat field protocols, sensor calibration, long-term monitoring, reference sites, and consented local accounts",
                  "Name place, ecosystem boundary, measure, season, and time span. Distinguish one indicator from overall system health and correlation from a demonstrated causal pathway.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
