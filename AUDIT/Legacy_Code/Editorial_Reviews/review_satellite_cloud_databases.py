"""Niche-specific editorial questions for satellite internet, cloud, and databases."""

from review_angle_plans import audit, revise_domain


SATELLITE = """history_origins|From Relay to Broadband|Which dated deployment made satellite internet practical for a defined community?|Compare spacecraft, ground network, terminals, and service records.
famous_examples|A Satellite Service Rechecked|What does a well-known deployment actually deliver to users?|Check plan, place, equipment, availability, and measured performance.
hidden_stories|Ground Work Behind the Constellation|Who installs terminals, maintains gateways, and handles service failures?|Use consented worker accounts and operator records.
beginner_explainers|A Request Through Space|How does a home terminal reach an internet service?|Trace terminal, spacecraft, gateway, terrestrial network, and server.
advanced_concepts|Orbit and Network Delay|How much of application delay comes from orbit and how much from the rest of the path?|Compare measured paths, load, and terrestrial endpoints.
mysteries_unsolved_cases|A Service Drop Investigated|Which evidence separates weather, obstruction, congestion, and ground failure?|Use incident timing, terminal data, and independent measurements.
technology_innovation|A New Satellite Link Design|Did an antenna or network change improve a specified user task?|Compare matching terminals, plans, locations, and dates.
people_personalities|Choosing a Satellite Network|Who made a consequential design or licensing decision?|Trace filings, engineering choices, and affected users.
major_events|A Constellation Launch and Service Start|When did launch, licensing, and usable service actually occur?|Build a dated timeline from regulator and operator records.
how_it_works|Satellite to Ground Route|How are traffic and control handed among terminal, spacecraft, gateway, and network?|Bound one architecture and route; distinguish space links from ground links.
rise_fall|Adoption in a Remote Area|Did uptake reflect coverage, equipment price, capacity, or alternatives?|Compare subscriptions with affordability and usable quality.
then_vs_now|Two Satellite Internet Eras|How did one user task change across orbit and terminal generations?|Match geography, plans, weather, and application.
future_developments|A Proposed Constellation Expansion|What must be licensed, launched, connected, and maintained before service improves?|Separate announced capacity from active coverage.
myths_vs_facts|Coverage Map Equals Service?|What conditions can prevent usable service inside a mapped area?|Check eligibility, terminal view, capacity, price, and local rules.
documentary_stories|A Rural Connection Journey|How did one household or institution obtain and use service?|Use consented accounts, invoices, installation records, and measurements.
system_boundary|Where Satellite Service Ends|Which provider, terminal, gateway, ISP, and app controls affect a complaint?|Draw the responsibility boundary for one plan.
input_output_trace|A Video Call via Satellite|What data path and delay does a call encounter?|Use privacy-safe testing with named endpoints and timestamps.
design_tradeoff|Orbit, Capacity, and Coverage|How does one architecture trade terminal cost, delay, and area served?|Compare defined orbit and ground configurations.
failure_mode|When a Gateway Fails|What redundancy allows service to continue or fail?|Use a public incident and identify independent ground dependencies.
testing_limits|What a Satellite Speed Test Misses|Can a single fast result describe daily usability?|Measure delay, loss, availability, congestion, and application performance.
standards_interoperability|Terminal Across Networks|Which radio, spectrum, and provisioning rules permit compatibility?|Check license, interface specification, and vendor restrictions.
security_threat_model|Privacy on a Satellite Path|Who can observe terminal location, metadata, or traffic?|Name endpoints, encryption, operator access, and realistic adversary.
maintenance_lifecycle|Keeping a Constellation Working|What replacements, software, gateway upkeep, and disposal are required?|Use dated operator and regulator records.
infrastructure_dependencies|A Satellite Still Needs Ground|Which electricity, fiber, gateways, and support systems can stop service?|Map correlated failures and backup routes.
accessibility_usability|Remote Access Beyond Coverage|Can intended users afford, install, power, and use the connection?|Test equipment, plan terms, language, and assistive needs.
independent_replication|Repeating a Satellite Performance Claim|Can another user reproduce a quoted result?|Report location, sky view, plan, terminal, time, weather, and method.
responsible_deployment|Costs of More Space Capacity|Who gains connectivity and who bears spectrum, debris, or night-sky impacts?|Compare documented benefits, affected groups, and mitigation.
field_software_architecture|A Satellite Network's Control Plane|Which services authenticate terminals and route sessions?|Use a disclosed architecture and state unknown internals.
field_interface_design|Explaining Link Trouble|Can terminal software help users distinguish obstruction from outage?|Test accessible messages and recovery steps.
field_version_changes|A Terminal Firmware Update|What changed in service or compatibility after one update?|Compare release notes, measurements, and rollback options.
field_open_standards|Open Satellite Interfaces?|Can independent equipment interoperate under published rules?|Check specifications, licensing, certification, and field evidence.
field_technical_debt|Legacy Ground and Terminal Constraints|Which installed components limit upgrades?|Trace compatibility, replacement cost, and service continuity.
"""

