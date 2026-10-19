"""Editorial questions for human behavior."""

from review_angle_plans import audit, revise_domain


BEHAVIOR = """history_origins|How a Behavior Became a Research Topic|Why did researchers begin measuring one common action?|Trace original question, method, context, and later revisions.
famous_examples|A Famous Behavioral Finding Revisited|Does one celebrated effect replicate in relevant settings?|Check sample, outcome, preregistration, replication, and limits.
hidden_stories|People Outside the Experiment|Who was excluded from one behavioral claim?|Examine recruitment, language, culture, age, and accessibility.
beginner_explainers|Observed Action Versus Stated Intention|Why can what people say differ from what they do?|Use one bounded case and compare measures without accusing participants.
advanced_concepts|Person, Situation, and Behavior|How do context and individual differences jointly shape an action?|Compare repeated observations, constraints, and variation.
mysteries_unsolved_cases|An Unexpected Choice Pattern|Which explanations fit one observed decision?|Test framing, incentives, selection, measurement, and chance.
technology_innovation|A Digital Behavior Measure|Does one app or sensor capture the action it claims to?|Check validity, missing data, privacy, and reactivity.
people_personalities|A Researcher's Design Choice|How did one team's assumptions affect a behavioral study?|Review protocol, power, ethics, analysis, and critique.
major_events|Behavior During a Disruption|Which actions changed after one crisis and for whom?|Compare contemporaneous data, constraints, and alternatives.
how_it_works|Testing a Behavioral Explanation|How are hypotheses, controls, and outcomes specified?|Follow a published study and explain causal limits.
rise_fall|A Habit Over Time|What evidence shows one behavior became more or less common?|Use compatible series, cohort context, and reporting changes.
then_vs_now|The Same Choice in Two Eras|How did circumstances and measured choices change?|Match population, options, incentives, and data method.
future_developments|A Behavior-Change Program|What would show one proposed intervention works fairly?|Define outcome, consent, comparison, persistence, and unequal effects.
myths_vs_facts|A Claim About Human Nature|Does a universal behavior claim survive cross-context evidence?|Check population, task, culture, and counterexamples.
documentary_stories|One Decision in Its Setting|What constraints shaped a person's choice?|Use consented account, available options, and no inferred motive.
lived_experience|The Meaning of an Action|How does a participant explain their own behavior?|Compare their account with context without claiming diagnosis.
institutional_pathway|Rules That Guide Action|How does one institution make some choices easier?|Trace defaults, eligibility, sanctions, and actual uptake.
incentives_norms|Reward and Social Expectation|Which pressures shape a named behavior?|Compare incentives, norms, resources, and observed actions.
access_and_exclusion|Who Can Choose Otherwise?|Which physical, financial, or social barriers constrain one action?|Measure available options before attributing behavior to preference.
community_variation|A Pattern Within Groups|How much does behavior vary inside a named population?|Disaggregate responsibly and avoid stereotypes.
policy_in_practice|A Nudge in the Real World|Did one design change produce a lasting outcome?|Check comparison, opt-out, unintended effects, and ethics.
survey_vs_story|Self-Report Versus Trace Data|Why do two measures of behavior differ?|Compare consent, recall, measurement, coverage, and privacy.
power_and_voice|Who Defines the Problem Behavior?|Whose interests set one intervention target?|Review authority, evidence, affected people, and alternatives.
unintended_consequence|A Change That Backfired|Did one intervention shift harm to another group or task?|Compare intended outcome, spillovers, and costs.
comparative_setting|One Behavior in Two Contexts|Which situational differences explain different rates?|Match measurement, population, access, and norms.
change_over_time|A Cohort or Period Effect?|Does a trend reflect aging, generation, or current conditions?|Use longitudinal or repeated cross-section data with limits.
ethical_dilemma|Observing Without Intrusion|How can a behavior be studied while respecting autonomy?|Review consent, privacy, deidentification, and alternative methods.
field_social_norms|A Behavior Others Notice|How do expectations and sanctions affect one action?|Use voluntary accounts and distinguish perception from measured prevalence.
field_relationship_network|Behavior Spreads Through Ties?|Does a network pattern show influence or shared context?|Check timing, selection, confounding, and third-party privacy.
field_group_identity|Identity and Action|How do people connect one behavior to belonging?|Use self-description and avoid assigning a trait to all members.
field_community_support|Changing Behavior Together|What resources help a group make an intended change?|Trace support, constraints, outcomes, and unequal labor.
field_power_difference|Researcher Influence on Behavior|Does being observed alter what participants do?|Document recruitment, setting, incentives, and reactivity.
"""


if __name__ == "__main__":
    revise_domain("171", "171_human_behavior", BEHAVIOR,
                  "Human behavior through observed choices, context, methods, variation, incentives, and ethical intervention.",
                  "peer-reviewed and replicated studies, preregistered protocols where available, behavior measures with validation, comparable surveys, institutional records, and consented participant accounts",
                  "Name behavior, population, setting, method, and date. Avoid universal human-nature claims, mind reading, or diagnosis; distinguish association from causal evidence and protect participant privacy.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
