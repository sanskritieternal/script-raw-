"""Editorial question designs for brands, products, and advertising."""

from review_angle_plans import audit, revise_domain


BRANDS = """history_origins|A Brand's First Market|Which product and customers established a named brand?|Use dated packaging, sales, ownership, and competitors.
famous_examples|An Iconic Brand Rechecked|What evidence supports its claimed reputation?|Compare product performance, price, loyalty, and marketing.
hidden_stories|Who Builds the Brand|Which designers, manufacturers, retailers, and service workers matter?|Trace contracts, labor, and credit.
beginner_explainers|Brand, Company, and Product|How do name, legal owner, and actual offer differ?|Map entities and dated trademark and product records.
advanced_concepts|Loyalty or Lock-In|Why do customers stay with one brand?|Test satisfaction, switching costs, distribution, and habit.
mysteries_unsolved_cases|Why a Rebrand Failed|Which records distinguish name, product, price, and distribution causes?|Compare dated outcomes and alternatives.
technology_innovation|A Digital Brand Channel|Did a platform change reach or customer trust?|Measure acquisition, repeat use, cost, and privacy.
people_personalities|A Brand Decision Maker|Who chose a consequential identity or positioning change?|Use briefs, testing, approvals, and dissent.
major_events|A Brand After a Recall|How did one event affect sales and trust?|Trace official notice, remediation, consumer response, and time.
how_it_works|Promise to Product|How does a brand claim become a customer experience?|Follow design, sourcing, promotion, sale, and support.
rise_fall|Brand Share Over Time|What explains a measured gain or decline?|Define market, denominator, channels, and product mix.
then_vs_now|One Brand Across Owners|What changed after acquisition or licensing?|Compare product, quality, price, labor, and identity.
future_developments|A Brand's Conditional Path|Which product and market assumptions shape its future?|State competition, trust, costs, and ownership scenarios.
myths_vs_facts|Premium Means Better?|Do measured outcomes justify a price difference?|Compare matched products, use, warranty, and total cost.
documentary_stories|A Brand Claim's Life|How was one promise proposed, approved, challenged, and revised?|Build a dated source trail.
value_chain|Where the Brand Captures Value|Which stages does owner control and which are outsourced?|Map production, distribution, licensing, and service.
incentive_map|Owner, Licensee, and Retailer|Where do quality and margin incentives diverge?|Read contracts and complaints.
unit_economics|A Branded Sale|What remains after manufacturing, channel, marketing, and returns?|Use defined item, period, and allocation.
consumer_outcome|What Did Buyers Get|Did the product deliver its stated benefit?|Compare tested use, satisfaction, safety, and support.
market_structure|A Brand in Its Market|Which substitutes constrain its price?|Define product category, geography, and customer segment.
risk_transfer|Who Handles Defects|How do warranty terms shift costs among seller, maker, and buyer?|Read dated terms and outcomes.
regulatory_choice|A Claim or Mark Dispute|How did a named authority handle it?|Name jurisdiction, date, allegation, finding, and remedy.
historical_shock|A Brand During Supply Disruption|How did shortages affect quality and price?|Trace suppliers, availability, and customer response.
data_definition|Measuring Brand Strength|Do awareness, market share, and repeat purchase tell the same story?|State sample and metric.
access_and_affordability|Who Can Buy or Use It|How do price, distribution, design, and service affect access?|Compare customer groups and alternatives.
business_failure|A Brand Without a Business|Why did a well-known name cease or change owners?|Separate brand sale, firm insolvency, and product exit.
long_term_tradeoff|Brand Extension Costs|When does adding products dilute trust or help customers?|Track category, quality, margin, and repeat purchase.
field_supply_chain|Who Makes the Product|How transparent is a brand's sourcing claim?|Trace supplier tiers, audit scope, and gaps.
field_brand_claims|One Promise Tested|What evidence supports the exact words on a label?|Date claim, identify metric, test method, and exceptions.
field_customer_experience|Brand Across Touchpoints|Does service match the advertising?|Compare purchase, delivery, use, return, and support.
field_market_entry|A New Rival Brand|Which shelf, platform, and trust barriers matter?|Measure placement, ad costs, and customer switching.
field_product_lifecycle|A Branded Product Across Versions|How did features, quality, and price change?|Use dated versions and ownership history.
"""

