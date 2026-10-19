"""Editorial question designs for niche 217, Clouds & Atmosphere."""

from review_angle_plans import audit, revise_domain


CLOUDS = """history_origins|How Clouds Became Classified|Which observation rules made cloud descriptions comparable?|Trace historical atlases, names, photographs, and revisions.
famous_examples|An Unusual Cloud Rechecked|What evidence supports a claimed rare cloud form?|Check image time, location, viewing angle, WMO criteria, and weather setting.
hidden_stories|The Observers Behind Cloud Records|Whose work turns sky views into consistent data?|Trace surface observers, satellite teams, pilots, forecasters, and archivists.
beginner_explainers|Reading a Cloud Layer|Which features identify one cloud genus and what cannot be inferred?|Use official criteria, height, texture, precipitation, and uncertainty.
advanced_concepts|Clouds and Radiation|How can a cloud both reflect sunlight and trap outgoing heat?|Compare height, thickness, particle type, day or night, and measured flux.
mysteries_unsolved_cases|Why One Cloud Layer Persisted|Which conditions explain a documented cloud event?|Test moisture, temperature inversion, lift, wind, and aerosols.
technology_innovation|Clouds from Satellite|Which cloud properties can one satellite channel retrieve?|Compare resolution, viewing angle, calibration, cloud overlap, and ground checks.
people_personalities|A Cloud Classification Choice|How did one named scientist or committee change terminology?|Use original proposal, observations, objections, and adopted standard.
major_events|Clouds During a Weather Event|How did cloud structure evolve before one storm?|Match satellite, radar, surface observations, and timing.
how_it_works|From Vapor to Droplets|Which conditions cause a cloud to form and persist?|Trace cooling, saturation, aerosols, mixing, and measured evidence.
rise_fall|A Cloud-Cover Trend|What supports a regional change in cloud amount?|Compare instruments, observation time, satellite calibration, and uncertainty.
then_vs_now|Cloud Observation Across Eras|How do manual logs and satellites differ?|Match region, season, cloud variable, observer bias, and method.
future_developments|Clouds in a Changing Climate|Which uncertainties matter for one cloud feedback?|Specify region, cloud type, model assumptions, and observations.
myths_vs_facts|Can One Cloud Predict Rain?|How well does one observed form predict local precipitation?|Compare base rates, humidity, dynamics, forecast horizon, and false alarms.
documentary_stories|A Sky Observation Investigated|What created one documented unusual cloud scene?|Use time-stamped images, weather data, satellite view, and classification.
observation_to_explanation|One Dramatic Cloud Photo|What can a photograph establish?|Verify location, time, lens, perspective, classification, and weather context.
measurement_method|Measuring Cloud Cover|How do observers, lidar, and satellites estimate a cloud variable?|Compare definition, vertical layers, resolution, calibration, and error.
scale_and_timespan|One Sky Versus a Climate Pattern|At what scale is a cloud claim supported?|Define station, region, season, years, and sampling frequency.
field_vs_lab|Droplets in a Cloud Chamber|Does a lab result predict atmospheric cloud behavior?|Compare aerosols, temperature, turbulence, scale, and field validation.
natural_variation|Normal Cloudiness or Trend?|How much cloud cover varies with weather patterns?|Use long stable records and circulation context.
mechanism_chain|From Aerosols to Cloud Change|Which evidence links particles to a measured cloud effect?|Trace source, concentration, nucleation, droplet response, and alternatives.
extreme_case|An Exceptional Cloud Observation|How was a rare cloud height or form verified?|Check instrument, classification, metadata, and independent imagery.
classification_debate|Which Cloud Name Fits?|Why do trained observers disagree over one cloud form?|Apply WMO criteria, height, transition states, and image limitations.
interacting_systems|Clouds, Surface, and Air|How do land or ocean conditions interact with one cloud regime?|Compare moisture, heat, aerosols, circulation, and feedback.
data_gap|Clouds Hidden from a Sensor|Which layers or conditions does one observing system miss?|Map night, cloud overlap, polar coverage, surface glare, and resolution.
prediction_test|Did a Cloud Forecast Hold?|How did predicted cloud cover compare with observations?|Match valid time, region, cloud level, verification method, and error.
human_impact|Cloud Information in Decisions|Who uses cloud observations and with what limits?|Examine aviation, solar energy, agriculture, and warning contexts.
field_field_sampling|A Cloud Observation Protocol|Which variables and timing make one cloud question testable?|Specify cloud amount, genus, height, weather, photographs, and standards.
field_land_use|Surface Change and Local Clouds|Did one land-use change alter a local cloud pattern?|Compare heat, moisture, circulation, season, and controls.
field_weather_variability|Weather Versus Cloud Trend|How much apparent change follows shifting circulation?|Use comparable long records and circulation indices.
field_habitat_change|Cloud or Fog and a Habitat|How does a cloud regime affect moisture at one site?|Measure fog interception, soil water, vegetation, and alternative sources.
field_restoration_evidence|Can Landscape Management Alter Fog Water?|Which measurable result followed one local intervention?|Compare water capture, ecology, cost, weather controls, and limits.
"""


if __name__ == "__main__":
    revise_domain("217", "217_clouds_atmosphere", CLOUDS,
                  "Clouds and atmosphere through standardized classification, formation mechanisms, radiation, observation methods, forecasting, and local effects.",
                  "WMO cloud classification, calibrated surface and satellite observations, radar and lidar records, weather archives, and peer-reviewed field or model studies",
                  "Name cloud type, location, observation time, instrument, and classification standard. Do not turn a single sky photo into a weather forecast or climate trend; use current official forecasts for decisions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
