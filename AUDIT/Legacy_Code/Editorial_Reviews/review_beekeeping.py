"""Editorial question designs for niche 192, Beekeeping."""

from review_angle_plans import audit, revise_domain


BEEKEEPING = """history_origins|How Managed Hives Took Shape|Which tools and land practices changed beekeeping in one region?|Compare dated manuals, equipment, crop patterns, and beekeeper accounts.
famous_examples|A Celebrated Apiary Examined|What can one successful apiary actually demonstrate?|Define climate, colony count, forage, management, costs, and outcome measure.
hidden_stories|Work Behind Honey and Pollination|Whose labor supports a managed bee operation?|Trace seasonal workers, queen breeders, transport crews, inspectors, and growers.
beginner_explainers|What an Apiary Needs|Which obligations arise before someone keeps bees in one locality?|Check current registration, neighbors, forage, water, disease oversight, and training.
advanced_concepts|Colony Health Has Multiple Causes|How do parasites, pathogens, forage, pesticides, and management interact?|Separate measured exposure from a demonstrated cause in a defined study.
mysteries_unsolved_cases|A Colony Loss Investigation|What can records establish about one unusual loss episode?|Review inspection, mite counts, treatments, weather, forage, and uncertainty.
technology_innovation|A Hive Monitor Tested|Does one monitoring device improve decisions or colony outcomes?|Compare sensor accuracy, intervention timing, cost, and field validation.
people_personalities|A Beekeeper's Decision|How did one beekeeper or researcher change local practice?|Use dated records, adoption evidence, dissent, and measured outcomes.
major_events|A Disease or Pest Arrival|How did one documented pest arrival alter beekeeping?|Trace surveillance, spread, policy response, and management costs.
how_it_works|Inside a Managed Colony|How do colony roles and seasonal cycles affect an apiary?|Explain brood, forage, reproduction, and management without universalizing timing.
rise_fall|What Colony Counts Conceal|Did a change in hive numbers reflect healthy populations?|Compare additions, splits, losses, replacements, and reporting coverage.
then_vs_now|An Apiary Across Two Eras|How have hive care, costs, and pollination contracts changed?|Use comparable records, region, season, and operation size.
future_developments|Scenarios for Managed Bees|Which changes could reshape one apiary's viability?|State assumptions about forage, climate, pests, crop demand, and regulation.
myths_vs_facts|Are More Hives Always Better for Nature?|When might adding managed bees help crops but pressure wild pollinators?|Define place, floral resources, native species, and quality of evidence.
documentary_stories|One Pollination Season|How do growers and beekeepers coordinate a documented crop season?|Trace contracts, movement, bloom, colony condition, and consented accounts.
observation_to_explanation|Dead Bees at an Entrance|What can a visible symptom establish about colony loss?|Compare inspection findings, baseline mortality, timing, and alternative causes.
measurement_method|Counting Colony Loss|How do surveys define and measure lost colonies?|Check denominator, reporting period, replacement, sampling, and uncertainty.
scale_and_timespan|Hive Health at Which Scale?|Can one apiary's losses explain a regional trend?|Compare colony, operation, landscape, and multi-year measures.
field_vs_lab|A Treatment in Lab and Apiary|Does a laboratory result hold under field conditions?|Compare dose, hive conditions, mite pressure, duration, and side effects.
natural_variation|The Normal Seasonal Cycle|Which colony changes reflect season rather than crisis?|Use local climate, forage, brood, and multi-year baselines.
mechanism_chain|From Mite to Colony Loss|What evidence links a parasite, pathogen, and colony-level outcome?|Trace exposure, infection, timing, competing stressors, and intervention.
extreme_case|An Unusually High Loss Report|How was a reported loss calculated and verified?|Check sampled operations, definitions, period, uncertainty, and exclusions.
classification_debate|What Counts as Colony Collapse?|How does a specific loss diagnosis differ from other hive losses?|Compare case definitions, field signs, and available diagnostic evidence.
interacting_systems|Bees, Crops, and Wild Habitat|How do managed pollination and landscape change affect each other?|Trace crop demand, floral resources, pesticide exposure, and wild pollinators.
data_gap|What Apiary Records Miss|Which missing measurements limit a colony-health claim?|Check unreported small operations, treatment data, forage, and pathogen tests.
prediction_test|Did a Health Forecast Hold?|Did a proposed risk indicator predict subsequent colony outcomes?|Match forecast date, sample, season, intervention, and measured loss.
human_impact|Costs of Keeping Colonies Alive|Who bears the costs of pollination and health management?|Compare beekeeper, grower, worker, consumer, and ecological effects.
field_land_stewardship|Forage Beyond the Hive|How does land management influence food available to bees?|Use floral surveys, mowing and planting records, pesticides, and seasons.
field_seasonal_conditions|A Hive Through the Year|Which seasonal conditions change an apiary's needs?|Specify region and compare bloom, temperature, stores, mites, and inspection.
field_skill_and_safety|Working Around a Hive|What training and safety planning does one apiary require?|Check local rules, protective practice, incident response, and nearby public use.
field_resource_use|Honey, Wax, and Colony Reserves|How are harvested products balanced against colony needs?|Compare harvest records, feed inputs, winter outcomes, and operation goals.
field_local_knowledge|What Beekeepers Notice First|Which local observation improves a formal monitoring question?|Attribute consented experience and test against inspection and survey data.
"""


if __name__ == "__main__":
    revise_domain("192", "192_beekeeping", BEEKEEPING,
                  "Beekeeping through managed colony health, pollination work, land use, measurement, labor, and economic trade-offs.",
                  "current local apiary rules, agriculture surveys, colony inspections, pest and pathogen studies, forage records, contracts, and consented beekeeper and grower accounts",
                  "Name species, region, operation type, season, and date. Distinguish managed honey bees from wild pollinators and colony counts from health; verify treatment and safety guidance with current local authorities.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
