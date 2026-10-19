"""Editorial question designs for knowledge and quiz formats."""

from review_angle_plans import audit, revise_domain


KNOWLEDGE = """history_origins|How a Fact Entered Common Knowledge|When and through which sources did one claim become widely taught?|Trace dated publications and corrections.
famous_examples|One Familiar Fact Rechecked|What does its best primary source actually establish?|Define place, date, and wording.
hidden_stories|Knowledge beyond the Canon|Whose evidence was left out of a standard overview?|Compare source selection and contributors.
beginner_explainers|From Question to Reliable Answer|Which source and definition must a learner check first?|Work through one bounded example.
advanced_concepts|Facts with Conditions|How does a true statement change with scale or definition?|Compare two valid frames and limits.
mysteries_unsolved_cases|A Question without a Settled Answer|What is known, disputed, or unmeasured?|Show evidence gaps rather than force certainty.
technology_innovation|A Tool for Finding Answers|Does a search or reference tool help verify one claim?|Compare source traceability and error rate.
people_personalities|Who Defined the Standard Answer?|Which people and institutions selected a familiar formulation?|Use curriculum and reference history.
major_events|A Fact Gets Revised|Which new evidence changed a textbook answer?|Trace dated editions and studies.
how_it_works|Checking a General-Knowledge Claim|How do definition, source, date, and counterexample affect confidence?|Demonstrate a transparent verification path.
rise_fall|A Once-Common Answer Fades|Why was a popular answer dropped?|Compare original evidence and later correction.
then_vs_now|The Same Question across Time|How did a time-sensitive answer change?|Include both as-of dates and scope.
future_developments|Questions Likely to Change|Which facts need a dated update before reuse?|Identify changing institutions or measurements.
myths_vs_facts|A Plausible False Fact|Which part of a familiar claim fails?|Compare exact wording with primary evidence.
documentary_stories|One Answer's Source Trail|How did a claim travel from record to classroom and media?|Follow citation chain and revisions.
concept_sequence|Build a Knowledge Map|Which prerequisite ideas make a broad topic understandable?|Sequence three claims with explicit links.
misconception|An Overgeneralized Rule|What example reveals a common learner misunderstanding?|Use pre-response and counterexample.
worked_example|Verify a Number|How can a learner reproduce one published statistic?|Show denominator, unit, year, and source.
retrieval_practice|Recall with Context|Does revisiting a fact after delay improve accurate recall?|Use equivalent items and feedback.
feedback_design|Explain an Incorrect Answer|Which explanation identifies the mistaken assumption?|Compare feedback quality, not just score.
assessment_quality|Does a Question Test Understanding?|Can guessing or wording cues produce the right answer?|Audit distractors and learner responses.
visual_explanation|A Diagram with Evidence|Does a chart make relationships clearer without hiding scale?|Show labels, source, and uncertainty.
transfer_to_new_case|Apply the Rule Elsewhere|Can a learner use a concept in an unfamiliar example?|Test transfer separately from recall.
language_access|Translate without Changing the Claim|Which term shifts meaning across languages?|Use expert review and learner feedback.
learner_variation|Different Starting Knowledge|What prior knowledge changes difficulty?|Compare groups without assuming fixed ability.
source_literacy|Primary versus Repeated Claim|Can learners trace a statement to evidence?|Compare original record and secondary repetition.
curriculum_tradeoff|Breadth and Depth|What is lost when a lesson covers many facts quickly?|Compare recall and explanation outcomes.
field_learner_misconceptions|Listen before Explaining|Which wrong answer reveals a coherent model?|Collect anonymous response and reasoning.
field_lesson_sequence|Order the Concepts|Which sequence reduces prerequisite confusion?|Test short lessons with comparable learners.
field_assessment_design|Write a Fair Question|Does the item have a defined, current, sourced answer?|Pilot and revise ambiguity.
field_memory_and_recall|Retest after Delay|What remains after initial success?|Use delayed equivalent items and correction.
field_inclusive_learning|Multiple Ways to Respond|Can different learners access the same concept?|Check language, audio, visual, and timing options.
"""

