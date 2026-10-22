# System-wide reusable invocation prompts

**Output destination:** Read root `output.md` first. Use its configured root for new projects unless this request supplies an explicit override. Continue an existing project at its actual path.

Updated: 2026-10-19. Workspace: `F:\The Script of 1`.

This library applies to every registered niche and supported production workflow. No topic, niche ID, language, audience, genre, duration or episode is fixed by these templates. Supply your request and let the agent resolve the appropriate registry records. These are natural-language requests, not installed slash commands.

**Execute only the user's selected request. Reading this file does not authorize running all the examples.** If a new topic is supplied without a prompt number, use P02. If an existing episode path is supplied with a request to continue, use P09. If no topic, project or task is supplied, ask what the user wants to work on.

## Start here — universal prompt

Use this for any subject. Replace the fields, or write “choose suitable defaults” where you want the agent to decide.

```text
Read Prompt for Invoke.md and follow its common setup.
Execute P02 for this request only.

Topic or story idea: <YOUR_TOPIC_OR_IDEA>
Language: <YOUR_LANGUAGE_OR_CHOOSE_DEFAULT>
Audience: <YOUR_AUDIENCE_OR_CHOOSE_DEFAULT>
Duration: <EXACT_SECONDS_OR_CHOOSE_SUITABLE_DEFAULT>
Treatment: <EXPLAINER_DOCUMENTARY_FICTION_RETELLING_OR_CHOOSE>
Mode: autonomous.
Scope: complete the text workflow through final audit.
Media: I will generate media externally using AI tools.

Search the current registry and select the best-fitting existing niche and angle.
Show the selected route, episode question, configuration and assumptions.
Proceed with defensible defaults; ask only for essential missing information.
Validate each stage and report genuine unresolved review requirements.
```

Short form for any new topic:

> Read `Prompt for Invoke.md`. Use P02. Topic: <YOUR_TOPIC>. Language: <LANGUAGE>. Audience: <AUDIENCE>. Duration: <SECONDS>.

For questions before production:

> Read `Prompt for Invoke.md`. Use P03 for <YOUR_TOPIC>. Ask the essential setup questions first.

For existing work:

> Read `Prompt for Invoke.md`. Use P09 for <EXACT_EXISTING_EPISODE_PATH>.

P02 works across all registered subjects. P04, P06 and P07 are optional specialized treatments; choose one only when it fits your request. They do not restrict the universal workflow.

## Choose a prompt

| ID | Request | Stopping point |
|---|---|---|
| P01 | Find a niche and angle | Recommendation only |
| P02 | Complete text workflow autonomously | Phases 0–5 attempted; remaining gates reported |
| P03 | Interactive setup and production | Required interactive approval stages |
| P04 | Sacred narrative or traditional retelling | Source-specific text workflow |
| P05 | Use a known niche | Episode under a verified niche home |
| P06 | Original children's cartoon | Fictional story and production text |
| P07 | Factual technical/science explainer | Evidence-backed text workflow |
| P08 | Use an idea-bank entry | Ready-idea episode or readiness findings |
| P09 | Continue an existing episode | Next unfinished phase |
| P10 | Research first | Phase 1 |
| P11 | Narration/dialogue only | Script and necessary upstream support |
| P12 | Production bible | Phase 2 |
| P13 | Scene breakdown and prompts | Phase 3 |
| P14 | YouTube metadata | Metadata and affected consistency records |
| P15 | Compile production package | Phase 4 |
| P16 | Final audit | Seventy-item audit and remaining gates |
| P17 | Revise an episode | Requested revision and affected downstream outputs |
| P18 | Language adaptation | Language revision with timing review |
| P19 | Connected series | Series planning only |
| P20 | Deeper topics and ideas | Coverage/idea planning only |
| P21 | System audit | Evidence-backed reports and recommendations |
| P22 | Archive cleanup plan | Move proposal only |
| P23 | External AI generation handoff | Instructions from existing episode content |

## Common setup — applies to the selected prompt

### Entry files

Read these current workspace files first:

