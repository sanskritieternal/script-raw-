"""Editorial question designs for retail and logistics niches."""

from review_angle_plans import audit, revise_domain


RETAIL = """history_origins|From Shopfront to Platform|How did one retailer's selling channel change over time?|Compare dated catalogues, store records, websites, and customer access.
famous_examples|A Marketplace Success Story Tested|Which results made one platform famous, and who benefited?|Compare seller fees, buyer outcomes, and labor alongside sales growth.
hidden_stories|The Work Behind Next-Day Delivery|Whose warehouse, courier, and support work is obscured by checkout?|Trace one order with worker accounts and employment terms.
beginner_explainers|What Happens After Checkout?|Which actors handle payment, stock, shipment, returns, and remedy?|Follow a bounded order and distinguish seller from marketplace duties.
advanced_concepts|True Cost of a Retail Sale|How do returns, fees, fulfillment, and customer service change unit economics?|Use disclosed figures or clearly labeled scenarios with the same denominator.
mysteries_unsolved_cases|Why Did Sales Drop?|Which causes fit a retailer's sudden decline?|Compare stockouts, pricing, traffic, conversion, competition, and measurement changes.
technology_innovation|Ranking the Digital Shelf|How does search placement affect which sellers consumers find?|Examine sponsored labels, ranking tests, and seller dependence.
people_personalities|The Independent Seller on a Platform|How did one seller's choices change as platform rules evolved?|Use consented business records and avoid making one case typical.
major_events|A Retailer During a Disruption|How did one dated event alter stock, prices, deliveries, and returns?|Build a timeline from orders, supplier notices, and customer reports.
how_it_works|Inventory to Customer|How is a product counted, reserved, fulfilled, delivered, and returned?|Trace actual handoffs and points where records can differ.
rise_fall|Why a Store Closed|Which factors explain the closure of one retail location?|Compare rent, demand, labor, online sales, and local access effects.
then_vs_now|One Product's Retail Journey|How did buying the same product change across two periods?|Compare total price, choice, delivery time, return rights, and access.
future_developments|Evaluating a New Fulfillment Model|What would show whether a proposed model helps retailers and customers?|Define cost, speed, worker conditions, returns, and emissions.
myths_vs_facts|The Cheapest Price Claim|Does a low headline price remain lowest after fees and returns?|Compare identical items, dates, terms, shipping, and remedies.
documentary_stories|An Order With a Problem|How did one purchase move from complaint to refund or repair?|Use consented records and check actual legal and platform obligations.
value_chain|Who Earns From the Basket?|How are revenue and costs split among seller, platform, payment firm, and courier?|Map one order's charges and services with dated contracts.
incentive_map|Why Promote This Listing?|Which incentives shape the shelf, search rank, and sales pitch?|Compare commissions, ads, inventory goals, and consumer disclosure.
unit_economics|Does Free Shipping Pay?|Who covers shipping, returns, and handling under a retail offer?|Model disclosed or hypothetical orders with explicit assumptions.
consumer_outcome|Did Delivery Meet the Promise?|How often did a seller meet advertised price, timing, and product condition?|Use a defined sample and complaint or tracking records.
market_structure|Independent Sellers or One Owner?|How concentrated is a product category across apparent storefronts?|Trace ownership, platform rules, and measurable market share.
risk_transfer|Who Pays When a Parcel Fails?|How are lost, damaged, or late orders allocated between parties?|Compare contract terms, consumer rights, and actual resolution.
regulatory_choice|A Marketplace Safety Rule|Did a product or seller-verification rule improve buyer safety?|Compare coverage, enforcement, incident data, and seller burden.
historical_shock|Retail Under a Supply Shock|How did a shortage change allocation and customer access?|Compare stock records, purchase limits, prices, and affected groups.
data_definition|What Counts as a Sale?|Do reported retail sales include canceled or returned orders?|Check transaction status, gross versus net value, and time period.
access_and_affordability|Who Cannot Use the Store?|Which payment, language, disability, transport, or delivery barriers remain?|Test one service with users and compare total access costs.
business_failure|A Retail Expansion That Failed|Which assumptions about demand, margin, or logistics proved wrong?|Compare original plan, performance, external shocks, and alternatives.
long_term_tradeoff|Convenience and Its Cost|Does faster delivery shift costs to labor, packaging, or transport?|Compare matched orders across speed options and system boundaries.
field_supply_chain|A Stockout's Path|At which handoff did inventory fail to reach the shelf?|Use supplier, warehouse, and store records with timestamps.
field_brand_claims|Marketplace Trust Badges|What does one badge or guarantee actually verify?|Read criteria, audit process, exclusions, and customer understanding.
field_customer_experience|The Return Journey|Can a customer complete a return under the advertised terms?|Test steps, time, cost, accessibility, and actual remedy.
field_market_entry|A New Seller's First Year|What obstacles shape a small seller's entry into a retail channel?|Compare setup fees, ranking, fulfillment, cash flow, and customer acquisition.
field_product_lifecycle|After the Purchase|How do warranty, repair, resale, and disposal affect retail value?|Track a defined product's actual options and costs."""


