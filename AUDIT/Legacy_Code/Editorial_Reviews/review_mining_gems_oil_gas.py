"""Editorial question designs for mineral and hydrocarbon extraction."""

from review_angle_plans import audit, revise_domain


MINING = """history_origins|A Mine Opens|Which deposit, demand, and land decisions led to one mine?|Trace dated maps, permits, and community records.
famous_examples|A Mine beyond Its Output|What do production, safety, and restoration records show?|Specify mine, commodity, period, and ownership.
hidden_stories|Workers and Neighbors|Whose labor or land experience is absent from a mine's story?|Use attributed accounts and public records.
beginner_explainers|From Deposit to Product|How are resource, ore, waste, and saleable product distinguished?|Follow one commodity and facility.
advanced_concepts|Ore Grade and Recovery|How do grade, processing losses, and price shape a mine plan?|Use dated reserve and process assumptions.
mysteries_unsolved_cases|Unexpected Water Quality|Which samples could distinguish mine drainage from natural background?|Compare upstream, downstream, and seasonal data.
technology_innovation|A Mining Method Change|Did a new method improve recovery, safety, or disturbance?|Use matched production and monitoring data.
people_personalities|A Mining Decision|Who approved expansion and who contested it?|Trace hearings, technical reports, and consent claims.
major_events|A Mine Incident|What did an official investigation establish and remedy?|Separate finding from initial report.
how_it_works|Ore through a Mine|How do extraction, hauling, processing, waste, and water management connect?|Use one site flow diagram and measured balance.
rise_fall|A Mine Closes|Which depletion, cost, policy, or hazard factors drove closure?|Use dated production and closure documents.
then_vs_now|Mine Site after Closure|What changed in water, land, work, and access?|Compare baseline, closure targets, and monitoring.
future_developments|A Proposed Mine|What evidence would test promised output and impacts?|Treat feasibility and approval as separate stages.
myths_vs_facts|Reserve versus Resource|Does a published mineral estimate mean recoverable production?|Read classification, date, and economic assumptions.
documentary_stories|One Deposit's Decision Trail|How did exploration become extraction or rejection?|Build a dated permit and technical record.
system_boundary|Mine versus Supply Chain|Which effects belong to extraction, processing, transport, and use?|State commodity, place, and lifecycle unit.
input_output_trace|Ore, Water, and Waste|Where does each stream go in one operation?|Use measured mass and water balances.
design_tradeoff|Recovery and Disturbance|What did a chosen mining method gain and cost?|Compare feasible alternatives under one deposit.
failure_mode|A Documented Mine Failure|Which physical and management factors were established?|Use regulator investigation without operational instructions.
testing_limits|Core Samples versus Production|Where did sampled grade fail to predict recovered output?|Check sampling, dilution, and processing data.
standards_interoperability|Rules for a Mine|Which mining, labor, water, and land rules apply?|Name jurisdiction, facility, and date.
security_threat_model|Mine Continuity Planning|What public controls protect records, people, and facilities?|Stay at governance and resilience level.
maintenance_lifecycle|Equipment and Waste Facilities|Which inspection histories reveal deterioration?|Use dated monitoring and repair records.
infrastructure_dependencies|Mine, Power, and Water|Which outside services constrain production?|Map energy, water, road, and workforce links.
accessibility_usability|Who Can Inspect or Participate?|Can affected people access information and hearings?|Check language, travel, disclosure, and timing.
independent_replication|Recheck a Grade Claim|Can another analyst reproduce ore-grade or recovery figures?|Use sampling frame, assays, and denominator.
responsible_deployment|Opening and Closing a Mine|What monitoring and financial provisions follow the project?|Read permits, closure plans, and observed results.
field_prototype_testing|Pilot Processing Trial|Which scale-up risks does a pilot leave unresolved?|Compare feed variability and full-scale operation.
field_design_tolerance|Ore Variability|How does deposit variation affect equipment and recovery assumptions?|Use spatial assays and sensitivity ranges.
field_manufacturing_method|From Ore to Concentrate|Which process route determines yield and waste?|Trace plant records at a high level.
field_failure_investigation|Investigating a Mine Incident|Which field, maintenance, and worker records support the finding?|Avoid unsupported blame.
field_repair_path|Restoration after Damage|What measured evidence shows a remedy worked?|Compare targets with follow-up monitoring.
"""

