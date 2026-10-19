"""Editorial question maps for aviation and maritime transport."""

from review_angle_plans import audit, revise_domain


AVIATION = """history_origins|An Air Route Takes Shape|Which aircraft, infrastructure, rules, and demand enabled one early air route?|Compare dated route records, aircraft limits, airports, and the service actually delivered.
famous_examples|A Famous Aircraft Reexamined|What did one celebrated aircraft achieve, and what were its operating limits?|Use a named model and period; compare specifications, service records, and contemporary claims.
hidden_stories|The Work Behind a Flight|Whose ground, maintenance, cabin, or air-traffic work is missing from one flight story?|Use attributed accounts, staffing records, and documented responsibilities.
beginner_explainers|How an Airplane Stays in Flight|How do lift, thrust, weight, and control interact on one aircraft?|Explain a defined flight regime through authoritative diagrams and measured limits, without flying instructions.
advanced_concepts|Range, Payload, and Reserve|How did designers and operators balance range, payload, and safety margins for one aircraft?|Compare design data with documented operating constraints and uncertainty.
mysteries_unsolved_cases|An Aviation Investigation's Open Questions|Which parts of one incident are established, disputed, or still unknown?|Read the responsible investigation's evidence and findings; do not assign blame beyond them.
technology_innovation|An Aircraft Innovation in Service|Did one design change improve its intended performance or safety outcome?|Compare certification evidence, test conditions, service data, and unintended tradeoffs.
people_personalities|A Decision in the Aviation System|What information and authority did a named designer, controller, or crew member have?|Reconstruct one dated decision using records and the constraints known then.
major_events|A Turning Point in Aviation Safety|What changed after one documented accident or major safety event?|Trace investigation findings, recommendations, implementation, and later measurement.
how_it_works|From Schedule to Arrival|Which aircraft, crew, airport, airspace, weather, and maintenance systems support one service?|Map a dated route through public operational records without actionable procedures.
rise_fall|Why an Aircraft Program Changed Course|Why did one aircraft model or route expand, contract, or end?|Compare costs, demand, safety record, regulation, alternatives, and dates.
then_vs_now|Aviation Across Two Eras|How did one route or aircraft role change across two periods?|Compare equivalent measures for capacity, access, emissions, and safety exposure.
future_developments|A Proposed Aviation Change|What evidence would show whether a proposed aircraft or airspace change works?|Specify intended users, test conditions, infrastructure, training, costs, and measurable outcomes.
myths_vs_facts|Checking an Aviation Superlative|Does a familiar first, fastest, or safest claim survive consistent definitions?|Check dates, aircraft class, measurement method, and primary records.
documentary_stories|One Flight Through Its Records|What can the documented sequence of one flight or service launch establish?|Build a sourced timeline with records, attributed accounts, and explicit gaps.
system_boundary|Where the Flight System Begins and Ends|Which risks belong to the aircraft and which depend on airport, airspace, crew, and weather?|Define one operation and map interfaces using public records.
input_output_trace|Fuel, Energy, and Flight Output|How did one aircraft turn fuel or stored energy into a measured transport service?|Trace a defined route's energy, load, distance, and data limits without operating instructions.
design_tradeoff|The Aircraft Design Compromise|What was gained and given up by one wing, engine, or cabin design choice?|Compare original requirements, test results, operating constraints, and alternatives.
failure_mode|A Documented Failure Chain|How did multiple conditions contribute to one investigated aviation occurrence?|Use the official report's causal language, uncertainty, and recommendations.
testing_limits|What a Flight Test Can Prove|Which operating conditions did a certification or flight test cover, and which were outside it?|Read dated test and approval records before comparing with service experience.
standards_interoperability|Aircraft Meets Airspace|How did compatibility between one aircraft, airport, and air-traffic system affect deployment?|Use applicable dated standards and a named jurisdiction, distinguishing requirement from performance.
security_threat_model|Protecting Aviation Systems|Which broad security assumptions shaped one public aviation-system design?|Discuss published policy and resilience outcomes without vulnerabilities or bypass detail.
maintenance_lifecycle|An Aircraft Through Its Service Life|What inspections, repairs, and modifications shaped one fleet's reliability?|Compare public maintenance directives, fleet records, and reported outcomes.
infrastructure_dependencies|The Systems Behind an Airport|Which runway, power, navigation, staffing, and ground systems constrained one service?|Use public plans and performance records without exposing operational weak points.
accessibility_usability|Who Can Use This Air Service?|Which cost, disability access, language, or route barriers affect a defined passenger group?|Compare current service provisions and passenger evidence in a named jurisdiction.
independent_replication|Can an Aircraft Claim Be Reproduced?|Do independent measurements support one advertised range, noise, or efficiency claim?|Match aircraft variant, load, route, weather, and measurement method.
responsible_deployment|Introducing a New Aircraft Safely|What approval, training, support, and monitoring accompanied one aircraft's entry into service?|Compare documented rollout plan, authority findings, and early service evidence.
field_route_capacity|When an Air Route Reaches Capacity|Which airport or airspace constraint limited one route at a dated time?|Compare scheduled demand, slot or runway records, delay measures, and alternatives.
field_vehicle_design|An Aircraft Built for a Particular Job|How did one aircraft's design fit its intended route or mission?|Connect design requirements to test and service evidence, including compromises.
field_maintenance_system|A Maintenance System Under Review|How did one fleet's inspection and repair system detect or miss a problem?|Use public findings and corrective action records; avoid repair instructions.
field_safety_case|The Evidence for an Aviation Safety Claim|Which tests, assumptions, and authority decisions supported one safety claim?|Name aircraft variant and approval date; distinguish evidence from later experience.
field_construction_impact|Building Aviation Infrastructure|How did one airport or production-facility project affect neighboring people and services?|Compare impact assessment, construction records, monitoring, and local accounts."""


