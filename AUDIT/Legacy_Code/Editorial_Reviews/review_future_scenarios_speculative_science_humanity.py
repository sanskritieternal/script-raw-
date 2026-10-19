"""Editorial question designs for scenarios and speculative science."""

from review_angle_plans import audit, revise_domain


SCENARIOS = """history_origins|A Civilization Forecast Revisited|Which assumptions drove a dated future vision?|Compare forecast and outcome.
famous_examples|A Published Scenario Set|How did its pathways vary policy, technology, and social choices?|Read model documentation.
hidden_stories|Who Is Missing from Global Scenarios?|Which populations and unpaid work are absent from aggregate models?|Check variables and consultation.
beginner_explainers|Scenario versus Prediction|Why does a plausible pathway not assign one certain future?|Use a bounded example.
advanced_concepts|Coupled Social and Environmental Change|How do population, energy, food, and institutions interact?|Draw explicit causal model.
mysteries_unsolved_cases|Which Future Is More Plausible?|What indicators could distinguish two scenarios over time?|Name uncertainty.
technology_innovation|A Technology in a Scenario|Which adoption and resource assumptions enable its effect?|Separate invention from deployment.
people_personalities|A Scenario's Author|Which values and methods shaped one modeler's choices?|Read methods and critique.
major_events|A Shock to a Scenario|How did a real crisis expose model assumptions?|Compare pre-event version.
how_it_works|Building a Civilization Scenario|How do drivers, branching choices, model outputs, and narratives connect?|Show traceability.
rise_fall|A Forecast That Failed|Which premise or feedback was wrong?|Avoid hindsight simplification.
then_vs_now|Two Generations of Global Modeling|How did data, participation, and uncertainty reporting change?|Compare source documents.
future_developments|Several Civilizational Pathways|What policy and physical conditions distinguish them?|Keep plural and conditional.
myths_vs_facts|One Inevitable Global Future?|What choices and uncertainties make that claim unsound?|Use scenario contrasts.
documentary_stories|A Scenario's Policy Journey|How was a model used, contested, and revised?|Trace dated decisions.
assumption_inventory|Scenario Premise Register|Which growth, equity, climate, and governance choices are embedded?|Record ranges.
readiness_check|Using Scenarios for a Decision|Do alternatives, affected groups, and revision triggers appear?|Review decision process.
physical_limits|Civilization's Resource Constraints|Which energy, land, water, and material budgets bound a pathway?|Define scale and data.
governance_choice|Who Chooses the Future?|How do institutions and communities shape a modeled pathway?|Map decision power.
unequal_futures|Different Lives in One Scenario|Who gains and loses within a global average?|Disaggregate outcomes.
scenario_pair|Two Paths from the Same Starting Point|How do governance choices change outcomes?|Hold baseline consistent.
failure_to_launch|A Transformation That Stalled|Which finance, trust, or institutional barrier mattered?|Use historical analog with limits.
unintended_effect|A Solution Shifts Harm|Where could a modeled transition move costs elsewhere?|Track supply chains.
social_adaptation|Society Responds to Change|How do people alter behavior and institutions?|Avoid fixed-behavior assumption.
ethical_boundary|Trading Present Costs for Future Gains|Whose consent and rights constrain the scenario?|State value choices.
signal_vs_hype|A Scenario Headline|Does it accurately describe conditional model output?|Check assumptions and ranges.
reversible_steps|Adaptation under Uncertainty|Which choices can be revisited as signals emerge?|Set indicators.
field_human_agency|Human Choices in a Model|Are people represented as agents or fixed inputs?|Inspect model design.
field_body_and_identity|Whose Humanity Is Assumed?|How do health, disability, and identity vary across futures?|Use affected voices.
field_rights_framework|Rights across Pathways|Which existing protections could strengthen or erode?|Name place and institution.
field_resource_inequality|Resource Burdens by Region|Who extracts, consumes, and bears pollution?|Use disaggregated data.
field_institutional_adaptation|Institutions that Could Change|What capabilities enable revision rather than lock-in?|Compare governance cases.
"""

