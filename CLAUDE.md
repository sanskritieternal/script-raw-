# V6 production agent — schema 5.0

Optional content depth planning: browse `REGISTRY/DEPTH_MASTER_LIST.md` and follow `REGISTRY/DEPTH_PLANNING_GUIDE.md`. Plans live inside niche `Planning/` folders and reuse existing angles and idea banks. The source library records access feasibility only. The user generates media externally; prepare the text/scene/prompt package using `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/AI_GENERATION_HANDOFF.md`. No audiovisual pilot is requested.

Read `CORE/PIPELINE/CONTRACT.md` first. Resolve every new project by stable niche ID from `REGISTRY/NICHE_TAXONOMY.csv`, its CAT file in `REGISTRY/Niches/<ID>_<Slug>/`, and a Q3 angle file in its `Angles/` folder. Its NICHE file records identity and planning links. `REGISTRY/CONFIG_SCHEMA.json` defines Q1–Q42.

## Modes

- Interactive: ask only for decisions not already supplied, show the resolved 42 answers, and request approval after Phases 1, 2 and 4 and after the first Phase 3 batch.
- Domain preset: use the current subject preset as defaults, show overrides to the user, and use the same approval gates.
- Autonomous: resolve defaults and generate drafts without routine questions. It cannot certify unsourced claims or bypass human review for High/Critical Q8, Strict/Critical Q41, sensitive living-person allegations, medical or financial advice, or material contested claims.

## Operating sequence

1. `python -m Tools.validation.validate_repository` checks the source registry. Choose an ID from `REGISTRY/NICHE_TAXONOMY.csv` and preview with `python -m Tools.projects.create_project --id <ID> --angle <angle_slug> --dry-run`; then supply a specific `--story-question "...?"` when creating CONFIG. It never overwrites an existing CONFIG.
2. Execute Phases 0 through 5 in order using `CORE/PIPELINE/CONTRACT.md` and the corresponding `MASTER_Phase*.md` source. Keep the project under `OUTPUT/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/`.
3. Use `Claim_Ledger.md` to connect material research claims to sources and scenes. A topic preset contains planning defaults, not verified facts.
4. Lock Q3, Q15, Q16 and Q42 after Phase 2 approval. If a lock changes, regenerate affected downstream work.
5. Issue a completion certificate only after Phase 5 has no blocking findings. A completed text package does not prove assets were rendered or published.

Preserve legacy outputs under `OUTPUT/Legacy/`. Do not treat them as schema 5.0 projects.


## Shared production workflow 1.1

New episode creation now supplies 32 unfinished production documents and PRODUCTION_MANIFEST.json. Complete research and episode decisions; drafts do not pass Phase 2. Read [the shared workflow guide](CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md) for applicability, manifest fields and the preview-first migrate/scaffold/compile commands. Existing un-enrolled episodes remain compatible. Compile with `python -m Tools.projects.production_workflow compile <episode> --write`; changed inputs or manual package edits require rebuilding. This does not approve sources, rights, actual media or human publication review.


## Optional episode ideas

Use [IDEA_MASTER_LIST.md](REGISTRY/IDEA_MASTER_LIST.md) and [IDEA_BANK_GUIDE.md](REGISTRY/IDEA_BANK_GUIDE.md). An optional IDEA_BANK.json belongs inside a niche home; topic is a field and angle remains a registered angle choice. `python -m Tools.projects.idea_bank init/add` preview by default and require --write to persist; `build-index` refreshes the generated index. Only ready_for_project ideas may be selected with `python -m Tools.projects.create_project --id <ID> --idea-id <IDEA-ID>`. The idea supplies angle/story; conflicting arguments are rejected. CONFIG retains its immutable source snapshot. Existing Q defaults and explicit overrides still control production. Idea readiness does not certify research, assets or human publication review. Do not populate generic ideas or empty banks across every niche.

## Full-detail production requirement

Read `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/PRODUCTION_DETAIL_STANDARD.md` before drafting or reviewing a production bible. Applicable saved files must contain usable individual profiles/specifications, episode decisions, scene references, worked examples and acceptance checks. Do not condense the bible to fit a chat response. Save coherent complete files in stages when necessary, record remaining work honestly and continue. Keep the chat summary brief without shortening the saved deliverables. Do not use repeated boilerplate or unsupported facts to pad length; justified inapplicability may remain concise. Passing the structural validator is not proof that the content has the required depth.

## Consistent depth across every production document

Before marking Phase 2 editorially ready, use `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/EDITORIAL_DEPTH_REVIEW_TEMPLATE.md` alongside PRODUCTION_DETAIL_STANDARD.md. Review every canonical file against its file-specific completion evidence and save actual findings/section examples in the episode's Phase 5 editorial review record. Do not claim all files reviewed when only a subset was checked. Complete each individual character/location/object/outfit dossier and required prompt; use actual relationship/event/state tables. Keep navigation summaries and justified inapplicability concise. Distinguish missing editorial content from genuinely pending model/media/reviewer work. Save complete files in coherent batches rather than truncating to fit a chat response. The 32-document manifest and configuration questions are unchanged; structural checks do not evaluate prose depth.

## Configurable project output

Read the workspace-root `output.md` before creating a new video project. Its `output_root:` value is the single shared default destination; blank or absent means the system folder's `OUTPUT` directory. The creator resolves it through `Tools.projects.output_location.resolve_output_root`. An explicit destination/`--output-root` overrides it for one project. Relative roots resolve from the system folder. Preserve `<configured root>/<niche ID_slug>/<specific project>/` and all phase subfolders; do not use the niche ID as an episode number.

Once a project exists, use its actual supplied path for every research, production, scene, package, audit, status and review file. Compile/migrate/validate commands receive that actual project path. A later setting change affects new projects and does not relocate or duplicate ongoing work. Project-local citations/links remain relative to the project; templates and registry/catalog files stay in this workspace. `OUTPUT` in older examples/catalog views denotes the default root or an existing location, not an instruction to ignore output.md.

Run `python -m Tools.projects.create_project --id <ID> --angle <registered angle> --dry-run` to inspect the configured destination without writing. Supply `--output-root "<folder>"` only for an intentional one-project override. Unknown/malformed settings report an error; do not silently save somewhere else.
