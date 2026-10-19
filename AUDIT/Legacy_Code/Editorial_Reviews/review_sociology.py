"""Editorial questions for sociology."""

from review_angle_plans import audit, revise_domain


SOCIOLOGY = """history_origins|How a Social Category Emerged|When did one institution begin classifying people in a particular way?|Trace forms, law, language, and affected people's responses.
famous_examples|A Landmark Social Study Revisited|What did one influential study establish and miss?|Compare question, sample, method, ethics, replication, and context.
hidden_stories|People Outside the Dataset|Which groups or informal practices were excluded from one study?|Check sampling frame, language, access, and missing records.
beginner_explainers|From Individual Story to Social Pattern|How can a sociologist test whether one experience is common?|Explain population, sample, measure, comparison, and limits.
advanced_concepts|Structure and Personal Choice|How do institutions and individual decisions interact in one outcome?|Compare incentives, constraints, variation, and observed behavior.
mysteries_unsolved_cases|A Social Trend with Competing Causes|Which explanations fit one measured change?|Test timing, composition, policy, economy, and measurement changes.
technology_innovation|A Platform Reshapes a Social Tie|Did one digital system change how a group connects?|Compare before and after networks, access, incentives, and privacy.
people_personalities|A Researcher's Field Decisions|How did one sociologist's position affect access and interpretation?|Review method notes, reflexivity, participant feedback, and critique.
major_events|A Shock to a Community|How did one event alter routines and institutions?|Compare dated observations, different groups, and recovery paths.
how_it_works|Studying a Social Practice|How can interviews, observation, and surveys answer related questions?|Show what each method observes and its blind spots.
rise_fall|A Social Organization's Membership|Why did participation in one association change?|Compare eligibility, costs, work schedules, migration, and data definitions.
then_vs_now|A Social Norm Across Generations|What evidence shows one norm changed?|Compare surveys, behavior, laws, language, and cohort effects.
future_developments|A Proposed Social Policy|Which evidence would indicate its likely effects?|Identify mechanism, comparable cases, affected groups, and uncertainty.
myths_vs_facts|A Claim About a Generation|Does one broad stereotype fit disaggregated evidence?|Check age, cohort, period, class, place, and counterexamples.
documentary_stories|A Social Institution in Daily Use|How does one institution shape an ordinary decision?|Follow voluntary participants and document rules and variation.
lived_experience|A Person Inside a Social Pattern|How does one participant interpret an observed trend?|Use consent and avoid making the person stand for a population.
institutional_pathway|How a Rule Reaches People|Which agencies, employers, or associations implement one policy?|Trace discretion, budgets, enforcement, and appeal.
incentives_norms|Doing What Others Expect|How do rewards and social expectations affect one practice?|Compare stated norm, observed behavior, sanctions, and alternatives.
access_and_exclusion|Barriers to Participation|Who cannot enter one social institution and why?|Measure price, documents, location, disability, language, and informal rules.
community_variation|No Single Community View|How do positions differ within a named group?|Sample across roles and protect minority viewpoints and privacy.
policy_in_practice|A Reform in Everyday Life|Did one new rule change behavior as intended?|Compare implementation, outcomes, unintended effects, and timing.
survey_vs_story|A Poll Against Field Observation|Why might reported attitudes and observed actions differ?|Check wording, social desirability, sample, setting, and time.
power_and_voice|Who Defines the Research Question?|How do funders, institutions, and participants shape one study?|Inspect governance, consultation, publication, and benefit.
unintended_consequence|A Program Changes Incentives|Did one intervention create new burdens or exclusions?|Compare stated goals with varied lived and measured outcomes.
comparative_setting|One Practice in Two Places|Which contextual differences alter a social pattern?|Match population, rules, economy, measurement, and history.
change_over_time|A Trend or a Data Break?|Did one social indicator genuinely change?|Audit definitions, survey mode, coverage, and population.
ethical_dilemma|Studying a Vulnerable Group|How can one question be answered without adding risk?|Review consent, anonymity, data minimization, and participant benefit.
field_social_norms|A Rule People Actually Follow|How does one group teach and enforce a norm?|Use observation and interviews with consent and internal variation.
field_relationship_network|Mapping Social Connections|Which ties matter for one collective activity?|Use permission, minimal data, and protect third parties.
field_group_identity|A Label and Self-Description|How do official categories compare with people's own terms?|Check context, multiple identities, and changing usage.
field_community_support|Informal Help in a Crisis|How do people organize support beyond formal services?|Trace reciprocal work, limits, unequal burdens, and consent.
field_power_difference|Researcher and Participant|How might status affect what someone feels able to say?|Use transparent recruitment, voluntary participation, and reflexive review.
"""


if __name__ == "__main__":
    revise_domain("168", "168_sociology", SOCIOLOGY,
                  "Sociology through social patterns, institutions, norms, inequality, methods, and variation within groups.",
                  "published studies with sampling and method details, disaggregated surveys, institutional records, ethical approvals where applicable, and voluntary consented interviews and observation",
                  "Name population, place, period, measure, and method. Avoid turning one story into a population claim, protect participants and third parties, and distinguish correlation, mechanism, and causal evidence.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
