"""Editorial questions for mobile and nomadic societies."""

from review_angle_plans import audit, revise_domain


NOMADIC = """history_origins|A Mobile Society's Documented Past|What evidence traces one named community's movement across a region?|Compare oral history, landscape, archaeology, and dated outside records.
famous_examples|A Well-Known Migration Revisited|How did participants explain one seasonal journey?|Use community accounts, routes, ecology, and changing access.
hidden_stories|Work Behind Seasonal Mobility|Whose herding, care, trading, and repair labor enabled movement?|Follow gendered and age-varied roles without fixed stereotypes.
beginner_explainers|What Does Nomadic Mean Here?|Which forms of mobility does one community actually practice?|Distinguish seasonal, pastoral, trading, and forced movement using local terms.
advanced_concepts|Land Rights Without Fixed Residence|How do access and stewardship work across a mobile route?|Trace customary rules, legal recognition, conflicts, and practice.
mysteries_unsolved_cases|An Uncertain Ancient Route|Which evidence supports competing reconstructions of one route?|Compare sites, dates, environmental change, texts, and uncertainty.
technology_innovation|Tools for Moving and Living|How did one transport or shelter design fit local conditions?|Compare materials, maintenance, labor, and practitioner knowledge.
people_personalities|A Leader Within a Mobile Community|How did one documented person make decisions amid collective authority?|Use attributed sources and distinguish individual from group choices.
major_events|A Border That Changed a Route|How did one state boundary or policy affect seasonal movement?|Map old and new access, enforcement, livelihoods, and community response.
how_it_works|Planning a Seasonal Move|What factors shape when and where one community moves?|Use consented accounts, pasture, water, weather, rights, and markets.
rise_fall|A Route Used Less Often|Why did use of one mobility corridor change?|Compare ecology, law, livelihoods, schooling, and alternative routes.
then_vs_now|A Journey Across Generations|How did one route and its meaning change over time?|Compare dated maps, family memories, rules, and present choices.
future_developments|A Proposed Grazing Agreement|Would one policy address practitioners' stated access needs?|Check local authority, ecological data, consultation, and implementation.
myths_vs_facts|Were Mobile Societies Isolated?|What evidence shows one community's exchange with neighbors?|Examine goods, language, marriage, markets, and records.
documentary_stories|One Seasonal Cycle|What does a year's movement reveal about work and decision making?|Follow participants with permission and protect sensitive locations.
source_trail|An Outsider's Description Checked|How did a colonial or state account characterize one community?|Compare author purpose with local testimony and other records.
material_evidence|What a Campsite Reveals|Which activities are visible in one site and which leave little trace?|Use excavation context, dating, and ethnographic caution.
chronology_dispute|Dating a Change in Mobility|When did one community begin using a route or vehicle?|Compare dated evidence, oral histories, and uncertainty.
ordinary_lives|Learning Across a Moving Landscape|How do children and adults learn place knowledge?|Use consented observation and avoid exposing private or sacred sites.
power_and_institutions|A State's View of Mobility|How did taxation, census, or land policy classify mobile people?|Compare law, records, enforcement, and self-description.
trade_and_exchange|A Market Along the Route|How did one mobile community exchange goods and services?|Trace dated markets, prices, routes, and mutual dependence.
language_and_labels|Names for Mobile Peoples|What do self-names and outside labels each imply?|Use speakers' preferred terminology and historical context.
maps_and_borders|A Seasonal Route on Modern Maps|What does a fixed border obscure about movement?|Compare routes, access rights, stops, and maps across periods.
conflicting_accounts|A Disputed Land Story|Why do community and official accounts of one place differ?|Attribute claims, compare evidence, and distinguish law from memory.
preservation_bias|The Archive of Settled Institutions|Why do records show administrators more clearly than mobile residents?|Compare written archives with material traces and oral knowledge.
turning_point_test|Was Settlement a Break?|Did one policy sharply end mobility or reshape it?|Check household-level routes, livelihood mixes, enforcement, and continuity.
legacy_and_memory|A Route Remembered Today|How is one former movement corridor recalled and used?|Use varied consented accounts and current land access evidence.
field_excavation_context|A Site in a Wider Route|What can archaeological context tell us about seasonal use?|Record stratigraphy, dating, environment, and alternative uses.
field_dating_methods|Dating a Mobile Encampment|How precise are the dates assigned to one site?|Explain sample, context, calibration, and range without false precision.
field_urban_life|Mobile People and Towns|How did one community interact with a nearby town?|Trace trade, services, schooling, policy, and periods of residence.
field_trade_routes|A Corridor of Exchange|Which evidence links one route to exchange over time?|Compare goods, sites, texts, ecology, and community memory.
field_writing_systems|Words About a Mobile Society|Whose writing survives and whose voice is absent?|Read inscriptions or documents in context and include oral sources.
"""


if __name__ == "__main__":
    revise_domain("150", "150_nomadic_civilizations", NOMADIC,
                  "Mobile societies through routes, land and water access, livelihoods, exchange, state relations, material evidence, and living knowledge.",
                  "community-approved oral histories, dated archaeological contexts and maps, ecological records, current and historical access rules, and records of trade, schooling, and state administration",
                  "Name community, route, period, and jurisdiction. Use preferred terms, avoid a settled-to-civilized hierarchy, respect sensitive locations and knowledge, and distinguish living practice from archaeological inference.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