- [CLAUDE.md](CLAUDE.md)
- [Production contract](CORE/PIPELINE/CONTRACT.md)
- [Invocation reference](CORE/RULES/INVOKE_COMMANDS.md)

Use [USAGE.md](USAGE.md) and the matching phase master as needed. The production contract governs active paths, Q1–Q42 meanings, handoffs and required review. This library does not override it.

### Script storage & workspace hygiene

Any auxiliary scripts (`.py`, generator scripts, batch migration tools) produced during generation MUST be saved inside the `Scripts/` folder, never in the root directory.

### Strict compliance & verification rule

All data generated during prompts MUST strictly follow every configuration lock, source citation standard, and scene timing constraint. Phase 3 scene records must strictly preserve the schema tags (`**Field:**`) required by `Tools/projects/production_workflow.py`.

### Automatic niche selection

Search [NICHE_MASTER_LIST.md](REGISTRY/NICHE_MASTER_LIST.md), [NICHE_TAXONOMY.csv](REGISTRY/NICHE_TAXONOMY.csv), candidate niche identities and their `ANGLE_PLAN.json` files. Compare actual scope, not just keywords. Read the chosen CAT defaults and registered angle file.

Show the selected ID/title, angle slug, bounded episode question and a short reason. Do not invent an ID, silently add a niche or force an unrelated angle. Ask one concise question if the routing choice would materially change the requested content and cannot reasonably be inferred.

For a broad subject, identify distinct subtopics, cases or story directions before narrowing the episode. Preserve any boundary already supplied by the user. Use this same routing process across all registered niches.

### Modes and defaults

| Mode | Behavior |
|---|---|
| Autonomous | Record defensible assumptions and proceed through internal gates when evidence supports them; ask only for essential missing information. |
| Interactive | Ask unanswered essential questions, show configuration choices and follow the approvals in CLAUDE.md and the contract. |
| Domain preset | Begin with the niche defaults, show overrides and follow the prescribed approval gates. |

Explicit user choices take precedence over defaults. Resolve an exact runtime in seconds before calculating scenes; use the applicable CAT default if duration is unspecified. The user's established media workflow is external AI generation; record the actual Q40 choice in CONFIG. A topic request can omit niche ID and angle because the agent will find them.

### Scope, evidence and completion

Use the canonical niche/episode path under `OUTPUT/`. Check for matching existing work before creating a duplicate. Preserve configurations, snapshot provenance and approved work; distinct episodes need distinct slugs.

Factual assertions require checked evidence and claim references. Original fiction must be identified as fiction; factual assertions inside it still need support. Traditional narratives need an identified text/edition/translation or retelling, with sourced material, interpretation and invented connective dialogue distinguished.

Prepare the requested text, narration, continuity, scenes, metadata and generation instructions. **The user generates media externally.** Editorial scene duration is not a promise about a provider's clip limits; check current tool capabilities when adapting instructions to a chosen provider.

Validate completed stages and report actual outcomes. “Complete Phases 0–5” means undertake the workflow; it does not guarantee certification. A routine “go” or autonomous request is not a human review signature. Preserve applicable review gates and report blockers. These prompts do not authorize media generation, uploads or publication, and do not establish rights or actual generated files.

## P01 — Find a niche and angle first

**Use:** route any subject before creating an episode.

```text
Use the common setup in Prompt for Invoke.md. Execute P01 only.
Topic: <YOUR_TOPIC_OR_IDEA>.
Language: <LANGUAGE_OR_DEFAULT>. Audience: <AUDIENCE_OR_DEFAULT>.
Proposed duration: <SECONDS_OR_CHOOSE_DEFAULT>.

Search the actual registry and compare the best-fitting niche candidates.
Recommend one existing niche ID/title and registered angle slug, with reasons.
Suggest three bounded episode questions and identify important retelling decisions.
Stop after the recommendation; do not create an episode.
```

## P02 — Complete text workflow with automatic routing

**Use:** provide any topic and let the agent resolve setup and production text.

