"""Editorial question designs for niche 198, Marine Life."""

from review_angle_plans import audit, revise_domain


MARINE_LIFE = """history_origins|How an Ocean Species Was Documented|Which specimens established one marine organism's identity?|Trace collection site, type specimen, description, and revisions.
famous_examples|A Celebrated Ocean Discovery Rechecked|What does one famous marine find actually establish?|Check identification, depth, location, sampling effort, and later observations.
hidden_stories|The Team Behind a Deep-Sea Sample|Whose work turns an ocean sample into a scientific record?|Trace vessel crew, technicians, local experts, curators, and identifiers.
beginner_explainers|Mapping Marine Life's Variety|How do major marine groups differ in habitat and life cycle?|Use named species and distinguish animals, plants, and microbes.
advanced_concepts|How Much Ocean Life Is Unseen?|Which sampling gaps limit an estimate of marine diversity?|Compare depth, geography, season, equipment, and identification backlog.
mysteries_unsolved_cases|An Organism Found Out of Place|Which explanations fit a verified unusual marine occurrence?|Test misidentification, currents, introduction, range change, and survey effort.
technology_innovation|Environmental DNA at Sea|What can water-sample DNA detect and what remains unproven?|Compare reference library, contamination, transport, timing, and specimen confirmation.
people_personalities|A Marine Taxonomist's Revision|How did one scientist change a species or group classification?|Use specimens, molecular data, dissent, and later tests.
major_events|A Marine Heat Event's Biological Effects|Which changes followed one documented heat event?|Define species, site, baseline, exposure, monitoring, and alternative causes.
how_it_works|A Marine Organism's Life Cycle|How do different stages of one species use the ocean?|Trace reproduction, dispersal, habitat, and survival with stage-specific evidence.
rise_fall|An Ocean Population's Trend|What evidence supports change in one named marine population?|Compare standardized sampling, movement, harvest, environment, and uncertainty.
then_vs_now|One Seafloor Site Across Decades|What can repeat surveys show about community change?|Match depth, transects, seasons, taxonomy, and equipment.
future_developments|Scenarios for a Marine Community|Which changes could alter one site's species mix?|State ocean warming, acidity, oxygen, fishing, and dispersal assumptions.
myths_vs_facts|Is the Deep Sea Empty?|What do specimens and surveys show for a defined deep habitat?|Avoid treating one camera transect as a complete inventory.
documentary_stories|A Specimen's Journey from Sea to Museum|How did a collected organism become evidence?|Trace collection, preservation, identification, catalog, and reanalysis.
observation_to_explanation|One Underwater Image's Limits|What can a photographed animal establish?|Separate occurrence from population size, breeding, and trend.
measurement_method|Surveying Marine Biodiversity|How does one method count or detect organisms in a defined habitat?|Examine transects, gear selectivity, detection, taxonomic resolution, and uncertainty.
scale_and_timespan|A Site Versus an Ocean Basin|At what scale can marine biodiversity findings be generalized?|Define region, depth, season, years, and sampling coverage.
field_vs_lab|A Marine Trait in Natural Water|Does a lab response hold under changing ocean conditions?|Compare temperature, chemistry, food, life stage, and field data.
natural_variation|Seasonal Turnover at Sea|How much change in community composition is normal?|Use multi-year and seasonal observations with consistent methods.
mechanism_chain|From Water Change to Population Effect|What evidence links one ocean condition to organism survival?|Trace exposure, physiology, reproduction, movement, and alternatives.
extreme_case|The Deepest or Largest Record|How was one exceptional marine record verified?|Check depth or size calibration, species ID, specimen, and independent records.
classification_debate|A Marine Species Boundary|Why do morphology and DNA disagree for one organism group?|Compare vouchers, reference sequences, life stages, and geography.
interacting_systems|A Marine Food Web in Evidence|How do prey, predators, and habitat interact at one site?|Use observed diets and abundance, distinguishing correlation from causation.
data_gap|Blank Spots in Ocean Collections|Which depths, regions, or organisms remain poorly sampled?|Map expedition routes, gear reach, specimen backlog, and data access.
prediction_test|Did a Range Model Work?|Did predicted habitat match later verified marine records?|Compare model version, survey effort, dates, and identification.
human_impact|One Human Pressure on Marine Life|How does a defined activity affect a species or community?|Measure exposure, response, recovery, and affected livelihoods.
field_species_variation|Different Forms of One Marine Species|How do age, sex, habitat, and geography change appearance?|Use vouchered specimens and genetics where relevant.
field_ecological_role|What This Marine Species Does|Which feeding or habitat role has been measured?|Separate direct field evidence from inferred ecosystem importance.
field_experimental_model|An Ocean Organism in Research|Which mechanism can one marine model species test?|State laboratory advantage, welfare and habitat context, and transfer limits.
field_evolutionary_history|Tracing an Ocean Lineage|Which fossils and molecular evidence support one relationship?|Compare dating, specimens, and alternative phylogenies.
field_conservation_status|What We Know About One Marine Species' Risk|Which evidence supports its conservation assessment?|Check range, trend, threats, sampling limits, date, and uncertainty.
"""


if __name__ == "__main__":
    revise_domain("198", "198_marine_life", MARINE_LIFE,
                  "Marine life through diverse organism groups, specimen evidence, survey coverage, life histories, food webs, and human pressures.",
                  "vouchered specimens, expedition and survey protocols, verified imagery, environmental DNA with reference data, long-term site monitoring, and species assessments",
                  "Name organism, habitat, depth, region, method, and date. Distinguish detection from abundance and avoid generalizing from a single transect or species to the whole ocean.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
