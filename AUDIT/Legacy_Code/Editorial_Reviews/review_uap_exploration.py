"""Editorial question review for UAP/astrobiology and exploration stories."""

from review_angle_plans import audit, revise_domain


UAP = """history_origins|How an Unidentified Sighting Was Studied|How did investigators first document one reported aerial event?|Trace dated witness reports, sensor records, collection methods, and later reviews.
famous_examples|A Widely Shared UAP Case Rechecked|What evidence exists for one famous unidentified observation?|Separate original data, later edits, testimony, and competing explanations.
hidden_stories|People Behind the Observation|Which operators or analysts contributed to a case beyond the public witness?|Use attributed official records and protect private individuals.
beginner_explainers|Unidentified Does Not Mean Extraterrestrial|What does an unidentified classification actually establish?|Explain missing data, ordinary alternatives, and the evidence needed for a stronger claim.
advanced_concepts|A Sensor's Apparent Motion|How can geometry or sensor settings change the perceived speed of an object?|Analyze one documented record with calibration and uncertainty.
mysteries_unsolved_cases|A Case That Remains Open|Which specific observations remain unexplained after review?|List available data, missing measurements, viable explanations, and confidence.
technology_innovation|Better Data for UAP Study|Which sensor or reporting change could improve one class of investigation?|Compare metadata, calibration, chain of custody, coverage, and privacy.
people_personalities|The Witness and the Analyst|How did different participants interpret one observation?|Attribute accounts and separate experience from measured evidence.
major_events|A Public Report Changes the Debate|What did one official UAP report conclude and leave unresolved?|Read dated report scope, case definitions, evidence, and recommendations.
how_it_works|Investigating a Reported Anomaly|How do investigators preserve and test evidence from one sighting?|Follow time, location, sensor, weather, air traffic, and independent review.
rise_fall|A Sensational Claim Reconsidered|Which new evidence weakened or narrowed one extraterrestrial interpretation?|Compare earlier claim with later authenticated data and corrections.
then_vs_now|One Sighting Across Investigations|Why did two reviews of the same event reach different conclusions?|Compare data access, methods, definitions, and publication dates.
future_developments|A Testable Search for Life|Which future observation could strengthen or weaken one proposed biosignature?|Specify instrument, confounders, follow-up, and evidentiary threshold.
myths_vs_facts|Checking a UFO Clip|Does a viral clip show the speed, place, or object claimed?|Verify provenance, metadata, geometry, editing, and alternative sources.
documentary_stories|A Report from Sighting to Review|How did one case move through witness account, data collection, analysis, and public claim?|Build a sourced timeline and label gaps.
assumption_inventory|Assumptions in an Extraterrestrial Claim|Which unstated assumptions connect an unusual observation to alien origin?|List sensor reliability, distance, object identity, and alternatives.
readiness_check|Is the Evidence Ready for Analysis?|What metadata and calibration would one observation need for a credible test?|Check original files, timestamps, sensor mode, location, and chain of custody.
physical_limits|A Claimed Maneuver Versus Measurement|Can speed or acceleration be estimated from the available data?|Show geometry, distance uncertainty, frame rate, and physical constraints.
governance_choice|Who Should Review a Report?|How can an institution collect UAP data transparently while protecting privacy?|Compare public protocols, evidence access, and oversight.
unequal_futures|Who Bears the Cost of a Search?|How would two proposed search methods distribute cost, access, and benefits?|Use conditional scenarios, not predictions about contact.
scenario_pair|Two Explanations for One Signal|What observations would distinguish a mundane cause from an unfamiliar one?|State predictions for each and feasible follow-up.
failure_to_launch|Why a Claim Cannot Be Tested|What missing data prevent a reported case from yielding a scientific conclusion?|Identify gaps without treating them as proof of any origin.
unintended_effect|Consequences of a False Alarm|What harms followed premature attribution of one anomaly?|Trace documented effects on witnesses, institutions, and public trust.
social_adaptation|Public Response to an Anomaly|How did a community or agency change reporting after a widely discussed case?|Use dated policy and behavior evidence without claiming mass belief.
ethical_boundary|Witnesses and Sensitive Data|How should an investigation protect people and legitimate sensitive information?|Discuss consent, redaction, and independent review without operational details.
signal_vs_hype|A Biosignature Headline Checked|Does a claim about life beyond Earth match the original measurement?|Separate molecule or pattern, abiotic alternatives, and required confirmation.
reversible_steps|Low-Risk Follow-Up|Which observation could be repeated before a stronger public claim is made?|Prioritize calibrated, independent, noninvasive measurements.
field_world_rule|Rules for Evidence|What standard would make a claimed extraterrestrial finding credible?|Define provenance, independent confirmation, alternatives, and uncertainty in advance.
field_plausibility_boundary|An Extraordinary Interpretation|What ordinary explanations must be ruled out before invoking alien technology?|Check instrument artifacts, atmosphere, aircraft, astronomy, and perspective.
field_point_of_view|What Each Observer Could Know|How did sensor operator, eyewitness, and later viewer see different information?|Map vantage point, time, equipment, and retrospective knowledge.
field_ethical_consequence|Costs of an Accusation|What happens when a private person or group is wrongly tied to a UAP claim?|Use documented case impact and protect identities.
field_adaptation_choice|A UAP Story as Fiction|If one case inspires fiction, which invented elements must be disclosed?|Distinguish authentic record, dramatization, and speculative worldbuilding."""


