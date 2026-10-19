"""Editorial questions for gardening plants and wildlife animals."""

from review_angle_plans import audit, revise_domain


PLANTS = """history_origins|A Garden Plant's Journey|How did one named plant enter a particular gardening tradition?|Trace botanical records, cultivation notes, trade, and local knowledge.
famous_examples|A Celebrated Garden Plant Under Test|Does one popular cultivar deliver its advertised traits in defined conditions?|Compare independent trials, climate, soil, pests, and maintenance.
hidden_stories|The People Behind a Garden Variety|Whose breeding, propagation, seed saving, or care is omitted from its story?|Use attributed records and respect community knowledge.
beginner_explainers|What a Plant Needs to Grow|How do light, water, soil, temperature, and species traits interact?|Use one identified species and local climate; mark advice as context-dependent.
advanced_concepts|A Garden's Soil-Plant System|How do soil structure, nutrients, organisms, and watering affect a defined outcome?|Compare measured conditions and controlled trials, not a single universal recipe.
mysteries_unsolved_cases|A Plant Decline With Several Causes|Which evidence distinguishes disease, water stress, pests, and site mismatch?|Use diagnostic studies and local observations; avoid confident remote diagnosis.
technology_innovation|A Gardening Method Tested|Did one irrigation, propagation, or growing medium improve a stated outcome?|Compare matched plots, inputs, yield or survival, and costs.
people_personalities|A Breeder or Botanist's Contribution|What did one named contributor actually develop or document?|Trace dated specimens, patents, publications, and collaborator roles.
major_events|A Plant Pest or Policy Change|How did one dated introduction, disease, or restriction affect gardeners?|Compare surveillance, plant losses, responses, and local rules.
how_it_works|From Seed or Cutting to Established Plant|Which biological stages matter in one plant's establishment?|Use species-specific research and describe stages without claiming universal timing.
rise_fall|A Garden Trend's Change|Why did one plant become popular and then decline?|Compare availability, climate fit, disease, fashion, and policy.
then_vs_now|A Garden Across Two Climates or Eras|How did planting choices change as conditions changed?|Compare matched sites, weather, management, and outcomes.
future_developments|A Proposed Garden Adaptation|What evidence would show that one planting strategy withstands future conditions?|Define species, place, climate scenario, biodiversity, and monitoring.
myths_vs_facts|Testing a Gardening Rule|Does a common plant-care rule hold for a named species and setting?|Compare controlled evidence with local soil, climate, and cultivar limits.
documentary_stories|One Garden's Measured Seasons|How did a bounded planting project change from plan to outcome?|Build a dated record of conditions, interventions, failures, and harvest or survival.
observation_to_explanation|From Yellow Leaves to Hypothesis|Which measured clues support one explanation for a plant symptom?|Compare multiple causes and confirmatory evidence without diagnosis by photo alone.
measurement_method|How to Measure Garden Success|Which survival, growth, yield, or biodiversity measure fits one question?|Define baseline, sampling, units, season, and confounders.
scale_and_timespan|One Season or a Lasting Result?|Does a short trial predict long-term performance of a planting?|Compare repeated seasons, weather variation, and maintenance.
field_vs_lab|A Plant Trial Meets a Real Garden|Which controlled findings transfer to variable home plots?|Compare cultivar, soil, climate, pests, and care intensity.
natural_variation|Why Identical Seeds Differ|How much variation arises from genotype, microclimate, and management?|Use replicated observations and avoid attributing every difference to one factor.
mechanism_chain|How a Gardening Intervention Works|What biological steps could explain one measured result?|Connect mechanism to plant outcomes and alternative pathways.
extreme_case|Plants at Environmental Limits|How does one species respond near heat, cold, drought, or shade limits?|Use range and trial evidence without extrapolating from a single survivor.
classification_debate|What Plant Is This?|How do accepted names and cultivar labels affect a gardening claim?|Check current taxonomy, synonyms, and verified specimen or seed source.
interacting_systems|A Garden as Habitat|How do planting, soil, insects, water, and neighboring land interact?|Measure a bounded garden and acknowledge wider ecological context.
data_gap|What Garden Evidence Is Missing?|Which missing measurements prevent judging one advice claim?|Identify controls, follow-up seasons, species identity, and adverse outcomes.
prediction_test|A Testable Plant-Care Claim|What would one small, lawful trial show about a proposed practice?|Specify comparison, replication, observations, and limits without hazardous chemicals.
human_impact|A Garden's Costs and Benefits|Who receives food, shade, access, or work from one planting choice?|Compare household and community outcomes with water and maintenance costs.
field_species_variation|Cultivars Are Not the Same|How do named cultivars differ under matched conditions?|Compare trials with verified identities and measured traits.
field_ecological_role|A Plant's Local Relationships|Which pollinators or other organisms use one plant in a named place?|Use field observations and distinguish visitation from ecological benefit.
field_experimental_model|A Garden Trial That Can Be Checked|How would a simple design isolate one treatment effect?|Specify comparable plots, randomization where feasible, measurements, and limitations.
field_evolutionary_history|From Wild Relative to Cultivar|Which selection steps produced a cultivated plant's traits?|Use taxonomy, breeding records, and genetic evidence without a single-origin myth.
field_conservation_status|Growing a Threatened Plant Responsibly|What do current conservation assessments and local rules imply for cultivation?|Check verified species identity, sourcing, disease risk, and habitat context."""


