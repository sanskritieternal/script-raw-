"""Direct editorial review of consciousness and spirituality questions."""
from review_angle_plans import revise_domain, audit

CONSCIOUSNESS = """history_origins|A Theory of Consciousness in Its Sources|When did one named philosophical or spiritual account appear?|Trace original text, later interpretation, and uncertain dating.
famous_examples|A Famous Consciousness Argument|What does one widely cited thought experiment or passage establish?|Reconstruct premises and objections without treating illustration as evidence.
hidden_stories|Voices Missing from the Debate|Whose lived or intellectual account is absent from one standard theory history?|Use attributed texts and consented voices without treating one experience as universal.
beginner_explainers|What Does Consciousness Mean Here?|How do awareness, reportability, selfhood, and spiritual experience differ?|Define the exact term before comparing theories or studies.
advanced_concepts|Neural Correlate and Explanation|What can a measured brain correlate establish about subjective experience?|Separate association, causal inference, and philosophical interpretation.
mysteries_unsolved_cases|An Open Question About Experience|Which aspect of one consciousness theory remains untested or disputed?|State proposed test, available evidence, and conceptual limits.
technology_innovation|A New Measure of Awareness|What does one brain-imaging or behavioral method actually detect?|Check validation, population, false results, and clinical limits.
people_personalities|A Thinker's Definition of Mind|How did one named thinker define consciousness or self?|Read primary writing and distinguish later summaries.
major_events|A Study Changes a Debate|Which claim did one dated experiment support or challenge?|Compare preregistered question, method, results, replication, and interpretation.
how_it_works|From Experience to Research Question|How can a first-person report become a measurable study question?|Specify operational measure, consent, comparison, and limits.
rise_fall|A Theory's Changing Reception|Why did one account gain or lose support?|Trace arguments, experiments, critique, and methodological shifts.
then_vs_now|A Traditional Idea in Current Discussion|How is one older account used in present philosophy or spirituality?|Separate original setting, translation, and current reinterpretation.
future_developments|A Test Between Theories|What observation could distinguish two current scientific proposals?|State predicted signal, population, and remaining ambiguity.
myths_vs_facts|A Brain Scan Proves a Metaphysics?|Does one popular claim go beyond what an imaging result measured?|Compare study design with philosophical conclusion.
documentary_stories|One Consciousness Claim's Evidence Trail|How did a claim move from source text or experiment into public discussion?|Track original, commentary, media version, and corrections.
text_source|A Passage About Self or Awareness|What does a named spiritual or philosophical text actually say?|Cite edition, translation, context, and interpreter.
interpretive_lineages|Two Accounts of the Self|How do named traditions differ on one precise claim?|Represent each in its own terms rather than merging vocabulary.
lived_practice|A Person's Spiritual Experience|What does one consented account reveal about meaning and context?|Treat it as testimony, not proof of a universal mechanism or diagnosis.
ritual_sequence|Experience Within an Observance|How do participants place a named experience within one rite?|Describe local public context with permission, not instructions.
language_translation|A Word for Consciousness|How do different renderings of one term change an apparent claim?|Compare original language, grammar, and commentaries.
regional_variants|An Idea in Two Communities|How do two settings teach or interpret a shared term?|Specify time, lineage, language, and practice.
art_and_devotion|An Image of Inner Experience|How does one artwork express awareness or selfhood?|Attribute artistic and devotional meaning without treating image as measurement.
community_memory|Remembering an Experience or Teacher|How does community memory shape an account of consciousness?|Compare attributed narrative with dated records.
ethics_in_context|Vulnerable People in Consciousness Research|How should one study address consent and uncertain interpretation?|Read ethics protocol and avoid individual prognosis or care advice.
source_and_history|A Theory's Transmission|What sources show one idea passing between traditions or disciplines?|Trace citations and translations, not resemblance alone.
encounter_and_exchange|Science and Spirituality in Dialogue|What did two named participants actually agree or dispute?|Compare their own statements and distinct evidence standards.
contemporary_voice|Two Present Interpretations|How do a practitioner and researcher describe the same experience differently?|Attribute standpoints and state what each can establish.
field_concept_definition|One Term, Several Meanings|Which definition of consciousness is needed for a bounded question?|Specify operational and philosophical meanings before evaluating evidence.
field_argument_structure|A Theory's Premises|Does one conclusion follow from its stated premises?|Map argument and strongest documented objection.
field_lived_interpretation|Meaning of an Experience|How does one community interpret a consented account?|Respect the person and avoid clinical inference from testimony.
field_translation_problem|A Contested Term for Self|What does the original-language context permit?|Compare editions, grammar, and named commentaries.
field_practice_and_claim|A Practice and a Claimed Effect|What does evidence establish about an exact practice and outcome?|Separate spiritual aim, self-report, measured result, harms, and study limits."""

if __name__ == "__main__":
    revise_domain("292", "292_consciousness_spirituality", CONSCIOUSNESS,
                  "Precise definitions of consciousness and selfhood, named spiritual interpretations, first-person experience, neuroscience evidence, and ethical limits.",
                  "specified primary philosophical and spiritual texts, translations and commentaries, registered empirical studies and replications, measurement protocols, ethics records, and consented accounts",
                  "Define the exact concept and claim; attribute spiritual and philosophical positions. Do not treat a subjective account as clinical proof or a neural correlate as proof of metaphysics; give no diagnosis or personal care advice.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