TRIVIA = """history_origins|A Trivia Item's History|Where did one famous question first appear?|Trace original wording and answer changes.
famous_examples|A Classic Question Audited|Is its familiar answer uniquely defensible?|Define period, region, and category.
hidden_stories|Whose Knowledge Is Called Trivial?|Which traditions or communities are missing from common trivia sets?|Audit source and topic distribution.
beginner_explainers|Building a Fair Trivia Question|What makes a prompt answerable from a reliable source?|Show scope, clue, and verification.
advanced_concepts|Ambiguity in a Superlative|How do measurement and category change the answer?|Test largest, first, or oldest claims carefully.
mysteries_unsolved_cases|A Disputed Answer|Which evidence prevents a single authoritative answer?|Mark alternate responses and uncertainty.
technology_innovation|Trivia Fact-Checking Workflow|Can a tool catch stale or ambiguous items?|Compare flagged cases with manual review.
people_personalities|Who Wrote the Answer Key?|How did a quiz writer choose and justify an answer?|Use drafts and correction history.
major_events|A Trivia Correction|What triggered correction of a published item?|Trace original prompt, challenge, and revised key.
how_it_works|Question to Answer Key|How are prompt, accepted variants, source, and explanation linked?|Follow one editorial workflow.
rise_fall|A Stale Trivia Fact|When did an answer stop being true?|Document dated status and update rule.
then_vs_now|Same Question, New Answer|Which event changed a time-sensitive response?|Include precise as-of dates.
future_developments|A Future-Proof Quiz Item|Which wording avoids predictable staleness?|Fix a historical date or require update review.
myths_vs_facts|A Viral Trivia Claim|Can the popular answer survive source checking?|Trace citation chain and exact claim.
documentary_stories|An Answer Key's Paper Trail|How did one disputed answer spread and get amended?|Use dated editions and corrections.
concept_sequence|From Clue to Context|Can linked trivia items build an accurate idea?|Sequence facts and explain relationship.
misconception|A Distractor with a Reason|Which plausible wrong choice reveals confusion?|Test learner explanations.
worked_example|Repair an Ambiguous Prompt|How can one question be rewritten to have a defensible key?|Show source and accepted variants.
retrieval_practice|Trivia as Recall Practice|Does repeat play aid later recall with correction?|Compare delayed retrieval and exposure.
feedback_design|Beyond Correct or Wrong|What brief feedback makes the underlying fact memorable?|Include reason and source.
assessment_quality|Answer-Key Robustness|Will independent reviewers agree on accepted responses?|Measure disagreement and revise.
visual_explanation|Image-Based Trivia|Can the question be answered without hidden visual cues?|Provide equivalent text and attribution.
transfer_to_new_case|Use a Trivia Fact|Can players apply the fact to a different case?|Ask a follow-up inference question.
language_access|Trivia across Languages|Does translation preserve the clue and answer space?|Check names, puns, and transliteration.
learner_variation|Different Knowledge Backgrounds|Who is advantaged by a particular item set?|Audit topic and cultural exposure.
source_literacy|Show the Evidence|Can players inspect the answer's original source?|Provide a dated citation and limits.
curriculum_tradeoff|Fun versus Accuracy|When does speed encourage misleading simplification?|Compare player experience and correction rate.
field_learner_misconceptions|Why Players Chose That Answer|What reasoning lies behind a common distractor?|Collect explanations without embarrassment.
field_lesson_sequence|Round Design|Does ordering clues help learning or just alter scores?|Test difficulty and context transitions.
field_assessment_design|Pilot the Item|Do players interpret it as intended?|Record alternate answers and ambiguity.
field_memory_and_recall|Return to a Corrected Fact|Do players retain the correction later?|Use delayed item with changed wording.
field_inclusive_learning|Accessible Trivia Play|Can players use caption, transcript, and flexible timing?|Check equivalent information across formats.
"""

