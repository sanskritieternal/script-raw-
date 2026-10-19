"""Editorial questions for the niche labelled primitive technology."""

from review_angle_plans import audit, revise_domain


TECHNOLOGY = """history_origins|Tracing a Tool's Earlier Forms|What evidence dates one material technique in a named region?|Compare archaeological context, dated objects, and later testimony.
famous_examples|A Widely Shared Build Reconsidered|What does one popular hand-build demonstrate and leave unknown?|Check material origin, editing, assistance, repeatability, and stated method.
hidden_stories|The Knowledge Behind a Simple Tool|Whose inherited expertise makes a seemingly basic technique possible?|Attribute named communities and practitioners with consent.
beginner_explainers|What Can a Build Demonstrate?|How is a controlled recreation different from evidence of historical use?|Define source model, materials, outcome, and uncertainty.
advanced_concepts|Testing a Historical Reconstruction|Which observations could test one proposed older manufacturing process?|Use artifact traces, material properties, documented trials, and alternatives.
mysteries_unsolved_cases|An Artifact with an Uncertain Method|Which competing explanations fit one object's manufacture?|Compare trace evidence, context, experiments, and unresolved gaps.
technology_innovation|An Old Material, a New Application|How does one adapted material process perform for a modern need?|Compare performance, energy, availability, maintenance, and context.
people_personalities|The Maker's Research Choices|How did one maker choose sources and revise a reconstruction?|Follow attributed notes, consultation, trials, and failed attempts.
major_events|A Discovery That Changed a Reconstruction|How did new evidence alter one accepted interpretation?|Compare original claim, new find, dating, and expert response.
how_it_works|Why a Material Holds Together|Which physical properties explain one construction technique?|Use qualified tests and diagrams without a hazardous build tutorial.
rise_fall|A Technique's Changing Use|Why did one process become less common or return?|Check materials, labor, costs, laws, and practitioner priorities.
then_vs_now|A Historical Method in a Modern Setting|Which parts of one recreated process match documented evidence?|Separate period evidence, modern substitutions, and camera choices.
future_developments|A Community-Led Skills Project|Could one project support knowledge transfer on community terms?|Check consent, teaching capacity, materials, ownership, and benefits.
myths_vs_facts|The Myth of Technology Stages|Does a linear primitive-to-advanced story fit one material tradition?|Compare local designs, changing uses, and the limits of that label.
documentary_stories|A Reconstruction from Evidence to Result|Which decisions and setbacks shaped one documented experiment?|Show source trail, controls, assistance, failures, and limitations.
creative_brief|Defining a Build Documentary|What can one filmed demonstration responsibly claim?|State purpose, evidence level, crew contribution, and safety boundary.
materials_and_tools|Where the Materials Came From|How do sourcing and preparation affect one result?|Trace provenance, permissions, material properties, and substitutions.
process_breakdown|A Process Without a False Shortcut|Which stages determine success in one historical technique?|Document observable stages and expert interpretation without dangerous instructions.
composition_choice|What the Camera Makes Invisible|How do filming and editing change viewers' sense of time and effort?|Compare raw work log, retakes, assistance, and final sequence.
collaborative_authorship|Who Helped Make This Build?|Which experts, assistants, and tradition holders shaped a demonstration?|Record consent, work, pay, credit, and decision authority.
adaptation_across_media|From Artifact to Online Demonstration|How does a video interpretation differ from a museum display?|Compare evidence, narrative compression, labels, and audience assumptions.
audience_reception|What Viewers Think Was Proved|Do viewers distinguish experiment from historical certainty?|Review comments or interviews with sampling limits and consent.
cultural_context|Whose Technology Is Called Primitive?|How does the niche label distort a named community's knowledge?|Use local terminology and practitioner perspectives in the episode title.
preservation_restoration|A Recreated Object and an Original|What can a replica teach without being mistaken for an artifact?|Label materials, methods, changes, and collection provenance.
rights_and_attribution|Who May Share the Technique?|What permissions govern one documented community-held process?|Check practitioner consent, customary restrictions, intellectual property, and credit.
style_comparison|Two Solutions to One Material Problem|How do different designs answer distinct environmental needs?|Compare documented contexts without ranking cultures on a progress ladder.
creative_failure|A Failed Trial as Evidence|What does one failed reproduction reveal about assumptions?|Record conditions, deviations, repeat attempts, and alternative explanations.
field_material_selection|Selecting a Material for an Experiment|Which material properties are necessary to test one hypothesis?|Use lawful sourcing, qualified assessment, and documented substitutions.
field_tool_control|What Tool Marks Can Reveal|Can a replica tool produce traces comparable to an artifact?|Compare microscopy, material, use wear, controls, and ambiguity.
field_pattern_design|Why This Structure Has Its Form|Which functional and cultural choices shaped one pattern?|Separate measured performance from interpreted meaning and living practice.
field_repairability|A Tool Through Its Working Life|How was one object maintained, repaired, or reused?|Use wear evidence, records, practitioner knowledge, and uncertainty.
field_craft_lineage|From Practitioner to Student|How is one material skill passed on today?|Follow consented instruction, adaptations, access, and community priorities.
"""


if __name__ == "__main__":
    revise_domain("142", "142_primitive_technology", TECHNOLOGY,
                  "Material technologies, historical reconstruction, and present-day makers examined through evidence, experiments, attribution, and cultural context; the registry label is a search alias, not an assessment of cultures.",
                  "dated artifacts and archaeological context, documented experiments and material tests, transparent production logs, and consented practitioner and community accounts",
                  "Avoid a primitive-to-advanced hierarchy and claims that one reconstruction proves historical use. Attribute community knowledge and honor restrictions; keep hazardous fabrication at documentary level and verify site access and material collection rules.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
