"""Create a validated Phase 0 project from the taxonomy and topic preset.

Example: python -m Tools.projects.create_project --id 275 --angle history_origins --story-question "What shaped Shaktism origins?"
Use --dry-run to inspect the resolved configuration without writing files.
"""
import argparse
import csv
import json
import math
import re
from pathlib import Path
from Tools.projects.production_workflow import MARKER
from Tools.projects.output_location import resolve_output_root

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "REGISTRY"
SCHEMA = json.loads((REGISTRY / "CONFIG_SCHEMA.json").read_text(encoding="utf-8"))


def niche_preset_path(row):
    stem = f"{row['id']}_{row['slug']}"
    return REGISTRY / "Niches" / stem / f"CAT_{stem}.md"


def identity_path(row):
    stem = f"{row['id']}_{row['slug']}"
    return REGISTRY / "Niches" / stem / f"NICHE_{stem}.md"


def parse_niche(row):
    path = niche_preset_path(row)
    if not identity_path(row).is_file():
        raise ValueError(f"Missing niche identity: {identity_path(row)}")
    if not path.is_file():
        raise ValueError(f"Missing niche preset: {path}")
    found = re.findall(r"^## (Q\d+): ([^\n]+)\n\*\*Default:\*\* ([^\n]+)", path.read_text(encoding="utf-8"), re.M)
    if [qid for qid, _, _ in found] != list(SCHEMA["questions"]):
        raise ValueError(f"Incomplete niche configuration: {path}")
    for qid, label, _ in found:
        if label != SCHEMA["questions"][qid]["label"]:
            raise ValueError(f"Niche schema label mismatch: {path} {qid}")
    values = {qid: value for qid, _, value in found}
    if values["Q1"] != row["primary_category"]:
        raise ValueError(f"Niche subject mismatch: {path}")
    return path, values


def episode_slug(question):
    slug = re.sub(r"[^a-z0-9]+", "_", question.lower()).strip("_")
    return slug[:48].rstrip("_")


