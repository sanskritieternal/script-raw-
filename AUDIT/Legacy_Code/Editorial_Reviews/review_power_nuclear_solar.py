"""Editorial question designs for power stations, nuclear systems, and solar technology."""

from review_angle_plans import audit, revise_domain


POWER = """history_origins|A Power Station Sited|Which fuel, water, grid, and demand constraints drove one site?|Trace dated plans and community response.
famous_examples|A Power Plant in Context|What do capacity and net generation records actually show?|Name units, fuel, and reporting period.
hidden_stories|People behind Electric Output|Whose operation, maintenance, or neighboring experience is omitted?|Use worker and local evidence.
beginner_explainers|Fuel to Net Electricity|Where does energy enter, convert, and leave a plant?|Follow a defined generating unit.
advanced_concepts|Dispatch and Efficiency|How do load and operating mode alter heat rate and emissions?|Use matched plant data.
mysteries_unsolved_cases|An Output Shortfall|Which outage, fuel, water, or grid factor explains a gap?|Compare operating logs and demand.
technology_innovation|A Plant Retrofit|Did one upgrade change net output, fuel use, or pollution?|Compare before and after with dispatch controls.
people_personalities|A Generation Decision|Who chose a plant design and who bore consequences?|Trace utility, regulator, and local records.
major_events|A Unit Enters Service|Which performance claims were met in the first operating period?|Compare commissioning and measured generation.
how_it_works|Plant and Grid Exchange|How do generator controls, switchyard, and dispatcher interact?|Use public system-level records.
rise_fall|A Station Retires|Which economics, reliability, or rule changes explain closure?|Use dated cost, output, and retirement filings.
then_vs_now|A Plant before and after Retrofit|What changed in generation, heat rate, and emissions?|Align fuel, demand, and season.
future_developments|A Proposed Generator|What data would validate its reliability and cost claims?|Separate plan, permit, build, and operation.
myths_vs_facts|Capacity Means Constant Power?|How does installed capacity differ from actual generation?|Calculate from metered output and time.
documentary_stories|A Plant through Its Records|How did one project change from proposal to retirement?|Trace permits, construction, operation, and closure.
system_boundary|Gross or Net Generation?|Which electricity use inside the plant changes an efficiency claim?|State meter and fuel boundary.
input_output_trace|Energy Flow through a Unit|How much input becomes net electricity, heat, and waste?|Use measured annual or test-period balances.
design_tradeoff|Efficiency and Flexibility|What is gained and lost by ramping a generating unit?|Compare heat rate, wear, and grid value.
failure_mode|A Documented Plant Outage|Which equipment and organizational factors were found?|Use official and operator review.
testing_limits|Acceptance Test versus Annual Use|Which conditions make a short test unrepresentative?|Compare ambient conditions, dispatch, and downtime.
standards_interoperability|Connecting a Generator|Which grid, emissions, and safety requirements applied?|Name market, unit, and date.
security_threat_model|Plant Continuity|Which public resilience controls address fuel or grid disruption?|Avoid operational vulnerability details.
maintenance_lifecycle|Aging Generating Units|How do inspection and outage records shape replacement?|Track equivalent hours, repairs, and cost.
infrastructure_dependencies|Fuel, Water, and Transmission|Which external links determine reliable output?|Map one plant's dependencies.
accessibility_usability|Public Plant Information|Can residents understand emissions and outage reporting?|Check units, timing, and disclosure gaps.
independent_replication|Recalculate Capacity Factor|Can published generation and capacity reproduce the claim?|Use same unit, period, and availability definition.
responsible_deployment|Starting and Retiring a Plant|What monitoring and cleanup obligations follow?|Compare promises with measured outcomes.
field_energy_balance|Net Energy Accounting|What share of fuel energy reached the grid?|Use heat rate and auxiliary load with uncertainty.
field_grid_integration|Plant during Peak Demand|Which ramp, reserve, and transmission limits matter?|Use local grid and dispatch evidence.
field_material_inputs|Materials and Consumables|Which fuel, water, chemicals, and parts sustain output?|Measure per net MWh with boundary.
field_operational_safety|Evidence for Plant Safety|Which inspections and incident records apply?|Name unit, regulator, and period.
field_lifecycle_emissions|Beyond Stack Emissions|How do extraction, construction, operation, and closure add up?|Specify fuel and lifecycle method.
"""

