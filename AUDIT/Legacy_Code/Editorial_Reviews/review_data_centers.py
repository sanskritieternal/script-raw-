"""Editorial questions for data center infrastructure."""

from review_angle_plans import audit, revise_domain


DATA_CENTERS = """history_origins|How a Data Center Campus Grew|Which demand and siting choices led to one facility?|Trace permits, customers, land, grid, network, and build phases.
famous_examples|A Model Facility Under Review|Does one celebrated data center meet its performance claims?|Compare meter boundaries, uptime, water, cost, and independent reporting.
hidden_stories|People Keeping Servers Online|Whose electrical, cooling, cleaning, security, and repair work is overlooked?|Follow roles, schedules, training, and attributed worker accounts.
beginner_explainers|What a Data Center Provides|Which services and physical systems make one digital application run?|Map servers, storage, network, power, cooling, and operators.
advanced_concepts|Efficiency and Total Demand|Can a more efficient facility still use more energy overall?|Compare workload growth, facility and IT power, time, and boundary.
mysteries_unsolved_cases|The Cause of an Outage|Which evidence explains one documented service disruption?|Compare incident report, logs, dependencies, timeline, and uncertainty.
technology_innovation|A Cooling Upgrade Tested|Did one cooling change reduce energy or water for the same workload?|Use comparable metering, climate, utilization, and maintenance data.
people_personalities|The Site Operator's Decisions|How does one team balance reliability, energy, water, and cost?|Use documented procedures, measurements, and interviews.
major_events|An Outage with Wider Effects|Which services were affected by one failure and for how long?|Trace dependencies, official status, users, restoration, and corrections.
how_it_works|A Request Through the Facility|How do compute, storage, network, power, and cooling support one task?|Use a high-level path with explicit system boundary.
rise_fall|A Facility's Closure or Retrofit|Why was one site upgraded, moved, or retired?|Compare equipment age, demand, grid, cooling, leases, and cost.
then_vs_now|Computing One Workload Across Time|How did resources needed for a comparable task change?|Normalize workload, service quality, hardware, facility overhead, and period.
future_developments|A Proposed Data Center|What would one new facility require from its host community?|Check grid, water, land, jobs, tax terms, resilience, and alternatives.
myths_vs_facts|Is the Cloud Weightless?|Which physical inputs and impacts support one online service?|Trace data movement, compute, electricity, water, hardware, and boundaries.
documentary_stories|A Day in Facility Operations|Which routine checks and incidents keep a data center available?|Follow authorized staff with security and privacy boundaries.
system_boundary|What Counts in a Facility Metric?|Which equipment and energy are included in one efficiency number?|Specify metering points, time period, shared loads, and reporting standard.
input_output_trace|Workload to Electricity and Heat|How does one task use computing resources and create heat?|Use measured utilization, power, cooling, and uncertainty.
design_tradeoff|Reliability Versus Resource Use|How do redundancy choices affect energy, cost, and uptime?|Compare service target, actual failures, spare capacity, and impacts.
failure_mode|A Single Point of Failure|Which dependency caused or amplified one outage?|Map power, network, software, cooling, and operational response.
testing_limits|A Benchmark's Real Meaning|Does one reported efficiency result represent typical operation?|Check workload, season, utilization, boundaries, and third-party audit.
standards_interoperability|A Service Across Facilities|Which interfaces let a workload move without disruption?|Examine data formats, network, power, operations, and switching cost.
security_threat_model|A Facility's Physical and Digital Risks|Which broad safeguards protect systems and customer data?|Describe governance, access, monitoring, and incident review without exploitable detail.
maintenance_lifecycle|Replacing an Aging Server Fleet|How do upgrades change performance, reliability, and waste?|Compare measured gains, embodied impacts, reuse, and disposal.
infrastructure_dependencies|The Grid Behind a Data Center|What power and transmission upgrades does one campus need?|Trace interconnection, peak demand, backup, costs, and public records.
accessibility_usability|Who Benefits from Local Hosting?|Does nearby infrastructure improve service for local users?|Compare latency, price, access, reliability, and digital inclusion.
independent_replication|Checking an Efficiency Claim|Can an outside analyst reproduce one published metric?|Require definitions, meter data, period, workload, and uncertainty.
responsible_deployment|A Facility in Its Watershed|How are water use and community priorities addressed?|Review permits, seasonal stress, cooling choices, consultation, and remedies.
field_software_architecture|Software's Role in Facility Load|How does one architecture choice affect compute and storage demand?|Compare equivalent service, utilization, traffic, and measured power.
field_interface_design|The Operator's Control View|Does one interface help staff spot and respond to a fault?|Use authorized usability evidence and incident records.
field_version_changes|An Update and Its Infrastructure Cost|Did one software version change workload or reliability?|Compare rollout, demand, performance, rollback, and confounding.
field_open_standards|Can Customers Leave?|Do open interfaces and export formats reduce lock-in for one service?|Check implementation, fees, data movement, and portability tests.
field_technical_debt|Deferred Work in a Facility|How did accumulated hardware or software maintenance affect reliability?|Use incident, upgrade, staffing, and financial records.
"""


if __name__ == "__main__":
    revise_domain("160", "160_data_centers_infrastructure", DATA_CENTERS,
                  "Data centers as physical and digital infrastructure through power, cooling, water, networks, software, labor, reliability, and local impacts.",
                  "facility permits and grid records, metered energy and water with boundary definitions, public incident reports, operational and workload data, lifecycle studies, and consented worker and community accounts",
                  "Name site, operator, workload, metric boundary, jurisdiction, and date. Avoid exposing operational security details; distinguish facility efficiency from total resource demand and verify promotional claims independently.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
