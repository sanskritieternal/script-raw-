"""Editorial questions for history of education."""

from review_angle_plans import audit, revise_domain


HISTORY = """history_origins|The Founding of One School System|Which needs and political choices shaped schooling in one place?|Use dated laws, budgets, enrollment, and community records.
famous_examples|A Celebrated School Reform Revisited|Who gained access after one reform and who remained excluded?|Compare stated aims with disaggregated attendance and completion.
hidden_stories|The Workers Behind Education|Whose teaching, care, maintenance, and organizing labor is omitted?|Trace staff records, oral histories, pay, and working conditions.
beginner_explainers|Reading an Old Enrollment Figure|What does one historical school statistic actually count?|Identify age range, school type, reporting area, exclusions, and source.
advanced_concepts|Compulsory Schooling and Real Access|Did a compulsory law make attendance possible for all children?|Compare enforcement with fees, distance, work, language, and disability.
mysteries_unsolved_cases|A Missing School Archive|What can be established when one institution's records are sparse?|Triangulate government records, local papers, objects, and memories.
technology_innovation|The Classroom Tool That Changed Practice|How did one educational technology affect teaching in a defined period?|Compare procurement, classroom use, costs, training, and outcomes.
people_personalities|A Teacher in Context|How did one educator's ideas meet institutional constraints?|Use letters, lesson plans, school records, and colleagues' accounts.
major_events|A Crisis and the School Calendar|How did one conflict, epidemic, or disaster alter learning access?|Trace closures, alternatives, attendance, and uneven effects.
how_it_works|From Policy to Classroom|How was one education reform funded and implemented?|Follow law, budget, teacher preparation, curriculum, and inspection.
rise_fall|The Life of a Local School|Why did one school open, expand, merge, or close?|Use population, policy, funding, transport, and community records.
then_vs_now|A School Day Across Generations|How did one community's school day change?|Compare timetables, curriculum, rules, access, and oral memories.
future_developments|Learning from a Past Reform|Which documented conditions matter for a current proposal?|Compare contexts carefully and avoid treating historical outcomes as forecasts.
myths_vs_facts|Were Schools Better Before?|Does one nostalgic claim fit evidence from a named time and place?|Check access, curriculum, assessment, dropout, and excluded groups.
documentary_stories|One Cohort Through School|What can records reveal about a defined group of pupils?|Follow enrollment, attendance, transition, and privacy limits.
source_trail|Where a Schooling Claim Began|Which document first supported a repeated claim about a reform?|Trace wording, date, measurement, and later citations.
material_evidence|What an Old Classroom Object Reveals|What can one desk, book, or register tell us about learning?|Check provenance, wear, use context, and what remains unknown.
chronology_dispute|When Did Education Become Universal?|Which threshold does each claimed date represent?|Separate legal entitlement, enrollment, attendance, completion, and equity.
ordinary_lives|A Pupil's Journey to Class|What practical barriers shaped one child's schooling?|Use permitted personal records, transport, household, and local accounts.
power_and_institutions|Who Set the Curriculum?|Which institutions decided what children would learn?|Trace authority, consultation, textbooks, teacher discretion, and resistance.
trade_and_exchange|The Economics of Schoolbooks|How did books reach classrooms and who paid?|Follow publishers, procurement, lending, reuse, and household expense.
language_and_labels|Which Language Counted as Schooling?|How did language policy affect access and identity?|Compare official texts, classroom practice, and community testimony.
maps_and_borders|The Geography of School Access|How did school locations and boundaries shape attendance?|Map travel time, catchments, transport, and demographic change.
conflicting_accounts|Two Memories of One School|Why do former pupils and official records describe it differently?|Attribute accounts, compare dates, and discuss memory and record limits.
preservation_bias|Whose School Records Survive?|How does archive selection skew education history?|Compare preserved elite institutions with missing rural or informal schools.
turning_point_test|Did a Reform Change Outcomes?|What evidence isolates one reform's effects?|Compare timelines, alternative changes, cohort definitions, and data quality.
legacy_and_memory|A School's Public Memory|How is one institution remembered by former pupils and neighbors?|Contrast commemorations, archives, and varied consented accounts.
field_oral_history|Interviewing Former Students|How can memories enrich a school history responsibly?|Seek consent, explain future use, and compare memories with dated records.
field_archive_gap|Reconstructing an Absent Classroom|Which sources can describe teaching where class records are lost?|Use curricula, exams, pay records, objects, and qualified inference.
field_material_culture|A Textbook as Historical Evidence|What did one book prescribe, and what did pupils actually encounter?|Compare edition, ownership marks, teacher notes, and oral accounts.
field_community_memory|A School's Place in a Community|How do different generations describe its role?|Include multiple groups and distinguish shared memory from fact.
field_representation_ethics|Telling Stories About Former Pupils|How should a documentary handle sensitive education records?|Apply access rules, consent, minimization, and fair context.
"""


if __name__ == "__main__":
    revise_domain("144", "144_history_of_education", HISTORY,
                  "History of education through policy, classrooms, access, language, labor, institutions, and whose records survive.",
                  "dated laws and curricula, school archives and budgets, enrollment metadata, historical maps and objects, and consented former pupil, teacher, and community accounts",
                  "Name place, period, school type, and population. Distinguish enrollment, attendance, completion, and learning; protect personal and child records; do not infer one universal school experience from elite archives.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
