"""Editorial question review for space and ancient technology plans."""

from review_angle_plans import audit, revise_domain


SPACE = """history_origins|How a Cosmic Model Changed|Which observation changed an accepted account of one astronomical system?|Trace the original measurement, interpretation, and subsequent tests in a dated case.
famous_examples|A Landmark Space Discovery Revisited|What did one celebrated discovery actually establish at the time?|Compare the original data and claim with later confirmation and remaining limits.
hidden_stories|The Work Behind a Space Result|Whose observing, computing, or instrument work was omitted from one discovery narrative?|Use dated team records and attributed accounts without inventing motives.
beginner_explainers|Reading Light from Space|What can light from a distant object tell us, and what cannot it tell us alone?|Use one observation to separate measured brightness or spectrum from inferred properties.
advanced_concepts|Modeling an Unseen World|How do different assumptions change an estimate of one exoplanet property?|Explain the observations, host-star inputs, model dependence, and uncertainty.
mysteries_unsolved_cases|A Cosmic Signal with Competing Explanations|Which explanations for one unresolved observation remain viable?|Compare dated predictions and discriminating tests; do not imply that unexplained means supernatural.
technology_innovation|An Instrument Changes the View|Which new measurement became possible with a specific telescope or detector?|Compare resolution, sensitivity, wavelength coverage, and calibration before and after.
people_personalities|A Discovery as Teamwork|What did named researchers contribute to one astronomical finding?|Reconstruct roles from publications and records, including prior work and independent checks.
major_events|A Mission's Decisive Observation|What did one mission observe at a turning point, and how was the result checked?|Use mission logs, released data, instrument limits, and later analysis.
how_it_works|How a Transit Reveals a Planet|How can a repeated dip in starlight support an exoplanet claim?|Follow light-curve measurement, alternative causes, follow-up, and selection effects.
rise_fall|Why a Space Hypothesis Lost Favor|Which observations weakened one once-plausible astronomical hypothesis?|Compare its predictions with subsequent data without rewriting the historical uncertainty.
then_vs_now|One Object, Two Generations of Measurement|How did improved instruments change estimates for one astronomical object?|Use comparable measurements, definitions, and uncertainty intervals from both periods.
future_developments|The Next Space Measurement|Which planned observation could distinguish competing models?|State instrument requirements and conditional outcomes; date mission and launch claims.
myths_vs_facts|Checking a Space Headline|Does a popular claim about a planet, star, or galaxy match the underlying data?|Read the original result and distinguish detection, interpretation, and speculation.
documentary_stories|A Discovery Through Its Data Trail|How did one space finding move from raw signal to public announcement?|Build a dated record of calibration, review, correction, and communication.
observation_to_explanation|From Photons to Physical Claim|Which inferential steps connect one observed signal to its proposed source?|Identify foreground effects, calibration, model assumptions, and alternatives.
measurement_method|Measuring an Astronomical Quantity|How was one distance, mass, or temperature estimated?|Name instrument, units, calibration, model inputs, and error sources.
scale_and_timespan|Cosmic Distance and Lookback Time|How does observing distant light affect claims about when an event occurred?|Choose one object and distinguish observed light, inferred distance, and cosmic chronology.
field_vs_lab|Calibrating a Telescope for the Sky|Which laboratory calibration holds or fails under actual observing conditions?|Compare detector tests with sky background, pointing, and in-flight performance.
natural_variation|Separating Planet Signal from Stellar Activity|Can changes in a star imitate a proposed planet signal?|Compare variability, repeat observations, wavelength evidence, and error estimates.
mechanism_chain|How an Orbit Produces a Signal|Which physical steps connect orbital motion to a measured light or velocity pattern?|Trace geometry, gravity, detector response, and inference using one system.
extreme_case|A Planet at the Edge of the Sample|Does one unusual exoplanet expose a limit of a model or a selection bias?|Check confirmation, parameters, detectability, and comparison population.
classification_debate|Defining a Celestial Class|Which criteria place a disputed object in one astronomical class?|Compare official definitions, measured properties, and the consequence of each rule.
interacting_systems|Star, Planet, and Instrument Together|How do stellar behavior and observing design interact in one planetary measurement?|Use a bounded system and quantify confounding where data allow.
data_gap|The Unobserved Part of a Survey|Which objects might a space survey systematically miss?|Examine target selection, cadence, sensitivity, orientation, and missing observations.
prediction_test|A Model Meets a New Observation|What did a dated space model predict before follow-up data arrived?|Compare prediction and observation with stated uncertainty and revision history.
human_impact|Using Space Data on Earth|How was one astronomical or planetary measurement used in an education or technology decision?|Trace the documented use and distinguish practical outcome from promotional claims.
field_observation_window|When Can a Target Be Seen?|How does a mission's observation window constrain one inference?|Compare target visibility, cadence, missed events, and scheduling records.
field_instrument_limit|The Detector's Blind Spot|Which sensitivity or calibration limit matters most for one reported signal?|Read instrument documentation and the analysis uncertainty budget.
field_orbital_dynamics|Reconstructing an Orbit|What measurements constrain the orbit of one planet, moon, or spacecraft?|Use dated positional or velocity data and show parameter uncertainty.
field_mission_tradeoff|Choosing a Mission Design|Which science measurements were gained or lost in one mission tradeoff?|Compare official mission objectives, mass or time limits, and alternatives.
field_planetary_environment|Evidence for a Planetary Environment|What do observations support about one planet's atmosphere or surface?|Separate direct measurement from retrieval-model inference and unresolved alternatives."""


