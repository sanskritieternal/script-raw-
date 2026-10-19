"""Editorial question designs for wind, hydro, and fusion energy."""

from review_angle_plans import audit, revise_domain


WIND = """history_origins|A Wind Farm Sited|Which wind resource, land, and grid factors shaped one project?|Use dated measurements and permitting records.
famous_examples|A Wind Project Rechecked|What does metered output show against forecast?|State turbine model, site, and period.
hidden_stories|People around a Wind Project|Whose land, labor, or wildlife concerns were omitted?|Use attributed local accounts and monitoring.
beginner_explainers|Wind to Grid Electricity|How do rotor, drivetrain, generator, and inverter connect?|Follow one turbine design.
advanced_concepts|Wake Losses across a Farm|How do turbine spacing and wind direction change output?|Compare model with site measurements.
mysteries_unsolved_cases|A Wind Yield Shortfall|Which wind, outage, curtailment, or wake factor explains it?|Use time-series weather and plant logs.
technology_innovation|A New Turbine Feature|Did blade or control changes improve annual output?|Compare matched sites and maintenance costs.
people_personalities|A Siting Decision|Who selected a location and who participated?|Trace public review and land agreements.
major_events|A Wind Project Connects|What generation and grid behavior followed commissioning?|Compare forecast and first-year records.
how_it_works|Wind Output over a Day|How do wind speed, direction, controls, and grid limits interact?|Use measured interval data.
rise_fall|A Wind Farm Repowered|Why were turbines replaced rather than repaired?|Compare output, cost, permits, and wildlife effects.
then_vs_now|Two Turbine Generations|What changed in annual yield, reliability, and materials?|Align wind resource and period.
future_developments|A Proposed Wind Design|Which tests and field years would support its claims?|Treat projection separately from deployed evidence.
myths_vs_facts|Turbines Always Generate?|How much does a named farm actually produce across a year?|Use net meter, outages, and curtailment.
documentary_stories|A Wind Project's Record|How did resource study, siting, build, and operation differ?|Trace dated filings and output.
system_boundary|Turbine or Wind Plant?|Which losses sit in wake, wiring, availability, and transmission?|Define energy meter boundary.
input_output_trace|Wind through Rotor to Meter|Where does captured energy go?|Use wind and electrical measurements.
design_tradeoff|Larger Rotor, New Constraints|What output gains and transport or material costs followed?|Compare equal-site scenarios.
failure_mode|A Documented Turbine Fault|Which part and operating conditions caused loss?|Use inspection and service records.
testing_limits|Power Curve versus Annual Energy|Why can certified curve differ from site yield?|Check wind distribution, turbulence, and downtime.
standards_interoperability|Turbine and Grid Rules|Which test and interconnection standards apply?|Name model, location, and edition.
security_threat_model|Wind Plant Control Access|What public controls protect remote monitoring and updates?|Avoid exploitable configuration detail.
maintenance_lifecycle|Blades and Drivetrain over Time|Which failures shape service and replacement?|Use fleet and site records.
infrastructure_dependencies|Wind and Transmission|Which road, port, grid, and storage limits affect output?|Map one project.
accessibility_usability|Community Participation|Who could see and challenge project evidence?|Check notices, language, and timing.
independent_replication|Recalculate Capacity Factor|Can another analyst reproduce a reported figure?|Match net output, rated capacity, and period.
responsible_deployment|Monitoring after Wind Siting|Which wildlife, noise, and land commitments were followed?|Compare permit and measured outcomes.
field_energy_balance|Wind Energy Delivered|How does modeled wind energy compare with metered electricity?|State resource data and losses.
field_grid_integration|Wind during Grid Constraints|When was output curtailed, and why?|Use operator and plant interval records.
field_material_inputs|Materials in a Turbine|Which steel, concrete, composites, and transport are counted?|Set project lifecycle boundary.
field_operational_safety|Wind Work and Public Safety|Which inspections and incident records apply?|Name site, authority, and period.
field_lifecycle_emissions|Wind Lifecycle Accounting|Which manufacture, construction, operation, and retirement stages matter?|State lifetime and output denominator.
"""

