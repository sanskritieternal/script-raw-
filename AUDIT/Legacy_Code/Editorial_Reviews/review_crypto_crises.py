"""Editorial question-design revisions for cryptocurrency and economic crises."""
from review_angle_plans import revise_domain, audit

CRYPTO = """history_origins|From Digital Cash Ideas to Crypto Networks|Which design problem did an early crypto network set out to solve?|Trace a dated proposal, launch, and actual design choices.
famous_examples|A Crypto Project Behind the Headline|What did one prominent network or token demonstrate in practice?|Separate its stated purpose from measured use and failures.
hidden_stories|Who Maintains the Network?|Whose technical and governance labor is missing from a project's public story?|Trace named contributors, funding, and decision processes.
beginner_explainers|Token, Network, and Custody|What does a user actually own or control in one crypto arrangement?|Distinguish the token, ledger, wallet keys, and intermediary claim.
advanced_concepts|Consensus and Finality|When is a transaction considered final on a named network?|Explain the rule, assumptions, delays, and failure modes.
mysteries_unsolved_cases|An Unexplained Market Move|Which explanations for a documented crypto-market event remain unproven?|Compare dated trades, disclosures, and missing data without assigning motive.
technology_innovation|A Claimed Protocol Advance Tested|Which constraint did a protocol change measurably address?|Compare throughput, security, cost, and decentralization before and after.
people_personalities|Governance Beyond the Founder|Who can change a crypto protocol or service?|Map maintainers, validators, issuers, users, and formal control.
major_events|A Network Disruption Reconstructed|What failed during one documented outage or exploit?|Use public incident reports and consequences; omit actionable attack steps.
how_it_works|A Crypto Transfer End to End|What happens from signing a transfer to settlement or redemption?|Trace wallet, network, intermediary, fees, and finality for one asset.
rise_fall|A Project's Growth and Collapse|Which documented dependencies failed when a crypto project contracted?|Compare claims, reserves or funding, governance, and dated outcomes.
then_vs_now|One Network Across Two Versions|Which material properties changed after a protocol upgrade?|Compare compatible metrics and user effects at two dates.
future_developments|A Conditional Crypto Use Case|What must change before a proposed crypto use case works at scale?|State technical, legal, cost, and adoption assumptions.
myths_vs_facts|Testing a Crypto Promise|Does a common promise about anonymity or decentralization hold for one system?|Define the claim and inspect architecture and real-world operation.
documentary_stories|One Token's Paper Trail|What do issue documents and transaction records show about one token?|Trace issuance, governance, distribution, and later changes.
product_terms|The Claim Behind a Stablecoin|What exactly can a holder redeem, from whom, and under which terms?|Read issuer terms and dated reserve disclosures for one product.
household_cash_flow|Payment Use Versus Price Exposure|What costs and volatility arise when a household uses one crypto payment route?|Use a labeled hypothetical payment and dated fees.
risk_and_time|Risks Before and After Settlement|Which risks change while a crypto transaction is pending or held?|Separate network, custody, issuer, and market risks by stage.
fee_effect|The Real Cost of a Crypto Transfer|Which network and intermediary charges apply to one transfer?|Use dated fee schedules and a transparent scenario.
consumer_protection|What Protection Actually Applies|Which protections cover a user of one crypto service in a named jurisdiction?|Check legal classification, registration, custody terms, and exclusions.
market_vs_household|A Price Rally and a User's Exposure|Why does a market headline not describe one holder's actual outcome?|Distinguish entry price, fees, custody, liquidity, and taxes.
historical_policy|A Crypto Rule in Practice|What changed after one jurisdiction adopted a crypto rule?|Compare legal text, implementation, and observed compliance.
inflation_effect|Crypto and an Inflation Claim|Does a claimed inflation hedge hold over a specified period?|Define the asset, currency, horizon, and comparison measure.
fraud_warning|Checking a Token Promotion|Which claims in a crypto promotion can be verified from primary records?|Inspect issuer identity, rights, disclosures, and official alerts.
comparison_method|Two Crypto Arrangements Compared Fairly|How do two named arrangements differ in control, fees, and risk?|Use the same user task, jurisdiction, and date.
access_gap|Who Can Actually Use the Network?|Which device, connectivity, identity, or fee barrier limits participation?|Compare the protocol's open design with actual access requirements.
uncertainty_range|More Than One Crypto Outcome|Which assumptions dominate a hypothetical crypto-use cost or return range?|Vary price, fees, liquidity, and time without forecasts or recommendations.
field_fee_structure|Network Fee and Service Fee|Who receives each charge in one crypto transaction?|Read protocol mechanics and intermediary terms separately.
field_risk_disclosure|What a Token Disclosure Leaves Out|Which material risk is described or absent in an issuer's disclosure?|Compare dated documents with the actual rights and dependencies.
field_regulatory_protection|One Activity, One Legal Classification|Which authority oversees a named crypto activity in one jurisdiction?|Distinguish asset type, exchange, custody, and payment functions.
field_household_effect|Crypto Use in a Household Budget|What happens when a household must pay a fixed bill with a volatile asset?|Use a clearly hypothetical cash-flow example and fees.
field_market_cycle|Liquidity Through a Crypto Downturn|How did trading depth or redemption change in one downturn?|Use dated market and issuer data, stating data gaps."""

