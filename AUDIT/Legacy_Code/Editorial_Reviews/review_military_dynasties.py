"""Editorial question review for military history and dynastic history."""

from review_angle_plans import audit, revise_domain


MILITARY = """history_origins|Why a Force Was Formed|Which political or security decision created one military formation?|Compare founding orders, financing, recruitment, and local context.
famous_examples|A Battle Beyond the Legend|What did one well-known battle change, and what persisted?|Use campaign records, casualty evidence, civilian accounts, and later outcomes.
hidden_stories|Support and Civilian Labor|Whose transport, medical, manufacturing, or domestic work sustained one campaign?|Trace records and attributed accounts beyond commanders.
beginner_explainers|Reading a Campaign Map|How do historians reconstruct the movement of a force?|Compare dated orders, unit diaries, terrain, maps, and reporting gaps.
advanced_concepts|Strategy and Actual Capacity|Could a commander's plan be carried out with available people and supplies?|Compare orders with personnel, transport, timing, and enemy information known then.
mysteries_unsolved_cases|A Disputed Battlefield Event|Which accounts of one event can be reconciled with physical and documentary evidence?|Compare date, vantage point, translation, and surviving records.
technology_innovation|A Tool Changes a Campaign|What did one weapon, communication, or medical change actually alter?|Compare adoption, training, constraints, outcomes, and nontechnical causes.
people_personalities|A Commander's Decision in Context|What did a named leader know when making one decision?|Use contemporary orders and reports, not hindsight or imagined intent.
major_events|A Turning Point Tested|Did one military event materially change the course of a conflict?|Define outcome and compare subsequent resources, decisions, and timelines.
how_it_works|From Order to Field Action|How did one command move through planning, supply, communication, and execution?|Trace a documented operation without presenting actionable tactics.
rise_fall|A Force's Changing Effectiveness|Why did one military organization gain or lose capacity over time?|Compare recruitment, training, supply, leadership, and political support.
then_vs_now|Remembering a Campaign Differently|How has one conflict's official account changed between two periods?|Compare archives, scholarship, monuments, and affected communities.
future_developments|An Unfinished Historical Question|Which newly available records could clarify one contested event?|Name archive, evidence gap, and limits without predicting a definitive answer.
myths_vs_facts|A Wartime Legend Checked|Does a familiar story match contemporaneous records?|Locate the earliest claim and compare orders, diaries, casualty data, and later retellings.
documentary_stories|A Campaign Through Its Records|How did one bounded campaign unfold for forces and civilians?|Build a dated multi-source timeline with uncertainty visible.
source_trail|Who Produced a War Record?|What did the author of one official account know and need to report?|Examine purpose, audience, censorship, timing, and missing attachments.
material_evidence|Objects from a Conflict|What can one artifact or damaged site show about an event?|Check provenance, dating, condition, and alternative explanations.
chronology_dispute|Two Timelines of an Operation|Why do sources disagree about when an event occurred?|Compare clocks, calendars, reporting delay, and location.
ordinary_lives|Life During Mobilization|How did one military campaign alter ordinary work, food, or movement?|Use letters, ration records, local archives, and attributed testimony.
power_and_institutions|Who Authorized Force?|Which institution had formal and practical authority over one operation?|Compare law, command structure, orders, and accountability.
trade_and_exchange|Supply Across Borders|How did trade, requisition, or allied supply sustain one campaign?|Follow documented goods and affected communities.
language_and_labels|Names for a Conflict|How do different names for one event reflect competing claims?|Attribute each term and avoid treating one source's label as neutral.
maps_and_borders|A Front Line on the Map|How accurately do dated maps show control at a specific moment?|Compare cartography, unit reports, civilian accounts, and uncertainty.
conflicting_accounts|Opposing Reports of One Action|Where do two sides' records agree and diverge?|Check provenance, translation, censorship, and physical evidence.
preservation_bias|Whose War Records Survived?|How do archive gaps distort a campaign narrative?|Identify destroyed, restricted, or never-created records and affected voices.
turning_point_test|Before and After One Battle|Which measurable resources or decisions changed after a supposed turning point?|Compare the same indicators on both sides before and after.
legacy_and_memory|A War Memorial's Story|Whom does one memorial honor or omit?|Compare dedication records, local debate, and current community views.
field_strategic_choices|A Choice Among Historical Options|Which alternatives did decision makers actually consider?|Use dated planning records and constraints; avoid speculative reenactment as fact.
field_civilian_experience|Civilians in a Military Zone|What can documented civilian accounts show about one operation's effects?|Use consent and privacy safeguards with corroborating records.
field_logistics|The Supply Constraint|Which documented shortage changed one campaign's course?|Compare inventories, transport, distribution, and field reports without operational guidance.
field_leadership_claims|Testing a Leadership Legend|Does one leader's reputation match documented decisions and outcomes?|Compare contemporaneous evidence, team roles, and later mythmaking.
field_aftermath|After the Fighting|What happened to displaced people, veterans, land, and institutions after one conflict?|Use dated records and affected voices over a defined period."""


