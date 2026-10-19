# V6 production agent — schema 5.0

Optional content depth planning: browse `REGISTRY/DEPTH_MASTER_LIST.md` and follow `REGISTRY/DEPTH_PLANNING_GUIDE.md`. Plans live inside niche `Planning/` folders and reuse existing angles and idea banks. The source library records access feasibility only. The user generates media externally; prepare the text/scene/prompt package using `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/AI_GENERATION_HANDOFF.md`. No audiovisual pilot is requested.

Read `CORE/PIPELINE/CONTRACT.md` first. Resolve every new project by stable niche ID from `REGISTRY/NICHE_TAXONOMY.csv`, its CAT file in `REGISTRY/Niches/<ID>_<Slug>/`, and a Q3 angle file in its `Angles/` folder. Its NICHE file records identity and planning links. `REGISTRY/CONFIG_SCHEMA.json` defines Q1–Q42.

## Modes

- Interactive: ask only for decisions not already supplied, show the resolved 42 answers, and request approval after Phases 1, 2 and 4 and after the first Phase 3 batch.
- Domain preset: use the current subject preset as defaults, show overrides to the user, and use the same approval gates.
- Autonomous: resolve defaults and generate drafts without routine questions. It cannot certify unsourced claims or bypass human review for High/Critical Q8, Strict/Critical Q41, sensitive living-person allegations, medical or financial advice, or material contested claims.

## Operating sequence

1. `python validate_repository.py` checks the source registry. Choose an ID from `REGISTRY/NICHE_TAXONOMY.csv` and preview with `python create_project.py --id <ID> --angle <angle_slug> --dry-run`; then supply a specific `--story-question "...?"` when creating CONFIG. It never overwrites an existing CONFIG.
2. Execute Phases 0 through 5 in order using `CORE/PIPELINE/CONTRACT.md` and the corresponding `MASTER_Phase*.md` source. Keep the project under `OUTPUT/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/`.
3. Use `Claim_Ledger.md` to connect material research claims to sources and scenes. A topic preset contains planning defaults, not verified facts.
4. Lock Q3, Q15, Q16 and Q42 after Phase 2 approval. If a lock changes, regenerate affected downstream work.
5. Issue a completion certificate only after Phase 5 has no blocking findings. A completed text package does not prove assets were rendered or published.

Preserve legacy outputs under `OUTPUT/Legacy/`. Do not treat them as schema 5.0 projects.


## Shared production workflow 1.0

New episode creation now supplies 26 unfinished production documents and PRODUCTION_MANIFEST.json. Complete research and episode decisions; drafts do not pass Phase 2. Read [the shared workflow guide](CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md) for applicability, manifest fields and the preview-first migrate/scaffold/compile commands. Existing un-enrolled episodes remain compatible. Compile with `python production_workflow.py compile <episode> --write`; changed inputs or manual package edits require rebuilding. This does not approve sources, rights, actual media or human publication review.


## Optional episode ideas

Use [IDEA_MASTER_LIST.md](REGISTRY/IDEA_MASTER_LIST.md) and [IDEA_BANK_GUIDE.md](REGISTRY/IDEA_BANK_GUIDE.md). An optional IDEA_BANK.json belongs inside a niche home; topic is a field and angle remains a registered angle choice. `idea_bank.py init/add` preview by default and require --write to persist; `build-index` refreshes the generated index. Only ready_for_project ideas may be selected with `create_project.py --id <ID> --idea-id <IDEA-ID>`. The idea supplies angle/story; conflicting arguments are rejected. CONFIG retains its immutable source snapshot. Existing Q defaults and explicit overrides still control production. Idea readiness does not certify research, assets or human publication review. Do not populate generic ideas or empty banks across every niche.
