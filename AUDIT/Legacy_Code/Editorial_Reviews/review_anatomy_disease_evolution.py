"""Editorial questions for human anatomy, disease science, and evolution."""

from review_angle_plans import audit, revise_domain


ANATOMY = """history_origins|A Body Structure First Described|Which observation changed a named anatomical account?|Use dated dissection, imaging, and terminology records.
famous_examples|A Textbook Diagram Rechecked|Which structures and variations does one familiar image omit?|Compare atlas with documented human samples.
hidden_stories|People Behind Anatomical Knowledge|Who donated bodies, prepared specimens, drew atlases, and taught?|Trace consent, credit, and historical context.
beginner_explainers|Location, Structure, and Function|Where is one organ and how does its shape support a task?|Use accepted terminology and a bounded example.
advanced_concepts|Variation Is Part of Anatomy|How often does a named arrangement vary across people?|Check sample, imaging method, and population.
mysteries_unsolved_cases|An Unclear Anatomical Image|Which variant or imaging artifact explains a structure?|Compare modalities and avoid individual diagnosis.
technology_innovation|A New Anatomy Imaging Method|What detail became visible and what remained hidden?|Compare resolution, contrast, and validation.
people_personalities|An Anatomy Atlas's Authors|Who decided what counted as typical anatomy?|Read source specimens, editorial choices, and omissions.
major_events|A Terminology Revision|What structure name changed and why?|Use dated anatomical standards and professional discussion.
how_it_works|An Organ System in Motion|How do structure and neighboring tissues enable function?|Use measured anatomy and physiology.
rise_fall|An Anatomical Belief Corrected|Which new observation overturned an earlier description?|Compare original and later evidence.
then_vs_now|Studying Anatomy Across Eras|How did dissection, microscopy, and imaging alter one claim?|Compare what each method could measure.
future_developments|A New Human Atlas|What populations and variations must it represent?|Specify sampling, consent, resolution, and access.
myths_vs_facts|Everyone Has the Same Body Map?|Which normal variants complicate a single diagram?|Use prevalence-aware, neutral terminology.
documentary_stories|A Specimen Becomes an Atlas Image|How did collection, consent, imaging, annotation, and teaching occur?|Follow provenance and rights.
observation_to_explanation|An Image to an Anatomical Claim|Which landmarks support a structure label?|Check orientation, scale, and expert validation.
measurement_method|Measuring an Organ|Which imaging or specimen method produced a dimension?|Report body position, age range, and uncertainty.
scale_and_timespan|Anatomy Through Development|How does a structure change with age or condition?|Use defined population and time period.
field_vs_lab|Atlas and Living Body|How do preserved specimens differ from in vivo imaging?|Compare tissue state, posture, and motion.
natural_variation|Normal Range of Structures|Which variants occur without pathology?|Use population data and avoid personal conclusions.
mechanism_chain|Structure Supports Function|Which anatomical links are directly tested?|Connect form, movement, blood supply, and physiology.
extreme_case|Rare Variant in Context|What can an uncommon structure teach without sensationalizing?|Compare larger studies and clinical uncertainty.
classification_debate|Where One Structure Ends|How do atlases define a boundary?|Compare nomenclature and imaging evidence.
interacting_systems|Anatomy Across Organ Systems|How do nerves, vessels, and tissues meet in a region?|Map a bounded functional path.
data_gap|Missing Bodies in Reference Atlases|Which ages, sex traits, body sizes, or populations are underrepresented?|Audit source data and ethical access.
prediction_test|Testing an Anatomical Model|Which imaging or specimen evidence could challenge a map?|Predefine landmark and validation method.
human_impact|Anatomical Representation in Care|How can a narrow reference affect teaching or design?|Use educational and clinical studies, not personal advice.
field_species_variation|Comparative Anatomy's Limits|Which animal structure resembles a human one and where does it differ?|Use matched landmarks and function.
field_ecological_role|Body Structure and Environment|How do activity or environment shape measured anatomy?|Use population studies and avoid deterministic claims.
field_experimental_model|Model of Human Structure|What do a cadaver, image, or digital model each omit?|Compare living function and variation.
field_evolutionary_history|History of a Human Structure|Which comparative evidence supports an evolutionary account?|Use phylogeny, fossils, and development.
field_conservation_status|Preserving Anatomical Collections|How are historic specimens and scans curated ethically?|Trace consent, preservation, access, and community concerns; legacy slug retained.
"""

