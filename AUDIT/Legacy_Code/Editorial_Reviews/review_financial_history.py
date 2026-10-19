"""Question-design review of four finance niches whose subject is historical inquiry."""
from review_angle_plans import revise_domain, audit

MONEY = """history_origins|Early Evidence of Money|What is the earliest secure evidence for a named payment medium?|Compare dated objects and records without assuming one universal origin.
famous_examples|A Currency Object in Context|What does one famous coin or note reveal about its users?|Study issue authority, denomination, circulation, and surviving evidence.
hidden_stories|Who Made and Moved Money?|Whose labor and access are missing from a monetary history?|Use mint, merchant, or household records for one community.
beginner_explainers|What Counted as Money?|Why did a community accept one object or record in payment?|Define unit, issuer, trust, and use in one period.
advanced_concepts|Value Without a Single Anchor|How did people judge value among multiple monies?|Compare exchange records and legal rules in one market.
mysteries_unsolved_cases|An Uncertain Coinage Date|Which evidence could narrow the date or origin of a monetary object?|Compare hoards, inscriptions, and archaeological contexts.
technology_innovation|A Payment Technology Changes Practice|What changed when one payment medium or record system appeared?|Trace adoption, limitations, and users across a dated transition.
people_personalities|An Issuer's Monetary Choice|Why did a named authority alter a currency's design or value?|Use decrees, mint records, and contemporary responses.
major_events|A Monetary Reform Reconstructed|What changed after one dated currency reform?|Compare legal text, circulation evidence, and prices.
how_it_works|One Historical Payment|How did one documented transaction actually settle?|Follow unit, medium, intermediaries, and record of receipt.
rise_fall|A Currency Gains and Loses Acceptance|What evidence shows a medium expanding or retreating in use?|Compare dated transactions across places and groups.
then_vs_now|Two Ways to Record Payment|Which functions changed between a physical and later recorded payment?|Compare ownership, transfer, access, and trust in dated cases.
future_developments|A Historical Claim About the Future of Money|Which past predictions about money did or did not materialize?|Read original forecasts against later records without predicting the next form.
myths_vs_facts|Testing a Barter-to-Money Story|Does one popular origin story fit documented exchange practices?|Examine its source and evidence from a bounded society.
documentary_stories|One Note's Life in the Archive|What can a surviving monetary object tell us about circulation?|Use provenance and issuer records, stating what cannot be inferred.
product_terms|Terms Printed on a Historical Note|What could a holder legally claim under one note issue?|Read dated issue terms and distinguish promise from practice.
household_cash_flow|Household Payments in a Past Economy|What monetary units appear in a surviving household account?|Reconstruct income and bills with source limits.
risk_and_time|A Delayed Historical Payment|What risk arose when payment and delivery occurred at different times?|Use one merchant or government record to trace obligations.
fee_effect|The Cost of Converting Money|How did mint, exchange, or transfer charges affect a transaction?|Use a dated fee schedule and one illustrative amount.
consumer_protection|Historical Protection Against Bad Money|Which rule addressed counterfeiting or failed redemption?|Compare official rule and observed enforcement; avoid present-day advice.
market_vs_household|Currency Change and Daily Purchases|Did a monetary reform affect household prices as officials expected?|Compare public claims with dated price and wage records.
historical_policy|Why a Monetary Standard Changed|Which pressures led one state to alter its monetary standard?|Use debates, legislation, and subsequent evidence.
inflation_effect|What Could a Unit Buy?|How did purchasing power change in one documented period?|Use a consistent basket and discuss source comparability.
fraud_warning|A Historical Counterfeit Case|How was one counterfeit identified and documented?|Use archival reports without explaining operational forgery methods.
comparison_method|Two Money Systems, Same Task|How did two monetary systems handle the same kind of payment?|Compare acceptance, divisibility, recordkeeping, and enforcement.
access_gap|Who Could Use Official Money?|Which groups had limited access to an issued currency?|Use denominations, wages, geography, and local records.
uncertainty_range|Historical Prices With Missing Data|How much do uncertain prices alter an estimate of purchasing power?|Show a transparent range and provenance of each input.
field_fee_structure|Charges in a Monetary System|Who collected a conversion or minting charge?|Read dated rules and distinguish nominal from actual cost.
field_risk_disclosure|Warnings on a Monetary Promise|Which risks were disclosed when a money claim was issued?|Compare issue documents and later redemption experience.
field_regulatory_protection|Authority Behind a Currency|Which body issued, redeemed, or policed a monetary instrument?|Map legal powers for one jurisdiction and date.
field_household_effect|A Currency Reform at Home|How did one household's recorded payments change after reform?|Compare the same household or similar records before and after.
field_market_cycle|Money Supply Through a Shock|How did circulation of one monetary medium change during a crisis?|Use dated issue and transaction data, noting missing coverage."""

