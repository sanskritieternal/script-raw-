"""Editorial question designs for airports, caves, and national parks."""

from review_angle_plans import audit, revise_domain


AIRPORTS = """history_origins|Why an Airport Was Built Here|Which land, route, and political decisions selected one site?|Use dated plans, land records, and competing proposals.
famous_examples|A Model Airport Rechecked|Which service claims hold for a defined traveler?|Compare actual transfers, waits, access, costs, and disruptions.
hidden_stories|Work Behind the Terminal|Which workers keep an airport operating beyond the flight crew?|Trace cleaning, baggage, maintenance, ground handling, and contractors.
beginner_explainers|The Complete Airport Journey|What must happen from ground arrival to boarding?|Map check-in, security, border control where applicable, gate, and assistance.
advanced_concepts|Capacity at the Bottleneck|Why can more gates fail to reduce delay?|Compare runway, airspace, terminal, staffing, and schedule constraints.
mysteries_unsolved_cases|A Persistent Delay Pattern|Which records explain recurrent congestion?|Test weather, schedules, runway use, staffing, and data definitions.
technology_innovation|A Passenger Technology Tested|Did a biometric or self-service system shorten the journey?|Measure errors, queues, consent, privacy, and accessible alternatives.
people_personalities|The Expansion Decision|Who shaped a consequential airport project?|Use board minutes, consultations, alternatives, and outcomes.
major_events|An Airport During Disruption|How did one event change passenger and worker flows?|Build a dated timeline from airport and authority records.
how_it_works|Airside and Landside Handoffs|Which organizations control each part of a journey?|Trace airport, airline, security, border, and ground transport responsibilities.
rise_fall|Why Passenger Numbers Changed|What explains a measured traffic shift?|Check routes, airline choices, catchment, counting, and shock periods.
then_vs_now|A Terminal Across Two Eras|How did capacity, access, security, and labor change?|Use comparable plans, passenger data, and dated rules.
future_developments|An Airport's Conditional Expansion|Which assumptions determine a proposal's value?|State forecast, noise, land, emissions, finance, and alternatives.
myths_vs_facts|The Fastest Airport Route?|Does a claimed shortcut improve door-to-door time?|Include ground access, queues, terminal distance, and delay risk.
documentary_stories|One Passenger Through the System|What happened at every handoff on a documented journey?|Use consented records and anonymize personal travel data.
map_vs_ground|Terminal Map Versus Actual Transfer|Which stairs, distances, queues, or closures are omitted?|Check current maps and site-specific accessibility information.
route_choices|Two Airports for One Destination|Which complete journey works for a defined traveler?|Compare fare, transfer, time, reliability, assistance, and total cost.
seasonality|An Airport in Peak and Off-Peak Periods|How do queues, staffing, and routes change?|Use dated schedules and comparable passenger counts.
local_voice|Neighbors of an Airport|How do nearby communities describe costs and benefits?|Seek varied accounts and data on jobs, access, noise, and land.
landscape_process|Weather and Airport Siting|Which wind, terrain, or water factors shaped operations?|Use meteorological, topographic, and planning records.
accessibility|Can a Traveler Complete the Transfer?|Where can assistance fail from curb to aircraft?|Verify booking, security, distances, boarding, and alternatives.
infrastructure|What Keeps an Airport Running|Which runway, power, baggage, water, and data systems matter?|Trace maintenance, outages, redundancy, and capacity.
environmental_pressure|An Airport's Local Footprint|How can noise, land, air quality, and energy be measured?|Define boundary, monitoring period, flight mix, and affected residents.
safety_decision|Current Airport Disruption Information|Which live notices matter before travel?|Check airport, airline, authority, and ground transport updates.
place_history|The Land Before the Airport|Who used the site before acquisition?|Use land records, maps, and affected community histories.
comparison_of_places|Two Airports, Different Access|Why does a terminal serve its region differently?|Compare catchment, transit, cost, accessibility, and schedules.
responsible_access|Shared Airport Space|How do passenger practices affect workers and others?|Use current rules and worker perspectives on queues and assistance.
field_service_handoff|A Missed Assistance Request|Where did information stop between airline and airport?|Trace a consented case, timestamps, and responsibility boundaries.
field_visitor_flow|Where Queues Form|Which node limits throughput at a defined hour?|Measure arrivals, processing, staffing, and accessible lane use.
field_staff_labor|One Ground-Handling Shift|How does workload change with flight peaks?|Use consented schedules, staffing, delays, and safety records.
field_access_and_cost|The Usable Airport Trip's Price|What does a traveler pay to reach and use a flight?|Include ground transport, baggage, assistance, fees, and disruption.
field_local_impact|Benefits and Burdens Nearby|Who gains employment and who faces airport impacts?|Compare local hiring, procurement, noise, transport, and land data.
"""

