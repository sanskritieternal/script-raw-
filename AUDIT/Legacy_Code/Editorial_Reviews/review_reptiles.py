"""Editorial question designs for niche 195, Reptiles."""

from review_angle_plans import audit, revise_domain


REPTILES = """history_origins|How a Reptile Was First Described|Which specimens established the identity of one reptile species?|Trace type material, locality, original description, and later revision.
famous_examples|A Celebrated Recovery Examined|What does one reptile recovery case show about conservation?|Compare baseline, intervention, monitoring, threats, and continuing dependence.
hidden_stories|The People Behind a Reptile Survey|Whose knowledge and labor produced one population estimate?|Trace local guides, survey teams, identifiers, and land stewards.
beginner_explainers|Reptiles Are Many Lineages|How do snakes, lizards, turtles, and crocodilians differ?|Compare physiology and life history without treating one species as typical.
advanced_concepts|Counting a Hard-to-See Species|How can researchers estimate a reptile population despite imperfect detection?|Explain repeat surveys, capture methods, assumptions, and uncertainty.
mysteries_unsolved_cases|A Range Gap Investigated|Why is a reptile missing from seemingly suitable habitat?|Test survey effort, barriers, prey, climate, disturbance, and taxonomy.
technology_innovation|A New Reptile Monitoring Tool|Does one imaging or tracking method improve evidence?|Compare detection, animal welfare, cost, and field validation.
people_personalities|A Reptile Conservation Decision|How did one named researcher or manager alter a recovery effort?|Use plans, objections, dated actions, and measured results.
major_events|An Invasive Species Arrival|How did one documented arrival affect a native reptile?|Trace verified predation, habitat change, response, and uncertainty.
how_it_works|Temperature and Reptile Activity|How does temperature affect one reptile's behavior or development?|Specify species, life stage, setting, and measured range.
rise_fall|A Population Under Pressure|Which factors explain a measured change in one reptile population?|Compare repeatable counts, habitat, harvest, predation, and climate.
then_vs_now|A Reptile's Range Across Time|What can historic and recent records show about distribution?|Match names, sites, seasons, survey methods, and detection.
future_developments|Scenarios for One Reptile|How might habitat and temperature changes affect one species?|State model assumptions, dispersal limits, and conservation options.
myths_vs_facts|The Dangerous Reptile Claim|How does evidence compare with a popular claim about one species?|Verify identification, place, exposure, behavior, and actual risk.
documentary_stories|A Nesting Site Through One Season|What happened at one documented reptile nesting site?|Use dated monitoring, habitat records, and consented stewardship accounts.
observation_to_explanation|One Sighting's Limits|What can a single reptile sighting establish?|Separate presence from population size, breeding, and trend.
measurement_method|Surveying a Cryptic Reptile|How does one survey method estimate occurrence or abundance?|Examine season, effort, identification, detectability, and uncertainty.
scale_and_timespan|Local Loss or Species Decline?|At what scale is a reptile trend supported?|Define species, population, region, years, and comparability.
field_vs_lab|A Thermal Trait in Nature|Does a controlled temperature result predict field behavior?|Compare lab conditions with microhabitats, life stages, and field data.
natural_variation|When Reptile Counts Fluctuate|How much yearly variation can occur without a sustained decline?|Use longer time series and weather and survey context.
mechanism_chain|From Habitat Change to Survival|Which evidence links a specific land change to reptile survival?|Trace shelter, food, movement, reproduction, and threats.
extreme_case|An Exceptional Reptile Record|How was a record size, age, or range claim verified?|Check specimen, method, species ID, date, and independent documentation.
classification_debate|A Disputed Reptile Species|Which evidence supports splitting or combining one lineage?|Compare type specimens, morphology, genetics, and geography.
interacting_systems|Reptiles in Their Food Web|How do prey, predators, and habitat jointly shape one species?|Identify observed links and alternatives before causal claims.
data_gap|Where Surveys Have Not Looked|Which missing places or seasons weaken a conservation claim?|Map survey coverage, access barriers, and identification limits.
prediction_test|Did a Habitat Model Work?|Did predicted suitable habitat match later reptile observations?|Compare model version, survey effort, dates, and false negatives.
human_impact|Living Alongside a Reptile|How do people and one reptile species affect each other?|Examine land use, verified conflict, conservation benefit, and perception.
field_species_variation|Variation Within a Reptile Species|How do age, sex, season, and locality change appearance?|Use identified specimens and avoid creating false species distinctions.
field_ecological_role|What This Reptile Actually Does|Which prey, predators, or habitat functions involve one reptile?|Use direct field evidence and quantify where possible.
field_experimental_model|A Reptile as Research Model|Which question can one reptile species help researchers answer?|State experimental strengths, animal welfare limits, and transfer limits.
field_evolutionary_history|A Reptile Lineage Through Time|Which fossils and phylogenies support one evolutionary account?|Compare dating, specimen placement, and competing interpretations.
field_conservation_status|Assessing One Reptile's Risk|What evidence supports the current status of one species?|Check assessment date, range, trend, threats, survey coverage, and uncertainty.
"""


if __name__ == "__main__":
    revise_domain("195", "195_reptiles", REPTILES,
                  "Reptiles through distinct lineages, museum specimens, detectability, population evidence, ecological roles, and conservation decisions.",
                  "vouchered specimens and taxonomic revisions, repeatable field surveys, habitat and threat records, dated conservation plans, and species assessments",
                  "Name species, place, life stage, season, and assessment date. Do not infer population change from sightings or generalize risk from one reptile to all; seek current local and clinical sources for encounter safety.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