GEMS = """history_origins|A Gem Deposit Becomes a Mine|Which geology, land rights, and demand drove extraction?|Trace dated maps, permits, and trade records.
famous_examples|A Gem Field Reexamined|What do actual output and provenance records establish?|State mineral, site, period, and sampling limits.
hidden_stories|Miners behind a Gem|Whose labor and community costs disappear in retail storytelling?|Use attributed accounts and local records.
beginner_explainers|Source Rock to Gem|How do formation, transport, recovery, and sorting connect?|Follow a specified gem material and deposit type.
advanced_concepts|Proving Geographic Origin|Which inclusion or trace-element evidence supports a source claim?|Compare reference samples and overlapping signatures.
mysteries_unsolved_cases|A Stone with Uncertain Source|What laboratory and custody evidence is missing?|Do not infer origin from color or seller account alone.
technology_innovation|A Sorting Method|Does new screening improve recovery without increasing breakage?|Compare matched feed and yield data.
people_personalities|A Mining Community's Choice|Who negotiated access and who did not?|Trace tenure, consultation, and benefit records.
major_events|A Gem Mine's Expansion|What changed in production, land, and worker conditions?|Use dated approvals and monitored outcomes.
how_it_works|Gem Recovery and Identification|How is a recovered stone linked to deposit and laboratory result?|Follow sample label and custody.
rise_fall|A Gem Field Declines|Was output reduced by depletion, price, access, or reporting?|Compare records and uncertainty.
then_vs_now|A Site before and after Mining|What happened to land, water, livelihoods, and access?|Use baseline and repeat observations.
future_developments|A Proposed Gem Operation|Which geology and social evidence would justify investment?|Treat claims as conditional.
myths_vs_facts|Ethical Gem Label|What does a particular certificate actually verify?|Check scope, material, and custody gaps.
documentary_stories|One Stone's Documented Trail|Which records connect mine, parcel, laboratory, and sale?|Do not claim traceability across missing transfers.
system_boundary|Mine or Retail Chain?|Which labor and environmental claims cover extraction alone?|Name entity, parcel, and time.
input_output_trace|Gravel to Sorted Stones|What volumes and losses are recorded at each stage?|Use feed, recovered weight, and waste records.
design_tradeoff|Recovery and Landscape|How do mining methods change yield and disturbance?|Compare same deposit and protection conditions.
failure_mode|A Documented Gem-Mine Incident|Which cause and remedy are established?|Use official investigation without procedural detail.
testing_limits|Small Sample, Big Claim|How representative is a parcel of a deposit?|Check sample size, spatial bias, and quality distribution.
standards_interoperability|Which Certificate Applies?|Does a rough-diamond trade rule apply to this gem?|Name material, transaction, jurisdiction, and date.
security_threat_model|Record Integrity|How are origin and custody records protected from substitution?|Discuss auditability, not evasion methods.
maintenance_lifecycle|Mine and Processing Equipment|Which upkeep affects recovery and worker exposure?|Use site logs and inspection records.
infrastructure_dependencies|Remote Gem Site|Which water, road, power, and buyer access shape operation?|Map site-specific dependencies.
accessibility_usability|Community Access to Evidence|Can affected residents understand permits and monitoring?|Check language and disclosure.
independent_replication|Recheck an Origin Claim|Can another lab match a geographic attribution?|Use reference-set coverage and uncertainty.
responsible_deployment|Mine Benefits and Closure|Which promises to workers and neighbors were fulfilled?|Compare agreements, monitoring, and testimony.
field_prototype_testing|A Recovery Pilot|What yield and breakage does a small trial show?|Define feed grade and size distribution.
field_design_tolerance|Variable Gem Quality|How does grade uncertainty affect a mine plan?|Model plausible quality and recovery ranges.
field_manufacturing_method|Sorting and Cutting Boundaries|Which value is created at mine, cutter, or seller?|Keep custody and labor stages distinct.
field_failure_investigation|A Disputed Provenance|Where did the evidence chain fail?|Audit records and laboratory method.
field_repair_path|Restoring a Gem Site|What measured land and water outcomes followed closure?|Compare plan and actual monitoring.
"""

