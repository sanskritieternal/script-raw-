"""Editorial question designs for niche 210, Rivers."""

from review_angle_plans import audit, revise_domain


RIVERS = """history_origins|How a River Found Its Course|Which geologic and climate changes shaped one river reach?|Use dated landforms, sediments, maps, and uncertainty.
famous_examples|A Famous River Recovery Rechecked|Which outcomes improved after one river intervention?|Compare baseline flow, sediment, habitat, species, and community effects.
hidden_stories|Who Measures and Maintains a River?|Whose work produces flow data and keeps a river usable?|Trace gauge crews, local stewards, water users, engineers, and analysts.
beginner_explainers|Reading a River Basin|How do headwaters, tributaries, channel, floodplain, and outlet connect?|Map one named basin with land and water use.
advanced_concepts|Stage Is Not Discharge|Why can the same water level imply different flows?|Explain channel shape, rating curve, sediment change, and calibration.
mysteries_unsolved_cases|An Unexpected Low-Flow Reach|Which factors explain a documented flow decline?|Test rainfall, snow, diversions, groundwater, storage, and instrument changes.
technology_innovation|A New River Sensor Tested|Does one instrument improve flow or water-quality estimates?|Compare calibration, site limitations, missing data, and field checks.
people_personalities|A River Management Decision|How did one named community or official change allocation or access?|Use rights, plans, public input, implementation, and outcomes.
major_events|After a River Flood|What changed in channel, floodplain, and community after one flood?|Compare pre-event maps, peak flow, sediment, damage, and recovery.
how_it_works|From Rain to Streamflow|How do precipitation, storage, infiltration, and routing shape one river hydrograph?|Specify basin, season, gauges, and uncertainty.
rise_fall|A River's Flow Trend|What supports a persistent change in discharge?|Use long comparable gauge series and account for dams, withdrawals, and climate.
then_vs_now|A River Reach Across Two Eras|How have flow, channel, land use, and habitat changed?|Match season, gauge location, map method, and definitions.
future_developments|Scenarios for a River Basin|Which plausible conditions could alter flows and habitat?|State climate, demand, storage, land use, and policy assumptions.
myths_vs_facts|Is a Straightened River Safer?|What evidence shows the effects of channel straightening at one reach?|Compare flood risk, erosion, habitat, maintenance, and downstream effects.
documentary_stories|A River Decision Reconstructed|Why did one dam, diversion, or restoration decision happen?|Trace dated proposals, rights, monitoring, and affected voices.
observation_to_explanation|One High-Water Photograph|What can a flood image establish?|Separate local stage, discharge, recurrence, cause, and risk.
measurement_method|How a Streamgage Works|How does stage become a discharge estimate?|Explain datum, velocity measurements, rating curve, revisions, and uncertainty.
scale_and_timespan|One Reach Versus a Basin|At what scale is a river claim supported?|Define drainage area, reach, season, years, and observation coverage.
field_vs_lab|Sediment Movement in Nature|Does a flume result predict one river's channel change?|Compare grain size, flow variability, vegetation, and field validation.
natural_variation|Seasonal Highs and Lows|How much flow variation is expected in one river?|Use long records and climate context before trend claims.
mechanism_chain|From Land Use to Water Quality|Which evidence links a land change to downstream conditions?|Trace runoff, pollutant transport, timing, concentrations, and alternatives.
extreme_case|A Record River Flood|How was an exceptional flow or stage verified?|Check gauge datum, rating curve, flood marks, time, and uncertainty.
classification_debate|Where a River Begins or Ends|Why do definitions change river length or status?|Compare source, channel, flow permanence, and mapping conventions.
interacting_systems|River and Floodplain Together|How do seasonal connections affect sediment, nutrients, and habitat?|Measure exchanges rather than treating channel as isolated.
data_gap|Ungauged Parts of a Basin|Which reaches or seasons lack direct measurements?|Map gauges, tributaries, flood events, water use, and model dependence.
prediction_test|Did a River Forecast Hold?|How did a flow or flood prediction compare with later gauges?|Match issue date, lead time, basin, observed value, and uncertainty.
human_impact|Who Depends on This River?|How are water, flood risk, livelihoods, and ecosystem needs distributed?|Use rights, measured use, local accounts, and trade-offs.
field_field_sampling|A Reach Survey Designed Well|Which measurements answer one river question?|Choose cross-sections, discharge, sediment, habitat, timing, and controls.
field_land_use|A Basin Conversion's Effect|How did one land-use change affect runoff or river ecology?|Compare before and after data, weather, reference basins, and mechanisms.
field_weather_variability|Weather Versus Management|How much of a flow change reflects climate rather than a water decision?|Use matched precipitation, snow, storage, withdrawal, and gauge data.
field_habitat_change|A River Habitat Mosaic|Which riffles, pools, banks, or floodplain areas changed?|Compare repeat maps, flow, sediment, and species surveys.
field_restoration_evidence|Did River Restoration Work?|Which predefined outcomes improved after intervention?|Compare flow, habitat, species, risk, cost, and long-term controls.
"""


if __name__ == "__main__":
    revise_domain("210", "210_rivers", RIVERS,
                  "Rivers through basin boundaries, measured discharge, sediment, floodplains, water rights, ecological change, and restoration evidence.",
                  "calibrated streamgage records and methods, basin maps, land and water-use records, sediment and water-quality surveys, habitat monitoring, and consented local accounts",
                  "Name river reach, basin, gauge, jurisdiction, season, and date. Distinguish water level from discharge and a single event from a long-term trend; use current official alerts for flood safety.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
