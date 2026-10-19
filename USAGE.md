# Using the V6 content factory

Optional depth planning starts at [DEPTH_MASTER_LIST.md](REGISTRY/DEPTH_MASTER_LIST.md). Read [the planning guide](REGISTRY/DEPTH_PLANNING_GUIDE.md) for topic maps, series, source references and ready ideas. After editing mapped ideas or planning JSON, rebuild both idea and depth indexes. The user's external AI generation workflow uses [AI_GENERATION_HANDOFF.md](CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/AI_GENERATION_HANDOFF.md); the current work ends with the text/scene/prompt handoff.

The registry has 550 stable niche IDs, 550 CAT configurations, 550 NICHE identity files, 17,069 planning angles, 550 output landing folders and 46 subject tags. Niches 001 and 004 remain pilots; the other 548 plans have reviewed question designs. IDs 501-530 have 20 angles each; the 20 niches added in the next batch have 453 angles in total, with subject-specific counts. Sources and neighboring boundaries are recorded in expansion plans; episode facts still require Phase 1 research. Browse `REGISTRY/NICHE_MASTER_LIST.md` and read `REGISTRY/ANGLE_SCOPE_GUIDE.md` before selecting an episode.

## Start an episode

1. Find the ID in `REGISTRY/NICHE_TAXONOMY.csv` or browse `REGISTRY/Niches/README.md`.
2. Open `REGISTRY/Niches/<ID>_<Slug>/NICHE_<ID>_<Slug>.md`, review its CAT defaults, then choose one angle from `Angles/ALL_TOPICS_BY_NICHE.md`.
3. Run `python validate_repository.py` and `python create_project.py --id 275 --angle history_origins --dry-run`.
4. Run `python create_project.py --id 275 --angle history_origins --story-question "What specific question will this episode answer?"`. It writes `OUTPUT/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/01_Phase0_Configuration/CONFIG.md` and refuses to overwrite an existing CONFIG. `--episode-slug` and `--overrides answers.json` are optional. For variable Q42, pass `--scene-plan durations.json` with positive whole seconds summing to Q14.
5. Continue through Phases 1–5 using `CORE/PIPELINE/CONTRACT.md`. Research claims require evidence; final completion requires an audit with no blockers.

## Where information lives

| Path | Purpose |
|---|---|
| `REGISTRY/NICHE_TAXONOMY.csv` | Stable IDs, subject tags and canonical paths |
| `REGISTRY/CATEGORY_INDEX.md` | Browse 46 broad subject tags |
| `REGISTRY/Niches/README.md` | Browse all 550 niche homes |
| `REGISTRY/NICHE_MASTER_LIST.md` | All IDs, angle counts, plan status and file routes |
| `REGISTRY/ANGLE_SCOPE_GUIDE.md` | Scope fields, editing commands and use in research |
| `REGISTRY/Niches/<ID>_<Slug>/CAT_<ID>_<Slug>.md` | Editable Q1–Q42 defaults for one niche |
| `REGISTRY/Niches/<ID>_<Slug>/NICHE_<ID>_<Slug>.md` | Identity and planning links; no Q answers |
| `REGISTRY/Niches/<ID>_<Slug>/ANGLE_PLAN.json` | Editable angle scopes, questions, evidence prompts and boundaries |
| `REGISTRY/Niches/<ID>_<Slug>/Angles/` | Generated Q3 choices and index; counts vary by niche |
| `OUTPUT/<ID>_<Slug>/` | Niche landing folder and episode projects |
| `REGISTRY/CONFIG_SCHEMA.json` | Schema 5.0 Q labels and seed values |
| `REGISTRY/MASTER_VISUAL_STYLE.md` | Visual direction by stable ID |
| `CORE/PIPELINE/CONTRACT.md` | Paths, gates and handoffs |

Run `python populate_niches.py --verify-content` to check all angle files and `python materialize_niches.py --verify-content` to check identities and output landings. The default `populate_niches.py` is read-only; `--create-missing` creates absent angles without overwriting edits; `--sync-content` regenerates angle files from the plans. Add `--id 448` to check or sync only one niche. `materialize_niches.py` creates missing CAT, NICHE and landing files without overwriting edited CATs.

Run `python review_angle_plans.py --scope-audit` to check the scope context in all 550 plans. New project configurations snapshot the selected angle's scope. Narrow it to the actual episode in the story question and Phase 1 research summary.

Run `python validate_project.py <project-directory> --through <phase-number>` to check a project's completed phase structure, IDs, timing and citation links. It does not judge whether evidence supports a claim or whether assets were produced. `OUTPUT/Legacy/` contains historical projects. Old path maps and the schema 4 archive are in `REGISTRY/` and `AUDIT/Niche_Home_Migration_2026-10-16/`.


## Shared production workflow 1.0

New episode creation now supplies 26 unfinished production documents and PRODUCTION_MANIFEST.json. Complete research and episode decisions; drafts do not pass Phase 2. Read [the shared workflow guide](CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md) for applicability, manifest fields and the preview-first migrate/scaffold/compile commands. Existing un-enrolled episodes remain compatible. Compile with `python production_workflow.py compile <episode> --write`; changed inputs or manual package edits require rebuilding. This does not approve sources, rights, actual media or human publication review.


## Reviewed niche expansion - 2026-10-18

The external 100-candidate list was compared with existing plans before adopting IDs 531-550. See [candidate decisions](AUDIT/CANDIDATE_REVIEW_2026_10_18/CANDIDATE_COMPARISON.md). External P531-P630 labels are proposal references, not reserved registry IDs. Existing IDs, CATs and angle plans are preserved; remaining proposals are future candidates, angle work or cross-topic links.


## Optional episode ideas

Use [IDEA_MASTER_LIST.md](REGISTRY/IDEA_MASTER_LIST.md) and [IDEA_BANK_GUIDE.md](REGISTRY/IDEA_BANK_GUIDE.md). An optional IDEA_BANK.json belongs inside a niche home; topic is a field and angle remains a registered angle choice. `idea_bank.py init/add` preview by default and require --write to persist; `build-index` refreshes the generated index. Only ready_for_project ideas may be selected with `create_project.py --id <ID> --idea-id <IDEA-ID>`. The idea supplies angle/story; conflicting arguments are rejected. CONFIG retains its immutable source snapshot. Existing Q defaults and explicit overrides still control production. Idea readiness does not certify research, assets or human publication review. Do not populate generic ideas or empty banks across every niche.
