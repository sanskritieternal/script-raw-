"""Editorial questions for digital biology, AI research, and developer AI."""

from review_angle_plans import audit, revise_domain


DIGITAL_BIOLOGY = """history_origins|Biology Becomes Computable|Which dataset or computational method changed a defined biological question?|Use dated repository, method, and study records.
famous_examples|A Digital Biology Claim Rechecked|Did one model predict a result later tested experimentally?|Compare prediction, independent experiment, and uncertainty.
hidden_stories|People Behind Biological Data|Who collected specimens, annotated records, and maintained repositories?|Trace credit, consent, and data provenance.
beginner_explainers|From Sample to Digital Record|How does a biological specimen become analyzable data?|Trace sampling, measurement, metadata, processing, and interpretation.
advanced_concepts|Model Versus Living System|Which assumptions make a biological simulation useful or misleading?|Compare predictions with independent observations.
mysteries_unsolved_cases|A Dataset Disagreement|Why do two biological datasets disagree?|Check species, sampling, protocol, version, and annotation.
technology_innovation|A New Biological Model|Did it improve a named research task?|Test external data, baseline, uncertainty, and laboratory confirmation.
people_personalities|A Data Stewardship Decision|Who decided how biological records would be shared?|Examine contributors, communities, access, and attribution.
major_events|A Repository or Method Release|What became possible after one data or software release?|Use dated availability and independent reuse evidence.
how_it_works|A Computational Biology Pipeline|How are raw observations cleaned, analyzed, and interpreted?|Trace a named dataset and versioned workflow.
rise_fall|A Biological Hypothesis Reassessed|What new data or method changed confidence?|Compare original and later evidence without claiming universal reversal.
then_vs_now|One Question Across Data Generations|Did additional resolution improve biological inference?|Match organism, sampling, outcome, and measurement method.
future_developments|A Proposed Digital Biology Tool|What would validate usefulness beyond training data?|Require external samples, mechanistic checks, and practical outcome.
myths_vs_facts|A Model Replaces Experiments?|Which predictions still need observation or intervention?|Separate computational plausibility from biological confirmation.
documentary_stories|A Dataset's Journey|How did a specimen and its records reach a published result?|Follow consent, metadata, analysis, and reanalysis.
observation_to_explanation|From Record to Biological Account|Which measurements support an explanation rather than correlation?|Trace specimen, instrument, model, and independent evidence.
measurement_method|How Biological Data Are Measured|Which sampling and instrument choices shape a digital record?|Report protocol, calibration, metadata, and error.
scale_and_timespan|Scale Changes an Inference|Does a finding hold across molecule, organism, population, or ecosystem?|Define scale and observation period.
field_vs_lab|Digital Prediction Meets Living Context|Does a laboratory or computational result persist in the field?|Compare conditions, controls, and measured outcome.
natural_variation|Variation Beyond the Reference|Which organisms or populations differ from a reference dataset?|Check sampling, taxonomy, and uncertainty.
mechanism_chain|From Sequence to Function|Which causal steps connect a digital pattern to biological effect?|Seek experimental tests for each proposed link.
extreme_case|An Outlier That Tests the Model|Does an unusual organism or condition reveal a model limit?|Check data quality before biological interpretation.
classification_debate|What Counts as One Biological Group?|How do alternative taxonomies or annotations change results?|Compare versioned definitions and evidence.
interacting_systems|Organisms in Their Context|Which ecological or molecular interactions were omitted from a model?|Map interacting processes and available observations.
data_gap|Missing Specimens and Metadata|Which geographic or biological gaps limit inference?|Audit collection design and repository completeness.
prediction_test|A Computational Claim Put to Test|Which independent experiment or observation could falsify a prediction?|Specify outcome, control, and sample before testing.
human_impact|People and Biological Data|How do sampling, reuse, and applications affect communities?|Check consent, access, benefit sharing, and harms.
field_species_variation|Variation in the Data|Does a result hold across species or populations?|Check taxonomy, sampling, and biological relevance.
field_ecological_role|Model in an Ecosystem|Does a digital prediction account for species interactions?|Compare field observations and context.
field_experimental_model|Computational and Wet-Lab Model|What does each experimental system reveal or miss?|State organism, cell model, intervention, and external validity.
field_evolutionary_history|Phylogeny from Digital Evidence|Which data and assumptions support an inferred relationship?|Compare markers, reference versions, and uncertainty.
field_conservation_status|Data for Conservation Decisions|Can digital observations inform a species assessment?|Check geographic coverage, sampling bias, and official status source.
"""

