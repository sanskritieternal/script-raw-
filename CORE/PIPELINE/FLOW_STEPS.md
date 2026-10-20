# V6 flow steps — schema 5.0

Use `CORE/PIPELINE/CONTRACT.md` for the authoritative file tree, counts and gates. Use `REGISTRY/CONFIG_SCHEMA.json` for Q1–Q42.

| Step | Read | Produce | Check before advancing |
|---|---|---|---|
| Select niche | `NICHE_TAXONOMY.csv`, niche index, visual style row | Stable ID, subject, angle | Category and topic path resolve |
| Phase 0 | Subject CAT preset, niche preset, topic preset, explicit answers | `01_Phase0_Configuration/CONFIG.md` | All 42 values and provenance; exact Q14; parseable Q42; risk gate |
| Phase 1 | CONFIG and credible primary/secondary sources | Research Bible and `Claim_Ledger.md` | Material claims sourced and disputes qualified; approval in interactive/domain preset mode |
| Phase 2 | CONFIG, claim ledger, Phase 1 outputs, 16 numbered templates | Production Bible | Q3/Q15/Q16/Q42 locked; approval in interactive/domain preset mode |
| Phase 3 | Phase 1 evidence and Phase 2 locks | One `Scene_Breakdown.md` plus language scripts as needed | Sequential IDs, claim citations, duration sum equals Q14; scenes 1-25 approved first in interactive mode |
| Phase 4 | All scenes, research and locks | `Production_Package.md` | Complete script, production instructions and source references; approval in interactive/domain preset mode |
| Phase 5 | All project outputs | `Audit_Report.md`, then certificate only if passing | No blockers, placeholders, citation gaps, timing mismatch or unresolved review flags |

The default 600-second runtime and fixed eight-second scenes produce 75 scenes in one master file, reviewed in 25-scene ranges. For other fixed lengths use `ceil(Q14 seconds / Q42 seconds)` and shorten the last scene if needed. Variable timing requires a scene-by-scene sum. Changing Phase 2 locks invalidates downstream phases. Autonomous drafting never waives human review for high-risk content.

## Configurable project output

Read the workspace-root `output.md` before creating a new video project. Its `output_root:` value is the single shared default destination; blank or absent means the system folder's `OUTPUT` directory. The creator resolves it through `Tools.projects.output_location.resolve_output_root`. An explicit destination/`--output-root` overrides it for one project. Relative roots resolve from the system folder. Preserve `<configured root>/<niche ID_slug>/<specific project>/` and all phase subfolders; do not use the niche ID as an episode number.

Once a project exists, use its actual supplied path for every research, production, scene, package, audit, status and review file. Compile/migrate/validate commands receive that actual project path. A later setting change affects new projects and does not relocate or duplicate ongoing work. Project-local citations/links remain relative to the project; templates and registry/catalog files stay in this workspace. `OUTPUT` in older examples/catalog views denotes the default root or an existing location, not an instruction to ignore output.md.

Run `python -m Tools.projects.create_project --id <ID> --angle <registered angle> --dry-run` to inspect the configured destination without writing. Supply `--output-root "<folder>"` only for an intentional one-project override. Unknown/malformed settings report an error; do not silently save somewhere else.
