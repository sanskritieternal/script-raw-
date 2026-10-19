"""Question-design review for housing, currency, and insurance niches."""
from review_angle_plans import revise_domain, audit

REAL_ESTATE = """history_origins|How Property Rights Took Shape|Which legal change altered ownership or tenancy in one place?|Use dated land, title, and legislative records.
famous_examples|A Landmark Property Deal Revisited|What does one widely cited sale or development actually show?|Compare contract terms, financing, and later outcome.
hidden_stories|Who Made the Neighborhood?|Whose work or displacement is absent from a development story?|Use planning, labor, title, and resident records.
beginner_explainers|What Transfers in a Property Sale?|Which rights and obligations change hands in one transaction?|Explain title, encumbrances, financing, and local rules.
advanced_concepts|Price Versus Total Housing Cost|Why can the sale price understate the cost of holding a property?|Model financing, taxes, insurance, maintenance, and timing.
mysteries_unsolved_cases|Why a Property Stayed Vacant|Which explanations for one documented vacancy remain uncertain?|Compare ownership, permitting, condition, and market records.
technology_innovation|A Tool for Buying or Managing Property|Did one digital property tool improve a measured process?|Compare access, errors, privacy, and transaction costs.
people_personalities|Who Approved the Project?|Which decisions determined the fate of one development?|Trace owner, lender, planner, and affected residents.
major_events|A Zoning Decision's Consequences|What changed after one land-use rule was adopted?|Compare permits, housing supply, prices, and local testimony.
how_it_works|A Property Transaction End to End|What happens between an accepted offer and recorded transfer?|Map inspection, financing, title, closing, and registration.
rise_fall|A Development That Stalled|Which financing or approval problem delayed a documented project?|Use dated filings and distinguish stated from proven causes.
then_vs_now|One Property Market in Two Periods|How did a neighborhood's tenure and prices change?|Use consistent boundaries and price definitions.
future_developments|A Conditional Housing Project|Which cost or rule would determine whether a proposed project proceeds?|State scenario assumptions and avoid price forecasts.
myths_vs_facts|Testing a Property Return Claim|Does a popular claim about homeownership returns include all costs?|Compare gross price change with financing and maintenance.
documentary_stories|One Parcel's Paper Trail|What do title and planning records reveal about one site?|Build a dated chain and identify missing documents.
product_terms|A Mortgage Term That Matters|Which disclosed loan term changes the cost of one example purchase?|Use a dated offer and identical hypothetical inputs.
household_cash_flow|The Monthly Cost of Owning|How does a property payment interact with taxes and upkeep?|Use a labeled household budget, including irregular costs.
risk_and_time|Holding Period and Property Risk|How does a short holding period change transaction-cost exposure?|Compare dated cost schedules and hypothetical horizons.
fee_effect|Closing Costs on One Transaction|Which charges appear at closing and who receives them?|Read a dated closing disclosure for one jurisdiction.
consumer_protection|What a Buyer Can Verify|Which disclosure or inspection right applies to one sale?|Specify jurisdiction, property type, and date.
market_vs_household|A Price Index and One Home|Why can a market index differ from a single property's outcome?|Compare location, quality, leverage, and transaction timing.
historical_policy|A Housing Rule in Practice|Who gained or lost access after one dated property-policy change?|Compare legal text, take-up, supply, and affected voices.
inflation_effect|Real Cost of Housing|How do nominal prices and incomes compare after inflation?|Use consistent price and income series in one area.
fraud_warning|Verifying a Property Offer|Which details of a listing or transfer request can be checked independently?|Use official records and consumer alerts; avoid a scam playbook.
comparison_method|Rent and Buy on Equal Terms|How do renting and buying compare for one hypothetical horizon?|Include taxes, fees, maintenance, mobility, and uncertainty.
access_gap|Who Can Enter the Market?|Which credit, deposit, legal, or accessibility barrier excludes a group?|Use eligibility rules and local data.
uncertainty_range|A Purchase With Variable Costs|Which assumption changes an example ownership cost most?|Vary rate, maintenance, and holding period transparently.
field_fee_structure|Where Transaction Charges Arise|Which fees are lender, government, or service charges?|Read the actual estimate and closing statement.
field_risk_disclosure|What Property Documents Reveal|Which known risk is disclosed or missing from sale documents?|Compare disclosures, inspection, and public records.
field_regulatory_protection|The Limits of Property Protections|Which buyer or tenant protections apply to one transaction?|Specify jurisdiction and legal status of the parties.
field_household_effect|Housing Cost and Financial Buffer|How does a housing cost change affect one household's remaining income?|Use a clearly hypothetical budget with irregular costs.
field_market_cycle|Property Through a Cycle|How did prices, sales, and construction move through one local cycle?|Use dated local series and avoid causal shortcuts."""

