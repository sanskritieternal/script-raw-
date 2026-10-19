"""Editorial questions for making processes and invention histories."""

from review_angle_plans import audit, revise_domain


MADE = """history_origins|How a Production Process Began|Which material, demand, and tool changes produced one manufacturing method?|Compare dated factory, patent, and trade records.
famous_examples|A Familiar Product's Factory|What does one well-known product's actual process involve?|Follow a named model or batch through public production evidence.
hidden_stories|Workers Behind the Product|Whose sourcing, inspection, maintenance, or packaging labor is omitted?|Use attributed worker accounts and documented process roles.
beginner_explainers|The Stages of Making|How do raw inputs become one finished, tested product?|Map public steps, measurements, and waste without operational instructions.
advanced_concepts|Yield and Quality|How do defects, rework, and process variation affect one production line?|Use defined units, sampling, and consistent denominators.
mysteries_unsolved_cases|A Defect's Uncertain Source|Which process stages could explain one documented product problem?|Compare lot, material, test, and service records with uncertainty.
technology_innovation|A New Production Method|Did one automation or material change improve yield or worker conditions?|Compare before and after with volume, cost, safety, and quality controls.
people_personalities|A Process Designer's Decision|Who proposed and implemented one factory change?|Read engineering notes, worker feedback, and dated results.
major_events|A Factory Disruption|How did one shortage, incident, or rule change alter output?|Trace inputs, downtime, substitutions, quality, and recovery.
how_it_works|One Product's Production Flow|Which operations, tests, and logistics move one product from input to buyer?|Use one facility and period at an explanatory level.
rise_fall|Why a Process Was Replaced|Which cost, quality, safety, or environmental factors favored a new method?|Compare matched output and period-specific constraints.
then_vs_now|Making One Product Across Eras|How did labor, materials, throughput, and waste change?|Use equivalent product functions and measures.
future_developments|A Proposed Production Upgrade|What trial would show whether one planned method scales?|Specify yield, quality, safety, cost, energy, and worker effects.
myths_vs_facts|A Factory Efficiency Claim Checked|Does a claimed speed or sustainability gain survive full-process accounting?|Include upstream inputs, scrap, inspection, energy, and delivery.
documentary_stories|One Batch From Material to Market|How did a documented run proceed from sourcing through acceptance?|Build a dated timeline from production and quality records.
system_boundary|What Counts as Manufacturing?|Which effects belong to supplier, plant, distributor, and user?|Define one product and process boundary before making claims.
input_output_trace|Material and Energy Balance|How much input becomes product, byproduct, scrap, and emissions?|Use public measured units, losses, and uncertainty for a defined run.
design_tradeoff|A Production Compromise|What did one process gain and give up in speed, cost, quality, or worker burden?|Compare requirements, trials, and observed outcomes.
failure_mode|A Production Failure Chain|How did one documented defect pass through controls?|Use public recall or investigation findings without reproducing hazardous steps.
testing_limits|What Factory Inspection Covers|Which defects can one test detect and which may escape?|Compare sampling plan, detection limits, and field results.
standards_interoperability|A Product Meets a Standard|Which versioned specification governed one material or finished item?|Compare test method, certification scope, and independent performance.
security_threat_model|Integrity of a Production System|Which public controls protect product identity and traceability?|Discuss governance and audit outcomes without exposing operational vulnerabilities.
maintenance_lifecycle|Keeping the Line Running|How did machine maintenance affect downtime, defects, and worker load?|Use aggregate service and quality records.
infrastructure_dependencies|Inputs Beyond the Factory|Which water, power, transport, and supplier systems constrain production?|Map public dependencies and impacts without weak-point details.
accessibility_usability|Making for More Users|How did manufacturing tolerances and design affect accessibility?|Compare product tests with user experience across defined groups.
independent_replication|Can a Process Claim Be Reproduced?|Do independent trials support claimed yield, quality, or energy use?|Match input grade, batch size, equipment, and measurement method.
responsible_deployment|A New Line Starts Up|What testing, worker training, oversight, and monitoring preceded release?|Compare startup plan with quality and safety outcomes.
field_prototype_testing|From Pilot Batch to Scale|What did a pilot run prove about full-scale production?|Compare volume, materials, equipment, consistency, and unresolved risks.
field_design_tolerance|Variation Across Units|How did allowable dimensions or composition affect product quality?|Use drawings, control charts, and field failures.
field_manufacturing_method|Choosing a Process Route|Why did one maker use casting, forming, assembly, or another method?|Compare product requirements, yield, cost, and worker effects.
field_failure_investigation|Tracing a Defective Lot|Which evidence identifies a cause rather than a coincidence?|Compare traceability, tests, alternative causes, and corrective action.
field_repair_path|Designed for Repair?|Can a failed product be repaired rather than discarded?|Compare part access, service cost, safety, and actual repair rates."""