MARITIME = """history_origins|A Sea Route Takes Shape|Which vessels, ports, trade demand, and rules enabled one early maritime route?|Use dated voyage, port, cargo, and regulatory records for a bounded period.
famous_examples|A Famous Vessel Reexamined|What did one celebrated ship achieve, and what constraints did it face?|Compare design records, voyages, cargo or passenger figures, and contemporary claims.
hidden_stories|The Labor Behind a Voyage|Whose crew, dock, repair, or shore work is missing from one ship story?|Use attributed testimony, crew lists, port records, and documented conditions.
beginner_explainers|How a Ship Makes a Voyage|How do buoyancy, propulsion, navigation, cargo, and port access work together?|Explain one vessel type and voyage through authoritative diagrams and records, without navigational directions.
advanced_concepts|Stability, Load, and Sea Conditions|How did one vessel's design and loading assumptions constrain its operation?|Compare design documents, loading records where public, conditions, and investigation limits.
mysteries_unsolved_cases|An Unresolved Maritime Loss|Which explanations for one vessel loss are supported by available evidence?|Compare responsible investigation, wreck evidence, weather, and record gaps without speculation as fact.
technology_innovation|A Maritime Innovation in Service|Did one hull, propulsion, or navigation change deliver its promised result?|Compare trials, operating data, costs, and conditions across comparable vessels.
people_personalities|A Maritime Decision in Context|What could a named captain, designer, port official, or crew member know at a turning point?|Use dated records, authority, constraints, and attributed accounts without hindsight blame.
major_events|A Turning Point in Maritime Safety|What changed after one documented casualty or major maritime event?|Trace official findings, recommendations, implementation, and subsequent evidence.
how_it_works|From Port to Port|Which vessel, crew, cargo, pilotage, port, and weather systems shape one voyage?|Map public records for a named voyage without providing navigation or emergency instructions.
rise_fall|A Shipping Service Changes Course|Why did one route, vessel class, or port service grow or decline?|Compare demand, costs, infrastructure, rules, competitors, and dates.
then_vs_now|One Maritime Route Across Eras|How did a defined sea route change in vessel size, time, work, and impact?|Use comparable route boundaries and measures for both periods.
future_developments|A Proposed Maritime Change|What evidence would establish whether a proposed vessel or port change helps?|Specify trial conditions, workforce, fuel or energy, costs, safety, and measured outcomes.
myths_vs_facts|Checking a Maritime Legend|Does a popular first, largest, or unsinkable claim fit the original records?|Define measure, date, vessel class, and the source of the claim.
documentary_stories|One Voyage Through Its Records|What can a vessel's documented journey establish from departure to aftermath?|Build a dated timeline from logs, port records, investigation, and attributed accounts.
system_boundary|Where the Voyage System Begins and Ends|Which outcomes depend on vessel, crew, port, channel, weather, and shore services?|Define one voyage and map public interfaces without weak-point detail.
input_output_trace|Energy, Cargo, and Delivered Service|How much energy and capacity did one vessel use to move a defined load?|Compare dated voyage, fuel or power, distance, and cargo records with measurement limits.
design_tradeoff|The Ship Design Compromise|What did one hull, propulsion, or cargo arrangement gain and sacrifice?|Compare intended service, design requirements, trials, and operational evidence.
failure_mode|A Documented Maritime Failure Chain|How did several conditions combine in one officially investigated casualty?|Follow findings and uncertainty in the responsible investigation; avoid unsupported blame.
testing_limits|What Sea Trials Can Prove|Which conditions did one sea trial or model test cover, and what remained untested?|Compare trial protocol, loading, sea state, and later service evidence.
standards_interoperability|Ship Meets Port and Route|How did a vessel's dimensions or equipment interact with port and navigation requirements?|Use dated public standards and a named route; distinguish compliance from performance.
security_threat_model|Maritime Security at System Level|Which public security assumptions shaped a vessel or port policy?|Explain governance and resilience outcomes without exploitable access details.
maintenance_lifecycle|A Vessel Through Its Service Life|How did survey, repair, and modification affect one vessel or fleet?|Use public inspection and casualty records, noting missing private maintenance data.
infrastructure_dependencies|The Port Behind the Voyage|Which channel, berth, labor, energy, and hinterland links constrained one service?|Compare public capacity plans, throughput, disruptions, and local effects.
accessibility_usability|Who Can Use a Maritime Service?|Which fare, disability access, schedule, or language barriers affect a defined passenger group?|Check current operator provision, jurisdictional rules, and passenger accounts.
independent_replication|Can a Vessel Claim Be Reproduced?|Do independent records support an advertised speed, capacity, or emissions claim?|Match vessel, load, route, weather, and measurement method.
responsible_deployment|A New Vessel Enters Service|What trials, crew preparation, port readiness, and monitoring accompanied deployment?|Compare public approval, rollout plans, and early service evidence.
field_route_capacity|A Sea Route at Its Limit|Which channel, berth, or fleet constraint restricted a dated service?|Compare demand, vessel calls, waiting times, and comparable capacity measures.
field_vehicle_design|A Ship Built for a Particular Route|How did one vessel's hull, draft, and cargo arrangement fit its intended service?|Connect design requirements with sea trials, port limits, and service records.
field_maintenance_system|A Maritime Maintenance System Under Review|How did survey and repair processes detect or miss a documented defect?|Use investigation and corrective-action records without repair instructions.
field_safety_case|The Evidence for a Vessel Safety Claim|Which design assumptions, trials, and approvals supported one safety claim?|Define vessel, route, flag or jurisdiction, and approval date; examine later evidence.
field_construction_impact|Building Ships or Ports|How did one shipbuilding or port project affect workers, neighbors, and the environment?|Compare impact assessment, construction records, measured effects, and local voices."""


if __name__ == "__main__":
    revise_domain("047", "047_aviation", AVIATION,
                  "Aviation through aircraft design, flight services, airports, airspace, maintenance, safety investigation, access, and local effects.",
                  "aircraft design and certification records, official occurrence investigations, public maintenance directives, flight and airport performance data, route records, and attributed worker and passenger accounts",
                  "Name aircraft variant, route, jurisdiction, and date. Distinguish official findings from speculation; avoid pilot or maintenance instructions, security vulnerabilities, and unsupported blame. Check current authority records before production.")
    revise_domain("048", "048_maritime", MARITIME,
                  "Maritime transport through vessel design, voyages, crews, ports, cargo, maintenance, safety investigation, access, and coastal effects.",
                  "vessel design and trial records, official marine casualty investigations, public survey and port records, voyage and cargo data, and attributed crew and community accounts",
                  "Name vessel, route, flag or jurisdiction, and date. Distinguish investigation findings from speculation; avoid navigational or emergency instructions, security vulnerabilities, and unsupported blame. Check current authority notices before production.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
