"""Editorial question designs for niche 200, Botany."""

from review_angle_plans import audit, revise_domain


BOTANY = """history_origins|How a Plant Was Named|Which specimens and descriptions established one plant species?|Trace type material, collection locality, naming, and revision.
famous_examples|A Famous Plant Discovery Rechecked|What does one celebrated botanical discovery actually establish?|Check specimen identity, earlier local knowledge, location, and later records.
hidden_stories|The People Behind an Herbarium Sheet|Whose field and curatorial work preserved one plant record?|Trace collectors, local guides, preparators, identifiers, and data workers.
beginner_explainers|Reading a Plant Specimen|What can a herbarium sheet tell us and what can it not?|Interpret label, date, place, morphology, and collection bias.
advanced_concepts|Plant Species Boundaries|When do morphology, genetics, and reproduction suggest different classifications?|Choose one disputed complex and compare the evidence.
mysteries_unsolved_cases|A Plant Missing from Its Recorded Site|What could explain an apparent local disappearance?|Test name changes, season, survey effort, land use, and climate.
technology_innovation|Digitizing Plant Collections|Does a digital herbarium improve research access and identification?|Compare image quality, label transcription, provenance, and remaining physical needs.
people_personalities|A Botanical Revision|How did one researcher's classification change understanding of a plant group?|Use publications, vouchers, objections, and later evidence.
major_events|A Drought or Land Change and Plants|How did one documented event alter a plant community?|Compare before and after plots, species, soil, rainfall, and confounders.
how_it_works|A Plant's Annual Cycle|How do germination, growth, flowering, and seed production unfold?|Choose one species and identify environmental triggers and variation.
rise_fall|A Plant Population's Trend|What evidence supports increase or decline of one species?|Compare repeat plots, recruitment, mortality, land use, and detection.
then_vs_now|One Flora Across Two Eras|What do historical and recent plant records reveal?|Match taxonomy, sites, season, collecting effort, and habitat.
future_developments|Where a Plant Could Grow Next|Which conditions might change a species' range?|State climate, soils, dispersal, land use, and model assumptions.
myths_vs_facts|Does Native Mean Harmless?|What evidence supports a common claim about one plant in one place?|Define native range, ecological interaction, context, and harm measure.
documentary_stories|A Plant Record Revisited|What happened when botanists returned to a historic collection site?|Trace original voucher, geolocation, modern survey, and uncertainty.
observation_to_explanation|One Flowering Plant's Meaning|What can a single bloom observation establish?|Separate phenology from population size, health, and climate trend.
measurement_method|Counting Plants in a Plot|How does one field protocol estimate abundance or cover?|Check plot design, season, life stage, identification, and uncertainty.
scale_and_timespan|One Plot Versus a Region|At what scale is a botanical trend supported?|Define taxon, habitat, region, years, and survey coverage.
field_vs_lab|A Plant Trait in Nature|Does a controlled growth response predict field performance?|Compare soil, competition, water, pests, life stage, and replication.
natural_variation|Good and Bad Seed Years|How much yearly variation is normal for one plant?|Use long-term seed, flowering, and weather records.
mechanism_chain|From Pollinator Loss to Seeds|Which evidence connects a pollinator change to plant recruitment?|Trace visits, pollen transfer, seed set, germination, and survival.
extreme_case|A Record Tree or Flower|How was an exceptional plant measurement verified?|Check species ID, measurement standard, date, and independent records.
classification_debate|A Plant Name in Dispute|Why do botanists split or combine one plant lineage?|Compare type specimens, morphology, sequences, and nomenclature.
interacting_systems|Plants, Soil, and Partners|How do microbes, pollinators, herbivores, and soil affect one plant?|Test measured links and competing explanations.
data_gap|Herbarium Blind Spots|Which locations, seasons, or groups are underrepresented in plant collections?|Map collecting effort, digitization, access, and identification backlog.
prediction_test|Did a Flowering Forecast Hold?|Did a predicted timing or range shift match later observations?|Compare forecast date, weather, survey methods, and measured response.
human_impact|A Plant and Human Use|How does one plant species affect or support a community?|Examine uses, access rights, trade, ecological effects, and local knowledge.
field_species_variation|Variation Within a Plant Species|How much do form and flowering vary by site or season?|Compare verified specimens, environment, age, and genetics.
field_ecological_role|What One Plant Provides|Which organisms use one plant for food or habitat?|Use field measurements and distinguish visitation from effective service.
field_experimental_model|Why Researchers Use This Plant|Which mechanism can one model plant test?|Identify experimental advantages and limits for other species or field conditions.
field_evolutionary_history|Tracing a Plant Lineage|Which fossils and genetic data support one evolutionary account?|Compare dating, taxon sampling, and alternative trees.
field_conservation_status|Evidence Behind a Plant's Risk Status|What supports the current assessment of one species?|Check range, population trend, threats, collection bias, date, and uncertainty.
"""


if __name__ == "__main__":
    revise_domain("200", "200_botany", BOTANY,
                  "Botany through specimens, taxonomy, plant life cycles, monitoring, ecological partners, and conservation evidence.",
                  "vouchered herbarium specimens, taxonomic revisions, repeat plant plots, phenology observations, controlled studies, land-use records, and species assessments",
                  "Name plant species, place, life stage, season, and date. Distinguish one collection or bloom from a population trend and attribute local and Indigenous knowledge with consent and context.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
