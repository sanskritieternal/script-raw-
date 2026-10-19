"""Editorial question designs for three human-futures niches."""

from review_angle_plans import audit, revise_domain


ROBOT = """history_origins|From Industrial Arm to Social Robot|Which technical and social changes brought robots into shared human spaces?|Trace dated deployments rather than fiction.
famous_examples|A Robot in a Public Setting|What tasks did a named deployed robot actually complete?|Use operating records and independent evaluation.
hidden_stories|People Supporting a Robot|Which teleoperators, cleaners, maintainers, and bystanders make the service possible?|Follow one documented site.
beginner_explainers|Robot, Automation, or AI?|What distinguishes a physical robot from software and remote control?|Show sensors, actuation, and human input.
advanced_concepts|Shared Autonomy in Practice|How are control and responsibility divided between operator and machine?|Map handoffs and failure states.
mysteries_unsolved_cases|A Claimed Labor Saving|What evidence would separate saved work from displaced or hidden work?|Measure total tasks over time.
technology_innovation|Safer Human–Robot Interaction|Which sensing or control change reduced a measured hazard?|Compare tests under defined conditions.
people_personalities|A Person Living with a Robot|What benefit and inconvenience does one user's account reveal?|Obtain consent and avoid generalizing.
major_events|A Robot Deployment Decision|Who approved a public trial and what changed after incidents?|Read procurement and incident records.
how_it_works|One Robot Service Workflow|How do request, perception, movement, human help, and recovery connect?|Diagram a real task.
rise_fall|A Robot Program Retired|Was withdrawal driven by cost, reliability, demand, or safety?|Compare dated records.
then_vs_now|Robot Capabilities across Generations|What tasks became dependable rather than just demonstrated?|Use comparable benchmarks.
future_developments|Robots in Daily Life|Which technical, cost, accessibility, and consent conditions must hold?|Frame as conditional scenarios.
myths_vs_facts|A Fully Autonomous Robot?|Where does the human operator enter a claimed autonomous system?|Audit a documented deployment.
documentary_stories|A Robot Trial's Public Record|How did design, testing, deployment, complaint, and revision unfold?|Build a dated evidence trail.
assumption_inventory|A Robot Society Scenario|Which mobility, safety, maintenance, and acceptance premises does it need?|Label uncertainties.
readiness_check|Before Robots Enter a Shared Space|Who can stop, repair, supervise, and complain about them?|Check actual procedures.
physical_limits|Batteries, Terrain, and Payload|What physical constraints bound a proposed robot task?|Use measured duty cycle and site conditions.
governance_choice|Who Authorizes the Robot?|How do owner, operator, regulator, and affected public share control?|Compare real governance options.
unequal_futures|Robot Benefits and Burdens|Who receives service while others face surveillance or job change?|Assess groups separately.
scenario_pair|Two Ways to Introduce Service Robots|How do consultation and unilateral rollout affect outcomes?|Hold task and setting constant.
failure_to_launch|A Pilot That Stayed a Pilot|Which reliability, price, or trust barrier prevented scale?|Use pilot and follow-up data.
unintended_effect|Work Shifted to Humans|Did the robot create new monitoring or exception-handling labor?|Observe complete workflow.
social_adaptation|People Change Paths around Robots|How do workers and users adjust behavior in a shared space?|Use field observation and consent.
ethical_boundary|Where Robots Should Yield|Which interactions require direct human choice or care?|State criteria and affected voices.
signal_vs_hype|Robot Demo versus Routine Service|What sustained-use evidence supports a society-wide claim?|Separate prototype and deployment.
reversible_steps|A Robot Trial with Exit|How can the site pause use and remedy harm?|Check contract and incident process.
field_human_agency|A Usable Override|Can a nearby person actually stop or redirect the robot?|Test in realistic conditions.
field_body_and_identity|Embodied Interaction and Attachment|How do design cues affect expectations of understanding or care?|Interview users without assuming feelings.
field_rights_framework|Rights in Robot-Mediated Space|Which privacy, safety, and accessibility duties apply?|Specify jurisdiction and operator.
field_resource_inequality|The Cost of Robot Service|Who pays for hardware, energy, repair, and training?|Use life-cycle and budget records.
field_institutional_adaptation|A Workplace after Robots|How did tasks, supervision, and accountability change?|Compare records before and after.
"""

