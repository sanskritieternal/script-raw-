"""Editorial questions for community stories."""

from review_angle_plans import audit, revise_domain


COMMUNITY = """history_origins|How a Community Space Began|Who created one shared place or organization and why?|Trace dated records, land, funding, and varied memories.
famous_examples|A Celebrated Local Initiative|What did one community project achieve and for whom?|Compare goals, participation, outcomes, and excluded voices.
hidden_stories|The Work That Holds a Community Together|Whose care, translation, organizing, and maintenance goes unseen?|Follow consented contributors and recognize unequal burdens.
beginner_explainers|What Makes This a Community?|How do people define belonging in one specific setting?|Compare self-description, institution, geography, and variation.
advanced_concepts|Shared Identity and Internal Difference|How can a collective story include disagreement?|Map positions, power, history, and areas of common action.
mysteries_unsolved_cases|A Disputed Local Memory|Why do accounts of one event differ?|Compare archives, oral histories, dates, vantage points, and gaps.
technology_innovation|A Digital Tool for Local Organizing|Did one platform help members communicate or participate?|Check access, moderation, privacy, workload, and actual use.
people_personalities|An Organizer Among Many|How did one person's role fit a wider network?|Trace collaborators, succession, conflict, and consented testimony.
major_events|A Change That Brought People Together|How did one event alter local relationships?|Compare before and after organizations, services, trust, and disagreement.
how_it_works|Making a Collective Decision|Who can propose, vote, object, and implement in one group?|Use current rules and observe practice with permission.
rise_fall|A Community Institution's Changing Reach|Why did one center or association grow, shrink, or close?|Check funding, demographics, access, leadership, and needs.
then_vs_now|One Neighborhood Across Generations|What changed for residents with different tenures?|Compare maps, housing, services, prices, and varied accounts.
future_developments|A Community's Proposed Plan|Does one plan reflect members' priorities and resources?|Review participation, budget, authority, accessibility, and follow-up.
myths_vs_facts|A Story Everyone Knows?|Does a common local origin story match records and varied memories?|Trace first telling, evidence, and competing accounts.
documentary_stories|A Week of Collective Work|What routine labor supports one community activity?|Follow consenting participants and avoid filming private moments.
lived_experience|Belonging and Its Limits|How does one person describe entry, support, or exclusion?|Use their terms without generalizing to all members.
institutional_pathway|Local Group Meets Public Agency|How does one community request become a funded service?|Trace meetings, applications, decisions, delivery, and appeals.
incentives_norms|Why People Volunteer|Which rewards, obligations, and constraints shape participation?|Compare roles, time, recognition, expenses, and burnout.
access_and_exclusion|Who Cannot Join Easily?|Which language, location, disability, cost, or status barriers matter?|Check formal rules and lived practice across groups.
community_variation|Different Views of One Project|How do members disagree about priorities?|Represent attributed positions and avoid a false consensus.
policy_in_practice|A Promise Made to Residents|Did one policy change the service residents receive?|Compare text, budget, rollout, complaints, and outcomes.
survey_vs_story|A Local Poll and Personal Accounts|Do measured opinions match compelling anecdotes?|Check sampling, nonresponse, wording, and who was reached.
power_and_voice|Who Gets the Microphone?|Who chooses spokespeople and controls publication?|Examine hierarchy, consent, editorial review, and benefit.
unintended_consequence|When a Helpful Project Excludes|Did one initiative raise costs or displace a need?|Compare intended benefit, uneven effects, and alternatives.
comparative_setting|Two Neighborhood Responses|Why did similar groups organize differently?|Compare resources, institutions, history, demography, and timing.
change_over_time|A Community Beyond One Crisis|How did mutual support persist or change afterward?|Track organizations, relationships, resources, and member views.
ethical_dilemma|Publishing a Neighbor's Story|Could identification damage relationships or safety?|Review informed consent, third-party privacy, context, and options.
field_social_norms|An Unwritten Local Rule|How do members learn and contest one norm?|Use varied interviews and observation with permission.
field_relationship_network|A Network of Mutual Aid|Which ties carry help when formal services fail?|Map minimally with consent and avoid revealing sensitive connections.
field_group_identity|Who Uses the Community Name?|How do boundaries and labels differ across members?|Use self-identification, history, and context, never imposed unanimity.
field_community_support|A Shared Resource in Practice|Who contributes to and uses one community resource?|Trace operation, access, funding, accountability, and strain.
field_power_difference|Filming in a Small Community|How can producers reduce pressure and future harm?|Negotiate scope, compensation, review, withdrawal, and long-term access.
"""


if __name__ == "__main__":
    revise_domain("169", "169_community_stories", COMMUNITY,
                  "Specific community stories through collective work, belonging, disagreement, institutions, mutual support, and local change.",
                  "community-held archives and meeting records, public budgets and service data, appropriately sampled surveys, and voluntary consented accounts from varied members",
                  "Name community, place, organization, and period. Do not present one spokesperson as consensus; protect small-group and third-party privacy, establish ongoing consent, and return context and review opportunities to participants.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
