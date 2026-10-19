"""Direct editorial review of geopolitical history and intelligence questions."""
from review_angle_plans import revise_domain, audit

GEOPOLITICS = """history_origins|Origins of a Geopolitical Arrangement|Which dated decisions created one alliance, border regime, or sphere of influence?|Read treaties, negotiations, maps, and contemporary objections.
famous_examples|A Turning Point in World Affairs|What changed after one widely cited geopolitical event?|Compare decisions, capabilities, and affected populations before and after.
hidden_stories|People Outside the Leaders' Room|Whose work or losses are missing from a familiar diplomatic history?|Use archival records and consented or published civilian accounts.
beginner_explainers|States, Interests, and Institutions|Which institutions could make and enforce a particular international decision?|Map domestic authority, treaty obligations, and practical limits in one case.
advanced_concepts|Power, Law, and Geography|How did legal obligations and material capacity shape one state's choices?|Compare official constraints, resources, alternatives, and outcomes.
mysteries_unsolved_cases|An Unresolved Diplomatic Motive|Which explanations for a decision remain plausible in the surviving record?|Separate contemporaneous documents from later memoirs and speculation.
technology_innovation|A Technology Changes Statecraft|Did one communication or transport technology alter a specific diplomatic process?|Compare timing, access, decisions, and unintended effects.
people_personalities|A Diplomat's Actual Role|What influence did one named negotiator have on a documented agreement?|Compare drafts, instructions, correspondence, and final text.
major_events|A Crisis Decision Sequence|Which decisions escalated or eased one dated international crisis?|Build a sourced timeline with each actor's position and uncertainty.
how_it_works|How an Agreement Was Reached|What steps led from proposal to ratification and implementation?|Trace domestic mandates, negotiation, signature, and compliance.
rise_fall|A Coalition Forms and Frays|Why did a named coalition gain and later lose cohesion?|Compare shared aims, institutions, public positions, and dated withdrawals.
then_vs_now|The Same Strategic Corridor in Two Eras|How did geography matter differently in two defined periods?|Compare transport, law, technology, and affected communities.
future_developments|A Proposed Regional Arrangement|What conditions would a public proposal need to work?|State assumptions and competing positions without forecasting conflict.
myths_vs_facts|A Simplified Geopolitical Story|Does a common explanation ignore a documented actor or constraint?|Test it against primary records and competing interpretations.
documentary_stories|An Agreement's Archive|What does a sequence of drafts and official messages reveal?|Explain missing records, classification, and later reinterpretation.
lived_experience|A Civilian in a Geopolitical Shift|What can one consented account show about policy's local consequences?|Pair testimony with service, migration, or economic records.
institutional_pathway|A Foreign Policy Decision's Route|Which offices and legislatures shaped one decision?|Map formal authority and documented participation in a named state.
incentives_norms|Why Allies Disagreed|Which documented interests led partners to different positions?|Use official statements and internal records without assigning hidden motives.
access_and_exclusion|Who Bore the Costs of a Policy?|Which group faced restricted movement, trade, or services?|Define group and period; compare law, implementation, and outcomes.
community_variation|One Decision, Different Local Effects|Why did two communities experience a regional policy differently?|Compare location, livelihoods, identity, and administrative access.
policy_in_practice|An International Commitment at Home|Did a government implement one treaty obligation as promised?|Compare agreement, domestic law, budget, enforcement, and monitoring.
survey_vs_story|Public Opinion and Historical Accounts|Do polling and personal accounts tell different stories about one policy?|Check sampling, question wording, timing, and whose voice is absent.
power_and_voice|Who Entered the Negotiation?|Which affected communities were represented in one settlement?|Read participant lists, consultation records, final terms, and critiques.
unintended_consequence|A Policy's Regional Spillover|What secondary effect followed a dated geopolitical decision?|Test timing and alternative causes using multiple sources.
comparative_setting|Two Agreements, Similar Aim|Why did comparable regional arrangements produce different results?|Match legal scope, enforcement, resources, and period.
change_over_time|A Diplomatic Relationship Across Decades|How did official commitments and practical cooperation change?|Track dated agreements, decisions, and measurable activity.
ethical_dilemma|Security Aim and Civilian Cost|How did decision makers account for foreseeable civilian harm?|Compare official record, applicable law, and documented effects.
field_legal_authority|Who Could Commit the State?|Which institution had authority for one treaty or security decision?|Read constitutional rules, ratification record, and legal challenges.
field_border_history|A Boundary in Diplomatic Negotiation|How did a border issue enter one wider international agreement?|Compare drafts, maps, final text, and implementation.
field_policy_implementation|Foreign Policy Meets Administration|How did domestic agencies implement one international commitment?|Trace rules, staffing, budgets, audits, and outcomes.
field_civilian_impact|Measured Civilian Effects|What happened to one population after a geopolitical measure?|Use disaggregated evidence and avoid attributing all change to one cause.
field_diplomatic_tradeoff|What Each Party Accepted|Which concessions are documented in one negotiated text?|Compare public positions, drafts, obligations, and enforcement."""

