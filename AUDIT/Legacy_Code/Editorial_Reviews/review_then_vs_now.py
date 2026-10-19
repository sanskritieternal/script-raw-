"""Editorial questions for then-versus-now stories."""

from review_angle_plans import audit, revise_domain


THEN_NOW = """history_origins|When a Comparison Began|Why did people first measure one changing feature?|Trace original purpose, population, method, and archive.
famous_examples|A Familiar Before-and-After Image|Does one striking pair show the same place and conditions?|Check coordinates, season, camera, editing, date, and context.
hidden_stories|Who Is Missing from the Old View?|Whose lives were not counted or photographed in one era?|Compare archive, population, access, and surviving testimony.
beginner_explainers|Making Two Dates Comparable|What must match before claiming a change?|Specify place, measure, population, units, season, and method.
advanced_concepts|A Trend Through Changing Definitions|How can an indicator be compared after its definition changed?|Reconstruct a common series or state the break explicitly.
mysteries_unsolved_cases|An Apparent Sudden Shift|Did a real change occur or did the measurement system change?|Compare records, instrument, boundaries, missing data, and witnesses.
technology_innovation|A New Tool Changes What We See|How did better measurement alter one historical comparison?|Compare old and new detection limits, coverage, and calibration.
people_personalities|A Life Across Two Eras|How does one person's experience illuminate broader change?|Use consented recollection and contemporaneous records without universalizing.
major_events|Before and After a Turning Point|What changed following one documented event?|Track timing, control or comparison, confounders, and affected groups.
how_it_works|Rebuilding a Comparable Series|How are two versions of a measure aligned?|Show source, transformations, assumptions, and uncertainty.
rise_fall|An Institution's Long Arc|Did one organization's service actually improve or decline?|Compare outcomes, users, resources, mission, and coverage.
then_vs_now|The Same Task in Two Periods|How did time, cost, access, and quality change for one task?|Choose matched user and conditions and adjust money consistently.
future_developments|Extrapolating a Past Trend|Which assumptions would have to hold for change to continue?|Test structural breaks, constraints, and alternative scenarios.
myths_vs_facts|Was the Past Simpler?|Does one nostalgic claim fit evidence for named people and places?|Compare benefits, burdens, excluded groups, and measurement quality.
documentary_stories|Returning to One Location|What does a repeat visit reveal and conceal?|Match vantage point, season, scope, and local accounts.
lived_experience|Memory and Dated Evidence|How do memories of change align with records?|Treat recollection as evidence of experience and check measurable claims.
institutional_pathway|A Policy's Long Implementation|What happened between a rule's adoption and its current practice?|Trace budgets, staff, enforcement, revisions, and results.
incentives_norms|Changed Rewards, Changed Behavior|Did new incentives help drive an observed change?|Compare payoffs, participation, timing, and competing causes.
access_and_exclusion|Who Could Use It Then and Now?|Did a service expand for some while excluding others?|Disaggregate price, location, language, disability, and eligibility.
community_variation|Different Histories in One Place|How do groups describe and measure change differently?|Use diverse sources and avoid a single community narrative.
policy_in_practice|A Reform Across Time|Did the intended benefit appear after implementation?|Compare stated goal, rollout, outcome, and alternative influences.
survey_vs_story|A Trend and a Vivid Anecdote|Does one remembered experience fit population evidence?|Check survey design, recall, sampling, and variation.
power_and_voice|Who Chose the Baseline?|Which date and metric make one change look favorable?|Test alternative baselines and identify interested parties.
unintended_consequence|A Gain with a Cost|Did one improvement create a new burden elsewhere?|Compare linked outcomes and affected groups across time.
comparative_setting|Two Places, Same Era Shift|Why did a similar change occur differently in two places?|Match definitions, context, policies, and timing.
change_over_time|More Than Two Snapshots|What happened between the chosen before and after dates?|Use a full time series where possible and show reversals.
ethical_dilemma|An Old Image of a Person Today|Can a historic photo be reused without exposing or misrepresenting someone?|Check rights, consent where feasible, context, and present harm.
field_source_verification|Dating a Before Photo|What proves one image's place, date, and authenticity?|Trace original negative or file, archive metadata, and corroboration.
field_story_framing|A Transformation Headline|Does one title imply a cause the evidence cannot support?|Compare wording to measurements and alternative explanations.
field_audience_measurement|What Viewers Infer from Two Images|Do audiences notice scale, season, and missing intervals?|Test interpretation and revise labels accordingly.
field_platform_incentive|Before-and-After for a Feed|How does a short format reward dramatic but unrepresentative pairs?|Compare selection, editing, reach, caveats, and source access.
field_editorial_correction|Fixing a False Comparison|What must change when one date or definition proves wrong?|Document original claim, corrected evidence, revised image, and notice.
"""


if __name__ == "__main__":
    revise_domain("165", "165_then_vs_now", THEN_NOW,
                  "Then-versus-now stories through matched measures, archival provenance, changing definitions, multiple time points, and varied experiences.",
                  "dated original images and records, comparable time series with metadata, policy and institutional histories, documented transformations, and consented firsthand accounts",
                  "Name place, population, metric, baseline, and end date. Do not infer causation from two snapshots; disclose breaks in definitions, inflation adjustments, archive gaps, and image edits.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
