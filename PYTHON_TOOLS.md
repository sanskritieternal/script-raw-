# Python tools

Run current commands from the repository root. These files remain there because the pipeline, tests, and documentation refer to their paths or import them directly.

| Task | Current entry point |
|---|---|
| Create and validate an episode project | `create_project.py`, `validate_project.py` |
| Materialize and check niche homes and angles | `materialize_niches.py`, `populate_niches.py`, `niche_home_templates.py`, `validate_repository.py` |
| Refresh registry documentation and audits | `build_niche_master_list.py`, `review_angle_plans.py`, `audit_repository.py`, `verify_editorial_completion.py` |
| Validate contract behavior | `test_contract.py` |
| Preserve registry expansion and migration compatibility | `expand_niches_501_530.py`, `generate_niche_files.py`, `restructure_categories.py`, `reconcile_config_presets.py` |

The root holds 19 Python files. Completed editorial batch scripts, scope and expansion review batches, and three one-time migration scripts are in [AUDIT/Legacy_Code](AUDIT/Legacy_Code/README.md). They are historical records; active plans are under `REGISTRY/Niches/`. Run `python review_angle_plans.py --scope-audit` for the current scope ledger and `python verify_editorial_completion.py` for the full registry review milestone (`--original-500` checks the earlier milestone).


| Expanded production task | Tool |
|---|---|
| Scaffold, preview migration, compile versioned packages | `production_workflow.py` |
| Workflow migration, mapping and stale-package tests | `test_production_workflow.py` |

Read [WORKFLOW_GUIDE.md](CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md) before migration. The CLI previews by default; writing requires --write.


| Idea planning task | Tool |
|---|---|
| Optional bank init/add, validation and master index | `idea_bank.py` |
| Readiness, duplicate, selection and snapshot tests | `test_idea_bank.py` |

See [IDEA_BANK_GUIDE.md](REGISTRY/IDEA_BANK_GUIDE.md) for schemas and commands.

## Optional content depth planning

`python Tools/depth_planning.py build-index` validates editable depth/source records and regenerates topic maps, series plans, the depth index and source reading view. `python Tools/depth_planning.py validate` checks references and freshness without writing. `validate_repository.py` includes this gate. Run `python -m unittest Tools.test_depth_planning -v` for broken-reference, source-status and prerequisite-cycle checks. See [DEPTH_PLANNING_GUIDE.md](REGISTRY/DEPTH_PLANNING_GUIDE.md).
