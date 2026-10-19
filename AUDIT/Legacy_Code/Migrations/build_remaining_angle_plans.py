"""Seed missing niche angle plans from field lenses; never overwrite an edited plan.

The resulting plans are editorial drafts. They contain research questions, not claims.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "REGISTRY"

FAMILY_CATEGORIES = {
    "history": "Ancient_Civilizations Conflict_Power_Exploration Cultural_Heritage Historical_People_Cultures",
    "technical": "Computing_Software Cybersecurity_Digital_Systems Energy_Industry Engineering_Inventions Robotics_AI Transport_Engineering",
    "natural": "Earth_Environment Life_Biology Math_Scientific_Methods Physical_Sciences Space_Astronomy",
    "creative": "Craft_Making Fiction_Worldbuilding Film_Production Food_Fashion Games_Puzzles Literature_Performance Performance_Magic Visual_Arts_Crafts",
    "social": "Careers_Workplace Childhood_Family Government_Geopolitics Home_Living Media_Formats_People People_Communities",
    "economic": "Commerce_Industry",
    "finance": "Finance_Banking",
    "education": "Learning_Education",
    "safety": "Crime_Safety_Public_Services",
    "religious": "Hindu_Traditions Philosophy_Spirituality World_Religions",
    "spatial": "Geography_Places Hospitality_Travel_Systems Land_Outdoor Sports_Adventure Travel_Experiences",
    "health": "Medicine_Healthcare Mind_Wellness",
    "futures": "Future_Worlds_Systems Human_Futures Speculative_Stories",
}

CONTEXT = {
    "history": ("a named source, object, or event", "primary records, material evidence, and attributed scholarship", "Do not turn uncertainty or tradition into an unsupported historical fact."),
    "technical": ("a defined system or deployment", "design documents, measurements, standards, and independent tests", "Separate a demonstration from reliable performance in actual use."),
    "natural": ("a defined organism, process, place, or observation", "peer-reviewed studies, field observations, and measurement methods", "State sample limits and avoid turning correlation into causation."),
    "creative": ("a named work, maker, or creative process", "the work itself, creator records, and documented audience or production context", "Separate artistic interpretation from claims about creator intent."),
    "social": ("a bounded community, institution, or lived case", "public records, participant accounts, and relevant research", "Avoid treating one person's experience as universal."),
    "economic": ("a defined product, market, institution, or transaction", "primary financial or policy records and clearly dated data", "Explain incentives and risks without presenting a planning angle as financial advice."),
    "religious": ("a named text, community, practice, or interpretation", "identified texts, translations, practitioner accounts, and scholarship", "Distinguish belief, source tradition, and independently verifiable history."),
    "spatial": ("a defined route, place, event, or outdoor practice", "maps, local records, site information, and firsthand accounts", "Check access, season, rights, and local context before recommending travel or activity."),
    "health": ("a defined health claim, care pathway, or lived experience", "clinical guidance, systematic reviews, and clearly scoped patient accounts", "Do not turn an episode prompt into diagnosis or treatment advice."),
    "futures": ("a stated scenario with explicit assumptions", "current technical evidence, constraints, and competing forecasts", "Label speculation and avoid presenting a forecast as an established outcome."),
    "finance": ("a defined household, product, institution, or historical period", "dated product terms, public financial records, and independently sourced data", "Explain risk and uncertainty without giving individualized financial advice."),
    "education": ("a defined learner, lesson, or knowledge task", "curriculum sources, learning research, and observed learner work", "Separate a teaching aid from a verified fact about every learner."),
    "safety": ("a documented incident, risk, or response system", "official records, qualified analysis, and consented accounts", "Protect victims and avoid actionable instructions for wrongdoing."),
}

BASE = [
    ("history_origins", "Origins and Development of {niche}", "Trace one source-backed beginning or early turning point, then show how the area changed without assuming a single origin.", "What evidence explains an early turning point in {niche}?"),
    ("famous_examples", "A Defining Example of {niche}", "Choose one widely cited example, explain why it became prominent, and test what it actually demonstrates.", "What does a well-known example of {niche} really show?"),
    ("hidden_stories", "Overlooked Work Behind {niche}", "Recover a documented contribution or neglected case and explain why usual summaries leave it out.", "Whose work or experience is missing from a familiar account of {niche}?"),
    ("beginner_explainers", "The Essentials of {niche}", "Define one foundational idea through a concrete case, then mark what a beginner's model leaves out.", "What must a newcomer understand first about {niche}?"),
    ("advanced_concepts", "A Hard Problem in {niche}", "Unpack a specific difficult question, its competing explanations, and the evidence that could distinguish them.", "Which hard question in {niche} remains open, and why?"),
    ("mysteries_unsolved_cases", "Unresolved Questions in {niche}", "Start with a genuine source or measurement gap; compare plausible explanations and label speculation.", "What remains unresolved in a documented case of {niche}?"),
    ("technology_innovation", "Methods and Tools Shaping {niche}", "Examine one method or tool that changed the field, including what it enabled and what it did not.", "Which method changed how people work with {niche}?"),
    ("people_personalities", "People and Communities Shaping {niche}", "Follow a documented choice by a person or group and trace its consequences without reducing the field to a hero story.", "Who made a consequential choice in {niche}, and what followed?"),
    ("major_events", "A Turning Point in {niche}", "Reconstruct a bounded event, its immediate context, and the later change for which evidence exists.", "Why did one event become a turning point in {niche}?"),
    ("how_it_works", "How One Case in {niche} Works", "Follow one case step by step, naming inputs, actors, decisions, and where uncertainty enters.", "What actually happens in a specific case of {niche}?"),
    ("rise_fall", "Growth, Setback, and Change in {niche}", "Trace one documented rise and setback while testing rival explanations rather than assuming an inevitable cycle.", "What caused a rise or reversal in a case of {niche}?"),
    ("then_vs_now", "{niche} Across Time", "Compare two dated cases with the same criteria and account for changes in evidence and definitions.", "What has genuinely changed in {niche} over time?"),
    ("future_developments", "The Next Questions for {niche}", "Build conditional scenarios from present evidence and explicit constraints instead of predicting one outcome.", "Which conditions would shape the next development in {niche}?"),
    ("myths_vs_facts", "Claims, Sources, and Evidence in {niche}", "Choose one circulating claim, identify its source, test supporting evidence, and state what remains uncertain.", "How well does the evidence support a popular claim about {niche}?"),
    ("documentary_stories", "One Documented Story from {niche}", "Follow a specific case from context through decisions and consequences using traceable sources.", "What does one well-documented story reveal about {niche}?"),
]

FAMILY_LENSES = {
    "history": """source_trail|The Source Trail|Trace the earliest attested account and later retellings; identify where evidence changes.|How did the account of one case in {niche} develop?
