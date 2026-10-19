"""Editorial questions for disability history."""

from review_angle_plans import audit, revise_domain


DISABILITY = """history_origins|How an Access Barrier Was Built|When did one institution adopt a design or rule that excluded people?|Trace plans, policy, use, and disabled people's responses.
famous_examples|A Disability Rights Campaign Revisited|What did one campaign change in law and daily access?|Compare organizers' demands, enacted rule, enforcement, and outcomes.
hidden_stories|Disabled People Behind an Innovation|Whose design, testing, and organizing work was credited to others?|Trace original artifacts, correspondence, and public recognition.
beginner_explainers|Disability in Historical Sources|How did past institutions classify impairment and access?|Read period labels critically with self-description and context.
advanced_concepts|Rights on Paper, Access in Practice|Did one legal change remove barriers for varied disabled people?|Compare buildings, services, employment, enforcement, and variation.
mysteries_unsolved_cases|A Missing Advocate's Name|Which records can identify a disabled contributor?|Compare meeting notes, photos, oral histories, and uncertainty.
technology_innovation|Assistive Technology in Context|Who shaped one tool and did it improve user-defined tasks?|Trace design, cost, repair, access, and user accounts.
people_personalities|An Activist Beyond Inspiration|What work, conflict, and alliances shaped one person's campaign?|Use original statements, collaborators, institutional records, and critique.
major_events|An Occupation or Protest for Access|What happened and which demands were met?|Trace participant accounts, media, negotiation, law, and aftermath.
how_it_works|Making an Institution Accessible|How did one group move from complaint to actual change?|Follow organizing, decision authority, funding, implementation, and use.
rise_fall|A Disability Organization's Changing Role|Why did one group grow, split, or close?|Check membership, governance, funding, policy, and internal debate.
then_vs_now|The Same Journey Across Generations|How did one route's accessibility change?|Compare transport, physical barriers, information, price, and user accounts.
future_developments|An Archive Led by Disabled People|Which missing histories should a collection prioritize?|Check access formats, consent, community governance, and resources.
myths_vs_facts|A Single Hero Made Access Happen?|Does one-person storytelling omit collective action?|Trace collaborators, institutions, opposition, and long implementation.
documentary_stories|A Place Through Disability History|What does one building reveal about changing access and activism?|Compare plans, renovations, protests, and current users.
source_trail|Where an Access Claim Came From|Which document supports a repeated rights-history claim?|Trace original text, date, jurisdiction, and later simplification.
material_evidence|An Assistive Object's Provenance|What can one device show about design and daily use?|Check maker, modifications, repairs, ownership, and user context.
chronology_dispute|When Was Access Won?|Which date marks a demand, law, retrofit, or usable service?|Separate stages and people who remained excluded.
ordinary_lives|Work and Care Beyond Institutions|What records show a disabled person's ordinary routines?|Use consented family, work, community, and object histories.
power_and_institutions|Who Decided What Was Normal?|How did medicine, schools, employers, and states define disability?|Compare official categories with disabled people's accounts.
trade_and_exchange|The Cost of Participation|What expenses did disabled people face for work, travel, or communication?|Trace wages, devices, support, benefit rules, and access.
language_and_labels|Words for Disability Over Time|How did official terms differ from people's preferred language?|Quote only with historical context and current participant preference.
maps_and_borders|The Geography of Accessibility|Where were services and routes available or absent?|Map facilities, travel time, rights, and local decisions.
conflicting_accounts|A Movement's Internal Debate|How did disabled advocates differ on strategy or priorities?|Use attributed voices and avoid one universal disability view.
preservation_bias|Institutions Hold the Files|How do medical and charity records dominate the archive?|Seek self-authored media, protest records, art, and oral history.
turning_point_test|Did a Law Change Daily Life?|Which outcomes improved after one rights reform?|Compare implementation, enforcement, varied groups, and time.
legacy_and_memory|How Access Wins Are Remembered|Who is named in monuments and exhibits?|Compare participant records, public commemoration, and omissions.
field_oral_history|Interviewing Disability Advocates|How can access and control be built into an interview?|Offer preferred formats, consent, review, breaks, and communication support.
field_archive_gap|Finding Self-Authored Sources|What evidence exists outside official case files?|Search community publications, personal collections, and digital archives.
field_material_culture|An Adapted Everyday Object|What does a modification reveal about skill and unmet design need?|Check maker, use, repair, and original environment.
field_community_memory|A Local Access Campaign|How do participants and later users remember its effects?|Use varied accessible interviews and document disagreement.
field_representation_ethics|Beyond Tragedy and Inspiration|How can a film center disabled people's agency and material barriers?|Review framing, access, consent, language, and participant feedback.
"""


if __name__ == "__main__":
    revise_domain("179", "179_disability_history", DISABILITY,
                  "Disability history through disabled people's agency, access, law, built environments, objects, institutions, and collective action.",
                  "self-authored disability movement records, dated policy and implementation files, building and transport plans, object provenance, and accessible consented oral histories",
                  "Name place, period, institution, and group. Use participant-preferred language, avoid tragedy or inspiration framing, distinguish legal rights from practical access, and provide accessible participation and review.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