REAL_ESTATE_ECON = """history_origins|A Housing Market Takes Shape|Which infrastructure or policy change altered one local housing market?|Use dated land, population, and planning records.
famous_examples|A Housing Boom Tested|What did a frequently cited housing boom actually measure?|Compare prices, transaction volume, rents, and credit.
hidden_stories|Whose Housing Costs Are Missing?|Which renters or informal households are absent from market data?|Use survey coverage and local accounts.
beginner_explainers|Supply, Demand, and Housing Stock|Why can a new housing project have a delayed effect on availability?|Distinguish stock, flow, vacancy, and household formation.
advanced_concepts|The Identification Problem in Housing|How can researchers separate a policy effect from simultaneous market change?|Compare study designs and assumptions for one case.
mysteries_unsolved_cases|Why Prices Diverged|Which explanations remain plausible for two areas with different price paths?|Compare jobs, supply rules, credit, and amenities.
technology_innovation|A New Way to Measure Housing|Did a data tool improve the accuracy of a housing-market estimate?|Check sample coverage, listing bias, and validation.
people_personalities|Actors Behind a Housing Constraint|Which owners, lenders, builders, or officials shaped a local outcome?|Trace incentives and documented decisions.
major_events|A Shock to Housing Supply|How did one event affect construction or occupancy?|Use permits, completions, rents, and migration data.
how_it_works|From Zoning to Completed Homes|Where can housing supply be delayed?|Map land, approval, finance, construction, and occupancy.
rise_fall|A Housing Cycle Explained|What drove a local rise and reversal in activity?|Compare credit, employment, supply, and prices by date.
then_vs_now|Two Periods of Affordability|Did housing become less affordable for the same population?|Compare prices, rents, income, borrowing costs, and quality.
future_developments|A Conditional Supply Scenario|What would have to happen for a proposed supply change to affect rents?|State timing, scale, demand, and location assumptions.
myths_vs_facts|Testing a Housing Market Claim|Does a popular explanation fit the local evidence?|Compare timing and alternative mechanisms.
documentary_stories|One Development and Its Market|What did a completed project change in nearby housing indicators?|Use bounded geography and before-and-after data cautiously.
product_terms|Loan Terms in a Housing Model|How does a change in mortgage terms affect an affordability calculation?|Use identical property and income inputs.
household_cash_flow|Housing Burden Beyond Rent|Which costs remain after rent or mortgage payments are counted?|Use household expenditure data and a defined population.
risk_and_time|Interest Rates and Construction Lag|Why can housing respond slowly to a rate change?|Trace financing, approvals, and project completion times.
fee_effect|Transaction Costs and Mobility|How might taxes and fees discourage a move?|Compare dated transaction costs with an illustrative decision.
consumer_protection|Regulation and Market Outcomes|Did a consumer or tenant protection alter access or supply?|Compare intended and measured effects for one jurisdiction.
market_vs_household|Aggregate Prices, Unequal Access|Why can stable average prices coexist with poor affordability?|Disaggregate by income, tenure, place, and quality.
historical_policy|One Land-Use Reform Evaluated|Did a dated planning reform increase completed housing?|Compare permits and completions with plausible counterfactuals.
inflation_effect|Nominal and Real House Prices|How does the choice of deflator change a housing trend?|Show nominal, consumer-price-adjusted, and income-relative measures.
fraud_warning|Misleading Housing Statistics|Which presentation choice makes a housing claim deceptive?|Check base year, geographic boundary, and omitted costs.
comparison_method|Two Cities, Same Housing Measure|How do two cities compare after matching definitions?|Align tenure, dwelling quality, income, and dates.
access_gap|A Housing Access Gap|Which measurable rule or cost blocks a defined group?|Use eligibility, location, and household survey data.
uncertainty_range|Forecasting Housing Supply|Which assumption drives a range of housing supply estimates?|Vary completion, demand, and migration transparently.
field_fee_structure|Fees in Development Cost|Which taxes and approval charges appear in a project budget?|Read local fee rules and distinguish marginal from average cost.
field_risk_disclosure|What a Housing Forecast Omits|Which uncertainty is absent from one market projection?|Compare assumptions with observed variance.
field_regulatory_protection|Planning and Tenant Rules|Which regulatory rule applies to one market segment?|Map jurisdiction, housing type, and enforcement.
field_household_effect|Housing Prices and Household Balance Sheets|Who gains and loses when local property prices change?|Separate owners, renters, debtors, and prospective buyers.
field_market_cycle|Credit and Construction Through a Cycle|How did lending and building respond to one downturn?|Use dated local data and account for policy changes."""

