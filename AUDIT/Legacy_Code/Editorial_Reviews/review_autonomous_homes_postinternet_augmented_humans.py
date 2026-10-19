"""Editorial question designs for connected homes and human augmentation."""

from review_angle_plans import audit, revise_domain


HOMES = """history_origins|From Home Automation to Autonomy|Which household controls gained sensing and learned behavior?|Trace dated products.
famous_examples|A Smart Home in Use|Which chores or controls are truly automated in a documented home?|Observe exceptions.
hidden_stories|People Maintaining a Smart Home|Who installs, updates, troubleshoots, and cleans devices?|Use a household service log.
beginner_explainers|Connected versus Autonomous Home|Does the system follow a schedule, remote command, or inferred intent?|Name device and task.
advanced_concepts|Coordination across Home Devices|How do sensors, rules, cloud services, and manual override interact?|Map data flow.
mysteries_unsolved_cases|A Claimed Energy Saving|Does a smart controller reduce total energy under comparable conditions?|Adjust for weather and occupancy.
technology_innovation|Local Control for a Home Device|Does operation continue during internet loss?|Test under specified conditions.
people_personalities|A Resident's Daily Experience|Which convenience and burden does one account reveal?|Include all household members.
major_events|A Smart-Device Security Failure|What changed after a disclosed flaw or service outage?|Use vendor and incident records.
how_it_works|From Sensor to Home Action|Who or what authorizes a lock, heat, or light change?|Trace one event.
rise_fall|A Device Becomes Unsupported|What functions fail after updates end or a service closes?|Use lifecycle record.
then_vs_now|Smart Home Claims over Time|What once required cloud control and what now runs locally?|Compare products and versions.
future_developments|A More Autonomous Household|Which reliability, safety, privacy, and accessibility needs remain?|Keep scenario conditional.
myths_vs_facts|A Home That Runs Itself?|Which work remains for residents and service workers?|Inventory tasks.
documentary_stories|One Household Automation Failure|How did detection, override, repair, and recovery unfold?|Use documented incident.
assumption_inventory|Autonomous Home Scenario|Which connectivity, power, consent, and device-support premises are required?|List failure points.
readiness_check|Before Automated Locks or Heat|Are safe defaults, access, updates, and manual override tested?|Use device-specific evidence.
physical_limits|Sensors in Real Rooms|How do layout, glare, noise, and occupants affect detection?|Test varied conditions.
governance_choice|Who Controls Household Data?|Can renters, children, guests, and caregivers influence settings?|Map roles and permissions.
unequal_futures|Who Can Use Smart Housing?|How do price, internet access, disability, and tenancy shape benefit?|Compare households.
scenario_pair|Cloud-First versus Local Home|How do outage, privacy, and maintenance differ?|Hold task constant.
failure_to_launch|Automation No One Kept Using|Did complexity or false alarms outweigh benefit?|Use adoption records.
unintended_effect|Home Surveillance by Convenience|Can sensors enable unwanted monitoring of residents?|Trace access and logs.
social_adaptation|Living with Automated Decisions|How do people change habits around controls and alerts?|Interview varied users.
ethical_boundary|Consent inside a Shared Home|When should one resident's preference not bind others?|Use concrete settings.
signal_vs_hype|Demo Home versus Everyday Use|What sustained uptime and resident satisfaction are known?|Separate showroom and home.
reversible_steps|Home Automation Off Switch|Can residents disable features without losing essential access?|Test fallback.
field_resource_budget|Devices' Full Resource Cost|What electricity, replacement, and cloud resources are required?|Use lifecycle view.
field_habitat_design|A Home for All Occupants|How do controls work for disabled people, children, and visitors?|Test actual use.
field_governance_model|Household and Vendor Authority|Who can change settings or retain recordings?|Inspect contracts and controls.
field_dependency_chain|When Internet or Power Fails|Which doors, alarms, and temperature functions remain?|Map dependencies.
field_social_inclusion|Resident Voice in Design|Were tenants and less technical users represented?|Check research and outcome.
"""