HYDRO = """history_origins|A River Project Chosen|Which power, water, and land goals drove one dam?|Trace dated alternatives and affected communities.
famous_examples|A Hydropower Project in Context|What do generation and river records show?|Specify project, flow period, and license.
hidden_stories|Communities around the Reservoir|Who lost land, fish access, or livelihood?|Use local and licensing evidence.
beginner_explainers|Water to Electricity|How do head, flow, turbine, and generator interact?|Use one project and season.
advanced_concepts|Dispatch under Water Constraints|How do storage, inflow, and environmental flows constrain output?|Compare operations and license conditions.
mysteries_unsolved_cases|An Ecological Change|Which river and land drivers could explain a reported change?|Compare before-and-after and control sites.
technology_innovation|A Turbine or Passage Retrofit|Did it improve power or aquatic outcomes?|Use monitored results, not design intent.
people_personalities|A Dam Licensing Decision|Who weighed generation and river use, and whose claims counted?|Read docket and testimony.
major_events|A Relicensing Decision|Which conditions changed and what monitoring followed?|Compare old and new license terms.
how_it_works|A Dam over a Water Year|How do inflow, storage, release, and power output connect?|Use dated flow and generation series.
rise_fall|A Hydro Project Retires|Why was removal, retrofit, or continued operation chosen?|Compare cost, risk, power, and ecology.
then_vs_now|River before and after a Dam|How did flow, sediment, habitat, and access change?|Use comparable observations and time scales.
future_developments|A Proposed Hydro Project|What flow and community evidence would test its promise?|Treat licensing and forecasts as conditional.
myths_vs_facts|Renewable Means No Impact?|Which downstream and reservoir effects occur at a named project?|Use site monitoring and baseline.
documentary_stories|One Project's License History|How did plans, conditions, and actual operations evolve?|Build dated record and disputes.
system_boundary|Dam or River Basin?|Which effects extend upstream and downstream?|Define reach, season, and other dams.
input_output_trace|Inflow to Grid Output|Where does water pass and energy leave the project?|Use flow, head, spill, and meter records.
design_tradeoff|Storage and River Flow|What generation flexibility costs aquatic habitat or access?|Compare permitted release scenarios.
failure_mode|A Documented Dam Incident|Which sequence and remedy did official review establish?|Avoid operational vulnerability details.
testing_limits|Hydrology Forecast versus Drought|Which water assumptions failed under actual conditions?|Compare recorded inflow and climate variability.
standards_interoperability|License and Water Rights|Which agency and rules govern project operation?|Name jurisdiction, license, and date.
security_threat_model|Dam Service Resilience|Which public oversight covers physical and cyber continuity?|Stay at policy level.
maintenance_lifecycle|Aging Dam and Turbine|Which inspections drive repair or replacement?|Use regulator and owner records.
infrastructure_dependencies|Hydro and Basin Systems|Which irrigation, flood, grid, and fish systems depend on releases?|Map stakeholders and timing.
accessibility_usability|Public River Access|How did the project change access for different groups?|Compare sites, seasons, and rules.
independent_replication|Recheck a Hydro Output Claim|Can another analyst reproduce annual generation per flow?|Match units, period, head, and meter.
responsible_deployment|Monitoring License Commitments|Which fish, sediment, and safety measures were completed?|Compare terms and observed outcomes.
field_energy_balance|Water Potential to Net Power|How do head and flow relate to metered generation?|Account for spill and plant losses.
field_grid_integration|Hydro in Peak Service|What ramp and reserve can a specific project supply?|Use actual dispatch and water constraints.
field_material_inputs|Materials and Land|Which concrete, steel, inundation, and maintenance inputs count?|Set project lifecycle boundary.
field_operational_safety|Dam Safety Record|Which inspections and remedial actions apply?|Name project and oversight period.
field_lifecycle_emissions|Hydro Emissions Boundary|Which construction and reservoir emissions are included?|State basin, climate, lifetime, and output.
"""

