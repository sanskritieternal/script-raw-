"""Editorial question designs for practical digital and consumer protection."""

from review_angle_plans import audit, revise_domain


SAFETY = """history_origins|Personal Digital Safety over Time|Which threats changed as everyday services moved online?|Use dated incident evidence.
famous_examples|A Documented Account Compromise|What entry point and recovery sequence are verified?|Use consented or public records.
hidden_stories|Support after a Digital Incident|Who helps people recover accounts and money?|Trace institutional response.
beginner_explainers|Core Personal Safety Habits|How do updates, unique passwords, MFA, and phishing checks address different risks?|Use CISA guidance.
advanced_concepts|Risk-Based Account Protection|Why do account value and recovery options alter priorities?|Model one person's threat surface.
mysteries_unsolved_cases|A Suspicious Message|Which independent checks distinguish fraud from legitimate contact?|Avoid opening unknown links.
technology_innovation|Passkeys and Authentication|Which attacks can a specific sign-in method reduce?|State device and recovery limits.
people_personalities|A Survivor's Recovery Story|What barriers did a person face after a scam?|Use consent, no blame.
major_events|A Platform Security Change|Did a dated update reduce a known weakness?|Use vendor and incident evidence.
how_it_works|From Phish to Account Takeover|What broad stages explain the harm and defense?|Keep non-operational.
rise_fall|A Safety Feature's Adoption|Which usability or access issue limited uptake?|Use population data.
then_vs_now|Old and New Scam Channels|How did contact methods and defenses change?|Compare case types.
future_developments|Emerging Digital Safety Risks|What evidence supports a new threat claim?|Avoid panic forecasting.
myths_vs_facts|MFA Makes an Account Invulnerable?|Which residual risks remain and which forms work better?|Use current guidance.
documentary_stories|One Incident's Recovery Timeline|How were access, reporting, and follow-up handled?|Use verified record.
system_boundary|Which Devices and Accounts Matter?|What is included in one person's digital safety plan?|Map dependencies.
input_output_trace|A Login and Recovery Journey|Where do credentials, codes, and identity checks go?|Use safe conceptual diagram.
design_tradeoff|Security and Access|How do strong controls affect people with shared or lost devices?|Test varied users.
failure_mode|When Recovery Fails|What happens if an email or phone number is compromised?|Plan alternate recovery.
testing_limits|Limits of a Security Claim|What does a product test cover and omit?|Read scope and date.
standards_interoperability|Moving to a Safer Login|Can accounts and devices support a portable option?|Check compatibility.
security_threat_model|Threats to an Everyday Account|Which attacker goals and likely paths matter for this user?|Prioritize proportionately.
maintenance_lifecycle|Device Support Ends|What protection is lost when updates stop?|Check vendor support dates.
infrastructure_dependencies|Safety during an Outage|Can people recover or contact help when networks fail?|Test fallback channels.
accessibility_usability|Accessible Security Controls|Can disabled and older users complete setup and recovery?|Use inclusive testing.
independent_replication|Checking a Safety Tip|Do trusted sources agree it reduces a defined risk?|Compare CISA and platform guidance.
responsible_deployment|A Service's Safer Defaults|Which settings protect users without requiring expertise?|Review design and outcomes.
field_attack_surface|Personal Exposure Map|Which accounts, devices, and sharing settings create risk?|Use voluntary inventory.
field_data_protection|What Information Can Be Lost?|Which data are stored, shared, or backed up?|Check settings and policy.
field_incident_response|First Steps after Compromise|Which official reporting and recovery route fits the incident?|Name jurisdiction and service.
field_identity_controls|Identity and Recovery Options|Who can reset the account and how is that verified?|Inspect current settings.
field_security_usability|A Safety Step People Can Keep|Does a measure work in daily life and during device loss?|Test realistic scenario.
"""

