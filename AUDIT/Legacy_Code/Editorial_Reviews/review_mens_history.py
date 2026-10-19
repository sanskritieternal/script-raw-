"""Editorial questions for men's history as gender history."""

from review_angle_plans import audit, revise_domain


MEN = """history_origins|A Local Ideal of Manhood|When did one expectation about men emerge in a specific setting?|Trace dated texts, law, work, family, and dissent.
famous_examples|A Celebrated Male Role Reexamined|What did one public ideal ask of men and whom did it exclude?|Compare speeches, institutions, behavior, and varied accounts.
hidden_stories|Men's Care Work in the Archive|Which forms of fathering, nursing, or mutual aid have been overlooked?|Use household, workplace, welfare, and oral records.
beginner_explainers|Men's History as Gender History|What changes when men are studied as a gendered group?|Use one institution and compare norms with diverse lived practice.
advanced_concepts|Power and Constraint Together|How did one male privilege coexist with duties or exclusions?|Compare law, class, race, sexuality, age, work, and outcomes.
mysteries_unsolved_cases|An Unclear Male Role in Records|Can one person's duties or identity be reconstructed?|Compare multiple source types and avoid imposing modern labels.
technology_innovation|A Machine Changes Men's Work|How did one technical shift alter skills, risk, or household roles?|Use pay, injury, training, and family records.
people_personalities|A Man Beyond a Public Role|What do sources show about work, care, belief, and contradictions?|Use attributed records without speculative private motives.
major_events|A War or Reform Reshapes Roles|How did one event alter expectations of men?|Compare policy, recruitment, labor, households, and resistance.
how_it_works|Studying an Ideal and Its Practice|How can historians test what men were told against what they did?|Compare prescriptive texts with diaries, courts, work, and families.
rise_fall|A Male-Dominated Occupation Changes|Why did the workforce and status of one job shift?|Check wages, education, law, technology, and access.
then_vs_now|Fatherhood Across Generations|How did care time, legal duties, and expectations change?|Use comparable records and avoid an idealized past.
future_developments|An Archive Beyond Famous Men|Which ordinary men's lives need better documentation?|Identify source gaps, community priorities, privacy, and collections.
myths_vs_facts|Men Always Had One Role?|Does a universal claim about men's past fit different contexts?|Compare place, class, period, family structure, and counterexamples.
documentary_stories|A Working Day in One Man's Life|What can records support about job, home, and obligations?|Use dated documents and label uncertain reconstruction.
source_trail|A Repeated Claim About Manhood|Where did one historical generalization originate?|Trace first source, population, context, and later repetition.
material_evidence|An Object Made or Used by Men|What can its provenance reveal about skill and status?|Check maker, ownership, wear, role, and alternative interpretation.
chronology_dispute|When Did a Male Role Change?|Do different dates refer to law, norm, or actual behavior?|Separate each with matched evidence.
ordinary_lives|Men Outside Elite Archives|What records reveal everyday work, caregiving, and leisure?|Use wages, census, letters, objects, and oral histories.
power_and_institutions|How Institutions Made Masculinity|How did school, military, workplace, or state define men's roles?|Compare policy, enforcement, refusal, and unequal effects.
trade_and_exchange|Men's Labor and Household Money|How did one group earn, spend, and share resources?|Use pay, remittances, debts, and family records.
language_and_labels|Names for Men and Masculinity|How did terms change across language and class?|Read period vocabulary in context and respect self-description.
maps_and_borders|Men's Migration and Separation|How did movement reshape work and family obligations?|Trace routes, policy, correspondence, and people left behind.
conflicting_accounts|Different Men, Different Ideals|Why did men disagree about a role or obligation?|Present attributed debate and variation within groups.
preservation_bias|Why Powerful Men's Papers Dominate|Which archives privilege leaders over ordinary lives?|Compare collection practice and alternative local records.
turning_point_test|Did One Reform Change Men's Lives?|What actually changed after a named policy?|Compare groups, enforcement, household outcomes, and continuity.
legacy_and_memory|How a Male Figure Is Remembered|Does commemoration obscure collaborators or harmed groups?|Compare original record, public memory, and later critique.
field_oral_history|Interviewing Men About Past Roles|How can personal memory inform gender history?|Use voluntary consent and compare accounts with dated sources.
field_archive_gap|A Life Missing from Official Files|Which community or family records fill part of the gap?|Trace provenance and state uncertainty.
field_material_culture|Tools and Clothing as Evidence|What did an object signal about work or identity?|Compare use, access, period, and wearer or maker accounts.
field_community_memory|A Local Model of Manhood|How do generations remember one ideal differently?|Include varied men and other affected voices.
field_representation_ethics|Avoiding a Single Men's Story|How can a film show unequal power and diverse lives?|Check class, race, sexuality, age, relationships, and evidence.
"""


if __name__ == "__main__":
    revise_domain("178", "178_mens_history", MEN,
                  "Men's history as gender history through changing ideals, work, care, institutions, power, and variation among men.",
                  "dated institutional, legal, wage, family, military, and migration records, material objects, scholarly gender history, and voluntary consented oral accounts",
                  "Name place, period, group, and institution. Do not treat men as an unmarked universal norm or one homogeneous group; distinguish prescribed masculinity from actual life and include people affected by men's power.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
