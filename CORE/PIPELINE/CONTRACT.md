# V6 production contract (schema 5.0)

This is the authoritative routing and handoff contract for the active V6 repository. Detailed phase files explain production practice; if an older example uses a six-folder taxonomy, an old `CAT_` preset, a duration range for Q14, or `01_Phase0_CONFIG`, use this contract and `REGISTRY/CONFIG_SCHEMA.json` instead.

## Inputs and identity

- Resolve the stable three-digit niche ID, current subject category, slug and topic path from `REGISTRY/NICHE_TAXONOMY.csv`.
- Each registered niche has one home: `REGISTRY/Niches/<ID>_<Slug>/`. `CAT_<ID>_<Slug>.md` supplies editable Q1–Q42 defaults; `NICHE_<ID>_<Slug>.md` records identity and planning links without Q answers. The 46 subject categories are taxonomy tags and schema seed overrides, not parallel runtime CAT files.
- Angle choices live at `REGISTRY/Niches/<ID>_<Slug>/Angles/<ID>_<Slug>_<Angle>.md`. Each supplies Q3 only. Every niche has an editable `ANGLE_PLAN.json`; generated drafts require editorial review before an angle becomes a specific episode. The original 15 slugs remain stable, and there is no fixed maximum angle count.
- Each angle plan entry has a distinct scope, a focus question, evidence directions and interpretation limits. New Phase 0 configurations snapshot the selected angle's Editorial scope section. Use that guidance to choose a concrete episode case and record coverage and exclusions in Phase 1. Scope does not add a Q number. See `REGISTRY/ANGLE_SCOPE_GUIDE.md`.
- The matching `OUTPUT/<ID>_<Slug>/` landing folder holds episode projects.
- Production format (documentary, animation, AI film), language and audience are configuration fields; they do not change the subject category.
- Q1-Q42 IDs and labels come from `REGISTRY/CONFIG_SCHEMA.json` version 5.0. Merge precedence: taxonomy Q1, niche CAT defaults, angle Q3, explicit project overrides. Record each answer's source.

## Canonical project path

### Optional episode idea layer

Optional topic maps and series plans live inside each niche's `Planning/` directory. Read [DEPTH_PLANNING_GUIDE.md](../../REGISTRY/DEPTH_PLANNING_GUIDE.md); the shared source library records access feasibility, not verified episode claims. These planning references add no Q numbers and do not override CAT defaults, selected angles or CONFIG snapshots. Repository validation checks their references and generated views. Copy relevant coverage/exclusions into Phase 1 deliberately.

Concrete proposals may live in `REGISTRY/Niches/<ID>_<Slug>/IDEA_BANK.json`; the topic remains a field, not another competing registry folder. Use [the idea guide](../../REGISTRY/IDEA_BANK_GUIDE.md) and IDEA_BANK_SCHEMA.json. Banks are optional; status, source leads, gaps and selected angle are checked by idea_bank.py and repository validation.

`create_project.py --id <ID> --idea-id <IDEA-ID>` requires ready_for_project status, derives angle/story question and rejects conflicting explicit values. CONFIG preserves the full creation-time idea snapshot, bank reference and integrity hash; later bank edits do not change the project. Q1-Q42 meanings and explicit override rules remain intact. Readiness is source feasibility only, not Phase 1 factual verification or human publication approval. Existing direct --angle/--story-question creation remains supported.

`OUTPUT/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/`

The project ID preserves the original niche ID. The episode slug is derived from the specific story question or supplied with `--episode-slug`, so multiple episodes can reuse one niche and angle without collision. CONFIG records a Q3 snapshot; later edits to an angle plan do not rewrite an existing project. `REGISTRY/LEGACY_TOPIC_PATHS.csv` and `REGISTRY/NICHE_HOME_PATHS.csv` map former paths.

## Six phases and gates

