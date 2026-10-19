"""Editorial question-design revision for niche 298 Central Banking."""
from review_angle_plans import revise_domain, audit

CENTRAL_BANKING = """history_origins|Why a Central Bank Was Established|Which problem was one central bank created to address?|Use the founding law and contemporary debates for a named jurisdiction.
famous_examples|A Central Bank Decision in Context|What did one widely cited policy decision achieve and fail to achieve?|Compare its stated objective, available evidence, and later outcomes.
hidden_stories|The People Behind a Policy Decision|Whose work or experience is absent from the official account of one decision?|Use attributed staff, legislative, and affected-community records.
beginner_explainers|What a Central Bank Is Mandated to Do|Which duties does a named central bank have under law?|Distinguish its legal mandate from commercial banking and fiscal policy.
advanced_concepts|Policy Tradeoffs Under Uncertainty|How did a central bank weigh conflicting indicators before one decision?|Compare forecasts, minutes, and data available at the time.
mysteries_unsolved_cases|Why a Policy Had an Unexpected Effect|Which explanations remain plausible for a policy outcome?|Separate measured effects from competing causal accounts.
technology_innovation|The Infrastructure of Monetary Operations|Which operational change altered how a central bank implements policy?|Trace a dated payment, reserve, or trading-system change.
people_personalities|Who Had the Vote?|How did governance rules shape a consequential central-bank decision?|Map appointment, voting, dissent, and recorded reasoning.
major_events|A Crisis Response Timeline|What did a central bank do at each stage of one financial shock?|Use dated announcements and balance-sheet data; distinguish aims from results.
how_it_works|From Policy Rate to Borrowing Cost|How can a policy-rate change reach households and firms?|Trace banking, market, and expectation channels in one jurisdiction.
rise_fall|Credibility After a Policy Error|How did an institution respond when a policy missed its objective?|Compare stated target, observed result, and later explanation.
then_vs_now|Two Monetary Frameworks|How did one central bank's framework change between two periods?|Compare mandates, instruments, communication, and outcomes consistently.
future_developments|A Conditional Policy Challenge|Which constraint would shape a future central-bank response?|State a dated scenario and alternative responses without prediction.
myths_vs_facts|Testing a Central-Bank Claim|Does a common claim about money creation match institutional records?|Define the claim and examine balance sheets, law, and operational rules.
documentary_stories|One Decision Through Its Papers|What do minutes, speeches, and data reveal about one policy decision?|Build a dated source trail and identify what was unknown then.
product_terms|The Terms of a Liquidity Facility|Which eligibility and collateral terms governed one central-bank facility?|Use the official facility notice and distinguish it from a consumer product.
household_cash_flow|Policy and Household Payments|How did a policy-rate move affect a defined household cost?|Use a dated, labeled example and actual contract-reset rules.
risk_and_time|Timing in Monetary Transmission|Why can a policy change have different effects over different horizons?|Compare immediate market effects with later lending and price data.
fee_effect|The Cost of Central-Bank Operations|Which operational or interest costs appeared on a central bank's balance sheet?|Read dated accounts and explain accounting limits; avoid treating them as retail fees.
consumer_protection|The Boundary Between Central Bank and Consumer Regulator|Which institution handles a specific banking consumer protection?|Map legal mandates in one jurisdiction and identify any shared duties.
market_vs_household|Market Reaction and Household Reality|Why can a market response differ from later household effects?|Compare dated market measures with household lending or price data.
historical_policy|A Change in the Policy Framework|Why did one central bank change its monetary framework?|Use official statements, legislative changes, and subsequent evaluations.
inflation_effect|Inflation Target and Lived Prices|How does an aggregate inflation measure relate to different household baskets?|Compare official components and distributional evidence without personal advice.
fraud_warning|Impersonation of a Central Bank|How can the public verify a message claiming central-bank authority?|Use official public notices and avoid repeating a fraud script.
comparison_method|Two Central Banks, One Mandate Question|How do two institutions with different legal mandates respond to the same shock?|Compare jurisdiction, objectives, tools, and time period before judging outcomes.
access_gap|Who Can Use Central-Bank Facilities?|Which institutions qualify for one liquidity or settlement facility?|Read the official eligibility rules and explain exclusions and rationale.
uncertainty_range|Forecast Ranges and Policy Choices|Which forecast assumption most changed a central bank's decision space?|Compare official scenarios and their dated uncertainty bands.
field_fee_structure|The Price of Reserve Services|How does a central bank set terms for one reserve or payment service?|Use official tariffs or interest terms, not retail account fees.
field_risk_disclosure|How Policy Risks Are Disclosed|Which risks did one policy statement identify at the decision date?|Compare the statement with later evaluations and omitted uncertainties.
field_regulatory_protection|A Central Bank's Supervisory Role|Which stability or supervisory power did a named central bank legally hold?|Distinguish its duties from separate regulators and deposit insurers.
field_household_effect|Distributional Effects of a Policy Move|Which households faced different costs after one policy change?|Use disaggregated, dated data and avoid a universal conclusion.
field_market_cycle|Monetary Policy Across a Cycle|How did a central bank change its stance through one economic cycle?|Compare objectives, decisions, inflation, output, and financial stress by date."""


if __name__ == "__main__":
    revise_domain(
        "298", "298_central_banking", CENTRAL_BANKING,
        "Central-bank mandates, monetary operations, transmission, crisis facilities, governance, and effects in named jurisdictions.",
        "founding law, dated monetary-policy statements and minutes, official facility terms, central-bank accounts, and independently sourced macroeconomic data",
        "Separate central banks from retail banks and other regulators; date policy claims and avoid individualized financial advice.",
    )
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