material_evidence|Objects and Physical Evidence|Use a dated object or site to test a specific interpretation without making it speak beyond the record.|What can one physical source establish about {niche}?
chronology_dispute|The Chronology Problem|Lay out proposed dates, their methods, and why specialists disagree.|Which dates in a case of {niche} are secure or disputed?
ordinary_lives|Everyday Experience|Reconstruct one ordinary role or practice from records that rarely center elites.|What can sources reveal about everyday life in {niche}?
power_and_institutions|Power and Institutions|Show how an institution shaped a particular decision and whose account survives.|How did an institution shape a turning point in {niche}?
trade_and_exchange|Routes of Exchange|Follow a traceable good, idea, or person across places and identify evidence of contact.|What evidence shows exchange in a case of {niche}?
language_and_labels|Words Used Then and Now|Compare historical terms with modern labels and explain where translation distorts the case.|How do changing labels affect a story about {niche}?
maps_and_borders|A Changing Map|Compare maps or geographic descriptions from different moments and test what changed on the ground.|How did place and boundaries shape a case of {niche}?
conflicting_accounts|Conflicting Witnesses|Put two attributed accounts side by side and test what each could know.|Why do sources disagree about one event in {niche}?
preservation_bias|What Survived the Archive|Examine which sources were preserved, lost, or never recorded and how that skews the narrative.|Whose perspective is missing from the record of {niche}?
turning_point_test|Was It Really a Turning Point?|Compare conditions before and after a claimed turning point using consistent criteria.|Did one event actually transform {niche}?
legacy_and_memory|History and Later Memory|Distinguish a documented event from how later communities commemorated or retold it.|How did memory reshape a case from {niche}?""",
    "technical": """system_boundary|Where the System Begins and Ends|Draw the components and external dependencies of one deployment before judging its performance.|What must be included to understand a system in {niche}?
input_output_trace|From Input to Output|Follow one input through processing, handoffs, and checks to a measurable output.|Where do errors enter a workflow in {niche}?
design_tradeoff|The Design Tradeoff|Compare two feasible designs against the same goal, cost, and constraint.|Which tradeoff governs a design choice in {niche}?
failure_mode|How a Failure Happens|Reconstruct one documented failure from mechanism to detection and response.|What failed first in a case of {niche}?
testing_limits|What a Test Really Measures|Examine a benchmark or test setup, its sample, and its relationship to real use.|Does a common test predict performance in {niche}?
standards_interoperability|Standards and Compatibility|Explain how one standard coordinates independent components and where compatibility breaks.|What changes when systems in {niche} must interoperate?
security_threat_model|A Specific Threat Model|Name an asset, adversary, pathway, and mitigation for a bounded technical case.|Which threat matters most for one system in {niche}?
maintenance_lifecycle|After Launch|Trace upkeep, upgrades, failures, and retirement rather than stopping at a product announcement.|What does long-term operation of {niche} require?
infrastructure_dependencies|Hidden Infrastructure|Map energy, network, materials, labor, or facilities behind one apparently simple service.|What infrastructure makes a case of {niche} possible?
accessibility_usability|Usability and Access|Compare how different users encounter the same design and where barriers arise.|Who cannot use a current approach in {niche}, and why?
independent_replication|Can the Result Be Repeated?|Check whether methods, inputs, and evaluation are sufficient for independent verification.|Can a reported result in {niche} be reproduced?
responsible_deployment|Deployment and Accountability|Follow who decides, monitors, remedies harm, and can stop a system in use.|Who is accountable when a deployment in {niche} goes wrong?""",
    "natural": """observation_to_explanation|From Observation to Explanation|Trace a measured pattern through competing mechanisms and the test that separates them.|What could explain a documented pattern in {niche}?
