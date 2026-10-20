# Archive inventory

Archived here:

- `one_time_setup/bulk_import.py`: one-time Git fast-import script for the initial repository snapshot. No active documentation, code, or tests refer to it.
- `legacy_python/expand_niches_501_530.py`: completed one-time registry expansion; retained as a historical record.
- `legacy_python/generate_niche_files.py`: old compatibility wrapper for `populate_niches.py`; no active caller.

Reviewed and retained in place:

- `AUDIT/`: historical reviews and snapshots, but current docs and tests link to files here, and tools write reports here.
- `AUDIT/Legacy_Code/` and `AUDIT/Legacy_Instructions/`: already serve as archives and are named by current documentation.
- `OUTPUT/Legacy/`: historical output explicitly preserved by `CLAUDE.md`.
- `REGISTRY/`, `CORE/`, `OUTPUT/`, `Tools/`, and `tests/`: current source data, templates, projects, scripts, and tests.
- `__pycache__/` and `Tools/__pycache__/`: generated Python cache, ignored by Git. Safe to regenerate; no value in moving it into an archive.
- `LOGS/`: empty.
