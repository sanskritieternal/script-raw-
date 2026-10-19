"""Editorially reviewed questions for online mysteries and game creation."""

from review_angle_plans import audit, revise_domain


MYSTERIES = """history_origins|Where an Online Mystery Began|What is the earliest verifiable appearance of one internet story?|Compare dated posts, archives, metadata, and later reposts.
famous_examples|A Famous Web Enigma Revisited|Which parts of a widely shared mystery have reliable evidence?|Separate original artifacts from interpretations and invented additions.
hidden_stories|The People Behind an Anonymous Artifact|Whose moderation, archiving, or creative work shaped one mystery?|Use voluntary, attributed accounts without seeking private identities.
beginner_explainers|How to Examine an Online Claim|Which checks help establish a post's date, source, and context?|Walk through a public, non-sensitive example and archive limits.
advanced_concepts|Evidence in a Reposted Thread|How do edits, mirrors, and missing pages complicate a claim's provenance?|Compare captures, timestamps, platform records, and uncertainty.
mysteries_unsolved_cases|A Question That Remains Open|What can and cannot be concluded about one public internet mystery?|Map competing explanations, discriminating evidence, and ethical boundaries.
technology_innovation|A Tool Changes the Search|Did reverse image search or web archives resolve one case?|Compare tool result with original records and false matches.
people_personalities|The Creator Speaks|What did a consenting creator say about one mysterious work?|Compare interview, dated work, and independent evidence without forced disclosure.
major_events|A Rumor Goes Mainstream|What changed when one online story reached news or broadcast media?|Trace dated posts, corrections, audience reach, and harms.
how_it_works|A Digital Trail's Limits|How can public artifacts be connected without overclaiming identity?|Explain URL, archive, image, and version evidence conceptually.
rise_fall|A Mystery Community Dissolves|Why did one forum or investigation group stop operating?|Compare moderation, platform change, harassment, and public records.
then_vs_now|An Internet Story Across Versions|How did one mystery's text or image change as it spread?|Compare archived versions with clear capture dates.
future_developments|What Evidence Could Resolve It?|Which lawful, non-invasive evidence would distinguish competing accounts?|State limits and avoid requesting personal data or intrusion.
myths_vs_facts|The Creepy Image's Real Source|Can the origin of one viral image be documented?|Trace publication, edits, licensing, and earliest available copy.
documentary_stories|A Mystery's Evidence Ledger|How did one online claim change from first post to debunk or open question?|Build source-linked chronology and mark unverified steps.
system_boundary|Which Platform Records Exist?|What evidence survives across site, host, archive, and social reposts?|Set boundaries and identify missing or private data.
input_output_trace|From Upload to Viral Copy|Which public copies show the path of one artifact?|Use dated links and hashes where available without deanonymization.
design_tradeoff|Anonymity and Verification|How does a platform's design affect what can be checked?|Compare privacy, moderation, timestamps, and authentication.
failure_mode|When an Archive Misleads|How can an incomplete capture create a false timeline?|Compare crawler limits, embedded content, and alternate records.
testing_limits|A Screenshot Is Not a Source|What does a screenshot fail to prove about a purported post?|Check original URL, capture date, edits, and independent corroboration.
standards_interoperability|A File Across Platforms|How can format conversion change a mysterious image or audio clip?|Compare metadata and content before and after reposting.
security_threat_model|Protecting People in an Investigation|What privacy and harassment risks arise when a mystery targets a person?|Use public ethics guidance and omit personal identifying details.
maintenance_lifecycle|A Lost Website's Remains|Which parts of a defunct site can be preserved or reconstructed?|Compare archives, source code releases, permissions, and gaps.
infrastructure_dependencies|Why a Page Vanished|Which hosting, domain, or platform changes explain one disappearance?|Use public registration and archive evidence at a non-exploitable level.
accessibility_usability|Who Could Read the Clues?|How did language, image-only text, or inaccessible design shape participation?|Compare original artifact and accessible transcriptions with provenance.
independent_replication|Can Others Verify the Finding?|Can a second researcher reproduce one non-invasive provenance check?|Publish source links and method without exposing private data.
responsible_deployment|Publishing a Mystery Episode|What checks reduce harm before presenting an unresolved internet claim?|Verify sources, seek response where appropriate, redact identities, and plan corrections.
field_software_architecture|An Interactive Puzzle's Public Code|What does released code reveal about one web mystery?|Inspect authorized artifacts without probing live systems.
field_interface_design|The Clue in the Interface|Did an interface element intentionally direct users to a clue?|Compare versions, creator statements, and alternative explanations.
field_version_changes|A Clue Appears Later|When did one website change add the contested detail?|Compare dated captures and release records; mark capture gaps.
field_open_standards|Preserving a Web Artifact|How do open formats affect whether a mystery can be studied later?|Compare accessible exports, dependencies, and archive fidelity.
field_technical_debt|Old Code, New Legend|Did a broken legacy feature become an unintended mystery?|Compare known bugs, maintenance records, and users' interpretations."""