TRANSHUMAN = """history_origins|A History of Human Enhancement Ideas|Which older medical and philosophical claims shaped transhumanism?|Compare texts in their period.
famous_examples|An Enhancement Claim Examined|What intervention and outcome does a named case actually demonstrate?|Separate treatment from speculation.
hidden_stories|People Missing from Enhancement Debates|Whose disability, care, and access perspectives were omitted?|Use attributed accounts.
beginner_explainers|Treatment, Assistance, Enhancement|Where do purposes and definitions overlap or differ?|Use concrete technologies and users.
advanced_concepts|Heritable versus Somatic Change|Why do inheritance and reversibility alter a proposal's stakes?|Use WHO distinctions.
mysteries_unsolved_cases|A Claimed Cognitive Gain|What controlled evidence would distinguish durable benefit from placebo?|Specify outcome and follow-up.
technology_innovation|An Intervention's Evidence Path|What must move from laboratory result to responsible human use?|Map trials, oversight, and access.
people_personalities|A Transhumanist Proposal's Author|Which experiences and assumptions shaped one influential argument?|Read primary writing and criticism.
major_events|A Human-Editing Governance Milestone|How did a dated event change oversight?|Compare guidance and practice.
how_it_works|From Proposal to Human Intervention|Who tests, consents, monitors, and can stop the process?|Trace a regulated example.
rise_fall|An Enhancement Promise Reconsidered|Which outcome or harm changed support for it?|Use dated evidence.
then_vs_now|Enhancement Claims across Decades|How did predicted capability compare with actual use?|Define comparable outcomes.
future_developments|Possible Human Enhancement Paths|Which scientific and social assumptions separate scenarios?|Do not present forecasts as outcomes.
myths_vs_facts|Can Enhancement Remove Human Limits?|Which biological and social limits remain in a specific claim?|Test one mechanism.
documentary_stories|A Proposal's Evidence Trail|How did theory, experiment, critique, and governance interact?|Use dated primary records.
assumption_inventory|A Transhumanist Future|What efficacy, safety, access, and consent premises are required?|List unknowns explicitly.
readiness_check|Before Offering Enhancement|Are evidence, consent, monitoring, and remedies adequate?|Use intervention-specific criteria.
physical_limits|Tradeoffs of Biological Change|Which energetic, developmental, or physiological limits matter?|Avoid universal optimization claims.
governance_choice|Who May Decide on Enhancement?|How do personal autonomy and public oversight intersect?|Compare concrete decisions.
unequal_futures|Enhancement and Stratification|Who could afford or be pressured into an intervention?|Assess distribution and coercion.
scenario_pair|Two Access Models|How would private sale and public provision change fairness?|Hold intervention and evidence fixed.
failure_to_launch|A Promising Idea without Clinical Use|Which safety or efficacy gap halted progress?|Read study and regulatory record.
unintended_effect|Performance Pressure|Could availability create new expectations in school or work?|Test with actual policy and users.
social_adaptation|Norms after an Enhancement Offer|How might family, employers, and insurers respond?|Use bounded scenarios and stakeholder views.
ethical_boundary|Changes to Future Generations|What consent and intergenerational issues arise with heritable changes?|Use WHO governance framework.
signal_vs_hype|Evidence behind an Enhancement Headline|Is it an animal study, human trial, or established outcome?|State population and endpoint.
reversible_steps|A Trial with Long-Term Follow-Up|What can be stopped and what cannot be reversed?|Specify intervention and obligations.
field_human_agency|Voluntary or Pressured Choice?|Can a person refuse without losing opportunity?|Examine institutional incentives.
field_body_and_identity|Continuity of Self|How do users describe changes to identity after an intervention?|Use consented qualitative evidence.
field_rights_framework|Enhancement and Human Rights|Which rights and oversight mechanisms apply to a proposal?|Name place, date, and intervention.
field_resource_inequality|Who Bears Research Costs?|How are risk, cost, and benefit divided among groups?|Use trial and access records.
field_institutional_adaptation|Schools and Workplaces Respond|Which policies would need revision if an intervention spread?|Distinguish present rule from scenario.
"""