DISEASE = """history_origins|A Disease Concept Takes Shape|Which observation separated a named condition from similar illness?|Use dated clinical, laboratory, and classification records.
famous_examples|A Famous Disease Study Rechecked|What population and outcome did it actually examine?|Read design, controls, uncertainty, and later replication.
hidden_stories|Patients and Public Health Workers|Whose care, reporting, and sample work made evidence possible?|Use consented accounts and credit teams.
beginner_explainers|Disease Mechanism and Diagnosis|How do symptoms, pathology, and testing relate for one condition?|Use current authoritative definitions without individual advice.
advanced_concepts|Cause Versus Association|Which evidence supports a mechanism rather than a risk marker?|Compare longitudinal, experimental, and clinical data.
mysteries_unsolved_cases|A Cluster with Unclear Cause|What is established about cases, exposure, and alternative explanations?|Use official investigation and avoid speculation about patients.
technology_innovation|A New Diagnostic Test|Did it improve a defined clinical decision?|Check sensitivity, specificity, population, and harms.
people_personalities|A Patient's Role in Research|How did affected people shape priorities or study design?|Use consented testimony and documented changes.
major_events|A Disease Classification Change|Which evidence changed a case definition?|Date the revision and compare before-and-after counts carefully.
how_it_works|From Exposure to Outcome|Which biological steps are supported for a named disease?|Separate established mechanism from hypotheses.
rise_fall|A Disease Rate Changes|Does the trend reflect cases, tests, reporting, or risk?|Use stable definitions and denominators.
then_vs_now|One Condition Across Treatment Eras|How did evidence and outcomes change?|Compare populations, care access, and endpoints.
future_developments|A Proposed Therapy or Test|Which studies would establish benefit and safety?|State population, comparator, outcome, and follow-up.
myths_vs_facts|A Symptom Proves a Diagnosis?|How many causes can produce it and what evidence distinguishes them?|Keep the episode educational, not diagnostic.
documentary_stories|A Disease Study's Evidence Trail|How did cases, samples, analysis, and review produce a finding?|Protect identities and trace methods.
observation_to_explanation|From Cases to Mechanism|What evidence links a factor to illness?|Compare confounding, dose, temporality, and biological tests.
measurement_method|Counting Disease|Which case definition and reporting system produced a rate?|Distinguish surveillance from clinical diagnosis.
scale_and_timespan|Individual Illness and Population Trend|Why can a population risk fail to predict one person's course?|Use explicit denominator and time window.
field_vs_lab|Lab Finding to Patient Benefit|Which cell or animal result has been tested in humans?|Separate preclinical from clinical evidence.
natural_variation|Different Disease Courses|How do age, context, genetics, and care affect outcomes?|Report variation without stereotypes.
mechanism_chain|A Disease Pathway Tested|Which causal steps have direct support?|Use bounded condition and competing mechanisms.
extreme_case|A Severe or Rare Case|What can it reveal without representing typical patients?|Compare cohort evidence and consent.
classification_debate|Defining a Disease Category|Which diagnostic or surveillance threshold matters?|Name authority, date, and purpose.
interacting_systems|Disease and Social Conditions|How do biology, environment, and access to care interact?|Use multidisciplinary evidence and affected voices.
data_gap|Who Is Missing from Studies?|Which populations or settings lack evidence?|Audit recruitment, reporting, and diagnostic access.
prediction_test|A Disease Hypothesis Tested|Which study would distinguish two causes or interventions?|Define comparator, outcome, and ethics.
human_impact|Living with a Condition|Which burdens and supports matter beyond a biomarker?|Use consented accounts and patient-centered outcomes.
field_species_variation|Pathogen or Model Across Species|Does a finding transfer between host species?|Check host biology and direct human evidence.
field_ecological_role|Ecology of Disease|How do environment and host interactions shape transmission or exposure?|Avoid simplistic blame and use field data.
field_experimental_model|A Model's Clinical Limits|What can cells or animals tell us about human illness?|State external validation and welfare safeguards.
field_evolutionary_history|Evolution of a Disease Agent or Risk|Which dated genetic and epidemiologic evidence supports change?|Avoid unsupported origins or attribution.
field_conservation_status|Wildlife Health and Conservation|When does a disease affect threatened host populations?|Use official assessments and avoid assuming all disease is infectious.
"""