```text
Use the common setup in Prompt for Invoke.md. Execute P02.
Topic: <YOUR_TOPIC_OR_STORY_QUESTION>.
Language: <LANGUAGE_OR_DEFAULT>. Audience: <AUDIENCE_OR_DEFAULT>.
Duration: <SECONDS_OR_CHOOSE_DEFAULT>.
Mode: autonomous. Media: external AI generation by me.

Find the best existing niche and registered angle. Narrow the episode question.
Show the resolved configuration, record reasonable assumptions and proceed
without routine approval pauses in autonomous mode.
Undertake Phases 0–5: configuration, research, production bible, scenes,
compiled text package and final audit. Validate each completed stage.
Preserve source/retelling attribution and continuity. Ask only when essential
information cannot reasonably be inferred. Report unresolved gates honestly.
```

Use this same P02 template for any registered subject. Factual, fictional and traditional treatments receive their appropriate evidence and applicability checks.

## P03 — Interactive setup and production

```text
Use the common setup in Prompt for Invoke.md. Execute P03.
Topic: <YOUR_TOPIC_OR_IDEA>. Mode: interactive.

Find suitable niche/angle candidates and help narrow one episode question.
Ask a small group of essential questions about language, audience, exact duration,
depth, treatment and scope. Skip anything already answered.
Explain recommended defaults plainly and show the configuration.
Then follow the interactive approvals in the contract and prepare
the approved text package for my external AI generation workflow.
```

## P04 — Sacred narrative or traditional retelling

**Use only when relevant:** a sacred, traditional, mythological or cultural narrative from any tradition. Otherwise choose P02 or another fitting workflow.

```text
Use the common setup in Prompt for Invoke.md. Execute P04.
Subject: <YOUR_TRADITIONAL_NARRATIVE_OR_EPISODE>.
Language: <LANGUAGE_OR_DEFAULT>. Audience: <AUDIENCE_OR_DEFAULT>.
Duration: <SECONDS_OR_CHOOSE_DEFAULT>.
Treatment: <RETELLING_INTERPRETIVE_ANALYSIS_OR_OTHER_SPECIFIED_TREATMENT>.
Mode: autonomous.

Select the relevant existing niche and angle after checking their scope.
Identify an accessible text/edition and attributed translation or retelling.
Ask about tradition only if the choice materially changes the requested story.
Record passage locators, context and important version differences.
Distinguish sourced narrative, interpretation and invented connective dialogue.
Do not present narrative chronology as verified historical dating.
Complete the text workflow through final audit, with scene-linked prompts.
If passages cannot be inspected, report the gap and proceed only with work
that does not depend on unverified assertions. Retain applicable review gates.
```

## P05 — Use a known niche

```text
Use the common setup in Prompt for Invoke.md. Execute P05.
Niche: <EXISTING_NICHE_ID_AND_TITLE>.
Topic: <YOUR_TOPIC_OR_STORY_QUESTION>.
Preferred angle: <REGISTERED_ANGLE_SLUG_OR_CHOOSE_THE_BEST_FIT>.
Language: <LANGUAGE_OR_DEFAULT>. Duration: <SECONDS_OR_CHOOSE_DEFAULT>.
Mode: autonomous.

Verify the niche/angle against the current registry and choose a bounded case.
Report a mismatch before forcing an unsuitable treatment.
Use the CAT defaults plus my overrides. Identify the sources, creative brief
or text/retelling appropriate to the subject and treatment.
Complete the text workflow through final audit for external AI generation.
```

## P06 — Original children's cartoon

**Use only when relevant:** an original fictional cartoon for a defined child age group.

```text
Use the common setup in Prompt for Invoke.md. Execute P06.
Story idea: <YOUR_ORIGINAL_STORY_PREMISE>.
Audience: <CHILD_AGE_RANGE>. Language: <LANGUAGE>. Duration: <SECONDS>.
Tone: <YOUR_TONE_OR_CHOOSE_AGE_APPROPRIATE_DEFAULT>. Mode: autonomous.

Resolve the appropriate existing story-craft niche and registered angle.
Choose the niche and creative angle from actual registry scope;
do not assume an ID or angle before checking.
Create original characters, a clear goal, a small obstacle and a satisfying ending.
Keep actions age-appropriate and avoid imitable dangerous behavior.
Identify the story as fiction. Research real-world learning, safety or
developmental assertions rather than treating them as automatically true.
Complete the text workflow through final audit, including exact dialogue,
character/world continuity, audio intent and prompts for my external animation tools.
```

