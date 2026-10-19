"""Editorial question review for gaming lore and medical human science."""

from review_angle_plans import audit, revise_domain


GAMING = """history_origins|Where a Game World Began|How did one game's setting or lore evolve from its earliest documented concept?|Compare dated design notes, releases, and credited creator accounts.
famous_examples|A Lore Reveal That Worked|How does one widely discussed reveal change the player's interpretation of earlier clues?|Analyze the released game and version-specific evidence.
hidden_stories|Creators Behind the World|Which credited writers, artists, or community contributors shaped one game setting?|Trace documented roles and attribution without inventing intent.
beginner_explainers|Reading Game Lore|How do dialogue, environment, rules, and optional records convey a fictional world?|Map one bounded quest or level and distinguish canon from interpretation.
advanced_concepts|A Rule That Carries Story|How does one mechanic express a game's theme or world rule?|Compare player action, feedback, narrative consequence, and alternative readings.
mysteries_unsolved_cases|An Open Lore Question|Which interpretations of a deliberately ambiguous event fit the released evidence?|Separate in-game clues, developer statements, and fan theories by version.
technology_innovation|A Tool Changes Worldbuilding|Which technical choice altered how a game's story could be delivered?|Compare engine or platform limits, authored content, and player experience.
people_personalities|A Writer's Documented Choice|How did a named creator explain a character or setting decision?|Use credited interviews and compare with the finished work.
major_events|A Patch Changes the Story|What did one update change in the game's lore or player understanding?|Compare version notes, in-game text, and community response.
how_it_works|How Environmental Storytelling Works|Which clues let a player infer a past event without direct exposition?|Follow one location and test whether clues are discoverable.
rise_fall|A Story Arc That Lost Momentum|Why did a documented revision or cancellation change a game's narrative?|Use production records and released material, distinguishing evidence from fan speculation.
then_vs_now|A Game World Across Versions|How did one series reinterpret its lore between two releases?|Compare rules, characters, continuity, and stated creative decisions.
future_developments|An Announced Story Expansion|Which known decisions constrain a planned lore expansion?|Use dated official announcements and label unreleased details as uncertain.
myths_vs_facts|A Fan Theory Checked|Which parts of a popular theory are supported by the current game?|Cite exact versioned clues and identify contradictions or missing evidence.
documentary_stories|The Making of a Game World|How did one lore element move from concept art to release?|Build a dated account from drafts, credits, and interviews.
creative_brief|A Worldbuilding Promise|What must a player understand, feel, or choose in one lore arc?|Define audience, core rule, clue path, and narrative payoff.
materials_and_tools|Assets That Tell the Story|Which text, image, sound, and level assets convey one fictional history?|Inventory versioned assets and their production roles.
process_breakdown|From Narrative Beat to Quest|How does a story beat become objectives, dialogue, level state, and testing?|Trace one documented sequence from design to release.
composition_choice|Where the Player Looks|How do camera, lighting, sound, and layout guide attention to a clue?|Analyze a playable scene, including optional routes.
collaborative_authorship|Who Writes the World?|How do narrative, art, systems, and localization teams shape one lore element?|Use credits and production records, noting revisions across teams.
adaptation_across_media|A Game Story in Another Medium|What changes when interactive lore becomes a comic, film, or book?|Compare agency, pacing, canon claims, and credited adaptation choices.
audience_reception|How Players Read a Clue|Did a defined player group understand one intended revelation?|Use consented playtests or attributed response, avoiding universal claims.
cultural_context|Borrowed Motifs in a Game World|How does a game use imagery or stories from a living culture?|Trace sources, consultation, community feedback, and possible stereotypes.
preservation_restoration|Preserving an Online Story|Which lore becomes inaccessible when servers, patches, or licenses change?|Compare archived versions and document gaps in playable history.
rights_and_attribution|Ownership of Game Lore|How are fan contributions, mods, and official content credited and licensed?|Read current terms for a named project and jurisdiction.
style_comparison|Two Ways to Reveal Lore|How do dialogue and environmental clues change player interpretation of the same event?|Compare discoverability, pacing, and ambiguity in named scenes.
creative_failure|When a Lore Clue Misfires|What documented player confusion prompted a narrative revision?|Compare earlier build, feedback, and shipped change.
field_rules_design|Rules of the Fictional World|Do the game's mechanics and story describe the same constraints?|Test a versioned level for exceptions and intended explanation.
field_player_strategy|Strategy Reveals Story|How does a player's optimal strategy reinforce or contradict a character's stated goal?|Compare incentives, available choices, and narrative consequences.
field_difficulty_curve|Challenge and Narrative Pace|Where does difficulty help or interrupt one story beat?|Examine encounter sequence, retries, accessibility options, and playtest evidence.
field_community_norms|Fan Canon and Official Canon|How does a community convention differ from released lore?|Attribute fan interpretation and official statements without ranking participation as illegitimate.
field_accessibility_design|Can Players Reach the Story?|Which audio, text, control, or timing barriers keep a defined group from narrative content?|Test available options and describe remaining gaps."""