NUCLEAR = """history_origins|A Reactor Project Chosen|Which energy need, design, and regulatory context shaped one plant?|Trace dated proposal and licensing records.
famous_examples|A Reactor Unit Reassessed|What do licensing and operating records show for a named unit?|Specify reactor design, site, and period.
hidden_stories|Workers and Host Communities|Whose labor or local concern is missing from the official story?|Use attributed testimony and review documents.
beginner_explainers|Fission to Grid Power|How do reactor heat, steam, turbine, and generator connect?|Explain at public system level for one design.
advanced_concepts|Defense in Depth|Which independent barriers and oversight tests apply to a bounded scenario?|Use licensing basis, not generic reassurance.
mysteries_unsolved_cases|An Unresolved Operating Event|Which inspection and plant records distinguish possible causes?|Separate preliminary notifications from final findings.
technology_innovation|A Reactor Design Feature|Which safety or performance claim has test and review evidence?|Name design version and regulatory status.
people_personalities|A Licensing Decision|Who evaluated a specific concern and whose views were heard?|Use docket and hearing records.
major_events|A Licensing Milestone|What did a permit or license authorize at that date?|Distinguish design approval, construction, and operation.
how_it_works|Oversight of an Operating Reactor|How are indicators, inspections, findings, and corrective actions linked?|Follow NRC public records.
rise_fall|A Reactor Retires|Which cost, condition, or policy evidence explains closure?|Read owner and regulator filings.
then_vs_now|A Unit across Operating Periods|How did output, inspection findings, and modifications change?|Align reporting definitions and dates.
future_developments|A Proposed Reactor|Which tests and licensing steps remain before operation?|Treat design claims and schedules as conditional.
myths_vs_facts|Licensed Means Risk-Free?|What does licensing evaluate, and what oversight continues?|State reactor and regulatory basis.
documentary_stories|A Plant's Docket History|How did a proposal become a licensed or abandoned project?|Trace public reviews and decisions.
system_boundary|Reactor or Fuel Cycle?|Which impacts arise from mining, enrichment, operation, and waste?|Define energy and lifecycle unit.
input_output_trace|Heat to Net Electricity|Where does reactor heat go through turbine and cooling?|Use public performance data, no operating procedures.
design_tradeoff|Cooling and Site Choice|How do water and thermal constraints shape design?|Compare environmental and performance records.
failure_mode|An Investigated Event|What sequence and corrective actions did regulator records establish?|Avoid speculative mechanisms or actionable details.
testing_limits|Design Analysis versus Service|Which assumptions need inspection and operational evidence?|Compare safety analysis and oversight findings.
standards_interoperability|Licensing Basis|Which requirements apply to a specified unit and amendment?|Name authority, date, and licensed configuration.
security_threat_model|Nuclear Security Governance|What public oversight framework exists?|Discuss only public regulatory scope and review.
maintenance_lifecycle|Unit Aging and Renewal|Which inspections and component replacements support continued operation?|Use licensing and service records.
infrastructure_dependencies|Plant and Supporting Systems|Which water, grid, emergency, and supply dependencies matter?|Use public planning evidence without sensitive detail.
accessibility_usability|Public Access to Reactor Records|Can residents interpret inspection findings and hearings?|Check dated docket and plain-language explanation.
independent_replication|Checking a Capacity Claim|Can public generation data reproduce a unit's output measure?|Match unit, time, and outage accounting.
responsible_deployment|Oversight through Decommissioning|Which monitoring and obligations continue after shutdown?|Use NRC and site records.
field_energy_balance|Heat and Net Power|How do reactor heat and auxiliary use translate into delivered electricity?|Use rated and metered figures with period.
field_grid_integration|Nuclear Unit on a Grid|How do outages and output affect system planning?|Use operator and grid data.
field_material_inputs|Fuel, Water, and Concrete|Which inputs belong in a nuclear lifecycle study?|Define material and site boundaries.
field_operational_safety|Reactor Safety Record|What do inspection findings and indicators actually cover?|Name unit, year, and finding significance.
field_lifecycle_emissions|Nuclear Lifecycle Accounting|Which construction, fuel-cycle, and decommissioning emissions are included?|State method and electricity denominator.
"""

