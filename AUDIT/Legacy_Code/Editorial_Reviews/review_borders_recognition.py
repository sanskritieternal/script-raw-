"""Direct question-design review for borders and disputed recognition."""
from review_angle_plans import revise_domain, audit

BORDERS = """history_origins|How a Boundary Was Drawn|Which dated agreement or decision established one border segment?|Read the instrument, maps, and implementation records; distinguish delimitation from demarcation.
famous_examples|A Famous Border in Its Legal Context|What do the governing documents say about one widely discussed boundary?|Compare treaty language, later agreements, and actual administration at a fixed date.
hidden_stories|Residents of a Border Change|Whose experiences are missing from the official account of a boundary shift?|Use consented testimony and records of residence, services, and movement.
beginner_explainers|A Border Is More Than a Line|What is the difference between a claimed boundary and an administered crossing?|Explain legal line, physical markers, controls, and local use in one place.
advanced_concepts|Competing Boundary Evidence|How do a treaty, map, and long practice bear on one dispute?|Describe their different legal and historical roles without deciding the case.
mysteries_unsolved_cases|A Segment Still in Dispute|Which boundary question remains unresolved in official records?|Identify parties' positions, available evidence, and procedural status by date.
technology_innovation|Mapping a Border with New Data|Does a new survey resolve a defined boundary uncertainty?|Compare measurement precision with the governing legal instrument and local realities.
people_personalities|Negotiators Behind a Boundary|What did named negotiators decide, and what remained for later implementation?|Use minutes, drafts, final text, and subsequent records.
major_events|A Boundary Agreement Takes Effect|What changed on the ground after a dated border agreement?|Compare markers, crossings, administration, and resident rights before and after.
how_it_works|From Treaty to Border Marker|How does a legal boundary become a marked and managed border?|Trace negotiation, ratification, delimitation, demarcation, and maintenance in one case.
rise_fall|A Crossing Opens and Closes|Why did use of one border crossing change over time?|Check rules, trade, transport, conflict, public health, and counting methods.
then_vs_now|Life Across a Border in Two Periods|How did a defined community's movement change after one policy or line change?|Compare equivalent groups, routes, documents, and service access.
future_developments|A Proposed Border Arrangement|What would a pending boundary or crossing proposal have to resolve?|Identify legal authority, implementation costs, and resident effects without predicting settlement.
myths_vs_facts|A Map Claim Under Examination|Does a popular map accurately show the legal and administered boundary?|Check date, projection, source, contested status, and official instruments.
documentary_stories|A Border Dispute's Paper Trail|How did a specific border claim travel through negotiation or adjudication?|Follow filings, maps, decisions, and implementation records.
lived_experience|A Resident Near the Line|What does one consented account reveal about everyday border administration?|Pair experience with dated rules and broader evidence.
institutional_pathway|Who Manages This Border?|Which agencies set the line, manage a crossing, and hear appeals?|Name the jurisdiction and distinguish legal mandates from practice.
incentives_norms|The Incentives Behind a Crossing Rule|How did revenue, security, or service pressures shape one rule?|Use official records and measured outcomes; test alternative explanations.
access_and_exclusion|Who Cannot Cross Easily?|Which documentation, cost, disability, or language barrier affects a defined group?|Use rights standards, local rules, and disaggregated evidence.
community_variation|Two Communities on One Border|Why do nearby communities experience the same line differently?|Compare crossing locations, family ties, livelihoods, and service access.
policy_in_practice|A Border Rule at the Checkpoint|Did actual administration follow a written rule?|Compare dated guidance, oversight reports, and consented accounts.
survey_vs_story|Counting Border Crossings|What can crossing statistics and personal accounts each establish?|Explain coverage, informal movement, nonusers, and safety of interviewees.
power_and_voice|Who Had a Say in Drawing the Line?|Which residents or institutions were heard in one border decision?|Compare consultation records, final terms, and excluded groups.
unintended_consequence|A Border Change's Spillover|What unexpected effect followed one boundary or crossing change?|Trace dates, controls, trade routes, and competing causes.
comparative_setting|Two Borders with Similar Rules|Why do comparable crossing rules produce different lived outcomes?|Align legal status, geography, services, and measurement.
change_over_time|A Boundary Through Successive Agreements|How did one segment's legal description and administration evolve?|Build a dated chain of instruments, maps, and practice.
ethical_dilemma|Security and Human Rights at a Crossing|How was one documented border measure assessed against rights obligations?|Read the applicable law, decision record, and affected accounts.
field_legal_authority|Authority to Set or Alter a Line|Which body could legally decide one border issue at a named date?|Read treaty, statute, mandate, and adjudication record.
field_border_history|A Border in Historical Layers|Which earlier lines shaped a present border segment?|Compare dated maps and instruments without assuming every historical line has current force.
field_policy_implementation|A Border Policy's Rollout|How did training, facilities, and review processes affect a new rule?|Use implementation records and resident outcomes.
field_civilian_impact|Costs of a Closed Crossing|Who bore the measurable cost of one closure?|Compare travel, trade, care, and family access for defined groups.
field_diplomatic_tradeoff|A Negotiated Boundary Compromise|Which interests were balanced in one public boundary agreement?|Use negotiating record and final obligations, attributing each party's position."""

