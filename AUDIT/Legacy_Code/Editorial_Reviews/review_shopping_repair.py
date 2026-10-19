"""Editorial questions for consumer buying guides and repair systems."""

from review_angle_plans import audit, revise_domain


SHOPPING = """history_origins|How Buyers Compared a Product|How did one consumer product's selling terms change over time?|Compare dated catalogs, warranties, prices, and retail access.
famous_examples|A Bestseller Under Review|Did a highly recommended product meet buyers' needs after purchase?|Compare independent tests, repair records, returns, and typical use.
hidden_stories|The Cost Behind the Bargain|Whose labor and materials made one low price possible?|Trace production, delivery, service, and worker conditions with sources.
beginner_explainers|Reading an Offer Before Buying|Which price, warranty, return, and seller terms matter for one product?|Use an actual dated offer and identify exclusions.
advanced_concepts|Total Cost of Ownership|When does the cheapest purchase cost more over its useful life?|Compare energy, consumables, repair, failure, and disposal on one horizon.
mysteries_unsolved_cases|Why Reviews Disagree|Which product or buyer differences explain conflicting reviews?|Check model version, use case, compensation, and sample size.
technology_innovation|A Comparison Tool's Ranking|How does one shopping tool select and order products?|Compare data source, affiliate payments, missing sellers, and results.
people_personalities|The Tester and the Seller|How did one reviewer evaluate a product, and what incentives existed?|Inspect test protocol, disclosures, and seller response.
major_events|A Recall Changes the Choice|What did one product recall reveal about pre-purchase information?|Trace notice, affected models, remedies, and later sales claims.
how_it_works|A Product Comparison That Helps|How can two products be compared for a defined buyer and task?|Set needs, same test conditions, full costs, and tradeoffs.
rise_fall|Why a Popular Product Disappeared|Which factors ended one model's production or sale?|Compare demand, defects, regulation, parts, and replacement.
then_vs_now|Buying the Same Function Across Time|How did price, durability, service, and access change?|Use comparable models and inflation-adjusted total cost.
future_developments|Evaluating a New Product Claim|What evidence should a shopper seek before trusting a proposed improvement?|Define test conditions, relevant outcome, warranty, and independent checks.
myths_vs_facts|Premium Means Durable?|Does higher price predict longer life for one product class?|Compare matched models, repair data, testing, and selection limits.
documentary_stories|A Purchase Through Its Life|How did one product perform from checkout to repair or disposal?|Use consented records and distinguish individual case from typical result.
value_chain|Who Sells and Services It?|Which firms provide manufacture, marketplace listing, delivery, and warranty?|Map responsibilities for one current offer.
incentive_map|Why This Product Is Recommended|Does placement or affiliate payment affect one buying guide?|Read disclosures, rankings, methodology, and product selection.
unit_economics|The Price Beyond the Sticker|Which recurring expenses dominate one product's ownership cost?|Use dated prices and a clearly labeled usage scenario.
consumer_outcome|A Product in Real Use|Does one model deliver its advertised performance under normal conditions?|Compare independent tests with buyer outcomes and failure rates.
market_structure|Are the Alternatives Independent?|Do apparently separate product brands share a manufacturer or service network?|Trace ownership, components, and warranty provider.
risk_transfer|Who Pays When It Fails?|Which warranty terms leave labor, shipping, or downtime to the buyer?|Compare written coverage and actual claims.
regulatory_choice|A Label That Guides Buyers|Did an efficiency or safety label help buyers understand a product?|Test criteria, enforcement, and consumer comprehension locally.
historical_shock|Shopping During a Shortage|How did a supply disruption change prices and available models?|Compare stock, substitutes, seller terms, and affected groups.
data_definition|What Is a Star Rating?|Does an average rating represent verified users of one current model?|Check review age, model mix, incentives, and filtering.
access_and_affordability|Who Can Use the Offer?|Which delivery, financing, language, or accessibility barriers change effective cost?|Compare total terms for defined buyers.
business_failure|A Product Promise That Failed|Which evidence shows why one brand's offer did not last?|Compare claims, service, costs, complaints, and market changes.
long_term_tradeoff|Repairable or Replaceable?|How do parts access and lifespan change the better buy?|Compare purchase, repair, downtime, disposal, and user needs.
field_supply_chain|The Same Model, Different Parts|Did a component or supplier change affect quality across production batches?|Check serial ranges, service bulletins, and controlled tests.
field_brand_claims|Testing a Product Superlative|What evidence supports one best, safest, or most sustainable claim?|Define comparator, measure, date, and certification scope.
field_customer_experience|Buying and Returning It|Can a buyer actually use the advertised return process?|Document steps, fees, deadlines, accessibility, and remedy.
field_market_entry|A New Product Brand|How can buyers evaluate a newcomer without long-term failure data?|Examine tests, parts, warranty backing, and uncertainty.
field_product_lifecycle|The Product After Sale|What options exist for repair, reuse, and disposal?|Compare manufacturer support, independent services, and local facilities."""