CLOUD = """history_origins|From Hosted Servers to Cloud|Which changes made one service on-demand and metered?|Compare dated provisioning, pooling, elasticity, and billing evidence.
famous_examples|A Cloud Migration Revisited|Did one migration improve its stated outcome?|Compare matched reliability, cost, latency, and operations before and after.
hidden_stories|People Operating the Cloud|Who maintains data centers, networks, support, and customer systems?|Trace labor and responsibility across organizations.
beginner_explainers|What Makes a Service Cloud?|Which features distinguish cloud from ordinary remote hosting?|Test NIST characteristics against a named offer.
advanced_concepts|Elasticity Under Load|When does autoscaling protect a workload and when does it lag?|Measure trigger, startup delay, capacity limit, and cost.
mysteries_unsolved_cases|An Unexplained Cloud Bill|Which resources and price rules explain a bounded cost spike?|Reconcile meter, region, storage, transfer, and discounts.
technology_innovation|A Managed Service's Promise|Which operational task did it remove and which controls did it hide?|Compare versions, provider duties, and user evidence.
people_personalities|A Cloud Architecture Decision|Who chose regions, services, and resilience targets?|Use design records and incident outcomes.
major_events|A Regional Cloud Outage|What failed first and how did dependencies spread?|Use dated provider postmortem and customer evidence.
how_it_works|Provisioning a Cloud Workload|How do API, identity, scheduler, compute, storage, and network combine?|Trace a named service model and region.
rise_fall|Why a Service Left the Cloud|Which workload, cost, governance, or performance change drove the move?|Compare documented alternatives and full migration costs.
then_vs_now|One Workload Before and After|How did deployment time, reliability, and total cost change?|Normalize traffic, region, team effort, and time period.
future_developments|A Proposed Cloud Feature|What must be shown before its promised benefit is credible?|Specify availability, compatibility, price, and observed workload.
myths_vs_facts|Cloud Means Infinite Capacity?|Where do quotas, regional supply, and service limits appear?|Use current provider limits and a defined workload.
documentary_stories|An Application's Cloud Move|What happened from decision to steady-state operations?|Follow dated design, migration, incident, and billing records.
system_boundary|Who Owns Which Failure?|Which tasks belong to provider, customer, and software supplier?|Map a named IaaS, PaaS, or SaaS service and contract.
input_output_trace|A Cloud Request and Bill|What resources does one request consume and how are they charged?|Trace network, compute, storage, logs, and meter.
design_tradeoff|Multi-Region Resilience|Which failures does a second region address and what does it cost?|Model data consistency, traffic routing, testing, and fees.
failure_mode|A Dependency Cascade|How did one service failure affect otherwise healthy components?|Use postmortem timelines and distinguish cause from correlation.
testing_limits|Cloud Benchmark Reality|Does a vendor benchmark predict a particular workload?|Specify hardware, region, concurrency, data, and price basis.
standards_interoperability|Moving Between Providers|Which API, image, data, and identity dependencies block portability?|Test export and redeployment rather than naming a standard alone.
security_threat_model|A Cloud Identity Boundary|Who can access data or change infrastructure?|Define roles, keys, provider controls, logging, and attacker capability.
maintenance_lifecycle|Keeping a Cloud Service Supported|How do runtime updates, deprecations, and backups reach customers?|Check dated provider notices and customer actions.
infrastructure_dependencies|The Physical Cloud|Which power, cooling, facilities, and networks support one region?|Map failure domains without assuming public detail is complete.
accessibility_usability|A Cloud Tool for Its Operators|Can a team deploy, monitor, and recover accessibly?|Test interface, documentation, alerting, and support.
independent_replication|Reproducing a Cloud Cost Claim|Can another team rerun the workload and estimate the bill?|Publish region, instance, load, duration, and pricing date.
responsible_deployment|Cloud Footprint and Local Effects|What energy, water, labor, and data-location impacts accompany a deployment?|Compare disclosed methods and affected communities.
field_software_architecture|Managed Service Dependencies|Which provider components and customer code make the app work?|Draw the actual request and failure paths.
field_interface_design|A Cloud Console's Risky Action|Does the interface make scope and cost clear before a change?|Test comprehension, permissions, and recovery.
field_version_changes|A Managed Runtime Upgrade|Which behavior and support guarantees changed?|Compare release notes, regression tests, and rollback.
field_open_standards|Open Format or Provider Lock-In?|Can data and workloads move using published interfaces?|Attempt export, import, and independent implementation.
field_technical_debt|Cloud Configuration Debt|Which shortcuts now make deployments fragile or costly?|Trace inventory, drift, ownership, and migration effort.
"""

