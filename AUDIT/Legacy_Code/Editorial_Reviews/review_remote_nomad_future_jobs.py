"""Editorial question designs for remote and changing work."""

from review_angle_plans import audit, revise_domain


REMOTE = """history_origins|A Remote-Work Policy Emerges|Which tasks and technology led an employer to offer remote work?|Trace dated policy and worker input.
famous_examples|A Remote Team Reexamined|What do output and worker accounts show about a named arrangement?|Specify period, roles, and comparator.
hidden_stories|Home Costs behind Remote Work|Who supplies space, power, care, and equipment?|Use worker diaries and employer policy.
beginner_explainers|Where Work Actually Happens|How do remote, hybrid, and home-based work differ?|Use one occupation and contract.
advanced_concepts|Coordination without Co-location|How do time zones and task dependencies affect handoffs?|Use project and communication records.
mysteries_unsolved_cases|A Productivity Claim|Which metrics and selection effects could explain it?|Compare output quality and worker mix.
technology_innovation|A Collaboration Tool Tested|Did a tool improve work rather than message volume?|Measure task outcomes and worker load.
people_personalities|A Worker Changes Location|What does one consented experience reveal about access?|Pair account with organizational evidence.
major_events|A Return-to-Office Decision|What changed in work and retention after a dated policy?|Compare roles and periods.
how_it_works|Remote Project Handoffs|How are goals, decisions, files, and feedback shared?|Trace one documented workflow.
rise_fall|A Remote Policy Reversed|Which evidence and incentives drove the reversal?|Read management and worker records.
then_vs_now|A Team before and after Remote Work|How did outcomes and time use change?|Align task, staffing, and period.
future_developments|A Proposed Remote Model|What would validate its effects on access and performance?|Treat prediction as conditional.
myths_vs_facts|Remote Means Flexible?|Who still faces fixed meetings and monitoring?|Use schedules, policy, and worker reports.
documentary_stories|One Policy's Life|How did proposal, trial, revision, and use unfold?|Build dated decision trail.
lived_experience|One Remote Workday|What paid work, interruptions, and unpaid setup occurred?|Use consented diary with context.
institutional_pathway|Requesting Remote Work|Which published steps and eligibility rules apply?|Name employer and jurisdiction.
incentives_norms|Availability Signals|Do response-time expectations lengthen work?|Compare policy, message logs, and self-report.
access_and_exclusion|Who Can Work Remotely?|Which job tasks, housing, disability, and network factors exclude people?|Compare roles and groups.
community_variation|Remote Work across Occupations|Why do the same policies produce different experiences?|Match job tasks and management.
policy_in_practice|Written Rule versus Use|Does a remote policy match actual scheduling and promotion?|Compare records and worker accounts.
survey_vs_story|A Remote-Work Survey|Who responded and who is missing?|Check occupation mix and nonresponse.
power_and_voice|Who Sets Work Location?|What influence do workers have over hybrid schedules?|Use bargaining and policy evidence.
unintended_consequence|Flexible Work and Visibility|Did a policy alter access to projects or promotion?|Compare worker cohorts carefully.
comparative_setting|Two Remote Teams|How do tools, time zones, and management differ?|Use common outcome measures.
change_over_time|Remote Work across a Year|How did hours, travel, and output evolve?|Use repeated observations.
ethical_dilemma|Monitoring a Home Workspace|What information is collected and who controls it?|Review consent, policy, and effects.
field_skill_signals|Evidence of Remote Collaboration|Which artifacts show reliable communication?|Assess work, not location stereotypes.
field_hiring_filters|Remote Job Eligibility|Which location and schedule filters block applicants?|Audit ads and current terms.
field_workplace_power|After-Hours Requests|Who can decline and under what rules?|Use actual expectations and worker accounts.
field_career_transitions|Moving to Remote Work|Which training and support ease a transition?|Compare onboarding outcomes.
field_worker_support|Support outside the Office|Are equipment, access, and help services available?|Check policy and actual uptake.
"""

