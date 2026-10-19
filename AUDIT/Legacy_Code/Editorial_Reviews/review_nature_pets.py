"""Editorial questions for nature documentaries and pets."""

from review_angle_plans import audit, revise_domain


NATURE = """history_origins|How a Nature Film Was Made|Which scientific and camera methods shaped one early nature documentary?|Compare production records, original footage, and contemporaneous research.
famous_examples|A Celebrated Wildlife Sequence Reexamined|What does one famous sequence actually show about the animals?|Check filming location and date, editing, species identity, and independent research.
hidden_stories|Field Teams Behind the Footage|Whose local guidance, camera, sound, or research work is missing from the credits?|Use production records and attributed contributor accounts.
beginner_explainers|What a Wildlife Shot Can Show|How do observation, editing, and narration turn footage into a claim?|Use one sequence to separate visible behavior from inferred motive.
advanced_concepts|Representativeness in Wildlife Film|Can one filmed event support a claim about an entire species?|Compare scene selection with field-study samples and natural variation.
mysteries_unsolved_cases|An Unidentified Animal Behavior|Which explanations for a filmed behavior remain plausible?|Check raw footage, context, expert disagreement, and repeat observations.
technology_innovation|A Camera Changes the View|What did one filming tool reveal and what bias did it introduce?|Compare technical limits, disturbance, sample coverage, and independent observations.
people_personalities|A Filmmaker's Editorial Choice|Why did a named producer use one scene to tell a wider story?|Use interviews, scripts, rushes where available, and scientific response.
major_events|A Film Changes a Conservation Debate|Did one release alter attention, policy, or support for a species?|Compare dated audience and policy evidence without assuming causation.
how_it_works|From Field Observation to Finished Scene|How was one wildlife sequence filmed, logged, selected, edited, and narrated?|Follow production evidence and disclose captive or staged material.
rise_fall|A Documentary Method's Lifecycle|Why did one filming approach become common or fall out of use?|Compare cost, welfare, scientific value, and audience expectations.
then_vs_now|One Habitat Filmed Across Eras|How did the depiction and measured condition of a place change?|Compare camera methods, season, location, and ecological data.
future_developments|A New Nature-Film Method|What evidence would show that a proposed technique improves accuracy or welfare?|Define disturbance, transparency, coverage, and viewer understanding.
myths_vs_facts|A Wildlife Film Claim Checked|Does a memorable narration line match species-level research?|Trace the original scene, sample, study methods, and exceptions.
documentary_stories|One Shoot From Plan to Broadcast|How did a team document a species and decide what viewers saw?|Build a dated account from permits, field logs, edits, and scientific review.
observation_to_explanation|What Can the Camera Infer?|Which explanation of a filmed action is supported beyond the image?|Compare behavior study, ecological context, and alternative interpretations.
measurement_method|Counting What Was Filmed|How did camera placement and recording time affect observed behavior?|Specify effort, detection probability, selection, and disturbance.
scale_and_timespan|One Moment or a Life Cycle?|Does an episode represent days, seasons, or years accurately?|Compare shot dates, biological timing, narration, and editing.
field_vs_lab|Captive Footage and Wild Behavior|When does controlled footage illustrate rather than document wild behavior?|Disclose setting and compare with field evidence.
natural_variation|Not Every Animal Acts Alike|How much variation did the final cut omit?|Check raw logs and field studies by age, sex, season, and location.
mechanism_chain|From Behavior to Ecological Claim|What evidence connects a filmed act to a population-level effect?|Trace mechanism, repeated measures, and alternative causes.
extreme_case|An Exceptional Wildlife Scene|Why was one rare event selected, and how rare is it?|Compare film selection with field frequency and detection limits.
classification_debate|Which Species Is On Screen?|How does identification or taxonomic revision alter the claim?|Use validated identification, locality, and current taxonomy.
interacting_systems|A Scene Within Its Ecosystem|Which other species and habitat conditions shape the filmed event?|Pair footage with local ecological data, not a single predator-prey narrative.
data_gap|What the Crew Could Not Film|Which seasons, habitats, or behaviors are absent from one production?|Audit access, permits, equipment, and unfilmed observations.
prediction_test|Can a Filmed Claim Be Tested?|What field observation would confirm or challenge a narration claim?|Set species, outcome, sampling, and independent replication.
human_impact|People Near the Filmed Habitat|How did production and conservation affect local residents?|Use permits, spending, access, and attributed community voices.
field_species_variation|Two Populations on Film|How do two filmed populations differ under equivalent measures?|Match season, habitat, camera effort, and species identity.
field_ecological_role|A Filmed Animal's Role|Does the footage support a claimed ecological function?|Compare field data on interaction and outcome with scene selection.
field_experimental_model|Testing a Wildlife-Film Technique|Could a non-invasive comparison measure camera disturbance?|Specify ethical controls, permits, behavior outcomes, and limitations.
field_evolutionary_history|An Evolution Story on Screen|Which fossil, genetic, and comparative evidence supports narration about a trait?|Separate historical inference from a present-day visual illustration.
field_conservation_status|A Status Claim in a Film|Was the species' conservation status accurate for the film's date and place?|Check assessment date, geography, criteria, and subsequent changes."""


