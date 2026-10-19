"""Editorial question designs for niche 211, Waterfalls."""

from review_angle_plans import audit, revise_domain


WATERFALLS = """history_origins|How One Waterfall Formed|Which rock, river, and erosion processes created a named fall?|Use geologic maps, channel profiles, dated sediments, and uncertainty.
famous_examples|A Celebrated Waterfall Rechecked|What makes one famous fall distinctive under comparable measures?|Define height, width, discharge, season, and measurement method.
hidden_stories|People Behind a Waterfall Site|Whose labor and land knowledge shape access and stewardship?|Trace Indigenous and local knowledge, site workers, guides, and managers with consent.
beginner_explainers|Reading a Waterfall Landscape|How do upstream channel, ledge, plunge pool, and gorge connect?|Use one site, flow range, rock type, and maps.
advanced_concepts|Height, Flow, and Appearance|Why can waterfall rankings change with definition and season?|Compare vertical drop, cascades, discharge, seasonal flow, and data quality.
mysteries_unsolved_cases|Why a Fall Changed Course|Which evidence explains a documented shift in a waterfall?|Test erosion, landslide, flood, engineering, or mapping error.
technology_innovation|Mapping a Dangerous Drop|Does lidar or photogrammetry improve waterfall measurements?|Compare datum, water spray, access, resolution, and ground checks.
people_personalities|A Waterfall Access Decision|How did one named steward or manager change visitor access?|Use rights, safety records, design plans, local input, and outcomes.
major_events|After a Rockfall or Flood|What changed at one waterfall after a documented event?|Compare channel geometry, flow, closures, habitat, and recovery.
how_it_works|The Making of a Gorge|How do water, rock resistance, and sediment move a fall over time?|Use measured rates where available and state uncertainty.
rise_fall|Changing Waterfall Flow|What supports an increase or decline in flow at one fall?|Use upstream gauges and account for diversion, season, drought, and dams.
then_vs_now|A Waterfall Across Two Periods|How have flow, landform, access, and use changed?|Match date, season, viewpoint, gauge, and map method.
future_developments|Scenarios for One Waterfall|Which plausible conditions could alter flow or access?|State climate, water management, erosion, infrastructure, and uncertainty.
myths_vs_facts|The Tallest Waterfall Claim|How do measurement choices affect a superlative?|Compare single drop versus total cascades, datum, evidence, and independent survey.
documentary_stories|A Fall's Turning Point|How did one documented event change a waterfall landscape?|Trace dated maps, flow, site accounts, decisions, and subsequent monitoring.
observation_to_explanation|A Powerful Waterfall Image|What can one photograph establish about flow?|Separate appearance from discharge, season, flood risk, and long-term trend.
measurement_method|Measuring a Waterfall|How are height and water flow measured at one site?|Explain vertical datum, survey alignment, upstream gauge, timing, and uncertainty.
scale_and_timespan|A Fall Versus Its Watershed|At what scale is a waterfall change claim supported?|Define waterfall site, upstream basin, season, years, and water use.
field_vs_lab|Erosion in Model and Gorge|Does a flume result explain one fall's retreat?|Compare rock layers, sediment load, flow variation, and field evidence.
natural_variation|Seasonal Flow at a Fall|How much visible change is expected through a year?|Use repeated gauge data and comparable images.
mechanism_chain|From Diversion to Falls Habitat|Which evidence links water withdrawal to downstream ecological change?|Trace intake, flow, spray zone, species, and alternative drivers.
extreme_case|A Record Waterfall Measurement|How was an exceptional height or flow claim verified?|Check method, dates, drop definition, and independent replication.
classification_debate|What Counts as One Waterfall?|Why do lists disagree about cascades and total height?|Compare continuous drop, steps, channel separation, and conventions.
interacting_systems|Falls, Gorge, and River Life|How do flow and spray shape one local habitat?|Use measured moisture, plants, fish passage, and geology.
data_gap|What We Cannot Measure at the Falls|Which seasons or points are missing from the record?|Map gauge distance, inaccessible ledges, floods, and survey uncertainty.
prediction_test|Did a Flow Forecast Hold?|How did predicted waterfall flow compare with later gauge data?|Match forecast issue date, upstream operations, rainfall, and observations.
human_impact|Who Uses a Waterfall Site?|How are tourism benefits, water rights, site risk, and conservation costs shared?|Use visitor data, local accounts, and management records.
field_field_sampling|A Safe Waterfall Survey Plan|Which remote and permitted measures answer one site question?|Choose maps, gauges, imagery, habitat plots, dates, and access boundaries.
field_land_use|Upstream Change, Downstream Fall|How did one land or water-use change affect a waterfall?|Compare upstream records, flow, sediment, and reference periods.
field_weather_variability|Rainfall Versus Structural Change|How much of a dramatic visual shift follows ordinary weather?|Use multi-year gauges, season, and comparable images.
field_habitat_change|The Spray-Zone Habitat|Which organisms changed near a waterfall?|Compare repeated surveys, moisture, disturbance, and access effects.
field_restoration_evidence|Did Waterfall-Site Restoration Help?|Which ecological or access outcomes improved after intervention?|Check flow, habitat, visitor safety, cost, and long-term monitoring.
"""


if __name__ == "__main__":
    revise_domain("211", "211_waterfalls", WATERFALLS,
                  "Waterfalls through geology, water flow, measurement definitions, gorge habitat, land and water use, and responsible access.",
                  "geologic and topographic surveys, calibrated upstream gauges, repeat imagery with dates, site management records, habitat observations, and consented local accounts",
                  "Name waterfall, watershed, season, drop definition, and date. Do not equate photograph appearance with measured flow or infer access safety from historic descriptions; verify current closures and alerts.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
