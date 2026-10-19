"""Editorial questions for mountain systems and adventure sports."""

from review_angle_plans import audit, revise_domain


MOUNTAINS = """history_origins|How a Mountain Range Formed|Which geological evidence explains one range's formation?|Compare rock ages, structures, uplift estimates, and competing models.
famous_examples|A Famous Peak in Context|What does one well-known summit reveal about a wider mountain system?|Compare geology, ecology, access, and community meaning without treating it as typical.
hidden_stories|Lives Beyond the Summit|Whose farming, guiding, herding, or care work disappears from mountain narratives?|Use consented local accounts and livelihood records.
beginner_explainers|Why Elevation Changes Conditions|How do temperature, pressure, water, and habitats vary up one slope?|Use a named transect and actual observations, not a universal lapse rate.
advanced_concepts|Uplift and Erosion Together|Why can a mountain rise tectonically while its surface lowers?|Separate rock uplift, surface elevation, erosion, and measurement periods.
mysteries_unsolved_cases|A Slope Failure Under Review|Which evidence explains one documented landslide?|Compare geology, rainfall, land change, shaking, and uncertainty.
technology_innovation|Watching a Moving Mountain|Did satellite or ground sensors improve understanding of one slope?|Compare resolution, ground checks, lead time, and false alarms.
people_personalities|Who Mapped the Mountain?|How did local knowledge and scientific teams shape one mapping effort?|Credit guides, residents, surveyors, and named researchers.
major_events|A Glacier Lake Flood|How did one documented event unfold from source to downstream impact?|Use dated monitoring and official investigations; avoid attributing a single cause prematurely.
how_it_works|Snow to Downstream River|Which processes govern water leaving one mountain basin?|Trace precipitation, snowpack, melt, storage, and withdrawals.
rise_fall|A Glacier's Retreat|What observations show change in one glacier over time?|Compare mapped extent, mass balance, climate, and survey methods.
then_vs_now|One Valley Across Decades|How did vegetation, snow, land use, and livelihoods change?|Use comparable seasons and maps with resident accounts.
future_developments|Planning for a Changing Slope|What evidence would guide one mountain adaptation choice?|Compare hazard scenarios, exposure, local priorities, and maintenance needs.
myths_vs_facts|The Stable Mountain Myth|Does a quiet-looking slope imply low hazard?|Use landform history, monitoring, and exposure rather than appearance.
documentary_stories|A Mountain Decision in Records|How did a road, dam, or protected-area project change a valley?|Build a timeline of plans, consent, construction, impacts, and revisions.
observation_to_explanation|An Unusual Snow Line|Which evidence explains snow at a different elevation this year?|Compare storm timing, temperature, aspect, wind, and observations.
measurement_method|Measuring Mountain Change|How do elevation and glacier measurements differ across methods?|Compare instruments, reference surfaces, dates, and uncertainty.
scale_and_timespan|Weather Versus Mountain Climate|Can one season establish a long-term highland trend?|Use multi-decade records and distinguish elevation bands.
field_vs_lab|Rock Tests and Whole Slopes|Can a laboratory rock result predict a real slope's stability?|Compare joints, water, scale, and field observations without safety claims.
natural_variation|Two Sides of One Mountain|Why do nearby slopes support different vegetation and snow?|Compare aspect, exposure, soils, water, and land use.
mechanism_chain|Warming to Mountain Hazard|Which links connect a warming trend to one local hazard?|Test ice, permafrost, rainfall, and exposure separately.
extreme_case|An Exceptional Mountain Storm|What made one storm's impacts severe?|Compare rainfall, terrain, drainage, settlement, and preparedness.
classification_debate|What Counts as a Mountain?|How do elevation, relief, and local use yield different mountain boundaries?|Compare mapped definitions and consequences for data or policy.
interacting_systems|A Mountain Watershed|How do forests, snow, roads, and farms interact in one basin?|Trace flows and decisions through a defined catchment.
data_gap|The Empty High-Altitude Record|Which monitoring gaps weaken a claim about a mountain region?|Map stations, elevation bias, missing years, and local observations.
prediction_test|Did a Hazard Map Identify Risk?|How did one published map compare with later events?|Assess forecast scope, exposure, false negatives, and changed land use.
human_impact|Who Bears Mountain Risk?|How do hazard and resource changes affect different valley communities?|Compare tenure, access, infrastructure, and local accounts.
field_field_sampling|Sampling Along Elevation|How should a mountain transect capture ecological change?|Document sites, aspect, season, access limits, and repeatability.
field_land_use|A Road Across a Slope|How did construction change drainage, habitat, and local travel?|Compare plans, monitoring, maintenance, and residents' reports.
field_weather_variability|Microclimate on One Slope|How much do weather conditions vary with aspect and elevation?|Use calibrated stations and matched observation periods.
field_habitat_change|Species Moving Upslope|Is a measured range shift visible for one species?|Check detection methods, land use, climate, and barriers.
field_restoration_evidence|Repairing a Mountain Landscape|Did one restoration effort reduce erosion or improve habitat?|Compare baseline, control sites where possible, and long-term upkeep."""