POST = """history_origins|Internet Futures Revisited|Which past predictions of an internet successor came true?|Compare forecasts and observed use.
famous_examples|A Community Network or Offline Service|What needs does a deployed alternative meet?|State size and limits.
hidden_stories|People Excluded from Connectivity|Whose daily work is missed in post-internet rhetoric?|Use disaggregated access data.
beginner_explainers|What Could Post-Internet Mean?|Does it mean new interfaces, decentralized networks, or disconnection?|Define scenario first.
advanced_concepts|Layers beneath a New Interface|Which physical networks and protocols still carry its data?|Map architecture.
mysteries_unsolved_cases|A Decentralization Claim|Who actually controls identity, hosting, and discovery?|Inspect governance and infrastructure.
technology_innovation|An Alternative Network|What scale, latency, and reliability has it demonstrated?|Use real deployment metrics.
people_personalities|A User without Reliable Internet|Which local tools help and what remains inaccessible?|Use consented account.
major_events|A Network Shutdown or Outage|How did a documented disruption affect essential services?|Use incident and access evidence.
how_it_works|One Digital Service's Dependency Map|How do device, access network, cloud, identity, and payment connect?|Trace a transaction.
rise_fall|An Alternative Platform's Trajectory|Why did adoption grow or fade?|Compare usage and funding.
then_vs_now|Before and after Mobile Internet|What services and inequalities changed?|Align region and period.
future_developments|Multiple Network Futures|How might policy and infrastructure choices alter access?|Present conditional pathways.
myths_vs_facts|The Internet Is Disappearing?|Which supposedly new service still uses it?|Trace packet path.
documentary_stories|One Connectivity Project's Lifecycle|How did planning, operation, and maintenance unfold?|Use dated local records.
assumption_inventory|Post-Internet World Scenario|Which power, devices, standards, and institutions are assumed?|List hidden dependencies.
readiness_check|Before Replacing an Essential Online Service|Can people still access it during transition or outage?|Test fallback.
physical_limits|Network Capacity and Energy|Which geography, spectrum, power, and hardware constrain reach?|Use measured data.
governance_choice|Who Sets Network Rules?|How do public authorities, standards bodies, and platforms share influence?|Compare concrete systems.
unequal_futures|Connectivity Divide after a New Interface|Who pays and who is left with older devices?|Use ITU access figures.
scenario_pair|Local-First versus Cloud-First Service|How do privacy, outage tolerance, and reach differ?|Hold task constant.
failure_to_launch|A Network That Did Not Scale|Which interoperability or financing issue blocked expansion?|Read project follow-up.
unintended_effect|Fragmented Digital Public Space|Could closed networks reduce access or portability?|Compare user journeys.
social_adaptation|Institutions after Interface Change|How do schools, clinics, and governments support users?|Use service records.
ethical_boundary|Leaving People behind in Transition|What minimum access should remain during change?|Use affected people and rights.
signal_vs_hype|A Successor to the Internet?|What underlying network and adoption evidence exists?|Separate interface from infrastructure.
reversible_steps|Migration with a Return Path|Can people export data and use old channels while systems change?|Check interoperability.
field_resource_budget|A New Network's Material Ledger|What devices, energy, towers, and maintenance are needed?|Include rural reach.
field_habitat_design|Digital Access in Daily Places|How do home, school, and public space shape connectivity?|Use local evidence.
field_governance_model|Rules for a New Network|Who governs identity, moderation, and appeals?|Map authority.
field_dependency_chain|A Digital Service's Single Point of Failure|What breaks when one provider or cable fails?|Test redundancy.
field_social_inclusion|Offline Users in Future Design|Can the unconnected help decide priorities?|Check consultation.
"""

