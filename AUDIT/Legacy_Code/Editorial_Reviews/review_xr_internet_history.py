"""Editorially reviewed question designs for XR and internet history."""

from review_angle_plans import audit, revise_domain


XR = """history_origins|How Immersive Displays Developed|Which technical and creative problems drove one early VR or AR system?|Compare dated prototypes, patents, demonstrations, and user reports.
famous_examples|A Landmark Immersive Application|What did one celebrated XR experience actually let users do?|Test the archived version's interaction, hardware needs, and accessibility.
hidden_stories|Workers Behind the Virtual World|Whose 3D modeling, testing, moderation, and physical setup work is overlooked?|Use credits and attributed production accounts.
beginner_explainers|What VR and AR Add to a Scene|How does one application connect tracking, rendered content, and user input?|Follow a concrete interaction at a non-instructional level.
advanced_concepts|Presence and Performance|How do latency, tracking, and display design affect a user's experience?|Compare measured conditions with user feedback and comfort limits.
mysteries_unsolved_cases|Why a Prototype Failed|Which evidence explains one immersive demo's inconsistent performance?|Compare hardware, software, environment, and user testing records.
technology_innovation|A New Headset Generation|Which documented change improved one task and which problem remained?|Compare tracking, display, cost, accessibility, and independent tests.
people_personalities|Who Designed the Interaction?|How did artists, engineers, and users shape one XR interface?|Trace prototypes, usability sessions, decisions, and credits.
major_events|An XR Launch Revisited|Did a widely announced product reach its intended users?|Compare launch claims, availability, actual use, support, and later changes.
how_it_works|From Movement to Image|What processing steps turn a user's motion into an updated view?|Explain sensing, pose estimation, rendering, and display conceptually.
rise_fall|A Virtual Platform Closes|Why did one immersive service decline or shut down?|Compare adoption, cost, content, moderation, hardware, and company records.
then_vs_now|The Same XR Task Across Eras|How did one task change with hardware and software advances?|Compare user effort, quality, price, and access on equal terms.
future_developments|Testing a Proposed XR Use|What evidence would justify XR for one training or learning task?|Define comparator, user outcome, cost, access, and harms before deployment.
myths_vs_facts|The Fully Immersive Claim|Does one product deliver the experience advertised?|Compare available interaction, field of view, limitations, and user tests.
documentary_stories|An XR Project's Versions|How did one application change from prototype to public release?|Build dated record of design, testing, launch, and corrections.
system_boundary|The Whole XR Experience|Which hardware, room, network, and support conditions are required?|Map one use case end to end, including non-headset alternatives.
input_output_trace|A Gesture Through the System|Where can one input be delayed or misread before the display updates?|Use aggregate performance tests without security-sensitive details.
design_tradeoff|Visual Detail Versus Responsiveness|How does one application balance rendering quality and latency?|Compare measured frames, comfort, battery, and task success.
failure_mode|When Tracking Breaks|What user-visible problems arise when one system loses reliable tracking?|Use public tests and mitigation at a high level without exploit steps.
testing_limits|Demo Versus Daily Use|What does a short XR demo fail to reveal about long sessions?|Compare comfort, learning, accessibility, maintenance, and repeat use.
standards_interoperability|An Experience Across Headsets|What prevents one XR application from working on another device?|Compare API support, input mapping, assets, and version compatibility.
security_threat_model|Spatial Data and Privacy|Which information does one XR device collect about user and surroundings?|Review public permissions, retention, safeguards, and user control.
maintenance_lifecycle|Keeping an XR App Usable|How do headset and software updates affect one archived experience?|Track dependencies, compatibility, support, and preservation.
infrastructure_dependencies|A Headset Needs a Room|Which physical and network conditions make one XR use case workable?|Check space, lighting, power, connectivity, and safe access.
accessibility_usability|An Alternative to Headset Use|Can a person with a defined access need complete the same task?|Test controls, captions, motion alternatives, and nonimmersive paths.
independent_replication|Can Others Repeat the XR Result?|Did an independent group find the same benefit from one application?|Match hardware, task, participants, measures, and conditions.
responsible_deployment|Launching XR With Users|Which usability, privacy, and safety checks preceded one rollout?|Review testing, consent, support, monitoring, and withdrawal options.
field_software_architecture|Software Behind an XR Scene|Which components handle tracking, interaction, assets, and display?|Use public architecture or authorized documentation at a high level.
field_interface_design|Selecting an Object in XR|How does one interaction design affect speed, errors, and accessibility?|Compare user tests for gaze, controller, hand, and alternative inputs.
field_version_changes|A Version Breaks the Experience|What changed when one runtime or device version updated?|Compare release notes, bugs, user reports, and fixes.
field_open_standards|XR on the Web|Does a standard enable one experience across devices and browsers?|Compare specification status with actual implementation tests.
field_technical_debt|The Cost of a Custom XR Stack|Which unsupported components limit one project's longevity?|Trace maintenance work, staff knowledge, and migration options."""


