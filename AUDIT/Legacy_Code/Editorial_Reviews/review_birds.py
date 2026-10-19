"""Editorial question designs for niche 196, Birds."""

from review_angle_plans import audit, revise_domain


BIRDS = """history_origins|How a Bird Became a Named Species|Which specimens and observations established one bird's identity?|Trace original description, type material, locality, and revisions.
famous_examples|A Famous Migration Rechecked|What do tracking and counts establish about one migration?|Specify population, route, season, devices, and untracked birds.
hidden_stories|The Observers Behind Bird Data|Whose repeated work produces a long bird survey?|Trace volunteers, local experts, identifiers, data curators, and analysts.
beginner_explainers|Identifying One Bird Responsibly|Which traits and context distinguish a bird from lookalikes?|Use plumage, voice, behavior, season, geography, and uncertainty.
advanced_concepts|From Counts to Trends|How do repeated bird counts become population trend estimates?|Explain survey design, detection, route coverage, model, and uncertainty.
mysteries_unsolved_cases|A Bird Missing from a Familiar Site|Which factors could explain a documented local absence?|Test timing, observer effort, habitat, weather, movement, and identification.
technology_innovation|Automated Bird Detection|Does one acoustic or visual model improve survey data?|Compare recall, false positives, habitat noise, and expert verification.
people_personalities|A Bird Conservation Choice|How did one named person shape a recovery or monitoring effort?|Use dated plans, competing views, actions, and measured outcomes.
major_events|A Habitat Event and Its Birds|How did one fire, flood, or land conversion affect a bird population?|Compare before and after surveys and account for displacement.
how_it_works|The Annual Cycle of One Bird|How do breeding, molt, migration, and wintering connect?|Choose a species and population, using tracked and observed records.
rise_fall|The Trend of One Bird Species|What supports a rise or decline in a defined population?|Compare standardized estimates, intervals, habitat, and threats.
then_vs_now|A Bird Community Across Decades|Which changes survive differences in observers and survey methods?|Match sites, seasons, effort, taxonomy, and detection.
future_developments|A Bird's Range Under Change|Which plausible conditions could shift one species' range?|State habitat, climate, migration, and dispersal assumptions.
myths_vs_facts|Does Feeding Birds Always Help?|What evidence shows benefits and harms of feeding one species locally?|Consider season, disease, food quality, predators, and context.
documentary_stories|One Nesting Season Documented|What can a season of observations reveal about breeding success?|Use ethical distance, dated records, weather, and sample limits.
observation_to_explanation|One Rare Sighting's Meaning|What can a verified out-of-range sighting establish?|Separate vagrancy, survey effort, colonization, and range shift.
measurement_method|How a Bird Survey Works|What does a standardized count measure and miss?|Check timing, route selection, observer, detectability, and analysis.
scale_and_timespan|One Wetland Versus a Flyway|At what scale is a bird claim supported?|Define breeding population, migration route, local site, and years.
field_vs_lab|A Bird Trait Outside the Lab|Does a controlled behavior or physiology finding hold in the wild?|Compare stress, food, age, weather, and field validation.
natural_variation|Why Bird Counts Swing|How much annual change reflects weather, breeding success, or movement?|Use longer series and comparable methods.
mechanism_chain|From Habitat Loss to Bird Numbers|Which links connect a land change to one bird population?|Trace nesting sites, food, survival, recruitment, and movement.
extreme_case|An Exceptional Bird Record|How was a record distance, age, or count verified?|Check banding or tracking data, taxonomy, method, and independent review.
classification_debate|The Species Boundary in Birds|Why do checklists disagree over one bird lineage?|Compare genetics, voice, morphology, breeding evidence, and rules.
interacting_systems|Birds in an Ecosystem|How does one bird population interact with food and habitat?|Separate observed pollination, predation, dispersal, or competition from assumption.
data_gap|Birds Missing from Surveys|Which species or habitats are poorly covered by existing counts?|Map route bias, night activity, inaccessible sites, and detection limits.
prediction_test|Did a Range Forecast Hold?|Did a forecast of bird occurrence match later observations?|Compare model date, assumptions, effort, and measured records.
human_impact|A Bird Policy's Trade-offs|Who gains and loses from one bird protection measure?|Compare species outcome, land use, cost, and community evidence.
field_species_variation|One Bird's Changing Plumage|How do age, sex, molt, and season alter appearance?|Use verified specimens or images and avoid false species labels.
field_ecological_role|What One Bird Actually Contributes|Which ecological function is measured for a named bird?|Check diet, seed dispersal, pollination, or predation and magnitude.
field_experimental_model|Birds as Research Models|What can a chosen bird species reveal about a broader mechanism?|State experimental strengths, welfare constraints, and transfer limits.
field_evolutionary_history|A Bird Lineage Through Time|Which fossils and genomes support one evolutionary relationship?|Compare dating, sampling, and competing trees.
field_conservation_status|Evidence Behind a Bird's Status|What supports the current conservation assessment?|Check range, population estimate, trend, threats, date, and uncertainty.
"""


if __name__ == "__main__":
    revise_domain("196", "196_birds", BIRDS,
                  "Birds through species identity, annual cycles, standardized monitoring, migration, habitat, and conservation evidence.",
                  "vouchered specimens, verified sightings, standardized surveys, tracking data, habitat records, taxonomic revisions, and current species assessments",
                  "Name species or population, geography, season, and date. Distinguish sightings and counts from modeled abundance; avoid disturbing nests and verify any management or feeding advice with current local sources.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
