"""Apply the canonical Q1-Q42 schema to category and topic presets.

Existing topic defaults are backed up once to REGISTRY/LEGACY_TOPIC_DEFAULTS.csv.
Old category preset files are moved under AUDIT/Legacy_Instructions/Category_Presets/.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "REGISTRY"
SCHEMA = json.loads((REGISTRY / "CONFIG_SCHEMA.json").read_text(encoding="utf-8"))
QUESTIONS = SCHEMA["questions"]
CATEGORIES = REGISTRY / "Categories"
BACKUP = REGISTRY / "LEGACY_TOPIC_DEFAULTS.csv"


def answers(category, angle=None, visual=None):
    values = {qid: item["default"] for qid, item in QUESTIONS.items()}
    values.update(SCHEMA["category_overrides"][category])
    values["Q1"] = category
    if angle:
        values["Q3"] = angle
    if visual:
        values["Q15"] = visual
    return values


def question_block(values):
    return "\n".join(
        f"## {qid}: {QUESTIONS[qid]['label']}\n**Default:** {values[qid]}"
        for qid in list(QUESTIONS)[1:]
    )


def main():
    expected = {f"Q{i}" for i in range(1, 43)}
    if set(QUESTIONS) != expected:
        raise ValueError("Schema must define Q1-Q42 exactly")
    with (REGISTRY / "NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 500 or set(SCHEMA["category_overrides"]) != {r["primary_category"] for r in rows}:
        raise ValueError("Taxonomy and category overrides disagree")
    legacy_dir = ROOT / "AUDIT" / "Legacy_Instructions" / "Category_Presets"
    legacy_dir.mkdir(parents=True, exist_ok=True)
    active_categories = set(SCHEMA["category_overrides"])
    for path in CATEGORIES.glob("CAT_*.md"):
        if path.stem.removeprefix("CAT_") in active_categories:
            continue  # already canonical; reruns must not re-archive it
        destination = legacy_dir / path.name
        if destination.exists():
            raise ValueError(f"Legacy preset collision: {destination}")
        path.rename(destination)
    category_changes = 0
    for category in sorted(SCHEMA["category_overrides"]):
        values = answers(category)
        content = f"# CAT_{category} — Canonical Subject Preset\n\n> Schema: {SCHEMA['version']} | Subject category: {category}\n> Explicit project answers override these defaults. Q3 may be overridden by a topic angle; Q15 by the visual style registry.\n\n## Q1: Content Category\n**Default:** {category}\n" + question_block(values) + "\n"
        target = CATEGORIES / f"CAT_{category}.md"
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            target.write_text(content, encoding="utf-8")
            category_changes += 1

    backup_rows = []
    tasks = []
    for row in rows:
        category = row["primary_category"]
        directory = ROOT / row["current_path"]
        for path in directory.glob(f"{row['id']}_*.md"):
            content = path.read_text(encoding="utf-8")
            match = re.search(r"## Q2:.*?(?=\n---\n\n## Visual Style)", content, re.S)
            if not match:
                raise ValueError(f"Missing canonical topic block boundaries: {path}")
            old_block = match.group(0)
            defaults = re.findall(r"^## (Q\d+):[^\n]*\n\*\*Default:\*\* ([^\n]*)", old_block, re.M)
            if len(defaults) != 41:
                raise ValueError(f"Expected 41 defaults in {path}; found {len(defaults)}")
            if not BACKUP.exists():
                backup_rows.append([path.relative_to(ROOT).as_posix()] + [dict(defaults)[f"Q{i}"] for i in range(2, 43)])
            angle = re.search(r"^> Domain:.*?\| Sub-type: ([^\n]+)$", content, re.M)
            visual = re.search(r"^\| Primary Visual Style \| ([^|]+) \|$", content, re.M)
            if not angle or not visual:
                raise ValueError(f"Missing angle or visual style: {path}")
            tasks.append((path, content, match.span(), category, angle.group(1).strip(), visual.group(1).strip()))
    if len(tasks) != 7500:
        raise ValueError(f"Expected 7500 topic files, found {len(tasks)}")
    if not BACKUP.exists():
        with BACKUP.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["topic_path"] + [f"Q{i}" for i in range(2, 43)])
            writer.writerows(backup_rows)
    changes = 0
    for path, content, (start, end), category, angle, visual in tasks:
        values = answers(category, angle, visual)
        new_block = question_block(values) + "\n"
        new_content = content[:start] + new_block + content[end:]
        new_content = re.sub(r"^> (?:Production|Subject) Preset: .+$", f"> Subject Preset: CAT_{category}.md", new_content, count=1, flags=re.M)
        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            changes += 1
    print(f"Checked {len(tasks)} topic presets; updated {changes}; category presets updated {category_changes}")


if __name__ == "__main__":
    raise SystemExit("Historical schema 4 utility: active schema 5 niche CATs must not be rewritten")
