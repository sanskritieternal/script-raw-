"""Editorial question designs for niche 199, Coral Reefs."""

from review_angle_plans import audit, revise_domain


CORAL = """history_origins|How One Reef Formed|Which geological and biological processes built a named reef?|Use cores, sea-level history, species records, and dating uncertainty.
famous_examples|A Celebrated Reef Recovery Rechecked|What outcome followed one widely praised restoration effort?|Compare baseline, survival, coral cover, species mix, cost, and controls.
hidden_stories|The People Who Monitor a Reef|Whose work produces reef condition data?|Trace divers, boat crews, local stewards, taxonomists, and analysts.
beginner_explainers|What Makes a Coral Reef?|How do coral animals, symbionts, skeletons, and other organisms build a reef?|Use a named reef and distinguish living coral from reef structure.
advanced_concepts|Reef Health Has Many Metrics|Why can coral cover, bleaching, disease, and fish biomass disagree?|Compare measurement methods, depth, habitat, and time.
mysteries_unsolved_cases|Why One Patch Fared Better|Which factors could explain a difference in bleaching or survival?|Test depth, heat exposure, species, water quality, survey design, and history.
technology_innovation|A Reef Mapping Tool Tested|Does imagery or remote sensing improve one reef measure?|Compare ground truth, depth limit, resolution, cost, and error.
people_personalities|A Reef Protection Decision|How did one named steward or manager shape a reef intervention?|Use dated plans, local consent, counterarguments, and monitoring.
major_events|One Marine Heatwave on a Reef|What changed during and after a documented heat event?|Track temperature, bleaching, mortality, recovery, and uncertainty.
how_it_works|How Coral Bleaching Happens|What mechanisms connect heat stress, symbiosis, bleaching, and survival?|Separate bleaching observation from confirmed mortality.
rise_fall|A Reef's Long-Term Trajectory|What evidence supports change at one reef?|Compare consistent transects, coral cover, recruitment, disturbance, and data gaps.
then_vs_now|The Same Reef in Two Surveys|Which differences reflect change rather than method?|Match sites, depth, season, observers, taxonomic detail, and metrics.
future_developments|Scenarios for a Named Reef|Which conditions could shape its next decade?|State heat, storms, water quality, fishing, adaptation, and uncertainty.
myths_vs_facts|Does Bleached Mean Dead?|What can a bleaching photograph establish?|Distinguish pigment loss, tissue mortality, later recovery, and survey date.
documentary_stories|A Reef Through One Disturbance|How did a named reef respond to one documented event?|Build a dated sequence from monitoring, local testimony, and management records.
observation_to_explanation|One White Colony's Meaning|What can a single pale coral colony tell us?|Separate species ID, bleaching, disease, mortality, and reef-wide prevalence.
measurement_method|Counting Coral Cover|How does one protocol estimate live coral cover?|Examine transects, image annotation, depth, observer agreement, and uncertainty.
scale_and_timespan|A Patch Versus a Reef Region|At what scale does a coral condition claim hold?|Define patch, reef, habitat, region, season, and sampling frame.
field_vs_lab|Coral Heat Tolerance in Context|Does a lab heat response predict field survival?|Compare species, symbionts, duration, water chemistry, and field validation.
natural_variation|Normal Reef Change or Long Decline?|How much cover or community variation occurs between surveys?|Use multi-year site data and disturbance history.
mechanism_chain|From Heat Stress to Reef Function|Which evidence connects exposure, coral loss, and habitat change?|Trace temperature, bleaching, mortality, structural complexity, and fish response.
extreme_case|The Hottest Reef Observation|How was an exceptional thermal or bleaching record measured?|Check sensor, depth, baseline, duration, and independent confirmation.
classification_debate|Which Coral Is This?|How do morphology and genetics affect identification of one coral group?|Compare vouchers, imagery, molecular data, and revised names.
interacting_systems|Corals, Algae, Fish, and Water|How do grazing and water quality interact with coral recovery?|Test competing explanations using local monitoring.
data_gap|Where Reef Surveys Are Thin|Which habitats, depths, or seasons are missing from a condition claim?|Map sampling design, access constraints, and method sensitivity.
prediction_test|Did a Bleaching Forecast Hold?|How did a forecast compare with observed bleaching at a named reef?|Match prediction date, heat metric, survey timing, species, and false alarms.
human_impact|Who Depends on a Reef?|How do reef changes affect communities and uses?|Compare fisheries, tourism, coastal protection, access, and local testimony.
field_species_variation|Not All Corals Respond Alike|How does a heat event affect different coral species at one site?|Compare exposure, baseline cover, bleaching, mortality, and recovery.
field_ecological_role|A Coral's Habitat Role|Which organisms use the structure created by one coral group?|Use measured occupancy or behavior rather than broad reef claims.
field_experimental_model|What Coral Experiments Can Prove|Which restoration or tolerance question can one trial answer?|Specify controls, replication, duration, site, and transfer limits.
field_evolutionary_history|How Reef Builders Changed|Which fossils and genomes trace one coral lineage?|Compare dating, skeletal traits, molecular evidence, and uncertainty.
field_conservation_status|Evidence Behind a Coral Assessment|What supports the risk status of one coral species?|Check range, trend, threats, taxonomic certainty, date, and survey gaps.
"""


if __name__ == "__main__":
    revise_domain("199", "199_coral_reefs", CORAL,
                  "Coral reefs through formation, coral biology, bleaching, survey methods, restoration evidence, local use, and long-term change.",
                  "dated reef monitoring protocols and surveys, temperature and water-quality records, verified imagery, controlled restoration studies, local management plans, and species assessments",
                  "Name reef, depth, species, metric, and survey date. Distinguish bleaching from mortality and coral cover from overall reef health; avoid extrapolating one image or restored plot to an entire reef.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
