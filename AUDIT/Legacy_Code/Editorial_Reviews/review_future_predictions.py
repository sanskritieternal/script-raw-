"""Editorial questions for future predictions and scenarios."""

from review_angle_plans import audit, revise_domain


FUTURES = """history_origins|How a Forecasting Method Emerged|Why was one method created and for which decisions?|Trace original use, data, assumptions, and revisions.
famous_examples|A Famous Prediction Audited|What exactly did one dated forecast say and how did it fare?|Archive wording, horizon, conditions, measure, and outcome.
hidden_stories|Who Does Scenario Work?|Whose data, modeling, local knowledge, and review shape a forecast?|Trace credited roles, funding, and missing perspectives.
beginner_explainers|Prediction, Projection, Scenario|How do these three kinds of future statement differ?|Use one concrete topic and label assumptions and probabilities.
advanced_concepts|Forecast Skill Against a Baseline|Does one method beat a simple alternative?|Compare out-of-sample cases, horizon, metric, and uncertainty.
mysteries_unsolved_cases|Why a Forecast Missed|Which assumptions or shocks explain one failed prediction?|Compare original model, later data, changed context, and unknowns.
technology_innovation|A Tool Claimed to Forecast Better|Does one new forecasting tool improve decisions?|Test independent cases, calibration, cost, transparency, and harm.
people_personalities|The Forecaster and the Decision Maker|How was uncertain information communicated and used?|Use dated memos, interviews, institutional constraints, and alternatives.
major_events|A Shock Outside the Model|How did one unexpected event change an earlier outlook?|Compare pre-event scenarios, model updates, and decisions.
how_it_works|Building a Scenario Set|How do assumptions become several plausible futures?|Show inputs, causal links, range, internal consistency, and limits.
rise_fall|A Forecast That Lost Credibility|Why was one once-influential projection revised or abandoned?|Trace errors, data changes, validation, governance, and use.
then_vs_now|Past Forecast Versus Present Outcome|How fair is a hindsight audit of one forecast?|Match original conditional assumptions, metric, geography, and date.
future_developments|The Next Milestone That Matters|Which near-term observation would update one long-term outlook?|Define signal, threshold, date, source, and alternative explanations.
myths_vs_facts|A Certain Future?|Does a confident public claim reflect the source's uncertainty?|Compare headline, model range, conditions, and expert caveats.
documentary_stories|A Decision Under Several Futures|How did one organization plan despite uncertainty?|Follow scenarios, reversible steps, monitoring, and results.
assumption_inventory|What Must Be True?|Which assumptions drive one specific prediction?|List technology, demand, policy, environment, and dependencies.
readiness_check|From Prototype to Deployment|Which evidence shows a proposed technology is mature enough?|Compare validated setting, integration, maintenance, cost, and oversight.
physical_limits|A Future Claim Meets Constraints|Do energy, materials, time, or land needs fit plausible supply?|Calculate bounded requirements and uncertainty.
governance_choice|Who Can Choose This Future?|Which rules and institutions shape whether one scenario occurs?|Trace authority, budget, public participation, and enforcement.
unequal_futures|Who Gains and Who Bears Risk?|How do a proposal's outcomes vary across groups?|Compare access, cost, labor, geography, and protections.
scenario_pair|Two Plausible Paths|How do outcomes differ under two transparent assumptions?|Hold other factors consistent and avoid presenting either as destiny.
failure_to_launch|Why a Promising Idea Stalled|Which barriers prevented one forecast application?|Check validation, funding, regulation, infrastructure, and demand.
unintended_effect|A Future Intervention's Side Effects|What plausible burdens could accompany one benefit?|Use analogues, mechanisms, affected groups, and monitoring plan.
social_adaptation|People Change Alongside Technology|How might use, institutions, and norms adapt to a new tool?|Ground possibilities in comparable cases and explicit uncertainty.
ethical_boundary|Should This Future Be Pursued?|Which values and rights are implicated by one proposal?|Present affected voices, governance choices, and alternatives.
signal_vs_hype|A Milestone or a Press Release?|Does one announcement show meaningful progress?|Check independently validated performance, scale, cost, and timeline.
reversible_steps|A Plan That Can Change Course|Which early actions allow learning without locking in harm?|Compare pilots, monitoring, stop criteria, and exit costs.
field_world_rule|Rules of a Scenario World|What explicit constraints make one scenario internally coherent?|State technology, institutions, resources, and what remains uncertain.
field_plausibility_boundary|Where a Scenario Stops Being Credible|Which assumption exceeds current evidence or physical limits?|Compare demonstrated capability, scaling, timelines, and bottlenecks.
field_point_of_view|Whose Future Is Being Told?|How does the outlook change when affected groups define success?|Include diverse priorities and disclose forecaster standpoint.
field_ethical_consequence|A Choice with Long-Term Effects|Which rights or obligations could one pathway create?|Trace causal assumptions, governance, alternatives, and uncertainty.
field_adaptation_choice|Responding to New Evidence|When should a plan be revised or abandoned?|Set measurable triggers, review dates, authority, and public feedback.
"""


if __name__ == "__main__":
    revise_domain("166", "166_future_predictions", FUTURES,
                  "Future predictions as conditional, testable scenarios shaped by assumptions, uncertainty, physical limits, governance, and affected people.",
                  "archived dated forecasts, model assumptions and version histories, independent validation, physical resource estimates, current policy records, and affected-community perspectives",
                  "Name horizon, geography, metric, scenario, and issue date. Distinguish prediction from conditional projection, avoid certainty from a prototype or press release, and test claims against baseline forecasts and real constraints.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
