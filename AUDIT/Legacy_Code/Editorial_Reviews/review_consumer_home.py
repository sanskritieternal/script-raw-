"""Editorial questions for consumer technology and home life."""

from review_angle_plans import audit, revise_domain


CONSUMER = """history_origins|A Consumer Device Category Emerges|Which need, component, price, and distribution choices enabled one device category?|Compare dated product records, standards, pricing, and user accounts.
famous_examples|A Hit Gadget Reexamined|What did one celebrated device deliver beyond its marketing promise?|Compare exact model, launch claims, independent tests, support, and user outcomes.
hidden_stories|People Behind a Device|Whose assembly, repair, software, accessibility, or support work is overlooked?|Use attributed worker accounts, credits, service records, and supply evidence.
beginner_explainers|The Device and Its Services|Which functions run on a consumer device and which depend on apps, accounts, or cloud services?|Map one feature's public components and data flow.
advanced_concepts|A Device's Real Cost of Use|How do purchase price, subscriptions, consumables, energy, and replacement interact?|Compare transparent total-cost scenarios for a named model and period.
mysteries_unsolved_cases|An Unexplained Product Failure|Which documented causes could explain one repeated consumer-device problem?|Compare defect reports, service notices, independent tests, and uncertainty.
technology_innovation|A New Feature in Daily Use|Did one consumer-device innovation improve a measurable task?|Compare matched users and devices, accessibility, energy, and tradeoffs.
people_personalities|A Product Decision and Its Makers|Who chose one consequential feature or limitation?|Trace design records, interviews, regulatory filings, and user feedback.
major_events|A Product Recall or Support End|What changed for owners after one recall or end-of-support notice?|Use dated notices, remedies, user impact, and follow-up.
how_it_works|From Tap to Result|How does one consumer-tech task pass through hardware, software, data, and service?|Trace public interfaces without exposing accounts or security vulnerabilities.
rise_fall|A Gadget's Market Life|Why did one product line grow, decline, or disappear?|Compare demand, competitors, ecosystem ties, repair, and support dates.
then_vs_now|One Household Task Across Device Generations|Did a new device make the task easier, cheaper, or more reliable?|Compare equivalent tasks and total cost across dated products.
future_developments|A Proposed Consumer Feature|What evidence would show that a planned feature benefits users?|Specify testing, accessibility, privacy, support, price, and failure conditions.
myths_vs_facts|A Gadget Claim Checked|Does a battery, speed, safety, or privacy slogan match independent evidence?|Name model, version, test conditions, and claim wording.
documentary_stories|One Device From Launch to Retirement|How did a product move through updates, failures, repair, and disposal?|Build a dated record from manuals, advisories, tests, and owner accounts.
system_boundary|Where a Device Ends|Which parts of one feature depend on device, app, network, cloud, or third party?|Draw a public component boundary and distinguish local from remote behavior.
input_output_trace|What Data a Device Uses|Which inputs produce one advertised output and where do they go?|Use public documentation and safe sample data, marking unknown transfers.
design_tradeoff|A Gadget Design Compromise|What did thinness, battery life, cost, durability, or repairability gain or sacrifice?|Compare design claims with matched tests and service evidence.
failure_mode|A Product Failure's Chain|How did one documented defect reach consumers?|Use public investigation or recall findings, impact, and corrective action.
testing_limits|The Limits of a Product Test|Which real use conditions did a lab test or certification omit?|Compare protocol with user conditions and uncertainty.
standards_interoperability|Devices That Should Work Together|Did one device meet a named interface standard across brands?|Check standard version and independent interoperability tests.
security_threat_model|Trust in a Connected Device|What data and control boundaries should one product protect?|Use public security documentation and high-level test outcomes without bypass steps.
maintenance_lifecycle|Updates and Repair Across Years|How did software support and parts availability affect a device's useful life?|Compare dated support policy, updates, service records, and owner costs.
infrastructure_dependencies|What a Smart Product Needs|Which power, network, account, or service dependencies affect one feature?|Map dependencies and published outages without live weak-point detail.
accessibility_usability|Can More People Use It?|How well does a device support different sensory, motor, and cognitive needs?|Compare documented features with testing by affected users.
independent_replication|Checking a Product Benchmark|Can a maker's claim be reproduced by independent testers?|Match firmware, settings, workload, sample, and measurement method.
responsible_deployment|Introducing a Connected Product|What testing, disclosures, update plans, and support accompanied launch?|Compare public commitments, early issues, and remedy outcomes.
field_software_architecture|Software Behind a Gadget|How are device firmware, app, and cloud responsibilities divided?|Map versioned interfaces and what happens when one part loses support.
field_interface_design|A Control People Understand|Did a device's physical or digital controls reduce errors?|Compare usability tests, accessibility, and observed user problems.
field_version_changes|A Firmware Update's Effects|Which features or behaviors changed in one product update?|Use release notes, matched tests, and user-impact reports.
field_open_standards|Open Compatibility in Practice|Does a claimed open standard allow independent devices to interoperate?|Name version, certification, and cross-brand tests.
field_technical_debt|Old Decisions in a New Device|Which legacy interface or dependency raises current cost or limits support?|Trace design history, compatibility demands, and migration options."""