AI_RESEARCH = """history_origins|A Research Method Emerges|Which dated experiment established a narrow AI technique?|Read original method, baseline, and replication.
famous_examples|A Benchmark Result Rechecked|Does a celebrated score transfer to a useful task?|Compare dataset, contamination risk, metric, and field test.
hidden_stories|Research Labor Behind a Model|Who labels data, maintains infrastructure, and reproduces results?|Credit contributors and examine conditions.
beginner_explainers|From Question to AI Experiment|How do hypothesis, data, baseline, model, and evaluation fit?|Trace a published study without assuming its claim is true.
advanced_concepts|Generalization Beyond a Test Set|What evidence supports performance outside training conditions?|Use independent split, shift, and uncertainty measures.
mysteries_unsolved_cases|A Result That Would Not Replicate|Which data, code, compute, or metric differences explain divergence?|Compare public artifacts and unresolved gaps.
technology_innovation|A New Model Architecture|Which capability improved under equal evaluation?|Control data, compute, metric, and baseline.
people_personalities|A Research Dispute|How did teams argue over one claim or method?|Read papers, critiques, responses, and replications.
major_events|An AI Paper's Impact|Which follow-up studies confirmed, limited, or rejected it?|Build dated citation and replication trail.
how_it_works|A Research Pipeline|How are data, training, validation, and reporting connected?|Follow a named experiment and versioned artifacts.
rise_fall|A Benchmark Becomes Obsolete|Which saturation, leakage, or task mismatch changed its value?|Compare original purpose with later use.
then_vs_now|A Capability Across Model Generations|Did progress persist under matched tests?|Control prompt, data access, tools, budget, and scoring.
future_developments|A Promised Research Direction|What falsifiable test would support the proposal?|State hypotheses, resource assumptions, and failure criteria.
myths_vs_facts|One Score Means General Intelligence?|Which tasks and populations lie outside the benchmark?|Inspect evaluation scope and uncertainty.
documentary_stories|A Claim from Preprint to Replication|How did the evidence change through review and reuse?|Follow dated versions and independent tests.
system_boundary|Model or Whole System?|Which results depend on retrieval, tools, humans, or prompt design?|Draw inference and evaluation boundaries.
input_output_trace|One Evaluated Example|What input, context, output, and grading produced a score?|Record protocol while protecting restricted test data.
design_tradeoff|Scale Versus Data Quality|Which investment improved the target outcome?|Compare controlled experiments and costs.
failure_mode|A Model's Systematic Error|What conditions reveal a repeatable failure?|Use benign, representative tests and report frequency.
testing_limits|The Missing Evaluation Population|Who or what was absent from the test?|Inspect dataset construction and external validity.
standards_interoperability|Research Artifacts for Reuse|Can others load and evaluate the model under clear terms?|Check format, license, dependency, and documentation.
security_threat_model|Research Release Risks|What misuse or data exposure is plausible for a named artifact?|Assess bounded risks without harmful recipes.
maintenance_lifecycle|An AI Result Over Time|What happens when datasets, libraries, and hardware change?|Track reproducibility and model updates.
infrastructure_dependencies|Compute Behind the Claim|Which hardware, energy, datasets, and software made the experiment possible?|Report resources and access limits.
accessibility_usability|Research Tools for Others|Can independent groups understand and rerun the method?|Test documentation and resource requirements.
independent_replication|Reproducing a Paper's Result|Can another team obtain a comparable score?|Publish seeds, code, data rights, hardware, and variance.
responsible_deployment|Research to Use|Which risks need study before a lab result reaches users?|Consult domain experts and affected groups.
field_training_or_control_data|Training Data Provenance|Which sources, labels, and exclusions shaped a result?|Check permissions, quality, leakage, and representation.
field_real_world_testing|Research Model in Context|Does performance hold on actual user tasks?|Measure distribution shift, costs, and harms.
field_human_oversight|Humans in the Evaluation Loop|Which judgments came from annotators or evaluators?|Document instructions, disagreement, and appeals.
field_failure_recovery|When a Research System Fails|How are invalid outputs identified and corrected?|Define monitoring, escalation, and rollback for trials.
field_hardware_dependency|Hardware as Experimental Variable|Did accelerator, precision, or memory change results?|Report configuration and repeatability.
"""

