"""Editorial question designs for computing education and careers."""

from review_angle_plans import audit, revise_domain


CODING = """history_origins|A Coding Curriculum Emerges|Which computing task shaped a teaching sequence?|Trace dated standards and course materials.
famous_examples|A Coding Lesson Rechecked|What can learners build and explain afterward?|Use independent task evidence.
hidden_stories|Teachers and Support behind Code|Whose debugging, feedback, or accessibility work is omitted?|Use course artifacts and credited accounts.
beginner_explainers|Program, Input, and Output|How can a beginner predict one program's behavior?|Use a small traceable example.
advanced_concepts|Abstraction for Learners|When does a useful abstraction hide a crucial detail?|Compare a model with execution evidence.
mysteries_unsolved_cases|Persistent Learner Bug|Which mistaken model explains repeated errors?|Use anonymized code and learner reasoning.
technology_innovation|A Coding Tutor Evaluated|Does an automated hint improve independent problem solving?|Compare delayed transfer tasks.
people_personalities|A Learner's Path|How did a student move from copying to design?|Use consented versions and context.
major_events|A Course Changes Language|What learning goals changed with a language or tool switch?|Compare assignments and outcomes.
how_it_works|From Prompt to Working Program|How do planning, implementation, testing, and revision connect?|Follow one bounded exercise.
rise_fall|A Teaching Tool Retired|Which access, maintenance, or learning evidence led to replacement?|Compare course records.
then_vs_now|Two Coding Courses|How do tasks and assessments differ across periods?|Align learner age and prior experience.
future_developments|A Proposed AI Coding Course|What independent skills must still be assessed?|Define tests and attribution.
myths_vs_facts|Syntax Equals Programming?|Can a learner reason about a new problem beyond memorized commands?|Use transfer challenge.
documentary_stories|One Program's Learning Trail|How did initial code, test failures, and feedback lead to revision?|Use version history.
system_boundary|Code or Whole System?|Which behavior depends on data, dependencies, and runtime?|Define environment before evaluating learner work.
input_output_trace|Trace a Program|What output follows a given input and state?|Show steps and test result.
design_tradeoff|Readability and Performance|When does a simpler solution better serve a learning goal?|Compare correct alternatives.
failure_mode|A Bug as Evidence|What test reveals the learner's assumption?|Explain cause, not just fix.
testing_limits|Passing One Test|What cases remain untested after a green check?|Design edge and property cases.
standards_interoperability|Moving Code between Systems|Which format or API assumption blocks reuse?|Use a small documented project.
security_threat_model|Safe Coding Lesson|What defensive input and permission checks fit the learner's level?|Keep examples non-exploitative.
maintenance_lifecycle|A Student Project over Time|Can another learner understand and modify it?|Review names, tests, docs, and changes.
infrastructure_dependencies|Learning Environment|Which device, network, and account access is required?|Check equal opportunity to participate.
accessibility_usability|Accessible Coding Tools|Can varied learners navigate editor, errors, and output?|Test assistive technology and alternatives.
independent_replication|Reproduce a Lesson Result|Can another teacher run the exercise?|Share version, environment, prompt, and rubric.
responsible_deployment|Publishing Learner Code|What privacy, license, and safety checks apply?|Use consent and school policy.
field_software_architecture|Organizing a Small App|Which modules separate concerns without confusing learners?|Use bounded code example.
field_interface_design|A Usable Program|Can a novice user understand inputs and errors?|Test with actual users.
field_version_changes|Library Update in Class|What broke when a dependency changed?|Compare lockfile, tests, and instructions.
field_open_standards|Portable Learning Artifact|Which open format enables reuse across tools?|Check export and import.
field_technical_debt|A Shortcut in Student Code|Which future change becomes harder?|Compare revision cost and learning goal.
"""