EXPLORATION = """history_origins|Why an Expedition Began|Which question or need motivated one documented journey?|Compare planning records, sponsors, local knowledge, and later retellings.
famous_examples|A Famous Journey Reassessed|What did one expedition achieve, and at whose cost?|Compare route, stated aims, logistics, local accounts, and aftermath.
hidden_stories|Guides and Support Teams|Whose navigation, translation, labor, or rescue work is missing from one adventure account?|Use credited and consented accounts, not a lone-hero frame.
beginner_explainers|Planning a Responsible Journey|What information must an expedition verify before travel?|Check permissions, season, route, communications, access, and local guidance.
advanced_concepts|Risk Changes Along a Route|How do terrain, weather, group ability, and evacuation options interact?|Use a defined trip and dated conditions, avoiding prescriptive hazard instructions.
mysteries_unsolved_cases|An Expedition with an Uncertain Route|Which proposed paths fit surviving journals and maps?|Compare distances, landmarks, dates, and local place knowledge.
technology_innovation|A Tool Changes Exploration|How did one navigation or transport tool alter what a journey could document?|Compare actual route, accuracy, weight, dependence, and failures.
people_personalities|A Leader's Decisions in Context|Which documented choices by one expedition leader shaped an outcome?|Compare diary, team accounts, conditions, and alternatives.
major_events|A Journey's Turning Point|What event forced one party to change plan or turn back?|Trace dated reports and avoid hindsight certainty.
how_it_works|From Expedition Plan to Field Record|How are route, observations, specimens, and permissions managed on one trip?|Follow a documented expedition through planning, travel, collection, and return.
rise_fall|When an Expedition Failed|Which conditions contributed to one unsuccessful journey?|Use multiple records and avoid blaming individuals without evidence.
then_vs_now|One Route Across Two Eras|How did access, mapping, and local control change between two dated journeys?|Compare methods and permissions under each period's conditions.
future_developments|A Proposed Expedition|What evidence would justify a future journey into a sensitive region?|Evaluate scientific or public value, local consent, safety, and impact conditionally.
myths_vs_facts|Testing an Explorer Legend|Does a popular first-to-arrive or untouched-land claim fit local and archival records?|Check Indigenous presence, maps, prior visits, and definitions.
documentary_stories|An Expedition Through Its Logs|How did one journey unfold day by day?|Build a sourced route and distinguish records from reconstruction.
map_vs_ground|A Planned Route in Reality|How did mapped distance and terrain compare with observed progress?|Use dated maps, route logs, elevation, and conditions.
route_choices|Why One Path Was Chosen|What tradeoffs drove a documented route decision?|Compare permission, distance, supplies, hazards, and local advice.
seasonality|The Same Place in Another Season|How would season change access and impact for one route?|Use historical records and current local guidance without guaranteeing passage.
local_voice|Communities Along the Route|How do residents describe an expedition's presence or legacy?|Use attributed, consented accounts and reflect disagreement.
landscape_process|Terrain That Shapes a Journey|Which geological or ecological process explains a route obstacle?|Combine field observation and local scientific records.
accessibility|Who Could Join the Journey?|Which physical, financial, cultural, or administrative barriers shaped participation?|Compare actual requirements and feasible alternatives.
infrastructure|The Expedition's Hidden Support|Which trails, boats, ports, communications, and supply systems made travel possible?|Trace a bounded route and credited support labor.
environmental_pressure|Expedition Footprint|What measurable effects did one journey leave on land, wildlife, or water?|Compare baseline, permits, waste, and follow-up observations.
safety_decision|The Choice to Turn Back|Which public evidence explains a documented go/no-go decision?|Use official advisories and expedition records, not unsafe route advice.
place_history|Before the Expedition Narrative|How was the traveled landscape used and named before outsiders arrived?|Center local records and community knowledge with permission.
comparison_of_places|Two Routes, Different Constraints|Why was one route viable while another was not?|Compare terrain, season, access rights, logistics, and impact.
responsible_access|When a Route Should Remain Unpublished|What risks arise from publicizing access to a sensitive place?|Consult custodians and site managers; withhold restricted coordinates.
field_trip_budget|The Full Cost of a Journey|What do permits, guides, transport, insurance, and local services add to one trip?|Use current quotes and date assumptions, without implying universal affordability.
field_route_reliability|How Often Is the Route Usable?|What dated evidence shows closures, delays, or seasonal limits?|Compare operator records, official alerts, and weather history.
field_local_etiquette|Visitor Conduct in Context|Which behaviors do hosts ask visitors to follow?|Use current local guidance and attributed community voices.
field_accessibility_check|Testing an Accessible Route|Does a claimed accessible journey match the needs of a defined traveler?|Check actual transport, paths, facilities, information, and alternatives.
field_environmental_footprint|Comparing Travel Impacts|How do two expedition plans differ in measurable environmental burden?|Bound transport, accommodation, waste, habitat disturbance, and uncertainty."""


if __name__ == "__main__":
    revise_domain("033", "033_ufo_extraterrestrial", UAP,
                  "UAP reports and the scientific search for life beyond Earth through provenance, sensor limits, alternative explanations, and testable evidence.",
                  "original sensor files and metadata, official case reports, weather and traffic records, calibrated astronomical observations, astrobiology research, and independent analyses",
                  "Unidentified is a statement about current evidence, not proof of extraterrestrial origin. Protect witnesses, verify media provenance, test ordinary alternatives, and clearly label fiction or speculation.")
    revise_domain("034", "034_exploration_adventure", EXPLORATION,
                  "Documented journeys through route decisions, local knowledge, logistics, permissions, safety, access, and environmental effects.",
                  "expedition logs and maps, permits and official advisories, weather and route records, community accounts with consent, budgets, and environmental observations",
                  "Verify conditions and permissions at production time, credit local guides and custodians, avoid colonial first-discovery framing, and withhold unsafe or restricted route details.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