RIGHTS = """history_origins|Consumer Protection Rules Develop|Which problem prompted a named rule in one jurisdiction?|Use dated primary law.
famous_examples|A Resolved Consumer Dispute|What purchase terms and remedy were documented?|Use official case record.
hidden_stories|People Unable to Claim a Remedy|Who faces language, transport, or proof barriers?|Use complaint and access evidence.
beginner_explainers|A Consumer's Purchase Record|Which receipt, contract, warranty, and advertisement matter?|Use a concrete transaction.
advanced_concepts|Express and Implied Claims|How can wording and omission shape a reasonable buyer's understanding?|Use regulator examples.
mysteries_unsolved_cases|A Denied Refund|Which policy, law, and evidence determine the actual right?|Name place and date.
technology_innovation|Digital Complaint Tools|Do online portals improve resolution for all users?|Compare access and outcomes.
people_personalities|A Buyer's Experience|What happened from purchase through complaint?|Use consent and records.
major_events|A Consumer Rule Changes|Which purchases are covered before and after the change?|Read effective date.
how_it_works|From Problem to Remedy|How do seller contact, documentation, escalation, and decision connect?|Use local official route.
rise_fall|An Enforcement Action|Did a regulator's order change business conduct?|Compare terms and outcomes.
then_vs_now|Consumer Rights across Channels|How do in-store, online, and marketplace purchases differ?|Check current jurisdiction.
future_developments|New Consumer Problems|Which current disputes might require better rules?|Use complaint trends, not forecasts.
myths_vs_facts|Every Purchase Has a Return Right?|Which seller policy and law actually apply?|Avoid universal rule.
documentary_stories|One Complaint's Evidence Trail|How did buyer, seller, and agency interpret the facts?|Use dated documents.
value_chain|Who Sold and Supplied It?|Which entity owes which remedy in this transaction?|Map contract and platform role.
incentive_map|Why Make a Misleading Claim?|Which sales incentives and enforcement risks matter?|Use documented practice.
unit_economics|Cost of a Remedy|How do refund, repair, and replacement costs affect seller behavior?|Use bounded example.
consumer_outcome|Was the Problem Resolved?|Did the buyer actually receive the promised remedy?|Track time and result.
market_structure|Platform versus Seller|Who controls listing, payment, and complaint process?|Inspect terms.
risk_transfer|Fine Print and Buyer Risk|Which terms move cost or burden to the consumer?|Check enforceability locally.
regulatory_choice|Which Authority Can Help?|How do sector and jurisdiction direct a complaint?|Use official agency map.
historical_shock|A Crisis Exposes Rights Gaps|How did a documented disruption affect delivery or refunds?|Compare cases.
data_definition|Counting Consumer Complaints|What does a complaint total measure and omit?|Use denominator and duplicates.
access_and_affordability|Access to a Remedy|Do fees, time, and language block a valid claim?|Measure practical burden.
business_failure|If the Seller Closes|What remedies remain through payment, manufacturer, or regulator?|Check current terms.
long_term_tradeoff|Cheap Product, Weak Support|How does short purchase price compare with repair and lifetime cost?|Use actual terms.
field_supply_chain|Tracing the Responsible Company|Which seller, importer, and maker handled the product?|Use invoice and labels.
field_brand_claims|Evidence behind an Advertisement|What substantiation supports an objective claim?|Use FTC standard and records.
field_customer_experience|The Complaint Journey|How many steps and days did resolution take?|Observe varied buyers.
field_market_entry|New Seller Obligations|What must a small entrant disclose or honor?|Name market and date.
field_product_lifecycle|Rights after Purchase|How do warranty, repair, updates, and disposal obligations change?|Trace product type.
"""