DATABASES = """history_origins|A Database Model Emerges|What problem did a named data model address?|Use dated papers, implementations, and workload context.
famous_examples|A Database Migration Revisited|Did one replacement meet its consistency and performance aims?|Compare schema, workload, failure tests, and migration cost.
hidden_stories|People Maintaining the Data|Who defines schemas, repairs records, operates backups, and answers users?|Credit operators, stewards, and affected communities.
beginner_explainers|From Record to Query|How does one application store and retrieve a record?|Trace schema, index, query, permissions, and returned result.
advanced_concepts|Isolation in a Real Transaction|Which concurrent outcome can a chosen isolation level permit?|Use a named engine, version, workload, and reproducible schedule.
mysteries_unsolved_cases|Where Did a Record Go?|Which logs, migrations, replicas, or queries explain a missing result?|Protect sensitive data and distinguish deletion from invisibility.
technology_innovation|A New Database Feature|Did an index or execution change improve the target workload?|Test latency, write cost, storage, and correctness.
people_personalities|A Data Design Choice|Who chose a schema or consistency rule and why?|Read design decisions and consequences for users.
major_events|A Database Incident Timeline|What sequence led from first error to recovery?|Use public postmortem, alerts, and restore evidence.
how_it_works|Commit and Read Back|How does a named engine make a write visible and durable?|Trace transaction, log, storage, cache, and replica path.
rise_fall|A Database Technology's Adoption|Which workload and organization choices explain use over time?|Separate popularity metrics from suitability and outcomes.
then_vs_now|One Query Before and After|What changed after schema or engine migration?|Control data size, hardware, indexes, concurrency, and version.
future_developments|A Proposed Database Capability|What would demonstrate safe usefulness in production?|Define compatibility, correctness, workload, and operational cost.
myths_vs_facts|Replication Is Backup?|Which failures can a replica copy but a retained backup recover?|Test deletion, corruption, restore point, and access controls.
documentary_stories|A Data Recovery Story|How did operators detect, contain, and restore a loss?|Use consented records and distinguish recovery claim from test.
system_boundary|Application Versus Database Guarantee|Which correctness duties belong to app code, schema, and engine?|Name transaction settings and failure assumptions.
input_output_trace|One Query's Path|What data enters a query and how is the result produced?|Trace parse, plan, index, access, and response for a named engine.
design_tradeoff|Index Gains and Write Costs|When does an index speed reads while increasing maintenance?|Benchmark a defined mix and data distribution.
failure_mode|A Failed Commit or Restore|What evidence shows whether data was lost or unavailable?|Use transaction logs, storage state, and restore test.
testing_limits|A Database Benchmark's Blind Spots|Does a headline throughput number match the intended application?|Specify schema, dataset, read-write mix, concurrency, and durability.
standards_interoperability|Moving Data Between Engines|Which schema and query semantics survive migration?|Test types, isolation, extensions, and exports.
security_threat_model|Who Can Read a Record?|Which identities, services, backups, and operators can access data?|Define privileges, encryption endpoints, logs, and retention.
maintenance_lifecycle|Upgrading a Live Database|How can version changes and schema migrations preserve service?|Plan compatibility, backfill, validation, and rollback.
infrastructure_dependencies|Storage Beneath the Database|Which disk, network, clock, and power assumptions affect correctness?|Map failure domains and engine guarantees.
accessibility_usability|Database Tools for Teams|Can operators and analysts understand errors and permissions?|Test interfaces, documentation, audit trails, and assistive use.
independent_replication|Reproducing a Database Claim|Can another team rerun a performance or correctness test?|Publish engine version, settings, data, workload, and method.
responsible_deployment|Data Collection and Retention|Which records should exist and who can challenge their use?|Check purpose, consent or authority, access, deletion, and harms.
field_software_architecture|Database in an Application|Which caches, queues, replicas, and services sit around the source of record?|Map consistency and recovery boundaries.
field_interface_design|A Query Tool's Dangerous Action|Does the interface reveal scope before update or deletion?|Test preview, permissions, transaction, and recovery.
field_version_changes|Engine Upgrade Regression|Which queries or behaviors changed after a version upgrade?|Compare release notes, plans, correctness, and rollback.
field_open_standards|Portable Data and Query?|Can another implementation read the format and reproduce semantics?|Test specification, export, extensions, and independent tool.
field_technical_debt|A Schema That Cannot Evolve|Which undocumented dependencies make a data change risky?|Trace queries, clients, ownership, backfills, and migration path.
"""


if __name__ == "__main__":
    revise_domain("321", "321_satellite_internet", SATELLITE,
                  "Satellite internet as an end-to-end service involving spacecraft, terminals, gateways, terrestrial connectivity, capacity, pricing, and access.",
                  "dated regulator and operator records, architecture documents, outage reports, independent measurements, and consented user accounts",
                  "Name orbit, provider, plan, terminal, location, and date. Separate coverage claims and peak rates from usable service; protect user location data.")
    revise_domain("322", "322_cloud_computing", CLOUD,
                  "Cloud computing through defined service models, measured resources, shared operational duties, workload outcomes, and physical infrastructure.",
                  "NIST definitions, provider specifications and price sheets, contracts, incident reports, workload measurements, and customer records",
                  "Name provider, service model, region, version, workload, and price date. Distinguish provider promises from measured customer outcomes.")
    revise_domain("323", "323_databases", DATABASES,
                  "Databases as versioned systems for data modeling, transaction correctness, querying, operations, recovery, and stewardship.",
                  "database documentation, design records, query plans, reproducible workloads, backup and restore tests, and incident postmortems",
                  "Name engine, version, isolation settings, schema, and workload. Do not generalize one engine's guarantees or expose production records.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
