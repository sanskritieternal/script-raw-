"""Editorial questions for family history."""

from review_angle_plans import audit, revise_domain


FAMILY = """history_origins|The Earliest Documented Family Link|Which records support one claimed relationship across generations?|Compare original documents, dates, names, and alternative matches.
famous_examples|A Public Family Story Rechecked|What survives of one often-retold family narrative?|Trace earliest telling, archives, omissions, and descendants' views.
hidden_stories|Relatives Missing from the Tree|Whose adoption, care, step, or nonlegal ties disappear from records?|Use consented accounts and explain records' categories.
beginner_explainers|A Family Tree as a Claim Map|How is each connection supported and how certain is it?|Label source, inference, conflicting evidence, and unknowns.
advanced_concepts|Same Name, Different Person|How can researchers avoid false links in a large archive?|Compare age, address, household, occupation, and independent records.
mysteries_unsolved_cases|A Gap Between Generations|Which evidence might resolve one missing parentage or migration link?|Map known records, plausible alternatives, and privacy limits.
technology_innovation|Digital Genealogy's Limits|What can searchable archives or DNA matching show?|Check database coverage, errors, consent, and unexpected disclosures.
people_personalities|An Ancestor Beyond Dates|What can documents reveal about one person's choices and constraints?|Use letters, work, land, and context without invented thoughts.
major_events|A Family During a Public Crisis|How did one dated event affect documented household choices?|Compare records, local context, and varied relatives' experiences.
how_it_works|Following One Archival Lead|How does a record lead to corroboration rather than a guessed link?|Trace provenance, transcription, independent source, and uncertainty.
rise_fall|A Household's Changing Circumstances|Which economic and social factors shaped one family's fortunes?|Compare property, wages, work, law, and migration.
then_vs_now|A Family Story Across Generations|How did later relatives retell one event differently?|Compare dated versions, new evidence, and memory context.
future_developments|What New Records Could Clarify|Which unresolved question might an archive release answer?|Name holdings, access rules, expected limits, and consent.
myths_vs_facts|A Claimed Famous Ancestor|Does documentation support one prestigious relationship?|Build a generation-by-generation chain and identify gaps.
documentary_stories|One Object Across a Family|What can an inherited item reveal about changing lives?|Trace ownership, date, material, stories, and uncertain links.
source_trail|Where a Family Claim Began|Which source first asserted one relationship or event?|Trace original record, copy, transcription, and later repetition.
material_evidence|A Photograph's Provenance|Who, where, and when does a family photo actually show?|Check original print, annotations, clothing, setting, and corroboration.
chronology_dispute|Two Birth Dates or Two People?|How can conflicting dates be evaluated?|Compare record purpose, informant, timing, and likely error.
ordinary_lives|A Working Day in the Family|What can routine records show about one household's labor?|Use pay, school, census, letters, and limits.
power_and_institutions|Who Was Legally Counted as Family?|How did inheritance, marriage, adoption, or citizenship law shape records?|Compare law in force with actual relationships and exclusion.
trade_and_exchange|The Family's Movement of Goods|What do remittances, parcels, or business records show?|Trace dated exchanges and avoid assuming motives.
language_and_labels|Names Across Languages|How did spelling, translation, or naming practice alter the record?|Compare original-language documents and self-used names.
maps_and_borders|Following a Family Route|How did borders and place names change along one migration?|Use period maps, documents, dates, and jurisdiction.
conflicting_accounts|Relatives Remember Differently|How can a story include incompatible memories fairly?|Attribute accounts, check records, and leave unresolved points open.
preservation_bias|Whose Family Papers Survive?|How did wealth, literacy, institutions, and loss shape the archive?|Compare documented and undocumented relatives without ranking importance.
turning_point_test|Was This the Defining Family Move?|Did one decision cause later outcomes or only precede them?|Check alternative causes and multiple family branches.
legacy_and_memory|Who Owns the Family Story?|How do descendants disagree about sharing intimate history?|Discuss rights, consent, privacy, and competing interests.
field_oral_history|Interviewing a Relative|How can one interview preserve memory without pressure?|Explain purpose, use, review options, and consent.
field_archive_gap|Research When Records Are Missing|Which other sources can help without overstating certainty?|Use neighbors, land, community archives, and transparent limits.
field_material_culture|An Heirloom's Real History|Can one object's maker and path be verified?|Compare marks, materials, provenance, and family accounts.
field_community_memory|A Family in a Wider Community|How do local records challenge a family-only account?|Use community archives and affected people's perspectives.
field_representation_ethics|Living Relatives in a Historical Film|Which facts can be shared without exposing someone?|Assess consent, sensitive records, third parties, and public interest.
"""


if __name__ == "__main__":
    revise_domain("173", "173_family_history", FAMILY,
                  "Family history through sourced relationships, archival gaps, migration, memory, material objects, and living relatives' privacy.",
                  "original civil, religious, land, work, and migration records with provenance, period maps, family objects, and voluntary consented oral histories",
                  "Name family, place, period, and each source. Do not treat a tree link or DNA match as proof without corroboration; protect living relatives, nonpaternity discoveries, adoption, and third-party information.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
