"""Editorial question designs for niche 197, Marine Mammals."""

from review_angle_plans import audit, revise_domain


MARINE_MAMMALS = """history_origins|How a Marine Mammal Stock Was Defined|Which evidence established the boundary of one managed stock?|Compare distribution, genetics, movement, breeding, and assessment history.
famous_examples|A Celebrated Recovery Rechecked|What does one marine mammal recovery case actually demonstrate?|Specify stock, baseline, protections, later counts, and remaining threats.
hidden_stories|The People Behind an Ocean Survey|Whose work produces a marine mammal population estimate?|Trace vessel crew, aerial observers, Indigenous knowledge holders, analysts, and reviewers.
beginner_explainers|Species Versus Stock|Why can one marine mammal species contain distinct managed populations?|Explain geography, breeding, intermixing, and jurisdiction with a named case.
advanced_concepts|Estimating Abundance at Sea|How do researchers estimate a stock they cannot fully observe?|Examine survey area, detection, movement, model, and uncertainty.
mysteries_unsolved_cases|An Unexplained Stranding Pattern|Which evidence could explain a cluster of strandings?|Separate reported events from causes; test disease, prey, noise, injury, and detection.
technology_innovation|Acoustic Monitoring at Sea|Does one listening method improve detection of a named species?|Compare call rates, silent animals, noise, coverage, and validation.
people_personalities|A Protection Decision|How did one named scientist, advocate, or manager change policy?|Use dated evidence, public debate, adopted measures, and outcomes.
major_events|A Vessel Strike Response|What changed after a documented marine mammal injury event?|Trace investigation, vessel measures, compliance, and subsequent evidence.
how_it_works|How Stock Assessments Are Built|Which data and judgments appear in one official stock assessment?|Track range, abundance, trend, human-caused mortality, and review.
rise_fall|A Stock's Measured Trajectory|What evidence supports a rise or decline in one stock?|Compare methods, survey coverage, time series, births, deaths, and uncertainty.
then_vs_now|A Marine Mammal Stock Across Assessments|What changed between two assessment cycles?|Match stock definition, data years, estimation method, threats, and conclusions.
future_developments|Scenarios for a Marine Mammal Stock|Which plausible changes could alter one stock's outlook?|State prey, ocean warming, traffic, fisheries, policy, and model assumptions.
myths_vs_facts|Does Seeing More Mean More Animals?|Can increased sightings establish population growth?|Check search effort, distribution shift, reporting, and independent surveys.
documentary_stories|One Animal's Tracked Journey|What does one documented track show and conceal?|Use authorized tracking data; distinguish individual behavior from stock pattern.
observation_to_explanation|From Sightings to a Claim|What can a group of vessel sightings establish?|Compare identification, effort, duplicate sightings, and survey design.
measurement_method|Counting Animals at Sea|How do aerial or shipboard surveys estimate abundance?|Explain transects, detection probability, coverage, and uncertainty interval.
scale_and_timespan|A Local Aggregation Versus a Stock|At what scale is a marine mammal claim valid?|Define season, habitat, stock boundary, and survey years.
field_vs_lab|Sound Exposure in Context|Does a controlled sound-response finding predict field behavior?|Compare dose, species, context, baseline, and ethical constraints.
natural_variation|Why Animals Shift Location|How much change in sightings reflects natural movement?|Use longer series, prey distribution, season, and observation effort.
mechanism_chain|From Fishing Gear to Population Effect|What evidence links an interaction to serious injury or stock outcome?|Trace exposure, incident verification, mortality estimate, and population model.
extreme_case|An Exceptional Dive or Migration|How was a record marine mammal behavior measured?|Check device, calibration, species ID, individual, and independent records.
classification_debate|Where One Stock Ends|Why do assessments disagree over a population boundary?|Compare genetics, movement, breeding evidence, and management need.
interacting_systems|Prey, Ocean, and Mammals|How do ocean conditions and prey jointly affect a named stock?|Separate observed diet, prey trend, movement, and demographic response.
data_gap|The Sea We Did Not Survey|Which missing areas or seasons weaken an abundance estimate?|Map survey coverage, detectability, access, and model sensitivity.
prediction_test|Did a Recovery Projection Hold?|How did one stock forecast compare with later estimates?|Match model version, assumptions, survey methods, dates, and uncertainty.
human_impact|Shared Waters, Unequal Costs|How do conservation rules affect fishers, vessels, coastal communities, and animals?|Compare verified risks, economic distribution, compliance, and outcomes.
field_species_variation|Individuals Within a Stock|How much behavior or appearance varies within a named population?|Compare age, sex, season, identity method, and sample size.
field_ecological_role|A Marine Mammal's Ecosystem Role|Which effects on prey or habitat have been measured?|Distinguish direct evidence, model inference, and popular claims.
field_experimental_model|What Tags Can and Cannot Tell Us|Which question can tagging answer for a particular species?|Discuss sample bias, device effect, duration, permissions, and welfare.
field_evolutionary_history|How a Marine Mammal Lineage Evolved|Which fossils and genomes support one evolutionary account?|Compare dates, sampling, anatomy, and alternative phylogenies.
field_conservation_status|Evidence Behind a Stock's Status|What supports the latest status designation of one stock?|Check assessment date, abundance, trend, mortality, threats, and review process.
"""


if __name__ == "__main__":
    revise_domain("197", "197_marine_mammals", MARINE_MAMMALS,
                  "Marine mammals through species and stock boundaries, population assessment, movement, threats, human use, and conservation outcomes.",
                  "current stock assessment reports, peer-reviewed surveys and methods, verified incident records, authorized tracking studies, and consented coastal and Indigenous accounts",
                  "Name species, stock, jurisdiction, season, and assessment year. Do not infer stock growth from sightings or one tracked animal; protect sensitive locations and follow current wildlife-viewing and research rules.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