measurement_method|How We Measure It|Explain instruments, sampling, calibration, and the uncertainty around one result.|How reliable is a commonly cited measurement in {niche}?
scale_and_timespan|Scale Changes the Answer|Compare the same process at two spatial or temporal scales using compatible evidence.|How does scale change a question in {niche}?
field_vs_lab|Field and Laboratory Evidence|Compare controlled studies with observations in real settings and explain their different strengths.|Why do field and lab findings differ in {niche}?
natural_variation|Variation, Not One Typical Case|Examine a range of organisms, samples, or locations rather than presenting one example as universal.|How much natural variation is hidden in a summary of {niche}?
mechanism_chain|A Mechanism Step by Step|Trace a causal sequence, identifying known steps and unresolved links.|Which step in a proposed mechanism of {niche} is least certain?
extreme_case|What an Extreme Case Teaches|Use one bounded extreme to test the limits of a general explanation.|What does an extreme case reveal about {niche}?
classification_debate|How Categories Are Defined|Compare two classification schemes and the evidence each emphasizes.|Why do experts classify a case in {niche} differently?
interacting_systems|Connected Processes|Map how two processes influence each other without claiming simple one-way causation.|Which interacting processes shape an outcome in {niche}?
data_gap|The Missing Data|Identify a specific gap in observations and how it limits a popular conclusion.|What key evidence is missing from a claim about {niche}?
prediction_test|A Prediction Put to the Test|State a model prediction, compare it with later observations, and examine deviations.|How well did a model predict a result in {niche}?
human_impact|Human Activity and the System|Separate measured human effects from background variation in a defined case.|What evidence links human activity to a change in {niche}?""",
    "creative": """creative_brief|The Creative Brief|Trace the goal, audience, constraints, and revisions behind one named work.|Which brief shaped a creative choice in {niche}?
materials_and_tools|Materials and Tools|Show how one material or tool enables some effects and rules out others.|How did a material choice shape a work in {niche}?
process_breakdown|From Draft to Final Work|Follow stages of making, including rejected alternatives and practical constraints.|What changed between the first and final version of a work in {niche}?
composition_choice|A Formal Choice|Analyze one choice of structure, rhythm, image, language, or interaction in its complete context.|How does one formal decision affect the experience of {niche}?
collaborative_authorship|Who Made the Work?|Identify roles, credit, and decision rights across a collaborative production.|Whose contribution is obscured in a case of {niche}?
adaptation_across_media|Adaptation Across Media|Compare a named source and adaptation, focusing on changes demanded by the new medium.|What did an adaptation of {niche} gain or lose?
audience_reception|Audience and Reception|Compare documented responses from distinct audiences without claiming a universal reaction.|Why did audiences interpret a work in {niche} differently?
cultural_context|A Work in Its Cultural Context|Situate one work or practice in the community and period that shaped it.|What context changes how a work in {niche} should be read?
preservation_restoration|Keeping a Work Alive|Trace the evidence and choices involved in conserving, restoring, or remaking a work.|Which restoration choice changes a case of {niche}?
rights_and_attribution|Rights and Attribution|Examine permissions, copying, credit, and contested ownership in one documented case.|Who can use or claim a work in {niche}?
style_comparison|Two Styles, One Task|Compare two makers solving the same creative problem with clear criteria.|How do different styles solve a shared problem in {niche}?
creative_failure|A Choice That Did Not Work|Study a documented abandoned approach and what it reveals about constraints, not merely taste.|Why did one creative approach in {niche} fail?""",
    "social": """lived_experience|A Lived Experience in Context|Center a consenting person's account and connect it to wider evidence without universalizing it.|What does one account reveal and not reveal about {niche}?
institutional_pathway|Through an Institution|Follow the rules, staff decisions, and handoffs affecting one person's or group's outcome.|Where does an institution shape experience in {niche}?
incentives_norms|Incentives and Norms|Compare stated rules with the incentives and informal norms observed in a bounded setting.|Why do people act differently from the formal rules in {niche}?
access_and_exclusion|Who Can Participate?|Identify practical, financial, language, or physical barriers and how they are measured.|Who is excluded from a process in {niche}?
community_variation|Different Communities, Different Outcomes|Compare two named communities while accounting for context and avoiding stereotypes.|Why do experiences of {niche} vary across communities?
policy_in_practice|Policy on the Ground|Trace a policy from its stated aim to implementation and documented outcomes.|Did a policy change everyday experience in {niche}?
survey_vs_story|Numbers and Narratives|Put population-level data beside individual accounts and explain what each can establish.|Where do statistics and stories disagree about {niche}?
power_and_voice|Who Gets Heard?|Map whose testimony counts in a decision and who has the power to respond.|Who shapes the public account of {niche}?
unintended_consequence|An Unintended Effect|Follow a well-intended decision through a documented secondary outcome.|What unexpected effect followed a change in {niche}?
comparative_setting|Same Question, Two Settings|Use the same criteria to compare institutions or communities in distinct settings.|What changes when {niche} is organized differently?
change_over_time|A Social Pattern Over Time|Compare dated evidence without assuming a smooth trend or a single cause.|What changed in a documented pattern of {niche}?
ethical_dilemma|A Real Decision Dilemma|Present competing responsibilities in one case and identify whose interests are at stake.|Why is one decision in {niche} difficult to judge?""",
    "economic": """value_chain|Follow the Value Chain|Trace inputs, labor, pricing, distribution, and final users for one bounded case.|Where is value created and captured in {niche}?