SOLAR = """history_origins|A Solar Design Reaches Use|Which cell, module, and policy steps enabled one installation?|Trace dated research and deployment records.
famous_examples|A Solar Project Rechecked|What do metered output and weather show for a named project?|State system size, location, and period.
hidden_stories|Solar Supply and Installation Labor|Whose manufacturing or field work is overlooked?|Use supplier, workforce, and site records.
beginner_explainers|Sunlight to AC Power|How do module, wiring, inverter, and meter connect?|Follow one system and distinguish DC from AC.
advanced_concepts|Yield Losses in the Field|How do temperature, shade, soiling, and inverter limits interact?|Use weather and component logs.
mysteries_unsolved_cases|A Solar Output Gap|Which measured factors explain actual yield below forecast?|Compare irradiance, outages, and model assumptions.
technology_innovation|A New PV Module|Which lab efficiency gains survived field conditions?|Use independent module and system tests.
people_personalities|A Siting Decision|Who chose the roof or land parcel and who was affected?|Use planning and host-community records.
major_events|A Solar Farm Connects|What output and grid service followed interconnection?|Compare approval, commissioning, and operation.
how_it_works|Solar Production over a Day|How do irradiance, module temperature, inverter, and grid affect output?|Use time-series measurements.
rise_fall|A Solar Technology Loses Market Share|Which cost, durability, or manufacturing factors mattered?|Compare dated prices and field data.
then_vs_now|Two Solar System Generations|What changed in efficiency, yield, reliability, and cost?|Align climate, capacity, and accounting basis.
future_developments|A Proposed Cell Technology|What outdoor durability and production evidence is needed?|Separate lab record from bankable deployment.
myths_vs_facts|Nameplate Equals Delivered Energy?|How do weather and system losses change actual generation?|Use annual AC meter and local resource.
documentary_stories|A Solar Project's Journey|How did design, permit, construction, and operation differ?|Trace dated contracts and measured performance.
system_boundary|Cell, Module, or Plant?|Which losses are counted in a published efficiency figure?|State irradiance and meter boundary.
input_output_trace|Sunlight to Grid Meter|Where do reflected, thermal, wiring, and inverter losses occur?|Use measured irradiance and AC output.
design_tradeoff|Tracking versus Fixed Mount|What extra output, cost, land, and upkeep follow a tracker?|Compare same location and period.
failure_mode|A Documented Solar System Fault|Which component caused lost output?|Use fault logs and field inspection.
testing_limits|Lab Rating versus Outdoor Yield|Which standard conditions differ from a real site?|Compare spectrum, temperature, shade, and soiling.
standards_interoperability|PV and Grid Connection|Which electrical, inverter, and interconnection rules apply?|Name jurisdiction and equipment version.
security_threat_model|Solar Monitoring and Control|Which public controls limit unauthorized changes?|Bound inverter and communication version.
maintenance_lifecycle|Modules through Service Life|What measured degradation and repair history exists?|Use repeated field tests and uncertainty.
infrastructure_dependencies|Solar and Network Capacity|Which feeder, storage, and transmission limits affect output?|Use utility and operator records.
accessibility_usability|Who Can Benefit from Solar?|Which ownership, roof, finance, and interconnection barriers apply?|Compare defined groups and local rules.
independent_replication|Recalculate a Yield Claim|Can another analyst reproduce annual kWh per kW?|Use weather, meter, outage, and capacity data.
responsible_deployment|Siting and Decommissioning|What land, access, and end-of-life commitments were monitored?|Compare plan with actual outcomes.
field_energy_balance|Solar Energy Delivered|How much measured AC energy follows incident sunlight?|State area, irradiance, and system boundary.
field_grid_integration|Solar at a Constrained Feeder|When is output curtailed or stored?|Use interval data and local limits.
field_material_inputs|Materials in a PV System|Which glass, metals, electronics, and land belong in analysis?|Set module and balance-of-system boundary.
field_operational_safety|Solar Installation Evidence|Which inspection and electrical findings apply?|Name project, authority, and period.
field_lifecycle_emissions|PV Lifecycle Emissions|Which manufacturing, transport, use, and retirement stages are counted?|State electricity denominator and lifetime assumption.
"""


if __name__ == "__main__":
    revise_domain("436", "436_power_plants", POWER,
                  "Power plants through measured net generation, fuel and water use, dispatch, outages, grid dependence, emissions, and retirement.",
                  "EIA generator and plant data, metered output, heat-rate records, grid reports, permits, emissions measurements, outage and maintenance records, and community accounts",
                  "Name plant, unit, fuel, grid, and period. Separate nameplate capacity, net generation, and actual availability; define the fuel and emissions boundary.")
    revise_domain("437", "437_nuclear_engineering", NUCLEAR,
                  "Nuclear engineering through licensed reactor designs, public operating evidence, NRC inspection and oversight, fuel-cycle boundaries, and decommissioning.",
                  "NRC licensing dockets and inspection findings, plant performance indicators, EIA net generation, environmental reviews, public incident records, and operator filings",
                  "Name reactor unit, license basis, authority, and date. Treat approvals and oversight as bounded evidence; avoid operational or security-sensitive instructions.")
    revise_domain("438", "438_solar_technology", SOLAR,
                  "Solar technology through cell-to-system performance, weather, inverter and grid losses, field durability, siting, and lifecycle evidence.",
                  "DOE photovoltaic yield and reliability research, independently measured module tests, site weather and AC-meter data, interconnection records, maintenance logs, and lifecycle studies",
                  "Name PV technology, system size, site, weather period, and measurement boundary. Separate laboratory efficiency from annual delivered electricity.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
