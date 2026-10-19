# How the V6 content factory works

For deeper content planning, use [topic maps and series](REGISTRY/DEPTH_MASTER_LIST.md) and [the planning guide](REGISTRY/DEPTH_PLANNING_GUIDE.md). Five pilot niches connect coverage, prerequisites, registered angles, ideas and reusable source references. The user generates media externally; [AI generation handoff](CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/AI_GENERATION_HANDOFF.md) explains how the existing production documents support that workflow.

The taxonomy answers **what the subject is**. Q3 answers **what angle the episode takes**. Q15 and Q40 describe **how it looks and is produced**. Keeping those decisions separate prevents documentary, animation and AI film from becoming competing subject folders.

Each stable ID listed in the registry maps to one of 46 subject categories in `REGISTRY/NICHE_TAXONOMY.csv`. Each ID has its own `REGISTRY/Niches/<ID>_<Slug>/` home: a CAT file with editable Q1–Q42 defaults, a NICHE identity file, and Q3-only angle choices. Its `OUTPUT/<ID>_<Slug>/` folder holds episodes. The subject category seeds new CATs but does not compete with the niche CAT at runtime. Taxonomy locks Q1; the selected angle supplies Q3; explicit project answers have final precedence. `REGISTRY/CONFIG_SCHEMA.json` version 5.0 defines question meanings. Q14 is an exact runtime; Q42 is a scene-duration plan.

Each angle also defines its research focus, coverage, evidence directions and limits in `ANGLE_PLAN.json`. Generated angle files display this guidance together, and new project configurations include a snapshot for Phase 1. Choose a concrete episode case and record its coverage and exclusions in the research summary. See `REGISTRY/ANGLE_SCOPE_GUIDE.md` for examples and editing commands.

The project then moves through six phases: configuration, evidence-backed research, production rules, scene breakdown, compiled package and final audit. `CORE/PIPELINE/CONTRACT.md` is the active phase and output contract. `CORE/PIPELINE/FLOW_STEPS.md` gives the sequence. Phases 1 and 2 establish facts and locked creative choices before scenes are drafted. Scenes cite claim IDs and their durations sum to the configured runtime. The final audit can block completion.

Run `python validate_repository.py` to check the registry and `python create_project.py --id 275 --angle history_origins --dry-run` to preview a project. Run `python audit_repository.py` to refresh the file-read inventory. The audit reports under `AUDIT/` describe the migration and remaining editorial gaps. Existing work under `OUTPUT/Legacy/` is historical.


## Shared production workflow 1.0

New episode creation now supplies 26 unfinished production documents and PRODUCTION_MANIFEST.json. Complete research and episode decisions; drafts do not pass Phase 2. Read [the shared workflow guide](CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md) for applicability, manifest fields and the preview-first migrate/scaffold/compile commands. Existing un-enrolled episodes remain compatible. Compile with `python production_workflow.py compile <episode> --write`; changed inputs or manual package edits require rebuilding. This does not approve sources, rights, actual media or human publication review.


## Optional episode ideas

Use [IDEA_MASTER_LIST.md](REGISTRY/IDEA_MASTER_LIST.md) and [IDEA_BANK_GUIDE.md](REGISTRY/IDEA_BANK_GUIDE.md). An optional IDEA_BANK.json belongs inside a niche home; topic is a field and angle remains a registered angle choice. `idea_bank.py init/add` preview by default and require --write to persist; `build-index` refreshes the generated index. Only ready_for_project ideas may be selected with `create_project.py --id <ID> --idea-id <IDEA-ID>`. The idea supplies angle/story; conflicting arguments are rejected. CONFIG retains its immutable source snapshot. Existing Q defaults and explicit overrides still control production. Idea readiness does not certify research, assets or human publication review. Do not populate generic ideas or empty banks across every niche.
