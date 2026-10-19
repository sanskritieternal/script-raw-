"""Direct question-design review of motivational stories."""
from review_angle_plans import revise_domain, audit

MOTIVATION = """history_origins|How an Inspiring Story Began|What do the earliest records show about one person's challenge and goal?|Build a dated timeline from documents and consented testimony.
famous_examples|A Celebrated Achievement Checked|What did one widely shared success story actually involve?|Verify chronology, resources, collaborators, setbacks, and outcome.
hidden_stories|The Helpers Behind the Hero|Whose support and labor did a familiar narrative omit?|Use consented accounts and records rather than a lone-genius frame.
beginner_explainers|What a Story Can Teach|Which bounded decision or practice is documented in one account?|Explain context and avoid promising the same outcome to every viewer.
advanced_concepts|Selection and Survivorship Bias|How many similar attempts did a famous story leave unseen?|Compare available cases, base rates, resources, and missing data.
mysteries_unsolved_cases|An Unverified Turning Point|Which dramatic claim in one biography lacks contemporaneous support?|State source gaps and avoid filling them with invention.
technology_innovation|A Tool in a Personal Journey|Did one tool make a documented difference for a named person?|Compare use, access, alternatives, and the person's own account.
people_personalities|A Person Beyond One Trait|How do the subject's own words complicate a simplified success persona?|Use consented interviews and dated writings.
major_events|A Turning Point in Context|What changed after one dated event in a person's life?|Trace opportunities, decisions, support, and uncertainty.
how_it_works|From Goal to Measurable Outcome|What steps and resources can be documented in one journey?|Map timeline and constraints without turning it into a universal recipe.
rise_fall|A Setback and Recovery|What support and conditions shaped a documented recovery?|Avoid portraying hardship as desirable or guaranteed to build strength.
then_vs_now|A Person at Two Points in Time|How did goals, circumstances, and wellbeing change?|Compare dated self-reports and independent records with consent.
future_developments|The Next Step Is Uncertain|What options does a subject describe after a milestone?|Attribute current plans and avoid predicting success.
myths_vs_facts|A Viral Quote or Anecdote Checked|Did the person actually say or do what a motivational post claims?|Trace earliest source, wording, context, and corrections.
documentary_stories|One Life Through Its Records|What do documents and consented interviews reveal beyond the headline?|Show chronology, gaps, supporting people, and ethical limits.
claim_evidence|A Lesson Versus a Causal Claim|What does one story establish about a strategy's effectiveness?|Separate observed experience from evidence across people.
care_pathway|Support During a Hard Period|Which practical, social, or professional supports were available?|Describe documented services without diagnosing or advising viewers.
benefit_harm|Costs of an Achievement|Which sacrifices or unintended harms accompany a celebrated result?|Use the subject's account and independent records; avoid glorifying burnout.
mechanism_vs_outcome|Why Did a Change Help?|Can one claimed habit be separated from other changes in the person's life?|Map alternatives and limits of a single case.
population_difference|Who Could Follow This Path?|Which resources or constraints differ for other people?|Compare access, timing, health, family, and institutions without blame.
quality_of_guidance|Advice Drawn from a Biography|Is a public lesson supported beyond one person's account?|Check relevant evidence and state its applicability limits.
access_to_care|Unequal Access to Opportunity|Which supports made the subject's path possible but remain scarce?|Use documented costs, eligibility, mentors, and structural context.
patient_experience|The Subject's Own Experience|How does the person describe the journey in their own words?|Use informed consent and avoid turning distress into spectacle.
misinformation_path|A Story Made Too Neat|Which edits removed setbacks or helpers from a viral narrative?|Compare first-hand record with later retellings.
prevention_boundary|When Inspiration Is Not Support|Could a slogan obscure a need for practical or professional help?|Use current guidance and support context without personal advice.
system_pressure|Institutional Conditions Behind Success|How did school, workplace, family, or public systems shape the outcome?|Document support and barriers instead of attributing everything to willpower.
historical_revision|A Biography Reconsidered|What did new documents change about a familiar life story?|Compare original reporting, new evidence, and corrections.
field_measured_outcome|What Was Achieved?|Which outcome is verifiable and how was it measured?|Distinguish award, skill, income, wellbeing, and self-report.
field_practice_adherence|Was the Routine Consistent?|What records support a claimed daily habit?|Check diaries, logs, witnesses, and retrospective exaggeration.
field_individual_difference|The Person, Not a Template|Which conditions made this path distinctive?|Identify constraints and privileges without diminishing agency.
field_stress_context|Pressure Around a Decision|What did the subject know and face at one turning point?|Use contemporaneous evidence and avoid mind-reading.
field_claim_limits|What One Story Cannot Prove|Which universal lesson exceeds a single success or recovery?|State selection bias, missing comparison, and other pathways."""

if __name__ == "__main__":
    revise_domain("016", "016_motivational_stories", MOTIVATION,
                  "Documented personal journeys with consent, full context, supporting people, measurable outcomes, and limits to generalized lessons.",
                  "dated primary records, original interviews with informed consent, contemporaneous statements, outcome data, relevant research for generalized claims, and corrections",
                  "Verify chronology and quotations; protect privacy and dignity. Do not infer diagnosis, promise that adversity produces growth, glorify burnout, or universalize a single life story.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
