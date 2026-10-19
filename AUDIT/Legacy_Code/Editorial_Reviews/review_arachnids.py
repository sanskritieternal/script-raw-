"""Editorial question designs for niche 194, Arachnids."""

from review_angle_plans import audit, revise_domain


ARACHNIDS = """history_origins|How an Arachnid Lineage Was Named|Which specimens changed the classification of one arachnid group?|Trace original description, type material, and subsequent revisions.
famous_examples|A Famous Spider Case Examined|Which claims about a widely discussed arachnid are supported?|Specify species and region; compare published behavior, distribution, and risk evidence.
hidden_stories|The Collectors Behind a Species Name|Whose sampling and curation made one arachnid discovery possible?|Trace field collectors, local experts, identifiers, and specimen repositories.
beginner_explainers|What Counts as an Arachnid?|How do spiders, scorpions, ticks, and mites differ?|Compare body plan, development, ecology, and classification.
advanced_concepts|Species Boundaries in Arachnids|When do appearance and genetics suggest different species limits?|Examine one contested complex using type specimens, morphology, and sequences.
mysteries_unsolved_cases|An Unexpected Arachnid Range|Which evidence could explain a species found beyond its known range?|Test identification, transport, habitat change, survey effort, and records.
technology_innovation|New Methods for Identifying Arachnids|Does imaging or DNA improve one group's identification?|Compare accuracy, reference coverage, cost, and specimen verification.
people_personalities|A Revision That Changed Arachnid Science|How did one taxonomist alter a disputed classification?|Use publications, specimens, counterarguments, and later tests.
major_events|An Arachnid Discovery Revisited|What changed after a documented discovery or range expansion?|Track collection, confirmation, research response, and public interpretation.
how_it_works|How One Spider Builds a Web|Which behaviors and structures create a web in a named species?|Use observed stages and avoid extending the pattern to all spiders.
rise_fall|A Changing Local Arachnid Population|What explains a measured change for one species?|Compare standardized surveys, prey, habitat, weather, and detection.
then_vs_now|Old Specimens, New Questions|What do historic and recent arachnid records show about one range?|Match taxonomy, localities, seasons, and collection effort.
future_developments|A Range Under Environmental Change|Which conditions could alter one arachnid's distribution?|State habitat, prey, climate, transport, and survey assumptions.
myths_vs_facts|A Common Arachnid Fear Tested|How does evidence compare with a popular risk claim?|Specify species and geography, distinguish identification from exposure and harm.
documentary_stories|From Field Find to Species Description|What evidence established one newly described arachnid?|Trace discovery, type specimen, diagnostic traits, peer review, and revision.
observation_to_explanation|One Spider Indoors|What can one indoor sighting reveal about local populations?|Separate accidental entry, residency, breeding, and identification uncertainty.
measurement_method|Surveying Hard-to-See Arachnids|How does one method detect a chosen group?|Examine trap placement, timing, habitat, life stage, and identification error.
scale_and_timespan|A Local Record Versus a Range Shift|At what scale does evidence support an arachnid distribution claim?|Define species, sites, dates, effort, and observation completeness.
field_vs_lab|Venom or Behavior in Context|Does a laboratory result predict an organism's behavior in nature?|Compare exposure, dose, life stage, species, and field observations without medical advice.
natural_variation|Why Individuals Look Different|Which normal changes occur across sex, age, season, and locality?|Use identified specimens and controlled measurements.
mechanism_chain|From Prey to Arachnid Abundance|What evidence links food availability to one arachnid population?|Trace prey, reproduction, survival, competitors, and detection.
extreme_case|The Rare Giant or Long-Lived Individual|How was an exceptional arachnid record verified?|Check identification, measurement, captivity, age evidence, and independent records.
classification_debate|The Boundaries of an Arachnid Group|Which traits or genes support a disputed relationship?|Compare alternative phylogenies, sampling, and uncertainty.
interacting_systems|Arachnids in a Food Web|How does one arachnid group affect prey and predators?|Use measured interactions and separate direct from inferred effects.
data_gap|What Collections Fail to Show|Which habitats or stages are missing from arachnid records?|Map geographic and seasonal gaps, collector bias, and unidentified specimens.
prediction_test|Did a Habitat Prediction Hold?|Did a forecast of arachnid occurrence match later surveys?|Compare model version, dates, sites, effort, and observed records.
human_impact|Living with Arachnids|How do arachnids affect people in a defined setting?|Distinguish ecosystem service, nuisance, exposure, verified risk, and perception.
field_species_variation|One Spider, Many Forms|How much variation belongs within one named species?|Compare morphology, sex, life stage, locality, and genetics.
field_ecological_role|A Predator's Actual Diet|Which prey does one arachnid species consume?|Compare direct field observations, gut contents, and lab feeding trials.
field_experimental_model|Arachnids as Research Models|What question can one arachnid model answer reliably?|Identify experimental controls and limits of transfer to other species.
field_evolutionary_history|An Arachnid Lineage Through Time|What fossils and molecular evidence support one evolutionary claim?|Compare fossil placement, dating method, phylogeny, and disagreement.
field_conservation_status|Assessing an Overlooked Arachnid|What evidence supports a conservation assessment for one species?|Check range, habitat, population trend, threats, survey quality, and date.
"""


if __name__ == "__main__":
    revise_domain("194", "194_arachnids", ARACHNIDS,
                  "Arachnids through distinct lineages, taxonomy, specimens, behavior, ecological roles, public perception, and conservation evidence.",
                  "vouchered museum specimens, taxonomic revisions, repeatable field surveys, behavioral studies, dated range records, and species assessments",
                  "Name species or lineage, geography, life stage, and date. Do not conflate all arachnids with spiders or infer human danger from a sighting; route any bite or sting guidance to current clinical and local public-health sources.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