## P07 — Factual technical or science explainer

```text
Use the common setup in Prompt for Invoke.md. Execute P07.
Question: <YOUR_FACTUAL_TECHNICAL_OR_SCIENTIFIC_QUESTION>.
Audience: <AUDIENCE_OR_DEFAULT>. Language: <LANGUAGE_OR_DEFAULT>.
Duration: <SECONDS_OR_CHOOSE_DEFAULT>.
Mode: autonomous. Media: external AI generation by me.

Find the best existing niche and angle. Use original papers or official
technical documentation appropriate to each claim and version.
Separate mechanisms, invented teaching examples and measured evidence.
Label synthetic examples and independently check their arithmetic.
State task/model/version limits and exclude unsupported current-product claims.
Complete the text package through final audit with narration, precise overlays,
citations, scene prompts and an honest report of remaining gates.
```

## P08 — Use an existing idea-bank entry

```text
Use the common setup in Prompt for Invoke.md. Execute P08.
Niche: <EXISTING_NICHE_ID>. Idea: <EXISTING_IDEA_ID>.
Language: <LANGUAGE_OR_DEFAULT>. Duration: <SECONDS_OR_CHOOSE_DEFAULT>.
Mode: autonomous.

Check the current idea bank, live status and source feasibility.
If ready_for_project, use the supported --idea-id route so CONFIG retains
its creation-time snapshot. Resolve my overrides explicitly.
Check for a matching existing episode before creating a duplicate.
Continue through the text phases and final audit.
If readiness is unsupported, report gaps; do not promote the idea just to pass a gate.
```

Choose an actual idea from the live idea index or bank and verify its current status. This guide supplies no preselected idea and is not a readiness record.

## P09 — Continue an existing episode

```text
Use the common setup in Prompt for Invoke.md. Execute P09.
Project:
<EXACT_EXISTING_EPISODE_PATH>

Read CONFIG, current progress/status and actual existing deliverables.
Identify the next unfinished phase from evidence and validation.
Complete that phase, preserve existing decisions and validate the result.
Update progress with changes, checks and remaining gates.
Stop after that phase; do not create a duplicate project.
```

To continue all remaining stages, replace the last line with: “Continue all remaining text stages through final audit while reporting genuine blockers.”

## P10 — Research first

```text
Use the common setup in Prompt for Invoke.md. Execute P10 only.
Project: <EXISTING_EPISODE_PATH>

Read CONFIG and its specific question; resolve missing configuration first.
Complete Phase 1's seven documents, including the claim ledger.
Use inspectable sources, exact locators, access dates, confidence and dispute notes.
Explain coverage/exclusions and record justified financial inapplicability.
Validate through Phase 1 and stop before production or scene writing.
```

New-topic form: “Configure an episode for <YOUR_TOPIC>, using <LANGUAGE>, <AUDIENCE> and <EXACT_SECONDS>; complete its appropriate research and stop after Phase 1.”

## P11 — Narration or dialogue only

```text
Use the common setup in Prompt for Invoke.md. Execute P11 only.
Topic: <TOPIC_OR_STORY_QUESTION>
Project: <EXISTING_EPISODE_PATH_OR_NEW_EPISODE>
Language: <LANGUAGE>. Audience: <AUDIENCE>. Duration: <EXACT_SECONDS>.

Resolve/read configuration and the evidence needed for factual statements.
Write narration/dialogue in 03_Phase2_PRODUCTION_BIBLE/11_Dialogue_Script.md.
Preserve factual claim references or clearly identify original fiction.
Use natural spoken wording and an honest timing estimate.
Report evidence/timing gaps. Stop after the script and necessary upstream support.
Do not mark the full production bible or later phases complete from a script alone.
```