REPAIR = """history_origins|How Repair Work Changed|Why did one class of product move from local service to replacement?|Compare design, parts, labor cost, warranties, and consumer habits.
famous_examples|A Repairable Design Examined|Which features made one product easier to maintain?|Compare manuals, parts, disassembly time, and service records.
hidden_stories|The Repair Workers|Whose diagnosis, sourcing, cleaning, and testing work is unseen?|Use attributed shop accounts and invoices with privacy protection.
beginner_explainers|What Repair Involves|How do diagnosis, parts, labor, testing, and warranty fit together?|Follow a completed professional repair without actionable hazardous steps.
advanced_concepts|Repair or Replace Decision|Which factors make a repair worthwhile for a defined product?|Compare fault, parts, labor, safety, remaining life, and environmental effects.
mysteries_unsolved_cases|Why Does the Failure Recur?|Which evidence distinguishes bad parts, design, use, or incomplete diagnosis?|Compare service history, independent assessment, and model-wide data.
technology_innovation|A Diagnostic Tool's Impact|Did one tool improve repair accuracy or access?|Compare false diagnoses, costs, training, and data rights.
people_personalities|A Skilled Repairer's Judgment|How did one professional decide whether to proceed or stop?|Use consented case record, risk assessment, and customer priorities.
major_events|A Repair Rule Changes|What changed after one documented policy or legal reform?|Compare applicability, parts access, prices, and actual repairs in a jurisdiction.
how_it_works|A Repair Workflow in Context|How does a shop take a product from intake to safe return?|Map diagnosis, estimate, approval, parts, work, testing, and documentation.
rise_fall|Why a Repair Shop Closed|Which market and policy pressures affected one local service network?|Compare demand, parts, training, rent, and manufacturer restrictions.
then_vs_now|One Appliance Across Generations|How did maintainability and service access change?|Compare specific models, manuals, parts, lifespan, and costs.
future_developments|Designing for Longer Use|What would show that a new design actually improves repairability?|Predefine parts, access, skill, time, cost, and verified safety.
myths_vs_facts|Repair Always Saves Resources?|When might repair have a smaller or larger footprint than replacement?|Compare remaining life, energy use, materials, transport, and boundaries.
documentary_stories|An Item's Repair History|How did one object move through failures, fixes, and decisions?|Use dated records, costs, user experience, and final outcome.
creative_brief|A Repair for a Real User|What does the owner need from one repair besides restored function?|Set cost, durability, appearance, timing, accessibility, and safety priorities.
materials_and_tools|Parts That Make Repair Possible|Which component and tool access determines whether a fix can be done?|Compare genuine and compatible parts, documentation, cost, and safety.
process_breakdown|Where Diagnosis Matters|Which test distinguished two plausible causes in one professional repair?|Use high-level evidence and avoid hazardous operational instructions.
composition_choice|Repair Visible or Invisible?|How did one conservator or repairer balance function and appearance?|Compare owner priorities, material reversibility, and documentation.
collaborative_authorship|Owner, Maker, and Repairer|Who contributed knowledge and decisions to one successful repair?|Trace consent, design information, diagnosis, and final approval.
adaptation_across_media|A Repair Guide Becomes Video|What safety and context vanish when a repair manual becomes a short clip?|Compare authorized documentation, omissions, and audience interpretation.
audience_reception|Did the Fix Satisfy the User?|How did owners rate durability, cost, and service after repair?|Use follow-up data and note selection bias.
cultural_context|Repair as Local Practice|How does a community's repair network sustain skills and access?|Use consented practitioner accounts and economic context.
preservation_restoration|Repair or Conserve an Heirloom|When should function be restored versus original material retained?|Compare owner, maker, conservator, and cultural priorities.
rights_and_attribution|Access to Repair Information|Who controls manuals, diagnostics, parts, and software access?|Check current law, contracts, safety, and independent service rights.
style_comparison|Two Repair Approaches|How do two approved methods differ in cost, durability, and reversibility?|Compare matched faults and professional assessments.
creative_failure|A Fix That Did Not Hold|What explains one repair's early failure?|Compare diagnosis, parts, testing, use, and warranty response without blame.
field_material_selection|Choosing Compatible Material|How does one replacement material affect safety and longevity?|Use manufacturer specifications and qualified tests, avoiding a how-to.
field_tool_control|Tools and Training Boundaries|Which tasks require specialist tools or certification?|Compare applicable standards, workplace training, and documented risks.
field_pattern_design|Designing a Replacement Part|What dimensions and tolerances matter for a documented non-safety-critical part?|Compare original specification, testing, and service outcome at a high level.
field_repairability|Scoring a Product's Repair Access|Which evidence best represents real repairability?|Measure parts, manuals, time, cost, software locks, and safe testing.
field_craft_lineage|Passing on Repair Skill|How do apprentices learn diagnosis and judgment from experienced workers?|Use consented shop observation and training records."""


if __name__ == "__main__":
    revise_domain("136", "136_shopping_consumer_guides", SHOPPING,
                  "Consumer buying guides through transparent comparison, real terms, total ownership cost, durability, repair, and remedies.",
                  "dated offers and product specifications, independent tests, warranties and return terms, service and recall data, current consumer guidance, and consented buyer accounts",
                  "Name product, model, seller, market, jurisdiction, and date. Disclose affiliate incentives, compare complete costs, and verify current safety and consumer-rights rules.")
    revise_domain("137", "137_repair_maintenance", REPAIR,
                  "Repair and maintenance through diagnosis, skilled labor, parts access, cost, safety, product life, and conservation choices.",
                  "manufacturer and professional service records, parts and warranty terms, qualified test results, current repair and safety rules, and attributed repairer and owner accounts",
                  "Name product, model, fault, jurisdiction, and date. Keep hazardous work at documentary level, refer safety-critical tasks to qualified professionals, and verify current repair rights.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
