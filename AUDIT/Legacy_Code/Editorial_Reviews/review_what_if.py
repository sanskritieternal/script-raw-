"""Editorial questions for what-if and alternative-reality stories."""

from review_angle_plans import audit, revise_domain


WHAT_IF = """history_origins|The Turning Point Behind a What-If|Which real decision anchors one counterfactual?|Establish date, available alternatives, actors, and evidence.
famous_examples|A Famous Alternate History Audited|Does one scenario preserve the constraints of its starting era?|Check technology, institutions, geography, resources, and chronology.
hidden_stories|Who Vanishes in the Alternate World?|Which affected groups disappear from a single-hero what-if?|Map documented stakeholders and plausible choices.
beginner_explainers|How a Counterfactual Works|What changes at the branch point and what stays fixed initially?|State one divergence, baseline history, and uncertain consequences.
advanced_concepts|From Divergence to Consequence|How strong is each link in one counterfactual chain?|Separate documented mechanism, analogy, model, and invention.
mysteries_unsolved_cases|A Close Historical Choice|Were two outcomes genuinely possible at the time?|Use contemporaneous plans, constraints, votes, and uncertainty.
technology_innovation|A Technology Arrives Earlier|What dependencies would an earlier invention have needed?|Check materials, skill, infrastructure, demand, and adoption.
people_personalities|One Person Makes Another Choice|How much could one individual plausibly change an outcome?|Compare institutional constraints and other actors' choices.
major_events|An Event That Did Not Happen|Which later effects depended on one actual event?|Trace multiple causal paths and avoid a deterministic alternative.
how_it_works|Building a Bounded Alternate Timeline|How can a scenario remain coherent after one changed premise?|Track chronology, resources, feedback, actors, and uncertainty.
rise_fall|A Power That Might Have Lasted|What would have been required to sustain one historical institution?|Test finance, legitimacy, rivals, ecology, and internal conflict.
then_vs_now|Actual History Versus a Hypothetical Path|Which claims belong to evidence and which to imagination?|Label the branch and every inferred step for viewers.
future_developments|What a What-If Teaches Planning|Can one alternative illuminate a current decision without forecasting it?|Extract mechanisms while naming changed context and limits.
myths_vs_facts|An Inevitable Outcome?|Does evidence support the claim that one historical outcome had to happen?|Examine feasible alternatives and constraints at the time.
documentary_stories|Following One Fork in History|How do people, institutions, and resources respond after one change?|Tell a bounded scenario with source notes and explicit fiction labels.
assumption_inventory|The Scenario's Hidden Premises|Which assumptions beyond the first change determine its ending?|List political, material, social, and environmental dependencies.
readiness_check|Could the Alternate Tool Exist?|Was one imagined technology technically and institutionally ready?|Compare period materials, methods, skills, and production capacity.
physical_limits|What the Alternate World Can Supply|Do transport, energy, food, and materials support one proposed outcome?|Use period-compatible estimates and ranges.
governance_choice|Who Would Decide Next?|Which institutions and interests could accept or resist the change?|Use documented rules and plausible incentives.
unequal_futures|Different Lives in the Alternate Path|Who might benefit or suffer under one changed decision?|Follow several groups and avoid claiming certainty for any.
scenario_pair|Two Plausible Branches|How do two coherent responses follow the same divergence?|Hold starting facts fixed and state distinct assumptions.
failure_to_launch|Why an Alternate Plan Might Fail|Which bottleneck could prevent a proposed path?|Test implementation, opposition, resources, and timing.
unintended_effect|A Second-Order Consequence|What other outcomes might change when one mechanism shifts?|Trace plausible feedback without an unlimited butterfly-effect claim.
social_adaptation|People React to the New Rule|How could households and organizations adapt?|Ground responses in documented behavior and comparable settings.
ethical_boundary|Using Real Suffering in a What-If|How can the story avoid trivializing victims or erasing agency?|Review framing with affected communities and label invention.
signal_vs_hype|A Plausible Fork or Fantasy?|Which part of a popular scenario lacks evidence or capacity?|Check baseline records, causal steps, and physical constraints.
reversible_steps|An Alternative Decision with Options|Could actors have changed course later?|Identify decision points, sunk costs, institutions, and uncertainty.
field_world_rule|The Rules of the Alternate World|What stays consistent after the single divergence?|Document chronology, demography, technology, and institutions.
field_plausibility_boundary|Where Evidence Runs Out|At which step does a scenario become mostly imaginative?|Tag every major claim by evidence type and confidence.
field_point_of_view|Whose Alternate World Is This?|How would different groups narrate the same changed event?|Use real historical perspectives without impersonating undocumented thoughts.
field_ethical_consequence|A Moral Choice in the Scenario|What new obligations or harms follow one proposed change?|Separate ethical analysis from claims about what would have happened.
field_adaptation_choice|Actors Change the Trajectory|Which plausible responses could undo or amplify the first divergence?|Test alternative strategies rather than fixing everyone else in place.
"""


if __name__ == "__main__":
    revise_domain("167", "167_what_if_alternative_reality", WHAT_IF,
                  "What-if and alternative-reality stories as bounded counterfactual reasoning with a documented branch point, plausible constraints, multiple actors, and clearly labeled invention.",
                  "contemporaneous records of the real event and feasible alternatives, period resource and institutional data, relevant causal scholarship, and attributed perspectives from affected groups",
                  "Name the real branch point and time horizon. Keep established history visually and verbally distinct from speculation; avoid deterministic chains, invented private thoughts, and trivialization of suffering.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
