"""Editorial question designs for niche 204, Plant Intelligence."""

from review_angle_plans import audit, revise_domain


PLANT_INTELLIGENCE = """history_origins|How Plant Behavior Became a Debate|Which experiments changed how researchers describe plant responses?|Trace original methods, replication, and competing terminology.
famous_examples|A Famous Plant Learning Claim Tested|What did one cited experiment measure and has it replicated?|Examine controls, sample size, preregistration, alternative mechanisms, and later studies.
hidden_stories|The Work Behind a Plant Response Experiment|Whose cultivation, instrumentation, and analysis make one result possible?|Trace growers, technicians, designers, and data analysts.
beginner_explainers|Response Is Not Thought|What can a plant's response to light or touch establish?|Explain stimulus, signaling, growth or movement, and inferential limits.
advanced_concepts|What Would Count as Learning?|Which operational test could distinguish learning from adaptation or habituation?|Define prediction, controls, repeatability, and alternative explanations.
mysteries_unsolved_cases|A Response No One Can Yet Explain|Which mechanisms remain plausible for one documented plant behavior?|Compare chemical, electrical, hydraulic, circadian, and growth pathways.
technology_innovation|Recording Plant Signals|Does one sensor reveal repeatable electrical or chemical activity?|Check calibration, artifacts, controls, biological meaning, and replication.
people_personalities|A Researcher's Interpretation|How did one scientist frame a disputed plant-behavior result?|Compare original evidence, critics' tests, and later revisions.
major_events|A Replication That Changed the Debate|How did a repeat experiment affect one claim?|Match protocol, plant material, environment, power, and outcome.
how_it_works|From Stimulus to Response|What pathway links a defined cue to a plant movement or growth change?|Trace receptor, signal, tissue response, and timing.
rise_fall|The Life of a Plant Cognition Claim|Why did support for one interpretation grow or weaken?|Follow studies, replication, definitions, criticism, and evidence quality.
then_vs_now|A Classic Experiment Repeated|What changes when a historical plant-response test uses modern controls?|Compare apparatus, species, measures, and interpretation.
future_developments|A Testable Plant Behavior Agenda|Which experiment would best separate rival explanations?|Predefine outcomes, controls, replication, and measurement limits.
myths_vs_facts|Do Plants Have Brains?|What does plant physiology show about signaling without neurons?|Distinguish networked response from animal neural architecture and subjective claims.
documentary_stories|One Contested Experiment Reconstructed|What did researchers actually do, observe, and conclude?|Use protocol, raw data where available, critiques, and replications.
observation_to_explanation|A Plant Turns Toward Light|What can one directional growth observation establish?|Separate phototropism from choice, anticipation, and learning claims.
measurement_method|Quantifying a Plant Response|How are stimulus and response measured in one experiment?|Check timing, blinding, controls, baseline, noise, and units.
scale_and_timespan|Seconds, Days, and Generations|Over what timescale does one claimed plant response occur?|Separate immediate signaling, developmental plasticity, and evolutionary adaptation.
field_vs_lab|A Lab Behavior Outdoors|Does a controlled response occur amid natural variability?|Compare light, water, wind, neighbors, and field replication.
natural_variation|Why Plants Respond Differently|How much variation comes from age, genotype, or condition?|Use repeated individuals and environmental controls.
mechanism_chain|How a Signal Changes Growth|Which measured steps connect a cue to a lasting change?|Trace detection, transport, gene expression, tissue growth, and reversal.
extreme_case|The Most Surprising Plant Claim|What evidence would confirm an extraordinary behavior report?|Demand defined outcome, negative controls, independent replication, and mechanism tests.
classification_debate|Defining Plant Cognition|How do different definitions change whether one result counts?|Compare operational criteria and identify what evidence would decide.
interacting_systems|Plants and Neighbor Signals|How does one plant respond to cues from another organism?|Separate emitted signal, reception, changed behavior, and adaptive outcome.
data_gap|What the Experiment Did Not Measure|Which unrecorded variables prevent a strong interpretation?|Audit environment, controls, plant history, sample size, and raw data.
prediction_test|Can a Plant Behavior Model Predict?|Does a predeclared model predict new response data?|Compare preregistered predictions, held-out plants, and rival models.
human_impact|Why Labels Change Decisions|How might calling plants intelligent influence research or stewardship?|Examine documented communication, funding, policy, and ethical arguments.
field_species_variation|One Result Across Species|Does a response found in one plant extend to another?|Compare related species, ecology, protocols, and failed replications.
field_ecological_role|Is the Response Useful?|Does one plant behavior improve survival or reproduction in nature?|Test fitness outcome under realistic conditions and competing causes.
field_experimental_model|Choosing a Plant Model|Which organism and setup best test a disputed behavioral claim?|Define trait, replication, controls, measurement, and transfer limits.
field_evolutionary_history|Origins of Plant Signaling|Which comparative evidence traces a response pathway across lineages?|Compare homologous genes, physiology, phylogeny, and uncertainty.
field_conservation_status|Behavior and Conservation Claims|Could a verified response affect management of a threatened plant?|First establish mechanism and field relevance, then check current status and threats.
"""


if __name__ == "__main__":
    revise_domain("204", "204_plant_intelligence", PLANT_INTELLIGENCE,
                  "Plant intelligence as a contested research label tested through operational definitions, plant signaling, controlled experiments, replication, and field relevance.",
                  "original experimental protocols and data, controlled replication studies, plant physiology and signaling research, field validation, and clearly attributed scientific critiques",
                  "Name species, cue, response measure, timescale, and operational definition. Do not equate signaling with consciousness, intention, brains, or sentience; distinguish measured behavior from interpretive labels.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
