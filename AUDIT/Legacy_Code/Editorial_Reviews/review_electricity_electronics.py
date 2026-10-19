"""Editorial questions for electricity and electronics."""

from review_angle_plans import audit, revise_domain


ELECTRONICS = """history_origins|A Circuit That Changed a Product|Which documented design step made one device practical?|Compare patents, prototypes, components, manufacturing, and use.
famous_examples|A Famous Device Under Test|Did one influential electronic product meet its original promise?|Compare specifications, independent tests, price, repair, and user needs.
hidden_stories|The Labor Inside Electronics|Whose mining, fabrication, assembly, testing, and repair work is overlooked?|Trace a named device and attributed worker accounts.
beginner_explainers|Voltage, Current, and Power in Context|What do these measurements say about one ordinary device?|Use labeled units and a verified product specification.
advanced_concepts|Why Efficiency Changes with Load|How does one device's energy performance vary in actual use?|Compare load profile, standby, conversion loss, and test method.
mysteries_unsolved_cases|An Intermittent Electronics Fault|Which evidence can distinguish design, component, and use conditions?|Review service records, failure analysis, and uncertainty.
technology_innovation|A New Component's Advantage|Which measured performance change does one component offer?|Compare equivalent conditions, reliability, cost, and supply.
people_personalities|The Engineers Behind a Device|How did one team balance performance, safety, price, and repair?|Use dated design records, tests, and attributed interviews.
major_events|A Product Recall and Its Cause|What did one electrical recall reveal about oversight?|Trace affected models, investigation, remedy, and later standards.
how_it_works|From Power Source to Output|How do the main blocks of one electronic device work together?|Use a high-level diagram and verified specifications.
rise_fall|Why a Connector or Format Disappeared|Which technical and market factors drove replacement?|Compare compatibility, performance, licensing, price, and adoption.
then_vs_now|One Function Across Device Generations|How did energy, size, durability, and repair change?|Use comparable devices and test conditions.
future_developments|A Proposed Electronics Standard|Would one change improve compatibility or safety?|Check current draft, tests, affected devices, costs, and alternatives.
myths_vs_facts|A Device Efficiency Claim|Does a marketing figure hold in typical conditions?|Define measurement boundary, load, temperature, and independent test.
documentary_stories|A Device from Design to Disposal|Where do benefits and burdens arise across its life?|Trace materials, fabrication, use, repair, and e-waste handling.
system_boundary|What Is Inside the Device Claim?|Which power supplies, accessories, and software affect performance?|Map components and state the test boundary.
input_output_trace|Power Into Useful Work|Where does electricity go in one device?|Use measured input, output, heat, standby, and uncertainty.
design_tradeoff|Small Size Versus Repair|How did one product balance compact design and service access?|Compare performance, fasteners, parts, warranty, and lifespan.
failure_mode|A Component's Failure Chain|Which evidence connects an initial fault to final device failure?|Use qualified inspection, service data, and alternative causes.
testing_limits|A Lab Rating in Real Use|Does a certification test represent ordinary loads and environments?|Compare test standard, sample, temperature, usage, and aging.
standards_interoperability|Can Two Devices Work Together?|Which standard versions and implementations determine compatibility?|Check current specifications, certification, and real interoperability.
security_threat_model|A Connected Device's Data Risks|What information does one product collect and transmit?|Map data flow, access, updates, retention, and user controls.
maintenance_lifecycle|A Device After Sale|How do updates, parts, and battery life affect long-term use?|Compare support period, repair records, costs, and retirement.
infrastructure_dependencies|The Network and Power Behind It|Which external systems must work for one electronic device?|Trace grid, charger, connectivity, cloud service, and failure modes.
accessibility_usability|Who Can Operate the Device?|Which controls, labels, interfaces, and costs exclude users?|Use diverse user testing and accessible-design criteria.
independent_replication|Can the Test Be Repeated?|Do independent labs reproduce one electronics claim?|Compare samples, firmware, configuration, methods, and error.
responsible_deployment|A Device in Everyday Life|How are safety, privacy, repair, and disposal handled?|Review documentation, actual practice, user remedies, and regulation.
field_prototype_testing|A Prototype Before Launch|What did early tests establish and leave uncertain?|Check sample size, conditions, failure log, and next tests.
field_design_tolerance|How Precise Must Components Be?|Which tolerances affect one device's reliability?|Compare specification, manufacturing variation, inspection, and failures.
field_manufacturing_method|Making a Circuit at Scale|How did production choices affect quality and cost?|Use high-level process records and measured yield, not hazardous instructions.
field_failure_investigation|Following a Returned Device|How did one company identify a recurring fault?|Trace complaint, examination, root-cause evidence, and correction.
field_repair_path|Can a Device Be Serviced?|Which parts and information are available for qualified repair?|Check model, warranty, access, safety, cost, and local rights.
"""


if __name__ == "__main__":
    revise_domain("161", "161_electricity_electronics", ELECTRONICS,
                  "Electrical and electronic devices through measured function, standards, design tradeoffs, repair, safety, privacy, and lifecycle.",
                  "versioned product specifications and standards, independent electrical tests, recalls and failure reports, repair documentation, manufacturing records, and consented user and worker accounts",
                  "Name model, version, use, jurisdiction, and date. Keep mains electricity, batteries, and circuit work at documentary level and refer hazardous testing or repair to qualified professionals.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