STOCK = """history_origins|How One Exchange Took Shape|Which trading need and membership rules shaped an early exchange?|Use charters, price lists, and trading records.
famous_examples|A Famous Market Episode Rechecked|What does one celebrated boom or crash actually show?|Compare contemporary prices, participation, and later retellings.
hidden_stories|Who Could Trade?|Whose exclusion or labor is absent from exchange history?|Use membership, brokerage, and worker records.
beginner_explainers|A Historical Share Trade|How did a buyer and seller transfer a share in one period?|Trace listing, broker, price, settlement, and ownership record.
advanced_concepts|Liquidity Before Electronic Trading|How did market design affect the ability to trade a share?|Compare order handling and spreads in a dated setting.
mysteries_unsolved_cases|Why Did This Market Break?|Which causes of one abrupt market move remain disputed?|Compare archived prices, news, rules, and data gaps.
technology_innovation|A Trading Technology's Consequences|Which cost or delay changed after a specific trading innovation?|Compare measurable effects and unintended exclusions.
people_personalities|Who Set Exchange Rules?|How did one rulemaker shape who could trade and under what terms?|Use meeting records, bylaws, and affected accounts.
major_events|A Market Closure Timeline|Why did an exchange close or restrict trading on one occasion?|Build a dated timeline of notices, prices, and reopening.
how_it_works|An Order Through a Historical Market|What happened to an order from placement to settlement?|Use contemporaneous rules and a documented trade.
rise_fall|A Company Through a Listing Cycle|What changed between one firm's listing, peak, and decline?|Read dated filings, prices, and corporate actions.
then_vs_now|Floor and Screen|Which trading functions changed when one market moved from floor to screen?|Compare access, speed, transparency, and oversight.
future_developments|Old Forecasts for the Exchange|Which predictions about market structure proved wrong?|Compare dated forecasts with later institutional change.
myths_vs_facts|Testing a Crash Legend|Does a popular story about a market crash match the record?|Check archived news, prices, and official inquiries.
documentary_stories|One Security's Trading Record|What can one listing's documents reveal about a period?|Trace prospectus, trades, disclosures, and delisting if applicable.
product_terms|Rights Attached to an Old Share|What rights did a holder of one historical security actually possess?|Read the issue and corporate documents rather than assume modern rights.
household_cash_flow|Dividends in a Household Record|How did share income affect one documented household?|Use accounts and tax or estate records with privacy care.
risk_and_time|Settlement Risk in an Earlier Market|Where could a historical trade fail before settlement?|Map counterparties, credit, and timing under dated rules.
fee_effect|The Historical Cost of Trading|How much did commissions and taxes add to one trade?|Use dated tariffs and a transparent example.
consumer_protection|When Investor Protection Changed|Which abuse did one securities reform target?|Compare legislation, enforcement, and observed practices.
market_vs_household|Index Recovery, Investor Experience|Why could an index recover while a historical investor did not?|Account for holdings, entry dates, dividends, and costs.
historical_policy|A New Exchange Rule in Practice|Did a dated trading rule change market behavior?|Compare intended and measured outcomes.
inflation_effect|Nominal Versus Real Market Return|How does inflation alter a historical return comparison?|Use price index, dividends, and consistent dates.
fraud_warning|A Historical Securities Fraud|Which promises were contradicted by surviving filings?|Use official investigations without turning tactics into a playbook.
comparison_method|Two Exchanges Compared|How did two markets differ for the same type of trade?|Compare membership, disclosure, fees, and settlement at matched dates.
access_gap|Opening the Market to New Investors|Which rule or cost limited participation in a named period?|Use minimum lots, commissions, legal barriers, and distribution data.
uncertainty_range|A Return Estimate With Missing Records|How do missing dividends or delistings change a historical estimate?|Show a bounded range rather than one precise claim.
field_fee_structure|Exchange, Broker, and Tax Charges|Who received each charge on a historical trade?|Read fee schedules and statutory rules.
field_risk_disclosure|What an Issuer Told Investors|Which material risk appeared in a period prospectus?|Compare disclosed risks with later filings and outcomes.
field_regulatory_protection|The Regulator's Changing Reach|What powers did a market supervisor actually have at one date?|Use statute and enforcement records.
field_household_effect|Market Losses Beyond the Index|Which households bore losses in one market downturn?|Use disaggregated ownership or survey data where available.
field_market_cycle|Boom, Drawdown, Recovery|How did prices, issuance, and participation move through one cycle?|Use dated series with consistent definitions."""