EVOLUTION = """history_origins|An Evolutionary Explanation Emerges|Which evidence and debate shaped a named evolutionary idea?|Use dated primary texts and later tests.
famous_examples|A Classic Evolution Example Rechecked|What populations, traits, and time span were observed?|Compare original study and independent follow-up.
hidden_stories|Collectors Behind Evolutionary Evidence|Who gathered specimens and local knowledge?|Credit contributors and provenance.
beginner_explainers|Variation, Inheritance, and Change|How can a trait frequency shift across generations?|Use a bounded population and measurable trait.
advanced_concepts|Selection Versus Drift|Which data distinguish adaptive change from chance?|Compare population size, fitness, and repeated samples.
mysteries_unsolved_cases|An Uncertain Lineage|Which fossil or genetic evidence constrains ancestry?|State missing branches and alternative trees.
technology_innovation|A New Evolutionary Tool|What did sequencing or dating reveal beyond older evidence?|Compare method, uncertainty, and independent validation.
people_personalities|An Evolutionary Debate|How did researchers revise a claim after new data?|Read original and critical work in context.
major_events|A Discovery Changes a Tree|Which specimen or sequence shifted a relationship?|Trace provenance, analysis, and peer response.
how_it_works|Evolution in a Population|Which mechanisms changed trait frequencies?|Separate mutation, selection, drift, migration, and recombination.
rise_fall|A Hypothesis Gains or Loses Support|Which tests changed confidence over time?|Compare dates, datasets, and model assumptions.
then_vs_now|One Lineage Across Methods|How did fossils and genomics change its reconstruction?|Compare compatible taxa and time periods.
future_developments|A New Evolutionary Test|Which data would resolve a disputed branch?|Specify samples, dating, model, and conservation ethics.
myths_vs_facts|Evolution Has a Goal?|What evidence shows change in context rather than toward perfection?|Use an observed population and tradeoffs.
documentary_stories|A Specimen to a Phylogeny|How did collection, dating, analysis, and revision occur?|Trace permissions and uncertainty.
observation_to_explanation|Trait Pattern to History|Which evidence supports common ancestry or adaptation?|Compare phylogeny, ecology, and alternatives.
measurement_method|Measuring Evolutionary Change|Which trait, allele, or fossil character was counted?|State sample, time, and error.
scale_and_timespan|Generations and Deep Time|Which evolutionary processes can be observed directly?|Separate experimental change from ancient reconstruction.
field_vs_lab|Selection in Lab and Wild|Do controlled results hold in natural populations?|Compare conditions and fitness measures.
natural_variation|Variation Within Populations|Which differences provide material for change?|Sample widely and avoid typological assumptions.
mechanism_chain|From Mutation to Outcome|Which steps link genetic change to phenotype and reproduction?|Use functional and population evidence.
extreme_case|Rapid Evolution Under Pressure|What does a fast-changing population reveal?|Check sampling and fitness tradeoffs.
classification_debate|Species Boundaries|Which concept and data define a species in one case?|Compare interbreeding, ecology, and phylogeny.
interacting_systems|Coevolution in Context|How do interacting species shape each other's change?|Use reciprocal evidence and alternative explanations.
data_gap|Missing Fossils or Genomes|Which times, places, or taxa limit a reconstruction?|Map preservation and sampling bias.
prediction_test|An Evolutionary Prediction|Which new fossil or sequence would challenge a tree?|State prediction before analysis.
human_impact|Evolutionary Evidence and Society|How are findings communicated without biological determinism?|Check history, uncertainty, and affected communities.
field_species_variation|Comparing Related Species|Which shared and distinct traits inform ancestry?|Control ecology and sampling.
field_ecological_role|Selection in an Ecosystem|Which interaction changes survival or reproduction?|Measure environment and fitness.
field_experimental_model|Experimental Evolution|What can a short laboratory lineage reveal?|State population and external-validity limits.
field_evolutionary_history|Reconstructing a Lineage|Which fossils, genomes, and dates support a branch?|Show competing trees and uncertainty.
field_conservation_status|Evolution in Conservation|How do diversity and local adaptation inform a current assessment?|Use official species status and population evidence.
"""


if __name__ == "__main__":
    revise_domain("352", "352_human_anatomy", ANATOMY,
                  "Human anatomy as the documented structure and variation of living bodies, specimens, and images across development and populations.",
                  "NIH anatomical reference resources, consented specimen and imaging studies, terminology standards, atlas provenance, and population variation research",
                  "Name structure, orientation, imaging method, population, and age range. Treat normal variation neutrally and do not diagnose a person from a diagram.")
    revise_domain("353", "353_disease_science", DISEASE,
                  "Disease science as study of defined conditions, mechanisms, case definitions, population patterns, tests, interventions, and patient outcomes.",
                  "WHO and CDC case-definition guidance, original clinical and epidemiologic studies, laboratory methods, systematic evidence, and consented patient accounts",
                  "Name condition, case definition, jurisdiction, population, and date. Distinguish surveillance from diagnosis and preclinical findings from proven patient benefit.")
    revise_domain("354", "354_evolution", EVOLUTION,
                  "Evolution as testable change in populations and lineages through inheritance, selection, drift, migration, and deep-time evidence.",
                  "original field and laboratory studies, dated fossils and geologic context, sequence datasets, phylogenetic methods, and conservation assessments",
                  "Name species or lineage, trait, population, time span, and uncertainty. Avoid teleology and unsupported direct-ancestor claims.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
