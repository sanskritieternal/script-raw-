# Shared production workflow 1.1

For this user's external AI media generation workflow, follow [AI_GENERATION_HANDOFF.md](AI_GENERATION_HANDOFF.md). Deliver the researched scene/prompt package; audiovisual generation is outside the current planning task. Planned asset status remains valid and does not assert that media exists.

Reusable across all registered niches. Configuration question schema remains 5.0; production workflow versioning is separate. The shared templates contain no episode 501 medical story.

## 1. Shared templates

Preserve outputs 00-15. Sixteen supporting documents are now standard. The original ten are: YOUTUBE_METADATA.md, STORY_BEAT_MAP.md, CHARACTER_WORLD_GUIDE.md, CAMERA_ANIMATION_GUIDE.md, MUSIC_SOUND_GUIDE.md, ASSET_REGISTER.md, DELIVERY_CHECKLIST.md, REVIEW_REVISION_LOG.md, VIEWER_GLOSSARY.md and ORIGINALITY_REVIEW.md. The six additional records are MAIN_CHARACTERS.md, SUPPORTING_CHARACTERS.md, CHARACTER_APPEARANCE_LOCK.md, LOCATIONS_ENVIRONMENTS.md, PROPS_COSTUMES.md and RELATIONSHIPS_TIMELINE.md. PRODUCTION_WORKFLOW.json defines applicability, supporting field checks and placement in the compiled package.

## 2. Applicability by episode

Each version 1.1 episode has all 32 files plus PRODUCTION_MANIFEST.json. Each document has status `draft`, `complete` or `not_applicable`. Drafts fail Phase 2. Allowed not_applicable entries need an episode-specific reason of at least 15 characters and matching “Not applicable” text in the document; remove scaffold content. Core identity, evidence, narration, asset, delivery and review records cannot be waived.

Documentary character/world records describe narrator, sourced entities, periods and depiction limits; fiction records character design, relationships and world continuity. Clearly separate invention from factual assertions. Financial, visualization, glossary or distribution documents may be inapplicable with a justified reason. Beat count fits the episode; it is not fixed at 25. Factual claims still need evidence inside fiction. Niche registry entries are not completed episodes.

## 3. Pipeline connections

Phase 0 supplies identity/language/risk/timing; Phase 1 supplies checked evidence; Phase 2 completes decisions and locks; Phase 3 supplies actual scene and asset references; Phase 4 compiles the snapshot; Phase 5 audits findings and actual review evidence. No command creates research conclusions, media licenses, human approvals or publication details.

New CONFIG files include `Production workflow version: 1.1`. Older episodes without that marker or a manifest retain their former checks. Adding a manifest enrolls an old episode; removing the manifest from a marked new episode does not bypass validation. No existing episode is silently bulk-migrated.

## 4. Generation and safe migration

`Tools.projects.create_project` now writes Phase 0 and all 32 draft production files, using the selected niche's actual configuration. Each scaffold is explicitly unfinished and cannot pass production validation. Complete Phase 1 evidence before accepting Phase 2.

Preview an existing episode without writing:

```powershell
python -m Tools.projects.production_workflow migrate "OUTPUT/<niche>/<episode>"
```

Write missing files and manifest explicitly:

```powershell
python -m Tools.projects.production_workflow migrate "OUTPUT/<niche>/<episode>" --write
```

`scaffold` has the same safe missing-file behavior. Existing editorial documents and CONFIG are preserved byte-for-byte. On initial enrollment only, `--adopt-existing` explicitly marks preserved documents internally complete after your review; new files remain draft. It does not approve evidence, rights, rendering or publication. Existing manifests cannot be reset by migration. Historical OUTPUT/Legacy projects are excluded.

### Structured mappings

The manifest records all 32 statuses, exact Q3/Q15/Q16/Q42 locks, and these arrays once scenes are available:

```json
{
  "beats": [{"start": 1, "end": 2, "claims": ["C001"]}],
  "assets": [{"id": "G01", "scenes": [1, 2], "status": "planned", "file": "graphics/G01.svg"}],
  "chapters": [{"start_seconds": 0, "title": "The question"}]
}
```

This illustrates the field structure, not any real episode's scene count. Beat ranges cover actual scenes exactly once, in order, and list the union of their claim IDs. Asset IDs must appear in ASSET_REGISTER.md and mappings cover all scenes; this explicitly links assets without rewriting legacy scene fields. Planned assets need not exist. Created/reviewed assets require actual in-episode files; reviewed entries require review evidence.

Applicable YouTube chapters start at zero and use unique actual scene boundaries; time/title lines in YOUTUBE_METADATA.md must agree exactly with the manifest. If distribution makes YouTube inapplicable, record the reason and leave chapters empty. Unknown actual URL/date/license/reviewer values may honestly remain Pending; unfinished editorial content may not be disguised as complete.

