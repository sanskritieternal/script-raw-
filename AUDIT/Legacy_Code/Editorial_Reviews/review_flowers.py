"""Editorial question designs for niche 201, Flowers."""

from review_angle_plans import audit, revise_domain


FLOWERS = """history_origins|How One Floral Form Was Described|Which specimens established the identity of a named flowering plant?|Trace type material, original illustration, locality, and revision.
famous_examples|A Famous Bloom Rechecked|What does one celebrated mass flowering event show?|Define species, site, observation years, weather, and observer effort.
hidden_stories|Who Records Flowering Seasons?|Whose observations make a long bloom record possible?|Trace local observers, gardeners, field botanists, and data curators.
beginner_explainers|What a Flower Does|How do the parts of one flower contribute to reproduction?|Use a named species and distinguish pollen transfer from seed production.
advanced_concepts|Bloom Timing and Pollinator Match|Does a timing shift change reproduction for one plant?|Compare flower stage, visitor presence, pollen transfer, and seed set.
mysteries_unsolved_cases|Why a Plant Did Not Bloom|Which evidence could explain a missed flowering season?|Test age, water, temperature, light, damage, and observation frequency.
technology_innovation|Automated Bloom Monitoring|Does imaging improve a flowering record?|Compare species recognition, phenophase definitions, timing, and field validation.
people_personalities|A Flower Researcher's Discovery|How did one named botanist or ecologist change understanding of a flower?|Use original records, later tests, and attribution to collaborators.
major_events|A Frost During Flowering|What happened to reproduction after one documented frost?|Compare exposure, flower damage, pollinator activity, and fruit set.
how_it_works|From Bud to Seed|Which stages connect a flower bud to a mature seed?|Trace opening, pollen transfer, fertilization, fruit, and failed stages.
rise_fall|The Changing Bloom at One Site|What supports a trend in flowering time or intensity?|Use repeated observations, consistent definitions, weather, and missing dates.
then_vs_now|A Bloom Record Across Decades|How comparable are historical and recent first-flower dates?|Check observer method, plant identity, site, and observation frequency.
future_developments|Flowering Under Future Conditions|Which plausible changes could alter bloom timing for one species?|State temperature, rainfall, light, genetics, and model assumptions.
myths_vs_facts|Does a Visitor Pollinate?|When does a flower visitor actually deliver effective pollen?|Compare visitation, pollen deposition, fertilization, and seed set.
documentary_stories|One Plant Through a Bloom Season|What can repeated observation of one plant reveal?|Track buds, open flowers, visits, fruit, weather, and uncertainty.
observation_to_explanation|An Early Flower Sighting|What can one unusually early flower establish?|Separate individual variation from population trend and climate attribution.
measurement_method|Recording a Bloom Precisely|How does a phenology protocol define and count flowering?|Specify plant identity, phenophase, observation interval, intensity, and gaps.
scale_and_timespan|One Garden Versus a Region|At what scale does a bloom timing claim hold?|Define species, site conditions, years, and geographic coverage.
field_vs_lab|A Flowering Trigger in Nature|Does a controlled light or temperature response hold outdoors?|Compare plant age, water, soil, competition, and field data.
natural_variation|Why Bloom Dates Vary|How much timing variation occurs among individuals and years?|Use multi-year records and local weather context.
mechanism_chain|From Pollinator Visit to Seed|Which steps link a visit to successful reproduction?|Trace pollen transfer, compatibility, fertilization, and seed viability.
extreme_case|An Exceptional Flowering Event|How was a record bloom duration or size verified?|Check species, measurement, observation gaps, and independent records.
classification_debate|Which Flowering Plant Is This?|Why do botanists disagree over a lookalike plant?|Compare type specimens, floral structures, genetics, and range.
interacting_systems|Flowers in a Seasonal Network|How do blooms and pollinators interact across one site?|Compare flowering schedules, visitor networks, resources, and effective pollination.
data_gap|Whose Blooms Go Unrecorded?|Which habitats, seasons, or plants are missing from flower data?|Map observation bias, inaccessible sites, and identification limits.
prediction_test|Did a Bloom Forecast Hold?|Did a forecast date match observed flowering?|Compare forecast issue date, plant identity, observation protocol, and error.
human_impact|A Bloom's Human Meaning|How does one flowering event affect people and place?|Compare cultural use, tourism, growing practices, access, and habitat effects.
field_species_variation|Different Flowers on One Species|How do age, genetics, environment, or sex change floral appearance?|Use verified individuals and repeated measurements.
field_ecological_role|What One Flower Provides|Which organisms use a flower and what benefit is measured?|Distinguish nectar or pollen use from effective pollination.
field_experimental_model|Testing a Flower Hypothesis|Which question can a controlled pollination experiment answer?|Specify controls, sample size, bagging effects, and field limits.
field_evolutionary_history|How a Floral Trait Evolved|Which phylogeny and trait evidence support one evolutionary claim?|Compare ancestral-state assumptions, fossils, and alternative routes.
field_conservation_status|Does This Flowering Plant Need Protection?|What evidence supports risk status for one species?|Check range, reproduction, threats, survey coverage, and assessment date.
"""


if __name__ == "__main__":
    revise_domain("201", "201_flowers", FLOWERS,
                  "Flowers through floral anatomy, phenology, pollination evidence, reproductive outcomes, and human meaning.",
                  "vouchered plant identity, repeated phenology observations, visitor and pollen-transfer studies, seed-set measurements, weather records, and species assessments",
                  "Name plant species, place, phenophase, observation interval, and date. Distinguish a flower visitor from an effective pollinator and one early bloom from a population or climate trend.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
