"""Editorial questions for megastructures and space exploration."""

from review_angle_plans import audit, revise_domain


STRUCTURES = """history_origins|Why a Giant Structure Was Proposed|Which public need and site constraint led to one megastructure proposal?|Compare dated alternatives, requirements, and decision records.
famous_examples|A Landmark Structure Reassessed|What performance did a celebrated bridge, dam, tower, or tunnel actually deliver?|Compare original goals with measured capacity, cost, maintenance, and effects.
hidden_stories|Builders Behind the Landmark|Whose design, construction, and maintenance work is missing from one structure's story?|Use contracts, labor records, credits, and consented accounts.
beginner_explainers|How a Large Structure Carries Load|Where do forces travel through one named structure?|Explain supports, materials, foundations, and operating conditions without design instructions.
advanced_concepts|Modeling a Structure's Risk|Which assumptions most affect one safety or capacity estimate?|Compare loads, material properties, degradation, boundary conditions, and uncertainty.
mysteries_unsolved_cases|An Unexpected Structural Behavior|Which explanations fit one monitored anomaly in a large structure?|Read inspection and instrument records; separate hypothesis from established defect.
technology_innovation|A Construction Method Tested|What constraint did one new method solve on a large project?|Compare schedule, cost, safety, quality, and independent verification.
people_personalities|The Engineer and the Institution|How did one named engineer's choice pass through review and approval?|Use design records, team roles, and institutional decisions.
major_events|A Project at a Turning Point|What event forced a redesign, closure, or change in operation?|Trace dated findings, decisions, and measured effects.
how_it_works|From Requirement to Operation|How does one megastructure move from concept through design, construction, inspection, and use?|Follow a documented project and decision gates.
rise_fall|When a Mega Project Underperformed|Which assumptions explain a gap between promised and observed benefit?|Compare forecasts, actual usage, costs, and alternative causes.
then_vs_now|A Structure Across Its Service Life|How did use, condition, and maintenance change between two dated inspections?|Use comparable measures and account for changed standards.
future_developments|A Proposed Major Expansion|What evidence would justify extending or replacing one structure?|Evaluate conditional demand, safety, cost, land, and environmental impacts.
myths_vs_facts|Checking a Megastructure Superlative|Does a tallest, strongest, or most efficient claim use comparable definitions?|Check dates, boundaries, measurements, and competing records.
documentary_stories|A Structure Through Its Files|How did one project proceed from proposal to current operation?|Build a sourced timeline of plans, contracts, tests, revisions, and public response.
system_boundary|Defining the Whole Facility|Which foundations, utilities, access routes, controls, and users belong in one performance claim?|Draw a case-specific boundary before calculating benefits or risks.
input_output_trace|Resources Into Service|What materials, energy, water, or traffic pass through one large facility?|Use measured flows with time period, losses, and external dependencies.
design_tradeoff|Two Designs, Different Costs|Which safety, capacity, cost, and ecological tradeoffs drove one selection?|Compare alternatives using the same criteria and dated evidence.
failure_mode|A Component's Failure Path|What evidence identifies how one structural element degraded or failed?|Read published investigations and avoid unsupported blame or operational weak-point detail.
testing_limits|What the Tests Missed|Which field conditions were absent from a model or component test?|Compare scale, loading, material variability, and monitoring after opening.
standards_interoperability|Connecting to Existing Networks|How did one structure meet transport, power, water, or building interfaces?|Name applicable versions of standards and documented exceptions.
security_threat_model|Protecting Essential Service|Which publicly documented hazard could interrupt a structure's function?|Discuss resilience and recovery at system level without exploitable details.
maintenance_lifecycle|The Cost of Continued Use|What inspections and repairs kept one structure operating?|Compare condition reports, budgets, closures, and deferred work.
infrastructure_dependencies|A Landmark Needs Lifelines|Which energy, drainage, communications, and access systems must also work?|Map public dependencies and documented outage effects.
accessibility_usability|Who Can Use the Structure?|How do design and operating rules affect users with different mobility or access needs?|Check actual routes, services, and user evidence.
independent_replication|Rechecking a Performance Claim|Can an independent audit reproduce one capacity or benefit estimate?|Compare inputs, methods, assumptions, and observed data.
responsible_deployment|Opening a Structure Safely|What evidence supported commissioning and public use?|Read official approvals, tests, monitoring plan, and known limitations.
field_route_capacity|A Link's Real Throughput|How much traffic or movement did a bridge, tunnel, or station actually carry?|Compare design demand, observed peak and average flows, and bottlenecks.
field_vehicle_design|Design Vehicle or Moving Load|Which vehicle dimensions and loads constrained one transport structure?|Read design basis and current usage, without giving unsafe load advice.
field_maintenance_system|Inspection Becomes Repair|How did an observed defect move through prioritization, funding, and completed work?|Trace inspection and maintenance records for one facility.
field_safety_case|Evidence for Structural Safety|Which tests, inspection findings, and analyses support a public safety claim?|State scope, responsible authority, date, and remaining uncertainty.
field_construction_impact|Costs at the Site|What land, water, emissions, or community changes accompanied one build?|Compare impact assessment, baseline, and observed outcomes."""


