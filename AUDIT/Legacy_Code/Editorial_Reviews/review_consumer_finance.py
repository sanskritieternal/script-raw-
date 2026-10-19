"""Editorial question-design revisions for personal finance and credit cards."""
from review_angle_plans import revise_domain, audit

PERSONAL_FINANCE = """history_origins|The Household Budget Across Time|How did one change in work or payment systems alter household budgeting?|Use dated wage, price, and household records in one setting.
famous_examples|A Famous Money Rule Tested|Under what assumptions does a popular budgeting rule work or fail?|Trace the rule's source and compare labeled hypothetical households.
hidden_stories|Financial Decisions Under Constraint|Whose financial choices are missing from idealized money advice?|Use disaggregated data and consented accounts for a defined group.
beginner_explainers|Income, Bills, Savings, and Debt|How can a household see its cash commitments over one month?|Build a fictional, labeled example with irregular costs.
advanced_concepts|Tradeoffs Between Liquidity and Return|How does access to money change the usefulness of a higher return?|Compare dated account terms and hypothetical time horizons.
mysteries_unsolved_cases|Why Similar Households Diverge|Which unobserved costs might explain different financial outcomes?|Compare published data with carefully bounded household accounts.
technology_innovation|A Money App's Actual Effect|Did one digital budgeting tool change a measurable decision?|Review its design, evaluation, privacy, and access barriers.
people_personalities|Who Shapes Financial Choices?|How did one employer, lender, or policymaker change household options?|Trace a documented rule or product decision and affected groups.
major_events|A Household Income Shock|How did one dated disruption change a household's financial choices?|Use anonymized or fictionalized records and period context.
how_it_works|Following a Monthly Cash Flow|When do income, bills, debt payments, and savings actually move?|Show a transparent calendar for one illustrative household.
rise_fall|A Financial Buffer Built and Lost|Which events changed one household's emergency savings?|Use consented or anonymized records; avoid moral judgment.
then_vs_now|Two Generations, Comparable Costs|How did a defined cost burden change between two cohorts?|Match geography, income measure, household size, and price basis.
future_developments|Planning Under More Than One Scenario|Which expense or income assumption most changes an example plan?|Show conditional scenarios without promising an outcome.
myths_vs_facts|Testing a Money Maxim|Does a popular personal-finance claim apply across income levels?|Check its evidence, definitions, and exceptions.
documentary_stories|One Bill's Financial Path|How did a single recurring expense affect a household budget?|Use an attributed or anonymized case with contract terms.
product_terms|Reading a Financial Product's Conditions|Which fee, rate, or access term materially changes an example outcome?|Use a dated disclosure for a named product class.
household_cash_flow|The Week Bills Cluster|How does payment timing create a shortfall despite adequate monthly income?|Use a labeled cash calendar and distinguish timing from total income.
risk_and_time|Short Goal, Long Goal|Why does the time horizon change the risks of saving or investing?|Compare hypothetical needs and relevant product constraints.
fee_effect|Small Fees Across a Year|What is the annual cost of a recurring fee for a defined use pattern?|Read dated terms and show arithmetic without a product recommendation.
consumer_protection|Where a Complaint Goes|Which authority or process handles one financial-product dispute?|Specify jurisdiction, product, provider, and time limit.
market_vs_household|A Headline and a Home Budget|Why can a national rate or market move affect households differently?|Compare two transparent scenarios using contract terms.
historical_policy|A Household Finance Rule Changed|Who became eligible after one dated policy change?|Compare legal text, implementation, and take-up.
inflation_effect|A Budget in Real Terms|Which expenses changed most for a defined household under inflation?|Use dated price series and a clearly labeled basket.
fraud_warning|Verifying a Money Offer|Which statements in a financial offer can be checked independently?|Use official records and alerts without detailing scam methods.
comparison_method|Two Options, Same Assumptions|How do two savings or credit products compare for one use case?|Use identical balances, dates, fees, liquidity, and risk criteria.
access_gap|Who Is Excluded From a Product?|Which rule or cost blocks a defined group from financial access?|Use eligibility terms and published access data.
uncertainty_range|A Budget With Variable Income|How does an income range change an example household buffer?|Vary one input at a time and label all assumptions.
field_fee_structure|Finding All the Charges|Which costs appear in a product disclosure and which depend on behavior?|Use a dated fee schedule and two illustrative patterns.
field_risk_disclosure|Risk Language in a Product Document|Which risk does a disclosure describe clearly or obscure?|Compare the stated risk with the product's actual mechanics.
field_regulatory_protection|Protection Depends on Product Type|What protection applies to one account or investment in one jurisdiction?|Separate deposit, investment, and insurance rules.
field_household_effect|Who Feels a Rate Change?|How does a rate change affect two households with different contracts?|Use labeled hypothetical balances and reset rules.
field_market_cycle|A Household Through a Cycle|How did income, debt cost, and savings change through one economic cycle?|Use dated, comparable household data rather than a market index alone."""