incentive_map|Who Has Which Incentive?|Map incentives of firms, workers, customers, and regulators in a documented decision.|Which incentive drives a surprising outcome in {niche}?
unit_economics|One Unit of the Business|Reconstruct costs and revenue for a clearly defined unit with dates and assumptions.|What must be true for one unit of {niche} to work economically?
consumer_outcome|What the Customer Receives|Compare marketing claims, contract terms, actual delivery, and complaints in one case.|Does a product or service in {niche} deliver what buyers expect?
market_structure|Competition and Concentration|Identify participants, market boundaries, and the evidence behind a concentration claim.|How does market structure affect a case of {niche}?
risk_transfer|Who Carries the Risk?|Trace how a contract, product, or decision shifts downside risk among participants.|Who absorbs a loss in a case of {niche}?
regulatory_choice|A Rule and Its Effects|Examine a dated rule, intended outcome, implementation, and documented tradeoffs.|What changed after a rule affected {niche}?
historical_shock|A Shock to the System|Follow one supply, demand, policy, or financial shock through a bounded market.|How did a shock travel through {niche}?
data_definition|What the Number Measures|Audit definitions, sources, time period, and exclusions behind one headline metric.|Is a common number about {niche} comparable over time?
access_and_affordability|Who Can Afford Access?|Compare costs and access for defined groups using dated data, not anecdotes alone.|Who is priced out of a part of {niche}?
business_failure|Why a Model Failed|Separate demand, execution, financing, and external conditions in one documented collapse.|Which factor best explains a failure in {niche}?
long_term_tradeoff|Short-Term Gain, Long-Term Cost|Trace a decision across a stated time horizon and identify who benefits or pays later.|What long-term cost follows a short-term gain in {niche}?""",
    "religious": """text_source|A Teaching in Its Source|Read a named passage in its wider text and compare at least one responsible translation.|What does the source actually say about a question in {niche}?
