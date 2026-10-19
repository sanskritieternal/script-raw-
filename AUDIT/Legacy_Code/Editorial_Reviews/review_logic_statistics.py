"""Editorial questions for arguments and statistical evidence."""

from review_angle_plans import audit, revise_domain


LOGIC = """history_origins|How a Reasoning Rule Developed|Which problem led to one formal or informal rule of inference?|Trace original text, later formulation, and changed assumptions.
famous_examples|A Classic Argument Revisited|Does a well-known argument still work when its premises are stated?|Reconstruct each premise and test validity and factual support separately.
hidden_stories|Who Framed the Debate?|Whose assumptions or experience were omitted from one public argument?|Compare participants, source access, and missing alternatives without motive claims.
beginner_explainers|Premise and Conclusion|How can a reader find what an argument actually claims?|Rewrite one real example in premise-conclusion form and identify unstated steps.
advanced_concepts|Valid but Not Sound|Can an argument be logically valid while based on a false premise?|Show a precise example and test premise truth independently.
mysteries_unsolved_cases|A Disputed Inference|Which step in one complex argument remains contested?|Compare rival reconstructions and the evidence needed to choose.
technology_innovation|A Claim-Checking Tool|Can automated argument mapping identify hidden assumptions reliably?|Compare tool output with expert coding and errors on real examples.
people_personalities|A Thinker's Argument in Context|What did a named thinker actually argue, and how was it revised?|Read primary text, response, and later interpretation.
major_events|A Debate Changed by Evidence|Which new fact altered one public argument?|Compare claims before and after with dated sources.
how_it_works|Testing an Argument|Which checks establish whether reasons support a conclusion?|Assess premise acceptability, relevance, sufficiency, and counterarguments.
rise_fall|A Once Persuasive Argument Fades|What changed in the evidence or assumptions behind it?|Compare its original setting with later findings and revisions.
then_vs_now|The Same Claim Across Eras|How did one argument's premises change over time?|Compare dated versions and the social or scientific context.
future_developments|What Would Change My Mind?|Which possible evidence would alter support for one conclusion?|State a falsifiable threshold and plausible alternatives before outcome.
myths_vs_facts|The Fallacy Label Tested|Does naming a fallacy actually refute one argument?|Reconstruct the strongest version and examine support, not labels alone.
documentary_stories|One Claim's Public Journey|How did an argument move from source to debate and correction?|Trace exact wording, citation, counterargument, and revisions.
observation_to_explanation|From Event to Cause|Does an observation warrant a causal conclusion?|List alternative causes and evidence that would separate them.
measurement_method|Checking the Evidence Premise|Was a key premise measured in a way that supports the argument?|Read source methods and limits before judging inference.
scale_and_timespan|One Case to General Rule|When does a single example fail to support a broad conclusion?|Compare scope of evidence with scope of claim.
field_vs_lab|Reasoning in Controlled and Public Settings|Does a logical classroom example map onto a messy real case?|State simplifying assumptions and missing evidence.
natural_variation|Noise Mistaken for Pattern|How can normal variation create a persuasive but weak argument?|Use a transparent illustrative series and alternative interpretations.
mechanism_chain|The Missing Middle Step|Which causal link is assumed but never shown in one argument?|Draw the chain and identify evidence for each link.
extreme_case|A Hard Case for the Rule|Does an edge case reveal a faulty assumption or a genuine exception?|Test the exact rule against a carefully defined case.
classification_debate|A Definition Drives the Dispute|Are two sides using the same meaning of a key term?|Compare explicit definitions and consequences for each claim.
interacting_systems|Several Causes, One Outcome|Why is a single-cause explanation inadequate in one case?|Map interactions and show which links have evidence.
data_gap|An Argument With Missing Evidence|Which premise lacks a traceable source?|Identify source gap and state what cannot be concluded.
prediction_test|A Claim Before the Outcome|Did one argument make a testable prediction in advance?|Compare dated prediction, conditions, outcome, and reinterpretations.
human_impact|Consequences of a Weak Argument|Who was affected when one unsupported inference guided a decision?|Trace decision record and outcomes without assuming intent.
field_proof_or_test|Testing a Formal Inference|Can a countermodel show that one conclusion does not follow?|State premises, construct a model, and check the conclusion.
field_definition_choice|Ambiguity in a Key Term|How does shifting the meaning of one word change an argument?|Use two clear interpretations and test each inference.
field_model_assumptions|Assumptions Under a Policy Claim|Which assumptions must hold for one proposed consequence to follow?|List conditions, evidence, and alternative outcomes.
field_counterexample|A Counterexample That Counts|Does a proposed counterexample satisfy the argument's premises?|Check each premise before claiming refutation.
field_teaching_difficulty|Where Reasoning Goes Wrong|Which inference error recurs in anonymized learner work?|Classify errors and test a revised explanation with a new case."""