INVENTIONS = """history_origins|The Problem Before the Invention|What earlier solutions existed for the task an invention addressed?|Compare dated devices, patents, users, and limitations.
famous_examples|A Famous Invention Reexamined|What did the earliest documented version actually do?|Compare prototype, patent claims, demonstrations, and later stories.
hidden_stories|Collaborators Behind an Inventor|Whose technicians, users, funders, or prior makers shaped an invention?|Use notebooks, patents, team records, and attributed accounts.
beginner_explainers|What Was New?|Which specific feature distinguished one invention from prior art?|Read claims and compare earlier devices without equating patent with success.
advanced_concepts|Inventive Step Versus Adoption|Why can a technically novel idea fail to become useful?|Compare proof of concept, reliability, cost, standards, and user fit.
mysteries_unsolved_cases|A Disputed Priority Claim|Who documented a working idea first, under what definition?|Compare dated notebooks, prototypes, filings, publications, and independent witnesses.
technology_innovation|A Prototype in Test|Which measured result showed an idea might work?|Compare setup, controls, failure modes, and later replication.
people_personalities|An Inventor's Revision|Why did one named inventor change a design after feedback?|Trace dated sketches, tests, collaborators, and constraints.
major_events|Patent, Demo, or Market Launch?|Which milestone actually changed an invention's trajectory?|Separate filing, working demonstration, production, and adoption dates.
how_it_works|From Idea to Useful Product|What steps moved one invention through prototype, testing, manufacture, and service?|Follow a documented case with setbacks and collaborators.
rise_fall|An Invention That Did Not Last|Why did one patented product fail or get replaced?|Compare performance, price, infrastructure, legal rights, and rivals.
then_vs_now|An Invention Across Versions|How did one device change from first prototype to current product?|Compare same function, materials, safety, cost, and users.
future_developments|An Unfinished Invention|What evidence would justify further work on one proposed design?|Set measurable function, reliability, cost, safety, and independent test.
myths_vs_facts|The Lone Genius Story Checked|Does the record support crediting one person alone?|Compare prior art, team records, patents, and parallel efforts.
documentary_stories|An Invention Through Its Archive|How did one idea develop from problem to public use?|Build a dated sequence of notes, prototypes, claims, tests, and adoption.
system_boundary|What the Invention Actually Includes|Which components and services are essential to one claimed function?|Define prototype, product, user, and infrastructure boundaries.
input_output_trace|A Prototype's Measured Function|What input did an early device use and what output did it produce?|Use contemporary test data, units, losses, and limitations.
design_tradeoff|Choosing Between Designs|Why did an inventor favor one material or mechanism over another?|Compare dated options, tests, costs, and later performance.
failure_mode|What a Failed Prototype Taught|Which documented fault prompted one redesign?|Use notebooks and tests without hazardous recreation details.
testing_limits|A Demo Versus Reliable Use|What conditions did one successful demonstration actually cover?|Compare duration, sample, environment, controls, and field experience.
standards_interoperability|An Invention Meets Existing Systems|What standards or interfaces helped or blocked adoption?|Use dated versions and independent compatibility evidence.
security_threat_model|Trust in a New Device|Which broad misuse or privacy concerns arose when an invention was deployed?|Use public design and governance records without bypass instructions.
maintenance_lifecycle|After the Patent|How did repair, updates, or supplies affect useful life?|Compare user records, service data, parts, and costs.
infrastructure_dependencies|The Network an Invention Needed|Which power, distribution, training, or regulatory systems supported it?|Trace public investments and adoption gaps.
accessibility_usability|Who Could Use the First Version?|Which cost, skill, physical, or language barriers limited adoption?|Compare demonstrations with actual users and adaptations.
independent_replication|Could Others Reproduce It?|Did independent teams repeat the original performance claim?|Match materials, design version, measurement, and reported failures.
responsible_deployment|An Invention Enters Public Use|What safety, user testing, and monitoring accompanied rollout?|Compare original safeguards, impacts, and later corrections.
field_prototype_testing|One Prototype's Evidence|Which hypothesis did a particular prototype test?|Examine its build date, procedure, result, and next revision.
field_design_tolerance|Precision Needed for Function|How did variation in parts affect one invention's reliability?|Use drawings and tests at a non-instructional level.
field_manufacturing_method|Making the Invention at Scale|What changed when a handmade prototype entered production?|Compare process, defects, labor, cost, and performance.
field_failure_investigation|Why It Failed in the Field|Which evidence explains a real-world failure after a promising demo?|Compare use conditions, service records, tests, and alternatives.
field_repair_path|Keeping an Invention Useful|Could users repair the device, or did it depend on specialist service?|Compare design, parts, costs, and actual lifespan."""


if __name__ == "__main__":
    revise_domain("088", "088_how_its_made", MADE,
                  "How products are made through actual material flows, workers, production methods, quality controls, scale, waste, and repairability.",
                  "dated process and quality records, manufacturer specifications, independent tests, applicable product standards, recall and service records, and attributed worker accounts",
                  "Name product, plant or process, batch, and date. Separate demonstration from full-scale yield, account for upstream and downstream effects, and avoid hazardous factory instructions or live vulnerabilities.")
    revise_domain("089", "089_inventions_inventors", INVENTIONS,
                  "Inventions and inventors through prior art, dated prototypes, patent claims, collaborators, testing, production, adoption, and service life.",
                  "dated inventor notebooks and drawings, patent filings and prior art, identified prototypes, independent tests, production and user records, and attributed collaborator accounts",
                  "Name invention version, claimed function, jurisdiction, and date. Distinguish patent, working prototype, commercial adoption, and sole-inventor mythology; avoid hazardous replication instructions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
