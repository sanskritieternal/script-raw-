"""Editorial question designs for internet, mobile technology, and 5G/6G."""

from review_angle_plans import audit, revise_domain


INTERNET = """history_origins|How Networks Interconnected|Which protocol and governance decisions enabled one interconnection?|Use dated RFCs, network maps, and operator records.
famous_examples|A Famous Internet Failure|What did a documented outage reveal about dependencies?|Trace routing, DNS, power, applications, and user effects.
hidden_stories|People Running the Internet|Who maintains cables, exchange points, routing, and support?|Credit operators and local technicians.
beginner_explainers|A Request Across Networks|How does a device reach a named service?|Map address, DNS, routing, transport, and server.
advanced_concepts|The End-to-End Trade-off|Where should reliability or security functions live?|Compare protocol design, network controls, and application needs.
mysteries_unsolved_cases|A Route That Disappeared|Which public measurements explain a reachability incident?|Check BGP, DNS, traceroute, and blind spots.
technology_innovation|A New Protocol Deployed|Did one protocol improve a defined user outcome?|Measure adoption, latency, compatibility, and failure.
people_personalities|A Standards Decision|How did one working group resolve a design dispute?|Read proposals, minutes, RFCs, and implementation evidence.
major_events|An Internet Outage Timeline|What failed first and which users were affected?|Use dated operator reports and independent measurements.
how_it_works|Autonomous Networks Together|How do networks exchange routes and traffic?|Trace one bounded path and peering arrangements.
rise_fall|Connectivity Over Time|What explains a measured access change?|Separate subscription, usable quality, affordability, and coverage.
then_vs_now|One Service Across Protocol Eras|How did speed, security, and reach change?|Compare matched tasks and dated implementation.
future_developments|Conditional Network Evolution|What assumptions shape a proposed change?|State interoperability, incentives, security, and deployment cost.
myths_vs_facts|The Internet Is the Web?|Which services share IP but differ above it?|Trace a concrete web and non-web task.
documentary_stories|One Packet's Approximate Journey|What can public measurements really show?|Name vantage points and avoid implying exact path certainty.
system_boundary|Where the Internet Service Ends|Which device, ISP, DNS, cloud, and app controls matter?|Draw a named service boundary.
input_output_trace|A Domain Lookup to Response|What inputs and outputs occur at each layer?|Use a safe trace and mask personal data.
design_tradeoff|Centralized Service on Distributed Networks|What improves and what fails when a service concentrates?|Compare latency, availability, control, and cost.
failure_mode|A DNS or Routing Error|How did a bounded error affect users?|Use public postmortem and measurements, not exploit steps.
testing_limits|What a Speed Test Misses|Does one measurement reflect real experience?|Check endpoint, time, congestion, packet loss, and application.
standards_interoperability|Why Two Implementations Interoperate|Which RFC requirements and deviations matter?|Compare version, test results, and edge cases.
security_threat_model|Trust on One Internet Path|Who can observe or alter data?|Define encryption endpoints, DNS, intermediaries, and adversary.
maintenance_lifecycle|An Internet Standard in Practice|How does a protocol change reach deployed systems?|Trace RFC, software, operator rollout, and old clients.
infrastructure_dependencies|Cables, Power, and Exchanges|Which physical systems keep a route working?|Map redundancy and correlated failures.
accessibility_usability|Connectivity That Can Be Used|What barriers remain after a link is available?|Test cost, language, disability access, device, and reliability.
independent_replication|Reproducing a Reachability Claim|Can another vantage point confirm an outage?|Share method, time, destination, and uncertainty.
responsible_deployment|A New Network Feature|Who gains, who loses, and who must consent?|Compare interoperability, privacy, operator cost, and access.
field_software_architecture|A Service's Network Stack|Which components are local, ISP, or cloud?|Map failure ownership for one service.
field_interface_design|User-Facing Network Error|Can a user understand and recover from failure?|Test message, fallback, accessibility, and support.
field_version_changes|A Protocol Migration|Which old clients stop working?|Compare version adoption, compatibility, and notices.
field_open_standards|An Open Protocol Claim|Is the specification public and independently implementable?|Check access, licensing, conformance, and deployments.
field_technical_debt|Legacy Network Constraint|Which old design complicates updates?|Trace version, operators, risks, and migration plan.
"""

