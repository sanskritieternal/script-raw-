"""One-time schema 4 to 5 migration: one CAT, NICHE and Angles folder per ID."""
import csv
import json
import re
import shutil
import subprocess
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "REGISTRY"
TAXONOMY = REGISTRY / "NICHE_TAXONOMY.csv"
BACKUP = ROOT / "AUDIT" / "Niche_Home_Migration_2026-10-16"


def checked(path):
    resolved = path.resolve()
    if resolved == ROOT or not resolved.is_relative_to(ROOT):
        raise ValueError(f"Path outside workspace: {path}")
    return resolved


def write_csv(path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def read_cat_values(path, schema):
    text = path.read_text(encoding="utf-8")
    found = re.findall(r"^## (Q\d+): ([^\n]+)\n\*\*Default:\*\* ([^\n]+)", text, re.M)
    if [qid for qid, _, _ in found] != list(schema["questions"]):
        raise ValueError(f"Incomplete old niche configuration: {path}")
    for qid, label, value in found:
        if label != schema["questions"][qid]["label"] or not value.strip():
            raise ValueError(f"Invalid old niche configuration: {path} {qid}")
    return {qid: value for qid, _, value in found}


def render_cat(row, values, schema):
    stem = f"{row['id']}_{row['slug']}"
    lines = [f"# CAT_{stem} - Niche Configuration", "",
             f"> Niche ID: {row['id']} | Subject category: {row['primary_category']}",
             f"> Schema: {schema['version']} | Editable Q1-Q42 defaults for this niche", "",
             "This is the only niche-level source of Q answers. The selected angle sets Q3; explicit episode answers have final precedence.", ""]
    for qid, definition in schema["questions"].items():
        lines.extend([f"## {qid}: {definition['label']}", f"**Default:** {values[qid]}"])
    return "\n".join(lines) + "\n"


def render_identity(row):
    stem = f"{row['id']}_{row['slug']}"
    return (f"# NICHE_{stem} - Identity and Planning\n\n"
            f"Niche ID: {row['id']}\nTitle: {row['title']}\nSubject category: {row['primary_category']}\n"
            f"Configuration: [CAT_{stem}.md](./CAT_{stem}.md)\n"
            "Angle index: [ALL_TOPICS_BY_NICHE.md](./Angles/ALL_TOPICS_BY_NICHE.md)\n"
            f"Visual style source: `REGISTRY/MASTER_VISUAL_STYLE.md` row {int(row['id'])}\n\n"
            "This file records identity and planning links. Q1-Q42 answers live only in the CAT file. "
            "Choose an angle and a specific story question before starting an episode.\n")


def render_output(row):
    stem = f"{row['id']}_{row['slug']}"
    return (f"# {row['id']} {row['title']}\n\n"
            f"Subject category: `{row['primary_category']}`. "
            f"Niche record: `REGISTRY/Niches/{stem}/NICHE_{stem}.md`. "
            f"Configuration: `REGISTRY/Niches/{stem}/CAT_{stem}.md`.\n\n"
            "Episode projects are created under this folder by `create_project.py`. "
            "This landing folder is not a completed episode.\n")


def main():
    schema_path = REGISTRY / "CONFIG_SCHEMA.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    if schema["version"] != "4.0" or BACKUP.exists():
        raise ValueError("Expected schema 4.0 and an unused backup directory")
    with TAXONOMY.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 500 or {int(r["id"]) for r in rows} != set(range(1, 501)):
        raise ValueError("Expected stable niche IDs 1-500")
    moves = []
    for row in rows:
        stem = f"{row['id']}_{row['slug']}"
        old_angles = checked(ROOT / row["current_path"])
        old_niche = checked(REGISTRY / "Categories" / "Niches" / row["primary_category"] / f"NICHE_{stem}.md")
        old_output = checked(ROOT / "OUTPUT" / row["primary_category"] / "Topics" / stem)
        home = checked(REGISTRY / "Niches" / stem)
        new_angles = checked(home / "Angles")
        new_output = checked(ROOT / "OUTPUT" / stem)
        if not old_angles.is_dir() or not old_niche.is_file() or not old_output.is_dir():
            raise ValueError(f"Missing old niche files: {stem}")
        if home.exists() or new_output.exists():
            raise ValueError(f"New niche path collision: {stem}")
        values = read_cat_values(old_niche, schema)
        if values["Q1"] != row["primary_category"]:
            raise ValueError(f"CAT subject mismatch: {stem}")
        moves.append((row, old_angles, old_niche, old_output, home, new_angles, new_output, values))
    for command in (("validate_repository.py",), ("populate_niches.py", "--verify-content")):
        subprocess.run([sys.executable, str(ROOT / command[0]), *command[1:]], cwd=ROOT, check=True)
    BACKUP.mkdir(parents=True)
    for name in ("NICHE_TAXONOMY.csv", "CONFIG_SCHEMA.json", "LEGACY_TOPIC_PATHS.csv",
                 "LEGACY_TOPIC_DEFAULTS.csv", "CATEGORY_INDEX.md"):
        shutil.copy2(REGISTRY / name, BACKUP / name)
    archive = BACKUP / "Schema4_Files.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zip_file:
        for path in (REGISTRY / "Topics").rglob("*.md"):
            zip_file.write(path, path.relative_to(ROOT).as_posix())
        for path in (REGISTRY / "Categories").rglob("*.md"):
            zip_file.write(path, path.relative_to(ROOT).as_posix())
    schema["version"] = "5.0"
    schema["description"] = ("Q1-Q42 schema for 500 independent niche CAT configurations; "
                             "46 subject overrides seed new CAT files but are not parallel runtime presets.")
    schema_path.write_text(json.dumps(schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    crosswalk = []
    for row, old_angles, old_niche, old_output, home, new_angles, new_output, values in moves:
        stem = f"{row['id']}_{row['slug']}"
        home.mkdir(parents=True)
        old_angles.rename(new_angles)
        (home / f"CAT_{stem}.md").write_text(render_cat(row, values, schema), encoding="utf-8")
        (home / f"NICHE_{stem}.md").write_text(render_identity(row), encoding="utf-8")
        old_niche.unlink()
        old_output.rename(new_output)
        (new_output / "README.md").write_text(render_output(row), encoding="utf-8")
        crosswalk.append({"id": row["id"], "subject_category": row["primary_category"],
                          "old_angles": old_angles.relative_to(ROOT).as_posix(),
                          "new_angles": new_angles.relative_to(ROOT).as_posix(),
                          "old_niche_preset": old_niche.relative_to(ROOT).as_posix(),
                          "new_cat": (home / f"CAT_{stem}.md").relative_to(ROOT).as_posix(),
                          "new_niche": (home / f"NICHE_{stem}.md").relative_to(ROOT).as_posix(),
                          "old_output": old_output.relative_to(ROOT).as_posix(),
                          "new_output": new_output.relative_to(ROOT).as_posix()})
        row["niche_path"] = home.relative_to(ROOT).as_posix()
        row["current_path"] = new_angles.relative_to(ROOT).as_posix()
    write_csv(REGISTRY / "NICHE_HOME_PATHS.csv", crosswalk, list(crosswalk[0]))
    fields = list(rows[0])
    write_csv(TAXONOMY, rows, fields)
    by_id = {entry["id"]: entry for entry in crosswalk}
    legacy_path = REGISTRY / "LEGACY_TOPIC_PATHS.csv"
    with legacy_path.open(encoding="utf-8", newline="") as fh:
        old_map = list(csv.DictReader(fh))
    for entry in old_map:
        entry["new_path"] = by_id[entry["id"]]["new_angles"]
    write_csv(legacy_path, old_map, list(old_map[0]))
    defaults_path = REGISTRY / "LEGACY_TOPIC_DEFAULTS.csv"
    with defaults_path.open(encoding="utf-8", newline="") as fh:
        defaults = list(csv.DictReader(fh))
    for entry in defaults:
        niche_id = Path(entry["topic_path"]).name[:3]
        item = by_id[niche_id]
        entry["topic_path"] = entry["topic_path"].replace(item["old_angles"], item["new_angles"], 1)
    write_csv(defaults_path, defaults, list(defaults[0]))
    # Pilots are kept under AUDIT but use the same ID-first project layout.
    old_pilot = checked(ROOT / "AUDIT" / "PILOTS" / "Physical_Sciences" / "Topics" / "343_physics")
    new_pilot = checked(ROOT / "AUDIT" / "PILOTS" / "343_physics")
    if not old_pilot.is_dir() or new_pilot.exists():
        raise ValueError("Pilot directory changed during migration")
    old_pilot.rename(new_pilot)
    for base in (ROOT / "OUTPUT", ROOT / "AUDIT" / "PILOTS"):
        for config in base.rglob("CONFIG.md"):
            text = config.read_text(encoding="utf-8")
            match = re.search(r"^Niche ID: (\d{3})$", text, re.M)
            if not match or match.group(1) not in by_id:
                continue
            item = by_id[match.group(1)]
            text = text.replace(f"Niche preset: `{item['old_niche_preset']}`",
                                f"Niche identity: `{item['new_niche']}`\nCAT preset: `{item['new_cat']}`")
            text = text.replace("Topic preset: `", "Angle preset: `")
            text = text.replace(item["old_angles"], item["new_angles"])
            text = text.replace("Question schema version: 4.0", "Question schema version: 5.0")
            text = text.replace(" | niche_preset |", " | niche_cat |")
            text = text.replace(" | topic_angle |", " | angle_preset |")
            text = text.replace(" | visual_style_registry |", " | niche_cat |")
            config.write_text(text, encoding="utf-8")
    # Remove only empty former folders inside the verified workspace.
    for folder in (REGISTRY / "Topics", REGISTRY / "Categories" / "Niches", ROOT / "OUTPUT"):
        for old_category in sorted({row["primary_category"] for row in rows}):
            path = folder / old_category
            if folder == ROOT / "OUTPUT":
                topics = path / "Topics"
                if topics.is_dir() and not any(topics.iterdir()):
                    checked(topics).rmdir()
            if path.is_dir() and not any(path.iterdir()):
                checked(path).rmdir()
    for path in (REGISTRY / "Topics" / "README.md", REGISTRY / "Categories" / "README.md"):
        if path.is_file():
            path.unlink()
    for path in (REGISTRY / "Topics", REGISTRY / "Categories" / "Niches"):
        if path.is_dir() and not any(path.iterdir()):
            checked(path).rmdir()
    for path in (REGISTRY / "Categories").glob("CAT_*.md"):
        path.unlink()  # exact copies are in the migration archive
    if (REGISTRY / "Categories").is_dir() and not any((REGISTRY / "Categories").iterdir()):
        checked(REGISTRY / "Categories").rmdir()
    old_pilot_parent = old_pilot.parent
    for path in (old_pilot_parent, old_pilot_parent.parent):
        if path.is_dir() and not any(path.iterdir()):
            checked(path).rmdir()
    print(f"Migrated {len(moves)} niche homes and 500 output folders; archive: {archive}")


if __name__ == "__main__":
    main()
