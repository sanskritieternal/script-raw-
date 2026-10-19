"""Editorial question designs for cultivated products and automation."""

from review_angle_plans import audit, revise_domain


LAB = """history_origins|From Tissue Culture to Cultivated Product|Which laboratory technique became a proposed consumer process?|Trace dated evidence.
famous_examples|A Cultivated Food Product|What did an actual consultation and inspection cover?|Read regulator records.
hidden_stories|Labor inside a Lab-Grown Supply Chain|Whose cell sourcing, cleaning, quality, and care work is invisible?|Follow one product.
beginner_explainers|What Can Be Grown in a Lab?|How do cultured cells, fermentation, and synthetic materials differ?|Name feedstock and output.
advanced_concepts|Scaling a Cell Culture Process|Which yield, contamination, and media constraints matter?|Use measured pilot data.
mysteries_unsolved_cases|A Sustainability Promise|What life-cycle evidence would test land, energy, and water claims?|Declare system boundary.
technology_innovation|A Growth-Media Change|Did it reduce cost or improve reliable yield?|Compare controlled production data.
people_personalities|A Product Developer's Tradeoff|How did safety, cost, or texture shape one design?|Use attributed project record.
major_events|A Regulatory Milestone|What did an authorization actually permit?|Name product and jurisdiction.
how_it_works|From Cell Bank to Product|How do growth, harvest, processing, testing, and labeling connect?|High-level process map.
rise_fall|A Lab-Grown Venture Changes Course|Which cost, demand, or scale challenge mattered?|Use filings and output data.
then_vs_now|Pilot Batch and Commercial Plant|What changed in throughput, consistency, and inspection?|Use comparable units.
future_developments|Possible Cultivated Products|Which technical and market milestones are needed?|State scenario assumptions.
myths_vs_facts|Lab-Grown Means Impact-Free?|Which inputs and waste streams still matter?|Use full life-cycle evidence.
documentary_stories|One Product's Route to Sale|How did research, consultation, inspection, and launch unfold?|Build dated record.
assumption_inventory|A Lab-Grown World|Which price, capacity, feedstock, and consumer premises are needed?|Quantify where possible.
readiness_check|Before Wider Production|Are quality, safety, labeling, and supply plans validated?|Use product-specific rules.
physical_limits|Energy and Nutrient Inputs|What mass and power are required per unit output?|Use measured yields.
governance_choice|Who Oversees Cultivated Products?|How do food, biotech, and environmental agencies divide duties?|Name jurisdiction.
unequal_futures|Access to Cultivated Goods|Who can afford them and who loses existing livelihoods?|Assess workers and consumers.
scenario_pair|Two Production Pathways|How do cultivated and conventional products compare on a common boundary?|Align output and context.
failure_to_launch|A Product That Stayed a Prototype|What bottleneck blocked regular manufacturing?|Use production and finance evidence.
unintended_effect|Shifted Supply-Chain Burden|Could a lab product increase specialized input demand?|Track upstream materials.
social_adaptation|People Evaluate a New Food|How do labeling, taste, and trust affect uptake?|Use representative consumer evidence.
ethical_boundary|Claims without Production Evidence|When should marketing avoid environmental or welfare claims?|Check proof and wording.
signal_vs_hype|Demo Meal versus Market Product|What volume, price, and safety record exists?|Separate tasting from supply.
reversible_steps|Pilot Plant Exit|How can waste, contracts, and workers be handled if production stops?|Check shutdown plan.
field_resource_budget|A Cultivation Input Ledger|How much media, water, energy, and cleaning material is used?|Use facility data.
field_habitat_design|Designed Production Environment|How do sterile conditions and worker access shape a plant?|Use actual facility controls.
field_governance_model|Accountability for a Cultivated Product|Who verifies safety and hears complaints?|Map approvals and recall routes.
field_dependency_chain|One Missing Growth Input|What happens when a critical medium or component is unavailable?|Trace alternatives.
field_social_inclusion|Communities in a Food Transition|Do farmers, workers, and consumers shape decisions?|Check consultation outcomes.
"""

