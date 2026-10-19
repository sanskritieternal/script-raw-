"""Editorial questions for records and extremes."""

from review_angle_plans import audit, revise_domain


EXTREMES = """history_origins|When a Record Category Began|Who first defined and measured one extreme?|Trace rule, instrument, coverage, and purpose.
famous_examples|A World Record Rechecked|What evidence supports one widely cited record?|Verify category, date, authority, instrument, and competing claims.
hidden_stories|The Observers Behind a Record|Who measured, calibrated, reviewed, and preserved the evidence?|Credit local observers, technicians, and evaluators.
beginner_explainers|What Counts as a Record?|Which definition, geographic scope, and time span govern one claim?|State eligibility, units, data start, and verification process.
advanced_concepts|An Extreme in a Sparse Dataset|How does limited coverage affect confidence in a record?|Compare missing places, instrument changes, sampling, and uncertainty.
mysteries_unsolved_cases|A Contested Record|Why do two authorities disagree on one extreme?|Compare definitions, source records, corrections, and unresolved issues.
technology_innovation|A Sensor Changes the Leaderboard|How did a new measurement tool alter reported extremes?|Check calibration, detection limits, coverage, and comparability.
people_personalities|An Evaluator's Judgment|How did one expert panel assess a disputed record?|Use published method, evidence, dissent, and decision.
major_events|The Day a Record Was Set|What conditions produced one documented extreme?|Compare contemporaneous observations and avoid single-cause claims.
how_it_works|How a Record Is Certified|What steps turn a measurement into an accepted record?|Follow observation, quality control, independent review, and archive.
rise_fall|A Record Later Withdrawn|Which new evidence changed the official listing?|Trace original basis, reanalysis, decision, and correction.
then_vs_now|Old and New Records Compared|Are two measurements truly comparable?|Check instrument, site, definition, precision, and time window.
future_developments|Could a Record Be Broken?|What can projections say about a future extreme category?|State model, scenario, uncertainty, and limits of individual prediction.
myths_vs_facts|The Biggest Ever?|Does a superlative claim survive a precise category definition?|Search original record and specify known exceptions.
documentary_stories|A Record Through Its Evidence File|How was one remarkable claim proposed, challenged, and accepted?|Follow original data, review, revisions, and public communication.
observation_to_explanation|An Extreme Measurement's Cause|Which processes plausibly contributed to one event?|Use multi-source evidence and distinguish association from attribution.
measurement_method|A Reading at the Limit|How was one extreme value measured and validated?|Explain instrument range, calibration, siting, quality control, and error.
scale_and_timespan|Hourly, Daily, and Lifetime Records|How does aggregation change which observation wins?|Compare intervals, units, coverage, and category rules.
field_vs_lab|A Controlled Limit Versus Nature|Can a laboratory extreme be compared with a field record?|Match definition, conditions, measurement, and context.
natural_variation|Extremes Within a Distribution|What makes one value unusual relative to its baseline?|Check sample length, season, location, and statistical uncertainty.
mechanism_chain|From Conditions to Record|Which documented chain led to one measured extreme?|Identify each supported link and competing explanations.
extreme_case|The Outlier That Tests the Rule|Does one extreme reveal a real process or an error?|Compare independent observations, physical plausibility, and review.
classification_debate|Two Categories, Two Champions|How do different classifications change a record holder?|Compare eligibility, threshold, exclusions, and authority.
interacting_systems|Several Causes of an Extreme|Which factors combined in one exceptional outcome?|Use measured interactions and avoid attributing all change to one factor.
data_gap|An Unobserved Place or Period|Could missing data hide a more extreme value?|Map coverage, preservation, method, and limits on conclusion.
prediction_test|A Forecast and the Record|Did a dated forecast capture the event's magnitude and location?|Compare issued forecast, uncertainty, later observation, and revisions.
human_impact|Lives Behind a Superlative|How did one extreme affect people without turning suffering into spectacle?|Use verified impacts and consented accounts with context.
field_proof_or_test|What Would Settle a Claim?|Which independent evidence could confirm or reject one record?|Specify records, calibration, witnesses, and decision authority.
field_definition_choice|The Rule That Changes the Answer|Which defensible category definition yields each result?|Present alternatives clearly and avoid one unqualified superlative.
field_model_assumptions|Estimating an Unmeasured Extreme|Which assumptions drive one modeled maximum?|Show inputs, sensitivity, uncertainty, and lack of direct observation.
field_counterexample|A Claim Meets an Earlier Case|Does a documented counterexample invalidate a record claim?|Check eligibility, dates, quality, and comparable measurement.
field_teaching_difficulty|Why Records Mislead|Which common confusion makes one extreme hard to understand?|Test explanations of units, baseline, rarity, and verification.
"""


if __name__ == "__main__":
    revise_domain("163", "163_records_extremes", EXTREMES,
                  "Records and extremes through category definitions, measurement, verification, uncertainty, context, and human consequences.",
                  "original observations and instrument metadata, authority rules and review decisions, calibration and quality-control records, comparable historical datasets, and documented impacts",
                  "Name record category, geographic scope, interval, authority, and date. Do not use an unqualified ever claim, distinguish measured from modeled extremes, and verify that the cited record remains current.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
