"""One-time migration of active V6 instructions to schema 3.0.

Archives the previous files under AUDIT/Legacy_Instructions before replacement.
Refuses to overwrite an archive, so it cannot silently rerun.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "AUDIT" / "Legacy_Instructions"
SCHEMA = json.loads((ROOT / "REGISTRY" / "CONFIG_SCHEMA.json").read_text(encoding="utf-8"))

RULES = """# V6 production agent — schema 3.0

Read `CORE/PIPELINE/CONTRACT.md` first. Resolve every new project by stable niche ID from `REGISTRY/NICHE_TAXONOMY.csv`, the current subject preset in `REGISTRY/Categories/`, and the topic angle file. `REGISTRY/CONFIG_SCHEMA.json` defines Q1–Q42. Older presets are archived under `AUDIT/Legacy_Instructions/Category_Presets/` and are not inputs.

## Modes

- Interactive: ask only for decisions not already supplied, show the resolved 42 answers, and request approval after Phases 1, 2 and 4 and after the first Phase 3 batch.
- Domain preset: use the current subject preset as defaults, show overrides to the user, and use the same approval gates.
- Autonomous: resolve defaults and generate drafts without routine questions. It cannot certify unsourced claims or bypass human review for High/Critical Q8, Strict/Critical Q41, sensitive living-person allegations, medical or financial advice, or material contested claims.

## Operating sequence

1. `python validate_repository.py` checks the source registry. For a new project use `python create_project.py --id <1-500> --angle <angle_slug> --dry-run`, then run without `--dry-run` to create CONFIG. It never overwrites an existing CONFIG.
2. Execute Phases 0 through 5 in order using `CORE/PIPELINE/CONTRACT.md` and the corresponding `MASTER_Phase*.md` source. Keep the project under `OUTPUT/<SubjectCategory>/Topics/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/`.
3. Use `Claim_Ledger.md` to connect material research claims to sources and scenes. A topic preset contains planning defaults, not verified facts.
4. Lock Q3, Q15, Q16 and Q42 after Phase 2 approval. If a lock changes, regenerate affected downstream work.
5. Issue a completion certificate only after Phase 5 has no blocking findings. A completed text package does not prove assets were rendered or published.

Preserve legacy outputs under `OUTPUT/Legacy/`. Do not treat them as schema 3.0 projects.
"""

DOCS = {
    "CLAUDE.md": RULES,
    "CORE/RULES/agents.md": RULES,
    "CORE/RULES/CLAUDE.md": "# V6 agent entry point\n\nUse the current [production contract](../PIPELINE/CONTRACT.md), [root agent instructions](../../CLAUDE.md), and `REGISTRY/CONFIG_SCHEMA.json`. The repository has 14 subject categories and six phases numbered 0–5. The category and topic preset lookup uses `REGISTRY/NICHE_TAXONOMY.csv`. Historical agent instructions are archived under `AUDIT/Legacy_Instructions/`.\n",
    "CORE/RULES/autonomous.md": """# Autonomous production rules — schema 3.0

Autonomous mode drafts phases in the order and folders defined by `CORE/PIPELINE/CONTRACT.md`. Use taxonomy Q1, category defaults, topic Q3/Q15, then explicit overrides. Write answer provenance and schema version to CONFIG.

At each gate verify the required output, not just its presence. Phase 1 must provide a source-backed claim ledger; Phase 2 must lock Q3/Q15/Q16/Q42; Phase 3 timing must sum exactly to Q14; Phase 4 must preserve claim citations; Phase 5 must report unresolved blockers. The agent may continue drafting while a review is pending, but must not mark a blocked phase approved or certify completion.

Human review is required before publication status for Q8 High/Critical, Q41 Strict/Critical, living-person allegations, medical or financial advice, or material contested claims. If a source cannot be checked, mark the claim unverified and keep it out of the final factual script. No unsupported statement becomes verified merely because an earlier phase included it.

Track project progress in its subject category. Never modify historical projects under `OUTPUT/Legacy/` during new production. Do not skip a phase or silently overwrite an approved output.
""",
    "CORE/RULES/INVOKE_COMMANDS.md": """# V6 command and invocation reference

The repository provides Python commands and agent instructions. Slash phrases in older documents are conversational requests; there is no slash-command parser in this repository.

