# The Script of 1

This repository holds the niche registry and a six-phase workflow for preparing episode research, scripts, scenes, and production packages.

| Folder | Contents |
|---|---|
| `CORE/` | Production contract, rules, and phase templates |
| `REGISTRY/` | Niche taxonomy, plans, angles, and source records |
| `OUTPUT/` | Episode projects and their deliverables |
| `Tools/projects/` | Project creation, idea banks, and production packaging |
| `Tools/registry/` | Registry generation, mapping, and editorial checks |
| `Tools/validation/` | Project and repository validation, file audit |
| `tests/` | Automated contract, idea, and workflow tests |
| `AUDIT/` | Review reports, pilots, and historical evidence |
| `_archive/` | Completed setup and migration scripts |

Run commands from this folder. For example:

```powershell
python -m Tools.validation.validate_repository
python -m Tools.projects.create_project --id 275 --angle history_origins --dry-run
python -m unittest discover -s tests -v
```

Read [USAGE.md](USAGE.md) for the production workflow and [PYTHON_TOOLS.md](PYTHON_TOOLS.md) for the tool list.

## Configurable project output

Read the workspace-root `output.md` before creating a new video project. Its `output_root:` value is the single shared default destination; blank or absent means the system folder's `OUTPUT` directory. The creator resolves it through `Tools.projects.output_location.resolve_output_root`. An explicit destination/`--output-root` overrides it for one project. Relative roots resolve from the system folder. Preserve `<configured root>/<niche ID_slug>/<specific project>/` and all phase subfolders; do not use the niche ID as an episode number.

Once a project exists, use its actual supplied path for every research, production, scene, package, audit, status and review file. Compile/migrate/validate commands receive that actual project path. A later setting change affects new projects and does not relocate or duplicate ongoing work. Project-local citations/links remain relative to the project; templates and registry/catalog files stay in this workspace. `OUTPUT` in older examples/catalog views denotes the default root or an existing location, not an instruction to ignore output.md.

Run `python -m Tools.projects.create_project --id <ID> --angle <registered angle> --dry-run` to inspect the configured destination without writing. Supply `--output-root "<folder>"` only for an intentional one-project override. Unknown/malformed settings report an error; do not silently save somewhere else.
