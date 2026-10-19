# V6 command and invocation reference

The repository provides Python commands and agent instructions. Slash phrases in older documents are conversational requests; there is no slash-command parser in this repository.

| Task | Supported command or file |
|---|---|
| List categories and IDs | `REGISTRY/NICHE_TAXONOMY.csv` |
| Check registry and presets | `python validate_repository.py` |
| Preview Phase 0 | `python create_project.py --id 275 --angle history_origins --dry-run` |
| Create Phase 0 | `python create_project.py --id 275 --angle history_origins --story-question "How did this tradition develop?"` |
| Supply answers | Add `--overrides answers.json` to the create command |
| Refresh file inventory | `python audit_repository.py` |

Valid niche IDs are three-digit stable numbers listed in `REGISTRY/NICHE_TAXONOMY.csv` (currently 001–550). Find angle slugs in the selected niche's `ALL_TOPICS_BY_NICHE.md`. Category names are the 46 `primary_category` values in the taxonomy. The canonical output path and approval gates are in `CORE/PIPELINE/CONTRACT.md`.

An agent can respond to natural-language requests such as “run Phase 1 for project 275” by following the matching phase master file and gates. `/run_all`, `/skip`, `/approve` and similar historical strings do not invoke a program by themselves.
