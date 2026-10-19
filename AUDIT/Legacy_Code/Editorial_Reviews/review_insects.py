"""Editorial question designs for niche 193, Insects."""

from review_angle_plans import audit, revise_domain


INSECTS = """history_origins|How an Insect Group Was Classified|Which specimen evidence changed the naming of one insect lineage?|Trace dated descriptions, type specimens, and later revisions.
famous_examples|A Famous Insect Population Rechecked|What does a well-known migration or outbreak actually demonstrate?|Define species, region, period, counts, and sampling limits.
hidden_stories|The Collectors Behind a Discovery|Whose field and museum work enabled a major insect finding?|Trace collectors, identifiers, local collaborators, and specimen records.
beginner_explainers|What Makes an Insect?|Which traits distinguish an insect from other arthropods?|Compare life stages and body structures using named examples.
advanced_concepts|One Species or Several?|How do morphology, genetics, ecology, and mating evidence affect a species boundary?|Choose a contested group and compare competing classifications.
mysteries_unsolved_cases|An Unexplained Local Decline|Which evidence could explain a documented change in one insect population?|Test survey method, habitat, climate, pesticides, disease, and uncertainty.
technology_innovation|A New Insect Survey Method|Does one sensor or genetic method improve detection?|Compare species coverage, false identifications, cost, and field validation.
people_personalities|The Scientist Who Revised a Group|How did one researcher's decision reshape insect taxonomy?|Use specimens, publications, criticism, and later acceptance.
major_events|An Invasion or Outbreak Revisited|What changed after one documented insect arrival or outbreak?|Trace surveillance, ecological effects, management, and unintended impacts.
how_it_works|Metamorphosis in One Species|What changes between the life stages of one insect?|Use developmental observations and distinguish this species from general claims.
rise_fall|Why One Insect Became Common|Which factors explain an increase or decline in a defined population?|Compare standardized counts, land use, weather, and predators.
then_vs_now|One Habitat's Insects Across Time|What can comparable collections reveal about species change?|Match sites, seasons, methods, identification standards, and effort.
future_developments|Insects Under Landscape Change|Which plausible habitat changes would affect a defined insect group?|State climate, host plant, land-use, and dispersal assumptions.
myths_vs_facts|Are All Insects Harmful?|What do ecological and economic studies show for a chosen insect group?|Distinguish pests, pollinators, decomposers, predators, and context.
documentary_stories|A Specimen's Scientific Journey|How did one collected insect become evidence for a claim?|Trace collection, curation, identification, publication, and reanalysis.
observation_to_explanation|A Backyard Sighting's Limits|What can a single insect sighting establish?|Separate occurrence from abundance, breeding, migration, and trend.
measurement_method|Counting Insects Consistently|How does one survey method sample a defined group?|Explain trap bias, season, effort, identification, and uncertainty.
scale_and_timespan|Local Change Versus Global Decline|At what scale is an insect trend actually supported?|Define taxon, geography, years, sampling coverage, and baseline.
field_vs_lab|An Insect Trait in the Wild|Does a lab observation predict field behavior or survival?|Compare temperature, food, predators, life stage, and replication.
natural_variation|Population Swings Between Years|How much variation is expected without a persistent trend?|Use long-term records and weather and sampling context.
mechanism_chain|From Host Plant to Insect Abundance|Which links connect plant change to a specific insect population?|Trace larval food, reproduction, survival, and detection.
extreme_case|The Exceptional Swarm|How was an extraordinary insect event measured?|Check taxon, area, density, duration, and independent records.
classification_debate|A Disputed Insect Name|Why do researchers disagree over one species or genus?|Compare type material, genetic data, morphology, and naming rules.
interacting_systems|Insects in a Food Web|How does changing one insect population affect plants and predators?|Identify measured links and alternative explanations.
data_gap|Unseen Insect Diversity|Which habitats or life stages are poorly represented in collections?|Map sampling gaps, curation backlog, identification limits, and bias.
prediction_test|Did a Range Forecast Hold?|Did one projected insect range shift match later observations?|Compare model assumptions, survey effort, dates, and occurrence data.
human_impact|A Control Program's Trade-offs|Who benefits and what else is affected by controlling one insect?|Assess target reduction, non-target species, cost, and local needs.
field_species_variation|Variation Within a Named Species|How much do color, size, or behavior vary within one insect species?|Compare sex, age, season, locality, and genetics.
field_ecological_role|One Insect's Actual Ecological Role|What does one species eat, pollinate, decompose, or prey upon?|Use field observation and distinguish direct evidence from assumption.
field_experimental_model|Why Researchers Study This Insect|Which scientific question does one model species answer well?|Identify experimental advantage and limits of transfer to other taxa.
field_evolutionary_history|Testing an Insect Lineage|Which fossils and genetic evidence support a proposed relationship?|Compare dated specimens, phylogenies, and uncertainty.
field_conservation_status|Is This Insect at Risk?|What evidence supports one species' conservation assessment?|Check range, trend, threats, survey quality, and assessment date.
"""


if __name__ == "__main__":
    revise_domain("193", "193_insects", INSECTS,
                  "Insects through taxonomy, life history, field measurement, ecological roles, population change, and conservation evidence.",
                  "vouchered museum specimens, taxonomic revisions, repeatable field surveys, ecological studies, dated range records, and species assessments",
                  "Name the species or group, location, life stage, season, and date. Do not generalize from one species to all insects or claim broad declines from non-comparable sightings; distinguish insects from other arthropods.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