TAX = """history_origins|The Origin of One Tax|Why was one tax introduced in a named jurisdiction?|Use legislation, fiscal needs, and contemporary debate.
famous_examples|A Famous Tax Reform Revisited|Did one widely cited reform achieve its stated goal?|Compare official rationale, implementation, and revenue data.
hidden_stories|Who Collected the Tax?|Whose administrative labor or burden is missing from tax history?|Use payroll, local, or household records.
beginner_explainers|How a Historical Tax Was Assessed|Who owed one tax, on what base, and by which method?|Read dated law and administrative instructions.
advanced_concepts|Incidence Versus Legal Liability|Who ultimately bore the cost of a historical tax?|Separate statutory payer from estimated economic incidence.
mysteries_unsolved_cases|A Tax Record's Missing Population|Whose payments may be absent from surviving records?|Inspect coverage, exemptions, evasion, and archival loss.
technology_innovation|A New Method of Tax Collection|How did one administrative technology change assessment or compliance?|Compare records and costs before and after adoption.
people_personalities|Who Designed a Tax Rule?|Which decision makers shaped one tax and whose objections were heard?|Trace drafts, debates, and affected groups.
major_events|A Tax Change at a Turning Point|What changed when a tax rule took effect during a crisis?|Compare timing, revenue, and public response.
how_it_works|From Assessment to Treasury|How did one historical tax payment move through the state?|Map base, assessment, collector, receipt, and enforcement.
rise_fall|A Tax That Was Repealed|Why did one tax lose political or administrative support?|Compare cost, revenue, resistance, and replacement.
then_vs_now|The Same Tax Across Two Eras|How did its base, rate, and exemptions change?|Compare law and effective burden at two dates.
future_developments|Old Predictions About Tax Reform|Which forecast about a past reform held up?|Read original forecasts against later revenue and behavior.
myths_vs_facts|A Tax Legend Checked|Does a popular story about a historical tax match primary records?|Identify the claim's earliest source and test it.
documentary_stories|One Tax Register's Story|What does a surviving tax record reveal about a community?|Explain its categories, exclusions, and privacy limits.
product_terms|A Tax Concession's Conditions|Who qualified for one historical exemption or relief?|Read the legal text and administrative practice.
household_cash_flow|Tax in a Household Ledger|How much of one household's recorded income went to a tax?|Use dated accounts and avoid claiming representativeness.
risk_and_time|Tax Arrears and Timing|How did payment deadlines affect taxpayers in one period?|Read rules and documented arrears cases.
fee_effect|The Cost of Collecting a Tax|How much did administration consume relative to revenue?|Compare dated budget and collection data.
consumer_protection|Rights in a Historical Tax Dispute|What recourse did a taxpayer have against an assessment?|Specify jurisdiction and date from statute and cases.
market_vs_household|Tax Revenue and Household Burden|Why can rising receipts hide uneven household effects?|Compare aggregate and disaggregated evidence.
historical_policy|A Tax Reform in Practice|What happened after one tax base or rate changed?|Compare stated goal, compliance, revenue, and distribution.
inflation_effect|Inflation and Tax Thresholds|How did nominal thresholds change real tax burdens?|Use period price and wage data with legal thresholds.
fraud_warning|A Historical Tax Evasion Claim|What do official records establish about one evasion allegation?|Use attributed findings and avoid a methods tutorial.
comparison_method|Two Tax Systems, One Measure|How did two jurisdictions tax the same activity differently?|Match period, base, exemptions, and enforcement.
access_gap|Who Could Claim Tax Relief?|Which administrative barrier blocked eligible people?|Use rules, take-up, and documented complaints.
uncertainty_range|Tax Revenue With Incomplete Records|How wide is a plausible estimate from surviving accounts?|Show assumptions and missing jurisdictions.
field_fee_structure|Administrative Charges Around Tax|Which filing or collection charges accompanied one tax?|Separate tax liability from service and penalty costs.
field_risk_disclosure|Uncertainty in Tax Estimates|Which assumptions did officials disclose in revenue forecasts?|Compare dated forecasts with later receipts.
field_regulatory_protection|Limits on Tax Authority|Which legal limit constrained an assessor or collector?|Use statute and recorded appeals.
field_household_effect|Tax Burden by Group|Which households paid more after a reform?|Use comparable data and a clear incidence model.
field_market_cycle|Tax Receipts Across a Cycle|How did revenue respond to an economic downturn?|Compare policy changes with underlying tax base changes."""

