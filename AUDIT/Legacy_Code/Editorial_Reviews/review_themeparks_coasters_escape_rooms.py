"""Editorial question designs for themed attractions, coasters, and escape rooms."""

from review_angle_plans import audit, revise_domain


THEME_PARKS = """history_origins|A Park's Design Context|Which dated plan or local condition shaped a named theme park?|Compare master plans, opening records, and later accounts.
famous_examples|One Park Land Examined|How do paths, facades, sound, and queues establish a themed place?|Walk a specified route using dated plans and recordings.
hidden_stories|Workers behind the Experience|Whose operations, maintenance, and service labor makes a land function?|Use staffing records and worker accounts with context.
beginner_explainers|From Gate to Attraction|How does a guest find, queue for, and experience a named attraction?|Map the actual journey, signage, and access conditions.
advanced_concepts|Capacity and Guest Flow|How do path width, ride throughput, and dwell time interact?|Use dated operating data and disclose measurement limits.
mysteries_unsolved_cases|A Park Plan Never Built|Which unbuilt feature can surviving plans actually confirm?|Separate concept art, approved project, and speculation.
technology_innovation|A New Park System in Practice|Which operational or storytelling problem did a documented tool address?|Compare before and after with reliability and labor effects.
people_personalities|A Designer's Documented Choice|Which named decision shaped a visitor route or attraction?|Use plans, design notes, and collaborator testimony.
major_events|A Park Expansion Opens|What changed in capacity, access, or visitor experience?|Compare plans and operating evidence across dated periods.
how_it_works|The Attraction as a System|How do entry, queue, dispatch, ride, exit, and reset connect?|Trace one published or observed workflow without exposing restricted details.
rise_fall|A Park Land Rethemed|Why was one themed area altered or removed?|Compare official plans, maintenance context, and dated visitor accounts.
then_vs_now|A Park Route Across Decades|Which paths, uses, and access options changed?|Compare dated maps and accessibility information.
future_developments|A Proposed Park Project|What permits, funding, capacity, and operating choices remain?|Treat proposal as conditional and date every source.
myths_vs_facts|An Opening-Day Legend|Does a popular claim about a park match contemporary records?|Find earliest telling and compare opening documents.
documentary_stories|Building a Park Land|How did concept, construction, testing, and opening shape one area?|Use versioned plans and credited teams.
creative_brief|The Guest's Intended Story|What experience did an attraction brief ask visitors to have?|Compare brief, layout, and observed guest path.
materials_and_tools|Sets that Must Operate Daily|How do material choices balance appearance, repair, and weather?|Identify actual components and maintenance evidence.
process_breakdown|Design to Daily Operation|Which handoffs move an attraction from concept to safe use?|Trace approvals, tests, training, and operating revisions.
composition_choice|A View along the Path|How do sightlines and sound cue the next destination?|Use mapped viewpoint and dated environment evidence.
collaborative_authorship|Who Built the Place?|Which designers, engineers, operators, and performers shaped an area?|Check credits, contracts, and official project records.
adaptation_across_media|A Story Becomes a Ride|Which story elements survive when a film or tale becomes a place?|Compare source, design plan, and guest experience.
audience_reception|A Visitor Response Sample|What do surveys or reviews show about one park feature?|State sample, time, and self-selection limits.
cultural_context|Themed Representation|Whose histories or imagery does a land borrow, and who can contest it?|Attribute sources and include relevant local perspectives.
preservation_restoration|Preserving a Changing Park|What can plans, footage, and oral histories reconstruct?|Identify versions and missing operational context.
rights_and_attribution|A Park's Licensed World|Which visual or story elements are licensed or newly created?|Check agreements and design credits where available.
style_comparison|Two Routes to Immersion|How do two attractions use space and narrative differently?|Compare matched visitor journeys and operating contexts.
creative_failure|A Park Feature Revised|What documented testing or operating issue led to a change?|Use dated design and maintenance records; avoid rumor.
field_rules_design|Rules for Using an Attraction|How are access, queue, and safety instructions communicated?|Review actual guest materials and relevant jurisdiction.
field_player_strategy|Choosing a Park Route|How do location, queue, and access needs affect a guest's options?|Use a dated map and observed conditions, not universal advice.
field_difficulty_curve|Intensity across a Visit|How are sensory and physical demands communicated between attractions?|Compare published descriptors with a specific route.
field_community_norms|Shared Space Etiquette|Which guest behaviors are requested and how are they enforced?|Use posted policies and dated observations.
field_accessibility_design|Access across the Guest Journey|Where do entrance, transfer, sensory, and information barriers occur?|Check current official accommodations and applicable standards.
"""

