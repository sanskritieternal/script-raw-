"""Editorial questions for human relationships."""

from review_angle_plans import audit, revise_domain


RELATIONSHIPS = """history_origins|How a Relationship Norm Changed|When did one expectation about family or friendship shift?|Compare dated law, surveys, media, and varied personal accounts.
famous_examples|A Widely Cited Relationship Study|What did one study find for whom and under what conditions?|Check design, sample, measures, replication, and limits.
hidden_stories|Care Work Within Relationships|Whose coordination, emotional, and practical labor is overlooked?|Use voluntary accounts and time-use evidence without assigning blame.
beginner_explainers|Studying Relationships Without Stereotypes|What can surveys and interviews reveal about a named relationship?|Define population, measure, context, and privacy boundary.
advanced_concepts|Support, Conflict, and Context|How do resources and institutions shape one relationship pattern?|Compare work, housing, health, policy, and individual variation.
mysteries_unsolved_cases|Why a Tie Weakened|Which documented factors could explain change in one relationship?|Avoid diagnosing private motives; examine circumstances and accounts.
technology_innovation|A Platform Between People|Did one communication tool change contact or support?|Compare access, use, privacy, quality, and different groups.
people_personalities|Two Perspectives on One Bond|How do participants remember the same relationship differently?|Use separate consent, attribution, and no forced reconciliation.
major_events|A Disruption to Social Ties|How did one crisis affect contact and care?|Compare before and after data, constraints, and varied experiences.
how_it_works|Maintaining a Support Network|What practices keep one community relationship network active?|Observe with consent and distinguish help from obligation.
rise_fall|An Organization for Social Connection|Why did one group gain or lose members?|Check access, time, costs, leadership, and changing needs.
then_vs_now|Friendship Across Generations|What evidence supports a claim of change in social ties?|Compare surveys with compatible questions and diverse accounts.
future_developments|A Program to Reduce Isolation|What evidence would show one initiative helps?|Define population, outcomes, consent, cost, and follow-up.
myths_vs_facts|A Universal Relationship Rule?|Does one popular advice claim hold across settings?|Check evidence, cultural variation, and known exceptions.
documentary_stories|A Network of Everyday Care|How do people coordinate help through an ordinary week?|Film with consent and protect third-party conversations.
lived_experience|What Support Feels Like|How does one participant describe help received and given?|Use their terms and avoid claiming representation of a group.
institutional_pathway|Rules That Shape Family Ties|How does one workplace or public policy affect time together?|Trace eligibility, use, barriers, and outcomes.
incentives_norms|Expectations of Reciprocity|How do norms of giving and receiving help differ?|Compare stated values, observed practice, and power differences.
access_and_exclusion|Who Can Join the Gathering?|Which cost, disability, language, or status barriers affect connection?|Check actual venue, schedule, and participant experiences.
community_variation|Different Kinds of Kinship|How do named communities define care and belonging differently?|Use preferred terms and acknowledge variation within groups.
policy_in_practice|A Leave Policy and Relationships|Did one rule change caregiving capacity?|Compare uptake, eligibility, income, schedules, and lived accounts.
survey_vs_story|Loneliness Data and One Life|How does one person's experience relate to measured patterns?|Check survey wording, sample, and individual difference.
power_and_voice|Who Defines a Healthy Relationship?|Whose norms shape a public relationship message?|Review evidence, cultural assumptions, funding, and affected voices.
unintended_consequence|When a Support Program Burdens Helpers|Did one intervention shift unpaid work onto certain people?|Compare workload, resources, outcomes, and alternatives.
comparative_setting|Two Places, Different Social Ties|Which housing or work conditions change opportunities to connect?|Match demographics, schedules, institutions, and measures.
change_over_time|A Tie Through Life Stages|How do support patterns change over a defined period?|Use longitudinal evidence and avoid one inevitable arc.
ethical_dilemma|Filming a Private Relationship|Can all affected people meaningfully consent to publication?|Review privacy, pressure, third parties, withdrawal, and alternatives.
field_social_norms|An Unspoken Relationship Rule|How is one expectation learned and challenged?|Use diverse voluntary accounts and observe context.
field_relationship_network|Mapping Who Helps Whom|What can a network map show without exposing private ties?|Collect minimal permissioned data and mask third parties.
field_group_identity|Who Counts as Family?|How do participants name close relationships?|Use self-description rather than imposing a fixed household model.
field_community_support|Relationships During a Crisis|Which ties provided practical help and which could not?|Compare services, resources, time, and unequal demands.
field_power_difference|Consent Between Unequal Partners|How might dependency affect willingness to speak on camera?|Interview separately, assess risk, and allow refusal without penalty.
"""


if __name__ == "__main__":
    revise_domain("170", "170_human_relationships", RELATIONSHIPS,
                  "Human relationships through support, care, norms, institutions, access, variation, and privacy-aware evidence.",
                  "peer-reviewed studies with defined populations, comparable surveys and time-use data, relevant policies, and separate voluntary consented accounts from participants",
                  "Name relationship type, population, place, and period. Avoid universal relationship advice or diagnosis, protect third-party privacy, and account for power or dependency in consent.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
