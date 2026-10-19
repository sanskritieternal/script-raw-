"""Question-design review for hospital stories and three public-safety niches."""
from review_angle_plans import revise_domain, audit

HOSPITAL = """history_origins|A Hospital's Changing Role|Which need or policy shaped one hospital's founding and later services?|Use dated charters, budgets, and service records.
famous_examples|A Celebrated Hospital Case Rechecked|What did one widely reported care case actually demonstrate?|Compare public account with consented records and independent review.
hidden_stories|The Team Behind a Patient's Care|Whose work disappears from a hospital success story?|Trace roles and handoffs without identifying private patients.
beginner_explainers|From Admission to Discharge|What happens at each handoff for one defined care pathway?|Map referral, assessment, treatment, discharge, and follow-up.
advanced_concepts|A Complex Safety Tradeoff|How did a hospital weigh two risks for a defined patient group?|Use published guidance and system-level evidence, not personal advice.
mysteries_unsolved_cases|A Hospital Outcome With Uncertain Cause|Which explanations for one reported outcome remain plausible?|Compare audit findings, case mix, and data limitations.
technology_innovation|A Hospital Tool in Practice|Did one new clinical or record system change measured outcomes?|Compare implementation, errors, access, and patient effects.
people_personalities|Who Changed Hospital Practice?|Which documented team decision changed a care process?|Use policy records, staff accounts, and outcome measures.
major_events|A Hospital Under Sudden Pressure|How did one hospital maintain or lose essential services during a shock?|Use dated staffing, demand, supply, and patient-safety data.
how_it_works|A Hospital Handoff Step by Step|Which information and responsibility move between two teams?|Use a published pathway and anonymized process evidence.
rise_fall|A Service Expanded Then Contracted|Why did one hospital service gain and later lose capacity?|Compare funding, workforce, demand, and governance.
then_vs_now|A Care Pathway in Two Periods|How did access and outcomes change for the same service?|Use compatible definitions and patient groups.
future_developments|A Conditional Hospital Expansion|Which workforce or facility constraint would determine a proposed expansion?|State assumptions and avoid claims of guaranteed benefit.
myths_vs_facts|Testing a Hospital Performance Claim|Does a headline ranking match patient-important outcomes?|Inspect case mix, denominator, measures, and uncertainty.
documentary_stories|One Hospital Case With Consent|What do consented records show about a care handoff?|Protect identity and pair personal account with process evidence.
claim_evidence|A Clinical Claim in Hospital Context|Does a study support the way a hospital intervention is described?|Compare population, comparator, outcomes, and evidence quality.
care_pathway|Where the Wait Occurs|Which step causes delay in one hospital pathway?|Use timestamps, capacity data, and referral criteria.
benefit_harm|A Hospital Intervention's Tradeoffs|Which measured benefits and harms mattered for a defined group?|Use absolute outcomes and current guidance.
mechanism_vs_outcome|A Plausible Process, an Actual Result|Did a proposed workflow improvement change patient outcomes?|Separate process measures from clinical outcomes.
population_difference|Who Was Not Represented?|Which patients are missing from a hospital evaluation?|Review inclusion criteria, follow-up, and subgroup data.
quality_of_guidance|From Guideline to Ward Practice|Where did one hospital adapt a national guideline?|Compare published guidance, local protocol, and rationale.
access_to_care|Getting to Hospital Care|Which geographic, financial, or language barrier delays a service?|Use local access data and patient accounts with consent.
patient_experience|A Patient's Handoff Experience|What can one patient account reveal about communication between teams?|Attribute testimony and avoid treating it as typical.
misinformation_path|A Misread Hospital Statistic|How did a performance claim spread beyond what the data support?|Trace source, denominator, and correction.
prevention_boundary|Preventing a Hospital Safety Event|Which system change has evidence of reducing one defined harm?|Use current safety guidance and measured outcomes.
system_pressure|Staffing and Patient Flow|How did staffing and demand interact during one period?|Use dated rosters, occupancy, delays, and safety data.
historical_revision|When Hospital Practice Changed|Which new evidence led to a documented protocol revision?|Trace old and new guidance and implementation.
field_clinical_evidence|Evidence Behind a Hospital Protocol|Which clinical evidence supports one local protocol?|Check relevance, certainty, and exceptions.
field_care_quality|Quality Beyond Throughput|Does faster discharge correspond to safe follow-up?|Compare readmission, patient experience, and time measures.
field_patient_safety|Learning From a Published Incident|Which system conditions contributed to one reported safety event?|Use investigation findings and protect individuals.
field_health_equity|Unequal Hospital Outcomes|Which groups experienced different access or outcomes?|Use comparable denominators and local context.
field_service_capacity|The Bottleneck in a Hospital Service|Which resource limits one defined service?|Compare beds, staff, equipment, and demand."""