MOBILE_TECHNOLOGY = """history_origins|From Portable Calls to Data|Which handset and network changes enabled one mobile service?|Use dated standards, devices, and deployments.
famous_examples|A Flagship Phone Rechecked|Which user task actually improved?|Compare battery, access, repair, privacy, price, and network.
hidden_stories|The Mobile Supply and Service Chain|Who mines, assembles, sells, repairs, and maintains devices?|Trace labor and supplier claims.
beginner_explainers|Phone, Radio, Core, App|What happens when a mobile app reaches a service?|Map handset, cell, operator core, internet, and server.
advanced_concepts|Coverage Versus Experience|Why can signal bars coexist with poor service?|Measure bandwidth, congestion, latency, backhaul, and device.
mysteries_unsolved_cases|A Mobile Outage Examined|Which component caused a documented service loss?|Compare operator notices, logs, geography, and alternatives.
technology_innovation|A New Device Feature|Did it improve a defined task or shift costs?|Test matched devices, software, network, and users.
people_personalities|A Design or Policy Decision|Who shaped one handset or operator feature?|Use dated specifications, approvals, and user outcomes.
major_events|A Mobile Network Change|How did a shutdown or upgrade affect customers?|Trace devices, coverage, notices, cost, and access.
how_it_works|A Call or Data Session|How do handset, radio access, core, and destination connect?|Follow a named service and technology generation.
rise_fall|Mobile Adoption Trend|What does a subscription count hide?|Separate SIMs, unique users, active use, and affordability.
then_vs_now|A Mobile Task Across Generations|How did time, cost, reliability, and privacy change?|Compare matched tasks and coverage.
future_developments|A Proposed Mobile Capability|What conditions would make it useful?|State standards maturity, deployment, devices, spectrum, and demand.
myths_vs_facts|Newer Always Faster?|When do coverage, congestion, and device limit gains?|Use matched measurements and applications.
documentary_stories|One Mobile Service Failure|How did a user and operator respond?|Use consented records and dated notices.
system_boundary|What the Phone Controls|Where do device, OS, app, carrier, and cloud responsibilities meet?|Map one feature and contracts.
input_output_trace|A Mobile Request|What data and identifiers travel across systems?|Use safe testing and protect personal information.
design_tradeoff|Battery, Speed, and Coverage|Which design improves one measure at another's expense?|Compare device and network configurations.
failure_mode|No Service in a Covered Area|Which plausible failures fit evidence?|Check maps, indoor conditions, SIM, backhaul, and outage.
testing_limits|Reading a Mobile Benchmark|Do lab and field numbers answer the same question?|Check band, device, load, location, and time.
standards_interoperability|Device Across Networks|Which bands, profiles, and protocol versions must match?|Use current operator and device specifications.
security_threat_model|Mobile Identity and Data|Which parties can access location or traffic metadata?|Define app, OS, carrier, and attacker capabilities.
maintenance_lifecycle|Device Support Period|How do updates, parts, and network sunset affect usable life?|Check dated vendor and carrier policies.
infrastructure_dependencies|Tower to Data Center|What backhaul, power, and core systems support one cell?|Trace outage resilience and redundancy.
accessibility_usability|A Phone for Defined Needs|Can a user complete a task across device, app, and network?|Test assistive features, language, cost, and support.
independent_replication|A Coverage Claim Tested|Can another observer repeat a measurement?|State route, device, plan, time, band, and method.
responsible_deployment|A New Mobile Feature|What privacy, access, and repair effects accompany it?|Compare groups and mitigation evidence.
field_software_architecture|Mobile App Dependencies|Which OS services, APIs, and backend are essential?|Map failure and data boundaries.
field_interface_design|A Mobile Flow in Use|Where do small screens or connectivity interrupt it?|Test with intended users and assistive tools.
field_version_changes|An Update's Trade-offs|Which devices gain or lose functionality?|Compare versions, bug reports, and security support.
field_open_standards|A Cross-Device Feature|Is it interoperable across vendors?|Check standard, test lab, and actual devices.
field_technical_debt|A Legacy Mobile Dependency|Which old radio or API slows change?|Trace compatibility costs and sunset plan.
"""