QUIZ = """history_origins|A Quiz Format Develops|Which broadcast or web choices shaped a named quiz channel?|Trace dated episodes and platform features.
famous_examples|A Popular Quiz Episode Audited|Are its questions, answers, and sources defensible?|Sample items and corrections.
hidden_stories|Work behind a Quiz Channel|Who researches, writes, edits, voices, and moderates?|Use credits and workflow evidence.
beginner_explainers|How a Quiz Episode Works|How do prompt, pause, reveal, and explanation guide play?|Analyze one episode timeline.
advanced_concepts|Learning versus Engagement|Does higher watch time mean better understanding?|Compare independent learning measures.
mysteries_unsolved_cases|A Score Spike|Is a score change due to learning, easier items, or selection?|Audit item difficulty and audience data.
technology_innovation|Interactive Quiz Feature|Did a new interaction improve access or learning?|Compare usage, errors, and feedback.
people_personalities|A Quiz Creator's Editorial Choice|Who sets topic and answer standards?|Read creator policies and revisions.
major_events|A Channel Changes Format|What changed in participation and learning after a redesign?|Compare dated episodes and responses.
how_it_works|Episode from Research to Upload|How are sources, accepted answers, timing, and captions checked?|Map production workflow.
rise_fall|A Quiz Series Loses Trust|Which documented answer or moderation failures mattered?|Trace corrections and audience response.
then_vs_now|Early and Recent Episodes|How did sourcing, accessibility, and difficulty change?|Use same rubric and sample size.
future_developments|A Proposed Quiz Feature|What evidence would justify personalization or automation?|Test accuracy, access, and privacy.
myths_vs_facts|A High Score Means Mastery?|Can repeat viewers answer new questions on the topic?|Separate memorized items from transfer.
documentary_stories|One Episode's Correction|How was a disputed answer reviewed and updated?|Trace source, edit, and viewer notice.
concept_sequence|A Learning-Oriented Quiz Series|Which sequence lets later questions build on earlier ideas?|Map prerequisites and test comprehension.
misconception|Wrong Answer as Evidence|Which recurring choice reveals a misunderstanding?|Use anonymous response patterns.
worked_example|Build One Verified Question|How do prompt, choices, key, source, and explanation fit?|Show editorial decisions and alternatives.
retrieval_practice|Recurring Questions|Does spaced return to a concept improve recall?|Compare delayed results with equivalent items.
feedback_design|The Reveal that Teaches|Which explanation helps after an incorrect answer?|Test concise correction and source link.
assessment_quality|Does the Score Mean Anything?|Are questions of comparable difficulty and free of clues?|Pilot with varied viewers.
visual_explanation|Quiz Screen as Evidence|Are images and charts readable and properly attributed?|Test on small screens and with text alternatives.
transfer_to_new_case|Beyond Recognizing an Answer|Can viewers solve a different example?|Include an applied follow-up.
language_access|Multilingual Quiz Publishing|Do captions and translations preserve question meaning?|Review names, units, and answer variants.
learner_variation|Who Can Keep Up?|How do prior knowledge and processing time affect participation?|Test modes with varied viewers.
source_literacy|Citations in a Quiz Video|Can a viewer verify a claim after the reveal?|Provide dated, direct sources.
curriculum_tradeoff|Entertainment and Coverage|Which topic depth is lost to rapid rounds?|Measure explanation and later recall.
field_learner_misconceptions|Analyze Viewer Answers|Which comments show a mistaken model rather than random error?|Sample respectfully and avoid public shaming.
field_lesson_sequence|Episode Order|Does arranging topics by prerequisite improve learning?|Compare viewer comprehension across sequences.
field_assessment_design|Review Before Upload|Which items have ambiguous keys or stale claims?|Use independent answer-key audit.
field_memory_and_recall|Follow-Up Episode|What can viewers answer weeks later?|Use equivalent items and correction.
field_inclusive_learning|A Quiz Everyone Can Play|Can viewers pause, extend time, use captions, and read text?|Check W3C timing and sensory-cue guidance.
"""


if __name__ == "__main__":
    revise_domain("443", "443_general_knowledge", KNOWLEDGE,
                  "General knowledge as carefully bounded, sourced, revisable claims taught with context and opportunities to check understanding.",
                  "primary source records, dated reference and curriculum editions, evidence reviews, learner responses, and education practice guides",
                  "Define terms, region, date, and measurement. A broad fact without scope or source is not ready for production; avoid implying one learner response proves mastery.")
    revise_domain("444", "444_trivia", TRIVIA,
                  "Trivia as concise, engaging, independently checkable questions with defensible answer keys, accepted variants, and corrections.",
                  "dated primary references, question drafts, answer-key reviews, player response samples, corrections, and accessible-format tests",
                  "Check superlatives, dates, transliteration, and alternative answers. Clearly mark uncertainty rather than force a single key when evidence does not support one.")
    revise_domain("445", "445_quiz_channels", QUIZ,
                  "Quiz channels as sourced question publishing and learning experiences with answer-key review, useful feedback, and accessible timing.",
                  "episode scripts and corrections, direct source citations, pilot answer data, delayed recall measures, captions and interface audits, and W3C accessibility guidance",
                  "Separate engagement metrics from learning. Give source-backed explanations and equivalent information across audio, visual, and text formats; allow time to respond.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
