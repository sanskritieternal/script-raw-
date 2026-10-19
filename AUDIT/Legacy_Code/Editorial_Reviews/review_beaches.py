"""Editorial question designs for niche 212, Beaches."""

from review_angle_plans import audit, revise_domain


BEACHES = """history_origins|How One Beach Formed|Which sediment sources, waves, and sea-level history built a named beach?|Use cores, shore maps, bathymetry, and dating uncertainty.
famous_examples|A Famous Beach Erosion Claim Tested|What do shoreline records show at one celebrated beach?|Define shoreline proxy, datum, years, season, and measurement error.
hidden_stories|The Work Behind a Beach|Whose labor and knowledge maintain access and measure coastal change?|Trace local residents, survey crews, lifeguards, cleaners, and land managers.
beginner_explainers|A Beach Is a Moving System|How do waves, tides, dunes, and sediment exchange shape a beach?|Use one named site and a dated seasonal cycle.
advanced_concepts|Erosion Versus Beach Position|Why can a shoreline retreat at one date mislead?|Compare tide, storm recovery, sandbar movement, long trend, and measurement proxy.
mysteries_unsolved_cases|Where Did the Sand Go?|Which factors explain unexpected narrowing at one beach?|Test storm transport, dredging, structures, sediment supply, and survey timing.
technology_innovation|Watching Beaches with Cameras|Does one remote method improve shoreline or sandbar monitoring?|Compare tide correction, image calibration, cloud or wave limits, and ground surveys.
people_personalities|A Coastal Management Choice|How did one named community or manager alter a beach?|Use plans, access rights, engineering records, local input, and outcomes.
major_events|A Beach After a Storm|What changed immediately and later after one documented storm?|Compare profiles, dunes, overwash, infrastructure, and recovery.
how_it_works|Sand Moving Alongshore|How do waves and currents shift sediment along one coast?|Use observed transport direction, source, barriers, and season.
rise_fall|A Beach Width Trend|What supports persistent narrowing or widening?|Use comparable profiles, tide datum, storm history, and uncertainty.
then_vs_now|One Beach Across Two Eras|How have shoreline, dunes, access, and use changed?|Match maps, profile lines, dates, seasons, and land rights.
future_developments|Scenarios for a Changing Shore|Which plausible factors could alter one beach?|State sea level, storms, sediment budget, development, and management assumptions.
myths_vs_facts|Does Beach Nourishment Stop Erosion?|What does one nourishment project achieve and for how long?|Compare sand volume, source, maintenance, habitat, cost, and downstream effects.
documentary_stories|A Beach Management Decision Reconstructed|Why was one beach nourished, armored, or left to move?|Trace hazard assessment, alternatives, rights, costs, and monitoring.
observation_to_explanation|One Narrow-Beach Photo|What can an image establish about coastal change?|Separate tide, seasonal shift, storm erosion, and long-term trend.
measurement_method|Measuring Shoreline Change|How are repeat beach profiles or shoreline positions compared?|Define datum, proxy, instruments, tide correction, spacing, and uncertainty.
scale_and_timespan|One Access Point Versus a Coast|At what scale does a beach-erosion claim hold?|Define beach cell, survey reach, season, years, and sediment connection.
field_vs_lab|Wave Models on a Real Beach|Does a controlled model reproduce observed sediment transport?|Compare bathymetry, grain size, storm sequence, and field validation.
natural_variation|The Seasonal Beach Cycle|How much beach width can change without net long-term loss?|Use repeated profiles and wave and tide context.
mechanism_chain|From Seawall to Neighboring Shore|Which evidence links one structure to sediment or wave change?|Trace wave reflection, transport, beach profile, and alternative causes.
extreme_case|A Record Coastal Retreat|How was an exceptional beach-change rate calculated?|Check start and end dates, shoreline definition, datum, storms, and error.
classification_debate|Where Does the Beach Begin and End?|Why do maps disagree on shoreline position?|Compare wet-dry line, vegetation, dune toe, tidal datum, and purpose.
interacting_systems|Beach, Dune, and Nearshore Bar|How do sand stores move between linked coastal habitats?|Use measured profiles and storm and recovery cycles.
data_gap|The Unmeasured Shore|Which storms, tides, or reaches are missing from coastal records?|Map survey dates, access, imagery quality, and datum changes.
prediction_test|Did a Coastal Forecast Hold?|How did one shoreline or water-level forecast compare with observation?|Match model issue date, storm, site, tide, and measured impact.
human_impact|Who Can Reach This Beach?|How do access, flood risk, tourism, and protection costs affect people?|Compare public rights, transport, infrastructure, and local testimony.
field_field_sampling|A Repeatable Beach Survey|Which profiles and ecological measures answer one site question?|Set fixed transects, tide reference, season, sediment, dune, and habitat metrics.
field_land_use|Development and Sediment Supply|How did one land-use or river change affect a beach?|Compare sediment records, maps, structures, storms, and controls.
field_weather_variability|Storm Loss Versus Persistent Change|How much of a shoreline shift follows one weather event?|Use before and after and longer repeat profiles.
field_habitat_change|A Beach Habitat Mosaic|Which dunes, wrack, intertidal, or nearshore areas changed?|Compare repeat maps and species surveys with tide context.
field_restoration_evidence|Did Beach Restoration Work?|Which predefined physical and ecological outcomes lasted?|Compare profiles, habitat, access, cost, maintenance, and downstream effects.
"""


if __name__ == "__main__":
    revise_domain("212", "212_beaches", BEACHES,
                  "Beaches through sediment movement, shoreline measurement, storms, dunes, public access, infrastructure, and restoration trade-offs.",
                  "repeat shoreline and beach-profile surveys, tide and wave records, sediment budgets, coastal imagery with datum, management plans, and consented local accounts",
                  "Name beach, shoreline definition, datum, survey season, and date. Distinguish a narrow beach at one tide from long-term erosion and verify current local hazard and access notices.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