INTELLIGENCE = """history_origins|An Intelligence Service's Mandate|Why was one agency created and what authority did it receive?|Read founding law, official debates, and early oversight records.
famous_examples|A Declassified Operation in Context|What do released records establish about one famous intelligence case?|Separate agency account, independent review, and still-withheld material.
hidden_stories|Analysts Behind a Decision|Whose analytical or support work disappears in an operation's public story?|Use declassified personnel and institutional records without exposing private identities.
beginner_explainers|The Intelligence Cycle in One Case|How did a public example move from requirement to assessment and decision?|Use declassified material; distinguish assessment from policy choice.
advanced_concepts|Uncertainty in an Assessment|How did analysts express confidence and alternative hypotheses?|Compare original assessment, underlying evidence if released, and later review.
mysteries_unsolved_cases|A Case with Missing Records|Which claim about one historical operation cannot be settled from released files?|Identify gaps, redactions, disputed accounts, and what is knowable.
technology_innovation|A New Collection Tool's Limits|What changed when one intelligence technology entered service?|Use declassified history and oversight; avoid operational instructions.
people_personalities|A Leader and the Evidence|How did one named official interpret an intelligence assessment?|Compare briefing record, decision memo, and later testimony.
major_events|An Intelligence Failure Review|What did an official inquiry find after one dated failure?|Separate the event, identified causes, recommendations, and implementation.
how_it_works|Oversight of a Secret Program|Which public bodies may authorize, review, and report on one intelligence power?|Specify country, law, date, and public reporting limits.
rise_fall|A Capability's Expansion and Reform|Why did one intelligence authority expand and later change?|Trace law, public reports, oversight findings, and outcomes.
then_vs_now|An Agency Before and After Reform|Did a documented reform change oversight or practice?|Compare mandates, public statistics, audits, and their limits.
future_developments|A Proposed Oversight Reform|What would a public reform proposal change in law and accountability?|Assess stated safeguards without predicting adoption or revealing tactics.
myths_vs_facts|A Spy Story Against the Archive|Does a popular version of one case fit declassified records?|Distinguish proven findings, agency claims, memoir, and speculation.
documentary_stories|From Secret File to Public Record|How did one case become knowable through release or inquiry?|Trace original documents, declassification, redaction, and later correction.
incident_timeline|Timeline of a Documented Operation|Which public decisions and events can be dated reliably?|Use declassified chronology and mark unknown intervals.
prevention_layer|Safeguards Against Abuse|Which oversight safeguard applied to a named intelligence power?|Read law, audit findings, and available compliance measures.
response_chain|From Warning to Official Response|Who received one documented warning and what action followed?|Use public inquiry and contemporaneous records; avoid operational detail.
evidence_integrity|Provenance of a Released Record|How was one declassified document created, handled, and interpreted?|Check origin, redactions, release context, and corroboration.
victim_perspective|People Affected by Surveillance or Error|What do consented accounts show about a documented intelligence practice?|Pair testimony with legal and oversight findings and protect privacy.
system_failure|An Inquiry's Causal Findings|Which institutional conditions contributed to one documented failure?|Distinguish inquiry conclusions from later speculation.
risk_communication|Communicating Uncertain Threats|How did public officials describe uncertainty in one warning?|Compare source assessment, public wording, and later evidence.
community_trust|Intelligence Power and Public Trust|How did one documented practice affect a defined community's trust?|Use representative evidence and oversight records, avoiding unsupported generalization.
false_positive|A Mistaken Identification|What safeguards failed in one officially documented mistaken identification?|Use public case records without repeating identifying details unnecessarily.
after_action|Were Recommendations Implemented?|Which recommendations from one public review were adopted?|Compare report, legal changes, audit follow-up, and measured results.
legal_boundary|The Reach of a Surveillance Authority|What did one statute authorize at a fixed date?|Read law and published legal interpretation; avoid jurisdiction-free claims.
resilience_design|Reducing Analytical Blind Spots|What documented process change sought to improve challenge and review?|Use public inquiry findings and later assessments, not tradecraft instructions.
field_evidence_handling|An Intelligence Claim's Evidence Chain|What publicly available evidence supported one assessment?|Trace declassified sources, confidence statements, and independent findings.
field_prevention_design|Oversight by Design|How was one accountability mechanism built into a new authority?|Compare law, reporting duties, audit access, and observed compliance.
field_response_timing|Delay Between Warning and Decision|What can public records establish about one response interval?|Date messages and decisions; mark undisclosed steps.
field_public_trust|A Disclosure and Public Confidence|Did one official disclosure change measured trust or scrutiny?|Compare surveys, oversight activity, and timing with other events.
field_victim_support|Remedy After an Intelligence Error|What public remedy was available to someone harmed by a documented error?|Read applicable law, complaint pathways, outcomes, and privacy safeguards."""

if __name__ == "__main__":
    revise_domain("014", "014_geopolitics_world_history", GEOPOLITICS,
                  "Dated geopolitical decisions, legal commitments, capabilities, diplomacy, and civilian effects in historical context.",
                  "treaties, diplomatic archives, official statements, maps, legislative records, independent historical collections, and consented affected accounts",
                  "Date and attribute contested territorial or causal claims; separate official position, documented action, and scholarly interpretation. Avoid forecasts and current operational advice.")
    revise_domain("099", "099_intelligence_espionage", INTELLIGENCE,
                  "Publicly documented intelligence history, assessment uncertainty, legal powers, oversight, accountability, and affected people.",
                  "declassified records, published laws and opinions, oversight and inspector-general reports, inquiry findings, and consented affected accounts",
                  "Use only public records; mark redactions and unknowns. Separate allegation, agency claim, and independent finding; protect private identities and omit operational tradecraft.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