CURRENCY = """history_origins|How a Currency Was Established|Which authority and rules created one named currency?|Read founding law, issue records, and contemporary exchange practice.
famous_examples|A Currency Reform in Context|What did one famous redenomination or currency change accomplish?|Compare stated aims, transition terms, and measured outcomes.
hidden_stories|Who Could Not Use Official Currency?|Whose payment practices were excluded from the official account?|Use denominations, geography, and local testimony.
beginner_explainers|Currency, Cash, and Bank Money|How does a banknote differ from a bank deposit in one jurisdiction?|Define issuer, claim, legal status, and use.
advanced_concepts|Nominal and Real Exchange Rates|Why can a currency move in price without the same change in purchasing power?|Use a dated two-country example and consistent price measures.
mysteries_unsolved_cases|An Exchange-Rate Move Explained|Which causes of one currency move remain uncertain?|Compare policy, trade, capital flows, and contemporaneous data.
technology_innovation|A New Currency Form|Which practical payment problem did one currency design address?|Compare security, access, durability, and cost after adoption.
people_personalities|The Decision to Change Currency|Who had legal authority over one currency decision?|Trace official minutes, statutes, and affected groups.
major_events|A Currency Conversion Timeline|What happened during one dated changeover?|Map announcement, conversion rule, circulation, and withdrawal.
how_it_works|Paying Across Currencies|How does a payment convert between two currencies?|Trace quoted rate, spread, fees, settlement, and timing.
rise_fall|A Currency's Loss of Acceptance|What evidence shows a currency losing practical use?|Compare prices, payment records, and policy actions.
then_vs_now|A Currency Across Two Regimes|How did its issuance or exchange rule change?|Compare law, monetary operations, and household use.
future_developments|A Conditional Currency Proposal|Which legal and technical requirements would govern a proposed form?|State assumptions and avoid claiming adoption is certain.
myths_vs_facts|Testing a Currency Claim|Does a popular claim about backing or value match official terms?|Check legal redemption, reserves, and actual practice.
documentary_stories|One Banknote's Journey|What can an issued note reveal about a monetary transition?|Use design, serial, issue, and withdrawal records.
product_terms|Terms of Conversion|Which official conversion rule determined the value of old units?|Read dated legal notices and actual exchange procedures.
household_cash_flow|Currency Change at the Household Level|How did a changeover affect a defined household's payments?|Use a labeled example with prices and wages.
risk_and_time|Timing a Cross-Currency Payment|Which risks arise between agreeing and settling a foreign-currency payment?|Separate rate, settlement, and counterparty exposure.
fee_effect|Exchange Rate Versus Conversion Cost|How much of a conversion cost comes from spread and explicit fees?|Use dated quoted rates and transparent arithmetic.
consumer_protection|Rights During a Currency Change|Which exchange rights or deadlines applied to holders?|Specify authority, jurisdiction, and dates.
market_vs_household|Exchange Rate and Local Prices|Why can a currency move affect households differently?|Compare imported goods, wages, debts, and timing.
historical_policy|A Currency Rule Changed|What happened after one exchange or issuance policy changed?|Compare official objectives with dated data.
inflation_effect|What One Unit Can Buy|How did domestic purchasing power change over a defined period?|Use a consistent price basket and report limits.
fraud_warning|Identifying an Official Currency Notice|Which claims about an exchange or note can be verified?|Use issuer and regulator notices without reproducing fraud tactics.
comparison_method|Two Currencies for One Purchase|How do two payment routes compare for the same transaction?|Include rate, spread, fees, settlement, and protection.
access_gap|Who Could Exchange Old Notes?|Which location, identity, or deadline rule limited conversion?|Use official terms and affected-group evidence.
uncertainty_range|A Currency Scenario With Two Rates|How does rate uncertainty change an illustrative cross-border cost?|Vary rates and fees without forecasting.
field_fee_structure|The Layers of Conversion Cost|Who receives each fee in a cross-currency transfer?|Read provider terms and payment-network charges.
field_risk_disclosure|A Currency Risk Stated Clearly|Which exchange or redemption risk appears in a contract?|Compare disclosure with actual legal rights.
field_regulatory_protection|Who Issues and Supervises Currency?|Which authority controls issuance or exchange in one jurisdiction?|Map central bank, treasury, and payment-provider roles.
field_household_effect|Foreign-Currency Debt at Home|How can a rate move change a household's fixed foreign-currency debt?|Use a labeled hypothetical example and dated rates.
field_market_cycle|Currency Through an Economic Cycle|How did the exchange rate, inflation, and trade move together?|Use consistent series and avoid causal shortcuts."""

