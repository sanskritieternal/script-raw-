"""Direct editorial review of documentary craft and broad science angles."""
from review_angle_plans import revise_domain, audit

DOCUMENTARY = """history_origins|A Documentary Form Emerges|Which dated films and production conditions shaped one nonfiction style?|Compare original works, equipment, institutions, and criticism.
famous_examples|A Celebrated Scene Examined|How did one famous documentary scene acquire its apparent immediacy?|Use production notes, raw material if available, and participant accounts.
hidden_stories|Labor Behind the Film|Whose research, translation, access, or editing work is absent from credits?|Compare records and consented collaborator accounts.
beginner_explainers|Evidence Becomes a Scene|How can a documentary build a scene from verifiable material?|Map source, participant, visual, edit, and disclosure decisions.
advanced_concepts|Narrative Versus Evidentiary Order|Where does a film's sequence differ from the underlying event timeline?|Compare edit, original records, and viewer inference.
mysteries_unsolved_cases|A Scene with Missing Source Material|What can and cannot be known about a disputed nonfiction scene?|Identify lost footage, conflicting accounts, and remaining records.
technology_innovation|A New Documentary Tool|How did one camera, archive, or synthetic-media tool change production?|Compare capability, provenance, disclosure, and failure risks.
people_personalities|A Filmmaker's Editorial Choice|What did a named maker decide and what did collaborators contest?|Use interviews, cuts, contracts, and participant views.
major_events|A Film Changes After Release|What changed after a correction, legal challenge, or new evidence?|Trace versions, public statements, participant effects, and distribution.
how_it_works|A Claim Through Production|How does one factual assertion move from research to final cut?|Track source ledger, script, edit, review, and citation.
rise_fall|A Documentary Style's Reception|Why did one approach gain attention and later criticism?|Compare films, audience, technology, and ethical debate.
then_vs_now|Two Eras of Nonfiction Production|How did consent, editing, and distribution change?|Use comparable projects and documented practices.
future_developments|A Proposed Documentary Workflow|What would a new process need to improve transparency and participant care?|Specify source access, consent, corrections, budget, and review.
myths_vs_facts|The Camera Never Lies?|Which claim about objectivity fails when framing and editing are examined?|Show a bounded scene's choices and evidence.
documentary_stories|A Film's Making in Documents|What do the pitch, footage, notes, and cut reveal about one project?|Trace production decisions and participant rights.
creative_brief|A Verifiable Story Promise|What bounded question and evidence make a documentary worth making?|Define audience, stakes, access, participants, and what cannot be filmed.
materials_and_tools|What Each Source Can Show|Which claims can footage, archive, interview, and data support?|State provenance and limits for each material type.
process_breakdown|From Research to Release|Where are factual and ethical decisions made in one production?|Map pitch, consent, filming, edit, fact check, legal review, and correction.
composition_choice|Framing Changes Meaning|How does one shot choice alter a viewer's inference?|Compare alternate framing with source context and participant response.
collaborative_authorship|Whose Story Is Being Told?|How did participants, researchers, translators, and editors shape a film?|Inspect credits, agreements, drafts, and consent.
adaptation_across_media|One Story in Film and Audio|What changes when a documented account moves between formats?|Compare evidence visibility, voice, pacing, and disclosure.
audience_reception|What Viewers Took Away|Did viewers infer a claim the film did not establish?|Use audience research and examine the film's cues.
cultural_context|A Film in Its Community|How does local context alter meaning of a scene or image?|Use community review and avoid treating one voice as representative.
preservation_restoration|Restoring a Documentary Record|Which edits or repairs should be disclosed in a restored film?|Compare source elements, restoration log, and historical context.
rights_and_attribution|Permission for a Source|Who can authorize one image, recording, or testimony's use?|Check rights, consent, source credit, and jurisdiction.
style_comparison|Two Films, Same Event|How do different evidence and editing choices shape the account?|Compare source selection, chronology, and participant treatment.
creative_failure|A Cut That Did Not Work|Which production decision led to a factual or ethical problem?|Use version history and corrective action, not blame alone.
field_shot_design|A Shot's Evidentiary Role|What does one planned shot establish, and what might viewers infer?|Define claim, context, staging disclosure, and consent.
field_production_workflow|A Source-Safe Shoot|How does a team preserve source notes and participant agreements on location?|Map roles, records, storage, and review without exposing private data.
field_sound_choices|Sound and Truthfulness|How can music or sound design change perceived certainty?|Compare raw audio, edit, mix, and disclosure.
field_editing_rhythm|Pacing and Chronology|Where did pace compress time or change causal impression?|Audit cuts against source timeline and clarify transitions.
field_distribution_format|A Film Across Platforms|How do clips or short formats alter context and correction reach?|Compare full film, promotional cut, captions, and update path."""

