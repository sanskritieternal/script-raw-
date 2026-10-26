# Scripts directory

## Current tools

Run the topic-bank commands from the repository root:

| Purpose | Command |
| --- | --- |
| Render, index, check, or apply a reviewed expansion | `python Scripts/manage_all_topic_banks.py ...` |
| Manage niche 001 | `python Scripts/manage_ai_topics.py ...` |
| Check archived source preservation | `python Scripts/validate_topic_bank_sources.py` |
| Check saved editorial decisions | `python Scripts/validate_editorial_review.py` |
| Refresh the topic report | `python Scripts/sync_topics_report.py` |

The production scripts also remain at this level. Existing documentation and scripts call these paths directly. The root now holds these entry points plus path-addressed evidence files.

## Topic-bank evidence and inputs

- `editorial_review_inputs/` holds saved review baselines and question candidates.
- `topic_expansion_inputs/` holds expansion working inputs.
- Root-level `editorial_review_*.json`, `editorial_pass_*.json`, `expansion_*.json`, and related review files are retained at their original paths. Topic-bank records and validators refer to some of these paths directly; move them only with a coordinated reference update.
- The completed editorial Python workflows are under `archive/topic_bank/`, grouped by niche range. Their JSON and text evidence remains at the root because topic-bank records cite those exact paths.

## Historical scripts

- `archive/episode_builds/` contains one-time episode builders and phase writers.
- `archive/maintenance_patches/` contains one-time patches to production scripts.
- `archive/topic_bank/001_184/`, `185_367/`, and `368_550/` contain completed niche-range workflows.
- `archive/topic_bank/shared/` contains cross-range review workflows; `ayurveda/` holds the one-time Ayurveda integration script; `legacy_generators/` holds the earlier topic-suite generator.

Archived scripts can write to `OUTPUT`, topic banks, evidence files, or production files when run. They are retained for provenance and are not part of the current topic-bank validation workflow. See [the archive guide](archive/README.md) before rerunning one.