| Phase | Directory | Required output and exit condition |
|---|---|---|
| 0 Configuration | `01_Phase0_Configuration/` | `CONFIG.md` with all 42 answers, schema version, exact Q14 seconds, Q42 timing, language and review gate. `create_project.py` builds and validates this file. |
| 1 Research Bible | `02_Phase1_RESEARCH_BIBLE/` | `Research_Summary.md`, `Facts_Documented.md`, `Financial_Figures_Verified.md` when applicable, `Timeline_Accuracy_Check.md`, `Source_List_with_Links.md`, `MASTER_CONTEXT_v1.md`, and `Claim_Ledger.md`. Mark nonfinancial data `Not applicable` rather than invent figures. Every material scripted claim must have evidence before Phase 2. |
| 2 Production Bible | `03_Phase2_PRODUCTION_BIBLE/` | The 16 numbered outputs `00_...` through `15_...`. `Visual_Style_Quick_Reference.md` is a source reference, optional as an output. Lock Q3, Q15, Q16 and Q42 after approval. |
| 3 Scene Breakdown | `04_Phase3_SCENE_BREAKDOWN/` | Numbered batch files, 25 scenes per batch by default, with scene durations summing to Q14 and claim IDs linking to Phase 1. For fixed duration, count is `ceil(Q14 / Q42)` and the last scene may be shorter. |
| 4 Production Package | `05_Phase4_PRODUCTION_PACKAGE/` | `Production_Package.md` compiling scenes, narration, visual and audio directions, source references, metadata and unresolved flags. No claim may lose its citation. |
| 5 Final Audit | `06_Phase5_FINAL_AUDIT/` | `Audit_Report.md` with evidence for each gate. Issue `Completion_Certificate.md` only if no blocking findings remain. A completed text package is not proof that video assets were rendered or published. |

Phase 1, Phase 2 and Phase 4 require explicit approval in interactive and domain preset modes. Phase 3 batch 1 requires approval in interactive mode. Autonomous mode may pass internal gates only after the required evidence is present. Q8 High/Critical, Q41 Strict/Critical, contested Q10/Q31 answers, or explicit risk flags for living-person allegations, medical or financial advice, and contested religious or historical claims require human review before publication status. `create_project.py --risk-flags ...` records those flags. Final certification requires an approved reviewer and date in CONFIG when review is required. A disclaimer does not replace evidence or review.

## Handoff checks

1. Phase 0 to 1: use Q1 subject, Q3 angle, Q7/Q8/Q41 risk, Q18/Q19 languages and Q14 timing. Do not treat preset defaults as verified research facts.
2. Phase 1 to 2: every material scripted claim has a claim ID, locatable source and section/page, exact access date, evidence summary, confidence, `Verified` status, dispute assessment and scene mapping. Exclude unsupported claims; a ledger ID alone does not make a claim verified.
3. Phase 2 to 3: use locked style, voiceover, scene template and timing; changing a lock requires regenerating downstream phases.
4. Phase 3 to 4: scene IDs are unique and sequential; durations sum exactly to Q14; every material factual scene references claim IDs.
5. Phase 4 to 5: audit script, visuals and metadata against CONFIG, research and production locks. Block completion for placeholders, broken citations or unresolved high risk findings.

## Validation commands

### Expanded production workflow 1.0

Keep the original 16 numbered Phase 2 files and add ten supporting templates plus PRODUCTION_MANIFEST.json, as defined by `03_Phase2_PRODUCTION_BIBLE/PRODUCTION_WORKFLOW.json`. See [the workflow guide](03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md) for all 26 documents, applicability, mappings, compiler and migration.

New CONFIG files are marked `Production workflow version: 1.0`; create_project.py supplies unfinished production scaffolds. Phase 2 requires completed applicable documents and matching locks; permitted Not applicable entries need reasons. Phase 3 checks beat/asset/chapter maps against actual scenes, claims and metadata. Beat count is not fixed. Existing unmarked/un-enrolled episodes keep previous checks; migration is explicit, preview-first and preserves editorial files. OUTPUT/Legacy is excluded.

For enrolled episodes, compile Phase 4 with `python production_workflow.py compile <project> --write`. All production documents and scene citations are included; Package_Inputs.json tracks input/output hashes. Changed inputs or manual package edits require recompilation. No command issues human approval or a completion certificate. This production version is separate from question schema 5.0.

- `python validate_repository.py` validates taxonomy paths, a CAT and NICHE file and output landing folder per registered niche, all base and curated angle files, links and one Phase 0 pilot per subject category.
- `python create_project.py --id 275 --angle history_origins --dry-run` previews project creation.
- A write requires `--story-question "...?"` with a specific researchable question. Angle choices are candidates, not finished topics.
- For `Q42: VARIABLE`, pass `--scene-plan plan.json` with positive whole-second durations summing exactly to Q14. The project validator checks each scene against that plan.
- `python validate_project.py <project-directory> --through 5` checks produced phase files, scene timing, claim IDs and all 70 final-audit rows. It is a structural check; source support and rendered assets require direct review.
- `python audit_repository.py` refreshes the checkmarked byte-read inventory and structural report.