interpretive_lineages|Different Interpretive Traditions|Compare two named interpretations with attribution and historical context.|Why do communities read a question in {niche} differently?
lived_practice|Practice as Lived|Document one community's practice with consent and avoid presenting it as universal.|How is a practice in {niche} lived in one community?
ritual_sequence|The Meaning of a Ritual Step|Explain one step in a documented ritual through participant accounts and source traditions.|Why does one ritual step matter in {niche}?
language_translation|A Word Across Languages|Compare how a key term is rendered and what each choice emphasizes.|What is lost when a term in {niche} is translated?
regional_variants|A Regional Tradition|Study a named local tradition on its own terms and trace its relation to wider narratives.|What is distinctive about one regional form of {niche}?
art_and_devotion|Meaning Through Art|Examine a named image, song, or performance with its community and interpretive context.|How does art communicate a meaning in {niche}?
community_memory|How a Community Remembers|Trace how a story or practice is transmitted across generations in a named setting.|What changes as a community passes on {niche}?
ethics_in_context|An Ethical Question in Context|Present a teaching and competing applications without flattening them into one rule.|How do interpretations of {niche} approach one ethical dilemma?
source_and_history|Tradition and Historical Evidence|Separate what a tradition recounts from what independent records can establish.|Which claims about {niche} are textual, devotional, or historical?
encounter_and_exchange|Traditions in Contact|Study a documented encounter and distinguish exchange from forced equivalence.|What changed when a form of {niche} met another tradition?
contemporary_voice|A Present-Day Voice|Center a consenting practitioner's account alongside other sources and internal diversity.|How does one practitioner describe the meaning of {niche} today?""",
    "spatial": """map_vs_ground|The Map and the Ground|Compare mapped routes or boundaries with conditions reported on site.|What does a map miss about a case of {niche}?
route_choices|Why This Route?|Compare routes by distance, access, risk, cost, and local impact using current data.|Why do people choose one route in {niche} over another?
seasonality|The Seasonal Difference|Compare the same place or activity across seasons with dated local evidence.|How does season change a case of {niche}?
local_voice|A Place Through Local Voices|Use attributed accounts from residents or workers rather than a visitor-only view.|How do local people describe a place central to {niche}?
landscape_process|How the Landscape Formed|Explain one geographic or human process visible in a defined place.|Which process shaped a landscape in {niche}?
accessibility|Who Can Reach It?|Check physical, legal, financial, and cultural access to one place or activity.|Who cannot easily take part in {niche}, and why?
infrastructure|The System Behind the Experience|Trace transport, services, labor, or maintenance supporting a destination or activity.|What infrastructure makes a case of {niche} possible?
environmental_pressure|Use and Environmental Cost|Measure one documented environmental pressure with local context and competing needs.|What environmental cost comes with a part of {niche}?
safety_decision|A Safety Decision|Reconstruct one decision under changing conditions using official guidance and observed constraints.|Which information matters most for a safe choice in {niche}?
place_history|A Place Before the Present|Trace a place's changing uses and names with local records and living memory.|How did a place connected to {niche} acquire its current role?
comparison_of_places|Two Places, Same Question|Compare two places using consistent criteria while explaining different histories.|Why do two places associated with {niche} offer different experiences?
responsible_access|Visitor and Community Tradeoffs|Identify who gains and who bears costs when access or tourism expands.|How can access to a place in {niche} affect its community?""",
    "health": """claim_evidence|A Health Claim Under Review|Define population, intervention or exposure, outcome, and quality of evidence for one claim.|How strong is the evidence for a claim in {niche}?
care_pathway|A Journey Through Care|Map decisions, referrals, delays, and communication in a bounded care pathway.|Where do people face the largest barrier in {niche}?
benefit_harm|Benefits and Harms Together|Compare measured benefits, adverse effects, and uncertainty for a defined population.|What tradeoffs appear in evidence about {niche}?
mechanism_vs_outcome|Mechanism Is Not Outcome|Explain a proposed mechanism and test whether patient outcomes support the inference.|Does a plausible mechanism in {niche} lead to measured benefit?
population_difference|For Whom Does It Apply?|Check who was included in a study and whether findings generalize to another group.|Whose experience is missing from research on {niche}?
quality_of_guidance|How Guidance Is Made|Trace evidence reviews, expert judgment, revisions, and conflicts in a named guideline.|Why did guidance related to {niche} change?
access_to_care|Access and Affordability|Compare documented barriers by location, cost, language, or disability.|Who has difficulty accessing support in {niche}?
patient_experience|Lived Experience and Evidence|Pair consenting accounts with population evidence while protecting privacy and avoiding generalization.|What does one person's experience illuminate about {niche}?
misinformation_path|How a Claim Spread|Trace a specific unsupported claim through its sources and corrections without amplifying instructions for harm.|Why did a misleading claim about {niche} persist?
prevention_boundary|What Prevention Can Do|Separate established preventive measures, uncertain proposals, and factors outside individual control.|What does evidence support for preventing a problem in {niche}?
system_pressure|A System Under Strain|Examine staffing, capacity, incentives, and patient outcomes in a defined setting.|Which system constraint shapes an outcome in {niche}?
historical_revision|When Medical Understanding Changed|Compare older and newer evidence without treating the current view as beyond revision.|What new evidence changed thinking in {niche}?""",
    "futures": """assumption_inventory|The Assumptions Behind a Scenario|List the technical, social, and economic assumptions required for one future claim.|Which assumption most changes a scenario in {niche}?
readiness_check|From Prototype to Deployment|Compare a proposed capability with current demonstrations and adoption constraints.|What remains between a concept in {niche} and real deployment?
physical_limits|Physical and Resource Limits|Test a scenario against energy, materials, time, biology, or engineering constraints.|Which physical constraint matters most for {niche}?
governance_choice|Who Sets the Rules?|Map institutions and choices that could steer or restrict a proposed future.|Who would govern a development in {niche}?
unequal_futures|Who Benefits First?|Compare access, costs, and potential harms across defined groups.|Who may be left out of a future shaped by {niche}?
scenario_pair|Two Plausible Paths|Construct contrasting scenarios from different stated assumptions without assigning false certainty.|Which assumption separates two futures for {niche}?
failure_to_launch|Why a Vision Might Stall|Examine a precedent where expectations outpaced capability or demand.|What could stop a proposed future in {niche}?
unintended_effect|A Second-Order Effect|Trace a plausible indirect consequence through a clear causal chain and label uncertainty.|What indirect effect might follow a development in {niche}?
social_adaptation|How People Might Adapt|Use historical analogies carefully to explore behavior, norms, and institutions.|How might communities adapt if a scenario in {niche} occurs?
ethical_boundary|A Hard Ethical Choice|Specify a proposed action, affected groups, and conflicting values rather than debating abstractions.|Which ethical dilemma could a future in {niche} create?
signal_vs_hype|A Signal or a Headline?|Test a claimed trend against dated evidence, base rates, and alternative explanations.|Is a supposed breakthrough in {niche} a durable signal?
reversible_steps|Decisions That Keep Options Open|Compare near-term choices for reversibility, learning value, and possible lock-in.|Which present choice would preserve options in {niche}?""",
    "finance": """product_terms|The Fine Print|Read terms, fees, eligibility, and exclusions for one product or arrangement.|Which contract term changes the real cost of {niche}?
household_cash_flow|Money In and Out|Map a realistic but clearly illustrative cash-flow case with stated assumptions.|Which cash-flow pressure matters most in {niche}?
risk_and_time|Risk Over Time|Compare outcomes across time horizons and adverse scenarios without predicting returns.|How does time change risk in {niche}?
fee_effect|The Cumulative Cost of Fees|Trace dated fees through a transparent example and show sensitivity to assumptions.|How much can fees change an outcome in {niche}?
consumer_protection|Protection and Redress|Identify disclosures, complaint routes, and limits of protection in one jurisdiction.|What protection applies in a case of {niche}?
market_vs_household|A Market Trend and a Household|Distinguish aggregate trends from the choices available to one household.|Why does a market headline not settle a decision in {niche}?
historical_policy|A Policy Through Time|Trace one dated rule change, its stated goal, and observed effects.|How did one policy change a part of {niche}?
inflation_effect|Purchasing Power|Explain a dated inflation scenario with transparent numbers and uncertainty.|How does inflation change a long-term question in {niche}?
fraud_warning|A Misleading Offer|Analyze warning signs and official records without repeating a harmful tactic as instructions.|Which claim should a consumer verify in {niche}?
comparison_method|A Fair Product Comparison|Use the same costs, risks, terms, and time horizon for two options.|What changes when options in {niche} are compared consistently?
access_gap|Who Can Use the System?|Examine eligibility, minimum balances, location, and documentation barriers.|Who has limited access to a service in {niche}?
uncertainty_range|More Than One Outcome|Present plausible ranges and the assumptions that drive them rather than one forecast.|Which assumption most changes an example outcome in {niche}?""",
    "education": """concept_sequence|What to Teach First|Map prerequisites for one clearly defined concept and test the order with learner work.|Which prerequisite blocks understanding in {niche}?
misconception|A Common Misunderstanding|Identify a documented error pattern and compare explanations that address it.|Why do learners make a specific error in {niche}?
worked_example|One Worked Example|Follow a concrete example step by step and mark where the example stops generalizing.|What does one worked example clarify in {niche}?
retrieval_practice|Remembering After the Lesson|Compare a learner's first answer with a later retrieval task, using appropriate evidence.|What helps learners recall a part of {niche} later?
feedback_design|Feedback That Changes Understanding|Examine what a learner is told after an error and whether it addresses the underlying idea.|Which feedback helps with a specific error in {niche}?
assessment_quality|What the Question Measures|Audit a quiz or task for ambiguity, difficulty, and alignment with its learning goal.|Does an assessment in {niche} measure the intended knowledge?
visual_explanation|A Diagram That Teaches|Compare two visual explanations and identify what each reveals or hides.|Which visual helps explain a concept in {niche}?
transfer_to_new_case|Can the Idea Transfer?|Test whether a learner can use a concept in a new context rather than recall one example.|Can learners apply a lesson from {niche} in a new case?
language_access|Learning Across Languages|Examine translation, terminology, and access for learners with different language backgrounds.|Which wording creates a barrier in {niche}?
learner_variation|Different Starting Points|Compare approaches for learners with different prior knowledge without labeling one group deficient.|How should a lesson in {niche} change with prior knowledge?
source_literacy|Where the Answer Comes From|Teach how to check a source, definition, or data claim relevant to the subject.|How can a learner verify a claim encountered in {niche}?
curriculum_tradeoff|Depth Versus Coverage|Compare what a course gains and loses when it chooses breadth or depth.|What deserves more time in teaching {niche}?""",
    "safety": """incident_timeline|A Verified Incident Timeline|Separate documented events, claims, and unknowns in one case while protecting affected people.|What can records establish about a case in {niche}?
prevention_layer|A Prevention Layer|Identify one intervention, its intended mechanism, and evidence of effectiveness.|Which preventive measure changes risk in {niche}?
response_chain|From Alert to Response|Follow the handoffs among witnesses, dispatch, responders, and support services.|Where did a response in {niche} gain or lose time?
evidence_integrity|Keeping Evidence Reliable|Trace collection, handling, and limits of a specific type of evidence.|What makes evidence in a case of {niche} reliable?
victim_perspective|Needs After an Incident|Center consented accounts and documented services without sensationalizing harm.|What support mattered after a case in {niche}?
system_failure|A Safeguard That Failed|Examine a documented failure of training, equipment, process, or oversight.|Which safeguard failed in a case of {niche}?
risk_communication|What the Public Was Told|Compare official warnings, uncertainty, and later corrections during one event.|How was risk communicated in a case of {niche}?
community_trust|Trust and Cooperation|Study how institutional conduct affects reporting, cooperation, and legitimacy.|What shaped trust in a response related to {niche}?
false_positive|When a Suspicion Was Wrong|Explain the harms of mistaken attribution and the checks that reduce it.|How can an investigation in {niche} avoid a false conclusion?
after_action|Learning from a Response|Compare recommendations after an incident with documented changes later.|Which lesson from a case in {niche} was actually adopted?
legal_boundary|What the Rules Allow|Identify jurisdiction, authority, privacy, and oversight in one bounded response.|Which legal boundary matters in a case of {niche}?
resilience_design|Preparing for the Next Case|Compare preparedness measures against a defined scenario and realistic resource limits.|What would improve resilience in {niche}?""",
}

