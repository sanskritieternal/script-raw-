"""Editorial question designs for historical mysteries and ancient India."""

from review_angle_plans import audit, revise_domain


MYSTERY = """history_origins|How a Historical Mystery Was Named|When did a question become a popular mystery and by whom?|Trace first claims and later retellings.
famous_examples|One Disputed Historical Case|Which facts are agreed and which claims remain contested?|Use primary records.
hidden_stories|People outside the Mystery Narrative|Whose ordinary lives were eclipsed by an elite or sensational story?|Find local records.
beginner_explainers|Evidence in a History Documentary|How do object, text, oral account, and later interpretation differ?|Show provenance.
advanced_concepts|Competing Historical Explanations|Which evidence would favor one interpretation over another?|State hypotheses in advance.
mysteries_unsolved_cases|An Unresolved Event|What is genuinely unknown versus merely omitted in a popular retelling?|Inventory sources.
technology_innovation|A New Analytical Method|Did imaging, dating, or materials analysis answer the stated question?|Check methods and uncertainty.
people_personalities|A Historian or Witness's Role|How did position and access shape what one person knew?|Read their own account.
major_events|A Turning Point under Review|Which contemporary records support its date and impact?|Compare independent accounts.
how_it_works|Building a Documentary Claim|How do research, verification, narration, and correction connect?|Follow one claim ledger.
rise_fall|A Popular Theory Rejected|Which new evidence or corrected reading changed consensus?|Trace revision.
then_vs_now|Past Account and Modern Interpretation|What did contemporaries know that later viewers assume?|Keep periods distinct.
future_developments|What New Evidence Could Emerge?|Which archive, excavation, or technique could narrow uncertainty?|Avoid promising solution.
myths_vs_facts|A Viral Historical Claim|Which parts are documented, inferred, or invented?|Use source hierarchy.
documentary_stories|A Mystery with an Honest Ending|Can the story retain suspense while disclosing uncertainty?|Script evidence transitions.
source_trail|Origin of a Striking Quote|Can it be traced to a dated original rather than a modern repost?|Check text and translation.
material_evidence|An Artifact's Context|Where was it found, altered, or moved?|Use excavation and custody record.
chronology_dispute|Two Proposed Timelines|Which dated sources or layers support each?|State dating uncertainty.
ordinary_lives|Daily Life beyond the Headline|What can housing, tools, or accounts show about non-elites?|Avoid overgeneralization.
power_and_institutions|Who Controlled the Record?|Which authority preserved or suppressed information?|Analyze production context.
trade_and_exchange|An Object Far from Home|Does its presence prove trade, travel, or later collection?|Test alternatives.
language_and_labels|A Name Applied Later|What did people call themselves and who supplied modern labels?|Check original language.
maps_and_borders|Changing Places|How did geography and political boundaries shift between sources?|Use dated maps.
conflicting_accounts|Two Witnesses Disagree|What interests and access shaped each version?|Do not force false certainty.
preservation_bias|What Survived?|How do lost archives and selective excavation skew the story?|Identify absent evidence.
turning_point_test|Was This Really a Turning Point?|Which measured change followed the event?|Compare before and after.
legacy_and_memory|A Mystery in Public Memory|How have tourism, politics, or media changed its meaning?|Distinguish history from remembrance.
field_excavation_context|A Find's Original Layer|Was context recorded well enough to support dating?|Use site report.
field_dating_methods|Testing an Age Claim|Which dating method and sample actually apply?|State calibration and range.
field_urban_life|Life in a Historical Settlement|What can street and household evidence reveal?|Avoid a single city archetype.
field_trade_routes|Route or Isolated Find?|What sequence of sites supports movement?|Require dated links.
field_writing_systems|A Difficult Inscription|What is legible, translated, and conjectural?|Compare editions and expertise.
"""

