"""Editorial question designs for niche 203, Fungi."""

from review_angle_plans import audit, revise_domain


FUNGI = """history_origins|How a Fungus Was Named|Which specimen and description established one fungal species?|Trace type material, host or substrate, locality, and later revisions.
famous_examples|A Famous Fungus Rechecked|What does a celebrated fungal case actually demonstrate?|Specify species, setting, observations, and limits of generalization.
hidden_stories|The People Behind a Fungus Collection|Whose collecting and curatorial work makes one taxonomic claim possible?|Trace field workers, local specialists, culture collections, and identifiers.
beginner_explainers|Fungi Beyond Mushrooms|How do fungal bodies, spores, and life cycles differ across groups?|Compare named examples and distinguish fungus from visible fruiting body.
advanced_concepts|A Fungus Has More Than One Name?|Why can morphology and DNA lead to taxonomic revision?|Use vouchered material, reference sequences, and naming history.
mysteries_unsolved_cases|An Unidentified Fungal Outbreak|Which evidence could establish cause in a documented case?|Check sampling, species ID, host condition, environment, and alternatives.
technology_innovation|Sequencing Fungal Diversity|What can DNA methods detect in soil or tissue?|Compare reference gaps, contamination, dormant spores, and live activity.
people_personalities|A Mycologist's Revision|How did one scientist change classification of a fungal group?|Use specimens, cultures, publications, dissent, and later evidence.
major_events|A Fungal Disease Arrives|How did a documented pathogen change one host population?|Trace identification, spread, management, and measured host effects.
how_it_works|From Spore to Fruiting Body|Which stages make a mushroom appear at one site?|Specify species, substrate, mycelium, weather, and reproductive cycle.
rise_fall|A Fungal Population's Apparent Change|What supports a rise or decline for one fungus?|Compare repeat surveys, fruiting variability, host availability, and detection.
then_vs_now|A Fungus Across Collections|What do historical and recent specimens show about its range?|Match taxonomy, sites, season, collection effort, and preservation.
future_developments|Fungi Under Habitat Change|Which plausible conditions could alter one fungal group?|State host, moisture, temperature, land use, and dispersal assumptions.
myths_vs_facts|Can Appearance Prove Edibility?|Why does visual resemblance fail to establish whether a wild fungus is safe?|Compare documented lookalikes and identification uncertainty without foraging advice.
documentary_stories|One Specimen's Identification Journey|How did a collected fungus become evidence for a species claim?|Trace location, substrate, voucher, microscopy, sequencing, and revision.
observation_to_explanation|A Mushroom After Rain|What can one fruiting observation establish?|Separate visible fruiting from underground persistence, abundance, and trend.
measurement_method|Surveying Fungal Diversity|How does one method estimate which fungi occur at a site?|Compare fruiting surveys, culture, DNA, season, and taxonomic resolution.
scale_and_timespan|A Patch Versus a Region|At what scale is a fungal distribution claim supported?|Define species, substrate, habitat, years, and sampling coverage.
field_vs_lab|A Culture Outside Its Habitat|Does laboratory growth predict a fungus's field role?|Compare substrate, competitors, host, moisture, and validation.
natural_variation|Why Fruiting Varies Between Years|How much can visible mushrooms change with weather?|Use multi-year and repeated surveys; separate fruiting from organism presence.
mechanism_chain|From Fungus to Host Damage|Which evidence links a fungus to a plant or animal disease?|Trace verified organism, infection, tissue effect, host outcome, and alternatives.
extreme_case|An Extraordinary Fungal Colony|How was a reported size, age, or spread verified?|Check genetic identity, boundary sampling, measurement, and date.
classification_debate|A Fungal Species Complex|Why do researchers split or combine one fungal lineage?|Compare type specimens, microscopic traits, DNA, host, and geography.
interacting_systems|Fungi in Soil and Food Webs|How do fungi, plants, microbes, and animals interact at one site?|Use measured exchanges and distinguish mutualism from mere co-occurrence.
data_gap|The Fungi We Have Not Recorded|Which taxa or habitats are missing from inventories?|Map substrate, season, geographic, and reference-sequence gaps.
prediction_test|Did a Fungal Range Forecast Hold?|Did a predicted occurrence match later verified specimens?|Compare forecast date, survey effort, species ID, and habitat.
human_impact|One Fungus and Human Activity|How does a named fungus affect livelihoods or ecosystems?|Examine forestry, agriculture, fermentation, disease, or conservation with context.
field_species_variation|Variation Within One Fungus|How do life stage, substrate, and environment alter appearance?|Use verified specimens and cultures before identifying variants.
field_ecological_role|What This Fungus Actually Does|Is one fungus a decomposer, parasite, or partner in a defined setting?|Use observed substrate use, host effect, and experimental evidence.
field_experimental_model|Fungi as Research Models|Which mechanism can one fungal model species test?|State laboratory advantages and limits of transfer to wild species.
field_evolutionary_history|A Fungal Lineage Through Time|Which fossils and sequences support one evolutionary account?|Compare dating, taxon sampling, and alternative trees.
field_conservation_status|Does This Fungus Need Protection?|What evidence supports a species assessment?|Check range, substrate or host dependence, threats, survey coverage, and date.
"""


if __name__ == "__main__":
    revise_domain("203", "203_fungi", FUNGI,
                  "Fungi through taxonomy, specimens, fruiting and hidden life stages, ecological roles, disease evidence, and conservation.",
                  "vouchered fungal specimens and cultures, taxonomic revisions, repeat field surveys, verified sequence databases, host records, and species assessments",
                  "Name fungal species or group, host or substrate, site, season, and date. Do not equate mushroom sightings with abundance or infer edibility from appearance; avoid consumption, diagnosis, or treatment advice.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
