"""Editorially reviewed questions for scientific careers and mathematics."""

from review_angle_plans import audit, revise_domain


SCIENTISTS = """history_origins|The Work Before a Discovery|Which earlier observations and tools made one discovery possible?|Trace prior publications, datasets, and collaborators with dates.
famous_examples|A Famous Discovery Revisited|What did the original experiment establish, and what came later?|Read methods and results before retelling a celebrated story.
hidden_stories|The Uncredited Contributors|Whose field, laboratory, computing, or technical work is absent from credit?|Compare notebooks, acknowledgments, correspondence, and worker accounts.
beginner_explainers|What Does a Discovery Claim Mean?|How did one scientist define and test a specific claim?|Distinguish observation, hypothesis, method, result, and uncertainty.
advanced_concepts|Discovery, Priority, and Proof|When can separate teams claim priority for a result?|Compare dated work, publication, replication, and the claim each team made.
mysteries_unsolved_cases|An Attribution Still Disputed|Which evidence supports rival accounts of one discovery?|Map archives, dates, missing documents, and later recollections.
technology_innovation|An Instrument Changes the Question|How did a new tool permit one scientist to observe something new?|Compare measurement limits before and after adoption.
people_personalities|A Scientist's Research Choice|Why did a named researcher pursue one question at a particular time?|Use dated correspondence and institutional context without mind-reading.
major_events|A Result That Redirected a Field|What changed in research after one published finding?|Track citations, competing work, replication, and later revisions.
how_it_works|From Observation to Accepted Result|Which checks turned one observation into a reliable finding?|Trace controls, analysis, independent tests, and peer criticism.
rise_fall|A Theory Loses Ground|Which observations or tests weakened one scientific explanation?|Compare original predictions, contradictory data, and replacement models.
then_vs_now|A Scientist's Claim Across Time|How did the interpretation of one result change?|Compare original paper, later evidence, and current bounded understanding.
future_developments|What Would Settle the Question?|Which feasible result would discriminate among current scientific explanations?|State competing predictions and limits without announcing a future discovery.
myths_vs_facts|The Eureka Moment Tested|Does a single-moment story fit the dated research record?|Compare notebooks, correspondence, published steps, and collaborators.
documentary_stories|A Discovery in Primary Records|How did one claim move from first observation to independent acceptance?|Build a dated, source-linked chain with disagreements and corrections.
observation_to_explanation|An Anomaly Becomes a Hypothesis|How did one scientist turn unexpected data into an explanation?|Show the observation, alternative causes, and proposed test.
measurement_method|What the Instrument Measured|Which calibration and sampling choices shaped one reported result?|Review original methods, errors, and later checks.
scale_and_timespan|From One Sample to a Field Claim|Was the original sample broad enough for later generalizations?|Compare population, time, geography, and subsequent studies.
field_vs_lab|Laboratory Result and Real World|Did a controlled finding survive outside the lab?|Compare conditions, independent replication, and boundary limits.
natural_variation|Signal Amid Variation|How did researchers distinguish a pattern from background variation?|Inspect controls, repeated measures, and uncertainty reporting.
mechanism_chain|A Scientist's Proposed Mechanism|Which links in the proposed mechanism were directly tested?|Separate measured steps, models, and later assumptions.
extreme_case|An Outlier That Mattered|Did an extreme case reveal a rule or a measurement problem?|Compare original record, verification, and broader evidence.
classification_debate|Naming a New Phenomenon|How did competing classifications affect one research claim?|Compare definitions, data assignments, and downstream conclusions.
interacting_systems|A Discovery Across Disciplines|Which fields contributed methods or concepts to one finding?|Trace cross-field collaboration and limits of each approach.
data_gap|The Missing Notebook or Dataset|Which absent evidence prevents a full account of one research result?|Inventory archives, missing files, and claims that cannot be resolved.
prediction_test|A Prediction Made Before Results|Did a theory predict an observation before it was measured?|Compare dated proposal, test protocol, result, and post hoc changes.
human_impact|Who Benefited From a Discovery?|How did one finding affect people after application?|Separate original scientific claim from later products, policy, and harms.
field_proof_or_test|Reconstructing a Decisive Test|Which controls and outcomes make one experiment informative?|Use published protocol and reports without unsafe replication instructions.
field_definition_choice|What Did Discovery Mean?|Does a priority dispute use the same definition of discovery?|Compare observation, explanation, publication, and application milestones.
field_model_assumptions|Assumptions Behind a Result|Which assumptions did one scientist state or leave implicit?|Trace model choice, calibration, and sensitivity analysis.
field_counterexample|A Contradictory Finding|How did researchers respond to a credible counterexample?|Check independent tests, corrections, and revised scope.
field_teaching_difficulty|The Simplified Discovery Story|What does a textbook version omit from the research process?|Compare original papers with classroom account and learner understanding."""