PETS = """history_origins|How an Animal Became a Companion|Which documented social and breeding changes shaped one pet relationship?|Use archaeological, genetic, historical, and household evidence with uncertainty.
famous_examples|A Popular Breed Reexamined|What do health and behavior data show beyond a breed's reputation?|Compare defined populations, selection bias, welfare, and individual variation.
hidden_stories|Care Work Behind Pet Ownership|Who provides daily feeding, cleaning, training, and veterinary support?|Use household time and cost records and attributed caregiver accounts.
beginner_explainers|Matching an Animal's Needs to a Home|What housing, social, activity, and health needs does one species have?|Use veterinary guidance for a defined life stage without individual diagnosis.
advanced_concepts|Welfare Beyond Basic Survival|How can physical health, behavior, and choice be evaluated together?|Compare veterinary and behavior measures for one pet context.
mysteries_unsolved_cases|A Behavior With Multiple Causes|Which medical, environmental, or learning factors might explain a pet behavior?|Review veterinary evidence; avoid diagnosing an individual animal remotely.
technology_innovation|A Pet Product Under Test|Does one feeder, tracker, or enrichment tool improve a measured outcome?|Compare independent trials, welfare, privacy, cost, and failure modes.
people_personalities|A Welfare Advocate's Contribution|What changed after one named researcher or practitioner published a finding?|Trace original study, critique, guidance, and implementation.
major_events|A Pet Policy Changes|What changed for animals and owners after one dated rule or shelter practice?|Compare intake, outcomes, costs, and local context.
how_it_works|A Pet's Daily Care System|How do housing, food, social interaction, activity, and veterinary care interact?|Map species-specific needs and owner constraints without treatment instructions.
rise_fall|A Breed or Pet Trend|Why did one type of pet gain or lose popularity?|Compare media, supply, welfare concerns, costs, and regulations.
then_vs_now|Pet Care Across Two Periods|How did one species' housing, medicine, and welfare expectations change?|Compare dated guidance and measured outcomes, not nostalgia.
future_developments|A Proposed Welfare Improvement|What evidence would show that one new shelter or ownership practice helps?|Define animal outcome, follow-up, owner burden, and comparison.
myths_vs_facts|A Pet-Care Claim Checked|Does a viral food, training, or breed claim fit current veterinary evidence?|State species, age, population, measured outcomes, and uncertainty.
documentary_stories|One Animal's Care Journey|What can a consented case reveal about adoption, care, and follow-up?|Use records and voices, protecting owner privacy and avoiding generalization.
observation_to_explanation|What a Pet Behavior Means|Which observations support one interpretation of a pet's behavior?|Compare context, body language research, medical alternatives, and observer bias.
measurement_method|Measuring Pet Welfare|Which health and behavior indicators fit one species and setting?|Define validated measures, timing, observer training, and welfare safeguards.
scale_and_timespan|A Week or a Lifespan?|Does a short pet-product or training study predict durable benefit?|Compare follow-up duration, life stage, and changing environment.
field_vs_lab|Shelter Findings at Home|Which findings from one controlled setting transfer to households?|Compare stress, population, environment, and care routines.
natural_variation|Not All Pets Behave Alike|How much variation exists within one breed or species?|Use representative samples and avoid stereotypes about individuals.
mechanism_chain|Why a Care Change Might Help|Which biological or behavioral steps could explain a measured welfare outcome?|Link mechanism to clinical or behavior evidence, not plausible story alone.
extreme_case|A High-Needs Animal|What does one severe case teach and what is not generalizable?|Use qualified clinical evidence and protect the animal and owner.
classification_debate|Breed Labels and Evidence|How reliably does a label describe ancestry or expected behavior?|Compare identification method, genetic data, and individual variation.
interacting_systems|Pets, People, and Home|How do space, schedules, other animals, and human needs shape welfare?|Use household context and veterinary assessment where relevant.
data_gap|What Pet Studies Miss|Which animals, owners, or outcomes are absent from a care study?|Audit recruitment, attrition, follow-up, and adverse effects.
prediction_test|Testing a Pet-Welfare Claim|What ethical study could evaluate one care intervention?|Set qualified oversight, comparison, outcomes, and stop criteria.
human_impact|Who Can Afford Good Care?|How do veterinary access, housing rules, and work schedules shape ownership?|Use local costs and services without blaming constrained owners.
field_species_variation|Care Needs Across Pet Species|How do two companion species differ in housing and social needs?|Compare authoritative species-specific welfare evidence.
field_ecological_role|Pets and Nearby Wildlife|How does one ownership pattern affect local wild animals?|Use local field evidence and humane options, avoiding unsourced blame.
field_experimental_model|A Safe Enrichment Evaluation|How can a team test whether one enrichment change helps?|Use veterinary or welfare oversight, baseline, behavior measures, and animal choice.
field_evolutionary_history|Domestication and Modern Traits|Which evidence links past selection to a present companion-animal trait?|Compare genetics, archaeology, breeding history, and alternative explanations.
field_conservation_status|A Wild-Animal Pet Claim|What conservation and legal issues arise for one species kept as a pet?|Check current status, sourcing, welfare, and local law; do not advise wild capture."""


if __name__ == "__main__":
    revise_domain("067", "067_nature_documentary", NATURE,
                  "Nature documentary through field observation, filming and editing choices, scientific inference, animal welfare, conservation, and local communities.",
                  "dated production logs and source footage where available, location and permit records, original field research and population methods, current taxonomy and conservation assessments, and attributed crew and community accounts",
                  "Name species, population, filming date, and setting. Disclose captive, staged, or composite scenes; distinguish footage from inference; avoid disturbance and vulnerable-location details.")
    revise_domain("068", "068_pets", PETS,
                  "Pets through species-specific welfare, household care, veterinary evidence, behavior, access, ownership cost, and animal-human impacts.",
                  "current veterinary and welfare guidance, original clinical and behavior studies, shelter and household outcome data, product tests, and consented owner and caregiver accounts",
                  "Name species, life stage, population, jurisdiction, and date. Do not diagnose or prescribe for an individual animal; verify current veterinary and local legal guidance and protect owner privacy.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