RECOGNITION = """history_origins|A Claim to Statehood Emerges|Which dated declaration or institutional change began one claim?|Read founding documents and preceding events without endorsing a sovereignty claim.
famous_examples|A Widely Discussed Recognition Dispute|What do states and international bodies actually say about one claimant?|Date each position and distinguish bilateral recognition from membership.
hidden_stories|Residents Beyond the Status Debate|Whose daily needs disappear in arguments about recognition?|Use consented accounts and documented access to services, travel, and rights.
beginner_explainers|Recognition, Membership, and Control|How do state recognition, UN membership, and effective administration differ?|Use a bounded case and quote the relevant institutions' own terminology.
advanced_concepts|Legal Status and Effective Control|What do differing legal and practical tests reveal about one claimant?|Compare applicable instruments, institutions, control, and contested interpretations.
mysteries_unsolved_cases|An Unresolved Status Question|Which formal issue remains unsettled in one status process?|Map positions, negotiations, rulings, and the limits of each record.
technology_innovation|Digital Services Under Disputed Status|How does status affect access to a named digital public service?|Compare identification, interoperability, privacy, and resident outcomes.
people_personalities|A Negotiator in a Status Process|What did one public figure propose and what was adopted?|Use dated statements, negotiation records, and implemented texts.
major_events|A Recognition Decision's Effects|What changed after one state announced a recognition decision?|Compare diplomatic relations, documents, trade, and resident access.
how_it_works|How Recognition Is Recorded|How does one state formalize and communicate recognition of another?|Trace official act, diplomatic exchange, and subsequent practice in a named case.
rise_fall|Support for a Status Claim Over Time|How did official positions toward one claimant change?|Build a dated list of state decisions and avoid inferring motives from counts alone.
then_vs_now|Status and Daily Administration|What changed for residents across two dated phases of a status dispute?|Compare documents, services, movement, and institutions.
future_developments|A Pending Status Proposal|What would one public proposal require from the parties and institutions?|Describe contingencies and rights protections without predicting recognition.
myths_vs_facts|Does UN Membership Equal Recognition?|Does a common claim confuse UN admission with states' recognition decisions?|Check UN rules and the specific diplomatic record.
documentary_stories|A Status Claim in Documents|How did a declaration become a sustained diplomatic question?|Follow official texts, responses, negotiations, and any relevant judgments.
lived_experience|Living with Disputed Status|What does one consented resident's account reveal about administrative barriers?|Pair testimony with dated documents and protect identity where needed.
institutional_pathway|Who Governs What?|Which institutions actually administer one service in a disputed area?|Map formal claims, effective control, and service delivery by date.
incentives_norms|Why States Take Different Positions|What public reasons do states give for differing recognition decisions?|Compare official statements with documented interests, without assigning hidden motives.
access_and_exclusion|Documents and Mobility|Which people struggle to obtain recognized travel or civil documents?|Use rules, acceptance records, and affected voices in a fixed period.
community_variation|Different Experiences Within One Territory|How do communities experience status and governance differently?|Compare place, identity, service access, and safety with care.
policy_in_practice|An Agreement's Local Effect|Did a status-related agreement change administration on the ground?|Compare text, rollout, monitoring, and resident outcomes.
survey_vs_story|Measuring Public Preferences|What can surveys and interviews establish about residents' status preferences?|Check sampling, wording, fear of disclosure, and representation.
power_and_voice|Who Participated in Status Talks?|Which affected groups had a voice in one formal process?|Compare delegates, consultation, final text, and omissions.
unintended_consequence|A Recognition Move's Spillover|What secondary effects followed a dated diplomatic decision?|Track trade, services, movement, and alternative causes.
comparative_setting|Two Status Disputes Compared|Which institutions and histories make two recognition cases comparable?|Align legal instruments, control, diplomatic positions, and residents' circumstances.
change_over_time|A Recognition Timeline|How did formal positions and effective administration change over decades?|Date official acts separately from observed governance.
ethical_dilemma|Status Policy and Resident Rights|How did one status decision balance diplomatic aims with rights and services?|Use legal obligations, decision records, and affected perspectives.
field_legal_authority|Who Can Grant Recognition?|Which authority made a specific recognition decision?|Read constitutional rules and official act; distinguish UN membership decisions.
field_border_history|Lines Around a Disputed Area|Which dated instruments and practices define the area's claimed boundaries?|Attribute competing claims and show uncertainty in maps.
field_policy_implementation|A Status Agreement at Work|What changed in local agencies after one published agreement?|Compare formal mandate, staffing, records, and complaints.
field_civilian_impact|The Cost of Uncertain Status|Which resident burdens can be documented in one service pathway?|Measure documentation, travel, benefits, or trade access with consent.
field_diplomatic_tradeoff|Conditions in a Recognition Debate|What conditions did parties publicly attach to one diplomatic decision?|Compare official statements and subsequent actions without treating forecasts as facts."""

if __name__ == "__main__":
    revise_domain("235", "235_borders", BORDERS,
                  "Border formation, evidence, administration, crossing access, resident effects, and rights obligations.",
                  "dated treaties and statutes, official boundary maps, court decisions, crossing rules, oversight reports, and consented resident accounts",
                  "Attribute competing territorial claims and date every map; distinguish legal delimitation, demarcation, and effective administration. Verify current rules and protect vulnerable interviewees.")
    revise_domain("238", "238_unrecognized_countries", RECOGNITION,
                  "Claims to statehood, bilateral recognition, international membership, effective governance, and residents' lives.",
                  "official recognition acts and statements, UN membership records, applicable legal instruments, institutional data, and consented resident accounts",
                  "Attribute sovereignty claims and avoid treating recognition as a universal binary. Separate a state's diplomatic act, UN membership, legal arguments, and effective control; date all positions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