INDUSTRY = """history_origins|Factory Automation to Autonomous Industry|Which tasks gained closed-loop control and which still need people?|Trace dated systems.
famous_examples|An Automated Production Line|What runs without intervention and when do operators step in?|Use site evidence.
hidden_stories|Human Work behind Autonomy|Who programs, cleans, maintains, and handles exceptions?|Observe full shift.
beginner_explainers|Automation versus Autonomy in a Plant|What can a machine sense, decide, and change within limits?|Name task and boundary.
advanced_concepts|Control under Uncertainty|How do sensors, quality checks, and safe stops interact?|Use one process diagram.
mysteries_unsolved_cases|A Productivity Gain Claim|Did total output per paid hour improve after installation?|Include downtime and rework.
technology_innovation|A Flexible Robotic Cell|What product variation and failure rate can it handle?|Use repeat tests.
people_personalities|A Technician's Changed Job|How did training, authority, and workload shift?|Use consented account.
major_events|A Plant Conversion Decision|What cost and labor terms accompanied automation?|Read records and agreements.
how_it_works|From Order to Finished Product|Where do people approve, inspect, and repair decisions?|Map workflow.
rise_fall|An Automation Project Rolled Back|What reliability or cost issue made manual work return?|Compare records.
then_vs_now|Before and after Plant Automation|How did safety, quality, staffing, and throughput change?|Use matched periods.
future_developments|A More Autonomous Factory|Which reliability and worker-safety milestones are needed?|Conditional forecast.
myths_vs_facts|Lights-Out Factory?|Which tasks still require humans and external services?|Audit site operations.
documentary_stories|One Production Fault|How did detection, stop, diagnosis, and restart occur?|Use incident trail.
assumption_inventory|Autonomous Industry Scenario|Which sensor, material, power, and labor assumptions hold it together?|List uncertainties.
readiness_check|Before Unattended Operation|Are hazard assessment, stop controls, and recovery tested?|Use site-specific evidence.
physical_limits|Wear, Tolerance, and Materials|Which process variations exceed automated control?|Measure scrap and stoppages.
governance_choice|Who Approves Machine Decisions?|How are safety and quality authority assigned?|Map actual roles.
unequal_futures|Automation Benefits and Worker Costs|Who gains productivity and who faces retraining or displacement?|Disaggregate occupations.
scenario_pair|Two Factory Designs|How do high automation and worker-assist models compare?|Hold product and output fixed.
failure_to_launch|A Pilot Cell without Plant Rollout|Which integration or return hurdle stopped it?|Use technical and financial data.
unintended_effect|New Maintenance Hazard|Did automation expose technicians during non-routine work?|Check incident and task data.
social_adaptation|Teams around Machines|How do supervisors and operators change reporting and trust?|Observe practice.
ethical_boundary|Worker Monitoring with Automation|What data collection is necessary and proportionate?|Use policy and worker voice.
signal_vs_hype|Autonomous Factory Headline|What share of time and tasks are truly unattended?|Measure shifts and exceptions.
reversible_steps|Manual Fallback|Can the plant operate safely when automation fails?|Test a documented fallback.
field_resource_budget|Automation Resource Ledger|How do energy, sensors, spares, and scrap affect total cost?|Include lifecycle.
field_habitat_design|A Safe Shared Workcell|How do guard zones, reach, and maintenance access work?|Inspect site plan.
field_governance_model|Industrial AI Accountability|Who records changes, audits faults, and authorizes restart?|Map procedures.
field_dependency_chain|A Supply or Software Outage|Which production steps stop and which can continue?|Stress-test dependencies.
field_social_inclusion|Workers in Design Decisions|Who had input on tasks, training, and safety?|Compare consultation with outcomes.
"""

