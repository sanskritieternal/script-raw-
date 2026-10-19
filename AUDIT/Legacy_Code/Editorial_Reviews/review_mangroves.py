"""Editorial question designs for niche 209, Mangroves."""

from review_angle_plans import audit, revise_domain


MANGROVES = """history_origins|How a Mangrove Shoreline Formed|Which tidal, sediment, and plant processes shaped one stand?|Use cores, shoreline maps, hydrology, and dated vegetation records.
famous_examples|A Celebrated Mangrove Planting Rechecked|Did one project create a functioning mangrove habitat?|Compare seedling survival, natural recruitment, hydrology, fauna, costs, and reference sites.
hidden_stories|People Who Steward the Tide|Whose knowledge and work sustain one mangrove landscape?|Attribute local harvesters, Indigenous stewards, fishers, nursery workers, and monitors with consent.
beginner_explainers|What Mangroves Need|How do tidal exchange, salinity, sediment, and species traits interact?|Use one site and distinguish mangrove plants from the whole ecosystem.
advanced_concepts|Restoration Starts with Water|Why can planting fail when tidal hydrology is wrong?|Compare elevation, inundation, drainage barriers, species, and natural recruitment.
mysteries_unsolved_cases|Why a Mangrove Stand Did Not Recover|Which factors explain failure after a storm or intervention?|Test water flow, salinity, sediment, propagules, pollution, and land use.
technology_innovation|Fine-Scale Mangrove Mapping|Does one remote-sensing method improve extent and condition estimates?|Compare canopy classification, tide stage, cloud cover, and field plots.
people_personalities|A Coastal Stewardship Choice|How did one named community or manager change mangrove governance?|Use tenure, participation, plan, implementation, and outcomes.
major_events|After a Coastal Storm|What changed in one mangrove stand after a documented storm?|Compare wind, surge, sediment, mortality, recruitment, and repeat storms.
how_it_works|Tides in a Mangrove Stand|How do water flow and sediment affect root habitat and establishment?|Specify site elevation, species, tide cycle, and field measures.
rise_fall|A Mangrove Extent Trend|What supports a gain or loss at one coast?|Match maps, classification, tide and season, ground checks, and land use.
then_vs_now|One Estuary Across Surveys|Which differences in mangrove cover and condition are real?|Compare imagery, plot design, species, hydrology, and dates.
future_developments|A Mangrove Coast Under Sea-Level Change|Which conditions shape possible landward migration?|State sediment supply, elevation, barriers, land rights, and scenarios.
myths_vs_facts|Does Planting Equal Restoration?|What outcomes distinguish a planted site from a recovered mangrove ecosystem?|Check hydrology, native species, fauna, function, survival, and time.
documentary_stories|A Restoration Decision Reconstructed|Why was one site planted or reconnected to the tide?|Trace original problem, alternatives, permits, community input, and monitoring.
observation_to_explanation|A Green Shoreline Image|What can one satellite image establish about mangroves?|Separate canopy presence from species, age, water regime, and function.
measurement_method|Monitoring a Mangrove Stand|How are extent, structure, and ecological condition measured?|Explain imagery, plots, elevation, salinity, recruitment, and uncertainty.
scale_and_timespan|One Plot Versus an Estuary|At what scale does a mangrove claim hold?|Define stand, creek, estuary, years, and sampling coverage.
field_vs_lab|Salt Tolerance in the Field|Does a controlled salinity response predict establishment?|Compare species, inundation, soil, competition, and field survival.
natural_variation|Normal Tidal and Seasonal Change|How much apparent site change reflects tide or season?|Use repeated measurements and consistent image timing.
mechanism_chain|From Culvert to Fish Habitat|Which evidence links restored tidal flow to ecological response?|Trace hydrology, salinity, plant recruitment, habitat structure, and fish use.
extreme_case|An Exceptional Mangrove Record|How was a record carbon, height, or storm-protection claim measured?|Check site, boundary, method, comparison, and uncertainty.
classification_debate|Which Shore Trees Are Mangroves?|How do species and habitat definitions change mapped extent?|Compare taxonomy, salinity, tidal influence, and regional conventions.
interacting_systems|Mangroves, Seagrass, and Reefs|How do materials or animals move among coastal habitats?|Use measured connectivity rather than assumed universal nursery value.
data_gap|Where Mangrove Maps Mislead|Which narrow creeks or degraded stands are missed?|Map resolution, tide, species identification, field access, and validation.
prediction_test|Did a Restoration Forecast Hold?|Did predicted recruitment or protection match later observations?|Compare model assumptions, site hydrology, storm exposure, and monitoring.
human_impact|Who Benefits from Mangroves?|How do fishing, wood use, coastal protection, and restrictions affect people?|Compare rights, livelihoods, hazards, ecological outcomes, and local testimony.
field_field_sampling|A Mangrove Baseline Plot|Which measures should a restoration project record first?|Include elevation, tidal exchange, salinity, species, seedling recruitment, and reference sites.
field_land_use|A Changed Mangrove Shore|How did a road, pond, or building alter tidal exchange?|Trace maps, permits, hydrology, vegetation, and community effects.
field_weather_variability|Storm Effects Versus Lasting Decline|How much of a change follows one weather event?|Compare pre-event records, repeat observations, and hydrologic context.
field_habitat_change|The Mangrove Creek Mosaic|Which creek edges, pools, and stands changed?|Use fine-scale maps and field measures of habitat and connectivity.
field_restoration_evidence|Did Mangrove Recovery Persist?|Which functions improved after one intervention and for how long?|Measure water flow, native recruitment, fauna, survival, maintenance, and costs.
"""


if __name__ == "__main__":
    revise_domain("209", "209_mangroves", MANGROVES,
                  "Mangroves through tidal hydrology, land rights, fine-scale mapping, species recruitment, restoration function, and coastal livelihoods.",
                  "tidal and salinity records, elevation and sediment measures, validated imagery, repeat vegetation and fauna plots, tenure and project documents, and consented local accounts",
                  "Name coast, stand, tidal setting, species, and date. Do not equate seedlings planted or canopy cover with ecosystem recovery or guaranteed coastal protection; respect tenure and access rights.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
