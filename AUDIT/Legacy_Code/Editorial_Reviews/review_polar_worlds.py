"""Editorial questions for ice and polar worlds."""

from review_angle_plans import audit, revise_domain


POLAR = """history_origins|How a Glacier Began|Which evidence reconstructs one glacier's formation and past extent?|Use landforms, dated cores, maps, and local historical records.
famous_examples|A Well-Known Ice Shelf Breakup|What observations establish one breakup's sequence and causes?|Compare satellite images, ocean, atmosphere, and glaciology research.
hidden_stories|People Behind Polar Measurements|Who gathers, calibrates, maintains, and interprets observations?|Credit field teams, local observers, data managers, and partners.
beginner_explainers|Sea Ice, Glacier, and Ice Sheet|How do three forms of ice differ in formation and measurement?|Use clear examples and avoid applying one trend to all ice.
advanced_concepts|Ice Loss and Sea Level|Which kinds of ice change sea level and through what mechanisms?|Separate floating and land ice, mass balance, ocean effects, and timescales.
mysteries_unsolved_cases|A Gap in the Ice Record|Which observations are missing for one place or period?|Compare satellites, field logs, models, and alternative reconstructions.
technology_innovation|A Satellite View of Ice|What can one sensor reveal about thickness or extent?|Check resolution, algorithm, validation, cloud or darkness limits.
people_personalities|An Observer's Route to Evidence|How did one scientist or community observer document ice change?|Use dated logs, methods, collaboration, and credited knowledge.
major_events|An Exceptional Melt Season|Which conditions produced one unusual season?|Compare weather, ocean, snow, baseline, and observation window.
how_it_works|How Sea Ice Forms and Moves|Which processes explain ice growth and drift in a named region?|Use ocean, wind, temperature, and measured ice state.
rise_fall|A Glacier's Advance and Retreat|How has one glacier changed across several decades?|Use comparable outlines, thickness, mass balance, and uncertainty.
then_vs_now|The Same Polar Place Across Time|What do matched observations show and conceal?|Align season, location, sensor, and measurement definition.
future_developments|A Polar Forecast Under Review|What range of future ice conditions is projected for one region?|Specify scenario, model ensemble, timescale, and limits.
myths_vs_facts|One Cold Year and the Long Trend|Does a short-term increase refute a longer ice trend?|Compare season, baseline, geography, metric, and uncertainty.
documentary_stories|Following an Ice Measurement|How does one observation become a published data point?|Trace instrument, calibration, processing, review, and revision.
observation_to_explanation|A Dark Patch on Snow|What could explain a measured surface change?|Compare impurities, melt, shadow, sensor artifacts, and sampling.
measurement_method|What Does Ice Extent Measure?|How is an ice threshold converted into an area or extent series?|Explain grid, concentration cutoff, sensor, and version changes.
scale_and_timespan|A Season, a Decade, an Ice Age|What questions can each ice timescale answer?|Use appropriate records and avoid extrapolating between scales.
field_vs_lab|An Ice Core from Field to Freezer|How do collection and laboratory analysis preserve its signal?|Trace site, depth, contamination, storage, dating, and uncertainty.
natural_variation|Ice Variability Within a Trend|Which regional and seasonal changes can occur around a long trend?|Use multiple years, comparable methods, ocean and atmosphere context.
mechanism_chain|From Warm Water to Ice Loss|Which observations connect ocean conditions to one glacier change?|Test temperature, circulation, grounding line, and alternative drivers.
extreme_case|The Record Low in Context|What makes one ice minimum exceptional and how reliable is the record?|Specify data start, metric, season, method, and uncertainty.
classification_debate|What Counts as Permanent Ice?|How do datasets classify snow, firn, glacier, and sea ice?|Compare definitions, thresholds, and intended uses.
interacting_systems|Ice, Ocean, and Ecosystem|How did changing ice alter a documented ecological relationship?|Compare habitat, species observations, ocean conditions, and other causes.
data_gap|A Region Satellites See Poorly|Which ice questions remain uncertain because of coverage or resolution?|Map limitations, field validation, and modeled assumptions.
prediction_test|Testing a Past Projection|How did a dated ice projection compare with later measurements?|Match scenario, region, metric, baseline, and uncertainty range.
human_impact|Travel and Livelihood on Changing Ice|How do people describe practical changes in one place?|Use community-led observation, consent, and current safety sources.
field_field_sampling|Choosing an Ice Sample|How does site selection affect what a sample can represent?|Check access, permit, stratigraphy, contamination, and qualified safety.
field_land_use|Structures on Frozen Ground|How does ground-ice change affect one settlement or route?|Compare soil, temperature, engineering records, maintenance, and local needs.
field_weather_variability|A Forecast and Polar Travel|How do rapidly changing conditions affect one planned operation?|Use official forecasts, local expertise, documented decisions, and alternatives.
field_habitat_change|An Ice-Dependent Habitat|What measured changes occurred for one species in one region?|Compare ice habitat, population methods, food web, and other pressures.
field_restoration_evidence|An Adaptation Project in the North|Did one community-led project meet its stated goals?|Compare baseline, monitoring, local priorities, cost, and maintenance.
"""


if __name__ == "__main__":
    revise_domain("153", "153_ice_polar_worlds", POLAR,
                  "Polar ice through observation, physical mechanisms, seasonal variability, long trends, ecosystems, and community experience.",
                  "versioned satellite and field datasets, ice-core and glacier records, documented methods and uncertainty, peer-reviewed process studies, and consented community-led observations",
                  "Name region, ice type, metric, period, and dataset version. Distinguish weather from climate and floating from land ice; honor Indigenous knowledge and consent; use current official safety information for travel.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
