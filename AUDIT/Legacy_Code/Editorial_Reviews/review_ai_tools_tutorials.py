"""Direct question-design review for AI tool tutorials."""
from review_angle_plans import revise_domain, audit

AI_TOOLS = """history_origins|A Tool's Version History|Which dated releases changed one AI tool's core task?|Compare vendor notes, archived interface, and independent tests.
famous_examples|A Popular Demo Reproduced|Can a widely shared AI demonstration be repeated under stated conditions?|Record model and tool version, inputs, settings, date, and output variance.
hidden_stories|People Behind a Seamless Demo|Which data, labeling, review, or integration work is missing from the showcase?|Use disclosed documentation and attributed worker accounts.
beginner_explainers|A First Task with an AI Tool|What input, output, and human check does one bounded use case require?|Show a reproducible task with version, data permissions, and success criterion.
advanced_concepts|Tool, Model, and Workflow|Which layer causes a behavior in one AI application?|Separate base model, retrieval, prompt, external tool, interface, and policy.
mysteries_unsolved_cases|An Output That Cannot Be Reproduced|Which missing setting or dependency explains a demo mismatch?|Check version, sampling, context, data source, and logs.
technology_innovation|A New Feature Under Test|Does one new capability improve a defined task?|Compare baseline, latency, cost, error, and independent evaluation.
people_personalities|A Designer's Tradeoff|What did one documented product decision prioritize?|Use release notes, design record, evaluation, and affected-user feedback.
major_events|A Model or API Change|What broke or improved after one dated release?|Run fixed test cases across versions and record migration effects.
how_it_works|An AI Workflow End to End|Where do input, model call, external data, review, and final action occur?|Map data flow and human approval points without hidden assumptions.
rise_fall|A Tool's Changing Reliability|How did task performance change across releases?|Use same benchmark, prompts, data, and scoring across dates.
then_vs_now|A Tutorial Across Versions|Which steps in an older tutorial still work?|Compare current interface and docs, noting deprecated commands.
future_developments|A Proposed AI Feature|What would need to be true for one announced feature to help users?|State dependencies and test plan without treating roadmap as availability.
myths_vs_facts|A Tool Claim Put to the Test|Does a marketing claim hold on representative user tasks?|Use independent cases, error analysis, and versioned conditions.
documentary_stories|A Tutorial's Revision Trail|How did one workflow change from first demo to stable practice?|Trace changelogs, failures, user reports, and corrections.
system_boundary|What the Tool Can Access|Which files, services, or permissions does one workflow actually use?|Verify interface and authorization at the documented version.
input_output_trace|One Run's Evidence|What exact input produced one displayed output?|Save sanitized prompt, configuration, tool calls, result, and date.
design_tradeoff|Speed, Quality, and Cost|Which tradeoff does one setting create on a defined task?|Measure latency, error, expense, and user impact.
failure_mode|A Known Failure Reproduced|When does one workflow fail and how is failure detected?|Use safe test data and specify consequence and fallback.
testing_limits|What the Demo Did Not Test|Which edge cases or user groups are absent from a tutorial?|List test coverage and plausible missing conditions.
standards_interoperability|A Format or API Boundary|Does the tool exchange data reliably with a named system?|Test schema, versions, errors, and portability.
security_threat_model|Untrusted Input in a Workflow|What can a malicious document or tool response influence?|Test boundaries safely; avoid publishing exploit instructions.
maintenance_lifecycle|Keeping a Tutorial Current|Which dependency or interface changes require a recheck?|Track versions, docs, test fixture, and update owner.
infrastructure_dependencies|What Makes the Demo Work|Which network, model, account, or hardware dependency is essential?|Document availability, quotas, privacy, and fallback.
accessibility_usability|Who Can Complete the Workflow?|Which keyboard, screen-reader, language, or cost barrier appears?|Test with affected users and representative tasks.
independent_replication|Can Another User Repeat It?|What must be documented for a second person to reproduce the result?|Provide sanitized data, settings, scoring, and expected variation.
responsible_deployment|From Demo to Real Use|Which risks emerge when one tutorial is used on consequential data?|Map permissions, review, monitoring, and rollback.
field_training_or_control_data|Data Behind the Behavior|What is known about the data or control instructions affecting output?|Use vendor disclosures and tests; mark unavailable provenance.
field_real_world_testing|Performance on Actual Tasks|How does a tool perform on a consented, representative workflow?|Measure quality and harms against a non-AI baseline.
field_human_oversight|Who Reviews the Result?|At which step can a person detect and correct an error?|Test review load, visibility, authority, and escalation.
field_failure_recovery|Recovering from a Bad Output|How does the workflow catch, reverse, and learn from an error?|Check logs, version history, rollback, and incident process.
field_hardware_dependency|Compute and Device Limits|Which device or compute requirement changes user experience?|Measure latency, energy or cost where relevant, and access."""

if __name__ == "__main__":
    revise_domain("007", "007_ai_tools_ai_tutorials", AI_TOOLS,
                  "Versioned AI tool tutorials for bounded tasks, reproducibility, evaluation, permissions, security, accessibility, and human oversight.",
                  "current official product documentation and release notes, versioned test inputs and outputs, independent task evaluations, security reviews, and consented user feedback",
                  "Name tool and model versions, date, permissions, and test task; verify current interface before production. Use sanitized data, disclose output variability, and require human checks for consequential results.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