CLOUD = """history_origins|A Cloud Role Develops|Which hosting and operations tasks shaped it?|Trace dated job descriptions and services.
famous_examples|A Cloud Team in Practice|What did engineers, operators, security, and finance specialists do?|Use credited system records.
hidden_stories|People behind Cloud Uptime|Whose on-call, support, and data-center labor is invisible?|Use work schedules and worker accounts.
beginner_explainers|Cloud Service Responsibility|How do provider and customer tasks differ by service model?|Use NIST definitions and one product.
advanced_concepts|Reliability versus Cost|How do redundancy choices affect spend and recovery?|Compare bounded architecture and incidents.
mysteries_unsolved_cases|A Cloud Bill Surprise|Which usage, pricing, or configuration evidence explains it?|Audit dated billing and logs.
technology_innovation|Infrastructure Automation|Did automation improve deployment reliability?|Compare change failure and recovery metrics.
people_personalities|A Cloud Career Transition|Which prior operations skills transferred?|Use consented case and role requirements.
major_events|A Cloud Service Outage|What did a public postmortem establish and change?|Separate cause from downstream effects.
how_it_works|From App to Cloud Service|Who designs, deploys, observes, and repairs it?|Map responsibilities and artifacts.
rise_fall|A Cloud Skill Loses Demand|Which tasks changed with managed services?|Compare jobs and actual work.
then_vs_now|Cloud Job Ads across Years|Which skills and responsibility claims changed?|Use consistent sample and region.
future_developments|A Proposed Cloud Role|What task evidence supports the role's future need?|Treat forecast as conditional.
myths_vs_facts|Certificate Equals Production Readiness?|Which operating tasks need real evidence?|Compare lab and incident work.
documentary_stories|One Deployment's Team|How did design, cost, security, and operations interact?|Trace decision and monitoring record.
lived_experience|A Week in Cloud Operations|What planned and incident work occupies time?|Use consented diary.
institutional_pathway|Cloud Entry Routes|Which apprenticeship and credential paths lead to jobs?|Compare cost and placement.
incentives_norms|Ship Faster or Stay Stable?|How do team goals affect change review?|Use deployment and incident data.
access_and_exclusion|Who Can Enter Cloud Work?|Which hardware, connectivity, credential, and network barriers exist?|Use applicant and training records.
community_variation|Cloud Roles across Firms|How does a small firm differ from a large provider?|Compare actual tasks.
policy_in_practice|Shared Responsibility|Are security and backup owners clearly assigned?|Compare contract and incident record.
survey_vs_story|A Cloud Talent Gap|Does a survey reflect actual open roles?|Check respondents and vacancy data.
power_and_voice|Who Can Stop a Release?|Can operators raise reliability concerns?|Use change-control evidence.
unintended_consequence|More Automation, New Work|Which review or failure modes appeared?|Compare before and after.
comparative_setting|Two Cloud Teams|Why did uptime or cost differ?|Match workload and objectives.
change_over_time|Cloud Work across a Migration|Which tasks grew or disappeared?|Use dated staffing and service records.
ethical_dilemma|Cost and Service Quality|Who decides which users bear downtime risk?|Use decision criteria and incident impact.
field_skill_signals|Operational Portfolio|Which artifacts show monitoring, recovery, and cost awareness?|Check reproducibility and permission.
field_hiring_filters|Cloud Job Requirements|Which tools are essential versus vendor-specific?|Compare tasks and job ads.
field_workplace_power|On-Call Burden|Who carries after-hours risk and receives support?|Use schedule and incident data.
field_career_transitions|From IT to Cloud|Which skills transfer and which require practice?|Compare role tasks.
field_worker_support|Training and Incident Recovery|Are time and support available after outages?|Check policy and worker experience.
"""

