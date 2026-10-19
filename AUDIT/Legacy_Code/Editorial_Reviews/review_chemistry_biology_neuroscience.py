"""Editorial question designs for chemistry, biology, and neuroscience."""

from review_angle_plans import audit, revise_domain


CHEMISTRY = """history_origins|A Chemical Idea Emerges|Which experiment changed the account of a named substance or reaction?|Use dated methods, samples, and later confirmation.
famous_examples|A Landmark Reaction Rechecked|What products and conditions were actually measured?|Compare original report, yield, and replication.
hidden_stories|People Behind a Chemical Result|Who prepared samples, built apparatus, and verified measurements?|Credit laboratory collaborators and technicians.
beginner_explainers|From Atoms to Measured Substance|How do composition, structure, and conditions explain one property?|Use a named material and measured value.
advanced_concepts|Reaction Pathway Versus Observation|Which intermediate steps are supported by evidence?|Compare kinetics, spectra, and alternative mechanisms.
mysteries_unsolved_cases|An Unexpected Chemical Product|Which contamination, competing reaction, or measurement error fits?|Review controls and independent analysis.
technology_innovation|A New Chemical Instrument|What previously hidden feature could it measure?|Compare calibration, detection limit, and validation.
people_personalities|A Chemistry Dispute|How were rival structural or mechanistic claims tested?|Read dated studies and critiques.
major_events|A Chemical Discovery Timeline|What happened from first signal to accepted interpretation?|Separate synthesis, characterization, replication, and use.
how_it_works|A Reaction Under Defined Conditions|What inputs, products, and energy changes are observed?|State concentration, temperature, apparatus, and limits.
rise_fall|A Chemical Explanation Revised|Which new measurement changed confidence in a model?|Compare dated evidence and competing accounts.
then_vs_now|Measuring One Chemical Quantity|How did sensitivity and uncertainty change across methods?|Use a matched analyte and units.
future_developments|A Proposed Chemical Process|Which test would support a claim of useful scale-up?|Measure selectivity, energy, waste, safety, and cost.
myths_vs_facts|Natural Means Chemically Safe?|Which exposure and dose evidence matters?|Separate substance identity, hazard, and context.
documentary_stories|One Sample to a Published Result|How was it made, characterized, and checked?|Follow provenance, lab notebook, controls, and review.
observation_to_explanation|A Spectrum to a Structure|Which peaks support an assigned molecule?|Compare standards, alternative structures, and uncertainty.
measurement_method|Quantifying a Chemical|Which assay, standard, and calibration produced a concentration?|Report matrix, detection limit, and error.
scale_and_timespan|Bench Reaction to Production|Which heat, mixing, and material limits change with scale?|Compare controlled trials and operating conditions.
field_vs_lab|Chemical Process Outside the Lab|Does a controlled result hold in environmental or industrial conditions?|Check matrix effects and monitoring.
natural_variation|Variable Samples|How do source and batch differences affect results?|Use replicates and trace provenance.
mechanism_chain|A Reaction Step by Step|Which proposed intermediates have been detected or constrained?|Separate model steps from directly measured species.
extreme_case|Chemistry at an Edge Condition|What does high pressure or low temperature reveal?|Use published measurements and safety context.
classification_debate|Naming a Chemical Class|Which structural or functional criteria define it?|Use IUPAC terms and discuss edge cases.
interacting_systems|A Reaction in a Mixture|Which competing molecules change behavior?|Test controlled combinations and interactions.
data_gap|An Unmeasured Chemical Path|Which missing intermediate or exposure limits inference?|Specify feasible test and detection threshold.
prediction_test|A Mechanism's Prediction|Which product or rate would distinguish two pathways?|Predefine conditions and analytical method.
human_impact|Chemical Claim in Use|Who is exposed to benefits, waste, or hazards?|Use product, workplace, and environmental evidence.
field_experimental_setup|A Chemical Experiment's Controls|Which blanks, standards, and conditions make a result interpretable?|Draw the apparatus and replication plan.
field_mathematical_model|Modeling a Reaction|Which kinetic or thermodynamic assumptions matter?|State variables, fitted range, and uncertainty.
field_measurement_error|Error in Chemical Analysis|Which calibration, contamination, or matrix effect dominates?|Report uncertainty budget and quality controls.
field_scale_transition|Molecule to Material|When does a property change from sample to bulk?|Compare composition, morphology, and processing.
field_technology_application|Chemistry in a Device or Process|Does a laboratory property survive real operation?|Measure durability, safety, and lifecycle.
"""