Script-only requests apply to any subject or genre. Fictional, factual and traditional treatments retain their appropriate evidence and labeling.

## P12 — Complete the production bible

```text
Use the common setup in Prompt for Invoke.md. Execute P12.
Project: <EXISTING_EPISODE_PATH>

Check CONFIG and Phase 1. Complete all 32 Phase 2 records with justified
applicability and accurate manifest statuses. Include narration, visual/voice rules,
continuity, beat plan, applicable numerical graphics, metadata, source limits,
asset register, audio decisions and delivery plan for external AI generation.
Record Q3/Q15/Q16/Q42 locks after the applicable internal/interactive approval.
Keep actual files, rights, recording and publication states honest.
Validate through Phase 2 and stop before scene generation.
```

## P13 — Scenes and generation prompts

```text
Use the common setup in Prompt for Invoke.md. Execute P13.
Project: <EXISTING_EPISODE_PATH>

Validate through Phase 2. Use the configured exact runtime and timing plan.
Create all required scene batches, normally 25 scenes per batch.
Include precise visual action, overlays, narration, claim/source references,
audio intent, transitions, continuity, asset IDs and scene-specific generation prompts.
Give start/end guidance and label synthetic examples. Keep exact math/text
as editorial overlays. Reconcile ledger scene links and manifest beat/asset/chapter maps.
Follow the configured approval mode, validate through Phase 3 and stop.
```

Example: 600 seconds with fixed eight-second scenes yields 75 scenes. This is editorial timing; the external tool's supported clip settings are checked separately.

## P14 — YouTube metadata only

```text
Use the common setup in Prompt for Invoke.md. Execute P14.
Project: <EXISTING_EPISODE_PATH>

Review script, research, timing and distribution choices. Complete or revise
YOUTUBE_METADATA.md: titles, description, sources, chapters, relevant tags,
thumbnail brief, pinned-comment proposal, upload decisions, publication record
and corrections workflow. Check current official guidance when policy/settings matter.
Match the actual episode promise. Use actual scene boundaries when available;
otherwise label chapter timing planned. Distinguish proposed copy from posted content.
Update affected manifest records and report whether recompilation is needed.
Do not upload, publish or rewrite unrelated content.
```

## P15 — Compile the production package

```text
Use the common setup in Prompt for Invoke.md. Execute P15.
Project: <EXISTING_EPISODE_PATH>

Validate Phases 0–3. Preview the supported shared compiler, then write the
production package when upstream checks pass. Verify scenes, narration,
citations, supplied prompts, production records, metadata and current fingerprints.
Preserve compiler history. Make corrections in authoritative upstream sources.
Validate through Phase 4 and stop before final certification.
Report remaining human-review and external-media requirements.
```

## P16 — Final audit

```text
Use the common setup in Prompt for Invoke.md. Execute P16.
Project: <EXISTING_EPISODE_PATH>

Recheck configuration, research, production records, scenes and compiled package.
Review all 70 audit items with evidence or justified N/A reasons.
Fix real in-scope defects, log revisions, rebuild affected outputs and recheck gates.
Report exact remaining findings and separate text checks from unperformed media tasks.
Do not invent reviewer approval or issue a certificate with an open required gate.
Record the actual outcome and provide a concrete review handoff if needed.
```

## P17 — Revise an episode

```text
Use the common setup in Prompt for Invoke.md. Execute P17.
Project: <EXISTING_EPISODE_PATH>
Requested change: <DESCRIBE_THE_EXACT_CHANGE_AND_WHAT_TO_PRESERVE>.

Inspect current configuration, evidence and approved decisions.
Explain the impact on narration, timing, scenes, chapters, assets and package inputs.
Make the requested revision with logged configuration/production changes.
Preserve source scope, snapshot provenance and existing history.
Rebuild affected outputs and rerun relevant checks.
Record review requirements needing renewal; an old approval does not
automatically approve materially revised content.
```

For a wording correction, replace the Change line with the exact passage and correction. Downstream work should follow the actual impact.

