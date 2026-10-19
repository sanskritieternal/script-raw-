"""Editorial question designs for niche 215, Extreme Weather."""

from review_angle_plans import audit, revise_domain


EXTREME_WEATHER = """history_origins|How an Extreme Record Was Established|Which observations first documented one named weather extreme?|Trace instrument, station, date, metadata, and later verification.
famous_examples|A Famous Weather Record Rechecked|Does one widely repeated record meet the relevant standard?|Check category, instrument, station history, quality control, and archive ruling.
hidden_stories|The People Behind Warnings and Data|Whose observations and communication work support one event account?|Trace forecasters, field observers, local responders, data teams, and affected people.
beginner_explainers|Extreme Relative to What?|How is one event classified as extreme?|Define variable, location, season, baseline, threshold, and return period.
advanced_concepts|Hazard, Exposure, and Vulnerability|Why can similar weather produce different losses?|Compare physical intensity, settlement, infrastructure, warnings, and capacity.
mysteries_unsolved_cases|An Unexpected Local Impact|Which factors explain damage beyond a forecast?|Test observation gaps, compound hazards, land use, infrastructure, and uncertainty.
technology_innovation|A Weather Sensor or Model Tested|Did one tool improve event detection or warning?|Compare lead time, false alarms, calibration, reach, and user response.
people_personalities|A Warning Decision Reconstructed|How did one named team decide what to communicate?|Use forecast versions, uncertainty, procedures, timing, and review.
major_events|One Event's Full Timeline|How did a documented extreme weather event develop and affect a place?|Match observations, forecasts, warnings, impacts, and later analysis.
how_it_works|Mechanism of One Weather Extreme|Which atmospheric processes produced a defined event?|Trace moisture, heat, circulation, terrain, and observation evidence.
rise_fall|Has This Extreme Become More Common?|What supports a trend for one hazard in one region?|Check consistent records, definitions, station changes, and uncertainty.
then_vs_now|Two Events on Equal Terms|How do two historic events compare after measurement and exposure are aligned?|Match variable, area, duration, baseline, damage units, and population.
future_developments|Scenarios for One Hazard|Which conditions could alter its future frequency or impact?|State emissions or climate scenario, land use, exposure, adaptation, and model spread.
myths_vs_facts|One Event Proves Climate Change?|What can an event attribution study actually conclude?|Distinguish weather mechanism, probability shift, intensity change, and uncertainty.
documentary_stories|From Forecast to Aftermath|What did official records and consented accounts show for one event?|Build a dated sequence and protect affected people's privacy and dignity.
observation_to_explanation|One Viral Weather Image|What can a photograph or clip establish?|Verify time, place, variable, context, and whether it represents wider conditions.
measurement_method|Verifying an Extreme Observation|How is a candidate record checked?|Examine sensor siting, calibration, metadata, neighboring stations, and expert review.
scale_and_timespan|One Station Versus a Region|At what scale is an extreme weather claim valid?|Define station, event footprint, season, return period, and record length.
field_vs_lab|A Weather Mechanism in Models|Does a modeled process reproduce a real event?|Compare observations, resolution, initial conditions, ensembles, and limitations.
natural_variation|Weather Noise and Long Trends|How much event variation can occur without a persistent trend?|Use long records and physically relevant covariates.
mechanism_chain|From Rain to Flood Loss|Which evidence links weather to human damage?|Trace rainfall, runoff, exposure, land use, infrastructure, and response.
extreme_case|The Record Holder's Evidence|How was one world or regional extreme accepted or rejected?|Use archive ruling, instrument record, category, and updated status.
classification_debate|What Counts as an Extreme?|How do thresholds and event boundaries change a count?|Compare percentile, absolute limit, duration, spatial area, and hazard type.
interacting_systems|Compound Weather Hazards|How did two conditions combine to increase impact?|Examine dependence, timing, exposure, and alternative drivers.
data_gap|The Event We Did Not Observe Well|Which missing sensors or reports limit conclusions?|Map station gaps, damaged instruments, inaccessible areas, and reporting bias.
prediction_test|Did a Warning Forecast Hold?|How did issued forecast and warning compare with observed conditions?|Match issue time, lead, location, threshold, uncertainty, and user response.
human_impact|Who Was Most Exposed?|How did one event affect different communities?|Compare location, housing, access to warning, services, and documented outcomes.
field_field_sampling|Building an Event Evidence File|Which observations are needed for one extreme claim?|Collect station metadata, radar or satellite, gauges, timing, and quality checks.
field_land_use|Land Use and Weather Damage|How did development change exposure to a defined hazard?|Separate weather intensity from drainage, surface, housing, and policy.
field_weather_variability|Event Versus Climate Signal|How do researchers separate variability from a changed probability?|Compare baseline, ensembles, physical mechanism, and uncertainty.
field_habitat_change|Ecological Effects of One Event|Which habitat changes followed an extreme event?|Use before and after surveys, reference sites, and recovery time.
field_restoration_evidence|Did an Adaptation Reduce Loss?|Which predeclared outcome improved after one resilience project?|Compare similar events, exposure, maintenance, cost, and unequal effects.
"""


if __name__ == "__main__":
    revise_domain("215", "215_extreme_weather", EXTREME_WEATHER,
                  "Extreme weather through verified observations, event mechanisms, forecast performance, attribution, exposure, and adaptation outcomes.",
                  "quality-controlled station metadata and measurements, official warnings and forecast archives, event investigations, peer-reviewed attribution analyses, and consented affected-community accounts",
                  "Name hazard, event, location, duration, baseline, and source date. Distinguish a verified record, forecast, trend, and attribution claim; use current official warnings for operational safety.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
