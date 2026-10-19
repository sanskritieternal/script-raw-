"""Editorial questions for AI short films and place-based travel stories."""

from review_angle_plans import audit, revise_domain


FILM = """history_origins|From Digital Effects to Generated Shots|Which production change made one kind of generated short-film image practical?|Compare dated tools, actual production examples, and creator accounts without claiming a single origin.
famous_examples|A Generated Short Film Examined|How did one released short combine human choices with generated media?|Trace credited roles, production disclosures, and the finished shots.
hidden_stories|Labor Behind a Generated Image|Which writing, editing, performance, or cleanup work is obscured by one-click descriptions?|Use version history, credits, and attributed crew accounts.
beginner_explainers|What Is Generated in an AI Film?|Which elements of a specific film were generated, recorded, or edited by people?|Map source assets to final frames and sound, noting unknown provenance.
advanced_concepts|Consistency Across Generated Shots|How did a team maintain character, location, and lighting continuity?|Compare shot iterations, reference use, fixes, and remaining artifacts.
mysteries_unsolved_cases|An Unclear Source Asset|Can the origin of a disputed image or voice element be established?|Inspect available logs and licenses; state what provenance records cannot show.
technology_innovation|A Tool Changes the Workflow|What task became faster or newly possible in one dated production?|Measure time, iterations, quality, cost, and human correction on the same basis.
people_personalities|A Director's Creative Control|Which decisions did a named filmmaker make after model output was produced?|Use scripts, prompts when available, edit decisions, and interviews.
major_events|A Release That Sparked Debate|What specific production or disclosure choice prompted a documented response?|Trace release, credited parties, audience reaction, and corrections.
how_it_works|From Script to Generated Sequence|How does a team turn a short script into usable shots?|Follow storyboard, asset sourcing, generation, selection, compositing, sound, and review.
rise_fall|Why a Tool Was Dropped|What documented failure led a production to replace an AI technique?|Compare quality, continuity, rights, cost, and schedule evidence.
then_vs_now|Two Generations of AI Short-Film Tools|Which production tasks changed between two dated tool versions?|Use the same shot brief and quality criteria, with version details.
future_developments|A Conditional Production Test|What must a new generative film tool demonstrate before adoption?|Define measurable continuity, control, rights, accessibility, and cost criteria.
myths_vs_facts|A One-Prompt Film Claim Checked|Does a promotional claim match the actual production workflow?|Review credits, iterations, manual edits, sound, and distribution work.
documentary_stories|One Short Film's Version History|How did a generated short evolve from concept to release?|Build a dated account of drafts, asset choices, revisions, and disclosure.
creative_brief|Defining an AI Film's Intent|Which parts of a short film should be generated, and for what narrative reason?|Name audience, story goal, tool role, human roles, budget, and rights constraints.
materials_and_tools|The Production Asset Ledger|Which models, inputs, recordings, and licenses were used in one short?|Record versions, provenance, consent, permissions, and retained files.
process_breakdown|One Shot from Prompt to Cut|How many steps did one final shot require?|Trace prompt or input, candidates, selection, repair, compositing, and edit.
composition_choice|Directing a Generated Frame|How does framing focus attention despite unstable generated detail?|Compare planned composition, candidates, and final shot.
collaborative_authorship|Crediting the Film Team|How should writing, performance, design, prompting, and editing contributions be described?|Use actual agreements, credits, and task records for one project.
adaptation_across_media|From Still Image to Moving Scene|What changes when a generated concept image becomes a cinematic sequence?|Compare continuity, timing, camera motion, and sound needs.
audience_reception|What Viewers Were Told|Did disclosure affect how a defined audience understood one short?|Compare actual disclosures and consented feedback; avoid universal claims.
cultural_context|Whose Visual Language Was Used?|Does a generated film borrow a living culture's imagery without context or permission?|Trace source references, creator choices, and community perspectives.
preservation_restoration|Keeping a Generated Film Reproducible|Which files and metadata are needed to preserve a completed short?|Inventory masters, versions, models, prompts, rights, and format dependencies.
rights_and_attribution|Consent for a Face or Voice|Was a performer or source creator informed and credited for a recognizable asset?|Check project agreements and applicable rules at the production date and place.
style_comparison|Two Ways to Make a Scene|How do generated and conventional methods differ for the same story beat?|Compare control, labor, cost, artifacts, and audience effect using a fixed brief.
creative_failure|When Generation Disrupts Story|Which visual inconsistency or rights problem forced a scene revision?|Document failure, repair attempts, and final creative decision.
field_shot_design|Planning a Controllable Shot|Which camera, subject, and motion choices reduce unwanted variation?|Compare storyboard requirements with tested outputs and editing options.
field_production_workflow|A Repeatable Short-Film Pipeline|Where do human review and approval occur in one generated-film workflow?|Map versions, responsibility, quality gates, and escalation for rejected assets.
field_sound_choices|Voice and Sound Provenance|How were speech, music, ambience, and effects sourced and mixed?|Record performer consent, licenses, generation disclosure, and intelligibility checks.
field_editing_rhythm|Pacing Generated Footage|How did cuts and shot length solve or expose generation limits?|Compare rough and final edits against story intention.
field_distribution_format|A Film Across Platforms|What changes when one short is delivered for cinema, mobile, or social video?|Compare aspect ratio, subtitles, sound, disclosure, and platform terms."""