## 5. Compilation and validation

```powershell
python -m Tools.validation.validate_project "OUTPUT/<niche>/<episode>" --through 3
python -m Tools.projects.production_workflow compile "OUTPUT/<niche>/<episode>"
python -m Tools.projects.production_workflow compile "OUTPUT/<niche>/<episode>" --write
python -m Tools.validation.validate_project "OUTPUT/<niche>/<episode>" --through 4
```

Compilation requires Phase 0-3 validation. It retains scenes verbatim, extracts narration and source citations, includes all research Markdown and all 32 production documents in eleven canonical sections, and records asset mappings and hashes. AI prompts are episode-specific if applicable; no tool is chosen automatically.

Package_Inputs.json fingerprints CONFIG, research, production/manifest, scene files, shared workflow specification, compiler implementation and package output. Upstream changes, compiler changes or manual package edits invalidate Phase 4 until rebuilding. Previous packages are retained under `05_Phase4_PRODUCTION_PACKAGE/History/<hash>/`.

The dedicated AI generation section collects supplied scene prompts, overlay instructions, reference inputs, start/end states, asset IDs and execution records. Inline and multiline prompt fields are supported. It invents no prompt for a scene that has none and selects no provider. The complete original scene records are still preserved in the scene section. Older packages without the compiler fingerprint require rebuilding before passing current Phase 4 freshness checks.

Validation checks status, placeholders, links, locks, fields, claim/scene references, beat coverage, assets, chapter timing and package freshness. It cannot establish source truth, originality, real rights, actual audiovisual quality, platform eligibility or reviewer authenticity. Required human-review/certification gates remain unchanged.

## 6. Existing-project rollout and tests

Preview migration per episode, preserve existing work, assess applicability, finish missing content and fill actual mappings before compilation. The earlier 501 episode folder is absent in the current workspace; it cannot be migrated here. Do not reconstruct its evidence or approvals from chat memory. Existing episode copies are used to test migration without rewriting historical pilots.

Run `python -m unittest tests.test_contract tests.test_production_workflow -v`. Coverage includes fresh scaffolds, safe migration, applicability, fixed/variable timing, scene/metadata/assets, package invalidation/rebuild and retained human-review gates. Registry topics remain unchanged.

## 7. Version 1.1 upgrade and design records

Version 1.0 manifests retain their 26-document contract in PRODUCTION_WORKFLOW_V1.json. Version 1.1 requires 32 documents. Old un-enrolled episodes still use their original checks; initial migrate/scaffold enrolls them in 1.1. Existing enrolled episodes use upgrade instead:

```powershell
python -m Tools.projects.production_workflow upgrade "OUTPUT/<niche>/<episode>"
python -m Tools.projects.production_workflow upgrade "OUTPUT/<niche>/<episode>" --write
```

Upgrade preserves CONFIG, existing editorial files, document statuses, locks and mappings. It adds six draft manifest entries, creates missing files, and changes the manifest version to 1.1. A preexisting new file is preserved and enrolled as draft, never automatically approved. Running upgrade again is a no-op. Review applicability and complete the new records before Phase 2 acceptance. Expanded older guides are not automatically inserted into episode copies: incorporate applicable new sections during editorial review. No existing complete text is overwritten. Shared compiler/spec changes invalidate old package fingerprints until rebuilding.

Character/world overview links authoritative profiles and existing configuration/status records. One individual has one profile and stable ID; main/supporting importance differs from story role. Appearance variants have effective events/scene ranges. Use stable location, prop and costume IDs in relevant scene fields, asset records and revision logs. All six design records allow justified Not applicable entries; validation checks status, required sections, placeholders and links, not the truth of descriptions or visual consistency of ungenerated media. Current validation does not parse a design-ID graph or certify every scene/variant reference; review those explicitly.

Use the shared [Phase 3 planning guide](../04_Phase3_SCENE_BREAKDOWN/SCENE_PLANNING_GUIDE.md) for the scene index and batch plan. Research and historical references remain in Phase 1 with claim/source locators. The chapter outline lives in STORY_BEAT_MAP.md. CAMERA_ANIMATION_GUIDE.md owns shot recipes and the selected generator/model profile; AI_GENERATION_HANDOFF.md is shared guidance, not a 33rd required episode output. No additional configuration questions or fixed provider limits are introduced.
# Optional planning outputs and guide synchronization

The 32-document production manifest remains unchanged. New project creation also supplies an optional Phase 3 `SCENE_PLANNER.md` and Phase 2 `GENERATOR_PROFILE.md`. Their reusable sources are [SCENE_PLANNER_TEMPLATE.md](../04_Phase3_SCENE_BREAKDOWN/SCENE_PLANNER_TEMPLATE.md) and [GENERATOR_PROFILE_TEMPLATE.md](GENERATOR_PROFILE_TEMPLATE.md). These records support the workflow; they do not prove editorial completion or media execution. Existing episodes opt in with the preview-first commands below.