WEALTH = """history_origins|How Wealth Was Recorded|What is the earliest usable record of wealth for one society?|Define assets and liabilities before comparing households.
famous_examples|A Celebrated Fortune in Context|How large was one famous fortune relative to its economy?|Use dated asset estimates and transparent denominators.
hidden_stories|Assets Missing From the Archive|Whose property or debt is absent from standard wealth histories?|Compare formal records with community and household evidence.
beginner_explainers|Income Is Not Wealth|How did a historical record distinguish earnings from net assets?|Use one estate, survey, or tax source and explain its limits.
advanced_concepts|Comparing Wealth Across Centuries|Which valuation and currency choices change a historical comparison?|Test multiple deflators, asset types, and denominators.
mysteries_unsolved_cases|The Missing Top of the Distribution|How do absent wealthy households affect a historical wealth estimate?|Compare source coverage and correction methods.
technology_innovation|A New Asset Changes Wealth Records|How did one financial innovation alter what could be owned or measured?|Trace legal rights, valuation, and access.
people_personalities|A Fortune's Institutional Roots|Which laws or institutions enabled one documented fortune?|Trace ownership, inheritance, market power, and public records.
major_events|A Wealth Shock|How did one war, reform, or crisis change measured wealth?|Use comparable before-and-after data and causal caution.
how_it_works|From Estate Inventory to Wealth Estimate|How can an inventory be converted into a net-wealth measure?|Show assets, debts, valuation date, and missing items.
rise_fall|A Family Fortune Across Generations|Which transfers and losses explain a fortune's change?|Use estate and business records across named generations.
then_vs_now|Two Wealth Distributions|How did wealth concentration change between two comparable periods?|Match units, coverage, valuation, and asset definitions.
future_developments|Past Predictions About Wealth|Which historical prediction of wealth distribution proved inaccurate?|Compare dated forecasts with later survey or tax data.
myths_vs_facts|Testing a Richest-Person Claim|Does a historical ranking survive a consistent valuation method?|Check source estimates and denominator choices.
documentary_stories|One Estate's Paper Trail|What does an estate file show and hide about wealth?|Read assets, debts, beneficiaries, and excluded property.
product_terms|Ownership Rights Behind an Asset|What rights did holders of one historical asset actually possess?|Read title, company, or legal records for a defined period.
household_cash_flow|Income and Asset Accumulation|Did a household's income translate into lasting wealth?|Use longitudinal records and account for debt and transfers.
risk_and_time|Preserving Wealth Across Time|Which asset risks mattered to a historical household?|Compare inflation, default, property loss, and liquidity.
fee_effect|Costs of Holding Wealth|Which taxes and management costs reduced a historical asset's value?|Use dated contracts, tax rules, and transparent arithmetic.
consumer_protection|Property Rights and Their Limits|Who could legally own or inherit assets in one period?|Specify jurisdiction, group, and legal change.
market_vs_household|Asset Boom and Wealth Distribution|Did rising asset prices benefit all households equally?|Compare ownership rates and net wealth by group.
historical_policy|A Rule That Changed Ownership|How did one land, inheritance, or financial rule reshape assets?|Compare legal text with distributional evidence.
inflation_effect|Nominal Fortune, Real Value|How does inflation change a historical wealth estimate?|Show several defensible comparison measures.
fraud_warning|A Disputed Historical Fortune|Which archival claims about one fortune are independently verifiable?|Audit sources without sensational claims.
comparison_method|Two Fortunes on Equal Terms|How can two historical fortunes be compared fairly?|Use the same asset definitions, date basis, and denominator.
access_gap|Who Could Accumulate Assets?|Which legal or institutional barrier limited ownership?|Use documented rules and affected people's records.
uncertainty_range|Wealth Estimates as Ranges|Which missing assets or valuation choices widen an estimate?|Show low and high assumptions with provenance.
field_fee_structure|Transaction Costs of Wealth Transfer|How did fees and taxes affect transfer of assets?|Use estate, property, or securities records.
field_risk_disclosure|Uncertainty in Historical Wealth Data|What did a wealth estimate omit or infer?|Read survey, tax, or estate methodology before quoting it.
field_regulatory_protection|Institutions Protecting Ownership|Which legal system enforced claims to one asset?|Compare formal rights with actual access to enforcement.
field_household_effect|Wealth and Household Security|How did asset ownership affect resilience in one historical shock?|Compare households with similar income but different assets.
field_market_cycle|Wealth Through an Asset Cycle|How did a property or equity cycle change net wealth by group?|Use dated ownership, debt, and valuation data."""