TRAVEL = """history_origins|How a Place Became a Destination|What documented change brought visitors to one previously little-known place?|Trace transport, promotion, local decisions, and earlier uses through dated records.
famous_examples|A Celebrated Hidden Place Revisited|What does one widely promoted destination actually offer and cost its hosts?|Compare visitor claims with local management, access, and community accounts.
hidden_stories|The Residents Behind the View|Whose work and everyday use are omitted from one travel portrayal?|Use attributed local accounts, land records, and service data with consent.
beginner_explainers|Finding a Place Responsibly|What should a visitor verify before planning access to a lesser-known site?|Check official status, routes, permissions, season, safety notices, and local rules.
advanced_concepts|Tourism Capacity in Practice|How can a site estimate pressure from visitors without a single magic number?|Compare ecological, infrastructure, cultural, and resident indicators in a defined season.
mysteries_unsolved_cases|A Place Name with Competing Origins|Which explanations of a site's name survive in records or oral accounts?|Attribute each version and distinguish documented history from uncertain tradition.
technology_innovation|Mapping Changes Access|How did a map or booking platform change visits to one place?|Compare dated visitor patterns, local response, and alternative causes.
people_personalities|Local Stewards of a Place|Who makes access or conservation decisions for one site?|Map formal authority and community roles from records and consented interviews.
major_events|When Visitation Changed Suddenly|What event altered access or visitor numbers at one destination?|Use dated counts, restrictions, local business accounts, and environmental observations.
how_it_works|A Visit from Arrival to Departure|Which transport, permit, guide, waste, and emergency systems support a visit?|Follow one authorized visitor route and identify responsible operators.
rise_fall|A Destination After the Hype|What changed after publicity increased or faded?|Compare visitor data, resident experience, maintenance, and ecological indicators over time.
then_vs_now|One Place Across Two Visitor Eras|How did access and local life change between two dated periods?|Use consistent boundaries, season, and measures for both periods.
future_developments|A Proposed Visitor Plan|What evidence would support or challenge a planned access expansion?|Examine public proposal, capacity data, community priorities, and conditional outcomes.
myths_vs_facts|Checking a Travel Claim|Does a claim that a site is secret, untouched, or empty fit its history and current use?|Consult local names, custodians, records, and maps; avoid erasing residents.
documentary_stories|A Route Through Local Voices|How did one destination's visitor story develop?|Build a sourced timeline including community, conservation, and business perspectives.
map_vs_ground|The Route on Screen and on Site|Does a published route match legal and practical access?|Compare current official maps, rights of way, closures, and local guidance.
route_choices|Two Ways to Reach a Site|How do routes differ in time, cost, accessibility, and impact?|Use current transport data and locally approved access points.
seasonality|A Place in Different Seasons|Which access, weather, ecological, or cultural conditions change through the year?|Use dated notices and observations; avoid promising safe access.
local_voice|Residents Define the Story|What do local residents want visitors to understand about this place?|Use attributed, consented accounts and reflect differences within the community.
landscape_process|Why the Landscape Looks This Way|Which natural and human processes shaped a visible feature?|Compare field observations, geologic or land-use records, and uncertainty.
accessibility|Who Can Actually Visit?|Which transport, terrain, cost, or information barriers affect a defined visitor group?|Check current facilities and include alternatives without implying universal access.
infrastructure|The Systems Behind a Scenic Stop|How do water, sanitation, paths, and rescue capacity constrain visits?|Use site-management records and dated capacity information.
environmental_pressure|Footprints at a Fragile Site|Which visitor effects can be measured over a defined period?|Compare baseline conditions, traffic, waste, erosion, and management response.
safety_decision|When to Turn Back|Which current conditions or official restrictions should end a planned visit?|Use site authority guidance; avoid publishing hazardous shortcuts or guarantees.
place_history|Before the Travel Post|What meanings and uses did the site have before tourist promotion?|Use local history, custodians' accounts, and archival sources.
comparison_of_places|Two Similar Sites, Different Access|Why do two places with similar scenery have different visitor policies?|Compare ownership, ecology, infrastructure, cultural significance, and local priorities.
responsible_access|Publicity and Its Costs|Should a sensitive place's exact location be publicized?|Weigh local consent, site resilience, safety, and visitor benefit without disclosing restricted coordinates.
field_map_accuracy|Checking a Place Pin|Is a map marker accurate and authorized for public use?|Verify with current official maps and custodians before publishing.
field_place_names|Which Name Belongs on the Map?|What do official and local names reveal about a place's history?|Attribute languages, dates, and community preferences without declaring one universal name.
field_local_history|A Story Told at the Site|Which evidence supports a local historical account?|Compare archival records, oral histories, and material traces with attribution.
field_visitor_access|Access Rules Today|Who may enter a specific site, by which route, and under what current conditions?|Check permits, hours, closures, mobility access, and custodial advice at production time.
field_landscape_change|A View That Changed|How has a site's landscape altered between two dated observations?|Use comparable images or measurements and assess human and natural drivers."""


if __name__ == "__main__":
    revise_domain("019", "019_ai_cinematic_short_films", FILM,
                  "AI-assisted short-film craft, production provenance, human authorship, performer consent, shot continuity, and distribution.",
                  "finished films, scripts and storyboards, asset and version ledgers, model documentation, production credits and agreements, performer consent, and dated creator accounts",
                  "Identify generated elements and their provenance. Obtain required rights and consent for people and source assets; disclose material synthetic content and verify current platform and contract terms.")
    revise_domain("020", "020_travel_hidden_places", TRAVEL,
                  "Place-based travel reporting through local history, authorized access, visitor capacity, resident voice, safety, and environmental change.",
                  "current official site and transport notices, management plans, maps, visitor and environmental data, local histories, and consented community accounts",
                  "Verify access and conditions at production time. Respect local custodians, privacy, restricted or sacred sites, and fragile habitats; do not disclose sensitive coordinates or unsafe routes.")
    rows = audit()
    print(f"Plans: {len(rows)}; reviewed question designs: {sum(r['status'] == 'editorial_question_reviewed' for r in rows)}")