```powershell
python -m Tools.projects.production_workflow prepare-planning "OUTPUT/<niche>/<episode>"
python -m Tools.projects.production_workflow prepare-planning "OUTPUT/<niche>/<episode>" --write
python -m Tools.projects.production_workflow sync-guides "OUTPUT/<niche>/<episode>"
python -m Tools.projects.production_workflow sync-guides "OUTPUT/<niche>/<episode>" --write
python -m Tools.projects.production_workflow scene-index "OUTPUT/<niche>/<episode>"
python -m Tools.projects.production_workflow scene-index "OUTPUT/<niche>/<episode>" --write
```

Prepare creates only missing records; it derives the planner's exact scene timing from CONFIG and leaves narrative/batch/evidence decisions draft. Complete the planner's placeholders before Phase 3 acceptance. An existing opted-in planner's timing table must match CONFIG. To revise timing, update CONFIG deliberately and reconcile the planner; prepare never overwrites existing work. The generator profile starts Pending selection and may stay pending for text planning. After selection, verify and record the actual provider/model's current capabilities, references and clip assembly. Validation checks profile structure, not the truth of provider claims.

Sync appends shared sections whose exact headings are absent from existing production documents; it preserves every original byte and marks changed manifest entries draft for editorial review. It does not replace or refresh text under headings that already exist. Reconcile outdated content within those sections manually. Repeating sync is a no-op until shared headings change.

Scene-index derives `MASTER_SCENES_INDEX.md` from CONFIG and actual scenes: IDs, exact start/end times, durations, chapter, claims and source file links. It refuses absent/incomplete scenes or timing mismatch and preserves a manually authored index. Only an index carrying the generated signature may be rebuilt. Phase 3 checks an existing index for stale content or edits; rebuild after scene changes. No index file is required for older episodes that have not opted in. Index structure does not imply research, editorial or media approval.

The compiler includes optional planner/index records with scene content and the optional generator profile with generation instructions. Their content and the helper implementation are fingerprinted; changes require package rebuilding. These checks do not establish narrative completeness, every design-ID relationship, actual provider capability or rendered quality. Run `python -m unittest tests.test_contract tests.test_production_workflow tests.test_planning_records -q` for focused coverage.

## Full-detail production requirement

Read `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/PRODUCTION_DETAIL_STANDARD.md` before drafting or reviewing a production bible. Applicable saved files must contain usable individual profiles/specifications, episode decisions, scene references, worked examples and acceptance checks. Do not condense the bible to fit a chat response. Save coherent complete files in stages when necessary, record remaining work honestly and continue. Keep the chat summary brief without shortening the saved deliverables. Do not use repeated boilerplate or unsupported facts to pad length; justified inapplicability may remain concise. Passing the structural validator is not proof that the content has the required depth.

## Consistent depth across every production document

Before marking Phase 2 editorially ready, use `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/EDITORIAL_DEPTH_REVIEW_TEMPLATE.md` alongside PRODUCTION_DETAIL_STANDARD.md. Review every canonical file against its file-specific completion evidence and save actual findings/section examples in the episode's Phase 5 editorial review record. Do not claim all files reviewed when only a subset was checked. Complete each individual character/location/object/outfit dossier and required prompt; use actual relationship/event/state tables. Keep navigation summaries and justified inapplicability concise. Distinguish missing editorial content from genuinely pending model/media/reviewer work. Save complete files in coherent batches rather than truncating to fit a chat response. The 32-document manifest and configuration questions are unchanged; structural checks do not evaluate prose depth.

## Configurable project output

Read the workspace-root `output.md` before creating a new video project. Its `output_root:` value is the single shared default destination; blank or absent means the system folder's `OUTPUT` directory. The creator resolves it through `Tools.projects.output_location.resolve_output_root`. An explicit destination/`--output-root` overrides it for one project. Relative roots resolve from the system folder. Preserve `<configured root>/<niche ID_slug>/<specific project>/` and all phase subfolders; do not use the niche ID as an episode number.

Once a project exists, use its actual supplied path for every research, production, scene, package, audit, status and review file. Compile/migrate/validate commands receive that actual project path. A later setting change affects new projects and does not relocate or duplicate ongoing work. Project-local citations/links remain relative to the project; templates and registry/catalog files stay in this workspace. `OUTPUT` in older examples/catalog views denotes the default root or an existing location, not an instruction to ignore output.md.

Run `python -m Tools.projects.create_project --id <ID> --angle <registered angle> --dry-run` to inspect the configured destination without writing. Supply `--output-root "<folder>"` only for an intentional one-project override. Unknown/malformed settings report an error; do not silently save somewhere else.