## P18 — Language adaptation

```text
Use the common setup in Prompt for Invoke.md. Execute P18.
Project: <EXISTING_EPISODE_PATH>
Adaptation: Change primary narration from <SOURCE_LANGUAGE> to <TARGET_LANGUAGE>.
Keep the audience, question and exact runtime unless a real conflict is found.

Preserve meaning, source qualifications, character voice and claim references.
Use natural wording in the target language, record the revision in CONFIG and the review log,
and recheck spoken fit, pronunciation, overlays, caption plan and metadata.
Update affected scenes/maps and rebuild an existing compiled package.
Actual audio fit remains pending until recorded; do not claim a generated dub.
```

## P19 — Connected series planning

```text
Use the common setup in Prompt for Invoke.md. Execute P19 only.
Series subject: <YOUR_SERIES_TOPIC_OR_STORY_WORLD>.
Language: <LANGUAGE_OR_DEFAULT>. Audience: <AUDIENCE_OR_DEFAULT>.
Plan: <NUMBER_OF_EPISODES_OR_RECOMMEND> episodes, <SECONDS_OR_RECOMMEND> each.

Find fitting existing niches and propose a coherent progression.
For each episode give a bounded question, angle, audience value, source feasibility,
scope exclusions and links to neighboring episodes. Identify prerequisites,
repeated coverage and unresolved retelling decisions.
Follow the optional planning guides for saved topic/idea/series records.
Keep readiness evidence-based. Stop at planning; do not create episode projects automatically.
```

## P20 — Deeper topics and concrete ideas

```text
Use the common setup in Prompt for Invoke.md. Execute P20 only.
Niche or subject: <NICHE_ID_OR_SUBJECT>

Review identity, angle scopes, existing topics/ideas and neighboring boundaries.
Identify meaningful coverage gaps and propose progression with prerequisites.
Develop concrete questions, cases, audience purpose and source leads.
Distinguish unverified discovery leads, inspected sources and verified claims.
Use REGISTRY/DEPTH_PLANNING_GUIDE.md and REGISTRY/IDEA_BANK_GUIDE.md for saved records.
Add useful nonduplicative proposals without an arbitrary volume target.
Stop at planning; do not create production episodes or empty banks across every niche.
```

## P21 — Audit the system

```text
Use the common setup in Prompt for Invoke.md. Execute P21.

Audit registry routing, presets, angle/idea scopes, Q1–Q42 wiring,
phase handoffs, production templates and validation against actual files.
Separate structural checks, editorial findings and unverified factual claims.
Refresh supported reports and produce a prioritized gap/fix list with evidence.
Do not restructure categories, bulk-generate niches or rewrite episodes during this audit.
Identify fixes possible locally and those requiring an actual external input or review.
```

## P22 — Archive cleanup plan

```text
Use the common setup in Prompt for Invoke.md. Execute P22 only.

Review candidates for _archive/. Trace imports, CLI entry points, tests,
runtime data paths and documentation links. Separate active dependencies,
historical records and disposable generated caches.
Propose exact source/destination paths, reasons and necessary reference updates.
Preserve current reports, unresolved findings and test fixtures unless relocation is justified.
Stop with a reviewable move plan; do not move or delete files in this request.
```

After reviewing a plan, authorize implementation explicitly: “Apply the reviewed archive plan, preserve history, update references and run affected validation.”

## P23 — Handoff for external AI generation

```text
Use the common setup in Prompt for Invoke.md. Execute P23.
Project: <EXISTING_EPISODE_PATH>
Preferred tool: <TOOL_NAME_OR_NOT_YET_SELECTED>

Inspect the actual episode package. Prepare scene IDs, intended editorial timing,
continuity references, narration, visual action, camera/motion, start/end states,
exclusions and exact overlay instructions as a usable handoff.
Keep provider-independent content clear. Adapt specific settings only after checking
current tool capabilities or documentation I supply.
If clips need splitting, retain parent scene IDs and total editorial timing.
Report missing reference files and actual rights/voice requirements.
I will generate media externally; deliver instructions without claiming rendered files.
```