CYBER = """history_origins|A Cyber Work Role Emerges|Which threats and organizational needs shaped it?|Trace dated frameworks and job tasks.
famous_examples|A Defensive Team Examined|What did analysts, engineers, and responders actually do?|Use authorized, public case evidence.
hidden_stories|Routine Security Labor|Whose alert triage, asset inventory, and training work is overlooked?|Use team workflows and credit.
beginner_explainers|Cybersecurity Roles by Task|How do prevention, detection, response, and governance differ?|Use NICE task statements.
advanced_concepts|Detection Quality|How do false alerts, missed events, and analyst time interact?|Use authorized evaluation data.
mysteries_unsolved_cases|A Disputed Incident Cause|What evidence remains unavailable or inconclusive?|Separate indicators from attribution.
technology_innovation|A Defensive Tool|Did it improve verified detection and response?|Compare test data and analyst workload.
people_personalities|A Defender's Career Path|Which transferable skills and mentors mattered?|Use consented account, no universal promise.
major_events|A Public Incident Review|Which response and governance lessons are documented?|Use official post-incident record.
how_it_works|A Security Work Cycle|How do inventory, monitoring, triage, remediation, and review connect?|Describe authorized high-level workflow.
rise_fall|A Security Job Title Changes|Which tasks persisted despite rebranding?|Compare dated descriptions.
then_vs_now|Cyber Roles across Years|What changed in tooling, regulation, and staffing?|Use comparable tasks and region.
future_developments|A Proposed Cyber Role|What evidence supports demand and training pathways?|Distinguish projection and vacancy.
myths_vs_facts|Hacking Skill Equals Security Career?|Which defensive tasks dominate a named role?|Read NICE and job artifacts.
documentary_stories|One Defensive Decision|How did evidence lead to a risk-reduction action?|Use sanitized authorization records.
lived_experience|A Week in Security Work|How are preventive and reactive tasks split?|Use consented diary, avoid sensitive details.
institutional_pathway|Entering Cyber Work|Which routes teach demonstrable tasks?|Compare programs, cost, and placement.
incentives_norms|Alert Metrics|Does a speed target distort investigation quality?|Use anonymized team evidence.
access_and_exclusion|Who Reaches Cyber Jobs?|Which clearance, degree, and network filters apply?|Compare role need and hiring data.
community_variation|Security in Different Sectors|How do hospital, school, and bank tasks differ?|Compare constraints without exposing systems.
policy_in_practice|Framework Adoption|Do assigned roles match actual authority and staffing?|Compare written policy and work.
survey_vs_story|Cyber Workforce Gap Claim|Is it based on vacancy, estimate, or survey?|Check method and occupation definition.
power_and_voice|Can a Defender Escalate?|What channels exist when a risk is ignored?|Use governance and outcome evidence.
unintended_consequence|New Tool, More Alerts|Did automation create unmanageable triage?|Measure precision and workload.
comparative_setting|Two Security Teams|Why did control outcomes differ?|Compare resources, assets, and scope.
change_over_time|A Role through Incidents|Which responsibilities expanded?|Use dated task and staffing records.
ethical_dilemma|Monitoring and Privacy|How does a team balance necessary logs and worker rights?|Use policy and stakeholder evidence.
field_skill_signals|A Defensive Work Sample|Does it show risk analysis and clear reporting?|Use sanitized, authorized artifact.
field_hiring_filters|Cyber Job Screening|Does a test match actual defensive work?|Check task, rubric, and access.
field_workplace_power|Security and Product Pressure|Who sets acceptable risk?|Use documented sign-off.
field_career_transitions|Adjacent Role to Cyber|Which IT, audit, or domain skills transfer?|Use actual transitions.
field_worker_support|Sustainable Incident Response|Are rotation, training, and recovery support available?|Check schedules and worker feedback.
"""


if __name__ == "__main__":
    revise_domain("463", "463_coding_education", CODING,
                  "Coding education through reasoning about programs, designing and testing small systems, interpreting errors, accessibility, and independent transfer.",
                  "CSTA computer-science learning objectives, versioned learner programs, task and rubric records, independent tests, learner explanations, and accessibility audits",
                  "Name learner level, language, runtime, task, and assessment. Passing copied examples or using a coding assistant does not alone establish independent programming skill.")
    revise_domain("464", "464_cloud_careers", CLOUD,
                  "Cloud careers through shared service responsibility, deployment, reliability, cost, security, on-call work, and real hiring paths.",
                  "NIST cloud definitions, dated job descriptions, authorized architecture and operations artifacts, public incident reviews, billing records, and worker accounts",
                  "Name role, cloud service model, employer type, location, and date. A vendor certificate is limited evidence and does not promise employment or production readiness.")
    revise_domain("465", "465_cybersecurity_careers", CYBER,
                  "Cybersecurity careers through NIST NICE tasks, defensive work evidence, governance, workload, responsible disclosure, and fair entry paths.",
                  "current NICE task and skill statements, dated job postings, authorized sanitized work artifacts, official incident reviews, training outcomes, and worker accounts",
                  "Name role, sector, jurisdiction, and date. Use public defensive evidence only; avoid exploit instructions, unsupported incident attribution, or job guarantees.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
