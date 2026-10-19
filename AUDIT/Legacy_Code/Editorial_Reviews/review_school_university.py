"""Editorial questions for school and university stories."""

from review_angle_plans import audit, revise_domain


SCHOOLS = """history_origins|Why This Institution Was Founded|Which local needs and choices led to one school's creation?|Use charter, funding, location, admissions, and community records.
famous_examples|A Celebrated Campus Initiative Tested|What did one well-known teaching initiative change for learners?|Compare stated aim, implementation, participation, and outcomes.
hidden_stories|Work Behind the Classroom|Whose service, care, and administrative labor makes study possible?|Follow consented staff accounts, roles, pay, and institutional records.
beginner_explainers|How a School Decision Is Made|Who decides one curriculum, timetable, or admissions rule?|Map current authority, consultation, funding, and appeal routes.
advanced_concepts|Grades and Actual Learning|How well does one assessment capture the knowledge it claims to test?|Compare task, scoring, reliability, access, and later application.
mysteries_unsolved_cases|Why a Program's Outcomes Differ|Which plausible factors explain varied results in one school program?|Check selection, attendance, teacher support, resources, and data gaps.
technology_innovation|A Campus Learning Tool in Use|Does one new tool help a defined group learn a specific skill?|Compare use, accessibility, evaluation, privacy, and support costs.
people_personalities|The Teacher's Design Choices|How does one teacher adapt a lesson to their learners?|Observe with permission and connect choices to goals and feedback.
major_events|A School Through a Disruption|How did one institution respond to a closure or other disruption?|Trace dated decisions, access, staff workload, and learner outcomes.
how_it_works|From Course Goal to Lesson|How is a stated learning goal translated into teaching and assessment?|Follow one course's sequence, materials, practice, feedback, and revision.
rise_fall|A Program Opens or Closes|Why did one department or school program change direction?|Compare demand, financing, staffing, results, and affected learners.
then_vs_now|A Course Across Two Generations|How did one subject's teaching and access change?|Compare dated syllabi, assessment, resources, and student mix.
future_developments|A Proposed Campus Reform|What would show whether one proposed change helps students?|Define outcome, comparison, implementation cost, and equity effects.
myths_vs_facts|One Campus Reputation Checked|Does a popular claim about one institution match its records?|Specify cohort, measure, period, comparison, and missing data.
documentary_stories|A Learner's Path Through One Course|What barriers and supports shape a student's progress?|Use voluntary consent, anonymized records, and broader context.
concept_sequence|Building a Difficult Idea|How does one course order prerequisites for a named concept?|Map lessons, examples, learner work, and points of confusion.
misconception|A Common Wrong Answer|What reasoning lies behind one recurring student error?|Analyze anonymized work and interview volunteers without labeling them.
worked_example|When a Worked Example Helps|Does one example prepare students for independent problems?|Compare example design, practice, learner work, and transfer.
retrieval_practice|Remembering After the Unit Ends|Does one course revisit knowledge after a delay?|Compare practice schedule, later recall, and learner burden.
feedback_design|Feedback Students Can Use|Does one feedback method tell learners what to do next?|Review timing, specificity, response opportunities, and student experience.
assessment_quality|What an Exam Measures|Do tasks and scoring match the course's stated aims?|Examine validity, consistency, accessibility, and unintended incentives.
visual_explanation|A Diagram in the Lesson|Does one visual clarify or distort the concept?|Test it with learners and check labels, scale, and accessibility.
transfer_to_new_case|Using Knowledge Elsewhere|Can learners apply one idea to a new situation?|Define the new task, prior teaching, comparison, and evidence of reasoning.
language_access|Learning in a Second Language|Which language choices help or block access in one course?|Compare materials, assessment language, support, and learner accounts.
learner_variation|Different Paths Through One Course|How do students with varied preparation and needs encounter it?|Use accessible observation and disaggregated, privacy-safe outcomes.
source_literacy|Checking a Course's Source|How are students taught to evaluate one disputed claim?|Follow source selection, context, evidence comparison, and assessment.
curriculum_tradeoff|What Fits in the School Year?|What was added or removed when one curriculum changed?|Compare hours, goals, teacher support, learner needs, and alternatives.
field_learner_misconceptions|Listening Before Explaining|What do learners already think about a named topic?|Use voluntary, anonymized responses and avoid deficit labels.
field_lesson_sequence|A Lesson Series Under Review|Does each step prepare students for the next?|Observe sequence, practice, feedback, and adjustment with consent.
field_assessment_design|Designing a Fair Task|Can one task assess understanding across different learner needs?|Check clarity, accommodations, scoring, and pilot results.
field_memory_and_recall|What Persists Months Later?|Which taught ideas can a group recall and use later?|Use appropriate comparison, consent, and no high-stakes inference.
field_inclusive_learning|Who Can Participate Fully?|Which classroom or campus barriers limit one group?|Check language, physical access, materials, scheduling, and support.
"""


if __name__ == "__main__":
    revise_domain("145", "145_school_university_stories", SCHOOLS,
                  "Specific school and university stories through governance, teaching design, learner experience, assessment, inclusion, and institutional change.",
                  "current institutional policies and course materials, anonymized learner work and outcomes, evaluations with defined comparators, accessibility review, and voluntary consented staff and learner accounts",
                  "Name institution, course, cohort, jurisdiction, and date. Protect minors and student records, obtain proper consent, avoid identifying struggling learners, and do not claim a teaching method works universally from one classroom.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