OIL_GAS = """history_origins|A Field Developed|Which geology, rights, and demand decisions led to production?|Trace dated leases, permits, and records.
famous_examples|A Field's Real Output|What do production and impact records show over time?|State oil or gas, field, and period.
hidden_stories|Workers and Host Communities|Whose risks and benefits are missing from an energy account?|Use attributed testimony and public data.
beginner_explainers|Well to End Use|How do production, processing, transport, refining, and consumption differ?|Follow one product and boundary.
advanced_concepts|Reservoir Decline and Recovery|How do forecasts compare with actual field production?|Use pressure, output, and uncertainty.
mysteries_unsolved_cases|An Emissions Discrepancy|Which measurements explain differences between inventory and observation?|Compare method, season, and site coverage.
technology_innovation|A Leak Detection Method|Does it find and reduce emissions in field use?|Compare detection threshold and verified repairs.
people_personalities|A Development Decision|Who approved an oil or gas project and who objected?|Trace official review and affected people.
major_events|A Pipeline or Well Incident|What did the official investigation establish?|Separate preliminary cause from final finding.
how_it_works|Gas from Well to Customer|How do gathering, processing, storage, and distribution connect?|Use one regional flow and measured volumes.
rise_fall|A Field Winds Down|Which production, price, and policy factors drove closure?|Use dated output and decommissioning records.
then_vs_now|An Energy Site after Closure|What land, water, leakage, and employment changes are measured?|Compare baseline and long-term monitoring.
future_developments|A Proposed Field or Pipeline|What demand, safety, and emissions evidence would test the proposal?|Treat forecasts as scenarios.
myths_vs_facts|Clean Gas?|How does a climate comparison change with methane-loss assumptions?|State time horizon and full lifecycle boundary.
documentary_stories|One Barrel or Gas Stream|How did a product move from field to market?|Track custody and transformations without claiming perfect tracing.
system_boundary|Where Does the Fuel Chain End?|Which emissions arise at production, processing, transport, and use?|Specify fuel, region, and functional unit.
input_output_trace|Hydrocarbon and Water Streams|Where do produced fluids, energy, and waste go?|Use facility-level balances and uncertainty.
design_tradeoff|Production and Emissions|What operational choice changed output, cost, and leakage?|Compare documented conditions.
failure_mode|A Documented Loss of Containment|What initiating and contributing factors did investigators find?|Use official record without operational instructions.
testing_limits|Inventory versus Direct Measurement|Which sources or episodic events can each method miss?|Compare sampling windows and detection limits.
standards_interoperability|Rules across the Chain|Which regulator covers wells, pipelines, and air emissions?|Name jurisdiction, asset, and date.
security_threat_model|Critical Energy Infrastructure|Which public resilience controls address disruption?|Avoid site vulnerabilities or exploitation steps.
maintenance_lifecycle|Aging Wells and Pipelines|Which inspections, repairs, and abandonment records exist?|Track asset and time period.
infrastructure_dependencies|Energy Supply Links|Which power, water, processing, storage, and pipelines constrain output?|Map one field and market route.
accessibility_usability|Public Access to Impact Data|Can residents find and interpret emissions and incident records?|Check reporting gaps and data latency.
independent_replication|Recalculate an Emissions Estimate|Can another analyst reproduce a methane figure?|Use activity data, factors, measurements, and boundary.
responsible_deployment|Operating and Retiring Assets|What monitoring, remediation, and financial responsibility are documented?|Compare commitments and results.
field_energy_balance|Energy In and Out|How much energy is used from production through delivery?|State units, conversion, and losses.
field_grid_integration|Gas Supply and Power Demand|How do storage and delivery constraints affect generation?|Use regional grid and pipeline data.
field_material_inputs|Materials in Oil and Gas Work|Which water, steel, chemicals, and land inputs can be measured?|Use facility records and lifecycle scope.
field_operational_safety|Safety Record for an Asset|Which incidents and inspections support a bounded claim?|Name operator, asset, regulator, and period.
field_lifecycle_emissions|Emissions across the Chain|How do measured methane and combustion emissions add up?|State source coverage, uncertainty, and time horizon.
"""


if __name__ == "__main__":
    revise_domain("433", "433_mining", MINING,
                  "Mining through geology, production, labor, site safety, waste and water, community rights, and closure evidence.",
                  "dated mine and permit records, assays and production balances, MSHA investigations, USGS environmental studies, water monitoring, and community accounts",
                  "Name commodity, mine, owner, jurisdiction, and period. Distinguish resources from recoverable reserves and measured impacts from forecasts; avoid operational extraction instructions.")
    revise_domain("434", "434_gem_mining", GEMS,
                  "Gem mining through deposit geology, sample quality, extraction, worker conditions, custody, certification limits, and site restoration.",
                  "USGS gem geology, site and labor records, laboratory reports with reference sets, parcel custody records, certificate terms, and environmental monitoring",
                  "Name gem material, deposit, parcel, place, and date. A rough-diamond trade certificate does not certify every gem or all labor and environmental conditions.")
    revise_domain("435", "435_oil_gas", OIL_GAS,
                  "Oil and gas through field output, processing and transport, worker and community effects, direct emissions evidence, and retirement obligations.",
                  "EIA energy-flow and production data, EPA emissions methods and measurements, PHMSA pipeline records, official incident reviews, permits, and community testimony",
                  "Name product, asset, regulator, place, and period. Distinguish direct measurements from inventories and specify lifecycle and climate time horizons.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