MATH = """history_origins|Where a Mathematical Idea Emerged|Which problems and earlier work led to one concept?|Compare dated texts, translations, and multiple traditions without sole-origin claims.
famous_examples|A Famous Theorem in Use|What does one theorem say exactly, and where does it apply?|State definitions and assumptions, then work one valid example.
hidden_stories|Contributors to a Proof|Whose earlier lemmas, computation, or teaching shaped a named result?|Trace publications and correspondence rather than eponym alone.
beginner_explainers|What Is a Proof?|How does a proof differ from checking many examples?|Use a small proposition and show the general logical step.
advanced_concepts|Changing an Assumption|What happens to one theorem if a key hypothesis is removed?|Build a valid counterexample and explain the role of the condition.
mysteries_unsolved_cases|An Open Problem's Boundary|What is known and unknown about one well-defined problem?|State exact formulation, partial results, and current status with dates.
technology_innovation|Computation Assists Proof|What did a computer check in one mathematical result?|Separate code, exhaustive cases, formal verification, and human argument.
people_personalities|A Mathematician's Problem Choice|How did a named mathematician approach one problem?|Use original work and context, distinguishing personal story from proof.
major_events|A New Proof Changes a Field|What did one published proof settle and what remained open?|Compare original theorem, proof dependencies, later corrections, and uses.
how_it_works|Following One Argument|Why does each step in a short proof follow?|Lay out definitions, inference, and conclusion with one worked case.
rise_fall|A Proposed Proof Fails|Which step failed in a once-claimed proof?|Locate the gap or counterexample and explain subsequent revision.
then_vs_now|One Concept Across Mathematical Eras|How did its definition or notation change?|Compare original and modern formulations while preserving logical content.
future_developments|A Path Toward an Open Problem|Which subproblem could genuinely advance a current question?|Map known results and conditional ideas without promising a solution.
myths_vs_facts|The Formula Origin Myth|Does a named formula have earlier versions or collaborators?|Check dated sources, attribution, and differences in formulation.
documentary_stories|From Conjecture to Theorem|How did one conjecture move through failed attempts and a final proof?|Build a dated record of statements, counterexamples, and peer scrutiny.
observation_to_explanation|A Pattern in Numbers|How can a numerical pattern suggest a conjecture without proving it?|Show examples, propose exact statement, and search for exceptions.
measurement_method|What Counts as a Calculation?|How can rounding or numerical error mislead a mathematical conjecture?|Compare exact arithmetic with approximate computation.
scale_and_timespan|Beyond the First Thousand Cases|Why do finite checks not settle an infinite claim?|Use a constructed counterexample or proof principle.
field_vs_lab|Abstract Result and Application|When does a theorem model a real-world situation accurately?|State model assumptions and compare with application data separately.
natural_variation|Random Example Versus General Rule|Can random tests reveal a structural mathematical truth?|Use tests as exploration and identify what proof must establish.
mechanism_chain|Why an Algorithm Works|Which invariant makes one algorithm correct?|Trace initialization, preservation, termination, and output.
extreme_case|A Boundary Case Exposes an Error|Which edge case breaks a plausible formula?|Check zero, equality, limits, or singular inputs as relevant.
classification_debate|Defining a Mathematical Object|How do two definitions change which examples belong?|Compare definitions, edge cases, and resulting theorems.
interacting_systems|One Idea Across Branches|How does a concept connect algebra, geometry, or probability?|Show a precise mapping and limits of the analogy.
data_gap|A Missing Proof Step|Which claim in a published argument needs additional justification?|Identify the lemma, cited source, and independent checks.
prediction_test|Testing a Conjecture Strategically|Which examples are most likely to expose a false conjecture?|Choose boundary and structured counterexamples, not only random cases.
human_impact|Mathematics in a Decision System|How can a mathematical model affect real people when deployed?|Separate theorem validity from data quality, objectives, and governance.
field_proof_or_test|A Proof in Full|Can a short proposition be proved from stated premises?|Present every essential inference and test illustrative cases afterward.
field_definition_choice|The Power of a Definition|Why does a precise definition settle an apparent disagreement?|Compare two formulations and show a separating example.
field_model_assumptions|When a Model Applies|Which assumption determines whether a mathematical model fits a case?|Vary one premise and compare formal result with actual context.
field_counterexample|One Case Refutes the Claim|What counterexample disproves a tempting general statement?|Verify the case satisfies all premises before showing failure.
field_teaching_difficulty|Where Learners Lose the Proof|Which inference in one proof is hardest for a defined learner group?|Use anonymized work, a targeted explanation, and delayed transfer."""


if __name__ == "__main__":
    revise_domain("118", "118_scientists_discoverers", SCIENTISTS,
                  "Scientists and discoveries through dated claims, tools, collaborators, tests, replication, attribution, and later reinterpretation.",
                  "original publications, laboratory and field records where available, correspondence and archives, independent replication reports, and credible science histories",
                  "Name scientist, exact claim, date, and field. Distinguish discovery, explanation, publication, and application; credit contributors and avoid unsafe experiment instructions.")
    revise_domain("119", "119_mathematics", MATH,
                  "Mathematics through precise definitions, examples, proofs, counterexamples, models, and the documented history of ideas.",
                  "original mathematical papers and texts, verified proofs and corrections, reputable historical scholarship, and anonymized learner work where relevant",
                  "State definitions and hypotheses before conclusions. Distinguish proof from numerical testing and mathematical validity from real-world model fitness; verify open-problem status before production.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
