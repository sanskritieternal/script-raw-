"""Optional niche idea banks, a generated index and immutable CONFIG snapshots."""
import argparse
from collections import Counter, defaultdict
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlparse
import csv

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "REGISTRY"
SCHEMA = json.loads((REGISTRY / "IDEA_BANK_SCHEMA.json").read_text(encoding="utf-8"))
STATUSES = set(SCHEMA["$defs"]["idea"]["properties"]["status"]["enum"])


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def fingerprint(value):
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def taxonomy():
    with (REGISTRY / "NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def bank_path(row):
    return ROOT / row["niche_path"] / "IDEA_BANK.json"


def valid_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def validate_idea(idea, row):
    errors = []
    definition = SCHEMA["$defs"]["idea"]
    if not isinstance(idea, dict):
        return ["Idea must be an object"]
    if set(idea) != set(definition["required"]):
        errors.append("Idea fields must match IDEA_BANK_SCHEMA.json exactly")
    prefix = "IDEA-" + row["id"] + "-"
    if not re.fullmatch(re.escape(prefix) + r"\d{4}", str(idea.get("idea_id", ""))):
        errors.append("Idea ID must bind to its niche: " + prefix + "0001")
    if idea.get("niche_id") != row["id"]:
        errors.append("Idea niche ID differs from bank")
    if not isinstance(idea.get("status"), str) or idea["status"] not in STATUSES:
        errors.append("Unknown idea status")
    for key in ("topic", "working_title", "story_question", "case", "place_period_version", "intended_audience", "purpose"):
        value = idea.get(key)
        minimum = definition["properties"][key]["minLength"]
        if not isinstance(value, str) or len(value.strip()) < minimum or "\n" in value or "|" in value:
            errors.append(f"Missing, too short or multiline idea field: {key}")
    if not str(idea.get("story_question", "")).endswith("?"):
        errors.append("Idea story_question must end with ?")
    plan = json.loads((ROOT / row["niche_path"] / "ANGLE_PLAN.json").read_text(encoding="utf-8"))
    if not isinstance(idea.get("angle_slug"), str) or idea["angle_slug"] not in {a["slug"] for a in plan["angles"]}:
        errors.append("Idea angle_slug is not in this niche's angle plan")
    for key in ("created_date", "updated_date"):
        if not valid_date(idea.get(key)):
            errors.append(f"Idea {key} needs a real ISO date")
    if valid_date(idea.get("created_date")) and valid_date(idea.get("updated_date")) and idea["updated_date"] < idea["created_date"]:
        errors.append("Idea updated_date precedes created_date")
    for key in ("evidence_gaps", "blocking_gaps", "related_ideas"):
        values = idea.get(key)
        if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
            errors.append(f"Idea {key} must be a list of nonempty strings")
        elif len(set(values)) != len(values):
            errors.append(f"Duplicate {key} entries")
    readiness = idea.get("readiness_note")
    if not isinstance(readiness, str):
        errors.append("readiness_note must be text")
    sources = idea.get("source_candidates")
    if not isinstance(sources, list):
        errors.append("source_candidates must be a list")
        sources = []
    checked = 0
    for source in sources:
        if not isinstance(source, dict) or set(source) != {"title", "url", "status", "checked_date", "check_note"}:
            errors.append("Invalid source candidate fields")
            continue
        parsed = urlparse(str(source["url"]))
        if parsed.scheme not in {"http", "https"} or not parsed.netloc or not isinstance(source["title"], str) or not source["title"].strip():
            errors.append("Source candidate needs a title and absolute HTTP(S) URL")
        if not isinstance(source["status"], str) or source["status"] not in {"unverified", "checked"}:
            errors.append("Source status must be unverified or checked")
        if source["status"] == "checked":
            if not valid_date(source["checked_date"]) or not isinstance(source["check_note"], str) or len(source["check_note"].strip()) < 15:
                errors.append("Checked source needs real date and access/feasibility evidence note")
            else:
                checked += 1
        elif source["checked_date"] is not None or not isinstance(source["check_note"], str):
            errors.append("Unverified source needs null checked_date and a text check_note")
    if idea.get("status") == "ready_for_project":
        if not checked or not isinstance(readiness, str) or len(readiness.strip()) < 20 or idea.get("blocking_gaps"):
            errors.append("Ready idea needs a checked source, readiness explanation and no blocking gaps")
    return errors


def read_bank(row):
    path = bank_path(row)
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or set(value) != {"schema_version", "niche_id", "ideas"}:
        raise ValueError("Invalid idea bank fields: " + str(path))
    if value["schema_version"] != "1.0" or value["niche_id"] != row["id"] or not isinstance(value["ideas"], list):
        raise ValueError("Idea bank version/niche/list mismatch: " + str(path))
    seen, questions = set(), set()
    for idea in value["ideas"]:
        errors = validate_idea(idea, row)
        if errors:
            raise ValueError(str(path) + ": " + "; ".join(errors))
        if idea["idea_id"] in seen:
            raise ValueError("Duplicate idea ID: " + idea["idea_id"])
        question = re.sub(r"\W+", " ", idea["story_question"].lower()).strip()
        if question in questions:
            raise ValueError("Duplicate normalized story question inside one bank")
        seen.add(idea["idea_id"]); questions.add(question)
    return value


def catalog():
    ideas, errors = {}, []
    for row in taxonomy().values():
        if not bank_path(row).exists():
            continue
        try:
            bank = read_bank(row)
            for idea in bank["ideas"]:
                ideas[idea["idea_id"]] = (row, idea)
        except (ValueError, TypeError, KeyError, OSError) as exc:
            errors.append(str(exc))
    for identity, (row, idea) in ideas.items():
        for related in idea["related_ideas"]:
            if related == identity or related not in ideas:
                errors.append(f"Unknown or self-related idea: {identity} -> {related}")
    return ideas, errors


def index_text():
    ideas, errors = catalog()
    if errors:
        raise ValueError("\n".join(errors))
    counts = Counter(i["status"] for row, i in ideas.values())
    lines = ["# Episode idea master list", "", "Generated by `python idea_bank.py build-index`. Banks are optional; no empty bank or generic idea is created for every niche.", "",
             f"**{len(ideas)} ideas** across **{len({r['id'] for r, i in ideas.values()})} niches**. Proposed ideas and source leads are not verified episode claims.", "",
             "| Status | Ideas |", "|---|---:|"]
    lines += [f"| {state} | {counts[state]} |" for state in sorted(STATUSES)]
    lines += ["", "| Idea ID | Niche | Topic | Working title | Angle | Status | Bank |", "|---|---|---|---|---|---|---|"]
    questions = defaultdict(list)
    for identity, (row, idea) in sorted(ideas.items()):
        rel = bank_path(row).relative_to(REGISTRY).as_posix()
        lines.append(f"| {identity} | {row['id']} {row['title']} | {idea['topic']} | {idea['working_title']} | {idea['angle_slug']} | {idea['status']} | [JSON]({rel}) |")
        questions[re.sub(r"\W+", " ", idea["story_question"].lower()).strip()].append(identity)
    lines += ["", "## Exact-question overlap signals", "", "These are review signals, not proof of duplicate scope.", ""]
    duplicates = [ids for ids in questions.values() if len(ids) > 1]
    lines += ["- " + ", ".join(ids) for ids in duplicates] if duplicates else ["No normalized exact-question duplicates across banks."]
    lines += ["", "See [IDEA_BANK_GUIDE.md](IDEA_BANK_GUIDE.md) for readiness, project creation and snapshot rules."]
    return "\n".join(lines) + "\n"


def select(niche_id, identity):
    row = taxonomy()[f"{int(niche_id):03}"]
    bank = read_bank(row)
    idea = next((i for i in bank["ideas"] if i["idea_id"] == identity), None)
    if idea is None:
        raise ValueError("Idea not found in the selected niche: " + identity)
    if idea["status"] != "ready_for_project":
        raise ValueError("Only ready_for_project ideas can create or preview an episode; proposed/researching is not readiness")
    return idea, bank_path(row).relative_to(ROOT).as_posix()


def snapshot_section(idea, source):
    return ("\n\n## Selected episode idea\n\n"
            f"Idea ID: {idea['idea_id']}\nSource idea bank: `{source}`\n"
            f"Idea snapshot SHA-256: {fingerprint(idea)}\n\n```json\n" +
            json.dumps(idea, ensure_ascii=False, indent=2) + "\n```\n\n"
            "This is a creation-time snapshot, not a live link or research approval. Later bank edits do not rewrite this episode. Phase 1 still verifies each material claim.\n")


def validate_snapshot(config, project, errors):
    present = "## Selected episode idea" in config or re.search(r"^Idea ID:", config, re.M)
    if not present:
        return
    try:
        section = config.split("## Selected episode idea", 1)[1]
        matches = re.findall(r"```json\s*\n(.*?)\n```", section, re.S)
        if len(matches) != 1:
            raise ValueError("Need exactly one complete idea JSON snapshot")
        idea = json.loads(matches[0])
        niche = re.match(r"\d{3}", project.name)
        row = taxonomy()[niche[0]] if niche else None
        if row is None:
            raise ValueError("Invalid snapshot project identity")
        problems = validate_idea(idea, row)
        if problems:
            raise ValueError("; ".join(problems))
        if idea["status"] != "ready_for_project":
            raise ValueError("Selected idea snapshot was not ready_for_project")
        expected = [f"Idea ID: {idea['idea_id']}", f"Idea snapshot SHA-256: {fingerprint(idea)}",
                    f"Source idea bank: `{row['niche_path']}/IDEA_BANK.json`",
                    f"Story question: {idea['story_question']}"]
        if any(line not in config.splitlines() for line in expected):
            raise ValueError("Idea ID, bank, hash or story question differs from snapshot")
        angle = re.search(r"^Angle preset: `([^`]+)`$", config, re.M)
        if not angle or Path(angle[1]).name != f"{row['id']}_{row['slug']}_{idea['angle_slug']}.md":
            raise ValueError("Selected angle differs from idea snapshot")
    except (ValueError, TypeError, KeyError, OSError) as exc:
        errors.append("Invalid idea snapshot: " + str(exc))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["init", "add", "validate", "build-index"])
    parser.add_argument("--id", type=int)
    parser.add_argument("--file", type=Path, help="Idea JSON object matching the schema; idea_id can be omitted for allocation")
    parser.add_argument("--write", action="store_true", help="Write init/add; otherwise preview")
    args = parser.parse_args()
    if args.command == "validate":
        ideas, errors = catalog()
        index = REGISTRY / "IDEA_MASTER_LIST.md"
        if not errors and (not index.is_file() or index.read_text(encoding="utf-8") != index_text()):
            errors.append("Idea master list is absent/stale; run build-index")
        if errors:
            raise SystemExit("\n".join(errors))
        print(f"Validated {len(ideas)} ideas; optional banks and index agree")
        return
    if args.command == "build-index":
        (REGISTRY / "IDEA_MASTER_LIST.md").write_text(index_text(), encoding="utf-8")
        print("Built REGISTRY/IDEA_MASTER_LIST.md")
        return
    if args.id is None or f"{args.id:03}" not in taxonomy():
        parser.error("Choose a registered --id")
    row = taxonomy()[f"{args.id:03}"]
    path = bank_path(row)
    if args.command == "init":
        if path.exists():
            raise FileExistsError("Will not overwrite an existing idea bank")
        value = {"schema_version": "1.0", "niche_id": row["id"], "ideas": []}
    else:
        if args.file is None:
            parser.error("add requires --file")
        value = read_bank(row) if path.exists() else {"schema_version": "1.0", "niche_id": row["id"], "ideas": []}
        idea = json.loads(args.file.read_text(encoding="utf-8"))
        if not isinstance(idea, dict):
            raise ValueError("Idea input must be a JSON object")
        number = max([int(i["idea_id"].rsplit("-", 1)[1]) for i in value["ideas"]] or [0]) + 1
        idea.setdefault("idea_id", f"IDEA-{row['id']}-{number:04}")
        errors = validate_idea(idea, row)
        if errors:
            raise ValueError("; ".join(errors))
        normalized = lambda q: re.sub(r"\W+", " ", q.lower()).strip()
        if any(i["idea_id"] == idea["idea_id"] or normalized(i["story_question"]) == normalized(idea["story_question"]) for i in value["ideas"]):
            raise ValueError("Duplicate idea ID or story question; edit the existing record instead")
        existing, problems = catalog()
        if problems:
            raise ValueError("\n".join(problems))
        if any(r not in existing for r in idea["related_ideas"]):
            raise ValueError("Related ideas must already exist")
        value["ideas"].append(idea)
    if args.write:
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        (REGISTRY / "IDEA_MASTER_LIST.md").write_text(index_text(), encoding="utf-8")
    print(f"{'Wrote' if args.write else 'Preview'} {path}: {len(value['ideas'])} ideas; no episode created")


if __name__ == "__main__":
    main()