CAVES = """history_origins|How a Cave Became Known|What evidence documents discovery, use, and later mapping?|Distinguish long-standing local knowledge from named exploration records.
famous_examples|A Celebrated Cave Rechecked|What does one famous cave illustrate and what is exceptional?|Compare geology, access, conservation, and source dates.
hidden_stories|People Missing from Cave History|Whose knowledge or labor shaped exploration and protection?|Use attributed community, guide, and survey records.
beginner_explainers|What Makes This a Cave|How did a named void form in its host rock?|Define rock, water or lava process, scale, and evidence.
advanced_concepts|Reading Cave Development|Which features distinguish competing formation sequences?|Use mapped passages, sediments, mineral dates, and uncertainty.
mysteries_unsolved_cases|An Unmapped Passage?|What remains unknown in a documented cave survey?|Separate survey gaps from unsupported hidden-chamber claims.
technology_innovation|A Cave Survey Method Tested|What did one mapping technique reveal or miss?|Compare survey accuracy, access limits, and conservation effects.
people_personalities|A Decision About Cave Access|Who decided whether a cave would open to visitors?|Use management records and affected community views.
major_events|A Closure That Changed a Cave|What documented event altered access or conservation?|Trace dates, evidence, rule changes, and outcomes.
how_it_works|Water, Rock, and Passage|How do processes create and alter one cave system?|Use local geology, hydrology, mapped features, and timescale.
rise_fall|Changing Cave Visitation|What explains a documented rise or decline?|Check counting method, access changes, season, and conservation limits.
then_vs_now|A Cave Across Surveys|What changed between two dated maps?|Separate new discovery from changed measurement or damaged features.
future_developments|Possible Cave Changes|Which physical or management conditions could alter this cave?|State water, climate, visitation, and conservation assumptions.
myths_vs_facts|A Cave Legend Checked|Which parts of a local story have documentary support?|Respect oral tradition while distinguishing genre and evidence.
documentary_stories|A Cave Survey Day|How did a documented survey build a map?|Use field notes and consent; omit sensitive location details.
map_vs_ground|Where a Cave Map Misleads|Which vertical, flooded, or unstable features need other evidence?|Compare survey grade, date, and managed visitor route.
route_choices|The Managed Cave Route|Why does a site offer one route and restrict another?|Use conservation, safety, accessibility, and authority records.
seasonality|A Cave's Seasonal Water|How do rainfall and groundwater change conditions?|Use monitoring series and current site notices.
local_voice|Communities and a Cave Site|How do custodians and nearby residents describe access?|Seek varied, consented views and land-rights context.
landscape_process|The Catchment Above the Cave|How does surface land use affect underground water?|Trace drainage, pollutants, and cave measurements.
accessibility|Can a Visitor Use This Cave Route?|Which slope, steps, width, light, and transport barriers matter?|Verify current managed route for a defined need.
infrastructure|What Protects a Show Cave|How do lighting, paths, monitoring, and staffing affect the site?|Trace maintenance and ecological trade-offs.
environmental_pressure|Visitor Effects Underground|What changes in temperature, carbon dioxide, wildlife, or formations?|Require site baseline, monitoring period, and attribution limits.
safety_decision|Current Cave Access Decision|Which authority notices determine whether a visit is possible?|Check permits, closures, weather, equipment, and managed route.
place_history|Human Use Before Tourism|What evidence shows earlier cave use or stewardship?|Use archaeology and community knowledge with cultural permissions.
comparison_of_places|Two Caves, Different Rules|Why do access policies vary?|Compare geology, ecology, ownership, risk, and community rights.
responsible_access|Why Some Cave Data Stay Private|When could publishing a location damage a site?|Check custodial guidance, wildlife protection, and legal access.
field_map_accuracy|Checking a Cave Survey|How reliable is one passage length or depth?|Name datum, survey grade, date, and measurement method.
field_place_names|Names for a Cave|Who named its passages and what older names exist?|Compare maps, community usage, authority, and translation.
field_local_history|A Cave in Local Memory|How do archival and oral accounts describe its use?|Attribute sources and avoid treating one account as universal.
field_visitor_access|From Entrance to Exit|Where does a managed route become unusable?|Check booking, transport, stairs, lighting, guide support, and exit.
field_landscape_change|A Changing Karst Surface|How does a surface change affect a cave below?|Use dated land, water, and geological records.
"""