HOME = """history_origins|A Household Practice Changes|Which technology, housing, labor, or social changes shaped one home routine?|Compare dated household records, design, and accounts across groups.
famous_examples|A Model Home Reexamined|How did one widely promoted home design work for actual residents?|Compare design claims, costs, maintenance, and occupant experience.
hidden_stories|Labor Behind a Comfortable Home|Whose cleaning, caregiving, repair, or service work is invisible in one idealized lifestyle?|Use attributed accounts and time-use or expenditure data.
beginner_explainers|A Home Choice in Context|What tradeoffs matter when evaluating one household design or routine?|Define residents, space, budget, access, climate, and maintenance.
advanced_concepts|Whole-Life Cost of a Home Choice|How do installation, energy, cleaning, repair, and replacement alter the calculation?|Compare transparent scenarios and uncertain assumptions.
mysteries_unsolved_cases|Why a Home Intervention Failed|Which factors explain a gap between expected and observed household outcomes?|Compare setup, behavior, building condition, and measurement limits.
technology_innovation|A Home Technology Under Test|Did one device or material improve comfort, safety, or effort?|Use independent tests and resident outcomes in a defined setting.
people_personalities|Who Designed the Domestic Ideal?|Whose values shaped one influential housing or lifestyle proposal?|Trace original plans, promotional material, critics, and residents.
major_events|A Housing Change in Daily Life|How did one policy or market shock alter a household practice?|Compare before and after using dated costs and resident accounts.
how_it_works|A Home System in Use|How do layout, ventilation, heating, storage, and routines interact?|Map one lived setting without building or health instructions.
rise_fall|A Home Trend's Lifecycle|Why did one design or lifestyle trend spread and later change?|Compare media, cost, available materials, and user experience.
then_vs_now|A Household Task Across Generations|How did time, cost, energy, and responsibility for one task change?|Use comparable tasks and account for unpaid labor.
future_developments|A Proposed Home Upgrade|What evidence would justify one household retrofit or new routine?|Define outcomes, full cost, accessibility, maintenance, and local rules.
myths_vs_facts|A Home Claim Checked|Does a popular claim about efficiency, cleanliness, or value fit measured evidence?|Specify home type, climate, measurement, and uncertainty.
documentary_stories|One Home's Changing Use|How did residents adapt a home over time?|Build a dated sequence from plans, repairs, costs, and consented accounts.
lived_experience|A Resident's Daily Route|Which parts of a home help or hinder one resident's ordinary routine?|Use consented observation and avoid treating one household as typical.
institutional_pathway|Who Supports a Home Change?|Which landlord, owner, builder, insurer, or local authority controls one repair?|Map actual responsibilities and dated process in a jurisdiction.
incentives_norms|Why a Household Choice Persists|How do time, money, tenancy, and social expectations shape one routine?|Compare stated preferences with practical constraints.
access_and_exclusion|Who Is Left Out of a Home Ideal?|Which cost, tenure, mobility, or space barriers block one proposed lifestyle?|Use defined households and local conditions.
community_variation|Different Homes, Different Practices|How does one home routine vary across households and places?|Compare matched tasks while respecting cultural and climate differences.
policy_in_practice|A Housing Standard at Home|Did a dated housing rule change actual living conditions?|Compare rule text, inspections, implementation, and resident outcomes.
survey_vs_story|Household Data and Experience|Do survey averages explain one resident's account?|Check question wording, sample, denominator, and context.
power_and_voice|Who Decides in the Household?|Whose needs prevail in one home design or purchase decision?|Use consented accounts and identify decision rights without stereotyping.
unintended_consequence|A Home Fix With a Side Effect|Did one change improve one outcome while worsening another?|Compare measured air, heat, energy, noise, or maintenance outcomes as relevant.
comparative_setting|Two Homes, One Need|How do two housing types meet the same household need?|Match climate, residents, space, tenure, and cost before comparing.
change_over_time|A Routine After a Life Change|How did aging, caregiving, or remote work alter use of one home?|Use dated accounts and access needs, protecting privacy.
ethical_dilemma|A Household Tradeoff|How should owners weigh affordability, comfort, and impacts on other residents?|State affected groups, options, costs, and authority.
field_space_constraints|Designing for Limited Space|Which layout choices improved use of one small home?|Compare measured space, circulation, storage, and resident feedback.
field_household_cost|What a Home Choice Really Costs|How do upfront, recurring, and replacement costs compare?|Use local prices and transparent household scenarios, not personal advice.
field_design_for_access|A Home Accessible to Its Residents|Which design barriers affected a defined resident group?|Compare current standards with user testing and feasible adaptations.
field_maintenance_burden|Who Keeps the Home Working?|How much time and money does one feature require to maintain?|Use service records and resident accounts over a stated period.
field_material_lifecycle|From Material Purchase to Disposal|What environmental and repair effects follow one home-material choice?|Compare product declarations, durability, repair, and end-of-life evidence."""


if __name__ == "__main__":
    revise_domain("063", "063_consumer_technology", CONSUMER,
                  "Consumer technology through device and service boundaries, independent performance tests, privacy, accessibility, repair, cost, and support life.",
                  "dated product manuals and support policies, standards and certification records, independent matched tests, recalls and advisories, and attributed owner and worker accounts",
                  "Name exact model, firmware, region, and test conditions. Separate marketing claims from measured outcomes, check current support and privacy terms, and avoid account or security bypass details.")
    revise_domain("064", "064_home_lifestyle", HOME,
                  "Home and lifestyle through resident needs, household labor, space, cost, access, housing systems, materials, and measured daily outcomes.",
                  "dated plans and housing rules, independent material and performance tests, household expenditure and time-use data, service records, and consented resident accounts",
                  "Name household, housing type, tenure, climate, place, and date. Label cost scenarios, protect resident privacy, and verify current local housing and health guidance before production.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