ANCIENT = """history_origins|Tracing an Ancient Technique|What is the earliest securely dated evidence for one making technique?|Compare archaeological context, dating method, and later examples without claiming a single inventor.
famous_examples|An Ancient Device in Context|What does one famous artifact reveal about the skills of its makers?|Inspect material, find context, analysis, and competing functional interpretations.
hidden_stories|Makers Behind the Monument|What evidence identifies the labor and specialist knowledge behind one ancient work?|Use workshop remains, marks, texts where available, and cautious attribution.
beginner_explainers|How Archaeologists Infer a Tool's Use|Which traces support an interpretation of an ancient object's function?|Explain context, wear, residues, comparison, and alternative uses.
advanced_concepts|Reconstructing a Production Sequence|Which steps in an ancient manufacturing process can be inferred from surviving evidence?|Compare unfinished pieces, tools, waste, material analysis, and experimental results.
mysteries_unsolved_cases|An Artifact with Several Plausible Uses|Which interpretations of a puzzling artifact fit the evidence?|Rank hypotheses by context and testable traces; absence of explanation is not proof of advanced lost technology.
technology_innovation|A Material Technique Spreads|How can a change in material processing be traced across sites?|Compare dated recipes, tool marks, sources, and local variation.
people_personalities|Attributing Ancient Ingenuity|Can one named individual be linked to a specific ancient technique?|Separate contemporary testimony, later legend, and material evidence.
major_events|When a Workshop Changed|What changed in production around one securely dated disruption?|Compare layers, raw material access, tools, and output before and after.
how_it_works|Reconstructing a Working Mechanism|How might one ancient mechanism have operated given its surviving parts?|Demonstrate a constrained model and identify missing components and assumptions.
rise_fall|Why a Technique Disappeared from View|Did one method end, move, or merely vanish from surviving records?|Compare dated evidence across regions and account for preservation bias.
then_vs_now|Ancient and Modern Making Compared|Which steps in one technique can be recreated with available ancient materials?|Keep tools and inputs historically plausible; label modern substitutions.
future_developments|A Test That Could Resolve a Dispute|Which feasible analysis could distinguish rival interpretations of an artifact?|Specify predicted traces, access requirements, and conservation constraints.
myths_vs_facts|Testing a Lost-Technology Claim|Does a popular claim about an ancient artifact follow from its archaeological context?|Trace the claim to evidence, check dates and provenance, and compare ordinary explanations.
documentary_stories|An Object's Evidence Trail|How did one artifact move from excavation to interpretation and display?|Follow field records, conservation, analysis, contested labels, and source gaps.
system_boundary|What Counts as the Ancient System?|Which surviving pieces and contextual features belong to one proposed device or workshop?|Define the site and assembly boundary before reconstructing function.
input_output_trace|Materials Into Artifact|What evidence connects raw inputs, labor, and finished output for one craft?|Track sources, waste, unfinished work, and product distribution.
design_tradeoff|Making Within Material Limits|Which material and tool constraints shaped one ancient design?|Compare plausible alternatives using actual finds and experimental results.
failure_mode|Wear and Breakage as Evidence|What can damage to one artifact reveal about its use or repair?|Distinguish ancient use-wear from burial, excavation, and conservation damage.
testing_limits|What a Replica Can Establish|Which claims does a reconstruction test, and which remain unproved?|Document substitutions, operator skill, measurement, and non-unique solutions.
standards_interoperability|Shared Measures and Fitting Parts|Is there evidence of repeatable dimensions or interchangeable components in one ancient production system?|Measure a defined sample and separate deliberate standardization from normal variation.
security_threat_model|Threats to the Evidence|How could looting, forgery, or disturbed context change the interpretation of one artifact?|Check provenance, chain of custody, scientific tests, and site records without revealing vulnerable locations.
maintenance_lifecycle|Evidence of Ancient Repair|How was one object maintained, patched, or reused during its working life?|Separate original manufacture from later repairs using stratigraphy and material analysis.
infrastructure_dependencies|The Network Behind a Craft|Which transport, fuel, water, or labor systems supported one ancient technology?|Map dated source and site evidence without assuming a centralized organizer.
accessibility_usability|Who Could Use the Technology?|What evidence shows who had access to one ancient tool or service?|Compare find locations, wear, texts where available, and social interpretations.
independent_replication|A Reconstruction Repeated|Can separate teams reproduce a proposed ancient process?|Compare methods, materials, outcomes, failed trials, and publication detail.
responsible_deployment|Explaining a Reconstruction Publicly|How should a museum present what is known and uncertain about a reconstructed device?|Compare display claims with primary evidence, community input, and conservation needs.
field_prototype_testing|Testing a Historically Plausible Replica|Which measured result supports or weakens one proposed use?|Prestate the test, record materials and substitutions, and compare with archaeological traces.
field_design_tolerance|How Precise Was the Making?|What range of dimensions appears in a defined group of ancient objects?|Use a measured sample, dating context, and measurement error before inferring intent.
field_manufacturing_method|Reading Workshop Traces|Which marks and waste reveal the order of making steps?|Compare microscopic traces with documented experimental replicas.
field_failure_investigation|Why Did This Object Break?|Can a fracture be linked to manufacture, use, burial, or recovery?|Inspect fracture surfaces and context with conservation expertise.
field_repair_path|An Object's Second Life|What repair sequence can be reconstructed from patches and altered surfaces?|Date and document each intervention; distinguish ancient adaptation from modern restoration."""


if __name__ == "__main__":
    revise_domain("012", "012_space_universe", SPACE,
                  "Astronomical observation, measurement, models, mission constraints, and uncertainty from nearby worlds to cosmic scales.",
                  "NASA and other observatory mission archives, calibrated data and instrument papers, primary research, dated model predictions, and independent follow-up observations",
                  "Distinguish observed signal, model-based inference, and speculation. State time, scale, detection bias, uncertainty, and alternatives; do not present an unconfirmed signal as discovery.")
    revise_domain("013", "013_ancient_technology_lost_knowledge", ANCIENT,
                  "Material evidence for ancient tools, craft, infrastructure, experimental reconstruction, provenance, and limits of interpretation.",
                  "excavation reports and context records, museum collections and conservation analyses, artifact measurements, dated texts where relevant, and published experimental archaeology",
                  "Ground interpretations in documented provenance and dated material evidence. Label replicas and modern substitutions, protect site and cultural heritage, and never treat an evidentiary gap as proof of a sensational lost technology.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
