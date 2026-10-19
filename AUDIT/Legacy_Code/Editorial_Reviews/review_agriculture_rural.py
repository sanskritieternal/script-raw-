"""Editorially revise agriculture and rural-life question designs."""

from review_angle_plans import audit, revise_domain


AGRICULTURE = """history_origins|How a Farming System Emerged|Which records show how one local farming system developed?|Trace crops, land access, tools, and farmers' accounts across a defined period.
famous_examples|A Model Farm Under Scrutiny|Which results made one farm widely cited, and are they transferable?|Compare measured yields, costs, inputs, weather, and neighboring farms.
hidden_stories|The Work Behind a Harvest|Whose labor and land rights are missing from a crop success story?|Use wage, tenure, and producer records with attributed worker accounts.
beginner_explainers|Following a Crop Season|What must happen between soil preparation and harvest for one crop?|Explain stages for a named location and season without prescribing farm practice.
advanced_concepts|Yield Is Not the Only Outcome|How do yield, soil condition, cost, and risk change under one practice?|Compare matched sites and times; state measurement uncertainty.
mysteries_unsolved_cases|Why Did the Harvest Fail?|Which candidate causes fit the evidence from one poor harvest?|Test weather, pests, inputs, timing, and market decisions without assuming one cause.
technology_innovation|A Tool Enters the Field|How did one agricultural tool affect labor, water use, or output?|Compare actual adoption data and maintenance demands across farm sizes.
people_personalities|Who Developed This Practice?|Which farmers, researchers, and workers shaped one farming method?|Trace dated contributions and avoid a lone inventor story.
major_events|A Drought and the Farm System|How did one documented dry season affect farm decisions and income?|Compare rainfall, water access, planting choices, and household outcomes.
how_it_works|Soil, Water, and Crop|Which interactions explain a crop's performance on one field?|Map soil properties, water, nutrients, and management with measured evidence.
rise_fall|Why a Crop Lost Ground|Why did farmers in one region reduce a once common crop?|Compare prices, water, pests, policy, and farmer choices over time.
then_vs_now|One Farm Across Generations|What changed in land use, inputs, labor, and returns?|Use comparable records and farmer accounts from two dated periods.
future_developments|Testing a Farming Proposal|What evidence would show whether a proposed practice works locally?|Specify baseline, outcomes, trial length, costs, and uncertainty before claims.
myths_vs_facts|One Farming Claim Checked|Does a popular claim about a crop or practice hold in a defined setting?|Compare field trials, conditions, and possible tradeoffs.
documentary_stories|A Season in Records and Voices|How did one farm respond to a documented season's constraints?|Combine weather, input, sale, and farmer records in a dated timeline.
observation_to_explanation|From Yellow Leaves to Cause|Which observations distinguish likely causes of one crop symptom?|Compare field observations with relevant testing and expert limits.
measurement_method|How Is Yield Measured?|Can two yield reports be compared fairly?|Check area, crop moisture, harvest losses, sampling, and dates.
scale_and_timespan|A Result Beyond the Trial Plot|Does a short plot trial predict farm or landscape outcomes?|Separate field size, season variability, and long-term soil effects.
field_vs_lab|Lab Finding Meets the Field|Does a promising lab result persist under real farm conditions?|Compare materials, climate, management, and measured outcomes.
natural_variation|Why Neighboring Fields Differ|How much variation exists without changing the intervention?|Use soil, slope, rainfall, and repeated observations across fields.
mechanism_chain|Tracing a Soil Practice|Which steps link one soil practice to crop performance?|Identify measured intermediate changes and alternative pathways.
extreme_case|A Farm in an Extreme Season|Which parts of a farming system held up under unusually harsh conditions?|Define the extreme event and compare yields, losses, and recovery.
classification_debate|What Counts as Regenerative?|How do competing definitions change which farms qualify for a label?|Compare stated criteria, measurements, and certification boundaries.
interacting_systems|Crop and Livestock Together|What changes when crop and livestock systems share land and resources?|Track feed, manure, labor, water, and disease safeguards in one case.
data_gap|The Missing Farm Records|Which missing data prevent a sound comparison of two practices?|Identify absent baselines, cost records, weather series, or representative farms.
prediction_test|Did the Forecast Help?|How accurately did one seasonal forecast guide a farm decision?|Compare forecast probability, actual weather, decisions, and losses.
human_impact|Who Bears the Farm Risk?|How are gains and losses from one agricultural change distributed?|Compare landholders, tenants, laborers, consumers, and local ecology.
field_land_stewardship|Stewardship on One Holding|How does a farm track soil and water condition over time?|Review consistent measurements, land tenure, and farmer priorities.
field_seasonal_conditions|Timing the Work|How did observed seasonal conditions alter one farm's schedule?|Use local weather and field logs rather than generic calendar rules.
field_skill_and_safety|Skill in Farm Work|What knowledge and safeguards does one farm task require?|Observe trained workers and applicable safety standards without hazardous instructions.
field_resource_use|Accounting for Inputs|How much land, water, energy, and labor does one crop system use?|Set system boundaries and compare measured inputs per relevant output.
field_local_knowledge|Farmers' Explanations Tested|How do local farmers interpret a recurring field problem?|Document consented accounts and compare them with observations, without erasing local expertise."""