if __name__ == "__main__":
    specs = [
        ("295", "295_money_history", MONEY,
         "Material, institutional, and social histories of payment media and monetary systems.",
         "dated monetary objects, mint and issue records, legal texts, transaction ledgers, and attributed scholarship",
         "Avoid one universal origin story; date monetary claims and distinguish official terms from actual use."),
        ("300", "300_stock_market_history", STOCK,
         "Historical exchange structures, securities, trading practices, regulation, participation, and cycles.",
         "dated exchange rules, prices, issuer filings, legal records, archival news, and scholarly analyses",
         "Use consistent historical return methods and avoid treating market history as investment advice."),
        ("314", "314_tax_history", TAX,
         "Historical tax rules, assessment, collection, incidence, compliance, and distributional effects.",
         "dated legislation, budgets, tax registers, administrative guidance, appeals, and attributed scholarship",
         "Specify jurisdiction and period; distinguish legal liability from economic burden and avoid current tax advice."),
        ("315", "315_wealth_history", WEALTH,
         "Historical wealth measurement, ownership, transfers, distribution, and institutional access.",
         "estate and tax records, asset valuations, household surveys, legal texts, and documented methodology",
         "Distinguish income from net wealth; state valuation assumptions, coverage gaps, and uncertainty."),
    ]
    for item in specs:
        revise_domain(*item)
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