BIOLOGY = """history_origins|A Biological Explanation Emerges|Which observation and experiment formed a testable account?|Use dated specimens, methods, and follow-up.
famous_examples|A Classic Biology Experiment Rechecked|What organism, population, and conditions were actually studied?|Read original design and replication.
hidden_stories|People Caring for Research Organisms|Who gathers samples, maintains colonies, and curates records?|Credit contributors and ethical oversight.
beginner_explainers|From Cell to Organism|How do parts and environments interact in one biological process?|Use a named species and bounded function.
advanced_concepts|Generalizing Across Organisms|Which findings from one model hold in another species?|Compare homologous mechanisms and direct tests.
mysteries_unsolved_cases|An Unexplained Biological Pattern|Which sampling, environment, or mechanism could explain it?|Separate observations from speculative cause.
technology_innovation|A New Biological Measurement|What new level of detail became visible?|Compare resolution, bias, and validation.
people_personalities|A Biology Debate|How did researchers test rival mechanisms?|Read experimental sequence and critiques.
major_events|A Discovery to Verification|Which studies moved a biological claim beyond an initial report?|Build dated independent evidence.
how_it_works|One Biological Mechanism|What inputs, regulation, and outputs create a function?|Trace molecules, cells, or organisms as appropriate.
rise_fall|A Biological Model Reassessed|What later evidence changed its scope?|Compare populations, environments, and replication.
then_vs_now|One Process Across Methods|How did observation and intervention improve understanding?|Use comparable species and endpoints.
future_developments|A Proposed Biological Test|What experiment would distinguish explanations?|Specify organism, control, outcome, and ethics.
myths_vs_facts|One Gene, One Trait?|How do regulation and environment complicate a simple claim?|Use a bounded trait and evidence.
documentary_stories|A Biological Sample's Journey|How did collection, measurement, analysis, and reuse occur?|Trace consent, provenance, and method.
observation_to_explanation|From Pattern to Mechanism|Which intervention supports a causal interpretation?|Compare observation, controls, and alternative pathways.
measurement_method|Measuring a Biological Trait|Which assay, population, and endpoint produced a value?|State protocol, variability, and error.
scale_and_timespan|Cell Result to Ecosystem Claim|When does a finding fail to transfer across scale?|Identify intermediate evidence and time span.
field_vs_lab|Organism in Lab and Wild|Which controlled conditions differ from natural settings?|Compare behavior, genetics, and environment.
natural_variation|Variation Within a Species|How do individuals and populations differ?|Sample beyond a single laboratory strain.
mechanism_chain|A Biological Pathway Tested|Which intermediate steps have direct evidence?|Use perturbation and rescue where appropriate.
extreme_case|An Organism at a Limit|What does an extreme habitat reveal about a process?|Check representativeness and measurement.
classification_debate|Defining a Biological Group|Which characters or sequence evidence support a classification?|Compare taxonomic alternatives.
interacting_systems|Organism and Environment|Which other species or conditions alter the outcome?|Measure interactions and confounders.
data_gap|Unstudied Life Forms|Which species, habitats, or populations lack evidence?|Map sampling and research bias.
prediction_test|A Biological Model's Test|Which observable outcome would challenge it?|State predicted change and control in advance.
human_impact|Human Use of Biological Knowledge|Who benefits or bears risk from an application?|Separate basic finding from validated use.
field_species_variation|Species Are Not Interchangeable|Does a process vary across related organisms?|Compare matched methods and phylogeny.
field_ecological_role|Role in a Living System|What does a species do in its ecosystem?|Use field observations and interaction data.
field_experimental_model|A Model Organism's Limits|What human or wild condition does it represent poorly?|Check external validation.
field_evolutionary_history|A Trait's History|Which evidence supports an evolutionary pathway?|Use phylogeny, fossils, and comparative anatomy.
field_conservation_status|Evidence for a Conservation Assessment|Which population and threat data support status?|Use official current assessment and local context.
"""