SCIENCE = """history_origins|Speculation before Measurement|How did one imaginative hypothesis become a testable question?|Trace primary work.
famous_examples|A Bold Physical Hypothesis|Which observations support and limit a named proposal?|Use original paper and follow-up.
hidden_stories|Who Builds the Evidence?|Which instrument and analysis teams are missing from a breakthrough story?|Use credits.
beginner_explainers|Possible, Plausible, Demonstrated|What evidence moves a claim between these labels?|Use one physics case.
advanced_concepts|Model Assumptions in Exotic Physics|Which simplifications make a result appear possible?|Inspect equations and regime.
mysteries_unsolved_cases|An Unexplained Observation|Which competing mechanisms fit the data?|Specify discriminating test.
technology_innovation|A Proposed Detector|Can current instruments measure the predicted signal?|Estimate sensitivity.
people_personalities|A Speculative Researcher's Argument|How did a named scientist bound a claim?|Read text and response.
major_events|A Claimed Anomaly Rechecked|What changed after calibration or independent replication?|Follow dated record.
how_it_works|From Theory to Experimental Test|How do prediction, apparatus, controls, and analysis connect?|Map one proposal.
rise_fall|A Hypothesis Ruled Out|Which observation closed part of parameter space?|State surviving variants.
then_vs_now|A Century of Speculative Ideas|Which became established and which remain untested?|Use dated evidence.
future_developments|A Testable Next Step|What experiment could narrow uncertainty?|State resources and limits.
myths_vs_facts|Mathematical Solution Equals Technology?|What physical constraints stand between equation and device?|Identify energy and stability.
documentary_stories|An Anomaly's Investigation|How did teams verify, contest, and revise a result?|Use primary records.
observation_to_explanation|From Strange Signal to Cause|Which alternative explanations must be excluded?|Use controls and independent instrument.
measurement_method|Measuring an Extreme Phenomenon|What can the instrument actually observe?|State calibration and proxy.
scale_and_timespan|Extrapolation beyond Tested Scale|Which parameters change across orders of magnitude?|Calculate range.
field_vs_lab|Laboratory Analog versus Universe|What feature is shared and what is not?|Declare analogy limits.
natural_variation|Noise and Apparent Anomalies|Could known variation produce the pattern?|Use baseline distribution.
mechanism_chain|A Speculative Mechanism's Steps|Which link has evidence and which is conjecture?|Show chain explicitly.
extreme_case|At the Limit of a Theory|Where does the mathematical approximation break?|State validity range.
classification_debate|What Counts as Evidence?|Do rival theories classify a signal differently?|Compare predictions.
interacting_systems|A Claim across Multiple Forces|Which ignored interaction could change the answer?|Test coupled model.
data_gap|Missing Observation|What measurement would most reduce uncertainty?|Specify feasible instrument.
prediction_test|A Falsifiable Prediction|What result would count against the claim?|Prestate threshold.
human_impact|Public Meaning of Speculative Science|How do headlines affect expectations and funding?|Track communication.
field_experimental_setup|Test without a Recipe|What controls and independent checks make a study credible?|Discuss design at conceptual level.
field_mathematical_model|Assumptions of an Exotic Model|Which boundary conditions produce its result?|Read source derivation.
field_measurement_error|Signal versus Instrument Artifact|How are systematic errors estimated?|Use calibration record.
field_scale_transition|From Demonstration to Application|Which laws and engineering limits apply at larger scale?|Show scaling calculation.
field_technology_application|A Claimed Future Device|What tested capability exists today?|Separate concept, prototype, and service.
"""

