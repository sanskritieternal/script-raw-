"""Editorial questions for historic buildings and map-based geography."""

from review_angle_plans import audit, revise_domain


CASTLES = """history_origins|Why a Fortified Site Was Built|Which political and geographic conditions led to one castle, fort, or palace?|Compare founding records, site archaeology, and prior land use.
famous_examples|A Landmark Beyond Its Facade|How did one famous fortified or royal building function across its life?|Compare documented building phases, residents, defenses, and later uses.
hidden_stories|Builders and Servants of a Landmark|Whose skilled labor and daily work made one site operate?|Use building accounts, household records, and archaeology.
beginner_explainers|Reading a Historic Building|How can a visitor distinguish original fabric from later additions?|Follow a named site through dated plans, materials, repairs, and interpretation.
advanced_concepts|Defense and Display Together|How did one structure balance protection, administration, and status?|Compare layout, period threats, ceremonies, and actual use.
mysteries_unsolved_cases|An Uncertain Building Phase|Which dates or functions for one surviving feature remain disputed?|Compare masonry, stratigraphy, accounts, and conservation records.
technology_innovation|A Construction Method Changes the Site|What did one new material or technique allow builders to do?|Compare dated phases, costs, performance, and craft evidence.
people_personalities|A Patron and the Building Team|Which design choices can be tied to a named patron or architect?|Use contracts, accounts, correspondence, and later alterations.
major_events|A Siege or Renovation That Altered a Site|What physical and administrative changes followed one documented event?|Compare plans, damage records, accounts, and later restoration.
how_it_works|How a Fort or Palace Operated|Which systems supplied water, food, access, heat, and security?|Map documented rooms and infrastructure for one dated period.
rise_fall|Why a Stronghold Lost Its Role|What changed when one fort or palace ceased its original function?|Compare military, political, maintenance, and local records.
then_vs_now|A Site Across Two Building Phases|What was changed, preserved, or reconstructed between two dated periods?|Use plans, photographs, fabric analysis, and conservation decisions.
future_developments|A Conservation Choice Ahead|Which evidence should guide a proposed restoration or new visitor facility?|Assess fabric, access, cost, community use, and uncertainty conditionally.
myths_vs_facts|A Castle Legend Checked|Does a popular tale about one room, tunnel, or siege fit the evidence?|Trace earliest telling and compare site records and archaeology.
documentary_stories|A Building Through Its Records|How did one site change from construction through current stewardship?|Build a dated account from contracts, maps, repairs, and local voices.
source_trail|Who Wrote the Building Account?|What did one inventory, plan, or chronicle intend to record?|Check author, purpose, date, omissions, and later copying.
material_evidence|Stone and Timber as Documents|What can one wall, joint, or timber reveal about a building phase?|Use dated fabric analysis and avoid assigning a function from appearance alone.
chronology_dispute|Dating an Alteration|Why do sources disagree on when one wing or defense was built?|Compare documentary dates, construction techniques, archaeology, and reuse.
ordinary_lives|Living in the Complex|What can records show about residents, servants, prisoners, or neighbors?|Use household, legal, and local evidence without treating elites as the whole site.
power_and_institutions|Who Controlled the Site?|How did ownership, garrison, court, or civic authority govern one building?|Compare deeds, appointments, budgets, and actual use.
trade_and_exchange|Materials and Money to Build|Where did stone, timber, labor, and funding come from?|Trace contracts, quarries, routes, and affected communities.
language_and_labels|Castle, Fort, or Palace?|Which definitions best describe one site at a given date?|Compare physical design, primary labels, and actual function.
maps_and_borders|A Building in Its Territory|How did a site's location relate to routes, boundaries, and settlements?|Use period maps and ground evidence without projecting modern borders backward.
conflicting_accounts|Two Stories of a Siege|Why do opposing or later accounts describe one event differently?|Compare vantage point, political purpose, archaeology, and dating.
preservation_bias|What Survived and What Did Not|How do demolition and selective restoration distort the site's apparent history?|Identify missing structures, reused materials, and curatorial choices.
turning_point_test|Did a Siege Change the Building?|Which measurable alterations followed a supposed turning point?|Compare fabric, budgets, garrison, and uses before and after.
legacy_and_memory|Who Owns the Site's Story?|How do current communities interpret a former royal or military site?|Use attributed perspectives, heritage policy, and contested memories.
field_strategic_choices|Why This Defensive Position?|What constraints shaped one historic siting choice?|Compare documented threat, terrain, water, routes, and alternative sites.
field_civilian_experience|Neighbors of a Fortification|How did building or garrisoning affect nearby residents?|Use land, tax, market, and personal records where available.
field_logistics|Supplying a Large Site|What quantities and routes sustained one castle or palace?|Read dated accounts and distinguish planned from delivered supplies.
field_leadership_claims|The Named Builder Claim|Was one ruler or commander truly responsible for a structure?|Compare patronage records, prior fabric, team labor, and later myth.
field_aftermath|After the Site Changed Hands|What happened to its buildings, workers, and local community?|Trace records across a bounded post-transfer period."""


