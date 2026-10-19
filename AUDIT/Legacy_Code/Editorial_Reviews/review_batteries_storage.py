"""Editorial questions for batteries and energy storage."""

from review_angle_plans import audit, revise_domain


STORAGE = """history_origins|How a Storage Chemistry Reached Use|Which discoveries and manufacturing choices enabled one battery type?|Trace dated research, patents, production, and applications.
famous_examples|A Grid Battery Project Evaluated|Did one installation deliver its stated service?|Compare dispatch, availability, cost, safety, and independent reports.
hidden_stories|Materials Behind Stored Electricity|Whose mining, refining, assembly, and recycling work is overlooked?|Trace a named chemistry and supply chain with worker accounts.
beginner_explainers|Energy Versus Power|Why do capacity and output describe different storage jobs?|Use a labeled example with units, duration, and losses.
advanced_concepts|Round-Trip Efficiency in Context|How much energy returns from one storage system after charging?|Define meter boundary, operating range, temperature, and auxiliary loads.
mysteries_unsolved_cases|An Unexpected Battery Failure|Which evidence explains one documented failure event?|Review official inquiry, operating data, design, response, and uncertainty.
technology_innovation|A New Storage Chemistry's Claim|Which performance gains hold outside a laboratory cell?|Compare scale, cycle life, safety, materials, and independent tests.
people_personalities|The Operators Behind a Battery Site|How do operators decide when storage is available and useful?|Use documented dispatch rules, maintenance, and attributed accounts.
major_events|A Safety Incident and Its Lessons|What changed after one documented storage incident?|Trace investigation, standards, emergency planning, and redesign.
how_it_works|A Battery in a Power System|How do cells, controls, conversion, and cooling work together?|Use a high-level block diagram and measured system performance.
rise_fall|Why a Storage Project Closed|Which technical and economic factors ended one installation?|Compare degradation, revenue, maintenance, contracts, and replacement.
then_vs_now|One Battery Application Across Decades|How did cost and performance change for a defined use?|Compare comparable system boundaries, prices, reliability, and safety.
future_developments|A Proposed Long-Duration Store|What must one technology prove for a specific grid need?|Define duration, cycling, location, costs, safety, and alternatives.
myths_vs_facts|Can Batteries Power Everything?|Which services can one storage design provide and for how long?|Compare power, energy, efficiency, recharge, and demand profile.
documentary_stories|One Battery's Full Life|Where do benefits and burdens arise from manufacture to end of life?|Trace materials, operation, maintenance, reuse, and recycling.
system_boundary|Where Storage Performance Is Measured|Which components and losses belong in a project claim?|Map cell, inverter, cooling, transformer, controls, and metering.
input_output_trace|Following a Charge and Discharge|How much energy entered, was stored, and was delivered?|Use dated meter data, clear units, state of charge, and losses.
design_tradeoff|Energy Density Versus Longevity|How did one design balance size, cost, cycles, and safety?|Compare validated use cases and operating windows.
failure_mode|A Thermal or Electrical Fault|How was a named fault detected and contained?|Use official incident records and qualified technical analysis.
testing_limits|A Cell Test Versus a Container|Why might laboratory results differ from a full system?|Compare sample, controls, auxiliary loads, safety, and duty cycle.
standards_interoperability|Connecting Storage to a Grid|Which current rules govern one installation's interface?|Identify jurisdiction, protection, testing, certification, and date.
security_threat_model|A Battery Control System's Exposure|Which cyber or physical threats could interrupt safe operation?|Map access, monitoring, updates, governance, and recovery at high level.
maintenance_lifecycle|Degradation in Real Service|How does one operator measure declining usable capacity?|Compare baseline, duty cycle, test method, warranty, and replacement.
infrastructure_dependencies|What a Battery Site Needs|Which land, grid connection, cooling, and response services matter?|Trace permits, interconnection, resources, and local capacity.
accessibility_usability|Who Benefits from Backup Power?|Does one storage project serve the people it claims to protect?|Compare outage history, access, prioritization, costs, and reliability.
independent_replication|A Performance Claim Rechecked|Has a second team reproduced one battery result?|Compare identical conditions, independent data, uncertainty, and scale.
responsible_deployment|Storage in a Community|How are safety, noise, cost, land, and benefits addressed?|Review consultation, monitoring, incident plans, and remedy routes.
field_energy_balance|A Complete Energy Account|What fraction of charged energy is delivered for one duty cycle?|Include conversion, standby, thermal management, and metering uncertainty.
field_grid_integration|Storage at a Constrained Feeder|Did one system reduce a measured grid constraint?|Compare before and after flows, dispatch, reliability, and alternatives.
field_material_inputs|The Chemistry's Supply Needs|Which materials dominate one battery's supply and risk?|Use bill of materials, sourcing, recycling, and substitution evidence.
field_operational_safety|A Site's Safety Case|Which hazards, controls, and emergency roles are documented?|Use current qualified assessment, permits, training, and incident response.
field_lifecycle_emissions|When Storage Changes Emissions|What generation does one system displace under actual dispatch?|Use time-specific grid mix, losses, embodied emissions, and counterfactual.
"""


if __name__ == "__main__":
    revise_domain("158", "158_batteries_energy_storage", STORAGE,
                  "Battery and energy storage systems through energy accounting, grid services, materials, degradation, safety, costs, and lifecycle effects.",
                  "dated project operating and meter data, independent performance tests, current grid and safety standards, incident inquiries, supply-chain records, and lifecycle assessments",
                  "Name chemistry, scale, location, duty cycle, measurement boundary, jurisdiction, and date. Keep electrical and fire hazards at documentary level and defer installation or incident response to qualified professionals.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
