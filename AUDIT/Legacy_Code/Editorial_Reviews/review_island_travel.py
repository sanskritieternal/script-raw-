"""Editorial question designs for niche 226, Island Travel."""

from review_angle_plans import audit, revise_domain


ISLAND_TRAVEL = """history_origins|How an Island Became a Destination|Which settlement, transport, and policy changes shaped visitor access?|Use dated maps, ferry or airport records, and resident histories.
famous_examples|A Paradise Image Rechecked|What does a celebrated island itinerary omit?|Examine residents, freshwater, waste, transport, land rights, and seasonal conditions.
hidden_stories|The Work Behind Island Holidays|Whose labor sustains transport, lodging, water, and food?|Trace residents, seasonal workers, crews, and public services.
beginner_explainers|Planning an Island Visit|Which ferry, flight, accommodation, water, and access constraints matter?|Check current operator and local authority information.
advanced_concepts|Visitor Capacity on an Island|How do limited infrastructure and ecosystems constrain visitor numbers?|Compare water, waste, energy, housing, habitat, and resident priorities.
mysteries_unsolved_cases|Why an Island Service Failed|Which factors explain a documented transport or utility disruption?|Test weather, maintenance, supply chains, demand, and governance.
technology_innovation|A New Island Service Tested|Did one booking, desalination, or transport tool improve outcomes?|Compare uptime, cost, energy, access, and residents' needs.
people_personalities|An Island Access Decision|How did one named community or authority shape tourism policy?|Use consultations, rights, plans, objections, and results.
major_events|An Island After a Storm|What changed for visitors and residents after one event?|Trace transport, water, housing, ecology, response, and recovery.
how_it_works|How Supplies Reach an Island|How do passenger and freight links support daily life and visits?|Map schedules, capacity, weather dependency, costs, and alternatives.
rise_fall|An Island's Visitor Trend|Why did arrivals change?|Check counts, season, transport seats, prices, rules, and reporting.
then_vs_now|One Island Across Two Decades|How did access, housing, services, and landscape change?|Compare dated records and consented resident accounts.
future_developments|Scenarios for an Island Destination|Which conditions could reshape travel and life?|State sea level, storms, transport, infrastructure, and local choices.
myths_vs_facts|The Uninhabited Island Claim|Who uses or holds rights in a supposedly empty island?|Check land records, seasonal use, conservation, and local knowledge.
documentary_stories|A Visitor Policy Reconstructed|Why did an island change bookings, fees, or entry?|Trace objectives, public input, implementation, and outcomes.
map_vs_ground|What an Island Map Misses|Which current paths, tides, restrictions, or services differ?|Compare map date, official notices, and local observations.
route_choices|Getting Around an Island|Why do residents and visitors choose different routes or modes?|Compare cost, timetable, accessibility, weather, and purpose.
seasonality|The Island Through the Year|How do storms, tides, holidays, or breeding seasons change visits?|Use local calendar and current access rules.
local_voice|Residents' View of Visitor Growth|How do different islanders describe tourism effects?|Seek consented accounts across livelihoods, tenure, and neighborhoods.
landscape_process|The Island's Moving Shore|Which waves, sediment, reefs, or geology shape one coast?|Use measured shoreline and habitat records.
accessibility|Who Can Reach This Island?|Which transport, booking, price, and facility barriers matter?|Define traveler needs and inspect current alternatives.
infrastructure|The Island Services Visitors Share|How do water, energy, sanitation, and transport capacity hold up?|Compare peak demand, maintenance, outages, and funding.
environmental_pressure|A Visit's Island Footprint|Which impacts are measurable at one destination?|Set boundaries for flights or ferries, water, waste, habitat, and energy.
safety_decision|Current Island Travel Conditions|Which official facts should be checked before departure?|Verify ferry or flight status, weather, access, health notices, and return options.
place_history|Before the Resort Map|Whose settlement, cultural use, and land rights preceded tourism?|Use archives, titles, and consented community history.
comparison_of_places|Two Islands, One Traveler Profile|Why do they differ in access and resource pressure?|Match season, size, transport, water, rules, and visitor demand.
responsible_access|Visitor Limits on an Island|Who benefits and who bears costs from a cap?|Compare resident needs, ecological evidence, equity, business, and enforcement.
field_map_accuracy|Checking an Island Access Map|Does a published map match current routes and permissions?|Check tide, date, ferry landing, sensitive habitat, and official notices.
field_place_names|Island Names and Languages|Which official and locally used names coexist?|Attribute source, language, community use, and contested status.
field_local_history|An Island's Layered Settlement|How did transport, work, and land use change?|Compare dated records with consented local accounts.
field_visitor_access|A Door-to-Island Access Audit|Where does a defined visitor face a barrier?|Check booking, vessel or aircraft, landing, local transport, lodging, and return.
field_landscape_change|A Changing Island Coast|How did shoreline or habitat edges move?|Use comparable maps, tide datum, storms, and field checks.
"""


if __name__ == "__main__":
    revise_domain("226", "226_island_travel", ISLAND_TRAVEL,
                  "Island travel through transport dependence, resident life, limited services, land rights, coastal change, and visitor impacts.",
                  "current ferry and flight and local access notices, service-capacity records, dated visitor counts, shoreline and ecological monitoring, land records, and consented resident accounts",
                  "Name island, jurisdiction, season, operator, and date. Check current transport and weather before practical advice; do not label lived-in or traditionally used land empty or assume visitor spending benefits residents equally.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
