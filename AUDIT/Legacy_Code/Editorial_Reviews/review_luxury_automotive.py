"""Editorial question review for luxury lifestyles and automotive stories."""

from review_angle_plans import audit, revise_domain


LUXURY = """history_origins|How a Luxury Signal Emerged|What made one product or practice a marker of status in a defined period?|Trace production, price, buyers, and contemporary accounts without assuming timeless prestige.
famous_examples|A Luxury House Under the Lens|What makes one celebrated brand's product distinctive beyond its marketing?|Compare materials, workmanship, scarcity, service, and independent evidence.
hidden_stories|Workers Behind the Finish|Whose labor is missing from the story of one luxury product?|Trace suppliers, artisans, pay or conditions where documented, and credited design.
beginner_explainers|What Buyers Pay For|Which parts of a luxury price reflect materials, craft, distribution, service, and brand?|Use a named product and available disclosures; mark unknown margins.
advanced_concepts|Scarcity by Design|How does controlled supply influence the market for one luxury item?|Examine production limits, waitlists, resale, and alternative explanations.
mysteries_unsolved_cases|An Unverified Provenance Claim|Can a famous object's ownership or origin story be established?|Compare dated records, material tests, and missing links without treating legend as fact.
technology_innovation|A New Technique in Luxury Making|What changed in quality or scale after one manufacturing technique appeared?|Compare dated products, production records, repairability, and labor effects.
people_personalities|The Named Designer and the Team|How much of one product's design can be attributed to a celebrated figure?|Use credits, archives, and collaborator accounts.
major_events|A Sale That Changed Perception|Did one auction, launch, or endorsement alter a luxury market?|Compare transaction records and later prices while accounting for broader trends.
how_it_works|From Material to Finished Object|What stages turn one raw material into a luxury item?|Trace sourcing, design, fabrication, quality control, and sale.
rise_fall|When Prestige Faded|Why did one luxury line lose demand or change position?|Compare product decisions, price, distribution, consumer data, and macro conditions.
then_vs_now|An Object Across Two Eras|How did the making and buying of one luxury category change?|Use comparable products and dated price, material, and audience evidence.
future_developments|A Luxury Strategy Under Test|What evidence would show whether a new brand strategy works?|Set measurable product, customer, labor, and environmental outcomes rather than predicting prestige.
myths_vs_facts|Testing an Exclusivity Claim|Does a brand's claim of rarity or handmaking match available evidence?|Check production count, processes, definitions, and independent records.
documentary_stories|One Object's Full Journey|What happened to one luxury item from sourcing to resale or repair?|Use documented chain of custody, ownership consent, and condition records.
value_chain|Where the Price Accumulates|Which stages of one product's chain capture value?|Compare known input, labor, wholesale, retail, and resale figures with gaps labeled.
incentive_map|Why Limit Supply?|What incentives do maker, retailer, reseller, and buyer face in one luxury market?|Map documented policies and behavior without presuming motives.
unit_economics|A Product's Cost Structure|What can public evidence reveal about the economics of one item?|Separate reported costs from estimates and explain confidentiality limits.
consumer_outcome|The Ownership Experience|What did owners actually receive beyond the initial product?|Examine service, durability, resale, warranty, and documented complaints.
market_structure|Who Controls Access?|How do authorized dealers, limited releases, and secondary markets interact?|Use one brand and period with actual channel rules.
risk_transfer|Who Bears the Risk of Prestige?|Which risks fall on makers, workers, retailers, or buyers when demand shifts?|Use contracts and documented outcomes for a bounded case.
regulatory_choice|Rules Behind a Luxury Claim|Which labeling, import, or environmental rule applies to one marketed claim?|Name jurisdiction and date; read the primary rule and enforcement record.
historical_shock|Luxury Demand in a Downturn|How did one documented shock affect production, employment, and sales?|Compare company and market records before and after.
data_definition|What Counts as Luxury Sales?|How do market reports define one luxury segment?|Inspect inclusion, geography, currency, price level, and missing firms.
access_and_affordability|The Cost of Entry|How did price and purchasing terms change access to one product?|Compare real prices, eligibility, financing terms, and resale fees.
business_failure|When a Luxury Venture Failed|Which decisions and conditions preceded one documented failure?|Use filings and dated accounts; avoid a single-cause morality tale.
long_term_tradeoff|Buy, Maintain, or Resell|What financial and material tradeoffs follow long ownership of one item?|Compare documented repair, storage, depreciation, and environmental evidence.
field_supply_chain|Following a Material|Can a brand's stated material origin be verified?|Trace available certificates, suppliers, audits, and gaps in chain of custody.
field_brand_claims|Reading a Sustainability Claim|What exactly does one luxury brand's environmental claim cover?|Check boundaries, measurements, verification, and excluded impacts.
field_customer_experience|Service Behind the Price|How consistently is a stated luxury service delivered?|Compare policy, observed cases, and selection bias.
field_market_entry|A New Label's Path|How did one entrant obtain production capacity, distribution, and recognition?|Trace dated financing, partnerships, channels, and sales evidence.
field_product_lifecycle|After the Sale|What happens to one luxury item through repair, reuse, and disposal?|Use service records, material composition, and secondhand outcomes."""