EMERGENCY = """history_origins|How an Emergency Service Formed|Which hazard or public need led to one service's creation?|Use dated law, budgets, and incident records.
famous_examples|A Response Often Called a Model|What did one celebrated response achieve and miss?|Compare official after-action findings and affected voices.
hidden_stories|The Dispatch and Support Workforce|Whose labor is missing from a response story?|Trace call-taking, logistics, maintenance, and handoffs.
beginner_explainers|From Call to Handoff|What happens between an emergency call and the receiving service?|Map dispatch, assignment, travel, care or assistance, and transfer.
advanced_concepts|Priority Under Limited Capacity|How does a service prioritize calls when demand exceeds resources?|Examine published policy and outcomes without tactical instructions.
mysteries_unsolved_cases|A Delay With Several Causes|Which parts of one response delay are documented or uncertain?|Compare timestamps, resource logs, geography, and reporting gaps.
technology_innovation|A Dispatch Tool Evaluated|Did one communication tool improve response coordination?|Compare reliability, accessibility, false alerts, and measured timing.
people_personalities|Who Decided the Response Plan?|Which institutional choices shaped one emergency service response?|Use plans, command records, and post-incident review.
major_events|A Demand Surge Timeline|How did one emergency service adapt during a documented surge?|Use dated call volume, staffing, mutual aid, and outcomes.
how_it_works|A Multiservice Response|How do emergency services coordinate a single incident?|Describe roles and public governance, not operational vulnerabilities.
rise_fall|An Emergency Service Under Strain|Why did service capacity improve and then decline?|Compare funding, workforce, demand, and geography.
then_vs_now|Response Capability Across Two Periods|Which capabilities measurably changed?|Use consistent incident types, geography, and outcome measures.
future_developments|A Conditional Capacity Plan|Which constraint would determine whether an expansion improves access?|State staffing, dispatch, fleet, and demand assumptions.
myths_vs_facts|Testing a Response-Time Claim|What does an average response time hide?|Check definitions, percentiles, geography, and incident severity.
documentary_stories|One Incident's Official Timeline|What can a public incident record establish about the response?|Protect affected people and distinguish records from inference.
incident_timeline|Minute-by-Minute Evidence|Which decisions are supported by a documented incident timeline?|Use released timestamps and note gaps; avoid tactical detail.
prevention_layer|An Earlier Chance to Reduce Harm|Which prevention measure could reduce demand for one response type?|Use evaluated programs and context.
response_chain|The Handoff That Mattered|Where did information move or fail between agencies?|Use official reviews and consented accounts.
evidence_integrity|Reliable Incident Records|Which record is sufficient to establish one response sequence?|Compare logs, dispatch data, and independent accounts.
victim_perspective|The Affected Person's Experience|What did a consented account reveal about service access?|Respect privacy and pair testimony with system data.
system_failure|A Systemic Response Gap|Which organizational conditions contributed to a published failure?|Focus on verified causes and corrective action.
risk_communication|A Warning People Could Use|Did a public alert convey the action and uncertainty clearly?|Compare message, timing, accessibility, and community response.
community_trust|Trust Before an Emergency|How did prior relationships affect response cooperation?|Use community testimony and program evaluation.
false_positive|An Alert That Was Not Confirmed|What does one false alarm reveal about verification and communication?|Use official findings without exposing exploitable processes.
after_action|What Changed After Review?|Which recommendation from an after-action report was implemented?|Compare report, funding, training, and later evidence.
legal_boundary|Authority During a Response|Which agency had legal responsibility at a specific stage?|Use jurisdictional law and incident command records.
resilience_design|Keeping Service Available|Which redundancy maintained emergency service during one disruption?|Use public-level system design and measured continuity.
field_evidence_handling|Documenting a Response Fairly|How were logs and testimony preserved for later review?|Use public records and chain-of-custody policy at a high level.
field_prevention_design|Reducing Repeat Incidents|Which evaluated intervention lowered a defined hazard?|Compare baseline, implementation, and outcomes.
field_response_timing|Where Time Was Lost|Which stage contributes most to a measured response interval?|Separate call processing, turnout, travel, and handoff.
field_public_trust|Accountability After an Incident|How did an agency explain its decisions to the public?|Compare records released, corrections, and community feedback.
field_victim_support|Support After Immediate Response|Which services were offered after one incident?|Use public program terms and consented accounts."""