SCIENCE = """history_origins|A Scientific Question Takes Shape|Which observation first made one bounded question testable?|Trace original measurement, proposed explanation, and later revisions.
famous_examples|A Landmark Result Revisited|What did one celebrated experiment or observation actually establish?|Read methods, uncertainty, controls, and subsequent confirmation.
hidden_stories|The People Behind the Data|Whose instrument, field, technical, or data work made a finding possible?|Use publications, lab records, and attributed accounts.
beginner_explainers|From Question to Test|What observation would distinguish two explanations of one phenomenon?|Define prediction, measurement, comparator, and uncertainty.
advanced_concepts|Model Assumptions Matter|Which assumption drives one scientific model's conclusion?|Vary inputs, compare observations, and state domain of validity.
mysteries_unsolved_cases|A Real Open Question|Which competing hypotheses remain consistent with current evidence?|Specify observed facts, missing measurements, and falsifiable differences.
technology_innovation|A Better Instrument|What new signal can one instrument measure, and at what limit?|Compare calibration, resolution, noise, and earlier methods.
people_personalities|A Scientist in a Collaboration|What did one researcher contribute to a discovery?|Use original papers, author roles, instruments, and collaborators.
major_events|A Result Forces Revision|How did a dated observation alter a scientific explanation?|Compare prior prediction, new data, response, and replication.
how_it_works|An Explanation as a Causal Chain|Which measured steps connect cause to observed effect?|Separate direct observation from modeled intermediates.
rise_fall|A Hypothesis Gains and Loses Support|Why did evidence favor and later weaken one theory?|Track experiments, alternative models, and uncertainty.
then_vs_now|Two Generations of Measurement|How did precision or scope change the answer to one question?|Compare units, sampling, instruments, and uncertainty.
future_developments|The Next Discriminating Test|Which observation could separate two live explanations?|Name measurable prediction and feasible instrument, not a promised breakthrough.
myths_vs_facts|A Science Headline Checked|Does a popular claim match the original result?|Compare study design, effect size, uncertainty, and applicability.
documentary_stories|A Finding Through Its Records|What do lab notes, data, publications, and corrections reveal?|Trace provenance and make gaps visible.
observation_to_explanation|From Signal to Claim|Which inference turns one observation into an explanation?|State calibration, alternative causes, and model assumptions.
measurement_method|What Was Actually Measured?|How did one study define and record its variable?|Inspect instrument, sampling, units, and validity.
scale_and_timespan|Changing Scale Changes the Question|Does a mechanism observed at one scale apply at another?|Compare spatial and time scales with evidence.
field_vs_lab|Lab Result in the Field|Which conditions differ between controlled and natural settings?|Compare selection, confounders, measurement, and replication.
natural_variation|Signal Against Background Variation|How large is the reported effect beside ordinary variation?|Show distribution, baseline, season, and measurement error.
mechanism_chain|A Mechanism with Missing Links|Which step in a proposed causal chain is directly supported?|Separate observed, inferred, and untested links.
extreme_case|What an Extreme Example Reveals|Does an unusual case test or merely illustrate a theory?|Check representativeness and boundary conditions.
classification_debate|Where a Category Breaks Down|Which observations challenge one scientific classification?|Compare definitions, borderline cases, and practical use.
interacting_systems|More Than One Cause|How do two processes interact in a measured outcome?|Use a bounded system and avoid single-cause storytelling.
data_gap|The Missing Measurement|Which data gap most limits one scientific claim?|Identify coverage, bias, missingness, and feasible remedy.
prediction_test|A Model's Risky Prediction|What did a model predict before new data were collected?|Compare preregistered or dated forecast with outcome and uncertainty.
human_impact|A Scientific Finding in Use|How did a measured result affect one policy or technology decision?|Separate evidence, value judgment, implementation, and effects.
field_experimental_setup|One Experiment's Controls|Which controls make a causal claim credible?|Inspect assignment, blinding where relevant, contamination, and protocol.
field_mathematical_model|A Model's Inputs and Outputs|Which equations or parameters matter for one result?|Explain assumptions, sensitivity, calibration, and validation.
field_measurement_error|Uncertainty Budget|Where did random and systematic error enter one measurement?|Read calibration and error analysis in the primary report.
field_scale_transition|From Small Test to Large System|What evidence supports scaling a lab result?|Check boundary conditions, field validation, and failure modes.
field_technology_application|A Finding Becomes a Tool|What additional engineering tests turned an insight into use?|Trace prototype, performance, safety, and independent evaluation."""

if __name__ == "__main__":
    revise_domain("005", "005_documentary_storytelling", DOCUMENTARY,
                  "Nonfiction story design, source provenance, participant consent, visual and sound choices, factual review, and correction across formats.",
                  "original footage and archives, production notes and version history, source and rights ledgers, consent records, published corrections, and attributed participant accounts",
                  "Distinguish filmed evidence from staging and inference; document consent and rights, protect vulnerable participants, disclose material reconstruction, and keep a correction path.")
    revise_domain("006", "006_science_big_questions", SCIENCE,
                  "Bounded scientific questions, testable predictions, measurement, uncertainty, replication, models, and real-world limits.",
                  "primary research papers and data, protocols, instrument calibration, independent replications, model documentation, and dated corrections",
                  "State the exact claim, scale, measurement, uncertainty, and competing explanation. Do not turn an open question into a solved one or generalize a result beyond its tested conditions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