STATISTICS = """history_origins|Why a Statistical Method Was Invented|Which research or administrative problem motivated one method?|Trace original assumptions, data type, and later modifications.
famous_examples|A Famous Dataset Reanalyzed|Does a widely cited result survive alternative valid analyses?|Compare original data, code, estimand, and sensitivity checks.
hidden_stories|Who Was Not Counted?|Which population was missed by a survey or administrative dataset?|Inspect sampling frame, nonresponse, and affected-group accounts.
beginner_explainers|What Does the Average Hide?|How can identical averages describe different distributions?|Use transparent small datasets and show spread and shape.
advanced_concepts|Estimand Before Estimate|What quantity is a study trying to learn, and what was actually measured?|Define target population, intervention or exposure, outcome, and method.
mysteries_unsolved_cases|Conflicting Statistics|Why do two credible estimates of the same topic disagree?|Compare definitions, populations, periods, adjustments, and uncertainty.
technology_innovation|A New Data Pipeline|Did automation improve timeliness at the cost of data quality?|Compare missingness, validation, revisions, and documentation.
people_personalities|The Statistician's Design Choice|Which sampling or modeling decision shaped one result?|Use methods records and team contributions rather than biography alone.
major_events|A Revision Changes the Headline|Why did an official estimate change after release?|Trace new data, correction, seasonal adjustment, or definition changes.
how_it_works|From Sample to Estimate|How is a sample used to estimate a population quantity?|Follow frame, selection, weighting, estimate, and uncertainty.
rise_fall|A Metric Loses Trust|Which documented errors or incentives weakened one indicator?|Compare original purpose, revisions, manipulation risks, and alternatives.
then_vs_now|A Trend That May Not Be Comparable|Did a method change create an apparent rise or fall?|Compare definitions, collection mode, coverage, and revised series.
future_developments|Designing the Next Data Collection|What information would most reduce uncertainty on one question?|Specify target, frame, sample, measurement, privacy, and cost.
myths_vs_facts|Significant Means Important?|Does a reported statistical significance imply a meaningful effect?|Compare effect size, uncertainty, study design, and practical threshold.
documentary_stories|A Number's Production Trail|How did one public statistic move from raw records to headline?|Trace cleaning, exclusions, modeling, review, and correction.
observation_to_explanation|A Correlation Appears|Can one observed association support a causal story?|Check confounding, reverse causation, design, and alternatives.
measurement_method|Measuring What Matters|Does a variable capture the concept named in a chart?|Compare operational definition, reliability, and validation.
scale_and_timespan|Daily Noise and Long Trend|How does aggregation change an apparent pattern?|Compare daily, monthly, and yearly views on one dataset.
field_vs_lab|Controlled Sample Versus Population|Can a study result apply outside its recruited participants?|Inspect selection, setting, intervention fidelity, and heterogeneity.
natural_variation|Separating Signal From Variation|Is a change larger than expected sampling or process variation?|Show uncertainty model and assumptions rather than one threshold.
mechanism_chain|From Treatment to Outcome|Which measured steps support a proposed causal pathway?|Distinguish total effect, mediation assumptions, and missing links.
extreme_case|An Outlier in the Dataset|Is an extreme value an error, a real case, or a sign of model failure?|Verify source, influence, and justified treatment.
classification_debate|Changing a Category|How do alternative category boundaries change an estimate?|Compare definitions, reclassified observations, and policy consequences.
interacting_systems|Two Variables Are Not Enough|Which interacting factors change one statistical relationship?|Use a prespecified model and clearly scoped interpretation.
data_gap|Missing Data Are Not Random|How could nonresponse distort one conclusion?|Map missingness, plausible mechanisms, and sensitivity ranges.
prediction_test|A Model Meets New Data|How well did a prediction perform beyond its training sample?|Check calibration, discrimination, time drift, and subgroup errors.
human_impact|A Metric Used to Allocate Resources|Who gains or loses when one indicator drives a decision?|Trace rule, data quality, appeals, and observed effects.
field_proof_or_test|Checking a Statistical Claim|Can an independent analyst reproduce one published estimate?|Use shared data and code, document differences, and protect privacy.
field_definition_choice|Who Is in the Denominator?|How does denominator choice change a reported rate?|Show counts, exclusions, time basis, and alternative rates.
field_model_assumptions|What the Model Assumes|Which assumption most influences one estimate?|Vary it transparently and report sensitivity.
field_counterexample|Averages Mislead|Can two groups have the same average but very different outcomes?|Construct valid small distributions and explain relevance.
field_teaching_difficulty|Reading Uncertainty Correctly|Which mistake do learners make about one confidence interval or p-value?|Use anonymized responses and test a clearer worked explanation."""


if __name__ == "__main__":
    revise_domain("120", "120_logic_critical_thinking", LOGIC,
                  "Logical and critical reasoning through explicit claims, premises, inference, definitions, alternatives, and the evidence behind public arguments.",
                  "original arguments and source documents, formal reconstructions, relevant empirical evidence, dated corrections, and anonymized learner work",
                  "Quote claims in context and distinguish validity from premise truth. Avoid fallacy-name shortcuts, motive speculation, and treating disagreement itself as proof of error.")
    revise_domain("121", "121_statistics_data", STATISTICS,
                  "Statistical reasoning through populations, measurement, sampling, uncertainty, modeling, reproducibility, and effects on decisions.",
                  "original datasets and code where available, survey and measurement methods, official revisions, independent reanalyses, and data documentation",
                  "Define population, denominator, period, and estimand. Distinguish association from causation and statistical significance from practical importance; protect private records.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