RECALL = """history_origins|How Recall Systems Developed|Which safety failures changed notification practice?|Use agency record.
famous_examples|A Named Product Recall|Which model and production dates were affected?|Read current official notice.
hidden_stories|Unreached Owners|Who may miss a recall because of resale or language?|Use completion and outreach data.
beginner_explainers|Recall, Warning, or Warranty?|What does each action ask the owner to do?|Use regulator definitions.
advanced_concepts|Serial and Batch Traceability|How precisely can an affected unit be identified?|Check notice and records.
mysteries_unsolved_cases|Is This Unit Affected?|Which model, serial, and purchase evidence resolves uncertainty?|Use official lookup.
technology_innovation|Better Recall Notification|Do registration or digital records improve owner reach?|Test completion rates.
people_personalities|An Owner's Recall Journey|How did a person learn of the hazard and obtain remedy?|Use consented account.
major_events|A Recall Expanded|What new evidence led to more units or a changed remedy?|Compare notice revisions.
how_it_works|From Hazard Report to Remedy|How do investigation, announcement, contact, and repair connect?|Trace one case.
rise_fall|A Recall Completion Campaign|Did outreach improve actual remedy use?|Read agency and company data.
then_vs_now|Initial Notice and Later Update|What changed in affected lots or remedy?|Use dated records.
future_developments|Reducing Recall Gaps|Which registration and resale practices could help?|Use measured bottlenecks.
myths_vs_facts|Every Model Is Recalled?|Why may only a specific batch or serial range be affected?|Check notice.
documentary_stories|One Defect's Evidence Trail|How did reports, tests, notice, and remedy unfold?|Use public records.
value_chain|Who Made and Sold the Unit?|How do manufacturer, importer, and retailer share contact duties?|Map named recall.
incentive_map|Why Was a Recall Delayed?|Which documented information and incentives shaped timing?|Avoid unsupported motive.
unit_economics|Cost of Recall Remedy|How do repair, replacement, logistics, and disposal add up?|Use disclosed figures.
consumer_outcome|Did Owners Get the Remedy?|What fraction of affected units were actually addressed?|Check denominator and date.
market_structure|Marketplace and Second-Hand Sales|How do platforms notify downstream owners?|Test practical reach.
risk_transfer|Unsafe Product in the Home|Who bears hazard while a remedy is unavailable?|Examine interim advice.
regulatory_choice|Which Recall Authority Applies?|Does product type route to CPSC, NHTSA, FDA, or another body?|Name jurisdiction.
historical_shock|A Defect Pattern Emerges|What earlier reports preceded a recall?|Use dated incident data.
data_definition|Units Recalled versus Incidents|Why are these counts different?|Explain scope and reporting bias.
access_and_affordability|Obtaining a Recall Remedy|Do shipping, travel, or proof requirements exclude owners?|Check real process.
business_failure|Recall after Company Closure|Who can deliver or explain remedy if maker is gone?|Read current agency notice.
long_term_tradeoff|Repair versus Replace|How do safety, waste, and time differ?|Use remedy-specific evidence.
field_supply_chain|Locating Affected Batches|Which production and distribution records identify units?|Follow official identifiers.
field_brand_claims|Company's Safety Statement|Does it match the regulator notice and observed hazard?|Compare dated claims.
field_customer_experience|From Notice to Fix|How many steps did an owner complete?|Observe user journey.
field_market_entry|Recalled Goods in Resale|How are marketplaces and resellers informed?|Check obligations locally.
field_product_lifecycle|Risk after a Repair|Does the remedy remain effective and are new failures tracked?|Use follow-up records.
"""

if __name__ == "__main__":
    revise_domain("495", "495_digital_safety", SAFETY,
                  "Digital safety through account and device risks, usable defenses, scam verification, recovery, accessibility, and ongoing support.",
                  "CISA Secure Our World guidance, FTC consumer recovery resources, vendor security notices, incident records, and user testing",
                  "Name service, user setting, threat, and jurisdiction. Avoid victim blame or operational attack instructions; advice must fit current official guidance.")
    revise_domain("497", "497_consumer_rights", RIGHTS,
                  "Consumer rights through transaction evidence, advertising claims, warranties, seller duties, complaint routes, and practical access to remedies.",
                  "current jurisdiction-specific law and regulator guidance, FTC advertising and refund resources as US examples, contracts, complaint records, and resolved case files",
                  "Name product, seller, jurisdiction, and purchase date. Return and warranty rights vary; these prompts are not legal determinations.")
    revise_domain("498", "498_product_recalls", RECALL,
                  "Product recalls through precise affected-unit identification, official notice changes, owner reach, remedy completion, and follow-up safety.",
                  "current CPSC, NHTSA, FDA, or local regulator recall notices, serial or lot identifiers, company remedy records, and completion data",
                  "Name product, model, serial or lot, jurisdiction, and notice date. Recall status and remedies can change; verify against the live regulator notice.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