NOMAD = """history_origins|A Mobile-Work Route Develops|Which connectivity and travel rules shaped one destination?|Trace dated infrastructure and policy.
famous_examples|A Nomad Destination Examined|What do cost, connection, and housing records show?|Name city, season, and worker type.
hidden_stories|Local Workers behind a Nomad Hub|Whose housing and service work is omitted?|Use local accounts and market data.
beginner_explainers|Travel and Work Permissions|Which visa, employer, tax, and insurance questions arise?|Use current destination-specific official sources.
advanced_concepts|Mobility and Tax Residence|How do days, client location, and employment status affect obligations?|Compare official rules for a named case; no personal advice.
mysteries_unsolved_cases|A Cost-of-Living Claim|Which expenses and exchange assumptions are missing?|Compare dated local and traveler budgets.
technology_innovation|Connectivity on the Road|Does a backup connection support actual work?|Use uptime logs and privacy considerations.
people_personalities|A Mobile Worker in Context|What tradeoffs does one consented account reveal?|Pair with host-community evidence.
major_events|A Work-Visa Program Changes|Which rule changed and who qualifies now?|Check official current text and date.
how_it_works|One Month in a Place|How do lodging, work permission, connectivity, and transport align?|Trace a realistic, dated itinerary.
rise_fall|A Nomad Hub Changes|How did demand, rent, or policy alter local use?|Use longitudinal local evidence.
then_vs_now|Destination across Two Seasons|How do costs and connectivity change?|Compare same neighborhood and service.
future_developments|A Proposed Nomad Program|Which impacts need monitoring?|Consider workers and residents before forecasts.
myths_vs_facts|Tourist Entry Allows Remote Work?|What do one country's visitor rules actually permit?|Read current official text, not social posts.
documentary_stories|A Mobile-Work Decision|How did a worker and host community experience one stay?|Use consented records and local testimony.
map_vs_ground|Listing versus Actual Workspace|Does mapped Wi-Fi or coworking match availability?|Verify hours, speed, access, and date.
route_choices|Moving between Work Bases|Which travel route balances time, cost, and legal status?|Use current transport and entry rules.
seasonality|Seasonal Work Conditions|How do weather, tourism, and price affect a stay?|Use monthly data.
local_voice|Residents on Nomad Demand|How do locals describe housing and service changes?|Sample multiple perspectives and records.
landscape_process|Place beyond the Postcard|Which water, heat, or flood conditions affect housing?|Use local hazard and seasonal evidence.
accessibility|Mobile Work with Access Needs|Which transit, lodging, and workspace barriers exist?|Verify site-specific features.
infrastructure|Power and Connectivity|Which network and utility failures disrupt work?|Check dated uptime and alternatives.
environmental_pressure|Footprint of Repeated Travel|What travel emissions and local resource use arise?|State route and accounting method.
safety_decision|Travel Advisory in Context|Which official notice applies to a route now?|Date source and avoid universal claims.
place_history|A Neighborhood before Nomad Marketing|What was its housing and work economy?|Use local records and resident accounts.
comparison_of_places|Two Potential Bases|How do permission, cost, access, and services differ?|Use same worker scenario and date.
responsible_access|Living as a Temporary Guest|How can a visitor respect local rules and housing pressure?|Use community and official guidance.
field_trip_budget|A Transparent Monthly Budget|What recurring and setup costs are included?|Show currency date, rent term, and taxes separately.
field_route_reliability|Can the Route Support Work?|How often do transit and internet delays matter?|Use dated service data and schedule buffer.
field_local_etiquette|Local Norms in Context|Which practices do local sources identify?|Avoid stereotyping a whole community.
field_accessibility_check|Verify a Workspace|Can a worker with defined needs enter and use it?|Check route, restroom, power, and communication.
field_environmental_footprint|Travel and Stay Impacts|How do flight, lodging, and local transport contribute?|Use explicit lifecycle and trip boundary.
"""