TRANSPORT = """history_origins|From Driver Aid to Automated Travel|Which control functions entered service first?|Use dated deployment evidence.
famous_examples|A Driverless Service in One City|Where, when, and under what conditions does it operate?|Check operator and regulator records.
hidden_stories|Remote Help and Street Labor|Which operators, cleaners, responders, and road users support the system?|Map full service.
beginner_explainers|Assistance versus Automated Driving|Who monitors the road and takes over at each level?|Use system-specific definitions.
advanced_concepts|Operational Design Domain|How do weather, roads, speed, and maps bound performance?|Read safety case.
mysteries_unsolved_cases|Is a Service Safer?|Which exposure and comparison group make crash rates meaningful?|Use miles and severity.
technology_innovation|A New Perception Stack|Which failure mode did a sensor or software change improve?|Check independent test evidence.
people_personalities|A Rider or Street User's Experience|What does one account reveal about access or confusion?|Use consent and context.
major_events|An Automated Vehicle Incident|How did investigation, recall, and deployment response unfold?|Use regulator records.
how_it_works|A Driverless Trip|How do dispatch, localization, driving, remote help, and emergency response connect?|Map one service.
rise_fall|A Deployment Suspended|Which safety or regulatory issue led to pause?|Trace dated decisions.
then_vs_now|Trial Routes and Public Service|What changed in ODD, supervision, and exposure?|Compare scope fairly.
future_developments|Wider Automated Transport|Which weather, safety, access, and insurance conditions remain?|Keep forecast conditional.
myths_vs_facts|Self-Driving Everywhere?|What places and conditions are excluded from a named system?|Read ODD.
documentary_stories|One Crash Investigation|What evidence established sequence and contributing factors?|Use official report.
assumption_inventory|Autonomous Mobility Scenario|Which mapping, infrastructure, connectivity, and policy premises matter?|Expose dependence.
readiness_check|Before a New Route Opens|Are road users, emergency services, and fallback plans covered?|Check local approvals.
physical_limits|Rain, Glare, and Road Geometry|What environmental constraints change sensor performance?|Use measured tests.
governance_choice|Who Permits and Monitors a Service?|How do local, state, and national roles differ?|Name jurisdiction and date.
unequal_futures|Who Gains Mobility?|Does the service include disability access and underserved areas?|Check route and price data.
scenario_pair|Two Transport Automation Models|How do fixed-route shuttle and flexible robotaxi risks differ?|Hold region explicit.
failure_to_launch|A Pilot without Expansion|Which safety, cost, or demand barrier stopped growth?|Use follow-up data.
unintended_effect|Road Users Adapt to Driverless Cars|Do pedestrians or drivers change behavior around them?|Use field observations.
social_adaptation|Transport Staff after Automation|How do driving, dispatch, and emergency roles change?|Use workforce evidence.
ethical_boundary|Testing on Public Roads|What consent and safety obligations are owed to bystanders?|Review actual safeguards.
signal_vs_hype|Demo versus Dependable Service|What trips and interventions were measured over time?|Separate showcase and operations.
reversible_steps|Safe Pull-Over and Suspension|Can a system reach minimal risk and stop service after faults?|Test documented procedure.
field_resource_budget|Fleet Energy and Maintenance|What vehicle, compute, cleaning, and repair inputs are needed?|Use operating data.
field_habitat_design|Streets for Automated and Human Users|What curb, crossing, and access design matters?|Study real street conditions.
field_governance_model|Incident Accountability|Who preserves logs, investigates, and remedies harm?|Map operator and regulator duties.
field_dependency_chain|When Maps or Connectivity Fail|Which trip functions remain safe?|Test degraded operation.
field_social_inclusion|Public Voice on Routes|Can riders, workers, and vulnerable road users shape deployment?|Assess consultation.
"""

if __name__ == "__main__":
    revise_domain("484", "484_lab-grown_world", LAB,
                  "Lab-grown products through actual cell culture, production scale, safety oversight, resource inputs, labor, and consumer access.",
                  "FDA cultured-cell food consultations, USDA inspection guidance, product-specific production and life-cycle data, worker records, and consumer research",
                  "Name product, process, jurisdiction, and scale. A prototype tasting or consultation does not prove mass supply or environmental superiority.")
    revise_domain("485", "485_autonomous_industry", INDUSTRY,
                  "Autonomous industry through bounded automated tasks, human operators, non-routine safety, production evidence, and worker participation.",
                  "OSHA robotics guidance, plant operating and incident records, independent productivity measures, contracts, and worker accounts",
                  "Name plant, process, shift, and automation boundary. Unattended operation in one cell is not a fully autonomous industry.")
    revise_domain("486", "486_autonomous_transportation", TRANSPORT,
                  "Autonomous transportation through operational design domains, measured safety, remote support, accessibility, road users, and public oversight.",
                  "NHTSA automated-driving guidance and crash reports, UNECE framework, operator safety cases, route and exposure data, and local approvals",
                  "Name system, route, jurisdiction, date, and conditions. Driver assistance and limited driverless service are different; crash counts need exposure.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
