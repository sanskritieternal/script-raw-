# V6 command and invocation reference

The repository provides Python commands and agent instructions. Slash phrases in older documents are conversational requests; there is no slash-command parser in this repository.

| Task | Supported command or file |
|---|---|
| List categories and IDs | `REGISTRY/NICHE_TAXONOMY.csv` |
| Check registry and presets | `python -m Tools.validation.validate_repository` |
| Preview Phase 0 | `python -m Tools.projects.create_project --id 275 --angle history_origins --dry-run` |
| Create Phase 0 | `python -m Tools.projects.create_project --id 275 --angle history_origins --story-question "How did this tradition develop?"` |
| Supply answers | Add `--overrides answers.json` to the create command |
| Refresh file inventory | `python -m Tools.validation.audit_repository` |

Valid niche IDs are three-digit stable numbers listed in `REGISTRY/NICHE_TAXONOMY.csv` (currently 001–550). Find angle slugs in the selected niche's `ALL_TOPICS_BY_NICHE.md`. Category names are the 46 `primary_category` values in the taxonomy. The canonical output path and approval gates are in `CORE/PIPELINE/CONTRACT.md`.

An agent can respond to natural-language requests such as “run Phase 1 for project 275” by following the matching phase master file and gates. `/run_all`, `/skip`, `/approve` and similar historical strings do not invoke a program by themselves.
# Production bible expansion

New episodes use production workflow 1.1 with 32 documents, including six cast/world records. Follow `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md`; record justified inapplicability where appropriate. For an existing enrolled version 1.0 episode, preview `python -m Tools.projects.production_workflow upgrade "<episode>"`, then add `--write` to add draft records while preserving existing work. `migrate` remains for initial enrollment. Evidence stays in Phase 1; the detailed scene index and batch plan stay in Phase 3. No additional Q numbers or media generation are introduced.

## Optional planning commands

`python -m Tools.projects.production_workflow prepare-planning "<episode>"` previews missing planner/profile drafts. `sync-guides "<episode>"` previews missing shared sections to append to existing production guides. `scene-index "<episode>"` previews an index derived from actual scenes and CONFIG. Each needs `--write` to persist. Complete planner drafts and rebuild stale generated indexes before Phase 3 acceptance. These commands do not generate media or approve episode content.

## Full-detail production requirement

Read `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/PRODUCTION_DETAIL_STANDARD.md` before drafting or reviewing a production bible. Applicable saved files must contain usable individual profiles/specifications, episode decisions, scene references, worked examples and acceptance checks. Do not condense the bible to fit a chat response. Save coherent complete files in stages when necessary, record remaining work honestly and continue. Keep the chat summary brief without shortening the saved deliverables. Do not use repeated boilerplate or unsupported facts to pad length; justified inapplicability may remain concise. Passing the structural validator is not proof that the content has the required depth.

## Consistent depth across every production document

Before marking Phase 2 editorially ready, use `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/EDITORIAL_DEPTH_REVIEW_TEMPLATE.md` alongside PRODUCTION_DETAIL_STANDARD.md. Review every canonical file against its file-specific completion evidence and save actual findings/section examples in the episode's Phase 5 editorial review record. Do not claim all files reviewed when only a subset was checked. Complete each individual character/location/object/outfit dossier and required prompt; use actual relationship/event/state tables. Keep navigation summaries and justified inapplicability concise. Distinguish missing editorial content from genuinely pending model/media/reviewer work. Save complete files in coherent batches rather than truncating to fit a chat response. The 32-document manifest and configuration questions are unchanged; structural checks do not evaluate prose depth.

## Configurable project output

Read the workspace-root `output.md` before creating a new video project. Its `output_root:` value is the single shared default destination; blank or absent means the system folder's `OUTPUT` directory. The creator resolves it through `Tools.projects.output_location.resolve_output_root`. An explicit destination/`--output-root` overrides it for one project. Relative roots resolve from the system folder. Preserve `<configured root>/<niche ID_slug>/<specific project>/` and all phase subfolders; do not use the niche ID as an episode number.

Once a project exists, use its actual supplied path for every research, production, scene, package, audit, status and review file. Compile/migrate/validate commands receive that actual project path. A later setting change affects new projects and does not relocate or duplicate ongoing work. Project-local citations/links remain relative to the project; templates and registry/catalog files stay in this workspace. `OUTPUT` in older examples/catalog views denotes the default root or an existing location, not an instruction to ignore output.md.

Run `python -m Tools.projects.create_project --id <ID> --angle <registered angle> --dry-run` to inspect the configured destination without writing. Supply `--output-root "<folder>"` only for an intentional one-project override. Unknown/malformed settings report an error; do not silently save somewhere else.

## Script storage and clean workspace rule

All generator, builder, or temporary `.py` scripts created during any prompt or workflow MUST be placed in `Scripts/` (or artifact scratch), never in the repository root.

## Phase 3 schema rule

`Scene_Breakdown.md` records must strictly preserve the bold field markdown schema (`**Scene <num>**`, `**Duration:**`, `**Dialogue / Narration:**`, etc.) mandated by `Tools.projects.production_workflow`.