LOGISTICS = """history_origins|How a Goods Route Formed|Why did one supply route or distribution hub develop?|Trace infrastructure, demand, policy, and dated shipper decisions.
famous_examples|A Celebrated Supply Chain Tested|What made one network seem efficient, and what vulnerabilities remained?|Compare cost and speed with disruptions, labor, and redundancy.
hidden_stories|Labor at the Handoffs|Which warehouse, port, driver, and customs work is invisible in a delivery story?|Use attributed worker accounts and job records along one route.
beginner_explainers|A Shipment Step by Step|How does one product move from producer to buyer?|Map custody, documents, modes, storage, and delivery in a named corridor.
advanced_concepts|Speed, Cost, and Resilience|What tradeoffs arise when a chain removes inventory or backup routes?|Compare lead-time variation, carrying cost, disruptions, and recovery.
mysteries_unsolved_cases|Where Did the Delay Begin?|Which evidence locates the cause of one delayed shipment?|Check timestamps, border processing, capacity, weather, and missing scans.
technology_innovation|Tracking a Shipment|Does digital tracking improve visibility and decisions?|Compare scan coverage, data quality, worker burden, and response time.
people_personalities|The Dispatcher Decision|What options did a logistics worker have during one disruption?|Use consented accounts and contemporaneous constraints, not hindsight.
major_events|A Port Closure's Ripple|How did a dated closure affect shipments, prices, and workers?|Trace a bounded product chain and alternative routes with dates.
how_it_works|Freight Across Modes|How are goods transferred between road, rail, sea, or air?|Follow a documented shipment and the contracts at each handoff.
rise_fall|Why a Freight Hub Lost Traffic|Which changes explain falling volume at one hub?|Compare routes, tariffs, infrastructure, reliability, and customer choices.
then_vs_now|The Same Route Across Time|How did travel time, cost, risk, and labor change?|Use the same product and endpoints with comparable measures.
future_developments|Testing a New Route|What evidence would justify moving freight to a proposed corridor?|Model volume, capacity, border rules, worker effects, and environmental cost.
myths_vs_facts|The One-Ship Bottleneck Story|Did a single incident cause a broad shortage?|Compare inventories, upstream capacity, demand, and alternate paths.
documentary_stories|A Container's Record|What does a complete chain of custody show for one shipment?|Reconstruct booking, handling, customs, delivery, and disputes.
value_chain|Who Does Each Logistics Job?|Which firms and workers store, move, clear, and deliver one product?|Map contracts, subcontracting, custody, and accountability.
incentive_map|Why a Route Is Chosen|How do prices, penalties, and service targets shape routing?|Compare shipper, carrier, broker, and worker incentives.
unit_economics|Cost Per Delivered Unit|Which costs matter when comparing two freight options?|Include handling, inventory, delay, damage, and return costs.
consumer_outcome|Reliability at the Door|How do logistics decisions change delivery promises and product condition?|Compare order-level tracking, damage, late deliveries, and remedies.
market_structure|Dependence on One Carrier|How concentrated is service for one route or product?|Measure alternatives, switching costs, capacity, and bargaining power.
risk_transfer|Who Bears Delay and Damage?|How do contracts allocate losses when goods arrive late or damaged?|Compare written terms with claims and actual recovery.
regulatory_choice|A Border Rule in Practice|Did a customs or safety change alter clearance time or risk?|Compare periods, shipment mix, compliance cost, and enforcement.
historical_shock|A Network Under Stress|How did a documented shock propagate through one supply chain?|Trace capacity, inventory, substitutions, and recovery across nodes.
data_definition|What Is On-Time Delivery?|Do two logistics reports measure punctuality the same way?|Check start point, promised window, denominator, and missing shipments.
access_and_affordability|The Last-Mile Gap|Which communities face higher delivery prices or worse service?|Compare geography, volume, infrastructure, and alternatives.
business_failure|A Distribution Plan That Failed|Which assumption about volume, labor, or cost broke down?|Compare forecast, actual throughput, contracts, and external changes.
long_term_tradeoff|Low Cost, Hidden Fragility|Does minimizing spare capacity raise disruption losses?|Compare normal-period savings with dated recovery costs and uncertainty.
field_supply_chain|Tracing a Handoff Failure|Which node caused a missing or damaged shipment?|Match scans, custody records, condition reports, and time stamps.
field_brand_claims|The Green Delivery Claim|Does a carrier's sustainability claim cover the full relevant route?|Check mode, load factor, boundaries, and independent method.
field_customer_experience|When Tracking Disagrees With Reality|How do customers experience gaps in shipment information?|Compare tracking events, actual receipt, service contacts, and remedies.
field_market_entry|A New Carrier's Barriers|What does a new logistics provider need to serve one route?|Assess licenses, equipment, network density, labor, and capital.
field_product_lifecycle|Reverse Logistics|How do returned, repaired, or recycled goods move backward?|Trace sorting, transport, costs, labor, and final disposition."""


if __name__ == "__main__":
    revise_domain("107", "107_retail_e-commerce", RETAIL,
                  "Retail and e-commerce as selling systems with inventory, digital platforms, buyer rights, fulfillment, labor, and product aftercare.",
                  "dated listings and terms, transaction and inventory data, seller and platform contracts, consumer complaints, current protection rules, and worker accounts",
                  "Name seller, platform, market, product, and date. Compare total cost and actual remedy, protect customer data, and verify current local consumer law.")
    revise_domain("108", "108_logistics_supply_chain", LOGISTICS,
                  "Movement and custody of goods across suppliers, warehouses, carriers, borders, and reverse flows, with attention to workers and reliability.",
                  "shipment and custody records, contracts, route and capacity data, relevant trade rules, worker accounts, and measured service outcomes",
                  "Name product, route, dates, and chain boundary. Distinguish promised from observed delivery, avoid exposing security-sensitive routes, and check worker and environmental effects.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