| Task | Supported command or file |
|---|---|
| List categories and IDs | `REGISTRY/NICHE_TAXONOMY.csv` |
| Check registry and presets | `python validate_repository.py` |
| Preview Phase 0 | `python create_project.py --id 275 --angle history_origins --dry-run` |
| Create Phase 0 | `python create_project.py --id 275 --angle history_origins` |
| Supply answers | `python create_project.py --id 275 --angle history_origins --overrides answers.json` |
| Refresh file inventory | `python audit_repository.py` |

Valid niche IDs are three-digit stable numbers 001–500. Find angle slugs in the selected niche's `ALL_TOPICS_BY_NICHE.md`. Category names are the 14 `primary_category` values in the taxonomy. The canonical output path and approval gates are in `CORE/PIPELINE/CONTRACT.md`.

An agent can respond to natural-language requests such as “run Phase 1 for project 275” by following the matching phase master file and gates. `/run_all`, `/skip`, `/approve` and similar historical strings do not invoke a program by themselves.
""",
    "USAGE.md": """# Using the V6 content factory

This repository is a structured prompt and preset system for video production. It contains 500 niche families, 15 planning angles per family, 14 subject categories, and a six-phase process. Presets are planning inputs, not researched stories.

## Start a project

1. Find the niche ID, title, current path and primary subject in `REGISTRY/NICHE_TAXONOMY.csv`.
2. Open its `ALL_TOPICS_BY_NICHE.md` and choose an angle slug. A generated angle is a candidate format; evaluate whether it makes a useful, supportable story before production.
3. Run `python validate_repository.py` and `python create_project.py --id 275 --angle history_origins --dry-run`.
4. Run the create command without `--dry-run`. It writes `OUTPUT/<SubjectCategory>/Topics/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/01_Phase0_Configuration/CONFIG.md` and refuses to overwrite an existing file. Optional `--overrides answers.json` accepts explicit Q-ID string answers.
5. Continue through Phases 1–5 using `CORE/PIPELINE/CONTRACT.md` and the matching master files. Research claims need sources before script production; completion requires a final audit with no blockers.

## Where information lives

| File | Purpose |
|---|---|
| `REGISTRY/NICHE_TAXONOMY.csv` | Stable ID, subject category, slug and path |
| `REGISTRY/CONFIG_SCHEMA.json` | Canonical Q1–Q42 labels and defaults |
| `REGISTRY/Categories/CAT_<SubjectCategory>.md` | Subject defaults |
| `REGISTRY/Topics/<SubjectCategory>/<Slug>/` | 15 angle presets and index |
| `REGISTRY/MASTER_VISUAL_STYLE.md` | Visual direction by stable ID |
| `CORE/PIPELINE/CONTRACT.md` | Paths, outputs, gates and handoffs |

Existing projects under `OUTPUT/Legacy/` predate schema 3.0 and have not passed its checks. The audit and old-to-new path maps are under `AUDIT/` and `REGISTRY/LEGACY_TOPIC_PATHS.csv`.
""",
    "HOW_IT_WORKS.md": """# How the V6 content factory works

The taxonomy answers **what the subject is**. Q3 answers **what angle the episode takes**. Q15 and Q40 describe **how it looks and is produced**. Keeping those decisions separate prevents documentary, animation and AI film from becoming competing subject folders.

Each stable ID from 001–500 maps to one subject category in `REGISTRY/NICHE_TAXONOMY.csv`. The 15 angle files under each niche are planning presets. The category preset supplies Q2–Q42 defaults; the topic supplies Q3 and Q15; an explicit project choice overrides either. `REGISTRY/CONFIG_SCHEMA.json` version 3.0 defines the question meanings. Q14 is an exact runtime; Q42 is a scene-duration plan.

The project then moves through six phases: configuration, evidence-backed research, production rules, scene breakdown, compiled package and final audit. `CORE/PIPELINE/CONTRACT.md` is the active phase and output contract. `CORE/PIPELINE/FLOW_STEPS.md` gives the sequence. Phases 1 and 2 establish facts and locked creative choices before scenes are drafted. Scenes cite claim IDs and their durations sum to the configured runtime. The final audit can block completion.

Run `python validate_repository.py` to check the registry and `python create_project.py --id 275 --angle history_origins --dry-run` to preview a project. Run `python audit_repository.py` to refresh the file-read inventory. The audit reports under `AUDIT/` describe the migration and remaining editorial gaps. Existing work under `OUTPUT/Legacy/` is historical.
""",
    "CORE/PIPELINE/FLOW_STEPS.md": """# V6 flow steps — schema 3.0