DEVELOPER_AI = """history_origins|AI in Developer Tools|Which task did an early code-assistance system actually support?|Use dated tools, studies, and task descriptions.
famous_examples|A Coding Assistant Demo Rechecked|Does it solve the same task in a real repository?|Compare environment, tests, human edits, and time.
hidden_stories|People Behind Generated Code|Who curates examples, reviews suggestions, and fixes failures?|Credit maintainers and developers.
beginner_explainers|A Suggestion's Journey|How does a prompt become code a developer may accept?|Trace context, model, edit, review, test, and commit.
advanced_concepts|Correctness Beyond Compilation|Does generated code preserve behavior and security?|Test edge cases, dependencies, and maintainability.
mysteries_unsolved_cases|A Passing Patch That Regressed|Which missed condition explains a generated-code failure?|Trace issue, review, test, and incident evidence.
technology_innovation|A New Coding Agent|Did it improve a defined development task?|Compare controlled repositories, success rate, intervention, and cost.
people_personalities|The Developer's Judgment|How did a reviewer accept, change, or reject an AI proposal?|Use consented workflow study and code review.
major_events|An AI Tool Rollout|What changed after a team introduced it?|Compare adoption, defects, review time, and workload.
how_it_works|AI Edit to Release|How does a generated change pass through normal delivery controls?|Map context, diff, tests, review, build, and deployment.
rise_fall|A Coding Tool Is Retired|Which quality, cost, trust, or workflow issue drove removal?|Compare records and developer feedback.
then_vs_now|One Task With and Without AI|Did time, quality, and comprehension change?|Use matched tasks and account for reviewer effort.
future_developments|A Claimed Autonomous Developer|What evidence would show reliable end-to-end delivery?|Require scoped tasks, independent tests, security, and accountability.
myths_vs_facts|Passing Tests Means Safe Code?|Which untested behavior or vulnerability can remain?|Inspect coverage, requirements, dependencies, and review.
documentary_stories|One AI-Assisted Pull Request|What did the model propose and what did people verify?|Follow diff, tests, comments, and release outcome.
system_boundary|Model, IDE, Repository, and Human|Which system can read, write, or execute code?|Draw permissions and approval boundaries.
input_output_trace|A Repository Prompt to Diff|What context was sent and how did a suggestion change files?|Use redacted logs and consented repository data.
design_tradeoff|Fast Suggestions and Review Load|Does more generated code save or shift work?|Measure accepted lines, defects, comprehension, and upkeep.
failure_mode|A Plausible Wrong Fix|Why did a generated patch miss the real bug?|Use harmless reproductions and code review evidence.
testing_limits|Coding Benchmark Versus Production|Which repository, dependency, and team conditions differ?|State task selection and grading limits.
standards_interoperability|AI Tool Across IDEs|Which context, diff, and tool protocols are portable?|Test named versions and permission models.
security_threat_model|Repository Context Exposure|Who can receive code, secrets, or build access?|Map data flow, permissions, retention, and defensive controls.
maintenance_lifecycle|Maintaining AI-Written Code|Who owns updates, documentation, and future debugging?|Track author attribution and review practice.
infrastructure_dependencies|A Coding Assistant's Supply Chain|Which model endpoint, IDE, packages, and build services are required?|Map outage and vendor dependencies.
accessibility_usability|Developer AI for Different Users|Can developers inspect, reject, and edit suggestions accessibly?|Test interfaces, explanations, and assistive workflows.
independent_replication|Repeating a Productivity Claim|Can another team reproduce a reported gain?|Publish task mix, baselines, metrics, model version, and review cost.
responsible_deployment|AI Code in a Real Product|Who is accountable for defects, licenses, and user harm?|Set review and escalation requirements.
field_training_or_control_data|Code Data and Context|Which repositories or prompts shaped an output?|Check permissions, leakage, provenance, and exclusions.
field_real_world_testing|Assistant in a Real Repository|Does it handle project constraints and passing tests?|Measure task completion and downstream maintenance.
field_human_oversight|Reviewing AI Changes|Can a human understand and reject each proposed diff?|Assess review time, authority, and evidence.
field_failure_recovery|Undoing a Bad AI Edit|Can the team find and reverse a harmful change?|Test version control, rollback, and incident response.
field_hardware_dependency|Compute Behind Developer AI|How do local device and remote model limits affect usability?|Measure latency, connectivity, and resource cost.
"""


if __name__ == "__main__":
    revise_domain("336", "336_digital_biology", DIGITAL_BIOLOGY,
                  "Digital biology as computational analysis and modeling of biological data tied to specimens, species, experiments, ecology, and conservation decisions.",
                  "versioned biological repositories, sample metadata, published methods, computational pipelines, independent experiments, and official species assessments",
                  "Name organism, population, dataset accession, reference version, and biological question. Distinguish modeled predictions from experimental or field evidence.")
    revise_domain("337", "337_ai_research", AI_RESEARCH,
                  "AI research as hypothesis-driven model and system experiments whose data, baselines, evaluation, replication, and resource costs must be documented.",
                  "original papers and revisions, released code and datasets, independent replication, NIST evaluation guidance, and controlled task results",
                  "Name model and artifact versions, task, benchmark, data access, and measurement uncertainty. Do not infer broad capability from a narrow score.")
    revise_domain("338", "338_developer_ai", DEVELOPER_AI,
                  "Developer AI as code suggestions and agents embedded in repositories, review, testing, deployment, and ongoing maintenance.",
                  "versioned tool documentation, consented repository diffs, developer workflow studies, test and incident records, and secure development guidance",
                  "Name tool and model version, task, repository context, human intervention, and review cost. Treat generated code as untrusted until verified.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