NEUROSCIENCE = """history_origins|A Neural Function Hypothesis|Which observation and experiment linked a neural structure to function?|Use dated methods and later tests.
famous_examples|A Famous Brain Study Rechecked|What did it actually measure and in whom?|Read sample, method, inference, and limitations.
hidden_stories|Participants and Research Staff|Who provided data, maintained instruments, and supported studies?|Use consented accounts and credit roles.
beginner_explainers|Neurons to Behavior|How can cells, circuits, body, and environment shape one task?|Use a bounded function without locating all cause in one region.
advanced_concepts|Correlation and Causation in the Brain|Which intervention supports a circuit-level claim?|Compare recording, perturbation, behavior, and confounders.
mysteries_unsolved_cases|An Unexplained Neural Signal|Could motion, instrument, or physiology explain it?|Inspect controls and independent methods.
technology_innovation|A New Neural Recording Method|Which cells or timescales became observable?|Compare resolution, invasiveness, and validation.
people_personalities|A Neuroscience Design Debate|How did a team choose participants, task, and method?|Read protocol and ethical review.
major_events|A Brain Map Release|Which data and analyses were released and independently checked?|Separate atlas publication from complete functional explanation.
how_it_works|A Neural Circuit in a Task|What signals and feedback are observed during a defined behavior?|Name species, method, and uncertainty.
rise_fall|A Brain Theory Reconsidered|Which replication or new technique changed confidence?|Compare evidence and model scope.
then_vs_now|One Neural Question Across Tools|How did recording or stimulation alter inference?|Match task and population where possible.
future_developments|A Proposed Neural Study|What method and participant safeguards are needed?|State hypothesis, validation, consent, and limits.
myths_vs_facts|A Brain Scan Reads Thoughts?|Which signal and trained task does it actually decode?|Explain narrow inference and individual variation.
documentary_stories|One Neural Finding's Path|How did participant recruitment, recording, analysis, and publication unfold?|Use consented and deidentified records.
observation_to_explanation|From Signal to Function|Which inference turns activity into a behavioral claim?|Check timing, controls, and alternatives.
measurement_method|Measuring Neural Activity|Which electrode, imaging, or behavior measure was used?|State spatial and temporal resolution.
scale_and_timespan|Synapse to Behavior|What evidence links different levels and time scales?|Identify missing intermediate tests.
field_vs_lab|Neural Task in Real Life|Does a controlled task represent everyday behavior?|Compare context, fatigue, and participant diversity.
natural_variation|Brains Differ Across People|How do age, experience, and health affect a result?|Report sample and within-person variation.
mechanism_chain|Circuit Contribution Tested|Which cells, connections, and feedback steps are supported?|Compare observation with causal intervention.
extreme_case|A Rare Neural Condition|What can an unusual case reveal without overgeneralizing?|Protect privacy and compare broader evidence.
classification_debate|Naming a Brain Cell Type|Which molecular, anatomical, or functional features define it?|Compare atlas criteria and uncertain boundaries.
interacting_systems|Brain, Body, and Environment|Which bodily and social factors alter neural measurements?|Include relevant context and confounders.
data_gap|Who Is Missing from Brain Data?|Which ages, conditions, or communities lack representation?|Audit recruitment and method accessibility.
prediction_test|A Neural Model's Prediction|Which new task or intervention would test it?|Specify outcome and alternative explanation.
human_impact|Using Neuroscience Claims|Who might be affected by overstated decoding or treatment claims?|Separate research from clinical evidence.
field_species_variation|Neural Systems Across Species|Which features are conserved and which differ?|Compare homologous circuits and task validity.
field_ecological_role|Neural Behavior in Context|How does an animal's environment shape a measured circuit?|Use field-relevant behavior and ethical observation.
field_experimental_model|Model Brain's Reach|What can animal or organoid models reveal about humans?|State structural, behavioral, and clinical limits.
field_evolutionary_history|Evolution of a Neural Feature|Which comparative evidence supports shared ancestry?|Use phylogeny, anatomy, and molecular data.
field_conservation_status|Conservation Context of a Study Species|Does research involve a threatened species or habitat?|Check current assessment, permits, and alternatives; this legacy biology slug is retained.
"""


if __name__ == "__main__":
    revise_domain("349", "349_chemistry", CHEMISTRY,
                  "Chemistry as evidence-based study of substances, structures, reactions, measurement, mechanisms, and real-world applications.",
                  "IUPAC terminology and metrology guidance, original experiments, analytical validation, lab notebooks, safety records, and independent replication",
                  "Name substance, conditions, units, analytical method, uncertainty, and exposure context. Distinguish measured products from proposed mechanisms and avoid procedural hazard instructions.")
    revise_domain("350", "350_biology", BIOLOGY,
                  "Biology as testable study of living systems across molecules, cells, organisms, populations, and ecosystems.",
                  "original biological studies, specimen and protocol records, independent replication, comparative data, field observations, and official species assessments",
                  "Name organism, population, condition, endpoint, and time. State limits of model-organism generalization and separate basic findings from applied claims.")
    revise_domain("351", "351_neuroscience", NEUROSCIENCE,
                  "Neuroscience as measurement and modeling of neural cells, circuits, behavior, and human experience with ethical and translational limits.",
                  "NIH BRAIN research frameworks, original recording and imaging studies, protocols, participant data protections, independent replications, and model comparisons",
                  "Name species or participant population, task, technique, and resolution. Do not infer mind reading or clinical benefit from a narrow neural correlation.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