RURAL = """history_origins|How a Village Took Shape|Which records explain the formation of one rural settlement?|Compare land, migration, ecology, and oral histories within a dated boundary.
famous_examples|A Model Village in Context|Does a celebrated village represent surrounding communities?|Compare infrastructure, livelihoods, governance, and who defined success.
hidden_stories|The Unrecorded Rural Workers|Whose labor sustained one village institution but went uncredited?|Use local accounts, wage records, and material traces where available.
beginner_explainers|How a Village Organizes Daily Life|Which shared arrangements shape daily life in one village?|Map water, transport, work, care, and governance with residents' accounts.
advanced_concepts|Many Rural Economies|How do farming, wages, remittances, and services interact in one place?|Compare household sources and seasonal changes without treating residents alike.
mysteries_unsolved_cases|A Disputed Village Origin|Which parts of a settlement's origin story can be verified?|Compare archives, archaeology where appropriate, and attributed oral accounts.
technology_innovation|A Rural Service Arrives|What changed when one village gained a new service or connection?|Compare access, costs, maintenance, and exclusion before and after.
people_personalities|Who Held Community Knowledge?|How did named residents transmit a local skill, language, or practice?|Use consented interviews and recognize multiple teachers and lineages.
major_events|A Village at a Turning Point|How did one flood, land reform, migration wave, or road affect residents?|Trace dated decisions and different household experiences.
how_it_works|How a Local Institution Functions|Who makes decisions in one village association or council?|Examine actual rules, meetings, resources, and resident access.
rise_fall|A Service Lost or Restored|Why did one rural school, market, or transport route decline or return?|Compare funding, use, policy, and resident accounts across dates.
then_vs_now|A Village Across Two Generations|What changed in housing, work, services, and cultural practice?|Use comparable records and resident perspectives without nostalgia.
future_developments|A Rural Proposal Under Review|Who would benefit from a proposed road, water, or digital service?|Compare costs, upkeep, land effects, and community priorities conditionally.
myths_vs_facts|Testing the Self-Sufficient Village Story|How dependent was one village on outside trade and services?|Trace goods, employment, money, and records across a defined period.
documentary_stories|A Year in Village Records|What do records and residents reveal about one year of change?|Combine council, school, market, and consented oral sources in chronology.
source_trail|Where the Village Story Came From|Which source first made a claim about one rural custom?|Follow citations and compare the claim with community accounts.
material_evidence|Reading Everyday Objects|What can one tool, building, or household object show about village life?|Document provenance, use, repair, and limits of inference.
chronology_dispute|When Did This Change Happen?|Why do official dates and residents' timelines differ?|Compare records, memory, definitions of the event, and uncertainty.
ordinary_lives|A Working Day in Context|What can a documented day reveal about one resident's work?|Use consented testimony and time-use evidence without treating one person as typical.
power_and_institutions|Who Could Decide?|How did land, caste, class, gender, or office shape one local decision?|Use context-specific records and affected voices without unsupported generalization.
trade_and_exchange|Beyond the Village Boundary|Which goods, jobs, and relationships connected one village to other places?|Map dated trade and migration links with sources from both ends.
language_and_labels|Who Calls It Rural?|How do official and resident labels differ for one settlement?|Compare census terms, local language, and effects on service eligibility.
maps_and_borders|The Village on Different Maps|Why do administrative and lived boundaries differ?|Compare dated maps, land records, access routes, and residents' descriptions.
conflicting_accounts|One Event, Several Memories|Why do residents remember one local event differently?|Attribute accounts, compare documents, and respect privacy and trauma.
preservation_bias|What Was Never Archived?|Whose village knowledge is absent from institutional records?|Identify archive selection rules and work with community stewards on ethical gaps.
turning_point_test|Did the New Road Change Life?|Which effects followed one rural infrastructure change?|Compare preexisting trends, affected households, and plausible alternative causes.
legacy_and_memory|How a Place Remembers|Which local event is commemorated, and which experiences are left out?|Compare memorials, records, and community perspectives across generations.
field_community_ownership|Who Controls the Story?|What control do residents have over collection and reuse of local histories?|Examine consent, access, credit, and community-led decisions.
field_object_provenance|A Village Object's Journey|How did one object move from use to collection or display?|Trace maker, owner, acquisition, and claims for return where relevant.
field_living_practice|A Practice Still Changing|How do participants maintain and adapt one rural tradition?|Use participant-led observation with consent and avoid freezing the practice in time.
field_conservation_choice|Keeping a Community Place|Which repairs help preserve a meaningful rural site without displacing use?|Compare local priorities, materials, cost, and maintenance capacity.
field_cultural_translation|Explaining a Local Term|What is lost when a village term is translated for outsiders?|Compare speakers' explanations, context, and alternatives before choosing wording."""


if __name__ == "__main__":
    revise_domain("093", "093_agriculture_farming", AGRICULTURE,
                  "Agriculture as a measured and lived system of crops, livestock, land, water, labor, markets, and local knowledge.",
                  "dated farm and weather records, field trials, land and labor records, current agricultural guidance, and attributed producer accounts",
                  "Name crop, farm system, place, season, and comparison. Distinguish trial results from local advice; respect land rights and local knowledge, and verify safety guidance before production.")
    revise_domain("094", "094_rural_life_village_culture", RURAL,
                  "Rural communities through everyday work, local institutions, infrastructure, memory, material culture, and living practices.",
                  "dated local records and maps, census and service data, material provenance, and consented accounts from residents and community stewards",
                  "Name community, place, and period. Avoid a single romantic village portrait; protect private information and seek community participation and consent for living-heritage documentation.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
