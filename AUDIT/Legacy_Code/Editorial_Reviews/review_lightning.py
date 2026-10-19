"""Editorial question designs for niche 216, Lightning."""

from review_angle_plans import audit, revise_domain


LIGHTNING = """history_origins|How Lightning Became Measurable|Which instruments changed understanding of one lightning property?|Compare dated observations, calibration, and interpretation.
famous_examples|A Famous Strike Claim Rechecked|What evidence supports a widely repeated lightning story?|Verify event time, location, strike detection, damage, and alternative causes.
hidden_stories|The People Behind Lightning Maps|Whose work turns sensor signals into usable event records?|Trace instrument teams, forecasters, validators, and local observers.
beginner_explainers|From Charge to Flash|How does charge separation lead to a lightning discharge?|Describe storm conditions and distinguish observed steps from open questions.
advanced_concepts|One Flash, Many Strokes|Why do datasets count lightning events differently?|Compare flash, stroke, pulse, sensor reach, and clustering method.
mysteries_unsolved_cases|An Unexpected Lightning Pattern|Which factors could explain a documented cluster or lull?|Test storm structure, sensor coverage, terrain, season, and error.
technology_innovation|Satellite Versus Ground Lightning Detection|Which system detects what kind of event?|Compare location accuracy, flash efficiency, coverage, latency, and validation.
people_personalities|A Lightning Research Decision|How did one named team test a disputed lightning mechanism?|Use original data, methods, critiques, and later evidence.
major_events|A Storm's Lightning Timeline|How did flashes evolve during one documented storm?|Match radar, sensors, storm phase, warnings, and impact records.
how_it_works|Inside a Lightning Channel|What observations show how a discharge develops?|Use high-speed imaging, electric-field measures, and uncertainty.
rise_fall|A Regional Lightning Trend|What supports a change in detected lightning frequency?|Account for sensor changes, coverage, storm climate, and counting rules.
then_vs_now|Lightning Observation Across Eras|How did better sensors change apparent event counts?|Compare same region, seasons, detection efficiency, and methods.
future_developments|Improving Lightning Warnings|Which measurable advance could improve lead time or reach?|State sensor, forecast, false-alarm, communication, and user assumptions.
myths_vs_facts|Lightning Never Strikes Twice?|What do location records show for one repeatedly struck site?|Define strike location, observation period, and detection limits.
documentary_stories|One Lightning Incident Investigated|What is established about a documented incident and its consequences?|Use official investigation, sensor record, weather, and consented accounts.
observation_to_explanation|A Flash in a Video|What can one clip establish?|Verify time, place, camera geometry, flash type, and source attribution.
measurement_method|Counting Lightning|How does a network locate and classify flashes?|Explain timing, triangulation, clustering, detection efficiency, and error.
scale_and_timespan|One Storm Versus a Climate Trend|At what scale is a lightning claim supported?|Define storm, region, season, years, and stable sensor coverage.
field_vs_lab|A Discharge in Lab and Storm|Which laboratory properties transfer to atmospheric lightning?|Compare scale, humidity, pressure, charge geometry, and observations.
natural_variation|Why Lightning Counts Swing|How much change follows ordinary storm variability?|Use long comparable records and convective weather context.
mechanism_chain|From Flash to Damage|Which evidence links a detected strike to an observed impact?|Trace strike location, current path, timing, inspection, and alternatives.
extreme_case|A Record Flash Verified|How was a claim of exceptional distance or duration checked?|Use official review, sensor data, definition, and uncertainty.
classification_debate|Cloud-to-Ground or In-Cloud?|Why do systems classify some events differently?|Compare waveforms, optical evidence, network algorithms, and validation.
interacting_systems|Lightning and Storm Dynamics|How do updrafts, ice, and precipitation relate to flash patterns?|Test measured links rather than treating flashes as a direct severity scale.
data_gap|Where Lightning Goes Unseen|Which areas or flash types are underdetected?|Map sensor density, range, ocean coverage, and algorithm limits.
prediction_test|Did a Lightning Forecast Hold?|How did a prediction compare with later detected activity?|Match issue time, region, lead time, event definition, and false alarms.
human_impact|Who Is Exposed to Lightning?|How do occupation, shelter, communication, and geography affect risk?|Use incident records and avoid blaming exposed people.
field_field_sampling|Evidence for a Lightning Event|Which measurements are needed to study one storm?|Specify radar, ground network, satellite, electric field, time sync, and approvals.
field_land_use|Built Environment and Exposure|How does one land-use pattern affect lightning consequences?|Separate strike frequency from shelter, structures, and human presence.
field_weather_variability|Weather Versus Detection Change|How much of an apparent trend follows sensor upgrades?|Compare stable-network periods and storm conditions.
field_habitat_change|A Lightning-Ignited Fire's Effects|What ecological change followed a verified ignition?|Separate ignition evidence from spread, drought, fuels, and management.
field_restoration_evidence|Did Lightning Risk Reduction Work?|Which outcomes improved after a site safety intervention?|Compare exposure, incidents, warning use, costs, and control periods.
"""


if __name__ == "__main__":
    revise_domain("216", "216_lightning", LIGHTNING,
                  "Lightning through storm physics, sensor definitions, event verification, forecasting, exposure, and impact evidence.",
                  "calibrated ground and satellite lightning observations, radar and weather archives, official incident investigations, instrument metadata, and verified event records",
                  "Name event, place, time, flash definition, and detection method. Do not infer individual strike risk from historical counts or use these research questions as current safety guidance; cite official live alerts when needed.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
