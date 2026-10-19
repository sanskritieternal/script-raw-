"""Editorial questions for the broad global cultures niche."""

from review_angle_plans import audit, revise_domain


CULTURES = """history_origins|A Practice in Its Own History|How do practitioners trace one named practice in one place?|Compare community accounts with dated records without inventing a single origin.
famous_examples|A Festival Beyond the Travel Image|What does one public celebration mean to those who organize it?|Follow consented organizers, preparation, costs, and different interpretations.
hidden_stories|The Work Behind a Cultural Event|Whose unpaid or low-paid labor sustains one practice?|Trace preparation, care, teaching, financing, and credit.
beginner_explainers|How to Describe a Culture Responsibly|What place, group, and period does one claim actually cover?|Use community-preferred terms and name variation and uncertainty.
advanced_concepts|Tradition and Change Together|How do practitioners choose which parts of a practice to adapt?|Examine generational debate, access, resources, and community authority.
mysteries_unsolved_cases|A Disputed Origin Story|Which parts of one cultural origin account can be documented?|Compare oral traditions, material evidence, written sources, and distinct purposes.
technology_innovation|A Digital Platform for a Living Practice|How did one community use media to teach or share a practice?|Check control, access, reach, unintended exposure, and consent.
people_personalities|A Practitioner in Context|How does one person's work relate to a wider practice?|Use consented narrative without treating one individual as representative.
major_events|A Rule That Changed a Practice|How did one policy or displacement alter cultural activity?|Trace dated decisions and different community responses.
how_it_works|How Knowledge Is Passed On|Who teaches one practice and what does learning involve?|Follow permitted instruction, relationships, time, and limits on disclosure.
rise_fall|Participation Through Time|Has one practice declined, transformed, or moved elsewhere?|Compare practitioner accounts, participation measures, and changing forms.
then_vs_now|One Practice Across Generations|Which elements changed and which still matter to participants?|Use dated evidence and multiple consented voices.
future_developments|A Community-Led Continuity Plan|Does one proposal support practitioners' own priorities?|Check decision rights, funding, teaching, access, and tradeoffs.
myths_vs_facts|A Cultural Stereotype Tested|Does a broad claim about one group fit documented variation?|Name claim, population, place, source, and counterexamples.
documentary_stories|A Year Around One Practice|How does its preparation and meaning change across a cycle?|Follow consenting participants and protect restricted moments.
lived_experience|What Participation Means to One Person|How does a participant describe their relationship to a practice?|Use their own terms and avoid extrapolating to the whole community.
institutional_pathway|From Local Practice to Official Listing|What changed when one institution recognized a tradition?|Compare nomination, consent, funding, tourism, and community control.
incentives_norms|Selling a Cultural Experience|How do tourism and markets shape one practice?|Trace prices, labor, benefits, adaptations, and practitioner views.
access_and_exclusion|Who Can Participate?|Which rules, costs, language, or location limit entry to one practice?|Compare stated norms with varied lived experiences.
community_variation|Different Views Within a Community|Which disagreements over one practice matter to its future?|Represent attributed viewpoints without declaring one voice universal.
policy_in_practice|A Cultural Protection Rule|Did one policy deliver what practitioners sought?|Compare legal text, implementation, resources, and actual access.
survey_vs_story|A Population Claim and Personal Accounts|Do available data support a popular description of one community?|Check definitions, sampling, dates, and lived variation.
power_and_voice|Who Gets to Tell the Story?|Who controls filming, translation, publication, and revenue?|Agree on consent, attribution, review, rights, and benefits.
unintended_consequence|When Recognition Changes a Practice|Did visibility bring burdens as well as benefits?|Compare attention, income, access, privacy, and local preferences.
comparative_setting|A Practice Across Two Places|How has one named practice adapted in different settings?|Compare local histories without ranking either as more authentic.
change_over_time|Cultural Change Without a Loss Story|What evidence shows continuity through adaptation?|Use dated objects, oral history, migration, and current choices.
ethical_dilemma|Should This Ceremony Be Filmed?|What do participants and custodians permit an outsider to show?|Apply free informed consent, restrictions, and safer alternatives.
field_social_norms|How a Local Rule Is Learned|How do participants explain expectations around one event?|Seek multiple viewpoints and distinguish norm from actual practice.
field_relationship_network|The People Who Sustain a Practice|Which relationships connect teachers, makers, and participants?|Map only with permission and avoid exposing private ties.
field_group_identity|A Name Applied from Outside|Does one broad label fit how people identify themselves?|Compare local terms, history, context, and self-description.
field_community_support|Maintaining Space for a Practice|What resources help one community continue an activity?|Examine venues, time, materials, funding, and control.
field_power_difference|An Outsider Recording a Tradition|How can a production reduce unequal power in the encounter?|Negotiate scope, compensation, ongoing consent, review, and withdrawal terms.
"""


if __name__ == "__main__":
    revise_domain("149", "149_global_cultures", CULTURES,
                  "Specific living cultural practices in named communities through meaning, transmission, variation, institutions, and control over representation.",
                  "consented practitioner accounts and community records, dated objects and policy documents, appropriately contextualized surveys, and documentation chosen by community participants",
                  "Never generalize from one person to an entire culture. Name group, place, practice, and period; use preferred terms, secure free prior informed ongoing consent, and honor restricted knowledge and community review.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