SPACEFLIGHT = """history_origins|Why a Mission Was Conceived|Which scientific or operational question drove one space mission?|Compare original objectives, alternatives, and feasibility studies.
famous_examples|A Landmark Mission Reexamined|What did one celebrated mission measure versus what later accounts claim?|Read instrument data, mission reports, and independent analysis.
hidden_stories|The Teams Behind a Spacecraft|Whose engineering, operations, and analysis work is absent from a mission narrative?|Use credited mission roles and attributed accounts.
beginner_explainers|From Launch to Data|How does an uncrewed mission travel, operate instruments, and return results?|Follow one mission's actual sequence and communication limits.
advanced_concepts|A Mission's Design Tradeoffs|How do mass, power, data rate, trajectory, and science time constrain one spacecraft?|Use a named mission and official design basis.
mysteries_unsolved_cases|An Unexplained Mission Signal|Which technical or scientific explanations fit one anomaly?|Compare telemetry, instrument artifacts, environmental causes, and follow-up.
technology_innovation|A Spacecraft Capability Proven|Which new component expanded what a mission could do?|Compare qualification tests, in-flight performance, and failures.
people_personalities|A Mission Decision Maker|How did a named scientist or engineer influence one documented choice?|Use design reviews and team records without a lone-genius story.
major_events|A Mission's Critical Maneuver|What did one launch, flyby, landing, or recovery event establish?|Trace planned sequence, telemetry, deviations, and public report.
how_it_works|Operating a Scientific Instrument|How does one space instrument turn a target into calibrated data?|Follow pointing, exposure, transmission, calibration, and analysis.
rise_fall|A Mission That Changed Scope|Why was one mission curtailed, extended, or repurposed?|Compare technical condition, budget, science return, and official decisions.
then_vs_now|Two Missions to the Same Target|How did instruments and questions differ across two dated missions?|Compare coverage, resolution, constraints, and actual results.
future_developments|A Planned Mission's Testable Goals|What must a proposed mission measure to answer its stated question?|Use current official plan, schedule uncertainty, and measurable success criteria.
myths_vs_facts|Checking a Spaceflight Claim|Does a public claim about distance, cost, or discovery match mission records?|Read official data and distinguish milestone from scientific inference.
documentary_stories|A Mission Through Its Archive|How did one mission move from concept to released data?|Build a dated record of reviews, launch, operations, anomalies, and archives.
observation_to_explanation|From Telemetry to Discovery|Which steps turn one received signal into a physical claim?|Separate sensor output, calibration, processing, model, and independent check.
measurement_method|A Space Instrument's Measurement|What quantity did one instrument actually record?|Inspect units, detector, calibration, noise, and retrieval assumptions.
scale_and_timespan|Light-Time and Mission Timing|How do distance and communication delay change a mission decision?|Use a named phase and distinguish planned from real-time control.
field_vs_lab|Qualification Versus Flight|Which ground tests did a component pass, and how did it behave in space?|Compare simulated conditions, integration, in-flight telemetry, and aging.
natural_variation|Signal Against Space Weather|Can natural environmental variation explain a reported anomaly?|Compare solar activity, radiation, thermal cycles, and instrument response.
mechanism_chain|A Maneuver's Physical Chain|How do navigation data, propulsion, and gravity produce one trajectory change?|Trace commanded action, measured motion, and uncertainty.
extreme_case|A Mission at an Operating Limit|What did a high-radiation, cold, or long-duration mission reveal about design margins?|Compare predicted environment, telemetry, and protective measures.
classification_debate|What Counts as Mission Success?|How do science and engineering teams define success differently for one mission?|Compare original requirements, achieved data, and revised objectives.
interacting_systems|Spacecraft and Environment|How did thermal, power, communication, and target conditions interact?|Analyze a bounded event with telemetry and alternatives.
data_gap|A Missing Observation Window|Which mission gap most limits one scientific conclusion?|Map coverage, pointing, downlink loss, detection limit, and follow-up.
prediction_test|A Mission Model Meets Telemetry|What did a dated navigation or instrument model predict before flight data arrived?|Compare predicted and measured values with uncertainty.
human_impact|Who Benefits from Mission Data?|How did one mission's data enter research, education, or policy?|Trace actual reuse and distinguish outcomes from promotional claims.
field_observation_window|A Target in View|How did orbital geometry and scheduling limit one observation?|Compare visibility, illumination, competing targets, and missed intervals.
field_instrument_limit|A Sensor's Detection Threshold|Which sensitivity or resolution limit matters for one mission claim?|Read calibration and error budget for the relevant operating mode.
field_orbital_dynamics|Choosing a Transfer Orbit|Which trajectory constraints determined one mission's route?|Compare launch energy, gravity assists, time, fuel, and navigation error.
field_mission_tradeoff|Science Within a Budget|Which science goal was gained or lost in one documented design trade?|Use mission objectives, resource limits, and official review records.
field_planetary_environment|Operating at the Target|Which measured conditions challenged a probe, lander, or rover?|Compare environment models, instrument readings, protection, and remaining unknowns."""


if __name__ == "__main__":
    revise_domain("031", "031_megastructures_engineering", STRUCTURES,
                  "Large civil structures through public purpose, design basis, construction, capacity, inspection, maintenance, safety, and local effects.",
                  "approved designs and alternatives, public project records, inspection and load-rating reports, measured use, published investigations, budgets, impact assessments, and community accounts",
                  "Name structure, jurisdiction, date, and design basis. Distinguish modeled from observed performance; avoid unsafe operational details or declaring a facility safe from a single metric.")
    revise_domain("032", "032_space_exploration", SPACEFLIGHT,
                  "Space-mission design, operation, calibrated data, mission constraints, anomalies, and science return.",
                  "mission requirements and design reviews, telemetry and instrument calibration, official mission logs, archived data, primary research, and dated anomaly reports",
                  "Distinguish planned capabilities, telemetry, processed data, and scientific inference. Date mission status and launch claims; state operating limits and uncertainty.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