PUBLIC_SAFETY = """history_origins|How a Safety Rule Emerged|Which documented risk led to one public-safety rule?|Use legislative and incident records in one jurisdiction.
famous_examples|A Safety Program Put to the Test|Did a celebrated prevention program reduce its target harm?|Compare evaluation design, outcomes, and confounders.
hidden_stories|Who Lives With the Risk?|Whose exposure is omitted from a public safety narrative?|Use disaggregated data and community accounts.
beginner_explainers|A Public Safety System's Roles|Which agencies are responsible for prevention, response, and recovery?|Map published mandates for one jurisdiction.
advanced_concepts|Risk, Exposure, and Vulnerability|Why can the same hazard produce unequal harm?|Compare exposure, infrastructure, resources, and measured outcomes.
mysteries_unsolved_cases|Why a Harm Rate Changed|Which explanations remain plausible for one safety trend?|Compare reporting changes, exposure, and interventions.
technology_innovation|A Safety Technology Evaluated|Did one tool reduce a defined harm without new harms?|Compare accuracy, access, privacy, and outcomes.
people_personalities|Who Set the Safety Standard?|Which decisions shaped a public-safety rule?|Use committee records and affected-group input.
major_events|After a Public Safety Incident|What policy or practice changed after one documented event?|Compare inquiry recommendations and implementation.
how_it_works|From Risk Report to Action|How does a community report trigger assessment and response?|Map public process and accountability, not exploitable detail.
rise_fall|A Safety Program That Lost Capacity|Why did one prevention program shrink or end?|Compare funding, staffing, evaluation, and public decisions.
then_vs_now|Safety Across Two Periods|Did a defined harm decrease using comparable measures?|Account for reporting practices and population change.
future_developments|A Conditional Prevention Plan|Which condition would determine a proposed program's effect?|State target hazard, resources, and evaluation plan.
myths_vs_facts|Testing a Safety Claim|Does a popular claim about risk match the relevant denominator?|Check definition, exposure, and reporting completeness.
documentary_stories|One Rule's Public Record|What does the paper trail show about a safety decision?|Trace proposal, consultation, adoption, and review.
incident_timeline|A Bounded Incident Timeline|What is known from official records about one safety event?|Use released facts, protect people, and label uncertainty.
prevention_layer|A Measure Before Harm Occurs|Which prevention layer has evidence of reducing one risk?|Compare evaluated interventions for a defined setting.
response_chain|Agencies Across a Response|Where did responsibility transfer during one event?|Use public role definitions and after-action records.
evidence_integrity|Data Behind a Safety Claim|How reliable is one incident dataset?|Inspect definitions, duplicate records, and missing cases.
victim_perspective|Lived Consequences of a Safety Failure|What does a consented affected person's account illuminate?|Pair testimony with system evidence and protect privacy.
system_failure|A Published Safety Investigation|Which institutional conditions contributed to harm?|Use official findings and avoid simplistic blame.
risk_communication|A Public Warning's Clarity|Could a defined audience understand and act on one warning?|Assess language, format, timing, and later feedback.
community_trust|Who Trusts the Safety System?|How did a community assess one safety institution's legitimacy?|Use survey and attributed local accounts.
false_positive|The Cost of a False Alarm|What harm can an inaccurate safety alert cause?|Use a documented case and measured response.
after_action|Recommendation Versus Implementation|Which corrective action was carried out after a review?|Compare recommendation, budget, policy, and later outcome.
legal_boundary|The Scope of Safety Authority|Which agency could legally act in one documented situation?|Read dated jurisdictional law and public guidance.
resilience_design|Safety During a System Disruption|Which public-facing capability remained available after a failure?|Use continuity plans and measured service data.
field_evidence_handling|Preserving Trustworthy Safety Records|How were incident records created and corrected?|Use published data-governance rules and audit trails.
field_prevention_design|Designing for a Defined Hazard|Which design change reduced exposure to one harm?|Compare before-and-after data with context.
field_response_timing|Time to Help|Which part of a response interval can a public dataset measure?|Separate dispatch, travel, and resolution metrics.
field_public_trust|Transparent Review of Harm|What information did an agency publish after one failure?|Assess timeliness, completeness, and community response.
field_victim_support|Support Beyond the Incident|What assistance was available to affected people afterward?|Use public eligibility rules and consented accounts."""