DYNASTIES = """history_origins|How a Dynasty Established Rule|Which claim and institutions supported one dynasty's accession?|Compare genealogy, law, force, alliances, and contemporary records.
famous_examples|A Reign Beyond the Portrait|What did one famous ruler actually govern and leave behind?|Compare decrees, finances, court records, and subjects' experiences.
hidden_stories|Households Behind the Crown|Whose labor and relationships sustained one royal household?|Use accounts, inventories, correspondence, and attributed local records.
beginner_explainers|How Succession Worked|Which rule governed succession in one polity at one date?|Explain written law, custom, competing claimants, and actual decision.
advanced_concepts|Legitimacy and Effective Power|Why could a formally recognized monarch lack practical control?|Compare court, treasury, military, landholders, and rival institutions.
mysteries_unsolved_cases|A Contested Heir|What evidence supports competing claims about one succession?|Examine dated birth, marriage, legal, and diplomatic records with gaps labeled.
technology_innovation|Communication of Royal Authority|How did a printing, coinage, or transport change shape one dynasty's reach?|Follow dated adoption, distribution, and local reception.
people_personalities|A Royal Figure in Their Records|How do private letters, public acts, and later biographies differ for one person?|Check provenance, intended audience, and contradictory testimony.
major_events|A Succession Crisis|What sequence of decisions turned one death or abdication into a political crisis?|Build a dated timeline of claimants, institutions, and public effects.
how_it_works|Governing Through a Court|How did a royal household and formal offices implement one policy?|Map appointment, revenue, orders, and local execution.
rise_fall|Why a Dynasty Lost Rule|Which political, fiscal, military, or social changes ended one dynasty's power?|Compare multiple causes and what survived afterward.
then_vs_now|A Monarchy Across Two Eras|How did the authority of one royal office change between two dated periods?|Compare law, practice, finance, and public accountability.
future_developments|A Historical Question for New Archives|Which uncatalogued or newly opened records might revise one dynastic account?|State existing evidence gap and plausible scope of change.
myths_vs_facts|A Royal Family Legend Checked|Does a popular ancestry or heroic claim match contemporary sources?|Trace earliest version, genealogy, documents, and contradictory evidence.
documentary_stories|One Succession Through Its Documents|How did a claim to rule proceed from assertion to recognition or failure?|Use dated correspondence, legal acts, and responses beyond the court.
source_trail|Who Wrote a Royal Chronicle?|What interests and sources shaped one chronicle of a reign?|Examine patronage, genre, date, translation, and omissions.
material_evidence|An Object of Rule|What can a coin, seal, palace room, or inscription reveal about authority?|Check dating, provenance, use, and later alteration.
chronology_dispute|Dating a Reign|Why do sources disagree on a ruler's start or end date?|Compare accession, coronation, effective control, calendar, and record survival.
ordinary_lives|Subjects Under a Dynasty|How did one royal policy affect ordinary households?|Use taxation, legal, land, and community records, not court accounts alone.
power_and_institutions|Crown, Council, and Assembly|Who could make or block one decision under a named ruler?|Compare legal authority, actual practice, and institutional conflict.
trade_and_exchange|Royal Revenue and Markets|How did one dynasty raise and spend resources through trade or taxation?|Trace documented flows and affected groups.
language_and_labels|What Is a Dynasty?|How do historians decide where one ruling house begins and ends?|Compare genealogy, marriage, adoption, claim, and political continuity.
maps_and_borders|Realm Versus Control|Did a royal map match the territory actually administered?|Compare charters, taxation, garrisons, and local records for a dated period.
conflicting_accounts|Rival Accounts of a Reign|Why do court and opposition sources depict one ruler differently?|Compare provenance, audience, censorship, and independent evidence.
preservation_bias|The Archive Favors the Court|Whose voices are missing from royal collections?|Identify survival and access limits and seek local or noncourt records.
turning_point_test|A Marriage or Coronation Tested|Did one royal event actually alter power or policy?|Compare authority, alliances, revenue, and subsequent acts before and after.
legacy_and_memory|How a Dynasty Is Remembered|Who shaped one dynasty's memorial image and who disputes it?|Compare monuments, textbooks, archives, and living community perspectives.
field_strategic_choices|A Succession Decision|Which options did royal advisers consider during one documented crisis?|Use correspondence and institutional constraints without claiming private thoughts.
field_civilian_experience|Life Under Dynastic Change|What changed for residents when a ruling house changed?|Compare local law, taxes, conflict, and testimony in a bounded place.
field_logistics|Moving a Royal Court|What transport, provisioning, and staffing made one court move possible?|Use household accounts, route records, and local burdens.
field_leadership_claims|Testing a Ruler's Reputation|Does evidence support one ruler's label as reformer or tyrant?|Compare specific policies, outcomes, source bias, and affected groups.
field_aftermath|After the Dynasty|Which institutions and social arrangements survived its end?|Trace law, property, personnel, and memory over a defined period."""


if __name__ == "__main__":
    revise_domain("035", "035_military_history", MILITARY,
                  "Military institutions and conflicts through dated records, capacity, logistics, civilian experience, competing accounts, and aftermath.",
                  "orders and unit diaries, maps and operational records, service and casualty records, artifacts, official investigations, local archives, and consented civilian or veteran accounts",
                  "Attribute claims by side and date, protect private people, avoid glorifying harm or giving actionable tactics, and include civilian effects and archival gaps.")
    revise_domain("036", "036_royalty_dynasties", DYNASTIES,
                  "Dynastic rule through succession, institutions, revenue, household labor, territory, subjects' lives, and contested memory.",
                  "charters and legal acts, chronicles, royal and state archives, correspondence, household accounts, coins and seals, local tax or court records, and critical translations",
                  "Distinguish legal claim, ceremony, and effective control. Treat genealogies and court chronicles as situated sources, protect living people, and seek voices beyond the palace.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
