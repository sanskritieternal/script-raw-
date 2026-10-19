"""Editorial questions for rankings and comparisons."""

from review_angle_plans import audit, revise_domain


RANKINGS = """history_origins|How a Ranking Began|Who chose the first criteria for one published ranking?|Trace founding purpose, data, weights, and target audience.
famous_examples|A Famous Top-Ten List Tested|Does one popular list answer the question its title implies?|Check population, criteria, missing entries, date, and source.
hidden_stories|Work Behind a Score|Whose data collection and judgment shape one index?|Trace respondents, coders, auditors, funding, and local context.
beginner_explainers|Reading a Ranking Responsibly|What does a position actually mean for one measured group?|Explain unit, score, margin, coverage, and tie rules.
advanced_concepts|How Weights Move the Winners|Would plausible weighting changes alter one ranking?|Recalculate sensitivity and show stable and unstable positions.
mysteries_unsolved_cases|A Sudden Rank Jump|Did one entity improve or did measurement change?|Compare raw indicators, definitions, missing data, and methods.
technology_innovation|An Algorithmic Recommendation List|How does one platform order options for a defined user?|Examine objective, inputs, paid placement, testing, and drift.
people_personalities|Who Designed the Index?|Which decisions did the authors make and why?|Use methodology, interviews, critiques, and revision history.
major_events|A Ranking After a Method Change|What changed in positions when one methodology was revised?|Recreate old and new scores on comparable data.
how_it_works|From Measurements to Rank|How are raw data cleaned, normalized, weighted, and sorted?|Walk through one transparent example with uncertainty.
rise_fall|A Leader Loses Its Place|Which measured changes explain one entity's fall?|Separate real changes from eligibility, data, and scoring revisions.
then_vs_now|Comparing Editions of One Ranking|Can positions from two years be compared?|Check item set, methods, units, coverage, and archived versions.
future_developments|A Proposed New Index|Would one new measure improve decisions?|Test validity, data burden, gaming, uncertainty, and user need.
myths_vs_facts|Number One for Everyone?|Does the top choice remain best under different priorities?|Compare profiles and avoid a universal verdict.
documentary_stories|Following a Ranking's Consequences|How did one list affect behavior or funding?|Trace publication, response, decisions, and alternative causes.
lived_experience|A Ranked Person's or Place's View|How do affected people interpret a score?|Use consented accounts alongside methodology and outcome data.
institutional_pathway|Where Ranking Data Come From|Which organizations collect and verify the inputs?|Map submissions, audits, incentives, and missing records.
incentives_norms|How a Score Changes Behavior|Did participants adapt practices to improve a metric?|Compare rules, responses, outcomes, and unintended effects.
access_and_exclusion|Who Is Missing from the List?|Which places or people were excluded by data or eligibility?|Check rules, coverage, language, cost, and access.
community_variation|One Score, Different Experiences|Does an average hide variation within a ranked group?|Disaggregate where justified and protect small populations.
policy_in_practice|A Decision Based on Rank|Was a ranking suitable for one actual policy choice?|Compare intended use, uncertainty, alternatives, and consequences.
survey_vs_story|Poll Results and Anecdotes|Do individual accounts fit the distribution measured?|Check sample, question wording, nonresponse, and context.
power_and_voice|Who Gets to Define Best?|Whose values are embedded in categories and weights?|Read consultation, governance, funding, and dissent.
unintended_consequence|When a Ranking Encourages Gaming|Did publication shift effort toward measurable proxies?|Compare behavior, target outcomes, and metric revisions.
comparative_setting|Two Lists of the Same Subject|Why do two reputable rankings disagree?|Compare populations, criteria, weights, dates, and uncertainty.
change_over_time|A Trend Beyond Position|Does an entity's actual score change when rank does?|Plot matched measures and note changes in competitors.
ethical_dilemma|Should People Be Ranked?|What harm can a public league table cause in one setting?|Assess consent, stigma, validity, benefits, and alternatives.
field_source_verification|Rebuilding the Top Five|Can a reviewer reproduce one list from original data?|Archive inputs, exclusions, formula, and discrepancies.
field_story_framing|The Headline Above a Ranking|Does a catchy superlative preserve methodological limits?|Compare headline, findings, caveats, and correction need.
field_audience_measurement|What Readers Infer from a Rank|Do readers understand score gaps and uncertainty?|Test comprehension with representative users.
field_platform_incentive|Paid Placement in a Best-Of List|Could commercial relationships influence order?|Review disclosures, affiliate terms, scoring, and independent results.
field_editorial_correction|Correcting a Misranked Entry|How should one data or method error be repaired?|Publish original and revised values, cause, affected positions, and date.
"""


if __name__ == "__main__":
    revise_domain("164", "164_rankings_comparisons", RANKINGS,
                  "Rankings and comparisons through definitions, data provenance, weighting, uncertainty, incentives, and actual decision use.",
                  "original datasets and metadata, published scoring rules, version histories, sensitivity analyses, independent audits, and consented accounts from affected groups",
                  "Name population, metric, geography, date, and intended use. Show sensitivity to weights and missing data, disclose commercial incentives, and avoid universal best claims when preferences differ.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