NATIONAL_PARKS = """history_origins|How a Park Was Established|Which legal and social decisions created one protected area?|Use designation documents, land histories, and affected voices.
famous_examples|A Celebrated Park Rechecked|Which features explain its reputation and what is overlooked?|Compare conservation goals, access, residents, and visitor pressure.
hidden_stories|Who Stewarded the Land First|Whose knowledge and work preceded park designation?|Use Indigenous and local sources with appropriate attribution.
beginner_explainers|What a National Park Protects|Which values and rules apply to one named park?|Read its legal designation and current management plan.
advanced_concepts|Conservation and Access Trade-offs|How does a park weigh habitat, visitors, and livelihoods?|Compare zoning, ecological measures, rights, and outcomes.
mysteries_unsolved_cases|Why a Species Trend Is Unclear|Which monitoring limits block a firm conclusion?|Check survey method, effort, baseline, and alternative causes.
technology_innovation|A Park Monitoring Tool Tested|Did remote sensing or sensors improve a decision?|Compare ground truth, coverage, cost, and privacy.
people_personalities|A Park Policy Decision|Who shaped one boundary or access rule?|Use minutes, consultations, legal authority, and dissent.
major_events|A Fire, Flood, or Closure|How did one documented event change park management?|Trace impacts, dated notices, response, and recovery.
how_it_works|From Law to Park Practice|How do zoning, staff, permits, and monitoring interact?|Map one park's authority and operational decisions.
rise_fall|Changing Visitor Numbers|What explains a measured use trend?|Check counting method, access, promotion, transport, and season.
then_vs_now|One Park Across Management Plans|What changed in priorities and measured outcomes?|Compare dated plans, budgets, ecological indicators, and rights.
future_developments|A Park Under Future Pressure|Which conditions could change conservation outcomes?|State climate, funding, visitor demand, and land-use scenarios.
myths_vs_facts|Is a Park Untouched Wilderness?|What land use and stewardship preceded designation?|Use archaeology, oral histories, and land records.
documentary_stories|One Management Decision|How did a proposal become a park rule?|Build a sourced timeline including consultation and implementation.
map_vs_ground|Park Boundary Versus Access|What does a map omit about permits, roads, or seasonal closure?|Check current authority maps and on-site conditions.
route_choices|Choosing a Park Visit Route|Which managed route works for a defined visitor?|Compare permitted access, time, habitat limits, and accessibility.
seasonality|A Park Across Seasons|How do ecology, staffing, and access change?|Use dated management notices and monitoring records.
local_voice|Neighbors and Custodians|How do local and Indigenous communities experience the park?|Seek varied attributed views and documented rights.
landscape_process|Why This Landscape Changes|Which fire, river, coast, or glacier process shapes the park?|Use site-specific physical evidence and timescale.
accessibility|Can Visitors Use the Offered Route?|Which transport, path, facility, or information barriers exist?|Verify current route for a defined visitor need.
infrastructure|Services That Support a Park|How do trails, roads, toilets, water, and staff affect protection?|Trace maintenance, capacity, and ecological costs.
environmental_pressure|Measuring Visitor Impact|Which indicator shows use pressure in one area?|Define baseline, visitor counts, habitat measure, and attribution.
safety_decision|Current Park Conditions|Which official notices matter before entry?|Check closures, weather, permits, and emergency information.
place_history|The Land Before Protection|What histories of settlement, use, and displacement shaped this park?|Use land records and community accounts with care.
comparison_of_places|Two Parks, Different Governance|Why do similar landscapes have different management choices?|Compare law, rights, funding, ecology, and visitation.
responsible_access|When Access Needs Limits|How are visitor opportunities balanced with habitat and community rights?|Use management rationale and affected voices.
field_map_accuracy|Testing a Park Map|Which boundary or trail layer is out of date?|Name edition, datum, authority, and ground check.
field_place_names|Whose Names Are on the Map|How have official and community place names changed?|Use naming records and attributed local usage.
field_local_history|A Park Story from Residents|Which local accounts complicate the official history?|Compare oral histories with archives and acknowledge disagreement.
field_visitor_access|A Full Park Visit Audit|Can a defined visitor reach and use the chosen site?|Check booking, transport, path, facility, information, and return.
field_landscape_change|One Measured Habitat Change|What evidence supports a claim that the landscape changed?|Compare matched imagery, field data, date, scale, and causes.
"""


if __name__ == "__main__":
    revise_domain("234", "234_airports", AIRPORTS,
                  "Airports as complete passenger journeys, infrastructure networks, workplaces, and neighboring places.",
                  "dated airport plans and passenger data, airline and authority notices, accessibility information, environmental monitoring, and consented worker and resident accounts",
                  "Name airport, itinerary, jurisdiction, date, and traveler needs. Verify live services and rules with responsible providers; protect passenger and worker data.")
    revise_domain("241", "241_caves", CAVES,
                  "Named caves through formation, mapping, custodianship, managed access, and conservation.",
                  "geological and hydrological studies, dated surveys, site management plans, monitoring, and attributed community accounts",
                  "Name cave and land authority. Respect location-sensitive data, cultural permissions, and current closures; no question is current caving or safety advice.")
    revise_domain("242", "242_national_parks", NATIONAL_PARKS,
                  "Named parks through legal designation, ecological monitoring, land histories, visitor access, and affected communities.",
                  "legal designation and management plans, dated park notices, ecological and visitor data, land records, and attributed local and Indigenous accounts",
                  "Name park, authority, date, and access need. Verify current rules and conditions; do not presume national-park status gives unrestricted access or erases prior rights.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