INSURANCE = """history_origins|How a Risk Pool Emerged|Which need and rule shaped one early insurance arrangement?|Use dated policy, mutual, or regulator records.
famous_examples|An Insurance Product in Context|What does one widely cited policy actually cover?|Read the dated contract and compare claims with exclusions.
hidden_stories|Who Could Not Get Covered?|Whose risks or communities were excluded from a scheme?|Use eligibility, underwriting, and affected-group records.
beginner_explainers|Premium, Deductible, and Limit|What does a policyholder pay before and after a covered loss?|Use a fictional claim with one dated policy form.
advanced_concepts|Pooling Risk and Adverse Selection|How can who enrolls change an insurance pool's costs?|Use a simplified model and state its assumptions.
mysteries_unsolved_cases|Why a Claim Was Denied|Which policy facts and records determine one disputed claim?|Compare contract language, evidence, and adjudication.
technology_innovation|Digital Claims Handling Tested|Did one claims tool improve speed without reducing fairness?|Compare measured processing and appeal outcomes.
people_personalities|Who Sets Coverage Rules?|Which insurer or regulator decision changed one coverage boundary?|Trace filings, consultations, and policy text.
major_events|A Disaster and Insurance Capacity|How did one event change claims, prices, or availability?|Use dated loss and renewal data for one area.
how_it_works|From Premium to Claim Payment|What steps connect enrollment to a paid claim?|Map underwriting, premium, event, documentation, adjustment, and appeal.
rise_fall|Coverage That Became Unavailable|Why did insurers withdraw or restrict one product?|Compare losses, reinsurance, regulation, and prices.
then_vs_now|One Policy Across Two Periods|How did coverage or exclusions change between policy versions?|Compare forms, limits, and effective dates.
future_developments|A Conditional Coverage Gap|Which conditions would make a risk harder to insure?|State loss, capital, regulation, and adaptation assumptions.
myths_vs_facts|Testing a Coverage Assumption|Does a common belief about what insurance covers match the contract?|Read definitions, exclusions, deductibles, and limits.
documentary_stories|One Claim's Paper Trail|What do records show about a specific claim decision?|Use consented or anonymized documents and appeal history.
product_terms|An Exclusion That Changes Protection|Which wording determines whether one hypothetical event is covered?|Read the exact dated policy and define the peril.
household_cash_flow|Premium and Out-of-Pocket Costs|How do premium, deductible, and uncovered loss affect a household?|Use a labeled illustrative budget.
risk_and_time|Waiting Periods and Renewals|When does coverage begin, end, or change?|Compare dated policy terms and renewal notices.
fee_effect|Total Cost of a Policy|Which charges appear beyond the headline premium?|Read fees, taxes, installments, and cancellation terms.
consumer_protection|Appealing a Claim Decision|What review or complaint process applies to one policy?|Specify jurisdiction, insurer type, and deadlines.
market_vs_household|Industry Losses and Individual Coverage|Why do industry-wide loss figures not describe one policyholder's claim?|Distinguish aggregate claims, specific exclusions, and limits.
historical_policy|An Insurance Rule Changed|Who gained protection after one dated insurance reform?|Compare enacted rule, product availability, and claims outcomes.
inflation_effect|Coverage Limits and Rising Costs|How can a fixed coverage limit lose purchasing power?|Use dated replacement-cost estimates and policy terms.
fraud_warning|Verifying an Insurance Offer|Which claims about an insurer or policy can be checked officially?|Use licensing and policy records without detailing fraud methods.
comparison_method|Two Policies on Equal Terms|How do two policies differ for the same hypothetical loss?|Compare covered event, limits, deductible, exclusions, and price.
access_gap|Who Cannot Obtain Coverage?|Which risk, location, price, or eligibility factor limits access?|Use filings and disaggregated availability data.
uncertainty_range|A Claim Under Different Losses|Which assumption most changes a policyholder's net cost?|Model several hypothetical losses with policy terms.
field_fee_structure|Where Premium Money Goes|Which costs fund claims, administration, and distribution?|Use insurer filings and distinguish premium from fees.
field_risk_disclosure|Reading the Coverage Summary|Which material exclusion is easy to miss in a summary?|Compare summary with full policy form.
field_regulatory_protection|Insurer Solvency and Policyholder Protection|Which protection applies if a licensed insurer fails?|Specify jurisdiction, product, limits, and exclusions.
field_household_effect|Coverage After a Loss|How did deductible and limits affect one household's recovery?|Use a consented or fictionalized case with dated terms.
field_market_cycle|Premiums Across a Loss Cycle|How did claims experience, capital, and prices move over time?|Use dated filings and avoid assuming a single cause."""


