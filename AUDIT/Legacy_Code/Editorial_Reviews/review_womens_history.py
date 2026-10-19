"""Editorial questions for women's history."""

from review_angle_plans import audit, revise_domain


WOMEN = """history_origins|Women's Place in One Institution|When and how did women enter a named field or organization?|Trace rules, actual participation, roles, and barriers.
famous_examples|A Celebrated Pioneer in Context|What did one woman contribute and who worked with her?|Use original work, institutional records, collaborators, and later credit.
hidden_stories|Unpaid Work That Sustained Change|Whose care, household, and organizing labor enabled public achievements?|Use time, wage, family, and movement records.
beginner_explainers|Reading Women's History Sources|Why may official records undercount women's activity?|Show naming, property, occupation, and archival rules in one case.
advanced_concepts|Access Is Not Equal Power|Did legal admission translate into authority and pay?|Compare participation, promotion, governance, compensation, and testimony.
mysteries_unsolved_cases|An Unidentified Woman in an Archive|Which evidence can establish a person's identity or role?|Compare image provenance, staff lists, dates, and competing matches.
technology_innovation|Women and a Technical Change|How did one technology alter women's work or opportunity?|Compare skill, pay, ownership, safety, and access.
people_personalities|A Woman Beyond the First Label|How do records complicate a single heroic biography?|Trace projects, collaborators, constraints, disagreement, and changing views.
major_events|A Rights Reform in Practice|What changed after one law or movement victory?|Compare implementation, access, resistance, and unequal effects.
how_it_works|Recovering an Overlooked Contribution|How can researchers connect an unnamed task to its maker?|Trace original documents, object marks, oral histories, and uncertainty.
rise_fall|A Women's Organization Over Time|Why did one group expand, change purpose, or close?|Check membership, funding, policy, internal debate, and outcomes.
then_vs_now|Women's Work Across Generations|How did pay, care burden, and opportunity change in one place?|Use comparable definitions and account for class and other differences.
future_developments|An Archive Correction Project|Which records and metadata should be improved next?|Set provenance, community input, privacy, and measurable discoverability.
myths_vs_facts|The First Woman Claim|Does one first claim depend on a narrow category?|Check definition, date, earlier candidates, and exclusion from records.
documentary_stories|A Day Reconstructed from Women's Records|What can one worker's or organizer's documents show?|Label sourced activities, context, and unknowns.
source_trail|A Repeated Women's History Claim|Where did one biographical fact or quote originate?|Trace original document, transcription, citation, and corrections.
material_evidence|An Object and Its Woman Maker|What evidence ties an object to a named maker?|Check provenance, labels, technique, acquisition, and alternative attribution.
chronology_dispute|When Was a Right Actually Won?|Which dates mark law, implementation, and broad access?|Distinguish each phase and jurisdiction.
ordinary_lives|A Woman's Working Week|How did paid and unpaid labor fit together?|Use diaries, time records, wages, family and institutional context.
power_and_institutions|Who Set the Rules for Women's Roles?|How did one institution allocate training, pay, or authority?|Read policies alongside personnel and lived records.
trade_and_exchange|Women's Economic Networks|How did a named group access credit, markets, or property?|Trace transactions, law, informal exchange, and limits.
language_and_labels|Names That Hide Women|How did marital names, titles, or occupational labels obscure records?|Compare original names, later indexing, and self-identification.
maps_and_borders|Women's Mobility and Place|How did geography and law shape one woman's movement?|Use dated routes, permits, work, migration, and safety context.
conflicting_accounts|A Movement's Internal Debate|Why did participants disagree on strategy or goals?|Use attributed statements and avoid one unified women's voice.
preservation_bias|Which Women's Papers Survive?|How did class, literacy, collecting, and institutions shape the archive?|Seek material, oral, and community records beyond elite papers.
turning_point_test|Did One Victory Transform Lives?|What changed and what persisted after a named reform?|Compare groups, outcomes, enforcement, and countervailing pressures.
legacy_and_memory|Who Is Remembered as a Pioneer?|How did commemoration privilege one person over collaborators?|Compare original work, monuments, school texts, and criticism.
field_oral_history|Interviewing Women About Past Work|How can memory add to incomplete employment records?|Seek consent, retain context, and compare dated records.
field_archive_gap|Finding a Woman in Others' Files|Which adjacent records may document someone missing from a catalog?|Search collaborators, payroll, correspondence, publications, and community archives.
field_material_culture|A Domestic Object as Labor Evidence|What can wear, repair, and design show about work?|Check provenance and avoid treating one object as universal.
field_community_memory|Women's History in Local Memory|How do different women and families remember one institution?|Use varied consented accounts and preserve disagreement.
field_representation_ethics|A Life Beyond Victim or Hero|How can a film show agency without hiding constraint?|Check sources, privacy, collaborators, and participant or descendant views.
"""


if __name__ == "__main__":
    revise_domain("177", "177_womens_history", WOMEN,
                  "Women's history through documented work, rights, institutions, networks, archival absence, contested credit, and varied lives.",
                  "original institutional, wage, legal, family, and movement records, object provenance, community archives, and voluntary consented oral histories",
                  "Name place, period, institution, and population. Do not generalize one woman's experience to all women; distinguish law from actual access, check first claims carefully, and credit collaborators and unpaid labor.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
