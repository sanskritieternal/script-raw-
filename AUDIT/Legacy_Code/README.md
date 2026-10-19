# Archived Python scripts

These files record completed migrations and editorial review batches. They are outside the active production commands and should not be rerun against the current schema 5 registry without checking their paths and assumptions.

- `Editorial_Reviews/` contains 247 one-time niche review scripts. Their results live in the current `REGISTRY/Niches/*/ANGLE_PLAN.json` files. The shared `review_angle_plans.py` audit command remains at the repository root.
- `Editorial_Reviews/review_scopes_501_530.py` records the later 600-scope revision and completion of pilot evidence/limit fields. It explicitly resolves the workspace from its archive location. Its results and change ledger are already materialized; the active plans are the editable source.
- `Editorial_Reviews/review_expansion_501_530.py` records the completed expansion question-design review, primary source entry points and neighboring-niche boundaries. It explicitly resolves the workspace; its original-plan backups and change ledgers are under `AUDIT/`.
- `Migrations/` contains three completed one-time builders or movers. Their original relative paths assumed that each script lived at the repository root. They are retained for provenance.
- The older files directly in this folder are earlier migration utilities.

Current commands and their roles are listed in [PYTHON_TOOLS.md](../../PYTHON_TOOLS.md). Do not treat these archived scripts as a second source of current CAT, NICHE, angle, or OUTPUT paths.

- `Migrations/expand_531_550.py` records the reviewed first 20-candidate expansion of 2026-10-18. It resolves the root from its archive location, previews by default, and refuses to reapply against an already expanded registry. The decision/data backups live in AUDIT/CANDIDATE_REVIEW_2026_10_18; current plans remain the editable source.