if __name__ == "__main__":
    specs = [
        ("112", "112_real_estate", REAL_ESTATE,
         "Property transactions, ownership and tenancy rights, financing, development, and household costs.",
         "dated title and planning records, contracts, mortgage disclosures, local market data, and attributed resident accounts",
         "Specify jurisdiction, property type, and dated terms; avoid individualized legal or financial advice."),
        ("313", "313_real_estate_economics", REAL_ESTATE_ECON,
         "Housing supply, demand, prices, rents, finance, policy, and distributional effects in defined markets.",
         "dated price and rent indices, permit and completion records, household surveys, planning rules, and documented study methods",
         "Define geography, tenure, quality, and time period; distinguish correlations from causal effects and avoid price forecasts."),
        ("312", "312_currency", CURRENCY,
         "Currency issuance, exchange, domestic purchasing power, changeovers, payment use, and legal roles.",
         "dated issuer notices, monetary law, exchange rates, price data, provider terms, and payment records",
         "Specify currency pair, jurisdiction, dates, and nominal versus real measures; avoid individualized financial advice."),
        ("499", "499_insurance_education", INSURANCE,
         "Insurance contracts, risk pooling, coverage, claims, access, and policyholder protections.",
         "dated policy forms, insurer filings, regulator guidance, claims data, and consented accounts",
         "Specify jurisdiction and policy version; distinguish illustrative scenarios from coverage determinations or personal advice."),
    ]
    for item in specs:
        revise_domain(*item)
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