MAPS = """history_origins|How a Map Was Made|What observations and purposes shaped one historical map?|Identify maker, patron, survey method, projection, and intended users.
famous_examples|A Famous Map Reexamined|What does one celebrated map show accurately and omit?|Compare its scale, date, coverage, labels, and ground evidence.
hidden_stories|Local Knowledge Behind the Survey|Whose guides, names, or measurements were absorbed without credit?|Use survey notes, community histories, and attributed accounts.
beginner_explainers|Reading Scale and Symbol|How do scale, legend, projection, and date affect a map claim?|Use one map to show what a symbol can and cannot establish.
advanced_concepts|A Projection's Tradeoff|Which spatial relationship is distorted in one map projection?|Compare area, shape, distance, direction, and intended use.
mysteries_unsolved_cases|A Place Missing from the Map|Was one mapped feature real, mislocated, renamed, or copied?|Trace source maps, observations, coordinates, and later surveys.
technology_innovation|A Survey Tool Changes the Map|What did GPS, remote sensing, or another tool improve for one region?|Compare coverage, precision, datum, access, and blind spots.
people_personalities|The Cartographer and the Institution|How did a named mapmaker's assignment shape what was shown?|Use commission, field notes, revisions, and institutional context.
major_events|When a Map Had to Change|What event forced a map's boundary, route, or feature revision?|Compare dated editions with legal and field records.
how_it_works|From Ground Measurement to Map|How did one survey turn observations into a published map?|Trace control points, coordinates, generalization, review, and update.
rise_fall|Why a Map Became Obsolete|Which environmental, political, or technical change undermined one map?|Compare its last update with later verified conditions.
then_vs_now|The Same Place on Two Maps|What changed in the place and what changed only in mapping method?|Align scale, datum, dates, names, and source evidence.
future_developments|A Map Update Proposal|Which new data are needed before one map layer can be revised?|Specify survey method, authority, local consultation, and uncertainty.
myths_vs_facts|A Viral Map Claim Checked|Does a shared map support the political or geographic conclusion drawn from it?|Check source, legend, scale, projection, date, and missing context.
documentary_stories|A Map's Provenance Trail|How did one map move from survey through editions and reuse?|Build a dated record of data sources, changes, and reinterpretation.
map_vs_ground|A Symbol in the Field|Does a mapped road, river, or settlement exist as depicted?|Compare current official data, field observation, access, and date.
route_choices|A Path Chosen by the Map|How did one mapped route compare with the actual journey?|Check terrain, distance, legal access, and route changes.
seasonality|A Feature That Moves or Disappears|How do seasonal water, snow, or vegetation affect a mapped feature?|Use dated imagery and local observations, not a static map alone.
local_voice|Names Used by Residents|How do local place names differ from an official map label?|Attribute language and community preference with consent.
landscape_process|Why a Boundary-Like Feature Shifts|Which natural process changed a riverbank, shoreline, or slope?|Compare repeated surveys and process measurements.
accessibility|Who Can Read or Use the Map?|Does one map serve users with different visual, language, or mobility needs?|Assess symbols, text, digital access, and route information.
infrastructure|Maps for Built Systems|What does a map of transport, utilities, or services leave out?|Compare mapped assets with operator records and actual access.
environmental_pressure|Mapping a Changing Habitat|Can one map show ecological change without confusing survey differences?|Align seasons, methods, classifications, and uncertainty.
safety_decision|When a Map Is Too Old|Which current conditions make a published route map unsafe to rely on?|Check official closures, hazard notices, datum, and update date.
place_history|Earlier Names and Uses|What do maps from different periods reveal about one place's history?|Compare labels with archival and community accounts, noting omissions.
comparison_of_places|Two Maps of the Same Area|Why do maps made for different purposes disagree?|Compare scale, projection, classification, authority, and date.
responsible_access|A Sensitive Site on the Map|Should exact coordinates for a sacred or fragile place be published?|Consult custodians and management rules before disclosure.
field_map_accuracy|A Map Pin Tested|How accurate is one mapped coordinate or elevation?|Check datum, scale, ground control, and stated error.
field_place_names|Choosing a Display Name|How should a map present official, historical, and local names?|Attribute each name, language, date, and jurisdiction.
field_local_history|A Lost Feature in Records|Can an old map's building or route be corroborated?|Compare cadastral, photographic, archaeological, and oral evidence.
field_visitor_access|Access Is Not a Line on a Map|Does a mapped path imply a legal or usable visitor route?|Verify ownership, permits, closures, terrain, and current notices.
field_landscape_change|Change or Cartographic Artifact?|Did a mapped shoreline or settlement actually move?|Compare aligned datasets and independent field evidence."""


if __name__ == "__main__":
    revise_domain("037", "037_castles_forts_palaces", CASTLES,
                  "Historic castles, forts, and palaces through building phases, labor, power, logistics, reuse, conservation, and community memory.",
                  "building accounts and plans, fabric and archaeological surveys, inventories, household and military records, dated maps, conservation reports, and local accounts",
                  "Date each building phase and distinguish original fabric from restoration. Avoid unverified legends or sensitive access details; include builders, residents, and current custodians.")
    revise_domain("038", "038_maps_geography_mysteries", MAPS,
                  "Maps and geographic claims through provenance, scale, projection, names, ground checks, change, and responsible disclosure.",
                  "original map editions and metadata, survey methods and control points, official geospatial datasets, field observations, legal access records, and community place-name accounts",
                  "State map date, scale, projection, datum, and uncertainty. Do not infer legal access from a drawn line or disclose restricted or fragile locations without custodian consent.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
