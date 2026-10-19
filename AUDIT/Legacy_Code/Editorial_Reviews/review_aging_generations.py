"""Editorial questions for ageing and generations."""

from review_angle_plans import audit, revise_domain


AGING = """history_origins|How an Age Category Was Defined|When did one policy or institution set a particular age boundary?|Trace law, pension, census, work, and changed meanings.
famous_examples|An Age-Friendly Project Evaluated|Did one local change improve everyday access for older residents?|Compare stated aims, usage, barriers, cost, and diverse voices.
hidden_stories|Care Across Generations|Whose unpaid and paid work supports people at different ages?|Use time-use data, wages, services, and voluntary accounts.
beginner_explainers|Reading an Ageing Statistic|What does one population measure count and conceal?|Specify age threshold, denominator, geography, period, and inequality.
advanced_concepts|Age, Period, and Cohort|Which of these could explain one observed difference?|Use longitudinal or repeated surveys with uncertainty.
mysteries_unsolved_cases|A Sudden Change in Older Adults' Outcomes|Did health, policy, migration, or measurement shift?|Compare dated data, service changes, population mix, and gaps.
technology_innovation|A Tool for Independent Living|Does one assistive technology meet users' own goals?|Check accessibility, reliability, training, cost, privacy, and alternatives.
people_personalities|An Older Person's Decisions|How does one person negotiate work, care, and independence?|Use their account without treating it as typical or diagnosing them.
major_events|A Crisis Across Ages|How did one event affect cohorts differently?|Compare exposure, resources, policy, and outcomes, avoiding age-only causes.
how_it_works|A Local Care System|How do family, paid care, health services, and transport interact?|Map eligibility, funding, workforce, user choices, and gaps.
rise_fall|An Intergenerational Program's Participation|Why did one program grow or shrink?|Check goals, access, staffing, funding, and participants' views.
then_vs_now|Retirement Across Two Cohorts|How did work, income, health, and policy differ?|Match age and context and adjust money consistently.
future_developments|Planning for an Ageing Population|What evidence supports one proposed service change?|Test demand, workforce, affordability, user priorities, and equity.
myths_vs_facts|A Claim About Older People|Does one stereotype fit evidence across ages and circumstances?|Disaggregate health, income, disability, place, and period.
documentary_stories|A Week in an Age-Friendly Place|Which design and service choices matter to diverse residents?|Follow voluntary participants and verify local infrastructure.
lived_experience|What Age Means to One Person|How does a participant describe age, ability, and identity?|Use self-description and avoid replacing it with a label.
institutional_pathway|From Age Rule to Real Benefit|Who qualifies for one pension or service and who does not?|Trace criteria, enrollment, appeals, coverage, and outcomes.
incentives_norms|Expectations About Retirement|How do work norms and household needs shape choices?|Compare policy, employer practice, finances, and preferences.
access_and_exclusion|An Older User at the Service Door|Which design, cost, language, or digital barriers matter?|Observe with consent and measure actual completion.
community_variation|No Single Older Generation|How do histories and resources differ among age peers?|Compare cohort within-group variation, place, and inequality.
policy_in_practice|An Age-Friendly Promise|Did one public plan change transport, housing, or care?|Check funding, implementation, usage, and lived experience.
survey_vs_story|A Longevity Trend and a Life|How should one personal story sit beside population data?|Explain denominator, variation, selection, and uncertainty.
power_and_voice|Who Designs Ageing Policy?|Are older adults involved in defining priorities and evaluating services?|Review consultation, representation, decision rights, and response.
unintended_consequence|When Digital Service Replaces a Counter|Did a change ease access for some and burden others?|Compare age, disability, digital access, costs, and alternatives.
comparative_setting|Ageing in Two Places|Why do similar-age populations have different opportunities?|Compare housing, care, transport, income, and policy.
change_over_time|Capacity Is Not a Fixed Age|How does one functional measure vary across people and time?|Use valid measures, context, adaptation, and limits.
ethical_dilemma|Filming Someone Receiving Care|How can autonomy and dignity be protected?|Check ongoing consent, privacy, dependency, and alternatives.
field_social_norms|Respect Across Ages|How do everyday expectations enable or restrict participation?|Use varied accounts and observed institutional practice.
field_relationship_network|Who Helps Whom?|How do support ties cross generations?|Map minimally with consent and protect nonparticipants.
field_group_identity|The Generational Label Test|Do people identify with a named generation?|Compare self-description, birth years, shared events, and internal difference.
field_community_support|A Place to Age Well|Which local resources do residents value most?|Use inclusive consultation, access mapping, and service data.
field_power_difference|Older Voice in a Care Setting|Can a participant decline filming when a caregiver or institution requests it?|Assess independent consent and meaningful alternatives.
"""


if __name__ == "__main__":
    revise_domain("174", "174_aging_generations", AGING,
                  "Ageing and generations through diverse lives, care, work, built environments, policy, access, and ageism.",
                  "age-disaggregated population and service data, longitudinal research, current policies, accessibility assessments, and independent voluntary accounts from older and younger people",
                  "Name age measure, cohort, place, and period. Avoid generational stereotypes and treating chronological age as ability; protect privacy and autonomy where care relationships affect consent.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