FUTURE = """history_origins|A Predicted Job Emerged|Which earlier forecast matched or missed a real occupation?|Compare dated prediction and current role.
famous_examples|A High-Growth Occupation|What do current task and employment data show?|Name classification, region, and year.
hidden_stories|Workers inside a Growth Story|Which low-paid support tasks make a new sector function?|Use worker and employer evidence.
beginner_explainers|Reading a Jobs Forecast|What do base year, growth rate, and openings mean?|Use one official projection.
advanced_concepts|Tasks versus Job Titles|How can technology change tasks without removing an occupation?|Compare task evidence over time.
mysteries_unsolved_cases|A Shortage Forecast|Which demand and training assumptions would resolve disagreement?|Read model and local vacancies.
technology_innovation|Automation in a Role|Which tasks were actually changed by a deployed system?|Compare workplace observations and quality.
people_personalities|A Worker Adapts|What support helped one person change roles?|Use consented account and context.
major_events|A Sector Shock|How did one policy or technology event alter hiring?|Compare before-and-after data carefully.
how_it_works|From Forecast to Job Opening|How do industry demand, occupation classification, and vacancies connect?|Trace one labor-market report.
rise_fall|A Once-Promising Role Declines|Which measured demand and task shifts explain it?|Use consistent occupation definitions.
then_vs_now|Past Forecast versus Actual Outcome|How accurate was an old projection?|Match geography, classification, and period.
future_developments|A Job Outlook Scenario|Which assumptions could change projected openings?|Show uncertainty, not certainty.
myths_vs_facts|Fast Growth Means Many Jobs?|How can a high rate start from a small base?|Calculate absolute openings.
documentary_stories|One Occupation's Change|How did tasks, training, and hiring evolve?|Use dated descriptions and worker accounts.
lived_experience|Work in an Emerging Role|What does a worker actually do during a week?|Use consented diary and role context.
institutional_pathway|Entering a New Occupation|Which credentials and routes are documented?|Check local and current requirements.
incentives_norms|Why Firms Redesign Jobs|Which cost, quality, and regulation pressures matter?|Compare employer claims and outcomes.
access_and_exclusion|Who Can Reach New Jobs?|Which training cost, geography, and hiring filters block entry?|Use labor data and applicant accounts.
community_variation|Different Regions, Different Futures|How do local industries change the outlook?|Compare matched occupations.
policy_in_practice|Training Program Results|Did a workforce program lead to actual placements?|Check completion, wages, and comparison.
survey_vs_story|A Future-Jobs Headline|Is it a survey opinion, model projection, or observed hiring?|Read methodology and population.
power_and_voice|Workers in Technology Decisions|Can workers shape task redesign and training?|Use bargaining and implementation records.
unintended_consequence|New Tool, New Workload|Did automation create monitoring or review labor?|Compare measured tasks and hours.
comparative_setting|Two Employers, Same Technology|Why did outcomes differ?|Compare workflow, training, and deployment.
change_over_time|Occupation across a Decade|Which tasks and pay measures changed?|Use consistent classification and price basis.
ethical_dilemma|Who Bears Transition Costs?|How are retraining time and displacement handled?|Use policy and worker evidence.
field_skill_signals|Proof of Emerging Skill|Which work sample shows actual capability?|Test task relevance and authorship.
field_hiring_filters|New-Role Job Ads|Which credentials are required versus preferred?|Audit dated postings and hires.
field_workplace_power|Task Redesign|Who sets pace and evaluates new tasks?|Use worker and manager records.
field_career_transitions|A Real Transition Path|How did people move into a new role?|Map training, income bridge, and placement.
field_worker_support|Support after Displacement|Which services reach affected workers?|Check eligibility and outcomes by place.
"""


if __name__ == "__main__":
    revise_domain("457", "457_remote_work", REMOTE,
                  "Remote work through task coordination, actual hours, access, employer policy, worker voice, and home-borne costs.",
                  "dated employer policies, project and task outcomes, ILO work-arrangement studies, anonymized worker diaries, surveys with sampling detail, and accessibility audits",
                  "Name occupation, employer arrangement, jurisdiction, and period. Distinguish remote eligibility, worker choice, output quality, and engagement metrics.")
    revise_domain("458", "458_digital_nomad", NOMAD,
                  "Digital-nomad travel through place-specific work permission, housing, connectivity, accessibility, local effects, and transparent costs.",
                  "current official immigration and tax guidance, employer policies, local housing and service data, route and connectivity records, and resident testimony",
                  "Name nationality, destination, work arrangement, date, and source. Travel permissions and tax treatment vary; do not imply a tourist entry permits all remote work.")
    revise_domain("459", "459_future_jobs", FUTURE,
                  "Future jobs through dated occupational projections, observed tasks and hiring, regional differences, training routes, and worker transitions.",
                  "BLS and local labor-market projections with methods, dated job postings, employer and worker records, training outcomes, and historical forecast comparisons",
                  "Name occupation classification, region, base year, and horizon. A model projection is not a vacancy or individual career guarantee.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
