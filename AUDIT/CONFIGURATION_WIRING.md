> **Historical report ? schema 5 supersedes these paths.** See `AUDIT/NICHE_HOME_MIGRATION.md` and `CORE/PIPELINE/CONTRACT.md` for the active layout.

# Configuration and pipeline wiring — schema 4.0

## Canonical question source

`REGISTRY/CONFIG_SCHEMA.json` defines exactly Q1-Q42 and the default values. Q1 is the subject category from `REGISTRY/NICHE_TAXONOMY.csv`. A `CAT_<SubjectCategory>.md` file supplies category defaults; one `NICHE_<ID>_<Slug>.md` file per niche supplies its resolved defaults and visual style. The selected topic angle overrides Q3, and the topic's visual registry value overrides Q15. Explicit project answers have final precedence. `create_project.py` writes each value and its source to CONFIG and refuses to overwrite an existing project configuration.

The earlier collision is resolved: Q4 means Content Depth Level, Q5 Visual/Media Priority, Q6 Interview/Documentation Segments, Q7 Content Sensitivity Level, Q8 Legal/Accuracy Concern, Q21 Graphics Requirement and Q42 Scene Duration Strategy. Q24 carries source quality; file naming is a project convention, not Q42. The old answers remain available in `REGISTRY/LEGACY_TOPIC_DEFAULTS.csv`.

## Dependent values

- Q14 is an exact runtime in seconds before Phase 3. The active default is `600 seconds`.
- Q42 is `FIXED n-SECOND` or `VARIABLE`. Fixed count is `ceil(Q14 / n)` and the last scene may be shorter. Variable projects provide `--scene-plan` with positive whole-second durations whose sum equals Q14; Phase 3 must match each planned duration.
- Q18/Q19 record actual language choices. Q15 visual style and Q40 generation method remain separate.
- Q8 High/Critical, Q41 Strict/Critical, contested Q10/Q31 answers, or explicit risk flags cause a pending human-review gate. The final certificate requires named, dated approval when that gate applies.

## Phase handoffs

| From | Required evidence | Next consumer |
|---|---|---|
| Phase 0 | All 42 answers, provenance, schema version, exact timing and risk gate in CONFIG | Research brief and scene arithmetic |
| Phase 1 | Six research documents plus `Claim_Ledger.md`, with source locations, access dates, confidence and dispute status | Phase 2 decisions and Phase 5 audit |
| Phase 2 | 16 numbered production files; locked Q3/Q15/Q16/Q42 | Phase 3 scenes |
| Phase 3 | Sequential scenes, exact duration plan and claim IDs | Phase 4 compilation |
| Phase 4 | Compiled script, asset directions, metadata and all used claim IDs | Phase 5 audit |
| Phase 5 | `Audit_Report.md` with A1–G10 statuses and evidence; certificate only after blockers are resolved | Text-package status |

`Visual_Style_Quick_Reference.md` in the Phase 2 source directory is a reference, not a seventeenth required output. A nonfinancial project keeps the financial files with a reasoned `Not applicable` entry rather than invented figures. The canonical project path is `OUTPUT/<SubjectCategory>/Topics/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/01_Phase0_Configuration/CONFIG.md`.

## Verification

`python -m Tools.validation.validate_repository` checks all 500 IDs, 46 category presets, 500 niche presets and output landing folders, 7,500 topic files and 46 Phase 0 pilots. `python -m Tools.registry.populate_niches --verify-content` compares every generated topic and index against the current source. `python -m Tools.validation.validate_project <path> --through 5` checks structural handoffs, timing, claim ID links and all 70 audit rows. The sourced 16-second physics text pilot under `AUDIT/PILOTS/` passes all six gates; a separate variable-duration Phase 0 fixture passes timing validation. These checks cannot establish that a source truly supports a claim or that a video asset has been produced.
