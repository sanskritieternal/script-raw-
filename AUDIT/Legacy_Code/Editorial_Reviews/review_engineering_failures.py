"""Editorial questions for engineering failures."""

from review_angle_plans import audit, revise_domain


FAILURES = """history_origins|How a Design Entered Service|Which assumptions and reviews preceded one failed system?|Trace requirements, approval, construction, tests, and early use.
famous_examples|A Famous Failure Reexamined|What does the primary investigation actually conclude?|Compare evidence, probable causes, contributing conditions, and later retellings.
hidden_stories|Warnings Before the Failure|Who noticed trouble and what happened to their reports?|Use dated inspection, maintenance, complaint, and decision records.
beginner_explainers|What an Investigation Can Establish|How are physical evidence, logs, interviews, and models combined?|Use one public inquiry and label uncertainty.
advanced_concepts|A Chain of Contributing Conditions|How did technical, organizational, and human factors interact?|Map causal evidence without reducing the event to one person.
mysteries_unsolved_cases|An Unresolved Failure Mechanism|Which explanations remain plausible after an inquiry?|Compare tests, missing evidence, model limits, and confidence.
technology_innovation|A Safety Measure After Failure|Did one new design or monitoring method reduce the identified risk?|Check validation, adoption, later incidents, and unintended effects.
people_personalities|The Decision Makers in Context|What information and authority did individuals have at key points?|Use contemporaneous records and avoid hindsight speculation.
major_events|The Event Minute by Minute|Which documented sequence led to a system's failure?|Reconstruct from synchronized evidence, with gaps marked.
how_it_works|The System Before It Failed|What normal functions and safeguards should have operated?|Use approved design, operating conditions, and maintenance history.
rise_fall|Warning Signs Across Years|Did one system degrade before a major failure?|Compare inspections, repairs, loads, incidents, and data gaps.
then_vs_now|What Changed After the Inquiry|Which recommendations became practice?|Trace standards, funding, inspection, training, and compliance.
future_developments|A Proposed Fix Under Test|Would one remedy address the documented failure mode?|Check causal link, validation, implementation, cost, and residual risk.
myths_vs_facts|A Simple Cause Story Challenged|Does a popular explanation omit critical factors?|Compare claim with investigation evidence and chronology.
documentary_stories|Following One Safety Recommendation|What happened from finding to implementation?|Trace responsible body, timeline, funding, verification, and open items.
system_boundary|Where the Failed System Ends|Which dependencies belonged in the safety analysis?|Map equipment, operators, software, maintenance, and environment.
input_output_trace|Signals Before an Incident|Which measurements showed changing performance?|Review sensor reliability, timestamps, thresholds, and response.
design_tradeoff|Cost, Capacity, and Margin|How did tradeoffs alter resilience in one documented design?|Use records, alternatives, safety factors, and approval.
failure_mode|The First Physical Break|What evidence locates initiation and propagation?|Compare debris, imaging, materials, loads, and competing hypotheses.
testing_limits|A Test That Missed the Risk|Why did pre-service testing fail to expose one hazard?|Compare test case, real conditions, sample, assumptions, and later evidence.
standards_interoperability|A Rule's Blind Spot|Did a code or interface requirement cover the actual hazard?|Compare applicable versions, compliance, performance, and revision.
security_threat_model|Malicious Versus Accidental Failure|Which evidence can distinguish tampering from fault or error?|Use verified forensic records and avoid unsupported allegations.
maintenance_lifecycle|Deferred Maintenance and Risk|Which maintenance choices contributed to one event?|Compare schedules, findings, resources, repairs, and causal evidence.
infrastructure_dependencies|A Failure That Spread|How did connected services amplify an incident?|Map dependencies, protections, recovery, and user impacts.
accessibility_usability|Could Operators Read the Warning?|How did interface design affect recognition and response?|Examine alerts, training, workload, observations, and tests.
independent_replication|Checking an Investigation Model|Can independent analysis reproduce one technical conclusion?|Compare assumptions, data, sensitivity, and alternative models.
responsible_deployment|Learning Without Scapegoating|How did an organization translate findings into safer practice?|Review transparent reporting, worker participation, remedy, and follow-up.
field_prototype_testing|A Prototype's Missed Signal|What did early test failures reveal and how were they handled?|Trace logs, decisions, retests, and production changes.
field_design_tolerance|A Margin That Was Too Small|Which design tolerance mattered in one failure?|Compare actual variation, loads, standard, and inspection evidence.
field_manufacturing_method|A Defect Introduced in Production|What records tie one process change to a later fault?|Use batch traceability, quality tests, failure analysis, and uncertainty.
field_failure_investigation|Evidence Preservation After Failure|How did investigators collect and protect key evidence?|Trace chain of custody, sampling, tests, and limitations.
field_repair_path|Was a Fix Effective?|Did one repair or retrofit remove the documented hazard?|Compare specification, qualified inspection, service record, and later monitoring.
"""


if __name__ == "__main__":
    revise_domain("162", "162_engineering_failures", FAILURES,
                  "Engineering failures through evidence chains, design assumptions, maintenance, human systems, investigations, recommendations, and verified fixes.",
                  "official inquiry reports and exhibits, dated design and maintenance records, physical evidence and qualified tests, standards in force at the time, and documented recommendation follow-up",
                  "Name incident, system, jurisdiction, and date. Avoid blame without evidence, preserve inquiry uncertainty and affected people's dignity, and keep hazardous repair or forensic work with qualified investigators.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