Use `CORE/PIPELINE/CONTRACT.md` for the authoritative file tree, counts and gates. Use `REGISTRY/CONFIG_SCHEMA.json` for Q1–Q42.

| Step | Read | Produce | Check before advancing |
|---|---|---|---|
| Select niche | `NICHE_TAXONOMY.csv`, niche index, visual style row | Stable ID, subject, angle | Category and topic path resolve |
| Phase 0 | Subject CAT preset, topic preset, explicit answers | `01_Phase0_Configuration/CONFIG.md` | All 42 values and provenance; exact Q14; parseable Q42; risk gate |
| Phase 1 | CONFIG and credible primary/secondary sources | Research Bible and `Claim_Ledger.md` | Material claims sourced and disputes qualified; approval in interactive/domain preset mode |
| Phase 2 | CONFIG, claim ledger, Phase 1 outputs, 16 numbered templates | Production Bible | Q3/Q15/Q16/Q42 locked; approval in interactive/domain preset mode |
| Phase 3 | Phase 1 evidence and Phase 2 locks | 25-scene batches plus language scripts as needed | Sequential IDs, claim citations, duration sum equals Q14; first batch approved in interactive mode |
| Phase 4 | All scenes, research and locks | `Production_Package.md` | Complete script, production instructions and source references; approval in interactive/domain preset mode |
| Phase 5 | All project outputs | `Audit_Report.md`, then certificate only if passing | No blockers, placeholders, citation gaps, timing mismatch or unresolved review flags |

The default 600-second runtime and fixed eight-second scenes produce 75 scenes in three batches. For other fixed lengths use `ceil(Q14 seconds / Q42 seconds)` and shorten the last scene if needed. Variable timing requires a scene-by-scene sum. Changing Phase 2 locks invalidates downstream phases. Autonomous drafting never waives human review for high-risk content.
""",
}


def phase0_document():
    lines = [
        "# Phase 0 — Configuration (schema 3.0)", "",
        "Resolve a stable niche ID through `REGISTRY/NICHE_TAXONOMY.csv`, load `CAT_<SubjectCategory>.md`, then the selected topic preset. Explicit project answers have the highest precedence. The canonical machine-readable definitions are in `REGISTRY/CONFIG_SCHEMA.json`; the path and handoff are in `CORE/PIPELINE/CONTRACT.md`.", "",
        "Use `python create_project.py --id <ID> --angle <slug> --dry-run` to validate the merge and runtime before writing. The output is `OUTPUT/<SubjectCategory>/Topics/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/01_Phase0_Configuration/CONFIG.md`. Record schema version and answer provenance.", "",
        "Q14 must be an exact number of seconds. Q42 must specify a fixed number of seconds or a complete variable scene plan. Q21 is Graphics Requirement; Q24 is Source Quality Requirements. Q1 is the subject category, while Q3 is the story angle. Q15 visual style does not determine Q40 generation method.", "",
        "| ID | Canonical question | Default |", "|---|---|---|",
    ]
    for qid, item in SCHEMA["questions"].items():
        lines.append(f"| {qid} | {item['label']} | {item['default'] or 'From taxonomy'} |")
    lines += ["", "High/Critical Q8 or Strict/Critical Q41 requires human review before publication status. An agent may draft further material, but cannot record the review as passed without evidence. Phase 0 defaults are planning decisions, never verified research claims.", ""]
    return "\n".join(lines)


DOCS["CORE/PIPELINE/01_Phase0_Configuration/MASTER_Phase0_Config.md"] = phase0_document()


def main():
    if ARCHIVE.exists():
        raise FileExistsError(f"Archive already exists; refusing to replace active instructions: {ARCHIVE}")
    for relative in DOCS:
        source = (ROOT / relative).resolve()
        if ROOT not in source.parents or not source.is_file():
            raise ValueError(f"Missing or unsafe source path: {source}")
    for relative, replacement in DOCS.items():
        source = ROOT / relative
        archived = ARCHIVE / relative
        archived.parent.mkdir(parents=True, exist_ok=True)
        archived.write_bytes(source.read_bytes())
        source.write_text(replacement, encoding="utf-8")
    print(f"Archived and refreshed {len(DOCS)} instruction files")


if __name__ == "__main__":
    main()