MEDICAL = """history_origins|How a Medical Explanation Changed|Which observation led researchers to revise one account of human disease?|Trace dated studies, diagnostic definitions, and later tests.
famous_examples|A Landmark Medical Study Revisited|What did one celebrated study establish for its actual participants?|Compare design, outcome, follow-up, limitations, and later replication.
hidden_stories|People Missing from the Evidence|Whose bodies or experiences were excluded from one medical knowledge base?|Inspect recruitment, historical records, and affected voices with care.
beginner_explainers|From Symptom to Testable Question|How do researchers turn one clinical observation into a study question?|Define population, comparator, outcome, and uncertainty without diagnosing viewers.
advanced_concepts|Biomarker Versus Patient Outcome|When does a laboratory measure predict a result that matters to patients?|Compare validation studies, thresholds, false results, and clinical outcomes.
mysteries_unsolved_cases|An Unresolved Medical Mechanism|Which competing explanations of a condition remain plausible?|Map human evidence, model evidence, and decisive future tests.
technology_innovation|A Diagnostic Tool Assessed|Does a new test improve decisions or outcomes for a defined group?|Compare accuracy, access, harms, costs, and clinical follow-up.
people_personalities|The Team Behind a Discovery|Who contributed to one medical finding and how was credit assigned?|Use publications, records, and ethical context.
major_events|A Medical Recommendation Changes|What new evidence prompted a dated guideline revision?|Compare prior and new evidence, target population, and remaining disagreement.
how_it_works|From Study to Clinical Guidance|How does one result move through replication, evidence review, and guideline writing?|Trace actual documents and decision thresholds.
rise_fall|A Treatment Hypothesis Reconsidered|Why did early promise fail or narrow in later testing?|Compare study designs, outcomes, adverse events, and populations.
then_vs_now|A Condition Across Two Eras|How did diagnosis or treatment of one condition change?|Compare definitions, outcomes, access, and reporting practices.
future_developments|The Next Useful Medical Test|What study could close a specific evidence gap?|Name population, comparator, outcomes, follow-up, safety, and ethics.
myths_vs_facts|Checking a Medical Headline|Does a public claim reflect the original study?|Report absolute effects, uncertainty, study type, and applicability.
documentary_stories|A Finding Through Its Records|How did one medical claim progress from observation to public use?|Build a dated chain of study, review, correction, and patient impact.
observation_to_explanation|From Association to Cause|What evidence connects an observed health pattern to a proposed cause?|Identify confounding, bias, mechanism, and stronger tests.
measurement_method|How an Outcome Was Measured|Did one study measure what patients or clinicians need to know?|Inspect instrument, units, timing, validation, and missing data.
scale_and_timespan|Short Result, Long Claim|Can a short study support a long-term health conclusion?|Compare follow-up, latency, attrition, and event rates.
field_vs_lab|From Model to Human Evidence|Does a cellular or animal finding apply to patients?|Compare dose, biology, endpoints, and human confirmation.
natural_variation|A Result Against Baseline|How large is a measured change beside ordinary variation?|Show distributions, measurement error, and meaningful thresholds.
mechanism_chain|The Missing Step in a Mechanism|Which link from molecular process to patient outcome is directly tested?|Separate observed steps from plausible but unverified ones.
extreme_case|What a Rare Case Can Teach|Does an unusual patient reveal a mechanism or merely suggest one?|Protect privacy and compare with broader evidence.
classification_debate|Where a Diagnosis Boundary Lies|How do changing criteria alter who is counted as having a condition?|Compare definitions, false positives, access effects, and dates.
interacting_systems|Several Causes, One Outcome|How do biology, environment, and care access interact in one condition?|Use a bounded population and avoid single-cause explanations.
data_gap|Who Is Missing from a Medical Dataset?|Which exclusions or missing outcomes limit one conclusion?|Inspect enrollment, subgroup sizes, follow-up, and feasibility of better data.
prediction_test|A Model's Clinical Prediction|How well did one dated model predict outcomes in an independent group?|Check calibration, discrimination, missingness, and practical consequences.
human_impact|Evidence Changes Care|How did one research result affect patients or services?|Compare guideline adoption, measured outcomes, and unequal access.
field_species_variation|Species Differences in a Medical Model|Which biological differences limit translating an animal result to humans?|Name species, pathway, dose, and human validation evidence.
field_ecological_role|A Microbe in Its Human Environment|How does one organism's role differ across body sites or populations?|Compare sequencing, culture, function, and confounders without declaring universal benefit or harm.
field_experimental_model|A Model of Human Disease|What can one cell, organoid, or animal model reproduce about a condition?|List tested features, failures, and ethical limits.
field_evolutionary_history|Evolution and Disease Susceptibility|Can an evolutionary explanation of one human trait be tested?|Compare genomic, population, and clinical evidence while avoiding adaptation stories without tests.
field_conservation_status|Safeguarding Human Research Samples|How are human specimens or datasets preserved and governed for future study?|Examine consent, storage, access, privacy, and representativeness."""


if __name__ == "__main__":
    revise_domain("025", "025_gaming_stories_lore", GAMING,
                  "Game lore and interactive narrative through versioned evidence, player agency, design craft, community interpretation, and access.",
                  "released versioned games and patch notes, design documents and credits, creator interviews, consented playtests, accessibility testing, and documented fan interpretations",
                  "Distinguish released canon, creator comment, and fan theory by version. Credit creators and communities, respect rights, and test whether accessibility options expose the story.")
    revise_domain("026", "026_medical_human_science", MEDICAL,
                  "Human medical research from observation and mechanism to clinical studies, guidance, patient outcomes, and ethical limits.",
                  "original human studies and protocols, trial registries, study datasets where appropriate, clinical guidelines, laboratory and animal studies, ethics records, and patient-reported outcomes",
                  "Define population, outcome, comparator, and date. Distinguish association, model result, clinical effect, and personal advice; protect patient privacy and check current guidance and harms.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