PRODUCTS = """history_origins|Why a Product Was Created|Which user need and constraints shaped its first version?|Use design briefs, early tests, and alternatives.
famous_examples|A Breakthrough Product Rechecked|What did it improve for defined users?|Compare performance, price, safety, and access.
hidden_stories|Workers Behind a Product|Who designs, sources, assembles, tests, ships, and repairs it?|Trace credited and outsourced labor.
beginner_explainers|Following One Product|How does it move from design to end-of-use?|Map materials, manufacturing, sale, support, and disposal.
advanced_concepts|Performance Versus Lifetime Cost|When does a higher specification fail to improve user value?|Test use case, reliability, maintenance, and replacement.
mysteries_unsolved_cases|A Product Failure Investigated|Which design, use, or manufacturing cause fits evidence?|Use tests, complaints, lots, and uncertainty.
technology_innovation|A New Feature Tested|Does it improve a measurable outcome?|Compare baseline, user group, cost, and harms.
people_personalities|A Design Decision|Who chose one consequential trade-off?|Use briefs, testing, and team accounts.
major_events|A Recall or Redesign|How did one event change the product?|Trace official notice, affected models, remedy, and results.
how_it_works|The Product's Operating System|Which components and services deliver its function?|Use a diagram tied to one version.
rise_fall|Product Demand Over Time|What explains sales changes?|Check price, competitors, distribution, season, and data definition.
then_vs_now|Version One and Today|What changed in performance, repair, cost, and safety?|Compare matched tests and specifications.
future_developments|A Product's Conditional Next Version|Which needs and constraints would justify change?|State material, cost, regulation, and user assumptions.
myths_vs_facts|A Spec Sheet Promise|Does one headline metric predict real use?|Test conditions, variance, durability, and alternatives.
documentary_stories|One Product from Brief to Recall|How did decisions and evidence accumulate?|Build dated timeline, not inventor mythology.
value_chain|Inputs to End User|Where are critical materials, manufacturing, and distribution?|Trace suppliers and dependencies.
incentive_map|Designer, Maker, Seller, User|Who benefits from a design choice and who bears cost?|Read warranty, margin, and return terms.
unit_economics|Profit per Unit|How do manufacturing, logistics, returns, and support affect margin?|Specify volume, period, and cost allocation.
consumer_outcome|Does It Work for Users|Which measured outcome matters most?|Define population, comparator, real use, and failure.
market_structure|Product Substitutes|What alternatives solve the same task?|Compare total cost and user needs in a defined market.
risk_transfer|Warranty and Repair|Who pays when the product fails?|Check terms, actual repair access, and consumer outcomes.
regulatory_choice|A Safety Standard Applied|What did a dated requirement change?|Name jurisdiction, product class, test, and enforcement.
historical_shock|Supply Shortage and Redesign|How did a missing component affect function?|Compare versions, prices, lead time, and quality.
data_definition|Counting Product Success|Are units shipped, sold, active, and returned different?|Reconcile denominators and periods.
access_and_affordability|Usable for Whom|Which design, price, language, or repair barriers matter?|Test with defined user groups and alternatives.
business_failure|A Product That Was Withdrawn|What evidence explains its exit?|Separate poor demand, safety, margin, and strategy.
long_term_tradeoff|Durability Versus Replacement|How do repairability and upgrades affect lifetime value?|Compare years of use, parts, waste, and full cost.
field_supply_chain|One Critical Component|Where does it come from and what happens if delayed?|Trace tiers, substitutes, and labor or environmental claims.
field_brand_claims|Packaging Promise Audited|Does evidence support the exact claim?|Check test conditions, scope, date, and exceptions.
field_customer_experience|From Unboxing to Repair|Where does real use depart from instructions?|Observe consentfully and include accessibility.
field_market_entry|Competing Product Launch|Which distribution and certification barriers matter?|Name market, shelf or platform, capital, and rules.
field_product_lifecycle|One Model's Full Life|How did launch, updates, repairs, and withdrawal unfold?|Use versioned records and user outcomes.
"""

