"""Editorial question designs for niche 202, Trees."""

from review_angle_plans import audit, revise_domain


TREES = """history_origins|How a Tree Species Was Named|Which specimens established a named tree's identity?|Trace type material, collection site, description, and revision.
famous_examples|A Famous Old Tree Rechecked|What evidence supports the age and history of a celebrated tree?|Check species ID, dating method, living tissue, site, and uncertainty.
hidden_stories|Who Keeps a Tree Inventory?|Whose field and data work produces a forest estimate?|Trace plot crews, taxonomists, local stewards, and analysts.
beginner_explainers|Reading a Tree's Structure|How do roots, trunk, canopy, and leaves serve one tree species?|Use a named species and distinguish function across age and site.
advanced_concepts|Tree Cover Is Not Forest Health|Why can canopy area increase while other forest measures worsen?|Compare species mix, age, mortality, regeneration, soil, and habitat.
mysteries_unsolved_cases|Why Trees Died in One Stand|Which evidence could explain a documented mortality cluster?|Test drought, insects, disease, fire, soil, and management history.
technology_innovation|Remote Sensing Versus Field Plots|Does one imagery method improve a tree estimate?|Compare canopy detection, species ID, calibration, cost, and field checks.
people_personalities|A Forest Decision Maker|How did one named manager or scientist change tree stewardship?|Use dated plans, objections, implementation, and measured outcomes.
major_events|After a Forest Fire|What changed in tree survival and regeneration after one fire?|Compare severity, species, seedlings, climate, management, and time.
how_it_works|How a Tree Grows|How do cambium, water transport, and photosynthesis connect?|Explain a named species under defined conditions without oversimplifying limits.
rise_fall|A Tree Population's Trajectory|What supports an increase or decline in a defined tree population?|Use repeated plots, recruitment, mortality, harvest, and uncertainty.
then_vs_now|One Stand Across Inventories|What changed between two comparable forest surveys?|Match plot design, definitions, species names, dates, and land boundary.
future_developments|A Forest Stand Under Change|Which scenarios could affect tree survival and regeneration?|State climate, disturbance, pests, management, and model assumptions.
myths_vs_facts|Does Planting Trees Always Restore a Forest?|When do planted trees improve or harm a chosen habitat?|Compare native ecosystem, survival, water, biodiversity, and long-term care.
documentary_stories|One Tree's Recorded Life|What can dated records reveal about a landmark tree?|Use planting or discovery record, measurements, weather, management, and consent.
observation_to_explanation|One Dead Tree's Meaning|What can a single dead tree tell us about forest condition?|Separate individual cause from stand-wide mortality and regional trend.
measurement_method|How Forest Inventories Count Trees|How does a probabilistic plot survey estimate forest attributes?|Explain plot selection, tree threshold, repeated measurement, and error.
scale_and_timespan|A Stand Versus a Region|At what scale is a tree trend supported?|Define population, stand, ownership, region, years, and sampling frame.
field_vs_lab|Drought Response in the Field|Does a controlled seedling result predict adult tree survival?|Compare age, roots, soil, competition, and multi-year field data.
natural_variation|Good and Bad Growth Years|How much tree growth varies with weather and site?|Use long records and separate age effect from environment.
mechanism_chain|From Drought to Tree Death|Which evidence links water stress to a measured mortality event?|Trace soil water, hydraulic stress, pests, crown change, and timing.
extreme_case|The Tallest or Oldest Tree Claim|How was an extraordinary tree record measured?|Check species, height or age method, date, damage, and verification.
classification_debate|A Tree Species in Dispute|Why do botanists disagree over one tree lineage?|Compare type specimens, leaves, reproductive traits, genetics, and range.
interacting_systems|Trees and Their Neighbors|How do fungi, insects, understory plants, and soil affect one stand?|Test measured links and competing causes.
data_gap|Forest Plots' Blind Spots|Which trees or habitats are weakly represented in an inventory?|Review inaccessible plots, urban trees, rare species, and measurement definitions.
prediction_test|Did a Forest Forecast Hold?|Did a predicted mortality or growth pattern appear in later plots?|Compare model version, assumptions, dates, and observations.
human_impact|Who Benefits from Trees Here?|How are shade, timber, habitat, and costs distributed?|Compare location, ownership, maintenance, access, and affected communities.
field_species_variation|One Tree Species Across Sites|How do form and growth differ by site and genotype?|Compare verified individuals, age, soil, climate, and management.
field_ecological_role|A Tree's Habitat Contribution|Which organisms use one tree species and how?|Measure nesting, food, shade, or substrate use without universal claims.
field_experimental_model|Testing Tree Management|What can a thinning or planting trial establish?|Specify controls, replication, duration, site history, and transfer limits.
field_evolutionary_history|Tracing a Tree Lineage|Which fossils and genomes support one evolutionary path?|Compare fossil placement, dating, and alternative trees.
field_conservation_status|Assessing One Tree Species|What supports its current conservation status?|Check range, population, regeneration, threats, survey coverage, and date.
"""


if __name__ == "__main__":
    revise_domain("202", "202_trees", TREES,
                  "Trees through species evidence, growth, repeat forest inventories, disturbance, regeneration, habitat, and stewardship.",
                  "vouchered identification, repeat forest plots and protocols, remote sensing with field calibration, climate and disturbance records, and species assessments",
                  "Name species, forest type, plot scale, geography, and date. Distinguish tree cover from ecosystem health and one tree's condition from a stand or regional trend.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