AUGMENT = """history_origins|Assistive Technology and Augmentation|How did restoration and performance enhancement develop differently?|Trace dated devices and users.
famous_examples|A Named Assistive Device|What function and limits did actual users experience?|Use evaluated outcomes.
hidden_stories|Repair and Training behind Augmentation|Who fits, maintains, and teaches use of a device?|Follow full care pathway.
beginner_explainers|Augment, Assist, Restore|What goal and baseline does each term assume?|Use specific examples.
advanced_concepts|Human-Device Adaptation|How do calibration and learning change measured performance?|Include user variation.
mysteries_unsolved_cases|A Claimed Superhuman Gain|What controlled test could establish sustained advantage?|Define task and comparator.
technology_innovation|An Exoskeleton or Interface Update|Did it improve a meaningful activity without new harm?|Use field or clinical evidence.
people_personalities|A User's Chosen Goal|Which task matters to the person using the device?|Use consent and avoid inspiration trope.
major_events|An Access or Safety Decision|How did a dated approval, coverage, or recall affect users?|Read official record.
how_it_works|A Human-Augmentation Loop|How do sensing, actuation, feedback, and user control connect?|Show failure mode.
rise_fall|A Device Abandoned after Trial|Was burden, fit, cost, or benefit the reason?|Use user follow-up.
then_vs_now|Assistive Devices across Generations|What changed in durability, cost, and daily use?|Compare similar populations.
future_developments|Possible Augmented Abilities|Which technical and social conditions must be met?|Avoid inevitable superhuman claims.
myths_vs_facts|Exoskeleton Equals Extra Strength?|Under what task, weight, and duration was benefit measured?|State tradeoffs.
documentary_stories|One Device's Path to Daily Use|How did design, fitting, training, and repair unfold?|Use consented account.
assumption_inventory|An Augmented-Human Scenario|Which power, biology, cost, and acceptance assumptions matter?|List uncertainty.
readiness_check|Before Widespread Use|Are safety, maintenance, consent, and user-defined benefit demonstrated?|Device-specific criteria.
physical_limits|Body and Battery Constraints|How do fatigue, fit, heat, and power bound performance?|Use measured tasks.
governance_choice|Who Sets Device Goals?|How do user, clinician, employer, and manufacturer interests differ?|Map decision authority.
unequal_futures|Augmentation Access|Who receives assistive products and who faces barriers?|Use WHO access evidence.
scenario_pair|Assistive versus Mandatory Workplace Use|How do autonomy and evidence needs differ?|Hold device fixed.
failure_to_launch|A Prototype without Daily Adoption|Which comfort, service, or coverage gap stopped it?|Use field data.
unintended_effect|Work Intensification|Could a wearable increase load expectations or surveillance?|Check work outcomes.
social_adaptation|Changing Norms around Ability|How do users and institutions adapt to a device?|Include disability perspectives.
ethical_boundary|Pressure to Enhance|Can a person refuse a device without losing work or support?|Examine power and policy.
signal_vs_hype|Lab Performance versus Daily Benefit|What real-world use and user-reported outcome exists?|Separate demo and sustained use.
reversible_steps|Stopping Device Use|Can the user remove it without losing access or essential care?|Check dependency.
field_human_agency|Who Controls the Device?|Can the user override or pause its action?|Test interface.
field_body_and_identity|Device and Self-Description|How do users describe their own bodies and abilities?|Avoid imposed labels.
field_rights_framework|Rights in Device Deployment|Which accessibility, privacy, and workplace protections apply?|Name jurisdiction.
field_resource_inequality|Purchase and Long-Term Service|Who covers fitting, updates, repairs, and replacement?|Use payer data.
field_institutional_adaptation|A Service Built around Users|How must clinics, employers, or schools change?|Follow user-defined needs.
"""

if __name__ == "__main__":
    revise_domain("487", "487_autonomous_homes", HOMES,
                  "Autonomous homes through bounded device capabilities, safety, privacy, manual override, household consent, and product lifecycle.",
                  "NIST consumer IoT baseline, FTC voice-assistant privacy guidance, product security and support records, household energy data, and resident accounts",
                  "Name device, task, users, and version. Remote control or a showroom demo is not a self-running home; test outages and unsupported devices.")
    revise_domain("488", "488_post-internet_world", POST,
                  "Post-internet scenarios through actual network dependencies, unequal connectivity, local alternatives, governance, and service continuity.",
                  "ITU connectivity statistics, documented community-network deployments, standards and network architecture, outage reports, and user evidence",
                  "Define what post-internet means in each question. A new interface may still rely on the internet, and access is highly unequal.")
    revise_domain("489", "489_augmented_humans", AUGMENT,
                  "Augmented humans through user-defined assistive benefit, measured task performance, bodily agency, workplace pressure, and equitable access.",
                  "WHO/UNICEF assistive-technology report, GAO workplace wearable assessment, UNESCO neurotechnology recommendation, device trials, and user accounts",
                  "Name device, user population, task, and duration. Restored function is not proof of above-baseline enhancement; users define their own goals.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