HUMANITY = """history_origins|Visions of Humanity's Distant Future|What period and values shaped a named vision?|Read original source.
famous_examples|A Long-Range Scenario|Which near-term decisions does it actually illuminate?|Treat as conditional.
hidden_stories|Excluded Futures|Whose descendants and cultures disappear in a single humanity narrative?|Compare perspectives.
beginner_explainers|Near, Long, and Ultimate Futures|Why do evidence and uncertainty change with time horizon?|Use concrete ranges.
advanced_concepts|Compounding Uncertainty|How do interacting unknowns limit very long-range forecasts?|Show sensitivity.
mysteries_unsolved_cases|Human Survival Far Ahead|Which hazards can be estimated and which remain unknowable?|Separate evidence levels.
technology_innovation|A Proposed Transformative Tool|What has actually been demonstrated and at what scale?|Use technology readiness.
people_personalities|A Futurist's Assumptions|Which values and data shaped one argument?|Read primary work and critique.
major_events|A Turning Point Reinterpreted|How did a real event change a future vision?|Compare dated accounts.
how_it_works|Constructing a Deep-Future Scenario|How do physical constraints, institutions, and values connect?|Make assumptions explicit.
rise_fall|A Failed End-of-History Claim|Which subsequent event contradicted it?|Avoid selective hindsight.
then_vs_now|Past Futures and Present Reality|What can forecast failures teach about humility?|Use multiple examples.
future_developments|Several Futures for Humanity|How do choices today alter only the nearer branches?|Avoid deterministic end states.
myths_vs_facts|One Ultimate Human Destiny?|Which physical and political uncertainties preclude certainty?|Distinguish belief and evidence.
documentary_stories|A Future Debate's Public Record|How did evidence, ethics, and politics shape discussion?|Use dated sources.
assumption_inventory|Deep-Future Premises|Which population, planetary, technological, and value assumptions are embedded?|List uncertainty.
readiness_check|Acting under Deep Uncertainty|Which present decisions are robust across very different futures?|Compare options.
physical_limits|Cosmic and Earthly Constraints|Which energy, distance, and environmental limits are established?|State timescale and model.
governance_choice|Who Speaks for Future People?|How can current institutions consider future interests?|Compare governance proposals.
unequal_futures|Many Human Futures at Once|How do class, region, and culture shape pathways?|Reject a single average.
scenario_pair|Two Long-Term Pathways|How does one policy choice alter nearer outcomes?|Hold physical baseline fixed.
failure_to_launch|A Grand Future Project Stalls|Which near-term resource or legitimacy gap blocks it?|Use actual project evidence.
unintended_effect|Today's Solution, Tomorrow's Lock-In|Could infrastructure foreclose future options?|Map irreversibility.
social_adaptation|Human Institutions Change|How might families, work, and identity evolve?|Mark speculation clearly.
ethical_boundary|Sacrifice for Distant Benefits|What rights constrain present costs imposed for a future vision?|State competing values.
signal_vs_hype|Certainty in a Distant Forecast|Which parts are measured, modeled, or philosophical?|Label confidence.
reversible_steps|Choices that Preserve Options|What can be monitored and revised later?|Define triggers.
field_human_agency|Agency in Humanity's Future|Which actions are choices rather than technological inevitabilities?|Identify decision-makers.
field_body_and_identity|Who Counts as Human in a Scenario?|How do disability, augmentation, and cultural identity challenge assumptions?|Use plural perspectives.
field_rights_framework|Rights of Present and Future People|Which legal protections exist and which are proposed?|Name jurisdiction.
field_resource_inequality|Who Uses Planetary Resources?|How would a pathway distribute extraction and environmental costs?|Use explicit model.
field_institutional_adaptation|Governance across Generations|Which institutions can learn and correct course?|Compare real mechanisms.
"""

if __name__ == "__main__":
    revise_domain("490", "490_future_civilization_scenarios", SCENARIOS,
                  "Future civilization scenarios through explicit drivers, plural paths, distributive effects, institutions, and revisable present choices.",
                  "IPCC scenario methodology, OECD strategic foresight, UN development assessments, model documentation, and affected-community input",
                  "Name horizon, geography, baseline, and choices. Scenarios are not predictions; global averages can hide inequity.")
    revise_domain("491", "491_speculative_science", SCIENCE,
                  "Speculative science through testable hypotheses, measurement, uncertainty, theory limits, and the gap between models and devices.",
                  "primary research papers, instrument methods, replication studies, model derivations, and independent experimental assessments",
                  "Name hypothesis, tested regime, observation, and alternative explanation. A mathematical possibility is not a working technology.")
    revise_domain("492", "492_ultimate_future_of_humanity", HUMANITY,
                  "Humanity's distant futures through multiple perspectives, physical bounds, intergenerational ethics, uncertainty, and present decisions.",
                  "IPCC scenario practice, OECD foresight methods, UN sustainability assessments, historical forecasts, and primary philosophical and policy proposals",
                  "State time horizon and evidence level. No single technological or civilizational destiny is established.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
