"""Editorial questions for humanitarian stories."""

from review_angle_plans import audit, revise_domain


HUMANITARIAN = """history_origins|How a Local Response Began|Which community actions preceded formal assistance in one crisis?|Use dated local records and consented accounts before agency narratives.
famous_examples|A Widely Praised Relief Operation|Which outcomes and gaps can be documented for one response?|Compare needs, delivery, independent evaluation, and community feedback.
hidden_stories|The Labor That Makes Aid Possible|Whose logistics, translation, care, and local knowledge are overlooked?|Follow paid and unpaid roles with consent and fair attribution.
beginner_explainers|From Need to Assistance|How does one program identify needs and decide eligibility?|Map criteria, access, appeals, data use, and community input.
advanced_concepts|Measuring Help Without Oversimplifying|How can a response's reach be separated from actual benefit?|Compare output, outcome, timing, quality, and excluded groups.
mysteries_unsolved_cases|Why Aid Did Not Arrive|Which documented barriers explain a delivery gap in one place?|Check access, security, funding, procurement, and conflicting accounts.
technology_innovation|A Digital Aid Tool in Practice|Did one registration or payment tool improve access?|Compare consent, errors, exclusion, privacy, costs, and remedies.
people_personalities|A Community Organizer's Choices|How did one local leader coordinate help under constraints?|Use consented testimony, contemporaneous records, and other perspectives.
major_events|A Turning Point in a Response|What changed after one documented crisis escalation?|Compare needs, decisions, resources, access, and outcomes by date.
how_it_works|Following One Aid Delivery|How did assistance travel from funding to recipient?|Trace procurement, logistics, local partners, distribution, and feedback.
rise_fall|When a Program Closed|Why did one service end, and what happened to users?|Check funding, handover, local capacity, need, and follow-up evidence.
then_vs_now|A Community Before and After Assistance|What changed, and what other forces contributed?|Use comparable measures and avoid attributing every change to aid.
future_developments|A Recovery Plan Under Review|Does one proposed plan match community priorities and capacity?|Compare consultation, budget, maintenance, risks, and alternatives.
myths_vs_facts|A Viral Crisis Story Verified|Which details of one widely shared claim can be confirmed safely?|Check source, date, place, context, identity risk, and correction path.
documentary_stories|A Day in Community-Led Response|What does one local team's routine reveal about needs and agency?|Film with informed consent, safety review, and participant control.
lived_experience|A Person's Account of Assistance|How does one participant describe what helped and what did not?|Use voluntary interview, chosen anonymity, and no aid-linked pressure.
institutional_pathway|Who Decides the Response?|How do donors, agencies, governments, and communities share authority?|Trace agreements, budgets, local participation, and appeals.
incentives_norms|Funding Rules and Field Choices|How did one grant's requirements shape what a program delivered?|Read targets, reporting, restrictions, adaptations, and outcomes.
access_and_exclusion|Who Could Not Reach the Service?|Which barriers kept an eligible group from help?|Examine language, disability, documents, geography, safety, and feedback.
community_variation|Needs Within One Community|How do priorities differ among groups affected by the same crisis?|Use safe, voluntary consultation without flattening internal differences.
policy_in_practice|A Protection Policy on the Ground|Did a stated safeguard work in one response?|Compare written rule, training, complaints, remedy, and participant views.
survey_vs_story|Numbers and Testimony Together|Do program statistics match the experiences of intended recipients?|Check sampling, definitions, missing groups, and consented stories.
power_and_voice|Who Can Refuse the Camera?|Can someone decline an interview without affecting assistance?|Inspect consent process, staff separation, timing, and alternatives.
unintended_consequence|When Help Creates a New Burden|Did one intervention create costs, conflict, or dependency?|Compare intended benefit, reported effects, and other explanations.
comparative_setting|Two Responses to Similar Needs|Why did two communities receive different forms of support?|Compare context, access, resources, local priorities, and measurement.
change_over_time|From Emergency to Recovery|How did needs and support change after immediate danger passed?|Use dated assessments, services, livelihoods, and participant priorities.
ethical_dilemma|Publishing a Crisis Survivor's Story|Is the public value of identification worth the possible risk?|Assess informed consent, dignity, future exposure, and safer alternatives.
field_social_norms|How Help Is Shared Locally|Which local practices shape distribution and mutual support?|Ask community members, check variation, and avoid prescriptive judgment.
field_relationship_network|The Network Behind Assistance|Which trusted links connect a person to support?|Map only with permission and protect identities and sensitive routes.
field_group_identity|Labels Applied to People in Crisis|Do agency categories reflect how people identify themselves?|Compare administrative labels, self-description, eligibility, and harm.
field_community_support|Mutual Aid Before Outside Aid|What resources did neighbors organize themselves?|Document chronology, capacity, constraints, and credit local actors.
field_power_difference|An Interview Across a Power Gap|How can a production reduce pressure on someone receiving aid?|Separate services from filming, use ongoing consent, privacy, and review.
"""


if __name__ == "__main__":
    revise_domain("148", "148_humanitarian_stories", HUMANITARIAN,
                  "Humanitarian response through community agency, access, delivery, accountability, measurable outcomes, and ethical representation.",
                  "dated needs and program records, independent evaluations, disaggregated outcome data, current standards and access rules, and voluntary consented accounts from affected people and local responders",
                  "Name crisis, place, program, and date. Never condition help on filming, protect identity and location where needed, assess downstream harm, seek ongoing informed consent, and distinguish delivery counts from benefit.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