FUSION = """history_origins|A Fusion Approach Developed|Which physics and engineering constraint drove one design?|Trace dated experiments and publications.
famous_examples|A Fusion Milestone Examined|What exactly was measured in a celebrated result?|State device, pulse, and energy-gain definition.
hidden_stories|Teams behind the Experiment|Which technicians and materials specialists made a result possible?|Use credited lab and facility records.
beginner_explainers|Fusion Energy Boundaries|What is the difference between plasma gain and net electricity?|Follow one experiment's input and output accounting.
advanced_concepts|Confinement and Heat Exhaust|Which measured limits constrain a sustained plasma?|Use peer-reviewed diagnostics and uncertainty.
mysteries_unsolved_cases|A Performance Gap|Which plasma, wall, or measurement effect remains unresolved?|Compare experiments and model assumptions.
technology_innovation|A New Magnet or Target|Which measured improvement matters at facility scale?|Distinguish component test from power plant.
people_personalities|A Program Choice|Who selected a fusion approach and how was it evaluated?|Read program reviews and team credit.
major_events|A Fusion Experiment Result|Which milestone was reached and what remains?|Separate energy gain, repetition, and electricity.
how_it_works|A Fusion Experiment at System Level|How do fuel, confinement, heating, and diagnostics interact?|Use public descriptions without operational settings.
rise_fall|A Fusion Concept Reassessed|Which experimental limits altered support?|Trace publications and funding decisions.
then_vs_now|Two Experimental Generations|What changed in confinement, pulse duration, and material tests?|Align metrics and methods.
future_developments|A Fusion Plant Proposal|Which integrated tests are required before grid supply?|Treat schedules and cost as projections.
myths_vs_facts|Net Energy Claimed|Is gain measured at target, plasma, facility, or grid meter?|State denominator and full boundary.
documentary_stories|One Result's Evidence Trail|How did design, diagnostic, repetition, and review establish a claim?|Use dated experimental reports.
system_boundary|Plasma versus Facility|Which magnets, lasers, pumps, and conversion loads are counted?|Draw an explicit energy boundary.
input_output_trace|Energy through a Fusion Shot|What measured input and output support a gain figure?|Use published units and uncertainty.
design_tradeoff|Performance and Materials|How does stronger confinement affect heat removal and component life?|Compare modeled and tested limits.
failure_mode|A Test Component Fails|What did inspection show about wall or magnet stress?|Use public lab evidence, no build instructions.
testing_limits|One Pulse versus Continuous Power|Which duty-cycle and component questions remain?|Compare experiment with plant requirements.
standards_interoperability|Fusion Regulation and Grid Plans|Which current rules or proposed standards apply?|Name jurisdiction, device, and date.
security_threat_model|Fusion Facility Governance|What public controls protect research and plant systems?|Keep discussion at oversight level.
maintenance_lifecycle|Materials under Neutron Exposure|What evidence supports component service intervals?|Distinguish simulation, test, and field use.
infrastructure_dependencies|Fusion Facility Inputs|Which electricity, cooling, fuel, and grid services are needed?|Quantify where evidence permits.
accessibility_usability|Explaining Fusion Metrics|Can the public compare claims with consistent definitions?|Define gain and measurement limits.
independent_replication|Repeat a Fusion Result|Has a result been reproduced under stated conditions?|Compare diagnostics and published uncertainty.
responsible_deployment|From Lab to Pilot Plant|What safety, waste, and community evidence is required?|Separate proposal from licensed operation.
field_energy_balance|Full Facility Energy|Would converted output exceed all facility electricity input?|Account for auxiliaries and conversion losses.
field_grid_integration|Hypothetical Fusion Generation|What operating evidence would a grid planner need?|Require ramp, outage, net output, and schedule data.
field_material_inputs|Fuel and Components|Which fuel supply, magnets, and shielding materials are quantified?|State conceptual design and lifecycle boundary.
field_operational_safety|Safety Evidence for a Fusion Device|Which tests and regulatory reviews are public?|Name device and scope; avoid blanket claims.
field_lifecycle_emissions|Projected Fusion Footprint|Which construction, fuel, operation, and retirement assumptions drive a model?|Label projection and uncertainty.
"""


if __name__ == "__main__":
    revise_domain("439", "439_wind_energy", WIND,
                  "Wind energy through measured resource and output, turbine reliability, grid limits, wildlife and community effects, and lifecycle inputs.",
                  "DOE wind research, site wind and meter data, operator outage and curtailment logs, permit monitoring, turbine service records, and host-community accounts",
                  "Name site, turbine version, period, and meter boundary. Separate rated power, power-curve tests, annual generation, and ecological observations.")
    revise_domain("440", "440_hydroelectricity", HYDRO,
                  "Hydroelectricity through river flow, turbine output, multi-use water decisions, dam oversight, community effects, and downstream ecology.",
                  "FERC project licenses and inspections, USGS river data, metered generation, flow and sediment records, environmental monitoring, and affected-community testimony",
                  "Name project, regulator, river reach, water year, and license condition. A renewable energy label does not establish ecological neutrality or dam safety.")
    revise_domain("441", "441_fusion_energy", FUSION,
                  "Fusion energy through reproducible experimental measurements, explicit gain boundaries, materials and duty-cycle challenges, and proposed plant evidence.",
                  "IAEA and DOE technical reports, peer-reviewed experiments, published diagnostics and uncertainty, component tests, and public regulatory and grid studies",
                  "Name device, experiment, date, and energy denominator. Distinguish plasma or target gain from net facility electricity and commercial delivery; omit operational build instructions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