ADVERTISING = """history_origins|A Campaign's Market Context|Which audience, medium, and business goal produced it?|Use dated brief, spend, and product records.
famous_examples|A Famous Ad's Effect Rechecked|What outcome can actually be attributed to it?|Separate reach, recall, sales, and other changes.
hidden_stories|Who Made the Message|Which strategists, designers, performers, and media buyers are overlooked?|Trace credits, contracts, and rights.
beginner_explainers|Reading an Ad Claim|What does an ad explicitly and implicitly promise?|Identify audience, product, channel, evidence, and omission.
advanced_concepts|Attribution of Sales|How can campaign effect be separated from season or price?|Compare experiments, control groups, and limitations.
mysteries_unsolved_cases|Why a Campaign Failed|Which evidence distinguishes creative, targeting, distribution, and product issues?|Check data and assumptions.
technology_innovation|Targeting System Tested|Did algorithmic placement improve outcomes or introduce harm?|Measure lift, privacy, exclusions, and bias.
people_personalities|A Creative or Approval Decision|Who shaped one consequential message?|Use drafts, research, approvals, and dissent.
major_events|A Challenged Advertisement|How did a complaint or ruling change the campaign?|Name jurisdiction, allegation, finding, and revision.
how_it_works|From Brief to Impression|How do research, creative, buying, serving, and measurement connect?|Trace one named campaign.
rise_fall|Ad Spend Across Channels|What explains a measured shift?|Check prices, audiences, platform rules, and definitions.
then_vs_now|Same Claim in Two Media Eras|How did targeting, disclosure, and measurement change?|Compare matched products and audiences.
future_developments|Conditional Changes in Advertising|Which privacy or platform shifts might alter a campaign?|State assumptions rather than prediction.
myths_vs_facts|Views Equal Persuasion?|What do impressions fail to prove?|Compare attention, recall, incremental sales, and sampling.
documentary_stories|One Claim from Draft to Withdrawal|How did evidence and approval evolve?|Build dated record including corrections.
value_chain|Money Through an Ad|Who takes a share from advertiser to publisher?|Map agency, exchange, platform, creator, and measurement.
incentive_map|Who Wants Which Metric|How do advertiser, agency, platform, and audience incentives differ?|Check contracts and optimization targets.
unit_economics|Cost per Incremental Customer|Does campaign revenue exceed full acquisition cost?|Define cohort, attribution, margin, and retention.
consumer_outcome|What Did the Audience Believe|Did the ad create a mistaken impression?|Use tested comprehension and actual product outcomes.
market_structure|Media Buying Power|How do platform choices and concentration affect advertisers?|Define channel, geography, and substitutes.
risk_transfer|Who Bears a False Claim|How are costs shared among brand, agency, publisher, and buyers?|Read contracts, rulings, and remedies.
regulatory_choice|Disclosure Rule in Practice|How did a dated rule affect a campaign?|Name jurisdiction and distinguish guidance from enforcement.
historical_shock|Advertising During a Demand Shock|Did firms cut or shift spend?|Compare sales, prices, budgets, and competitors.
data_definition|Ad Metrics Compared|Do impressions, reach, clicks, conversions, and lift differ?|Define each denominator and collection method.
access_and_affordability|Who Is Excluded by Targeting|Do placement and creative omit a group?|Examine reach, accessibility, language, and fairness.
business_failure|A Campaign Without Return|Why did high engagement fail to produce durable sales?|Check quality of traffic, margin, and repeat purchase.
long_term_tradeoff|Short Sales Versus Trust|Can a campaign lift purchases while harming later loyalty?|Compare time horizons and complaints.
field_supply_chain|The Ad Delivery Chain|Where can fraud or data loss occur?|Trace inventory, intermediaries, verification, and audits.
field_brand_claims|Substantiating Exact Words|What evidence existed before the ad ran?|Check claim, implied meaning, test quality, and date.
field_customer_experience|After the Click|Does landing page and purchase match the promise?|Compare price, availability, disclosure, delivery, and remedy.
field_market_entry|A Small Advertiser's Barrier|Which costs and platform rules affect entry?|Compare minimum spend, creative, measurement, and privacy.
field_product_lifecycle|Same Ad Across Product Versions|When did a once-correct claim become stale?|Trace product changes, archived ads, and corrections.
"""


if __name__ == "__main__":
    revise_domain("305", "305_brands", BRANDS,
                  "Brands through ownership, source identification, promises, product performance, customer experience, and market context.",
                  "dated trademarks and ownership records, packaging and advertising, product tests, market and warranty data, and consented customer and worker accounts",
                  "Name brand, owner, product, market, and period. Distinguish a mark from its legal owner and test claims against specific evidence; no legal advice.")
    revise_domain("306", "306_products", PRODUCTS,
                  "Products through design, supply, measured use, safety, repair, full cost, and disposal across versions.",
                  "dated design and specification records, independent tests, official recall data, supplier and repair records, and consented user accounts",
                  "Name product model, version, jurisdiction, and test conditions. Verify current recalls with the relevant authority; avoid treating specifications as real-use outcomes.")
    revise_domain("307", "307_advertising", ADVERTISING,
                  "Advertising through exact claims, substantiation, creative labor, delivery systems, measurement, and consumer understanding.",
                  "dated campaign materials and briefs, pre-claim substantiation, controlled lift studies, platform and spend data, and applicable authority records",
                  "Name ad, product, audience, channel, jurisdiction, and date. Distinguish impressions and clicks from incremental outcomes and allegations from rulings.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