FIVE_G_SIX_G = """history_origins|From IMT-2020 to IMT-2030|Which standards milestones define 5G and the 6G framework?|Use dated ITU and 3GPP documents.
famous_examples|A 5G Deployment Rechecked|Which capabilities did one network actually deliver?|Compare bands, core, coverage, load, and user tasks.
hidden_stories|The People Building Mobile Networks|Who plans sites, installs radios, maintains backhaul, and handles complaints?|Trace labor and suppliers.
beginner_explainers|What the G Means|How do radio, core, spectrum, and devices define a generation?|Separate standards label from deployment marketing.
advanced_concepts|Latency Across the Full Path|When does a radio improvement affect application delay?|Measure radio, core, transport, server, and load.
mysteries_unsolved_cases|A Disputed Performance Claim|Which test conditions explain inconsistent speeds?|Check band, device, distance, congestion, and method.
technology_innovation|A 5G Advanced Feature|What changed between named releases?|Compare published specifications and deployed support.
people_personalities|A Standards Compromise|How did participants resolve one radio or core issue?|Use contributions, minutes, releases, and implementation.
major_events|A Spectrum Award or Rollout|How did one decision change coverage and competition?|Trace license, site build, cost, and user outcomes.
how_it_works|A 5G Session|How do device, radio, transport, and core serve an app?|Follow one standardized and deployed configuration.
rise_fall|5G Adoption Over Time|What does a covered-population or connection count omit?|Separate coverage, active devices, usage, and quality.
then_vs_now|4G and 5G for One Task|What improvement is measurable in matched conditions?|Control device, place, load, plan, and app.
future_developments|6G as a Framework, Not a Product|Which proposed capabilities still require standards and deployment?|Date each proposal and avoid a rollout prediction.
myths_vs_facts|5G Everywhere Is Gigabit?|Why do bands and network conditions vary?|Use real deployment data and spectrum context.
documentary_stories|One Network Upgrade|What happened from spectrum to site and customer use?|Build a dated operator and regulator timeline.
system_boundary|Where a Generation Label Applies|Is a claim about radio, core, device, or complete service?|Specify architecture and version.
input_output_trace|A Device Handover|What information moves as a user changes cells?|Use standards and safe measurements; protect identifiers.
design_tradeoff|Coverage Versus Capacity|How do lower and higher bands change deployment?|Compare range, site density, throughput, and cost.
failure_mode|A 5G Service Interruption|Which radio, transport, core, or power failure fits evidence?|Use incident report and independent measures.
testing_limits|Peak Rate Versus Typical Rate|What does a lab maximum fail to predict?|Define spectrum, antenna, load, device, and percentile.
standards_interoperability|Multi-Vendor Network Claim|Which interfaces and release versions must match?|Check conformance and actual deployment.
security_threat_model|5G System Trust|Which identities, interfaces, and operators are exposed?|Use published security architecture, not attack instructions.
maintenance_lifecycle|Network Release Upgrades|How do operators deploy a new standards feature?|Trace software, devices, testing, rollback, and legacy support.
infrastructure_dependencies|Radio Needs Backhaul|Which fiber, power, sites, and core limit service?|Map bottleneck and redundancy.
accessibility_usability|Benefit for a Real User|Did new radio improve an accessible end-to-end task?|Test device, app, price, and coverage together.
independent_replication|Comparing 5G Tests|Can a claimed gain be repeated?|Report band, channel, device, geography, load, and version.
responsible_deployment|Who Gets New Coverage|Which communities gain or wait under rollout plans?|Compare licenses, investment, price, and measured access.
field_software_architecture|5G Core Functions|Which network functions serve a defined session?|Use a named release and deployed configuration.
field_interface_design|Explaining Signal to Users|Does a 5G icon communicate actual quality?|Test comprehension and user decisions.
field_version_changes|5G Release Comparison|What specific feature changed from one release to another?|Quote dated specifications and deployment status.
field_open_standards|Standard and Marketing Claim|Does a product implement a recognized specification?|Check conformance, version, options, and interoperability.
field_technical_debt|Older Networks During Upgrade|What legacy compatibility constrains rollout?|Trace spectrum refarming, devices, and service continuity.
"""


if __name__ == "__main__":
    revise_domain("318", "318_internet", INTERNET,
                  "The Internet as interconnecting networks and protocols, with routing, DNS, infrastructure, governance, and user access.",
                  "dated RFCs and standards discussions, operator postmortems, public routing and DNS measurements, network maps, and consented user and worker accounts",
                  "Name protocol, service, vantage point, and date. Distinguish network from application and do not infer a complete path from one measurement.")
    revise_domain("319", "319_mobile_technology", MOBILE_TECHNOLOGY,
                  "Mobile technology as devices, radio networks, operating systems, apps, service plans, accessibility, and repair.",
                  "dated device and operator specifications, standards, field measurements, support policies, incident records, and consented user and worker accounts",
                  "Name device, OS version, operator, place, and date. Protect identifiers and location data; verify current coverage and support with providers.")
    revise_domain("320", "320_5g_6g", FIVE_G_SIX_G,
                  "5G deployment and 6G framework questions through standards versions, radio and core architecture, measured service, and equitable access.",
                  "dated ITU and 3GPP publications, regulator spectrum records, operator deployment data, controlled field tests, and independent measurements",
                  "Name standard release, band, operator, device, location, and date. Separate 6G proposals from deployed products and laboratory peaks from typical service.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