WILDLIFE = """history_origins|How a Species Was Documented|When and where was one animal first described in scientific records?|Compare original description, specimens, Indigenous and local knowledge, and later taxonomy.
famous_examples|A Famous Wildlife Study Reexamined|What did one influential animal study measure and leave unresolved?|Check sampling, methods, geography, and subsequent replication.
hidden_stories|Local Observers and Field Workers|Whose tracking, guiding, data collection, or stewardship is missing from a wildlife story?|Use credited field records and attributed local knowledge.
beginner_explainers|A Species in Its Habitat|What food, shelter, movement, and life-cycle needs define one population?|Use a named species and place, distinguishing individual behavior from population patterns.
advanced_concepts|Counting Animals That Are Hard to See|How do detection probability and sampling design affect a population estimate?|Compare method, uncertainty, season, and habitat coverage.
mysteries_unsolved_cases|An Uncertain Population Trend|Why do two credible estimates disagree for one species?|Check area, method, effort, detection, and date before inferring change.
technology_innovation|A Wildlife Monitoring Tool|What can camera traps, tags, acoustics, or DNA reveal about one question?|Compare validation, disturbance, sampling bias, and data governance.
people_personalities|A Researcher's Field Decision|How did one named scientist or local steward shape a study?|Trace methods, collaborators, constraints, and later correction.
major_events|A Conservation Turning Point|What changed after one protected-area decision or documented threat?|Compare policy, habitat, population measures, and community effects.
how_it_works|A Species' Annual Cycle|How do feeding, breeding, movement, and survival connect?|Use one population's longitudinal evidence, not a universal species story.
rise_fall|A Population's Change|Which interacting pressures explain a documented increase or decline?|Compare habitat, climate, disease, harvest, and measurement uncertainty.
then_vs_now|A Habitat Across Two Periods|How did land use and wildlife presence change?|Use comparable maps, survey effort, and species definitions.
future_developments|A Proposed Conservation Action|What evidence would show whether one intervention helps?|Define target population, counterfactual, local rights, monitoring, and costs.
myths_vs_facts|Testing an Animal Behavior Claim|Does a popular claim hold across documented observations?|Check species, setting, sample, alternative explanations, and exceptions.
documentary_stories|One Population Through Its Records|How did a species' status change in one place over time?|Build a dated timeline from surveys, policy, habitat, and community accounts.
observation_to_explanation|From Sighting to Inference|What can a field observation establish about a species?|Separate occurrence, abundance, behavior, and causal explanation.
measurement_method|How Wildlife Is Counted|Which survey method fits one species and landscape?|Explain effort, detection, sampling frame, uncertainty, and disturbance.
scale_and_timespan|A Short Study Versus a Trend|How many seasons of evidence support one population claim?|Compare annual variation, survey consistency, and longer baselines.
field_vs_lab|Behavior in Captivity and Wild|Which results from a controlled setting transfer to free-ranging animals?|Compare ecology, stress, selection, and behavior measures.
natural_variation|Individuals and Populations Differ|How much behavioral or physical variation exists within one species?|Use representative samples across age, sex, season, and habitat as relevant.
mechanism_chain|How a Threat Affects Survival|Which steps link one pressure to population change?|Connect exposure, individual effect, reproduction, and population evidence.
extreme_case|Life at a Range Edge|What does one species reveal at the edge of its habitat or climate range?|Compare multiple sites and avoid generalizing from exceptional individuals.
classification_debate|A Species Boundary Revisited|What evidence supports splitting or combining named animal populations?|Compare morphology, genetics, geography, and conservation implications.
interacting_systems|One Animal in a Food Web|What documented interactions link one species to others?|Use local field evidence and distinguish correlation from causal effects.
data_gap|Who and What Was Not Counted?|Which missing habitats, seasons, or communities limit a wildlife dataset?|Audit sampling effort, access, and reporting bias.
prediction_test|A Forecast for a Population|What observation would test one ecological model's prediction?|State model assumptions, time horizon, monitoring, and falsifying outcomes.
human_impact|People and Wildlife Together|How do conservation and conflict affect nearby residents?|Use attributed local voices, ecological measures, and distribution of costs.
field_species_variation|Different Populations, Different Outcomes|How do two populations of one species differ under comparable measures?|Match ecology, survey methods, genetic context, and dates.
field_ecological_role|A Claimed Keystone Role|Does evidence show one animal changes a defined ecological outcome?|Compare interventions or natural contrasts and alternative causes.
field_experimental_model|Testing a Wildlife Hypothesis|Which ethical field design could isolate one proposed mechanism?|Use non-invasive methods, permits, controls, and disturbance limits.
field_evolutionary_history|Tracing a Species' Lineage|What fossil and genetic evidence supports one evolutionary account?|Compare dated specimens, phylogenetic models, and uncertainty.
field_conservation_status|What a Status Category Means|Which population and threat evidence supports one current assessment?|Check assessment date, geography, criteria, and data gaps."""


if __name__ == "__main__":
    revise_domain("065", "065_gardening_plants", PLANTS,
                  "Gardening and plants through verified species identities, local growing conditions, controlled trials, soil and ecological interactions, and responsible sourcing.",
                  "current taxonomic and distribution records, plant trial methods and results, local climate and soil measurements, extension research, and documented gardener and community experience",
                  "Name accepted species or cultivar, place, soil, season, and management. Avoid universal care rules or remote diagnosis; check current local invasive, toxic-plant, pesticide, and conservation guidance before production.")
    revise_domain("066", "066_wildlife_animals", WILDLIFE,
                  "Wildlife through named species and populations, field methods, behavior, ecology, conservation evidence, and effects on neighboring people.",
                  "peer-reviewed field studies and raw survey methods, taxonomic records, dated conservation assessments, habitat data, and attributed local and Indigenous knowledge where permission is granted",
                  "Name species, population, place, method, and date. Account for detection and sampling bias; do not publish vulnerable locations or wildlife-handling instructions, and verify current status and local permits.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
