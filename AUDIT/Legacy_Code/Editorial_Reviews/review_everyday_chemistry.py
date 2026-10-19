"""Editorial questions for chemistry in everyday life."""

from review_angle_plans import audit, revise_domain


CHEMISTRY = """history_origins|A Familiar Material's Chemical History|Which discovery changed how one household material was made or used?|Compare dated formulations, production records, and regulation.
famous_examples|A Popular Product Claim Tested|Does one cleaning or personal-care product perform as advertised?|Define use, comparator, measure, independent test, and conditions.
hidden_stories|Chemistry in a Supply Chain|Whose mining, refining, blending, and disposal work is overlooked?|Trace a named product and attributed worker accounts.
beginner_explainers|Reading a Product Ingredient List|What do named ingredients actually do in one product?|Use current formulation, amount where available, and intended use.
advanced_concepts|Dose, Exposure, and Hazard|How does actual exposure change the interpretation of one chemical hazard?|Separate hazard, route, amount, duration, population, and uncertainty.
mysteries_unsolved_cases|Why Two Tests Disagree|Which methods or conditions explain conflicting product results?|Compare samples, instruments, thresholds, controls, and reporting.
technology_innovation|A New Formulation's Tradeoffs|Did one replacement ingredient improve a defined outcome?|Compare performance, safety, cost, supply, and disposal.
people_personalities|The Chemist Behind a Product|How did a named team solve one documented formulation problem?|Use patents, laboratory records, independent tests, and credit.
major_events|A Chemical Product Recall|What evidence triggered one recall or restriction?|Trace defect, exposure, agency notice, remedy, and later change.
how_it_works|Why Soap Removes Grease|Which molecular interactions explain a familiar cleaning effect?|Use a bounded example and accurate visual model without a recipe.
rise_fall|An Ingredient Leaves the Market|Why did use of one ingredient decline?|Compare evidence, policy, cost, substitutes, and consumer demand.
then_vs_now|A Product Across Decades|How did one formulation's ingredients and performance change?|Compare actual dated labels and independent tests.
future_developments|A Promised Sustainable Chemical|Which evidence would support one lower-impact claim?|Define lifecycle boundary, performance, hazard, and independent verification.
myths_vs_facts|Natural Means Safe?|Does a claim about natural and synthetic chemicals hold in one case?|Compare chemical identity, dose, exposure, and evidence.
documentary_stories|A Product from Ingredient to Waste|What chemistry matters across one item's full life?|Trace inputs, use, byproducts, recycling, and disposal.
observation_to_explanation|A Color Change Explained|Which chemical and physical causes fit one visible change?|Compare controls, environment, and measured composition.
measurement_method|How a Product's Acidity Is Measured|What does one test measure and how reliable is it?|Explain calibration, temperature, sample matrix, and uncertainty.
scale_and_timespan|Fast Reaction, Slow Degradation|How do reaction and environmental timescales differ for one material?|Use dated measurements and avoid extrapolating from one test.
field_vs_lab|A Laboratory Claim at Home|Why might product performance differ outside controlled testing?|Compare water, temperature, surface, usage, and measurement.
natural_variation|Why One Batch Looks Different|Which harmless or consequential variations occur in one product?|Check manufacturing tolerance, storage, aging, and quality data.
mechanism_chain|From Ingredient to Effect|Which steps connect a molecule to one advertised outcome?|Test each link and separate plausible mechanism from observed benefit.
extreme_case|A Rare Exposure Event in Context|What does one severe case reveal and not reveal about usual use?|Compare dose, route, circumstance, population, and base rate.
classification_debate|Is This a Plastic, Polymer, or Composite?|How do material labels differ in one familiar item?|Compare composition, function, standards, and disposal implications.
interacting_systems|Water Chemistry and Cleaning|How do dissolved minerals affect one cleaner's performance?|Compare water composition, formulation, controlled results, and tradeoffs.
data_gap|An Ingredient with Limited Evidence|What information is missing before a broad safety claim?|Review exposure, long-term outcomes, vulnerable groups, and study quality.
prediction_test|A Formulation Model Meets Reality|Did one prediction match independent product testing?|Compare pretest claim, conditions, result, and uncertainty.
human_impact|A Chemical Choice in Daily Life|Who benefits and who bears costs from one product decision?|Compare performance, exposure, affordability, work, and waste.
field_experimental_setup|A Fair Product Comparison|How can one independent study isolate a chemical claim?|Specify comparator, outcome, controls, replication, and qualified safety.
field_mathematical_model|A Dilution or Decay Model|What assumptions does one simple quantitative model make?|Use published parameters, units, domain, and uncertainty without preparation steps.
field_measurement_error|When a Sensor Misleads|How can calibration or interference distort one chemical reading?|Compare reference test, detection limit, sample matrix, and error.
field_scale_transition|From Sample to Factory|Which chemical behavior changes when production scales up?|Examine heat, mixing, quality, energy, and professional controls at high level.
field_technology_application|Chemistry in an Everyday Device|Which material property enables one product's function?|Compare measured property, design constraint, durability, and disposal.
"""


if __name__ == "__main__":
    revise_domain("156", "156_chemistry_in_everyday_life", CHEMISTRY,
                  "Everyday chemistry through product claims, molecular mechanisms, exposure, measurement, manufacturing, and disposal.",
                  "current product labels and safety information, independent controlled tests, chemical measurements with method and uncertainty, dated regulatory records, and lifecycle data",
                  "Name product, formulation, use, jurisdiction, and date. Distinguish hazard from exposure and mechanism from measured effect; avoid hazardous mixing, synthesis, or home-experiment instructions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
