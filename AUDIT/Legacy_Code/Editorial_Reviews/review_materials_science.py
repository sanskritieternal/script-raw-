"""Editorial questions for materials science."""

from review_angle_plans import audit, revise_domain


MATERIALS = """history_origins|A Material Enters Everyday Use|Which evidence traces one material from invention to adoption?|Compare patents, tests, cost, supply, and early products.
famous_examples|A Famous Material Under Load|Did one celebrated material meet its claimed performance?|Compare independent tests, real service, failure reports, and use conditions.
hidden_stories|The Work Behind a Material|Whose extraction, processing, testing, and disposal labor is invisible?|Follow a named supply chain with attributed worker accounts.
beginner_explainers|What Makes a Material Suitable?|Which properties matter for one defined application?|Compare strength, mass, cost, environment, manufacture, and repair.
advanced_concepts|The Strength-Durability Tradeoff|Why can a material pass a single test but fail over time?|Compare fatigue, corrosion, temperature, wear, and service conditions.
mysteries_unsolved_cases|An Unexpected Material Failure|Which mechanisms fit one documented failure?|Review fracture evidence, loading history, environment, and uncertainty.
technology_innovation|A New Composite's Real Advantage|What does one composite improve and what does it complicate?|Compare matched tests, repair, cost, recycling, and supply.
people_personalities|A Materials Team's Choice|How did engineers select a material for one product?|Use dated specifications, tests, constraints, and design revisions.
major_events|A Failure That Changed a Standard|How did one incident alter testing or material selection?|Trace inquiry, evidence, revised requirements, and adoption.
how_it_works|Structure to Property|How does one material's internal structure affect a measured property?|Use imaging, composition, test method, and limits.
rise_fall|Why a Material Was Replaced|Which performance, cost, safety, or supply factors drove a switch?|Compare equivalent applications and full lifecycle effects.
then_vs_now|Two Generations of One Material|How did production and performance change?|Use comparable grades, test methods, conditions, and price.
future_developments|A Laboratory Material at Scale|What would one prototype need to prove before deployment?|Check repeatability, manufacture, durability, safety, and economics.
myths_vs_facts|Strongest Material for Everything?|Why does one headline property fail to determine best use?|Specify loading, direction, environment, form, cost, and lifetime.
documentary_stories|A Material's Journey into a Product|Where do its measurable properties and tradeoffs matter?|Trace sourcing, fabrication, testing, service, repair, and end of life.
system_boundary|The Material in Its Assembly|Which neighboring parts and conditions change its behavior?|Map joints, coatings, stress, heat, moisture, and maintenance.
input_output_trace|From Raw Feedstock to Finished Part|How do processing choices change material properties?|Compare documented inputs, quality measures, yield, and waste at high level.
design_tradeoff|Lightweight Versus Repairable|How did one design balance mass, strength, price, and service?|Use actual specifications and lifecycle evidence.
failure_mode|Where Cracks Begin|What evidence locates the cause of one material fracture?|Compare site, load history, microstructure, environment, and alternatives.
testing_limits|What a Standard Test Misses|Does one laboratory test represent real service conditions?|Compare sample geometry, duration, variability, and field evidence.
standards_interoperability|A Material Grade's Meaning|How do grades and test standards support interchangeability?|Check current specification, tolerances, certification, and application.
security_threat_model|Counterfeit or Mislabelled Material|How could a false certificate compromise one product?|Trace documentation, traceability, verification, and oversight.
maintenance_lifecycle|A Material in Long Service|How is degradation detected and managed?|Examine inspection, repair, replacement, cost, and failure records.
infrastructure_dependencies|What Production Requires|Which energy, water, equipment, and skills does one material need?|Map actual plant inputs and environmental constraints.
accessibility_usability|Material Choice for Users|How do weight, texture, heat, or cost affect users of one device?|Use diverse user testing and measured properties.
independent_replication|Can the Reported Property Be Repeated?|Do independent labs reproduce one material claim?|Compare samples, methods, conditions, statistics, and data access.
responsible_deployment|A Material's Full Burden|What changes when mining, manufacture, use, and disposal are counted?|Define lifecycle boundary, substitution, and uncertainty.
field_prototype_testing|A Part Outside the Lab|What did one prototype test show under real loading?|Check instrumentation, conditions, failures, comparison, and limits.
field_design_tolerance|How Much Variation Can a Part Take?|Which dimensional or property variations matter in one assembly?|Compare specification, process capability, inspection, and failures.
field_manufacturing_method|Two Ways to Make the Same Part|How do methods affect structure, cost, waste, and reliability?|Use matched parts and qualified test data.
field_failure_investigation|A Failed Part's Evidence Chain|How did investigators preserve and interpret one failed component?|Trace custody, inspection, testing, competing hypotheses, and correction.
field_repair_path|Can This Material Be Repaired?|Which repair method is approved for one product and why?|Check manufacturer guidance, qualified assessment, retesting, and cost.
"""


if __name__ == "__main__":
    revise_domain("157", "157_materials_science", MATERIALS,
                  "Materials science through measured properties, processing, failure, standards, lifecycle, and user-relevant tradeoffs.",
                  "versioned material specifications and test standards, independent laboratory results with conditions, manufacturing records, failure investigations, service data, and lifecycle assessments",
                  "Name material grade, form, product, environment, test method, and date. Avoid claiming one material is universally best; keep hazardous fabrication and safety-critical repair with qualified professionals.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