OVERRIDE_FAMILY_BY_ID = {
    "017": "creative", "044": "history", "075": "spatial", "077": "health",
    "083": "creative", "093": "natural", "135": "history", "191": "natural",
    "192": "natural", "240": "spatial", "250": "creative", "253": "history",
    "254": "history", "264": "creative", "265": "creative", "266": "creative",
    "267": "creative", "276": "religious", "408": "creative", "446": "spatial",
    "447": "spatial", "448": "spatial",
}

NICHE_FOCI = {
    "039": "excavation_context,dating_methods,artifact_provenance,site_ethics,conservation_decision",
    "075": "route_traditions,sacred_access,seasonal_crowding,local_communities,visitor_infrastructure",
    "276": "ritual_architecture,regional_temple_lineage,inscription_context,patronage_history,preservation_choice",
    "447": "flag_symbolism,design_changes,sovereignty_claim,official_use,contested_flags",
    "448": "capital_relocation,planned_capitals,multiple_capitals,contested_status,government_geography",
    "500": "retirement_horizon,withdrawal_risk,pension_terms,inflation_exposure,fee_compounding",
}

# Five extra lenses per subject tag. These are intentionally broad enough to fit
# every niche in the tag, while the plan's title and field lenses narrow the case.
CATEGORY_FOCI = {
    "Ancient_Civilizations": "excavation_context,dating_methods,urban_life,trade_routes,writing_systems",
    "Careers_Workplace": "skill_signals,hiring_filters,workplace_power,career_transitions,worker_support",
    "Childhood_Family": "age_appropriate_design,caregiver_choices,play_and_learning,household_routines,child_safety",
    "Commerce_Industry": "supply_chain,brand_claims,customer_experience,market_entry,product_lifecycle",
    "Computing_Software": "software_architecture,interface_design,version_changes,open_standards,technical_debt",
    "Conflict_Power_Exploration": "strategic_choices,civilian_experience,logistics,leadership_claims,aftermath",
    "Craft_Making": "material_selection,tool_control,pattern_design,repairability,craft_lineage",
    "Crime_Safety_Public_Services": "evidence_handling,prevention_design,response_timing,public_trust,victim_support",
    "Cultural_Heritage": "community_ownership,object_provenance,living_practice,conservation_choice,cultural_translation",
    "Cybersecurity_Digital_Systems": "attack_surface,data_protection,incident_response,identity_controls,security_usability",
    "Earth_Environment": "field_sampling,land_use,weather_variability,habitat_change,restoration_evidence",
    "Energy_Industry": "energy_balance,grid_integration,material_inputs,operational_safety,lifecycle_emissions",
    "Engineering_Inventions": "prototype_testing,design_tolerance,manufacturing_method,failure_investigation,repair_path",
    "Fiction_Worldbuilding": "internal_rules,character_motivation,narrative_pacing,setting_logic,genre_expectations",
    "Film_Production": "shot_design,production_workflow,sound_choices,editing_rhythm,distribution_format",
    "Finance_Banking": "fee_structure,risk_disclosure,regulatory_protection,household_effect,market_cycle",
    "Food_Fashion": "ingredient_or_fiber_origin,making_process,cultural_context,consumer_claims,waste_and_reuse",
    "Future_Worlds_Systems": "resource_budget,habitat_design,governance_model,dependency_chain,social_inclusion",
    "Games_Puzzles": "rules_design,player_strategy,difficulty_curve,community_norms,accessibility_design",
    "Geography_Places": "map_accuracy,place_names,local_history,visitor_access,landscape_change",
    "Government_Geopolitics": "legal_authority,border_history,policy_implementation,civilian_impact,diplomatic_tradeoff",
    "Hindu_Traditions": "textual_lineage,regional_practice,translation_choice,ritual_context,community_interpretation",
    "Historical_People_Cultures": "oral_history,archive_gap,material_culture,community_memory,representation_ethics",
    "Home_Living": "space_constraints,household_cost,design_for_access,maintenance_burden,material_lifecycle",
    "Hospitality_Travel_Systems": "service_handoff,visitor_flow,staff_labor,access_and_cost,local_impact",
    "Human_Futures": "human_agency,body_and_identity,rights_framework,resource_inequality,institutional_adaptation",
    "Land_Outdoor": "land_stewardship,seasonal_conditions,skill_and_safety,resource_use,local_knowledge",
    "Learning_Education": "learner_misconceptions,lesson_sequence,assessment_design,memory_and_recall,inclusive_learning",
    "Life_Biology": "species_variation,ecological_role,experimental_model,evolutionary_history,conservation_status",
    "Literature_Performance": "textual_form,performance_choice,audience_history,translation_or_adaptation,critical_reception",
    "Math_Scientific_Methods": "proof_or_test,definition_choice,model_assumptions,counterexample,teaching_difficulty",
    "Media_Formats_People": "source_verification,story_framing,audience_measurement,platform_incentive,editorial_correction",
    "Medicine_Healthcare": "clinical_evidence,care_quality,patient_safety,health_equity,service_capacity",
    "Mind_Wellness": "measured_outcome,practice_adherence,individual_difference,stress_context,claim_limits",
    "People_Communities": "social_norms,relationship_network,group_identity,community_support,power_difference",
    "Performance_Magic": "attention_and_perception,method_history,audience_contract,rehearsal_process,ethical_presentation",
    "Philosophy_Spirituality": "concept_definition,argument_structure,lived_interpretation,translation_problem,practice_and_claim",
    "Physical_Sciences": "experimental_setup,mathematical_model,measurement_error,scale_transition,technology_application",
    "Robotics_AI": "training_or_control_data,real_world_testing,human_oversight,failure_recovery,hardware_dependency",
    "Space_Astronomy": "observation_window,instrument_limit,orbital_dynamics,mission_tradeoff,planetary_environment",
    "Speculative_Stories": "world_rule,plausibility_boundary,point_of_view,ethical_consequence,adaptation_choice",
    "Sports_Adventure": "training_method,equipment_design,rules_and_fairness,injury_prevention,event_logistics",
    "Transport_Engineering": "route_capacity,vehicle_design,maintenance_system,safety_case,construction_impact",
    "Travel_Experiences": "trip_budget,route_reliability,local_etiquette,accessibility_check,environmental_footprint",
    "Visual_Arts_Crafts": "visual_composition,material_provenance,maker_technique,conservation_problem,audience_context",
    "World_Religions": "source_tradition,lived_practice,regional_variation,translation_issue,intercommunity_contact",
}