FIREFIGHTING = """history_origins|How a Fire Service Developed|Which urban or rural fire risk shaped one service's creation?|Use dated fire, building, and municipal records.
famous_examples|A Fire Response in Context|What did one widely cited fire response actually show?|Compare incident report, building conditions, and later lessons.
hidden_stories|The Work Beyond the Fireground|Whose prevention, dispatch, maintenance, or recovery work is omitted?|Use staff and public records with attribution.
beginner_explainers|Fire Service Roles in One Community|How do prevention, response, investigation, and recovery connect?|Map public roles and jurisdiction without tactical instruction.
advanced_concepts|Why Fire Risk Varies by Building|Which design and use factors change measured fire outcomes?|Compare building records, exposure, and incident data.
mysteries_unsolved_cases|An Uncertain Fire Cause|What can investigators establish about one documented fire?|Use released findings and label unresolved causes.
technology_innovation|A Fire Safety Tool Evaluated|Did one detection or suppression technology reduce harm?|Compare adoption, maintenance, and outcome evidence.
people_personalities|Who Changed the Fire Code?|Which public decision shaped one fire safety rule?|Trace inquiry, standards, consultation, and adoption.
major_events|A Fire That Changed Policy|Which rule or practice actually changed after a major fire?|Compare recommendations with implementation and later audits.
how_it_works|From Alarm to Public Incident Report|What information is collected and shared through a fire response?|Describe public-level process and privacy limits.
rise_fall|A Department's Capacity Over Time|Why did staffing or coverage change in one fire service?|Compare budgets, call demand, and service-area growth.
then_vs_now|Fire Risk Across Two Periods|Did a defined fire outcome change over time?|Use compatible incident definitions and exposure measures.
future_developments|A Conditional Fire Safety Upgrade|Which maintenance or adoption condition governs a proposed upgrade?|State costs, building type, and evaluation criteria.
myths_vs_facts|Testing a Fire-Risk Claim|Does a common safety claim match incident data?|Use denominators, reporting limits, and defined building types.
documentary_stories|One Fire Investigation's Record|What do public reports establish about a fire's sequence and impact?|Protect survivors and avoid operational detail that enables harm.
incident_timeline|A Fire Event by the Records|Which decisions can a released timeline support?|Compare dispatch, arrival, evacuation, and official findings.
prevention_layer|Preventing a Building Fire|Which public code or maintenance measure reduced a defined risk?|Use evaluated interventions rather than unsourced tips.
response_chain|Coordination at a Fire Incident|How did agencies hand off responsibility during one response?|Use official after-action reports at a high level.
evidence_integrity|What Fire Data Can Show|How reliable are incident records for comparing places?|Check reporting, classification, and missing data.
victim_perspective|Survivor Needs After Fire|What did consented survivors report about immediate and later needs?|Center privacy, housing, health, and recovery context.
system_failure|A Documented Fire Safety Breakdown|Which building and institutional factors contributed to one loss?|Use inquiry findings and distinguish cause from hindsight.
risk_communication|A Fire Warning Reaches Residents|Could residents understand an official warning in time?|Assess language, channels, accessibility, and timing.
community_trust|Fire Prevention With a Community|What made a prevention program trusted or distrusted?|Use local participation and evaluation records.
false_positive|False Alarm Burden|How did false alarms affect a service's capacity in one period?|Use call data and avoid detailing bypass methods.
after_action|What Changed After a Fire Inquiry?|Which recommendation was funded and implemented?|Compare report, code, inspection, and measured outcome.
legal_boundary|Who Enforces Fire Safety Rules?|Which authority inspects or enforces one building standard?|Specify jurisdiction, building type, and date.
resilience_design|Maintaining Fire Service During Disruption|Which public-level redundancy preserved coverage?|Use continuity plans without sensitive operational details.
field_evidence_handling|Preserving Fire Investigation Records|How are public findings supported by collected evidence?|Use published investigative standards at a high level.
field_prevention_design|A Building Design Change|Did one code change measurably lower fire harm?|Compare exposed buildings and adoption dates.
field_response_timing|Understanding Fire Response Intervals|Which stages explain a reported response time?|Separate call processing, turnout, travel, and reporting definitions.
field_public_trust|Explaining a Fire Service Decision|How did an agency account publicly for one difficult response?|Assess report completeness and community feedback.
field_victim_support|Recovery After a Fire|Which housing or support services were offered afterward?|Use public program rules and survivor accounts with consent."""


