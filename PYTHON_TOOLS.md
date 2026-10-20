# Python tools

Run commands from the repository root with `python -m`. The active code is grouped by purpose under `Tools/`; tests are under `tests/`.

| Purpose | Commands |
|---|---|
| Create and manage episodes | `python -m Tools.projects.create_project`, `python -m Tools.projects.production_workflow`, `python -m Tools.projects.idea_bank` |
| Maintain registry data | `python -m Tools.registry.populate_niches`, `python -m Tools.registry.materialize_niches`, `python -m Tools.registry.build_niche_master_list` |
| Review registry plans | `python -m Tools.registry.review_angle_plans`, `python -m Tools.registry.verify_editorial_completion` |
| Validate and audit | `python -m Tools.validation.validate_project`, `python -m Tools.validation.validate_repository`, `python -m Tools.validation.audit_repository` |
| Maintain category mappings | `python -m Tools.registry.restructure_categories`, `python -m Tools.registry.reconcile_config_presets` |
| Plan content depth | `python -m Tools.depth_planning` |
| Run tests | `python -m unittest discover -s tests -v` and `python -m unittest tests.test_depth_planning -v` |

`Tools/registry/niche_home_templates.py` is a shared renderer, not a command. The root `create_project.py` is a small compatibility launcher for existing `OUTPUT/*/README.md` pages. Current scripts import one another by package path. Completed migrations are in [_archive](_archive/README.md) and [AUDIT/Legacy_Code](AUDIT/Legacy_Code/README.md).

For workflows and examples, see [USAGE.md](USAGE.md), [WORKFLOW_GUIDE.md](CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md), [IDEA_BANK_GUIDE.md](REGISTRY/IDEA_BANK_GUIDE.md), and [DEPTH_PLANNING_GUIDE.md](REGISTRY/DEPTH_PLANNING_GUIDE.md).
## Production workflow 1.1

New episodes receive 32 production documents. Existing enrolled 1.0 episodes retain their 26-document contract until upgraded. Preview `python -m Tools.projects.production_workflow upgrade "<episode>"`; add `--write` to add missing design files as drafts and update the manifest. Existing editorial files and decisions are preserved. See `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md` for applicability and compilation.

## Planning helpers

Use `python -m Tools.projects.production_workflow prepare-planning "<episode>"`, `scene-index "<episode>"` or `sync-guides "<episode>"`. All preview by default; add `--write` to persist. Prepare preserves existing planner/profile files; scene-index rebuilds only generated indexes; sync preserves original content and appends missing headings for review. See the production workflow guide for validation and compilation behavior.

## Configurable project output

Read the workspace-root `output.md` before creating a new video project. Its `output_root:` value is the single shared default destination; blank or absent means the system folder's `OUTPUT` directory. The creator resolves it through `Tools.projects.output_location.resolve_output_root`. An explicit destination/`--output-root` overrides it for one project. Relative roots resolve from the system folder. Preserve `<configured root>/<niche ID_slug>/<specific project>/` and all phase subfolders; do not use the niche ID as an episode number.

Once a project exists, use its actual supplied path for every research, production, scene, package, audit, status and review file. Compile/migrate/validate commands receive that actual project path. A later setting change affects new projects and does not relocate or duplicate ongoing work. Project-local citations/links remain relative to the project; templates and registry/catalog files stay in this workspace. `OUTPUT` in older examples/catalog views denotes the default root or an existing location, not an instruction to ignore output.md.

Run `python -m Tools.projects.create_project --id <ID> --angle <registered angle> --dry-run` to inspect the configured destination without writing. Supply `--output-root "<folder>"` only for an intentional one-project override. Unknown/malformed settings report an error; do not silently save somewhere else.