ROLLER_COASTERS = """history_origins|A Coaster Design Develops|Which documented design change altered a particular coaster type?|Compare dated drawings, patents, and ride records.
famous_examples|One Ride's Layout|How does a named coaster's route create its sequence of sensations?|Use verified layout and operating version, not promotional superlatives.
hidden_stories|Engineering and Operations Labor|Whose design, inspection, and daily work keeps a coaster running?|Use manufacturer and operator records where available.
beginner_explainers|From Lift to Brake Run|How does a particular train gain, exchange, and lose energy?|Use a simplified bounded diagram with units and losses.
advanced_concepts|Forces along the Track|How do speed, curvature, and rider position affect measured acceleration?|Use actual or clearly illustrative data; state uncertainty.
mysteries_unsolved_cases|An Unverified Ride Record|Which claimed speed, height, or first status lacks primary evidence?|Define measurement and compare dated official sources.
technology_innovation|A New Launch or Restraint|Which design problem did a specific innovation address?|Consult manufacturer documents and relevant standards.
people_personalities|A Coaster Engineer's Decision|Which documented choice changed a layout or train?|Check plans, patents, and attributed accounts.
major_events|A Ride Opens or Changes|What tests and operating conditions accompanied a dated opening or retrofit?|Use official documents and version dates.
how_it_works|A Coaster Cycle|How do loading, dispatch, blocks, ride, and unloading coordinate?|Describe published concepts without guessing restricted controls.
rise_fall|A Coaster Retired|What documented condition led to closure or replacement?|Compare operator statements, inspection records, and chronology.
then_vs_now|A Ride after Retrofitting|What changed in train, track, restraint, or access?|Use identified versions and documented tests.
future_developments|A Proposed Coaster|Which design and approval questions remain before opening?|Treat plans and promotional specifications as provisional.
myths_vs_facts|Speed Record by What Measure?|Do headline ride rankings use comparable measurements?|Define height, drop, speed, date, and operating condition.
documentary_stories|Designing One Coaster|How did concept, simulation, fabrication, and testing shape a ride?|Trace published artifacts and responsible teams.
creative_brief|The Intended Ride Experience|Which sensation and capacity goals did a brief set?|Compare stated goals with verified layout and operation.
materials_and_tools|Track and Train Choices|How do documented materials and geometry support a design?|Use manufacturer records and avoid engineering approval claims.
process_breakdown|From Drawing to Certification|Which design, test, inspection, and operating steps are documented?|Specify jurisdiction and applicable standard version.
composition_choice|Sequencing Ride Elements|How do turns, hills, and pauses shape anticipation?|Map actual track order and rider viewpoint.
collaborative_authorship|Who Made the Ride?|What did designer, fabricator, operator, and regulator each contribute?|Distinguish roles using official records.
adaptation_across_media|A Coaster with a Story Theme|How does narrative design alter queue and ride interpretation?|Compare theming brief and actual course.
audience_reception|Different Rider Reports|What can selected reviews show about sensation and comfort?|State sample, variation, and measurement limits.
cultural_context|A Coaster in Its Park|How do site, local rules, and visitor mix shape its operation?|Use park and jurisdiction-specific evidence.
preservation_restoration|Documenting a Removed Coaster|Which drawings, footage, trains, and records survive?|Inventory provenance and version gaps.
rights_and_attribution|Coaster Design Credit|Which company or designer is credited for a particular component?|Check patents, contracts, and operator materials.
style_comparison|Two Coaster Layouts|How do matched ride types differ in pacing and geometry?|Compare verified layouts, trains, and operating conditions.
creative_failure|A Ride Element Redesigned|What documented test or operational issue prompted a change?|Use official revision records rather than rumor.
field_rules_design|Rider Instructions and Restraints|How are eligibility and restraint checks communicated?|Read current operator rules and jurisdictional requirements.
field_player_strategy|A Rider's Choices|What options does a guest have before boarding or choosing a seat?|Use actual queue and accessibility rules, not safety workarounds.
field_difficulty_curve|Intensity through the Course|Where do accelerations and visual exposure change?|Map documented elements and avoid universal comfort ratings.
field_community_norms|Queue and Ride Conduct|Which rider behaviors are prohibited or expected?|Use posted operator rules and dated context.
field_accessibility_design|Access to a Particular Coaster|Which transfer, restraint, and communication options are provided?|Use current operator details and applicable access standards.
"""

