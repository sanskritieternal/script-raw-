"""Editorial questions for microbiology."""

from review_angle_plans import audit, revise_domain


MICROBIOLOGY = """history_origins|How a Microbe Was Recognized|Which observations established one microorganism's identity?|Trace original reports, imaging, controls, and later classification.
famous_examples|A Familiar Microbe Beyond One Role|What functions does a named organism have in different settings?|Compare strain, habitat, measured effects, and context.
hidden_stories|Microbes That Make a System Work|Which microbial roles are omitted from a familiar ecosystem story?|Use field studies, molecular evidence, and measured processes.
beginner_explainers|What Is a Microorganism?|How do bacteria, archaea, microscopic fungi, protists, and viruses differ?|Use accepted definitions and explain where boundaries are debated.
advanced_concepts|Association Is Not a Microbial Cause|What evidence would link one microbe to an observed outcome?|Compare controls, timing, mechanism, alternative causes, and replication.
mysteries_unsolved_cases|An Unassigned Sequence|Why has one environmental genetic signal resisted interpretation?|Examine reference gaps, contamination, method limits, and new data.
technology_innovation|A Method That Revealed New Microbes|What did one sequencing or imaging method make visible?|Compare detection limit, bias, validation, and what it cannot infer.
people_personalities|A Research Team's Finding|How did one team move from sample to published claim?|Trace funding, methods, controls, peer review, and correction.
major_events|A Change in Microbial Classification|Why was one taxon revised or renamed?|Compare molecular evidence, naming rules, and practical consequences.
how_it_works|A Microbe in Its Environment|Which measured processes let one organism use local resources?|Explain mechanism from qualified studies without cultivation steps.
rise_fall|A Microbial Population Through Time|Which measured factors explain its increase or decline?|Compare repeated sampling, habitat, competition, and detection bias.
then_vs_now|A Discovery Reanalyzed|How did new methods change an older microbiology claim?|Compare original evidence, later tests, taxonomy, and limits.
future_developments|A Proposed Microbial Application|What evidence would justify one environmental or industrial use?|Define outcome, safety, containment, scale, and independent replication.
myths_vs_facts|Are All Microbes Harmful?|How does one claim about microbes compare with evidence of their varied roles?|Use specific taxa and ecological functions without overgeneralizing.
documentary_stories|One Sample Through a Research Lab|How does an observation become a microbial conclusion?|Follow permissions, qualified handling, controls, analysis, and uncertainty.
observation_to_explanation|A Change in a Microbial Community|Which mechanisms might explain one observed shift?|Compare environment, sampling, compositional data, and alternatives.
measurement_method|Counting What We Cannot See|How does one method estimate microbial abundance?|Explain detection, calibration, contamination control, and uncertainty.
scale_and_timespan|Microbial Change at Two Scales|How do hourly responses differ from long evolutionary change?|Use appropriate measurements and avoid treating one as the other.
field_vs_lab|A Culture and Its Original Habitat|How does a lab observation differ from behavior in nature?|Compare conditions, selected strains, community interactions, and validation.
natural_variation|A Microbiome's Normal Range|How variable is one microbial community across people or places?|Check population, repeated samples, method, and confounding.
mechanism_chain|From Microbe to Measured Effect|Which steps connect one organism to a system-level outcome?|Require evidence for each link and identify untested assumptions.
extreme_case|Life in an Unusual Habitat|What supports a claim of microbial survival under extreme conditions?|Compare sample integrity, independent methods, and contamination controls.
classification_debate|Where Does This Microbe Belong?|Why do taxonomic schemes place one organism differently?|Compare phylogeny, naming conventions, data quality, and version.
interacting_systems|A Microbe and Its Partners|How do several organisms jointly produce an observed process?|Use interaction studies and avoid assigning all credit to one taxon.
data_gap|The Unsequenced Majority|Which habitats or groups are missing from one reference database?|Check sampling geography, methods, deposition, and classification gaps.
prediction_test|A Microbial Model Tested|Did one model predict an independently observed outcome?|Compare training and test sets, conditions, error, and transportability.
human_impact|Microbiology and a Practical Decision|How did evidence about one microbe inform a bounded policy or product?|Trace findings, risk assessment, implementation, and outcomes.
field_species_variation|Strains Within a Named Species|How do different strains vary in function or risk?|Use qualified comparative data and avoid species-wide claims.
field_ecological_role|Microbes in a Nutrient Cycle|Which measured transformations involve a named group?|Link chemistry, community data, and field conditions.
field_experimental_model|A Model Organism's Limits|What does one laboratory model reveal and conceal?|Compare strains, conditions, target ecosystem, and external validation.
field_evolutionary_history|A Microbial Lineage Over Time|What do genomes and dated samples suggest about one lineage?|Check phylogenetic method, sampling, uncertainty, and alternative histories.
field_conservation_status|Protecting a Microbial Habitat|What evidence shows one habitat's microbial diversity is at risk?|Compare baseline, pressures, function, monitoring, and conservation options.
"""


if __name__ == "__main__":
    revise_domain("154", "154_microbiology", MICROBIOLOGY,
                  "Microbial diversity and function through observation, classification, ecology, controlled inference, and responsible applications.",
                  "peer-reviewed observational and experimental studies, versioned sequence and taxonomy databases, transparent sampling and controls, environmental measurements, and qualified biosafety assessments",
                  "Name organism or community, strain where relevant, habitat, method, and date. Avoid universal claims from one sample, distinguish association from causation, and keep culturing or handling details with qualified biosafety professionals.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