def load_row(niche_id):
    with (REGISTRY / "NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as fh:
        rows = {int(r["id"]): r for r in csv.DictReader(fh)}
    if niche_id not in rows:
        raise ValueError(f"Unknown niche ID: {niche_id}")
    return rows[niche_id]


def parse_topic(row, angle):
    path = ROOT / row["current_path"] / f"{row['id']}_{row['slug']}_{angle}.md"
    if not path.is_file():
        raise ValueError(f"Unknown angle or missing topic preset: {path}")
    text = path.read_text(encoding="utf-8")
    found = re.findall(r"^## (Q\d+): ([^\n]+)\n\*\*Default:\*\* ([^\n]+)", text, re.M)
    expected = ["Q3"]
    if [q for q, _, _ in found] != expected:
        raise ValueError(f"Incomplete topic configuration: {path}")
    for qid, label, _ in found:
        if label != SCHEMA["questions"][qid]["label"]:
            raise ValueError(f"Schema label mismatch: {path} {qid}")
    return path, {qid: value for qid, _, value in found}


def parse_duration(values, scene_plan=None):
    runtime = re.fullmatch(r"(\d+) seconds", values["Q14"])
    if not runtime:
        raise ValueError("Phase 3 needs an exact Q14 runtime in seconds")
    total = int(runtime.group(1))
    if total <= 0:
        raise ValueError("Q14 runtime must be positive")
    if values["Q42"] == "VARIABLE":
        if not isinstance(scene_plan, list) or not scene_plan or any(type(n) is not int or n <= 0 for n in scene_plan):
            raise ValueError("VARIABLE Q42 requires a JSON list of positive whole-second scene durations")
        if sum(scene_plan) != total:
            raise ValueError("Variable scene durations must sum exactly to Q14")
        return total, scene_plan, len(scene_plan)
    scene = re.fullmatch(r"FIXED (\d+)-SECOND", values["Q42"])
    if not scene or scene_plan is not None:
        raise ValueError("Fixed Q42 requires a positive duration and no variable scene plan")
    per_scene = int(scene.group(1))
    if per_scene <= 0 or per_scene > total:
        raise ValueError("Invalid fixed Q42 duration")
    return total, per_scene, math.ceil(total / per_scene)


def resolve(niche_id, angle, overrides=None, scene_plan=None):
    row = load_row(niche_id)
    _, niche_defaults = parse_niche(row)
    topic_path, topic_defaults = parse_topic(row, angle)
    values = dict(niche_defaults)
    sources = {qid: "niche_cat" for qid in values}
    sources["Q1"] = "taxonomy"
    values["Q3"] = topic_defaults["Q3"]
    sources["Q3"] = "angle_preset"
    overrides = overrides or {}
    for qid, value in overrides.items():
        if qid not in values or qid == "Q1":
            raise ValueError(f"Unknown or protected override: {qid}")
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Empty override: {qid}")
        values[qid] = value.strip()
        sources[qid] = "explicit_override"
    total, per_scene, count = parse_duration(values, scene_plan)
    if values["Q8"] not in {"Low", "Moderate", "High", "Critical"}:
        raise ValueError("Q8 must be Low, Moderate, High or Critical")
    if values["Q41"] not in {"Standard", "Strict", "Critical"}:
        raise ValueError("Q41 must be Standard, Strict or Critical")
    return row, topic_path, values, sources, total, per_scene, count


def render(row, topic_path, values, sources, total, per_scene, count, mode, risk_flags=None, story_question=None, project_episode_slug=None, idea_snapshot=None, idea_bank_ref=None):
    topic_text = topic_path.read_text(encoding="utf-8")
    scope_match = re.search(r"^## Editorial scope\s*\n(.*?)(?=^## |\Z)", topic_text, re.M | re.S)
    if not scope_match or not scope_match.group(1).strip():
        raise ValueError(f"Selected angle needs editorial scope: {topic_path}")
    scope_snapshot = scope_match.group(1).strip()
    risk_flags = list(risk_flags or [])
    contested = values["Q10"].lower() not in {"no contested claims", "no"} or values["Q31"].lower() not in {"no controversial claims", "no"}
    review = values["Q8"] in {"High", "Critical"} or values["Q41"] in {"Strict", "Critical"} or contested or bool(risk_flags)
    lines = [
        "# Phase 0: Configuration", "",
        f"Niche ID: {row['id']}", f"Niche: {row['title']}",
        f"Story question: {story_question or 'Routing preview only - choose a specific story question before production'}",
        f"Episode slug: {project_episode_slug or 'routing_preview'}",
        f"Subject category: {row['primary_category']}",
        f"Niche identity: `{identity_path(row).relative_to(ROOT).as_posix()}`",
        f"CAT preset: `{niche_preset_path(row).relative_to(ROOT).as_posix()}`",
        f"Angle preset: `{topic_path.relative_to(ROOT).as_posix()}`",
        f"Question schema version: {SCHEMA['version']}", f"Mode: {mode}",
        MARKER, "",
        "## Configuration answers", "",
        "| ID | Question | Answer | Source |", "|---|---|---|---|",
    ]
    for qid, definition in SCHEMA["questions"].items():
        lines.append(f"| {qid} | {definition['label']} | {values[qid]} | {sources[qid]} |")
    lines += ["", "## Selected angle scope", "", scope_snapshot, "",
              "This is the selected angle's planning guidance at project creation. "
              "Use the episode story question to choose the concrete case; document its coverage and exclusions in Phase 1."]
    timing_line = (f"- Variable scene durations: {', '.join(map(str, per_scene))} seconds"
                   if isinstance(per_scene, list) else f"- Fixed scene duration: {per_scene} seconds")
    final_line = (f"- Planned scenes: {count}; final scene: {per_scene[-1]} seconds"
                  if isinstance(per_scene, list) else f"- Planned scenes: {count}; final scene: {total - per_scene * (count - 1)} seconds")
    lines += ["", "## Phase 3 timing lock", "",
              f"- Exact runtime: {total} seconds", timing_line, final_line,
              "- Scene breakdown file: Scene_Breakdown.md", "- First review range: scenes 1-25", "", "## Review gate", "",
              f"- Risk flags: {', '.join(risk_flags) if risk_flags else 'None'}",
              f"- Human review required before publication: {'Yes' if review else 'No'}",
              f"- Human review status: {'Pending' if review else 'Not required'}",
              "- Phase 1 claims require supporting sources before Phase 2.",
              "- This configuration does not certify research, rendered assets, or publication readiness.", ""]
    content = "\n".join(lines)
    if idea_snapshot is not None:
        from Tools.projects.idea_bank import snapshot_section, validate_idea
        problems = validate_idea(idea_snapshot, row)
        if problems or idea_snapshot.get("status") != "ready_for_project":
            raise ValueError("Selected idea is not ready: " + "; ".join(problems))
        if story_question != idea_snapshot["story_question"] or topic_path.name != f"{row['id']}_{row['slug']}_{idea_snapshot['angle_slug']}.md":
            raise ValueError("Idea angle/story conflicts with episode configuration")
        if idea_bank_ref != row["niche_path"] + "/IDEA_BANK.json":
            raise ValueError("Idea bank reference differs from the selected niche")
        content += snapshot_section(idea_snapshot, idea_bank_ref)
    return content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, required=True)
    parser.add_argument("--angle", help="Angle slug; derived automatically when --idea-id is selected")
    parser.add_argument("--idea-id", help="Ready idea in the selected niche's optional IDEA_BANK.json")
    parser.add_argument("--mode", choices=["interactive", "domain_preset", "autonomous"], default="interactive")
    parser.add_argument("--overrides", type=Path, help="JSON object of explicit Q-ID answers")
    parser.add_argument("--scene-plan", type=Path, help="JSON array of scene durations, required when Q42 is VARIABLE")
    parser.add_argument("--risk-flags", nargs="*", choices=["living_person_allegation", "medical_advice", "financial_advice", "contested_religious_claim", "contested_historical_claim"], default=[])
    parser.add_argument("--story-question", help="Specific researchable question for this episode; required when writing CONFIG")
    parser.add_argument("--episode-slug", help="Optional short snake_case key for this episode; defaults to the story question")
    parser.add_argument("--output-root", type=Path, help="Override output.md for this project; otherwise use its setting or the system OUTPUT folder")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    args.output_root = resolve_output_root(args.output_root)
    selected_idea, idea_ref = None, None
    if args.idea_id:
        from Tools.projects.idea_bank import select
        selected_idea, idea_ref = select(args.id, args.idea_id)
        if args.angle and args.angle != selected_idea["angle_slug"]:
            parser.error("--angle conflicts with the selected idea")
        if args.story_question and args.story_question != selected_idea["story_question"]:
            parser.error("--story-question conflicts with the selected idea; revise the bank first")
        args.angle = selected_idea["angle_slug"]
        args.story_question = selected_idea["story_question"]
    if not args.angle:
        parser.error("Supply --angle or a ready --idea-id")
    overrides = json.loads(args.overrides.read_text(encoding="utf-8")) if args.overrides else {}
    scene_plan = json.loads(args.scene_plan.read_text(encoding="utf-8")) if args.scene_plan else None
    if not isinstance(overrides, dict):
        raise ValueError("Overrides must be a JSON object")
    row, topic, values, sources, total, per_scene, count = resolve(args.id, args.angle, overrides, scene_plan)
    if not args.dry_run and (not args.story_question or len(args.story_question.strip()) < 15 or not args.story_question.strip().endswith("?")):
        raise ValueError("Writing a project requires --story-question with a specific question ending in ?")
    story_slug = args.episode_slug or episode_slug(args.story_question or "routing_preview")
    if not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", story_slug):
        raise ValueError("Episode slug must be lowercase snake_case")
    content = render(row, topic, values, sources, total, per_scene, count, args.mode, args.risk_flags, args.story_question, story_slug, selected_idea, idea_ref)
    content += f"\n## Output location at creation\n\nOutput root: `{args.output_root}`\n\nAll phase outputs belong inside this specific project folder. Later output.md changes do not relocate this project.\n"
    project = f"{row['id']}_{row['slug']}_{args.angle}_{story_slug}"
    target = args.output_root / f"{row['id']}_{row['slug']}" / project / "01_Phase0_Configuration" / "CONFIG.md"
    if args.dry_run:
        print(f"Validated: {target} ({count} scenes)")
        return
    from Tools.projects.production_workflow import specification, TEMPLATES, scaffold
    for name in specification()["documents"]:
        if not (TEMPLATES / name).is_file():
            raise FileNotFoundError(f"Missing production template: {name}")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"Will not overwrite existing configuration: {target}")
    target.write_text(content, encoding="utf-8")
    scaffold(target.parent.parent, write=True)
    from Tools.projects.planning_records import prepare
    prepare(target.parent.parent, write=True)
    print(f"Created {target}")
    print(f"Created {len(specification()['documents'])} draft production documents and PRODUCTION_MANIFEST.json; complete research before production acceptance")
    print('Added optional SCENE_PLANNER.md and GENERATOR_PROFILE.md drafts; complete planning before Phase 3 acceptance')


if __name__ == "__main__":
    main()