CARS = """history_origins|The Origin of a Vehicle Design|Which problem did an early automobile design try to solve?|Compare dated prototypes, patents, road conditions, and contemporary use.
famous_examples|An Iconic Car Reassessed|What technical and social choices made one model influential?|Use specifications, sales, ownership accounts, and contemporary rivals.
hidden_stories|Workers and Suppliers Behind a Car|Which engineering, manufacturing, or maintenance labor is omitted from a famous car story?|Trace credited teams and supply records without assuming one inventor.
beginner_explainers|How a Car Moves and Stops|What path does energy take from source to wheels and brakes in one vehicle?|Use a named model and distinguish powertrain, control, and braking systems.
advanced_concepts|A Vehicle Tradeoff Quantified|How do mass, aerodynamics, power, and energy use interact in one design?|Compare measured results under stated test conditions.
mysteries_unsolved_cases|Investigating a Vehicle Failure|Which explanations for one documented defect remain supported?|Read investigation records and separate reported symptoms from proven cause.
technology_innovation|A Safety Feature Introduced|Did one new feature improve a measured outcome?|Compare design, test evidence, real-world data, and adoption period.
people_personalities|The Engineer and the Team|How did a named engineer's decisions shape one vehicle?|Use patents, project records, and collaborator accounts.
major_events|A Recall and Its Aftermath|What triggered one recall, and what did the remedy change?|Trace dated defect reports, investigation, notice, and completion data.
how_it_works|Inside One Vehicle System|How does one drivetrain, braking, or steering system operate?|Define components and inputs, then explain normal operation and limits.
rise_fall|Why a Model Was Discontinued|What evidence explains a car model's production end?|Compare demand, compliance, costs, reliability, and maker statements.
then_vs_now|A Car Type Across Two Generations|What changed in safety, energy use, and maintainability?|Compare models with similar roles under comparable measurements.
future_developments|A Vehicle Technology Claim to Test|What evidence would establish a proposed feature's benefit?|Define test conditions, failure modes, cost, and deployment limits.
myths_vs_facts|Checking a Car Performance Claim|Does a marketed range, efficiency, or safety statement match its test basis?|Identify cycle, configuration, temperature, and real-world variation.
documentary_stories|A Vehicle from Design to Road|How did one car move from concept through testing, launch, and ownership?|Use dated prototypes, regulatory records, reviews, and owner experience.
system_boundary|Defining the Vehicle System|Which components belong in the analysis of one car function?|Include energy source, controls, road, driver, and service context where relevant.
input_output_trace|Energy Through a Vehicle|Where does energy enter, convert, dissipate, or recover in one drive cycle?|Use measured consumption and losses for a named model and test.
design_tradeoff|A Choice with Costs|What did one design choice improve and compromise?|Compare mass, safety, cost, repairability, and performance evidence.
failure_mode|How a Component Fails|What evidence identifies the failure mode of one vehicle part?|Read service, testing, and investigation records; avoid speculation from anecdotes.
testing_limits|What a Vehicle Test Can Show|Which real-world conditions are absent from one lab or proving-ground test?|Compare protocol, vehicle configuration, environment, and uncertainty.
standards_interoperability|A Connector or Interface Standard|How does one standard affect vehicle compatibility and repair?|Name jurisdiction, version, supported models, and exceptions.
security_threat_model|Vehicle Software and Safety|What documented digital threat affects one connected-vehicle function?|Use published research and mitigations; omit exploit instructions.
maintenance_lifecycle|The Cost of Keeping a Car Running|How do service intervals and parts availability change over a model's life?|Use owner manuals, repair data, and dated parts access.
infrastructure_dependencies|A Car Depends on Its Network|Which roads, fuel or charging sites, and service facilities determine practical use?|Compare a defined journey and current availability.
accessibility_usability|Who Can Operate and Use This Car?|How do controls, entry, seating, and information affect a defined user group?|Use measurements and user testing, avoiding one-size-fits-all claims.
independent_replication|Repeating a Vehicle Claim|Can an independent test reproduce one advertised result?|Match configuration and protocol, then report variability.
responsible_deployment|A Safety Feature in Everyday Use|How should a new feature communicate its limits to drivers?|Compare manual language, interface, misuse evidence, and oversight.
field_route_capacity|A Car in the Transport System|How does a vehicle type affect road or parking capacity in one corridor?|Use traffic data and comparable occupancy assumptions.
field_vehicle_design|A Design from Prototype to Sale|Which prototype decisions survived into the production car?|Compare dated designs, homologation, manufacturing, and owner feedback.
field_maintenance_system|Repair Access in Practice|Can independent and authorized shops maintain one model?|Compare tools, manuals, parts, diagnostics, and cost in a named market.
field_safety_case|Evidence for a Safety Claim|What crash-test and field evidence supports one vehicle safety statement?|State tested configuration, rating scheme, date, and known gaps.
field_construction_impact|Making a Car's Components|What impacts arise from producing one major vehicle component?|Bound material extraction, fabrication, transport, and measured emissions."""


if __name__ == "__main__":
    revise_domain("021", "021_luxury_rich_lifestyle", LUXURY,
                  "Luxury products and status practices through makers, materials, price, service, claims, ownership, and social costs.",
                  "dated company filings and product records, supply-chain disclosures and audits, labor accounts, auction and resale records, product testing, and applicable marketing rules",
                  "Treat prestige and value as claims to examine. Attribute prices and provenance, disclose estimates, check marketing assertions, and avoid glamorizing exploitation or implying an item is an investment.")
    revise_domain("022", "022_cars_automotive_stories", CARS,
                  "Automotive design, engineering, testing, safety, maintenance, ownership, and transport-system effects.",
                  "manufacturer specifications and owner manuals, safety investigations and recalls, independent vehicle tests, emissions and fuel-economy protocols, repair records, and dated owner accounts",
                  "Name model, year, market, and test conditions. Distinguish lab ratings from real-world use, avoid unsafe driving or repair instructions, and check current recall and safety information.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