## Reusable terminal command patterns

The agent handles natural-language routing. Python creation requires the actual selected niche ID and registered angle, or a selectable ready idea. Chat invocation is sufficient for asking the agent to perform the workflow; terminal commands are optional.

**Replace all placeholders before executing commands.** Angle-bracket values below are input fields, not valid literal IDs or preselected episodes. Run from the repository root. Reading this guide executes nothing.

### Set your chosen inputs

```powershell
Set-Location -LiteralPath 'F:\The Script of 1'
$nicheId = '<SELECTED_EXISTING_NICHE_ID>'
$angleSlug = '<SELECTED_REGISTERED_ANGLE_SLUG>'
$storyQuestion = '<YOUR_BOUNDED_STORY_QUESTION_ENDING_WITH_QUESTION_MARK>'
$episodeSlug = '<UNIQUE_LOWERCASE_EPISODE_SLUG>'
$episodePath = '<EXACT_EXISTING_EPISODE_PATH>'
$ideaId = '<EXISTING_READY_IDEA_ID>'
```

### Validate and preview creation

```powershell
python -m Tools.validation.validate_repository
python -m Tools.projects.create_project --id $nicheId --angle $angleSlug --story-question $storyQuestion --episode-slug $episodeSlug --mode autonomous --dry-run
```

### Create configuration and unfinished production records

This writes a new project when its destination is absent. It does not research or write the complete episode by itself.

```powershell
python -m Tools.projects.create_project --id $nicheId --angle $angleSlug --story-question $storyQuestion --episode-slug $episodeSlug --mode autonomous
```

Use `--overrides <ANSWERS_JSON_PATH>` with an existing JSON object of valid Q-ID/string values to override answers. If Q42 is VARIABLE, also supply `--scene-plan <DURATIONS_JSON_PATH>` with positive whole-second durations summing to exact Q14. Replace the placeholder paths with actual prepared files.

### Preview a ready-idea selection

```powershell
python -m Tools.projects.create_project --id $nicheId --idea-id $ideaId --mode autonomous --dry-run
```

Verify live readiness and matching existing episodes before writing. The selected idea supplies the angle/question and is snapshotted in CONFIG.

### Validate or compile existing work

```powershell
python -m Tools.validation.validate_project $episodePath --through 3
python -m Tools.projects.production_workflow compile $episodePath
```

Compilation above previews. Writing is explicit:

```powershell
python -m Tools.projects.production_workflow compile $episodePath --write
python -m Tools.validation.validate_project $episodePath --through 4
```

Choose validation depth for the work actually completed. Through Phase 5 also checks the final report, zero blockers, certificate and applicable reviewer evidence. A blocked audit retains its actual outcome.

P01–P23 are reference labels, not Python commands. There is no installed `/run_all`, `/skip` or `/approve` parser. Human review is an actual evidence-bearing decision.

## Customize your request

| Detail | Reusable input |
|---|---|
| Topic/question | <YOUR_TOPIC_OR_SPECIFIC_STORY_QUESTION> |
| Runtime | <EXACT_SECONDS>, or ask the agent to choose a suitable exact default |
| Audience | <YOUR_INTENDED_VIEWERS_OR_AGE_GROUP> |
| Language | <YOUR_NARRATION_LANGUAGE>; specify overlay language if different |
| Treatment | Source-based retelling, factual explainer or original fiction |
| Mode | Autonomous or interactive |
| Scope | Research only, script only, next phase or all text phases through audit |
| Existing work | Exact episode directory, not only a niche landing folder |
| Media workflow | External AI generation by the user; provider can be selected later |
| Limits | No invented quotes; source/edition limits retained |

Replace every `<...>` field before sending a template, or explicitly ask the agent to infer that missing choice. A niche ID identifies a subject home, an idea ID identifies a proposal, and an episode path identifies existing work. The final report must still explain whether certification is blocked.

## Production bible design records (workflow 1.1)