if __name__ == "__main__":
    specs = [
        ("181", "181_hospital_stories", HOSPITAL,
         "Consent-aware hospital stories about care pathways, staff work, patient safety, access, and quality.",
         "published clinical guidance, hospital service data, safety investigations, dated records, and consented accounts",
         "Protect patient privacy and consent; define population and avoid diagnosis or individualized treatment advice."),
        ("182", "182_emergency_services", EMERGENCY,
         "Emergency service organization, dispatch, coordination, prevention, accountability, and recovery.",
         "official incident and after-action reports, service metrics, public policy, and consented accounts",
         "Protect affected people and avoid operational details that enable harm; verify jurisdiction and dates."),
        ("183", "183_public_safety", PUBLIC_SAFETY,
         "Public safety risk, prevention, response, accountability, unequal exposure, and recovery.",
         "official incident data, evaluations, legal mandates, public inquiries, and consented community accounts",
         "Avoid tactical or wrongdoing instructions; protect victims and distinguish incident claims from verified findings."),
        ("184", "184_firefighting", FIREFIGHTING,
         "Fire prevention, service capacity, response, investigations, code changes, and survivor recovery.",
         "official fire incident and inquiry records, building and code data, service measures, and consented survivor accounts",
         "Avoid operational or fire-setting details that enable harm; protect survivors and use current local safety guidance."),
    ]
    for item in specs:
        revise_domain(*item)
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