ESCAPE_ROOMS = """history_origins|An Escape Room Format Emerges|Which documented venue or game practice shaped a room format?|Compare dated designs and avoid a single-origin claim.
famous_examples|A Room's Puzzle Path|How does one named room guide teams from first clue to final task?|Use permitted design material and avoid unapproved spoilers.
hidden_stories|Designers and Game Masters|Whose writing, fabrication, testing, and live operation make a room work?|Check credits and operator testimony.
beginner_explainers|A Puzzle Chain|How does solving one task reveal the next without arbitrary guessing?|Diagram dependencies and intended clues.
advanced_concepts|Parallel versus Linear Puzzles|How do two dependency structures affect group participation?|Compare playtest observations for a specified room.
mysteries_unsolved_cases|An Unclear Clue|Is a puzzle ambiguous, misdirecting by design, or missing information?|Review test logs and multiple team paths.
technology_innovation|A Sensor in a Room|What interaction did electronics permit and what failure mode did it add?|Use actual build and maintenance records.
people_personalities|A Designer's Revision|Why did a creator change a clue or hint?|Compare design versions and playtest notes.
major_events|A Room Reopens after Redesign|What changed in timing, access, or puzzle sequence?|Compare published versions and operator records.
how_it_works|A Game Master's Role|When do rules, monitoring, hints, and reset enter a session?|Use actual operating protocol and participant consent.
rise_fall|A Puzzle Removed|What documented difficulty or operational problem caused its removal?|Use test data, not assumed player ability.
then_vs_now|One Room across Versions|How did puzzles and access options change after renovation?|Compare date-stamped builds and guest information.
future_developments|A Proposed Interactive Room|Which prototype claims are tested and which remain speculative?|Describe playtests and constraints, not adoption forecasts.
myths_vs_facts|The Perfect Success Rate?|What does a reported completion rate measure?|Define sample, hints, time limit, and exclusions.
documentary_stories|Building an Escape Room|How did concept, fabrication, playtest, and operation reshape a room?|Trace design artifacts and test feedback.
creative_brief|The Player Promise|What narrative and challenge goals did the brief establish?|Compare intended experience with observed playtest paths.
materials_and_tools|Locks, Props, and Sensors|Which objects give information and which just dress the setting?|Inventory function, durability, and reset burden.
process_breakdown|Testing a Puzzle|Which test exposed a gap in clue visibility or feedback?|Compare prototype, observation, and revision.
composition_choice|Placing a Clue in Space|How do sightlines and object placement affect discovery?|Map player viewpoints and test behavior.
collaborative_authorship|Who Designs a Room?|How do writer, puzzle designer, fabricator, operator, and tester contribute?|Use production records and credits.
adaptation_across_media|A Story Becomes a Physical Puzzle|Which narrative information must become an action or object?|Compare source story, puzzle brief, and room experience.
audience_reception|What Playtests Show|Which moments confused or delighted actual teams?|State sample, observation method, and variation.
cultural_context|Clues for Diverse Players|Which language or prior-knowledge assumptions affect access?|Test with relevant participants and alternatives.
preservation_restoration|Archiving an Interactive Room|What can photos, plans, reset guides, and video preserve?|Identify lost tactile and group experience.
rights_and_attribution|Borrowed Art in a Room|Which images, music, or story elements require permission?|Check actual license and maker credit.
style_comparison|Two Puzzle Structures|How do sequential and parallel rooms distribute team work?|Compare dependency diagrams and playtest data.
creative_failure|A Puzzle That Was Rebuilt|Which observation led to a new clue or mechanic?|Use recorded test behavior without blaming players.
field_rules_design|The Room's Rules|What can players move, open, or ask, and how clearly is this explained?|Review briefing and in-room feedback.
field_player_strategy|Team Coordination|How do teams divide search and reasoning without losing clues?|Use observed playtests, not a universal winning recipe.
field_difficulty_curve|Challenge over the Session|Where do teams stall and what hints restore progress?|Map timed tasks and hint interventions.
field_community_norms|Respecting the Room and Team|Which behavior rules support safe shared play?|Use posted policies and staff practice.
field_accessibility_design|Multiple Paths to a Clue|Can guests with differing mobility, vision, hearing, or language access participate?|Test specific room options and published accommodations.
"""


if __name__ == "__main__":
    revise_domain("386", "386_theme_parks", THEME_PARKS,
                  "Theme parks as designed and operated visitor environments combining spatial storytelling, queues, attractions, labor, safety communication, and access.",
                  "dated park maps and plans, attraction briefs, official operating and access information, worker accounts, maintenance and archive records, and bounded visitor research",
                  "Name park, attraction, jurisdiction, and date. Do not infer safety from a promotional description or universal guest experience from selected reviews.")
    revise_domain("387", "387_roller_coasters", ROLLER_COASTERS,
                  "Roller coasters as engineered and operated rides whose layout, energy, controls, access, maintenance, and rider experiences require version-specific evidence.",
                  "manufacturer plans and publications, operator information, applicable standards and inspection records where public, measured data, and bounded rider accounts",
                  "Name ride, version, operating condition, date, and jurisdiction. Avoid engineering certification or rider safety advice from general descriptions; verify current official requirements.")
    revise_domain("388", "388_escape_rooms", ESCAPE_ROOMS,
                  "Escape rooms as designed, tested, and operated group puzzle environments with explicit rules, dependency structures, hints, accessibility, and narrative context.",
                  "design documents, dependency diagrams, prototypes, playtest observations, operator protocols, accessibility information, and identified room versions",
                  "Name room and version. Distinguish designed path from actual player behavior, protect unpublished puzzle solutions where access is restricted, and check real safety and access policies.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