ADVENTURE = """history_origins|How an Adventure Sport Developed|Which communities and technologies shaped one sport's early practice?|Trace dated clubs, routes, rules, equipment, and local guides.
famous_examples|A Celebrated Expedition Revisited|What does one famous achievement reveal about preparation and support?|Credit local teams, conditions, decisions, and documented outcome.
hidden_stories|The Support Team Behind the Record|Whose route work, transport, rescue, and maintenance is omitted?|Use consented accounts and employment or event records.
beginner_explainers|What Makes the Activity Demanding?|Which physical, environmental, and judgment demands define one sport?|Explain risk categories without teaching hazardous maneuvers.
advanced_concepts|Risk, Exposure, and Skill|Why do the same conditions carry different risk for different participants?|Compare training, equipment, exposure, and supervision with uncertainty.
mysteries_unsolved_cases|An Incident With Uncertain Causes|Which factors are established and which remain unknown in one incident?|Use official or peer-reviewed reports, avoiding blame and actionable failure sequences.
technology_innovation|A Safety Tool's Limits|Did a new device change outcomes in one activity?|Compare certification, field performance, user training, and residual risk.
people_personalities|A Guide's Decision|What evidence and alternatives did a guide have at one turning point?|Use dated records and participant accounts without hindsight certainty.
major_events|After an Event Was Interrupted|How did organizers change practices following one documented disruption?|Track investigation, recommendations, implementation, and remaining limits.
how_it_works|How an Event Manages Risk|Which planning layers protect participants and bystanders?|Describe governance, screening, weather monitoring, and response at a high level.
rise_fall|A Route or Event Loses Use|Why did participation decline or return in one place?|Compare access, environmental change, cost, rules, and local priorities.
then_vs_now|One Sport Across Generations|How did equipment, rules, access, and safety culture change?|Compare dated standards and participation records.
future_developments|A Proposed Adventure Venue|What evidence would justify opening a new route or event?|Assess ecological impact, land rights, rescue capacity, access, and oversight.
myths_vs_facts|The Invincible Equipment Claim|Does certified gear eliminate the relevant risk?|Compare standard scope, compatible use, inspection, and incident evidence.
documentary_stories|A Competition or Expedition Timeline|What decisions shaped one documented event from planning to finish?|Use official records and participants' accounts; protect sensitive locations.
map_vs_ground|The Route on Paper and in Reality|How did actual terrain differ from one route's published description?|Compare maps, conditions, access rules, and dated observations without instructions.
route_choices|Why This Course Was Chosen|How did organizers balance challenge, safety, ecology, and access?|Compare proposed courses, permits, and local consultation.
seasonality|A Sport Across Seasons|How do conditions and permitted access change over a year?|Use local records and avoid implying a universally safe season.
local_voice|Residents Near the Event|How do nearby communities experience one adventure event?|Include jobs, closures, noise, land use, and consented perspectives.
landscape_process|Terrain That Changes|How do erosion, snow, water, or fire alter a venue over time?|Use monitoring and management records, not route-finding advice.
accessibility|Who Can Participate?|Which cost, design, transport, or qualification barriers shape access?|Compare facilities, adaptive programs, and participant perspectives.
infrastructure|The Support a Venue Needs|What public and private services make one event feasible?|Examine transport, communications, sanitation, emergency capacity, and maintenance.
environmental_pressure|Impact of Repeated Use|What measurable habitat or trail effects followed growth in one activity?|Compare baseline, use intensity, mitigation, and recovery.
safety_decision|When an Event Is Postponed|What documented criteria and authority governed one postponement?|Examine public policy and decision record without tactical thresholds.
place_history|Before It Became a Destination|What land uses and community relationships predated one sport venue?|Use maps, tenure records, and local accounts.
comparison_of_places|Two Venues, One Sport|Why do participant experience and impacts differ between venues?|Compare terrain, governance, access, safety systems, and ecology.
responsible_access|Managing Shared Land|How does one access rule balance recreation with community and habitat needs?|Compare permits, closures, participation, and monitored effects.
field_training_method|Evidence for Training|What outcomes support one supervised preparation program?|Compare participants, progression, injury reporting, and limitations.
field_equipment_design|What a Safety Standard Tests|Which failure modes does one equipment standard cover and omit?|Use published certification scope and independent tests without setup instructions.
field_rules_and_fairness|A Rule That Changed Competition|Did one rule alter fairness or participation?|Compare results, compliance, and athlete and organizer views.
field_injury_prevention|Reducing an Injury Pattern|Which intervention lowered a documented injury type?|Compare exposure-adjusted rates and study limits; defer personal advice to professionals.
field_event_logistics|An Event's Operational Footprint|How did transport, waste, and staffing affect one event?|Measure arrivals, resource use, worker conditions, and local impacts."""


if __name__ == "__main__":
    revise_domain("116", "116_mountains", MOUNTAINS,
                  "Mountain systems through geology, climate, water, habitats, hazards, livelihoods, land use, and local knowledge.",
                  "dated geological and climate observations, glacier and hydrology measurements, land-use and hazard records, field ecology, and consented community accounts",
                  "Name range, valley, elevation band, season, and period. Distinguish physical hazard from human exposure, respect local knowledge and land rights, and avoid route or hazard advice.")
    revise_domain("117", "117_adventure_extreme_sports", ADVENTURE,
                  "Adventure sports through participants, trained support, venues, equipment standards, event governance, inclusion, and environmental impact.",
                  "dated event and incident reports, current governing-body and equipment standards, participation and injury data, land-management records, and attributed local accounts",
                  "Name sport, venue, rules, jurisdiction, and date. Avoid actionable hazardous techniques, treat incident causes carefully, and verify current safety guidance and permissions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