P02 and P12 use the current 32-document workflow for new episodes. Read CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md. Complete the six cast/world records when relevant and record justified Not applicable decisions otherwise. Keep main/supporting profiles unique; link appearance variants, locations, props/costumes, chronology and scene references. Expand shot recipes, chapter timing and the external generator profile in their existing guides. Evidence stays in Phase 1; detailed scene planning stays in Phase 3. Existing version 1.0 episodes need an explicit upgrade before the six new records become mandatory; preserve their editorial content and decisions.

## Planner, generator profile and scene index

For P02/P12/P13, read the shared workflow guide's optional planning section. New projects also receive SCENE_PLANNER.md (Phase 3) and GENERATOR_PROFILE.md (Phase 2). Existing episodes can use the prepare-planning command, preview first and then --write. Fill narrative planning and reconcile CONFIG timing before Phase 3 acceptance; leave generator selection explicitly Pending until selected and verified. Use scene-index to derive MASTER_SCENES_INDEX.md after actual scenes exist, and rebuild it after scene changes. Use sync-guides to append missing shared headings to older production copies; existing content is preserved, changed records become draft, and sections with existing headings still need editorial review. The 32-document production manifest remains unchanged. No media generation is implied.

## Full-detail production requirement

Read `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/PRODUCTION_DETAIL_STANDARD.md` before drafting or reviewing a production bible. Applicable saved files must contain usable individual profiles/specifications, episode decisions, scene references, worked examples and acceptance checks. Do not condense the bible to fit a chat response. Save coherent complete files in stages when necessary, record remaining work honestly and continue. Keep the chat summary brief without shortening the saved deliverables. Do not use repeated boilerplate or unsupported facts to pad length; justified inapplicability may remain concise. Passing the structural validator is not proof that the content has the required depth.

## Complete individual character dossiers

When full character detail is requested, use the main/supporting dossier templates. Write each individual's physical features, outfit, accessories/weapons/jewellery decision, personality, arc, expressions, voice, relationships, full consistency prompt, exclusions and reference requirements as separate usable sections. Do not substitute a combined appearance paragraph, a table of names or repeated continuity warnings. Clearly label creative appearance concepts and keep mention-only concepts inactive unless depiction is explicitly revised.

## Consistent depth across every production document

Before marking Phase 2 editorially ready, use `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/EDITORIAL_DEPTH_REVIEW_TEMPLATE.md` alongside PRODUCTION_DETAIL_STANDARD.md. Review every canonical file against its file-specific completion evidence and save actual findings/section examples in the episode's Phase 5 editorial review record. Do not claim all files reviewed when only a subset was checked. Complete each individual character/location/object/outfit dossier and required prompt; use actual relationship/event/state tables. Keep navigation summaries and justified inapplicability concise. Distinguish missing editorial content from genuinely pending model/media/reviewer work. Save complete files in coherent batches rather than truncating to fit a chat response. The 32-document manifest and configuration questions are unchanged; structural checks do not evaluate prose depth.

## Configurable project output

Read the workspace-root `output.md` before creating a new video project. Its `output_root:` value is the single shared default destination; blank or absent means the system folder's `OUTPUT` directory. The creator resolves it through `Tools.projects.output_location.resolve_output_root`. An explicit destination/`--output-root` overrides it for one project. Relative roots resolve from the system folder. Preserve `<configured root>/<niche ID_slug>/<specific project>/` and all phase subfolders; do not use the niche ID as an episode number.

Once a project exists, use its actual supplied path for every research, production, scene, package, audit, status and review file. Compile/migrate/validate commands receive that actual project path. A later setting change affects new projects and does not relocate or duplicate ongoing work. Project-local citations/links remain relative to the project; templates and registry/catalog files stay in this workspace. `OUTPUT` in older examples/catalog views denotes the default root or an existing location, not an instruction to ignore output.md.

Run `python -m Tools.projects.create_project --id <ID> --angle <registered angle> --dry-run` to inspect the configured destination without writing. Supply `--output-root "<folder>"` only for an intentional one-project override. Unknown/malformed settings report an error; do not silently save somewhere else.