GAMES = """history_origins|How a Game Project Started|Which player goal, platform, and team constraints shaped one game?|Compare original pitch, prototypes, budget, and release.
famous_examples|A Celebrated Game's Design Record|Which choices made one game influential and which were later myths?|Use builds, developer records, reviews, and follow-on work.
hidden_stories|Uncredited Game Labor|Whose QA, localization, contract art, and support work shaped the release?|Compare credits, contracts, and attributed worker accounts.
beginner_explainers|From Input to Play|What happens when a player acts in one game?|Trace input, rules, state change, feedback, and save behavior.
advanced_concepts|Balancing a Game System|How do rules, rewards, and player strategies interact?|Compare playtest data and emergent outcomes for one mechanic.
mysteries_unsolved_cases|Why a Feature Was Cut|Which evidence explains removal of a planned feature?|Compare prototypes, schedules, technical limits, and creator accounts.
technology_innovation|A New Engine Capability|Did one engine feature change design or production cost?|Compare builds, performance, workflow, and maintenance.
people_personalities|A Designer's Decision in Context|What alternatives did a named developer have for one mechanic?|Use dated design notes and team contributions.
major_events|A Launch-Day Failure|What did one documented release problem reveal about development?|Trace public incident, testing, patch, communication, and player effects.
how_it_works|A Game's Production Loop|How do design, code, art, sound, test, and release depend on each other?|Follow one feature through tickets, builds, playtests, and revisions.
rise_fall|A Live Game Ends|Why did one game stop receiving support or close servers?|Compare revenue, players, costs, contracts, and preservation options.
then_vs_now|One Game Across Versions|How did rules, access, performance, and player experience change?|Compare dated builds and patch notes, not remembered gameplay alone.
future_developments|A Planned Game Feature|What evidence would show whether a proposed feature improves play?|Define playtest measures, accessibility, cost, and stopping criteria.
myths_vs_facts|The One-Developer Legend|Does a game's production record support sole-author credit?|Compare original code, art, testing, publishing, and later updates.
documentary_stories|A Mechanic's Revision History|How did one rule evolve from prototype to shipped version?|Build a dated chain of design notes, tests, changes, and reception.
system_boundary|What Is the Playable Game?|Which server, store, device, account, and accessibility dependencies matter?|Map a defined player journey from purchase to continued use.
input_output_trace|A Player Action Through Code|Which components turn one input into visible feedback?|Use authorized design or code records at a conceptual level.
design_tradeoff|Freedom Versus Clarity|How did one game balance player options against understandable goals?|Compare playtests, tutorials, and player outcomes.
failure_mode|A Bug Players Encountered|What public evidence explains one game failure and its fix?|Use patch notes and reproduction records without exploit instructions.
testing_limits|A Playtest's Blind Spots|Who and what did one test fail to represent?|Compare recruitment, hardware, session length, and accessibility needs.
standards_interoperability|A Game Across Platforms|Which input, save, performance, or store rules affected porting?|Compare platform requirements and actual versions.
security_threat_model|Player Data and Online Play|What risks did one online feature create for privacy or fairness?|Review public safeguards and outcomes without cheat or exploit steps.
maintenance_lifecycle|Keeping a Game Playable|How do patches, server costs, and old hardware affect long-term access?|Trace support timeline and preservation options.
infrastructure_dependencies|When the Server Is Part of the Game|What happens to play when one network or account service ends?|Compare offline modes, ownership terms, and player remedies.
accessibility_usability|A Game With Multiple Input Needs|Can players with defined access needs complete one core task?|Test remapping, captions, visual cues, pacing, and alternatives with users.
independent_replication|Can Another Team Repeat the Result?|Does one design claim hold in another game or player group?|Compare mechanics, recruitment, measures, and context.
responsible_deployment|Launching an Online Game|Which readiness checks cover fairness, safety, accessibility, and support?|Review load tests, moderation, incident response, and player communication.
field_software_architecture|A Game Feature's Components|How do engine, gameplay code, assets, and services support one mechanic?|Use public or authorized diagrams and version records.
field_interface_design|Reading the Game State|Does the UI let players understand a critical choice?|Compare user tests, errors, accessibility, and feedback.
field_version_changes|A Patch Changes Play|How did one patch alter balance, performance, or access?|Compare builds, notes, telemetry limits, and player accounts.
field_open_standards|Can the Game Be Preserved?|Do file formats and released tools permit future access?|Examine rights, documentation, dependencies, and emulation limits.
field_technical_debt|A Shortcut That Grew Costly|Which early design decision made later updates harder?|Trace code or production records and avoid hindsight blame."""


if __name__ == "__main__":
    revise_domain("130", "130_internet_mysteries", MYSTERIES,
                  "Internet mysteries as source-tracing investigations of public artifacts, archives, versions, rumors, and unresolved questions.",
                  "original public posts and files, dated web archives, metadata with provenance, creator statements given voluntarily, independent corroboration, and correction records",
                  "Name artifact, platform, capture date, and claim. Protect private people; do not deanonymize, harass, probe live systems, or present speculation as fact.")
    revise_domain("131", "131_game_development", GAMES,
                  "Game development through design, code, art, testing, player access, labor, distribution, updates, and preservation.",
                  "dated design and production records, playable builds and patch notes, authorized code or documentation, playtest methods, player feedback, and attributed developer accounts",
                  "Name game, build, platform, team, and date. Distinguish design goals from tested player outcomes, credit contributors, and avoid exploit or cheat instructions.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
