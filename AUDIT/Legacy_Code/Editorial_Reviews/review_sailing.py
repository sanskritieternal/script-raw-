"""Editorial question review for sailing and yachting."""

from review_angle_plans import audit, revise_domain


SAILING = """history_origins|A Harbor's Sailing History|How did sailing uses of one harbor change over time?|Compare charts, port records, boat types, and local accounts.
famous_examples|A Celebrated Voyage Revisited|What can original records establish about one famous sailing passage?|Compare logs, charts, weather, equipment, and later retellings.
hidden_stories|Work Behind a Recreational Voyage|Whose labor makes one yacht's journey possible?|Trace boatyard, marina, provisioning, rescue, and service work.
beginner_explainers|What a Passage Plan Must Cover|Which decisions belong in a plan for one short sail?|Use a bounded route, current chart, weather, tides, crew, and alternatives.
advanced_concepts|Wind, Tide, and Route Choice|How can the fastest plotted route be the wrong passage plan?|Compare forecast uncertainty, tidal windows, hazards, and shelter.
mysteries_unsolved_cases|A Voyage with Conflicting Accounts|Which claims about one historic sailing incident can be verified?|Separate logs, rescue records, forecasts, testimony, and unknowns.
technology_innovation|Electronic Navigation in Practice|What does one navigation device improve, and where can it mislead?|Compare chart currency, signal limits, power dependence, and backup methods.
people_personalities|The Skipper's Decisions|How did one skipper document and revise a voyage plan?|Use attributed logs and contemporaneous conditions without hindsight bias.
major_events|A Storm That Changed Sailing Practice|Which documented safety changes followed one severe event?|Compare inquiry findings, rule revisions, training, and adoption.
how_it_works|How a Sailing Boat Moves|How do sail, keel, hull, and rudder interact on one design?|Use model drawings and measured performance without claiming one universal setup.
rise_fall|A Yacht Class Grows and Declines|Why did one boat design gain or lose users?|Compare build cost, rule changes, maintenance, moorings, and replacement designs.
then_vs_now|The Same Coastal Passage Across Eras|How did charts, forecasts, communications, and rescue options change?|Bound vessel and route; compare dated equipment and risk context.
future_developments|A Lower Impact Marina Proposal|Would one marina change reduce its documented environmental burden?|Check design, power, waste handling, habitat, demand, and costs.
myths_vs_facts|A Claim About Sailing Safety|Does one familiar safety claim hold for a defined boat and trip?|Check incident evidence, vessel class, conditions, and reporting limits.
documentary_stories|A Working Day at a Yacht Harbor|What decisions and labor shape one day's departures and returns?|Follow consented crews and staff with current weather and port records.
map_vs_ground|Charted Water and Actual Access|Does a charted route reflect present conditions and restrictions?|Verify notices, depth, tide, obstacles, moorings, and local authority rules.
route_choices|Two Passages to One Destination|How do two routes differ for a specified yacht and crew?|Compare forecast, tides, distance, shelter, traffic, and safe alternatives.
seasonality|A Harbor Across the Sailing Year|How do seasonal winds and water conditions alter access?|Use historical observations, current forecasts, facilities, and traffic.
local_voice|Whose Waterfront Is It?|How do sailors, fishers, residents, and operators view one harbor change?|Use attributed consultation and document each group's stakes.
landscape_process|Why This Anchorage Is Sheltered|How do coastline, seabed, wind, and swell shape one anchorage?|Use charts and observations, distinguishing typical from current conditions.
accessibility|Who Can Join a Sailing Trip?|Which boat and marina features enable or exclude different participants?|Check boarding, facilities, training, costs, and consented user accounts.
infrastructure|A Marina as a Service System|Which facilities keep boats and people safe in one harbor?|Map berths, access, power, waste, rescue links, and maintenance.
environmental_pressure|A Popular Anchorage's Footprint|What environmental effects are documented at one anchorage?|Check habitat surveys, waste, mooring methods, traffic, and uncertainty.
safety_decision|Go, Delay, or Cancel?|What evidence supports one voyage decision under changing conditions?|Compare forecast updates, vessel limits, crew, alternatives, and official warnings.
place_history|A Waterfront Converted to Yachting|Who gained and lost access when one shore changed use?|Trace land records, policy, local livelihoods, and public access.
comparison_of_places|Two Sailing Harbors Compared|Why do two harbors offer different access and safety?|Compare geography, tides, services, fees, rescue, and user mix.
responsible_access|Sailing Through a Protected Area|How do current access rules protect wildlife and other users?|Check local restrictions, seasonal limits, enforcement, and observed impact.
field_training_method|From Course to Competence|What can one sailing training course demonstrate?|Review syllabus, instructor qualification, assessed skills, and limits.
field_equipment_design|A Lifejacket's Intended Use|What protection does one flotation device provide for its user and setting?|Check applicable standards, fit, upkeep, and limitations.
field_rules_and_fairness|Who Has the Right of Way?|How are collision and local harbor rules applied in one real setting?|Use current official rules, vessel types, traffic records, and enforcement.
field_injury_prevention|Learning from a Marine Incident|Which system changes could reduce harm in one documented case?|Use inquiry findings, weather, equipment, training, and rescue response.
field_event_logistics|A Regatta's Shared Waters|How does one event manage safety and access for all water users?|Review notices, permits, race area, support boats, weather, and emergency plan.
"""


if __name__ == "__main__":
    revise_domain("140", "140_sailing_yachting", SAILING,
                  "Sailing and yachting through voyages, vessel design, harbor access, navigation, work, safety, and environmental effects.",
                  "dated charts and port records, official marine forecasts and notices, vessel specifications, incident inquiries, current local rules, habitat surveys, and consented crew and waterfront accounts",
                  "Name vessel, crew, route, waters, jurisdiction, and date. Treat navigation and safety choices as documentary questions, never a live voyage plan; check current charts, weather, warnings, and local rules.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
