"""Editorial questions for biotechnology."""

from review_angle_plans import audit, revise_domain


BIOTECH = """history_origins|From Biological Discovery to Product|Which scientific finding enabled one biotechnology product?|Trace original result, later engineering, trials, and launch.
famous_examples|A Widely Cited Biotech Product Tested|What benefits and limits are documented for one named product?|Compare intended use, independent evidence, approved claims, and access.
hidden_stories|Work Behind a Biotech Breakthrough|Whose laboratory, manufacturing, clinical, and regulatory work is overlooked?|Trace roles and credit in original records.
beginner_explainers|What Makes a Product Biotechnology?|Which biological component or process is central to one product?|Define system boundary, intended function, and alternatives.
advanced_concepts|Evidence from Bench to Use|Why can a promising laboratory result fail in real deployment?|Compare model validity, scale, safety, quality, and user context.
mysteries_unsolved_cases|A Result That Did Not Replicate|Which factors could explain conflicting findings for one application?|Review protocols at a high level, samples, controls, analysis, and reporting.
technology_innovation|A New Measurement or Platform|What capability does one biotechnology platform add?|Compare performance, validation, cost, limitations, and risk assessment.
people_personalities|A Research Team's Decision|How did one team choose a development path under uncertainty?|Use dated publications, funding, design records, and attributed interviews.
major_events|A Regulatory Decision in Context|What evidence supported one approval, rejection, or restriction?|Compare submission, assessment, public decision, and later monitoring.
how_it_works|A Biotech Product's Function|How does one product produce its intended outcome?|Use a high-level mechanism and verified product documentation.
rise_fall|Why a Biotech Approach Was Abandoned|Which evidence or practical barriers ended one project?|Trace efficacy, safety, cost, manufacturing, and competing options.
then_vs_now|A Biotech Method Across Generations|How did one product class change in performance and oversight?|Compare matched indications, tests, standards, and availability.
future_developments|A Claimed Next-Generation Product|What milestones would support one proposed application?|Define evidence gaps, trials, scale, oversight, and access.
myths_vs_facts|A Biotech Claim Under Review|Does a public claim match the product's tested conditions?|Check source, comparator, population, outcome, and uncertainty.
documentary_stories|A Product's Evidence Journey|How did one idea move through testing, review, and real use?|Follow published records, independent checks, and patient or user experience.
system_boundary|Where the Product Begins and Ends|Which inputs, operators, and environments affect one biotech result?|Map components, process controls, users, and downstream effects.
input_output_trace|What Goes In and What Comes Out?|How is one product's stated output measured against its inputs?|Use documented performance data without operational recipe detail.
design_tradeoff|Sensitivity, Speed, and Cost|Which tradeoffs shaped one diagnostic or analytical tool?|Compare intended setting, errors, turnaround, cost, and access.
failure_mode|When a Biotech System Fails|What failure modes are documented for one product?|Review reports, detection, user impact, and corrective action.
testing_limits|A Trial's Boundaries|Who and what were excluded from one evaluation?|Check population, duration, endpoints, comparator, and follow-up.
standards_interoperability|A Product Within a Health System|Which standards let one tool's results be interpreted or shared?|Examine validation, data formats, quality systems, and jurisdiction.
security_threat_model|Protecting Biological Information|What privacy or misuse risks arise from one data workflow?|Map data collected, access, retention, safeguards, and governance.
maintenance_lifecycle|Keeping Performance Stable|How is one deployed product monitored over its lifetime?|Trace quality checks, updates, adverse reports, and retirement.
infrastructure_dependencies|What a Biotech Tool Depends On|Which facilities, trained staff, energy, and supply chains are needed?|Compare actual deployment setting with claimed portability.
accessibility_usability|Who Can Benefit from the Product?|Which price, language, disability, or location barriers limit use?|Use real service conditions and affected user accounts.
independent_replication|Can Another Team Confirm It?|Which independent evidence supports one performance claim?|Check protocols, sample diversity, conflicts, and consistent outcomes.
responsible_deployment|A Product After Approval|How are benefits, harms, access, and oversight tracked in use?|Compare monitoring duties, complaints, equity, and feedback.
field_prototype_testing|A Prototype's First Evidence|What can a small early test establish and not establish?|Review design, controls, outcome, risk review, and next tests.
field_design_tolerance|How Much Variation Is Acceptable?|Which product attributes must stay within validated limits?|Use public specifications, batch evidence, and quality assessment.
field_manufacturing_method|Scaling a Biotech Product|Which high-level production changes threaten comparability?|Compare public quality records, process validation, and oversight.
field_failure_investigation|Tracing an Unexpected Outcome|How was one suspected product failure investigated?|Follow reporting, independent review, corrective action, and uncertainty.
field_repair_path|Fixing a Deployed Tool|How can one instrument or software system be serviced safely?|Check authorized maintenance, recalibration, support, and downtime.
"""


if __name__ == "__main__":
    revise_domain("155", "155_biotechnology", BIOTECH,
                  "Biotechnology through evidence development, system performance, manufacturing quality, access, governance, and responsible use.",
                  "original research and independent replication, public regulatory assessments, validated product specifications, quality and adverse-event records, and consented user accounts",
                  "Name product, intended use, population, jurisdiction, and date. Keep biological procedures at a high documentary level, defer hazardous work to qualified oversight, and separate tested outcomes from promotional claims.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