INTERNET = """history_origins|Connecting Separate Networks|Which design problem led to one internet protocol?|Trace original papers, demonstrations, RFCs, and competing approaches.
famous_examples|An Internet Milestone in Context|What did one famous network event prove at the time?|Compare contemporary logs, participants, hardware, and later claims.
hidden_stories|People Outside the Pioneer List|Which operators, implementers, and institutions made a standard usable?|Use mailing-list archives, code, deployment records, and credits.
beginner_explainers|Internet Versus Web|How do interconnected networks differ from websites and browsers?|Follow one web request through access network, DNS, routing, and server.
advanced_concepts|Interoperability as a Historical Choice|Why did a protocol permit independent networks to connect?|Compare interface definitions, governance, and implementation evidence.
mysteries_unsolved_cases|A Disputed First on the Network|Can an internet milestone's claimed date or inventor be established?|Compare contemporaneous logs, RFCs, press, and definitions of first.
technology_innovation|An RFC Becomes Infrastructure|How did one protocol change move from proposal to broad deployment?|Trace versions, test networks, compatibility, and adoption metrics.
people_personalities|A Standards Contributor's Role|What did a named contributor add to one protocol or service?|Compare drafts, correspondence, implementations, and team work.
major_events|A Transition in Internet Governance|What changed when one coordination function moved institutions?|Trace formal agreements, stakeholder process, and observed operations.
how_it_works|A Packet's Journey in Context|Which systems were needed for a message to cross early networks?|Explain addressing, routing, transport, and application layers conceptually.
rise_fall|A Network Service Fades|Why did one widely used protocol or platform decline?|Compare user needs, competing standards, security, cost, and compatibility.
then_vs_now|One Internet Task Across Eras|How did sending a message or finding a site change?|Compare protocols, access costs, reliability, and user experience.
future_developments|The Next Protocol Transition|What would show that a proposed internet change can be deployed safely?|Define interoperability, security, cost, governance, and migration evidence.
myths_vs_facts|Who Invented the Internet?|Does a single-person claim fit the documented design and deployment history?|Separate packet switching, internetworking, web, and later commercialization.
documentary_stories|One Standard's Paper Trail|How did a technical proposal become an operational internet standard?|Build dated trail of drafts, review, implementation, and revision.
system_boundary|What Counts as the Internet?|Which layers and institutions belong in one historical account?|Define access, networks, names, applications, and governance explicitly.
input_output_trace|A Historical Message Path|What records show how data crossed one early network?|Use public diagrams and logs without live attack details.
design_tradeoff|An Architecture Choice|What did one internet design gain and sacrifice?|Compare stated goals, alternatives, scalability, and operational evidence.
failure_mode|An Outage in the Archive|What did a public postmortem show about one historical internet failure?|Trace causes and governance at a non-exploitable level.
testing_limits|Prototype Network Versus Public Internet|Which limits kept one early demonstration from proving global viability?|Compare scale, hardware, independent networks, and user tasks.
standards_interoperability|Two Implementations Meet|What testing showed that separate vendors could interoperate?|Read published test records, RFC requirements, and edge cases.
security_threat_model|Security Added Over Time|Why did one original design need later security mechanisms?|Compare historical assumptions and public standards without exploit steps.
maintenance_lifecycle|Old Protocols Persist|Why does a legacy internet feature remain deployed?|Compare compatibility, cost, users, support, and risk.
infrastructure_dependencies|Internet Beyond the Screen|Which cables, power, exchange points, and operators enabled one region?|Trace dated infrastructure and access disparities.
accessibility_usability|Who Could Get Online?|Which costs, language, disability, and geography barriers shaped early access?|Use adoption data and user accounts rather than a universal timeline.
independent_replication|A Network Experiment Repeated|Did another institution reproduce one early networking result?|Compare equipment, protocol version, conditions, and documented outcome.
responsible_deployment|A Protocol Transition in Practice|How did operators manage compatibility and service continuity?|Use public migration reports and governance records.
field_software_architecture|An Early Internet Service|Which software pieces made one historic service function?|Use released code, manuals, and diagrams at a conceptual level.
field_interface_design|An Early User Interface|How did one client interface affect who could use a network service?|Compare manuals, screenshots, training, and accessibility.
field_version_changes|A Standard Changes Between Drafts|Which revision altered one protocol's behavior or deployment?|Compare RFC text, rationale, and implementation records.
field_open_standards|The Open Specification|How did a public specification shape independent implementation?|Trace draft access, review, licensing, and adoption.
field_technical_debt|A Historical Shortcut Lives On|Which design assumption created later maintenance costs?|Use documented upgrades and avoid deterministic hindsight."""


if __name__ == "__main__":
    revise_domain("128", "128_virtual_reality_ar", XR,
                  "VR and AR through hardware, tracking, rendering, interaction, accessibility, privacy, standards, and measured user outcomes.",
                  "dated product specifications and release notes, standards drafts and implementation tests, independent usability and performance studies, consented user accounts, and privacy documentation",
                  "Name application, device, version, user group, and date. Separate demos from sustained outcomes, protect spatial and biometric data, and verify current comfort and accessibility guidance.")
    revise_domain("129", "129_internet_history", INTERNET,
                  "Internet history through network design, protocols, standards, operators, governance, access, and documented deployment.",
                  "original RFCs and papers, archived code and network logs, standards discussions, governance agreements, infrastructure records, and participant accounts",
                  "Name network, protocol, institution, and date. Distinguish internet from web, proposal from deployment, and individual contribution from collaborative infrastructure; omit exploitable details.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
