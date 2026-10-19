"""Editorial questions for childhood history."""

from review_angle_plans import audit, revise_domain


CHILDHOOD = """history_origins|How Childhood Was Recorded|Which institutions first documented children's lives in one place?|Compare family, school, court, health, and community archives.
famous_examples|A Famous Child-Reform Story Revisited|Did one law improve the lives of children it targeted?|Compare adoption, enforcement, access, and varied outcomes.
hidden_stories|Children Outside Official Archives|Whose play, work, disability, or migration is scarcely recorded?|Seek diverse sources and explain archival absence.
beginner_explainers|Childhood Is Historical|How did age, work, care, and schooling vary in a named time and place?|Use local records without claiming one universal childhood.
advanced_concepts|Law Versus Lived Childhood|Did formal child rights change everyday opportunities?|Compare policy with household, school, work, and service records.
mysteries_unsolved_cases|A Child's Uncertain Identity in Records|Which evidence can link two records without exposing descendants?|Compare names, ages, households, dates, and privacy limits.
technology_innovation|A Childhood Object in Context|How did one toy or learning tool change opportunities?|Compare access, cost, use, safety, and varied children.
people_personalities|A Child's Recorded Voice|What can one diary or interview reveal and what cannot it?|Preserve author, audience, editing, consent, and context.
major_events|Children During a Public Crisis|How did one event alter play, schooling, care, and safety?|Compare dated records and differences across groups.
how_it_works|A Child Protection System in One Era|How did reports move through actual institutions?|Trace law, staff, resources, practices, and documented outcomes.
rise_fall|A Local Children's Institution|Why did one school, home, or club open and close?|Examine funding, policy, need, oversight, and affected voices.
then_vs_now|The Same Childhood Task Across Eras|How did travel to school, play, or work change?|Match place and age and account for unequal access.
future_developments|What Childhood History Can Inform|Which past policy lesson applies to a current question?|Compare contexts and avoid predicting from one historical case.
myths_vs_facts|Were Children Always Safer Before?|Does a nostalgic claim fit records from one population?|Check mortality, violence, work, reporting, and missing data.
documentary_stories|A Day Reconstructed from Records|What can sources support about one historical child's routine?|Label documented facts, plausible inference, and unknowns.
source_trail|Where a Childhood Claim Came From|Which original source supports a repeated story about children?|Trace author, date, purpose, copying, and alternative sources.
material_evidence|A Child's Object as Evidence|What does one book, garment, or toy reveal?|Check provenance, repair, ownership, and survival bias.
chronology_dispute|When Did a Child Reform Take Effect?|Which date marks law, funding, implementation, or uptake?|Separate each stage and geographic variation.
ordinary_lives|Play and Work in One Household|What daily activities can be documented?|Use family records, school, work, artifacts, and children's own accounts.
power_and_institutions|Who Decided for Children?|How did adults and institutions shape choices in one era?|Compare law, family practice, children's actions, and constraints.
trade_and_exchange|The Cost of Raising a Child|Which goods and services did households secure or forgo?|Use prices, wages, care arrangements, and unequal resources.
language_and_labels|Names Applied to Children|How did historic age or status labels affect treatment?|Compare original terms, legal meaning, and modern interpretation.
maps_and_borders|A Child's Geography|How did home, school, work, and play space relate?|Use period maps, routes, safety, and access limits.
conflicting_accounts|Adults and Children Remember Differently|How can a story hold multiple perspectives?|Attribute accounts and compare contemporary records and memory.
preservation_bias|Which Children's Voices Survived?|How did literacy, class, institutions, and collecting shape the archive?|Seek material and oral sources beyond elite diaries.
turning_point_test|Was One Law a Childhood Revolution?|What changed and what continued after a reform?|Compare cohorts, enforcement, outcomes, and excluded children.
legacy_and_memory|How a Childhood Place Is Remembered|How do former pupils and neighbors interpret one site?|Use voluntary accounts and preserve disagreement.
field_oral_history|Adults Recall Their Childhood|How can memory be used responsibly?|Secure consent, date recollections, compare records, and avoid forced disclosure.
field_archive_gap|Reconstructing a Missing Child Record|Which other sources can establish context without a guessed identity?|Use aggregate records, local history, and explicit uncertainty.
field_material_culture|A Schoolbook's Wear|What can marks and repairs reveal about use?|Compare edition, provenance, classroom practice, and unknowns.
field_community_memory|Childhood Across a Neighborhood|How do generations remember spaces for care and play?|Include diverse households and compare maps and policy.
field_representation_ethics|A Child in a Historical Story|How should sensitive records and living descendants be treated?|Minimize identity exposure, assess public interest, rights, and consent.
"""


if __name__ == "__main__":
    revise_domain("175", "175_childhood_history", CHILDHOOD,
                  "Childhood history through children's own voices, care, play, work, schooling, law, archival gaps, and rights across specific places and periods.",
                  "dated school, family, legal, work, and health records with access limits, children's objects and writings, period maps, and voluntary consented recollections",
                  "Name place, era, age group, and source. Avoid universal or nostalgic childhood claims; protect children's records and living descendants, and distinguish direct evidence from reconstructed scenes.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