def slugify(value):
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", value.lower())).strip("_")


def parse_lenses(block):
    result = []
    for line in block.splitlines():
        cells = line.split("|")
        if len(cells) != 4:
            raise ValueError(f"Invalid field lens: {line}")
        result.append(cells)
    if len(result) != 12:
        raise ValueError(f"Field needs 12 lenses, found {len(result)}")
    return result


def build(row, family):
    niche = row["title"]
    case, evidence, boundary = CONTEXT[family]
    entries = []
    for slug, label, scope, question in BASE:
        entries.append({"slug": slug, "angle": label.format(niche=niche),
                        "scope": f"{scope} Use {case} in {niche}; identify the source and its limits.",
                        "question": question.format(niche=niche),
                        "evidence": evidence, "boundary": boundary})
    for slug, label, scope, question in parse_lenses(FAMILY_LENSES[family]):
        entries.append({"slug": slug, "angle": f"{label}: {niche}",
                        "scope": f"{scope} Ground the episode in {case} and identify what the evidence cannot settle.",
                        "question": question.format(niche=niche),
                        "evidence": evidence, "boundary": boundary})
    for focus in NICHE_FOCI.get(row["id"], CATEGORY_FOCI[row["primary_category"]]).split(","):
        label = focus.replace("_", " ").title()
        entries.append({"slug": f"field_{focus}", "angle": f"{label}: {niche}",
                        "scope": f"Investigate {focus.replace('_', ' ')} through one bounded case in {niche}. Define the actors, process, and outcome; compare relevant sources or observations and state remaining uncertainty.",
                        "question": f"How does {focus.replace('_', ' ')} shape a documented case of {niche}?",
                        "evidence": evidence, "boundary": boundary})
    if len(entries) != 32 or len({e["slug"] for e in entries}) != 32:
        raise ValueError(f"Duplicate or incomplete angle set: {row['id']}")
    return {"niche_id": row["id"], "status": "generated_editorial_draft",
            "purpose": f"Research-led planning directions for {niche} in {row['primary_category']}. Select a specific case and verify sources before production.",
            "generation_basis": "build_remaining_angle_plans.py field lenses v1",
            "editorial_principles": ["These are candidate angles, not established facts or finished episode questions.",
                                     "Keep the 15 original slugs stable for existing project references.",
                                     "Prefer a bounded case with traceable evidence over a broad overview.", boundary],
            "angles": entries}


def main():
    category_family = {category: family for family, names in FAMILY_CATEGORIES.items() for category in names.split()}
    with (REGISTRY / "NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 500 or set(category_family) != set(CATEGORY_FOCI) or set(category_family) != {r["primary_category"] for r in rows}:
        raise ValueError("Category coverage mismatch")
    created = 0
    for row in rows:
        path = REGISTRY / "Niches" / f"{row['id']}_{row['slug']}" / "ANGLE_PLAN.json"
        if path.exists():
            continue
        family = OVERRIDE_FAMILY_BY_ID.get(row["id"], category_family[row["primary_category"]])
        plan = build(row, family)
        path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        created += 1
    print(f"Created {created} missing niche angle plans; preserved all existing plans")


if __name__ == "__main__":
    main()
