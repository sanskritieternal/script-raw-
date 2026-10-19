"""Editorial questions for social experiments as research and media."""

from review_angle_plans import audit, revise_domain


EXPERIMENTS = """history_origins|Why a Social Experiment Was Proposed|Which question and prior evidence motivated one study?|Trace protocol, population, review, and original aim.
famous_examples|A Famous Experiment Reexamined|What did its design actually establish and what was overstated?|Compare original data, ethics, later critique, and replication.
hidden_stories|Participants Behind a Headline|Whose experiences and objections were omitted from one report?|Use permitted records and voluntary retrospective accounts.
beginner_explainers|What Makes a Social Test an Experiment?|How do assignment, comparison, and outcome define one study?|Use a published case without proposing a live intervention.
advanced_concepts|Causal Claims and Their Limits|Which alternative explanations remain after one experiment?|Examine randomization, attrition, contamination, measurement, and scope.
mysteries_unsolved_cases|Why a Result Did Not Replicate|Which differences explain conflicting findings?|Compare populations, protocol, analysis, context, and chance.
technology_innovation|Online Experimentation Under Review|How did one platform experiment affect users and consent?|Read protocol, disclosure, data, governance, and outcomes.
people_personalities|The Research Team's Choices|How did investigators respond to unexpected participant effects?|Use dated protocol amendments, oversight, and debriefing records.
major_events|A Study That Changed Ethics Review|Which documented criticism led to altered standards?|Trace event, inquiry, response, and later practice.
how_it_works|From Protocol to Published Result|How is one study reviewed, run, analyzed, and reported?|Follow registration, consent, safeguards, outcome, and correction.
rise_fall|A Widely Taught Finding Reassessed|Why did confidence in one experiment change?|Compare original result, replication, methods, and interpretation.
then_vs_now|Historic Study, Current Standards|How would one past design be evaluated under current rules?|Compare actual historical oversight with current local requirements.
future_developments|A Better Way to Test the Question|Could existing data or a lower-risk design answer it?|Compare validity, privacy, burden, oversight, and alternatives.
myths_vs_facts|The Experiment Proved Human Nature?|Does one small study support a universal claim?|Check sampling, setting, effect size, replication, and cultural context.
documentary_stories|Following One Experiment's Afterlife|How did a study move from paper to textbook and media?|Trace citations, simplification, critique, and correction.
lived_experience|A Participant's Later Account|How does one person describe participation and impact?|Use voluntary consent and distinguish memory from full study outcome.
institutional_pathway|Who Approved the Study?|Which institutions reviewed risk, consent, and data use?|Trace documented decisions and applicable jurisdiction.
incentives_norms|Rewards Inside a Study|Could payment, grades, or authority have affected participation?|Examine recruitment, compensation, withdrawal, and power.
access_and_exclusion|Who Was Eligible to Participate?|Did selection limit the result or burden one group?|Review recruitment, language, accessibility, exclusion, and fairness.
community_variation|Effects Across Groups|Did one intervention affect participants differently?|Check pre-specified analysis, sample size, harm, and privacy.
policy_in_practice|From Experimental Effect to Policy|Was one result suitable for a wider rollout?|Compare external validity, cost, long-term effects, and consent.
survey_vs_story|A Mean Effect and Individual Outcomes|What does an average conceal about participants?|Show distribution, attrition, and voluntary accounts.
power_and_voice|Who Owns the Research Question?|Were affected people able to challenge the design or interpretation?|Examine consultation, oversight, publication, and remedy.
unintended_consequence|An Intervention's Hidden Burden|What harms appeared beyond the measured endpoint?|Review complaints, monitoring, dropout, and follow-up.
comparative_setting|Same Experiment, New Context|Did a finding transfer to another place or time?|Compare protocol, population, institutions, and effect uncertainty.
change_over_time|Did the Effect Last?|What happened after the experiment ended?|Use follow-up measurements, attrition analysis, and participant welfare.
ethical_dilemma|Deception for a Public Reaction Video|Can a staged test justify deceiving bystanders?|Examine consent, distress, privacy, review, and non-deceptive alternatives.
field_social_norms|A Norm Tested in a Study|Did the task represent ordinary social expectations?|Compare field context, participant interpretation, and controls.
field_relationship_network|Spillovers Beyond Participants|Were friends or coworkers affected without consent?|Map potential exposure minimally and review safeguards.
field_group_identity|Labels Created by the Study|Could treatment categories stigmatize a group?|Inspect wording, public release, participant review, and alternatives.
field_community_support|A Community-Led Evaluation|Can a group choose how an intervention is assessed?|Review governance, voluntary participation, outcomes, and benefits.
field_power_difference|Refusing the Researcher|Could participants decline or withdraw without losing services?|Examine recruitment, authority, compensation, and actual practice.
"""


if __name__ == "__main__":
    revise_domain("172", "172_social_experiments", EXPERIMENTS,
                  "Social experiments as documented research and media practices, assessed through design, consent, causal evidence, participant welfare, and public interpretation.",
                  "original protocols and registrations, ethics-review and consent records, deidentified outcome and attrition data, replications, complaints and corrections, and voluntary participant accounts",
                  "Name study, population, setting, jurisdiction, and date. Do not stage deceptive public tests for content; evaluate live research with qualified oversight, informed consent, privacy safeguards, and risk review.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