BRAIN = """history_origins|Brain Enhancement before Interfaces|How did drugs, training, and prosthetics shape today's claims?|Trace distinct evidence lines.
famous_examples|A Brain Interface Trial|What function did a named participant regain in a documented trial?|Use published endpoint and consent.
hidden_stories|Support after Implantation|Who supplies surgery, calibration, repair, and long-term care?|Follow full service chain.
beginner_explainers|What Is Brain Enhancement?|How do restoration, assistance, and above-baseline performance differ?|Define intervention and outcome.
advanced_concepts|Decoding versus Understanding Thought|What do neural signals allow researchers to infer?|Specify task, training, and error.
mysteries_unsolved_cases|Does a Benefit Persist?|Which follow-up and comparison data would establish durable improvement?|Control for practice and selection.
technology_innovation|Implant and Wearable Tradeoffs|How do signal quality, invasiveness, and maintenance compare?|Use device-specific studies.
people_personalities|A Participant's Agency|What does one participant report about control and daily burden?|Use attributed consented account.
major_events|A BCI Trial Approval|Which safety and follow-up duties accompanied a dated study?|Read trial and oversight records.
how_it_works|From Neural Signal to Device Action|How do acquisition, decoding, feedback, and correction connect?|Show measured error rates.
rise_fall|A Brain-Enhancement Claim Challenged|Which failed replication or harm changed the picture?|Compare dated studies.
then_vs_now|Neural Interface Performance over Time|What improved under comparable tasks and populations?|Avoid incomparable demonstrations.
future_developments|Beyond Therapeutic BCI|What evidence would support workplace or consumer use?|Frame as conditional and separate settings.
myths_vs_facts|A Device That Reads Minds?|What limited task does a reported decoder actually perform?|State training and user cooperation.
documentary_stories|The Life of One Device Trial|How did recruitment, calibration, use, and support unfold?|Use clinical record and participant voice.
assumption_inventory|A Mass-Market Brain Interface|Which efficacy, surgery, privacy, and support premises are needed?|Label research gaps.
readiness_check|Before a Neural Device Trial|Are consent, cybersecurity, service, and exit plans concrete?|Use trial-specific documentation.
physical_limits|Brain Signals and Bandwidth|What noise, stability, and energy constraints bound performance?|Use measured system parameters.
governance_choice|Control of Brain Data|Who may collect, reuse, delete, and audit neural recordings?|Examine actual agreements.
unequal_futures|Access to Neural Assistance|Who receives clinical benefit and who carries ongoing costs?|Consider coverage and maintenance.
scenario_pair|Therapeutic and Workplace Uses|How do consent and power differ between these settings?|Keep device capability fixed.
failure_to_launch|A Device without Continuing Support|What happens if funding or manufacturer service ends?|Use GAO-described risks.
unintended_effect|New Dependence on a Device|Can an improvement create vulnerability to updates or withdrawal?|Document maintenance obligations.
social_adaptation|Life with a Neural Interface|How do users, carers, and clinicians adapt routines?|Use longitudinal reports.
ethical_boundary|Neural Monitoring at Work|What limits should apply to employer access and pressure?|Analyze specific use and rights.
signal_vs_hype|Demo versus Clinical Benefit|Does one controlled task establish everyday performance?|Compare real-world endpoints.
reversible_steps|Stopping a Neural Trial|What data, implant, and care duties continue after withdrawal?|Read protocol and consent form.
field_human_agency|User Control of Output|Can a participant correct or halt unintended device action?|Test practical interface behavior.
field_body_and_identity|Device and Sense of Self|How do participants describe ownership and agency?|Avoid assuming a universal experience.
field_rights_framework|Neural Data Safeguards|Which privacy and research rules apply now?|Specify jurisdiction and device class.
field_resource_inequality|Long-Term Device Access|Who pays for surgery, updates, and replacement?|Use coverage and trial plans.
field_institutional_adaptation|Clinical Support after a Trial|How does a health system plan lifelong follow-up?|Trace duties and funding.
"""

if __name__ == "__main__":
    revise_domain("469", "469_human-robot_society", ROBOT,
                  "Human–robot society through documented shared-space deployments, human labor, safety, agency, public governance, and bounded future scenarios.",
                  "NIST AI human-interaction framework, deployment and incident records, independent task evaluations, procurement documents, and affected-person accounts",
                  "Name robot, task, operator, setting, and date. A demonstration does not establish autonomous or society-wide use.")
    revise_domain("470", "470_transhumanism", TRANSHUMAN,
                  "Transhumanism through the distinction between treatment and enhancement, evidence for interventions, consent, heritability, access, and conditional futures.",
                  "WHO human genome editing governance and recommendations, registered trials, primary philosophical texts, clinical follow-up, and stakeholder accounts",
                  "Name intervention, population, jurisdiction, and time horizon. A philosophical goal or laboratory result is not a proven human benefit.")
    revise_domain("471", "471_brain_enhancement", BRAIN,
                  "Brain enhancement through measured neural-device capabilities, restoration versus enhancement, data control, long-term support, and user agency.",
                  "GAO brain-computer interface assessment, UNESCO neurotechnology recommendation, trial registries and protocols, published endpoints, and participant accounts",
                  "Name device, task, study population, and date. Clinical assistance does not establish above-baseline enhancement or unrestricted thought reading.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
