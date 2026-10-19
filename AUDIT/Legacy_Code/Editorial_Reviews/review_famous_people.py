"""Editorial questions for famous people as a public-history niche."""

from review_angle_plans import audit, revise_domain


PEOPLE = """history_origins|How Someone Became Famous|Which event or institution first made one person widely known?|Trace dated coverage, audience reach, and prior work.
famous_examples|A Reputation Tested Against the Record|Which achievements of one public figure are independently documented?|Compare original work, contemporary response, and later summaries.
hidden_stories|The Team Behind a Public Figure|Whose labor is absent from one person's success story?|Trace collaborators, assistants, family labor, and credit with evidence.
beginner_explainers|A Public Figure's Source Trail|How can an audience check a claim about a famous person's life?|Start with dated original records and distinguish later retellings.
advanced_concepts|Fame, Merit, and Gatekeepers|How did institutions shape who gained recognition in one field?|Compare selection, funding, distribution, and excluded peers.
mysteries_unsolved_cases|An Uncertain Biographical Claim|Which parts of a repeated story remain unverified?|Trace first appearance, source quality, contradictions, and limits.
technology_innovation|A Medium That Changed Recognition|How did one communication technology alter a person's reach?|Compare audience data, distribution, control, and timing.
people_personalities|The Person Beyond a Single Trait|Which roles and relationships complicate one familiar portrait?|Use attributed records and avoid speculative psychology.
major_events|A Public Turning Point|What changed after one documented event in a person's career?|Compare work, access, coverage, and decisions before and after.
how_it_works|How a Public Image Is Built|Who produces and circulates one figure's public narrative?|Map interviews, agents, institutions, media, and paid promotion.
rise_fall|A Reputation Across Time|Why did public recognition grow or recede in one period?|Compare dated work, coverage, institutions, and audience response.
then_vs_now|How One Figure Has Been Remembered|What changed between contemporary judgment and later memory?|Compare period sources, commemorations, and new evidence.
future_developments|The Archive Yet to Be Opened|What questions could newly accessible records clarify?|Identify holdings, access dates, permissions, and plausible limits.
myths_vs_facts|A Famous Quote or Anecdote Checked|Can one widely repeated quote be traced to a reliable source?|Find earliest record, context, variant wording, and attribution gaps.
documentary_stories|A Day That Reveals a Career|What do records from one bounded day reveal about the person's work?|Use schedule, correspondence, collaborators, and contemporaneous context.
lived_experience|The Person's Own Account|How did one figure describe a formative experience?|Compare interview or memoir with dated records and later revisions.
institutional_pathway|Who Opened the Door?|Which schools, employers, sponsors, or organizations enabled a career?|Trace admissions, hiring, funding, and networks without assuming motive.
incentives_norms|A Public Position and Its Incentives|How did a role's rules and rewards shape choices?|Examine contracts, policies, money, peers, and actual decisions.
access_and_exclusion|A Peer Who Was Overlooked|Why did comparable contributors receive different recognition?|Compare work, gatekeeping, documentation, and context.
community_variation|Different Audiences, Different Figure|How do communities remember the same person differently?|Use attributed accounts and avoid treating any group as uniform.
policy_in_practice|A Famous Person and a Public Policy|What did the person's advocacy change in implementation?|Trace proposal, enacted text, funding, outcomes, and other actors.
survey_vs_story|Popularity by Measure and Memory|Do audience measures match vivid personal recollections?|Compare survey definitions, sampling, era, and individual accounts.
power_and_voice|Who Speaks for a Person After Death?|How do estates, archives, and publishers shape the public record?|Examine rights, access, edits, and competing views.
unintended_consequence|An Endorsement's Wider Effect|What consequences followed one public endorsement?|Compare reach, intended aim, observable response, and alternatives.
comparative_setting|Fame in Two Media Systems|How did a person's reputation travel across different places?|Compare distribution, language, institutions, and audience evidence.
change_over_time|An Evolving Public Position|Did one figure's stated views and actions change?|Use dated statements and decisions, preserving context.
ethical_dilemma|Privacy and Public Interest|Which personal detail is necessary to explain a public action?|Apply relevance, verification, consent where possible, and harm review.
field_source_verification|Checking a Viral Biography|Can a popular online life story be sourced claim by claim?|Record original documents, independent corroboration, and unresolved items.
field_story_framing|Choosing a Life's Central Question|Which narrative frame best reflects the evidence without distortion?|Test chronology, alternative viewpoints, omissions, and source strength.
field_audience_measurement|How Famous Was the Person?|What does one metric of reach actually represent?|Define period, medium, denominator, geography, and missing audiences.
field_platform_incentive|A Platform's Role in Fame|How did one platform's ranking or payment system affect exposure?|Use documented rules, dated reach, and creator incentives.
field_editorial_correction|Correcting a Public-Life Story|How should new evidence change one published biographical claim?|Log original wording, stronger evidence, correction, and remaining uncertainty.
"""


if __name__ == "__main__":
    revise_domain("146", "146_famous_people", PEOPLE,
                  "Public figures through verifiable work, collaborators, institutions, media systems, changing reputation, and public memory.",
                  "dated original work and records, archival correspondence and interviews, documented media reach, institutional and financial records, and consented accounts from collaborators",
                  "Name person, place, period, and claim. Separate public-interest facts from private life, avoid inferred motives or diagnoses, corroborate anecdotes, and document corrections.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