INDIA = """history_origins|Defining Ancient India|Which regions and periods are covered by a particular claim?|Avoid one continuous civilization label.
famous_examples|Dholavira as a Case Study|What do site plans and excavation actually show?|Use UNESCO and ASI records.
hidden_stories|Ordinary People in Ancient South Asia|What can homes, crafts, and burials reveal beyond royal inscriptions?|State evidence limits.
beginner_explainers|Sources for Ancient India|How do archaeology, inscriptions, coins, and texts answer different questions?|Use dated examples.
advanced_concepts|Texts and Material Culture|When do a text's composition and a site's chronology diverge?|Avoid equating tradition with excavation.
mysteries_unsolved_cases|An Undeciphered Script Question|What is known from signs and context without a translation?|Do not invent readings.
technology_innovation|Ancient Water Management|What design and maintenance evidence survives at a named site?|Use site report.
people_personalities|A Person in an Inscription|What can a dated inscription establish about one person's acts?|Check provenance and translation.
major_events|A Polity's Change|Which sources support a proposed transition?|Compare regional evidence.
how_it_works|Reconstructing a South Asian Site|How do layers, artifacts, dates, and texts connect?|Map one excavation.
rise_fall|Beyond a Collapse Story|Did settlement patterns shift rather than abruptly vanish?|Compare regional chronologies.
then_vs_now|Ancient Site and Modern Memory|How have excavation and heritage policy changed interpretation?|Track dates and stakeholders.
future_developments|New Questions from Existing Collections|Which reanalysis may clarify a dated question?|Specify collection and method.
myths_vs_facts|A Sweeping Ancient India Claim|Which region and century actually support it?|Demand precise scope.
documentary_stories|One Site across Centuries|How did occupation, abandonment, excavation, and conservation unfold?|Use chronological evidence.
source_trail|A Classical Text's Version|Which manuscript or translation is being quoted?|Name edition and date.
material_evidence|Artifact and Findspot|Was an object found in a secure archaeological context?|Check catalog and layer.
chronology_dispute|Dating a Site Phase|How do radiocarbon, stratigraphy, and typology compare?|State ranges.
ordinary_lives|Work and Household Life|What do tools and residential spaces reveal about labor?|Avoid assumed identities.
power_and_institutions|Kings, Councils, and Monasteries|Which institution is supported by which source?|Separate periods and regions.
trade_and_exchange|Harappan Exchange Networks|What distribution and provenance show contact?|Distinguish contact from control.
language_and_labels|Names across Languages|How do inscriptions and later texts name a place or group?|Avoid anachronism.
maps_and_borders|A Changing South Asian Map|Can a political boundary be mapped for this exact period?|Show uncertainty.
conflicting_accounts|Text and Site Disagree|Which dates, genres, and purposes could explain the difference?|Do not collapse them.
preservation_bias|Monuments versus Everyday Materials|Why do stone and elite texts survive unevenly?|Explain missing evidence.
turning_point_test|A Claimed Cultural Break|Do settlement, pottery, and textual records show continuity or change?|Use multiple sites.
legacy_and_memory|Living Relationships to an Ancient Site|How do local communities and national heritage accounts differ?|Include present voices.
field_excavation_context|A Layer at Dholavira or Elsewhere|What was recorded before an artifact was removed?|Use excavation publication.
field_dating_methods|Calibrating an Ancient Date|Which sample and laboratory method support the chronology?|State interval.
field_urban_life|Harappan Urban Infrastructure|How were water, workshops, and residential space arranged?|Use a named site.
field_trade_routes|Evidence for a Specific Exchange Link|Which dated materials support a route between sites?|Avoid drawing unsupported lines.
field_writing_systems|What Can Be Said of Harappan Signs?|Which sign patterns are observed and why is reading disputed?|Avoid false decipherment.
"""

if __name__ == "__main__":
    revise_domain("002", "002_history_mystery_documentary", MYSTERY,
                  "History and mystery documentary through source trails, archaeological context, competing explanations, honest uncertainty, and responsible narration.",
                  "primary archives, excavation reports, dated maps and texts, object provenance, independent historical scholarship, and recorded corrections",
                  "Name event, place, period, and original source. Suspense should not turn a missing record or disputed interpretation into a proven conspiracy.")
    revise_domain("003", "003_ancient_india_civilization", INDIA,
                  "Ancient India through region-specific chronology, archaeology, inscriptions, texts, everyday life, trade, and modern stewardship.",
                  "Archaeological Survey of India excavation reports, UNESCO Dholavira and Nalanda site files, peer-reviewed archaeological analysis, inscriptions, and critical text editions",
                  "Name site, region, century, source, and interpretive uncertainty. Avoid treating diverse periods as one continuous polity or an undeciphered script as translated.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