CREDIT_CARDS = """history_origins|How Credit Cards Became Common|Which rule or network change widened card use in one market?|Use dated issuer, network, and regulatory records.
famous_examples|A Card Offer Under the Microscope|What does a widely promoted card offer actually cost for a defined use?|Read its dated agreement and model transparent scenarios.
hidden_stories|The People Behind Card Payments|Whose labor and decisions are invisible in a card transaction?|Trace issuer, merchant, network, and service roles.
beginner_explainers|Reading a Card Statement|What do balance, minimum payment, due date, and interest line mean?|Walk through an illustrative statement under stated terms.
advanced_concepts|Interest Across Billing Cycles|How can payment timing alter interest on a revolving balance?|Use a dated agreement and transparent arithmetic.
mysteries_unsolved_cases|Why a Card Charge Appeared|Which records can resolve a disputed charge and which cannot?|Trace transaction, authorization, posting, and dispute evidence.
technology_innovation|A New Payment Authentication Method|Did one authentication change reduce a measured fraud pattern?|Compare a documented rollout with before-and-after data and limits.
people_personalities|Who Sets a Card's Terms?|Which issuer or regulator decision changed a cardholder's costs?|Use dated agreement notices and policy records.
major_events|A Credit-Card Rule Changed|What changed for cardholders after one dated rule took effect?|Compare legal requirements with issuer practice and outcomes.
how_it_works|A Card Purchase End to End|What happens between a card tap and merchant settlement?|Map authorization, clearing, settlement, fees, and possible reversals.
rise_fall|A Balance That Grew|How can a revolving balance grow even when payments continue?|Use a hypothetical schedule with explicit rates, fees, and purchases.
then_vs_now|Card Terms in Two Periods|How did one common card term change over time?|Compare dated agreements using the same use pattern.
future_developments|A Conditional Card Payment Change|Which constraint would shape adoption of a new card feature?|Assess security, network support, cost, and access without prediction.
myths_vs_facts|Testing a Card Score Claim|Does a common claim about card use and credit scores match documented rules?|Specify jurisdiction and distinguish lender policy from scoring model.
documentary_stories|One Billing Dispute's Record|How did a cardholder's dispute proceed under the applicable rules?|Use consented or anonymized records and dated deadlines.
product_terms|The Clause Behind the APR|Which agreement term controls interest for one type of balance?|Read purchase, transfer, and cash-advance provisions separately.
household_cash_flow|Card Due Dates and Pay Dates|How does a due date affect a household's cash timing?|Use a fictional, labeled pay calendar and agreement terms.
risk_and_time|Promotional Rate Expiry|What happens when a promotional rate ends with a balance remaining?|Model one disclosed offer with explicit dates and conditions.
fee_effect|Annual, Late, and Transaction Fees|Which charges apply to a defined pattern of card use?|Read a dated fee table and avoid treating all cardholders alike.
consumer_protection|What a Billing Dispute Right Covers|Which transactions and deadlines are covered in one jurisdiction?|Use regulator guidance and a dated agreement.
market_vs_household|Rates and the Cardholder|Why can a benchmark-rate change affect two cardholders differently?|Compare variable and fixed terms with payment behavior.
historical_policy|A Card Protection in Practice|Did a dated card rule change fees or access for a defined group?|Compare policy intent, implementation, and observed outcomes.
inflation_effect|Prices, Card Balances, and Payments|How might a price shock change revolving balances for a defined group?|Use dated survey data and avoid asserting a single cause.
fraud_warning|Checking a Card Alert|Which details of a suspicious card alert can be verified safely?|Use issuer and regulator advice without reproducing attack steps.
comparison_method|Two Cards on Equal Use|Which card costs less for the same hypothetical purchases and payments?|Include rates, annual fees, rewards limits, and relevant dates.
access_gap|Who Qualifies for a Card?|Which eligibility or documentation rule restricts access?|Use issuer criteria and published data for a defined population.
uncertainty_range|Variable Rate, Variable Cost|How does a range of rates alter a revolving-balance illustration?|Show transparent assumptions and avoid a personalized recommendation.
field_fee_structure|Where Card Fees Enter|Which charges come from issuer terms and which from transaction context?|Separate annual, foreign, cash-advance, late, and merchant-side charges.
field_risk_disclosure|Reading a Card's Key Facts|Which important cost is easy to miss in a card disclosure?|Compare summary terms with full agreement for a dated offer.
field_regulatory_protection|Card Rules and Provider Duties|Which consumer rule applies to a named card arrangement?|Specify card type, provider, jurisdiction, and date.
field_household_effect|A Minimum Payment Illustration|How does paying only a stated minimum affect a hypothetical balance?|Use the exact agreement formula and explicit purchase assumptions.
field_market_cycle|Card Delinquencies Over Time|How did card balances and late payments move through one cycle?|Use comparable issuer or regulator data and note confounders."""


if __name__ == "__main__":
    revise_domain("008", "008_personal_finance", PERSONAL_FINANCE,
                  "Household cash flow, saving, debt, product terms, consumer rights, and uncertainty in defined examples.",
                  "dated product disclosures, regulator education and complaint data, household surveys, and transparent hypothetical calculations",
                  "State jurisdiction and assumptions; avoid individualized financial advice or guarantees.")
    revise_domain("294", "294_credit_cards", CREDIT_CARDS,
                  "Credit-card agreements, billing, interest, payments, disputes, access, and consumer protections in named jurisdictions.",
                  "dated card agreements, regulator rules and data, issuer disclosures, and transparent billing calculations",
                  "State jurisdiction, card type, dates, and applicable terms; avoid individualized financial advice.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
