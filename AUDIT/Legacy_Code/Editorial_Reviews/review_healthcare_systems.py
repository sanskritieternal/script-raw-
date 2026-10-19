"""Editorial questions for healthcare systems."""

from review_angle_plans import audit, revise_domain


HEALTHCARE = """history_origins|How One Health System Took Shape|Which policies built a region's current service structure?|Trace laws, financing, workforce, facilities, and population needs.
famous_examples|A Praised Reform Evaluated|Did one healthcare reform improve the outcome it promised?|Compare access, quality, cost, equity, and implementation.
hidden_stories|Workers Beyond the Doctor|Whose nursing, laboratory, community, cleaning, and logistics work is overlooked?|Use workforce records and consented accounts.
beginner_explainers|The Path from Need to Care|What steps must a person take to receive one service?|Map eligibility, referral, wait, treatment, follow-up, and cost.
advanced_concepts|Coverage Versus Effective Care|Does having an entitlement translate into timely quality service?|Compare enrollment, availability, clinical quality, outcomes, and expense.
mysteries_unsolved_cases|Why Two Regions Have Different Outcomes|Which system factors could explain a gap?|Check case mix, access, data quality, staffing, and policy.
technology_innovation|A Digital Tool in a Health System|Did one tool improve a defined care process?|Compare patient outcome, errors, workflow, equity, privacy, and cost.
people_personalities|A Health Worker in the System|How do staffing and rules shape one worker's decisions?|Use voluntary interviews and organizational records without blame.
major_events|A System Under Surge Pressure|How did one crisis affect care inside and outside the target condition?|Trace capacity, staffing, delayed services, outcomes, and recovery.
how_it_works|Financing One Service|Where does money come from and who pays at the point of care?|Trace budget, insurer, provider payment, patient cost, and incentives.
rise_fall|A Clinic Network's Expansion or Closure|Why did local service capacity change?|Check population, funding, staffing, demand, and travel time.
then_vs_now|A Care Pathway Across Decades|How did one patient's steps, waits, and costs change?|Compare same service, eligibility, measurement, and outcomes.
future_developments|A Proposed Service Expansion|What would one plan need to deliver safe care?|Assess workforce, facilities, demand, funding, continuity, and evaluation.
myths_vs_facts|A Simple Health-System Ranking|Does one score capture the care residents actually receive?|Review indicators, weights, equity, patient experience, and uncertainty.
documentary_stories|One Referral Through the System|Where do handoffs help or hinder care?|Use consented patient experience and anonymized service records.
claim_evidence|A Claim About Better Outcomes|What evidence links one system change to health improvement?|Check comparator, confounding, time, population, and uncertainty.
care_pathway|A Person Between Providers|Where do transfers, records, and follow-up fail or succeed?|Map actual steps, responsibilities, and patient feedback.
benefit_harm|A System Change's Tradeoffs|Did one policy improve access while creating other risks?|Compare intended benefits, patient safety, costs, and affected groups.
mechanism_vs_outcome|More Appointments, Better Health?|Did increased activity produce meaningful patient outcomes?|Separate throughput, quality, safety, and follow-up.
population_difference|Who Gets Timely Care?|How do service outcomes differ by place, income, disability, or language?|Use appropriate disaggregated data and protect privacy.
quality_of_guidance|A Guideline in Real Practice|Was one clinical recommendation current, evidence-based, and usable?|Check version, evidence review, implementation, and exceptions.
access_to_care|The Real Cost of Care|What travel, wait, paperwork, and payment barriers matter?|Measure full burden for a defined population and service.
patient_experience|What Patients Report|How does one group describe respect, communication, and continuity?|Use valid surveys and voluntary interviews without making one voice typical.
misinformation_path|A False System Claim|How did a misleading claim about access or outcomes spread?|Trace origin, data misuse, correction, and public effect.
prevention_boundary|Prevention and Treatment Capacity|Which institution is responsible for a named preventive service?|Map authority, financing, referral, and measured uptake.
system_pressure|A Staff Shortage's Effects|How did one workforce gap change waits and safety?|Check vacancies, workload, skill mix, outcomes, and alternatives.
historical_revision|A Policy Judgment Revisited|Why did evidence cause one earlier health-system conclusion to change?|Compare old and new datasets, methods, and policy context.
field_clinical_evidence|Linking Practice to Outcome|What study design can evaluate one service model?|Specify patient population, comparator, outcome, and limitations.
field_care_quality|Measuring Service Quality|Which indicators capture safety, effectiveness, timeliness, and dignity?|Check validity, reporting, risk adjustment, and user priorities.
field_patient_safety|Learning from Harm Reports|Does one reporting system lead to corrective action?|Trace event categories, confidentiality, investigation, and follow-up.
field_health_equity|An Equity Gap in One Service|Where does a disparity arise along the care pathway?|Measure need, access, treatment, outcomes, and structural barriers.
field_service_capacity|Can the System Meet Demand?|How do staffing, beds, supplies, and schedules constrain one service?|Compare actual capacity, utilization, peaks, and safe thresholds.
"""


if __name__ == "__main__":
    revise_domain("180", "180_healthcare_systems", HEALTHCARE,
                  "Healthcare systems through financing, workforce, service pathways, access, quality, safety, patient experience, and equity.",
                  "current system policies and budgets, workforce and service-capacity data, validated quality and outcome measures, clinical guidance with version, and voluntary consented patient and worker accounts",
                  "Name jurisdiction, service, population, and date. Distinguish coverage from effective care and throughput from health outcomes; protect patient information and verify medical claims with current authoritative evidence.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
