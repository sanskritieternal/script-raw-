"""Editorial question designs for niche 191, Fishing."""

from review_angle_plans import audit, revise_domain


FISHING = """history_origins|How Fishing Rights Took Shape|Which rules determined who could fish one waterbody?|Compare dated rights, gear rules, local practice, and enforcement.
famous_examples|A Famous Fishery Rechecked|What does one widely cited fishery reveal about harvest and recovery?|Define species, stock, location, years, and quality of catch data.
hidden_stories|Labor Behind the Catch|Whose work is missing from a familiar fishing story?|Trace crew, shore processors, guides, scientists, and enforcement staff.
beginner_explainers|Reading Fishing Rules|What must an angler verify before fishing one site?|Identify jurisdiction, license, species, season, size, gear, and closures.
advanced_concepts|Catch Is Not Stock Size|Why can recorded catches change without a matching population change?|Check effort, rules, gear, reporting, environment, and stock assessment.
mysteries_unsolved_cases|Why a Catch Collapsed|Which explanations fit a documented decline in one fishery?|Test abundance, effort, habitat, warming, reporting, and regulatory change.
technology_innovation|A Fishing Gear Change|Did one gear change alter catch, selectivity, or habitat impact?|Compare trials, adoption, cost, bycatch, and unintended effects.
people_personalities|A Fishery Decision Maker|How did one named person's choice change fishing access or management?|Use dated proposals, evidence, objections, and outcomes.
major_events|A Closure or Reopening|What changed after a major rule or environmental event in one fishery?|Separate short-term catch shifts from long-term stock effects.
how_it_works|How a Catch Limit Is Set|Which evidence and decisions lead to one fishing limit?|Trace survey data, model, uncertainty, public process, and rule.
rise_fall|The Changing Fate of One Stock|What drove a stock's measured rise or decline?|Compare standardized abundance estimates, removals, habitat, and climate.
then_vs_now|A Fishery Across Two Periods|How have access, gear, catch, and stock condition changed?|Use comparable dates, methods, units, and legal rules.
future_developments|A Fishery Under Changing Conditions|Which plausible factors could reshape one fishery?|State assumptions for habitat, temperature, demand, regulation, and effort.
myths_vs_facts|Does Release Mean Survival?|How well does evidence support a catch-and-release claim for one species?|Specify gear, handling, temperature, depth, and measured mortality.
documentary_stories|One Season in a Fishery|How did rules, conditions, and fishers' choices interact in one season?|Build a dated record from official data and consented accounts.
observation_to_explanation|From Few Bites to a Claim|Can one angler's observations explain a population trend?|Compare sampling effort, location, weather, and independent surveys.
measurement_method|Counting Recreational Catch|How does one survey estimate total recreational removals?|Examine sampling, nonresponse, uncertainty, and revisions.
scale_and_timespan|A Local Catch Versus a Regional Stock|At what scale is one fishing claim actually supported?|Define waterbody, stock boundary, season, and time series.
field_vs_lab|Fish Behavior in Experiment and Wild|Does a lab finding predict outcomes under actual fishing conditions?|Compare species, gear, temperature, handling, and field validation.
natural_variation|Normal Swings or a New Trend?|How much can abundance vary without a lasting stock change?|Use long series and environmental and measurement context.
mechanism_chain|From Habitat Change to Catch|What pathway links a habitat change to fish availability?|Separate recruitment, movement, abundance, effort, and catchability.
extreme_case|A Record Catch's Context|What makes one exceptional catch unusual?|Verify measurement, species, site, effort, and rules in force.
classification_debate|Which Species or Stock Is This?|How do identification or stock boundaries affect a fishing claim?|Compare taxonomy, genetic and movement evidence, and management units.
interacting_systems|Fish, Water, and People|How do harvest, water quality, habitat, and climate interact?|Choose one fishery and trace supported links without single-cause claims.
data_gap|The Fishery We Cannot Count Well|Which missing observations make a stock estimate uncertain?|Identify unreported catch, effort, discards, survey coverage, and bias.
prediction_test|Did a Fishery Forecast Hold?|How did a past projection compare with later stock observations?|Match model version, assumptions, dates, and measured outcomes.
human_impact|Who Bears a Fishery Rule?|How does one restriction affect anglers, workers, and ecosystems?|Compare distribution of costs, benefits, compliance, and stock response.
field_land_stewardship|Who Governs This Water?|How are fishing access and conservation duties shared?|Map jurisdiction, local rights, Indigenous roles, and public process.
field_seasonal_conditions|The Season Behind the Rule|How do breeding, movement, and weather shape one fishing season?|Compare biological evidence with current local dates and closures.
field_skill_and_safety|The Conditions for One Fishing Trip|Which site-specific skills and hazards matter for a defined trip?|Check vessel or bank access, weather, water, gear, and local safety notices.
field_resource_use|Harvest, Release, and Mortality|What total removals result from one type of fishing?|Count kept fish, discard mortality, unreported catch, and uncertainty.
field_local_knowledge|What Fishers Know and Surveys Miss|Which local observations can improve a fishery question?|Attribute consented accounts and test them against independent data.
"""


if __name__ == "__main__":
    revise_domain("191", "191_fishing", FISHING,
                  "Fishing through access rights, regulations, stock evidence, catch measurement, workers, habitat, and stewardship.",
                  "current jurisdiction-specific fishing rules, stock assessments, catch and effort surveys, habitat and climate records, and consented fisher and community accounts",
                  "Name species or stock, waterbody, jurisdiction, season, and date. Check current local rules before any practical guidance; distinguish catch, effort, and stock size and avoid presenting release as automatically harmless.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