CRISES = """history_origins|The Conditions Before a Crisis|Which vulnerabilities were visible before one economic crisis began?|Use dated credit, output, price, and policy records without hindsight.
famous_examples|A Crisis Often Used as a Template|Which features of a familiar crisis do not generalize to another?|Compare definitions, institutions, and transmission channels.
hidden_stories|Households Outside the Aggregate|Whose losses disappear inside a national crisis statistic?|Use disaggregated data and attributed lived accounts.
beginner_explainers|What Counts as an Economic Crisis?|How do recession, banking crisis, inflation shock, and sovereign distress differ?|Apply explicit definitions to one dated case.
advanced_concepts|A Shock Becomes a Feedback Loop|How did one initial shock amplify through credit, prices, or expectations?|Trace a proposed mechanism with dated evidence and alternatives.
mysteries_unsolved_cases|Why Did This Crisis Spread?|Which links in a crisis transmission chain remain disputed?|Compare competing explanations and missing data.
technology_innovation|A Financial Tool in a Crisis|Did one financial technology dampen or amplify a shock?|Compare its actual use, exposures, and measured effects.
people_personalities|Decision Makers Under Pressure|What did officials know when they chose a crisis response?|Use contemporaneous minutes, statements, and later reviews.
major_events|The Week a Crisis Escalated|Which events changed expectations during one bounded crisis window?|Build a dated timeline from primary records and market data.
how_it_works|From Shock to Job Loss|How did one shock travel from institutions to employment?|Trace credit, demand, business decisions, and time lags.
rise_fall|Recovery and Relapse|Why did one economy recover and then weaken again?|Compare output, jobs, prices, and policy by dated period.
then_vs_now|Two Crises, Same Measures|Which difference matters most when comparing two economic crises?|Hold definitions and denominators constant.
future_developments|Stress Signals, Not Predictions|Which measured vulnerability would worsen a hypothetical future shock?|State scenario assumptions and avoid predicting a crisis date.
myths_vs_facts|Testing a One-Cause Crisis Story|Does a popular single-cause explanation fit the evidence?|Compare multiple contributing mechanisms and their timing.
documentary_stories|One Firm Through a Crisis|What do records reveal about one firm's response to a downturn?|Use filings, employment records, and worker accounts in context.
product_terms|Contract Terms That Amplified Losses|Which loan or funding term worsened a documented crisis exposure?|Read dated contracts and separate borrower from system effects.
household_cash_flow|Income Shock in a Household|How did unemployment or price changes affect a defined household budget?|Use a labeled illustration supported by period data.
risk_and_time|The Timing of Crisis Losses|Why can short funding and long assets turn a shock into a run?|Use a simplified balance sheet and an identified crisis case.
fee_effect|Fees and Penalties During Distress|How did contract charges affect vulnerable borrowers in one crisis?|Use dated terms and measured incidence; avoid generalized advice.
consumer_protection|Protections Introduced After a Crisis|Which rule changed after a crisis, and whom did it cover?|Compare law, implementation, and documented exclusions.
market_vs_household|Market Stabilization and Family Recovery|Why can markets recover before household income does?|Compare dated asset, wage, employment, and debt measures.
historical_policy|A Crisis Policy Put to the Test|What did one fiscal or monetary response achieve?|Compare its stated target, rollout, counterfactual limits, and outcomes.
inflation_effect|Inflation During a Crisis|How did price increases affect different households in one crisis?|Use basket and income differences for a defined jurisdiction.
fraud_warning|Scams in a Crisis Environment|Which crisis-related claims did authorities warn consumers about?|Use official alerts without reproducing harmful tactics.
comparison_method|Comparing Crisis Responses|How did two jurisdictions respond to comparable shocks?|Match dates, exposure, institutions, and outcome measures.
access_gap|Who Missed Crisis Relief?|Which eligibility or delivery rule excluded a defined group?|Use program rules, take-up data, and participant accounts.
uncertainty_range|The Range of Recovery Forecasts|Which assumption explained differences between dated crisis forecasts?|Compare archived forecasts with later data, not hindsight alone.
field_fee_structure|Costs of Emergency Support|Who bore the fiscal or financial cost of one crisis facility?|Read dated facility terms, accounts, and later evaluations.
field_risk_disclosure|Warnings Before the Downturn|Which risk did institutions disclose before one crisis?|Compare contemporaneous filings with subsequent losses.
field_regulatory_protection|Safety Nets Under Stress|Which guarantee or resolution power was used in one crisis?|Specify jurisdiction, legal limit, and actual implementation.
field_household_effect|Distribution of Crisis Losses|Which groups experienced the largest employment or income losses?|Use comparable disaggregated data and context.
field_market_cycle|A Cycle in Credit and Output|How did credit, prices, and output move before and after a crisis?|Use dated series and avoid assuming correlation proves causation."""


if __name__ == "__main__":
    revise_domain("296", "296_cryptocurrency", CRYPTO,
                  "Crypto networks, tokens, custody, markets, governance, and legal protections in named jurisdictions.",
                  "protocol documents, dated transaction or market data, issuer terms, incident reports, and regulator publications",
                  "Date legal classifications and product terms; separate protocol claims from intermediary promises and avoid individualized financial advice.")
    revise_domain("299", "299_economic_crises", CRISES,
                  "Economic shocks, transmission, policy responses, distributional effects, and recovery in bounded historical cases.",
                  "dated macroeconomic series, policy records, financial disclosures, scholarly analyses, and attributed accounts",
                  "State definitions, jurisdictions, time windows, and causal uncertainty; avoid predictions or individualized financial advice.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
