"""Editorial questions for volcanoes."""

from review_angle_plans import audit, revise_domain


VOLCANOES = """history_origins|How One Volcano Formed|Which evidence explains a named volcano's growth?|Use geologic maps, dated rocks, and regional tectonic context.
famous_examples|A Famous Eruption Revisited|What do observations establish about one eruption's sequence?|Compare contemporary records, deposits, maps, and later analysis.
hidden_stories|Work Behind a Volcano Warning|Who maintains instruments, models, access, and local communication?|Follow observatory, emergency staff, and community roles.
beginner_explainers|Reading a Volcano Alert|What does one current alert level mean and not mean?|Use the issuing agency's definitions, date, area, and uncertainty.
advanced_concepts|Forecasting Without a Clock|How do monitoring changes inform a probabilistic eruption forecast?|Compare baseline, signals, past behavior, scenarios, and limits.
mysteries_unsolved_cases|A Volcano's Unexpected Behavior|Which observations challenge an earlier explanation?|Trace dated forecast, actual event, model revision, and uncertainty.
technology_innovation|Remote Sensing of Unrest|What can one satellite method detect that ground sensors miss?|Compare resolution, revisit time, validation, and blind spots.
people_personalities|A Scientist's Warning Decision|How did a named team weigh evidence and communicate risk?|Use dated bulletins, protocols, and attributed accounts.
major_events|An Eruption and Its Consequences|How did one event affect people, ecosystems, and infrastructure?|Map hazards, exposure, warnings, response, and recovery by date.
how_it_works|From Magma to Surface Hazard|Which processes link magma movement to one documented hazard?|Use site-specific observations and distinguish mechanisms.
rise_fall|A Volcano's Active and Quiet Periods|What do records reveal about changing activity?|Compare dated deposits, monitoring, reporting gaps, and timescales.
then_vs_now|Monitoring the Same Volcano Over Time|How did instruments and warning practice change?|Compare historical observations, current networks, and forecast limits.
future_developments|A Proposed Monitoring Upgrade|Which uncertainty would one added sensor reduce?|Check coverage, power, maintenance, cost, and response capacity.
myths_vs_facts|Can Eruptions Be Predicted Exactly?|What could scientists say before one eruption and with what confidence?|Compare contemporaneous forecast to outcome, avoiding hindsight.
documentary_stories|A Week at a Volcano Observatory|How does a team turn signals into public information?|Follow routine, anomalies, review, bulletin, and community communication.
observation_to_explanation|A Swarm of Earthquakes|What explanations fit one observed volcanic earthquake swarm?|Compare location, depth, gas, deformation, history, and alternatives.
measurement_method|Measuring Ground Deformation|How is one volcano's changing surface measured?|Explain instrument, reference frame, noise, calibration, and uncertainty.
scale_and_timespan|Days of Unrest, Millennia of Building|How do short signals relate to long volcanic history?|Compare monitoring windows with dated geologic record.
field_vs_lab|From Ash Deposit to Analysis|How do field samples and laboratory tests constrain an eruption story?|Track location, contamination, dating, chemistry, and inference.
natural_variation|What Is Normal for This Volcano?|How is baseline activity established and revised?|Use long records, seasonal effects, instrument changes, and gaps.
mechanism_chain|Why Ash Reached This Place|Which eruption and weather processes explain a documented ashfall?|Combine plume, wind, particle, and local observation data.
extreme_case|A Rare Large Eruption in Context|How does one extreme event compare with typical activity?|Use consistent measures, dated deposits, and reporting uncertainty.
classification_debate|What Counts as an Active Volcano?|How do agencies classify one volcano differently?|Compare criteria, time windows, hazard use, and uncertainty.
interacting_systems|Rain on Fresh Volcanic Deposits|How can weather alter hazard after an eruption?|Use rainfall, terrain, deposit, and event records.
data_gap|A Poorly Monitored Volcano|Which decisions are harder when sensors or history are missing?|Map coverage, local observations, communication, and uncertainty.
prediction_test|Evaluating an Old Forecast|How well did one dated forecast characterize possible outcomes?|Preserve original wording, probabilities, timeline, and actual events.
human_impact|Living Near a Volcano|How do residents balance livelihood, attachment, and hazard?|Use varied consented accounts, land use, and current plans.
field_field_sampling|Collecting Evidence Safely|What makes a volcanic sample scientifically interpretable?|Document site, date, permissions, chain of custody, and qualified safety plan.
field_land_use|A Hazard Map and Land Decisions|How does one community use volcanic hazard zones?|Compare map assumptions, planning rules, enforcement, and livelihoods.
field_weather_variability|Wind Changes an Ashfall Scenario|How does weather alter where ash may travel?|Compare forecast ensembles with measured plume and deposition.
field_habitat_change|Life After an Eruption|Which ecological changes are measured in one affected area?|Use repeat surveys, baseline, succession, and land-use context.
field_restoration_evidence|Rebuilding on Volcanic Ground|Which recovery actions helped and which remain uncertain?|Compare goals, monitoring, maintenance, and affected people's views.
"""


if __name__ == "__main__":
    revise_domain("152", "152_volcanoes", VOLCANOES,
                  "Volcanoes through geologic evidence, monitoring, forecast uncertainty, hazards, community decisions, and ecological change.",
                  "geologic maps and dated samples, observatory time series and archived bulletins, official hazard maps, meteorological records, and consented local accounts",
                  "Name volcano, area, event, and date. Use current official alerts for any present hazard, never imply exact prediction, and keep field access and sampling with qualified authorities and permissions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
