"""Audited ID-to-subject mapping for a smaller top-level category taxonomy.

Run without --apply to check the assignment grid. --apply performs a separate,
preflighted migration of topic, niche preset, and output landing paths.
"""
import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TAXONOMY = ROOT / "REGISTRY" / "NICHE_TAXONOMY.csv"


GROUPS = {
    "Finance_Banking": "8 112 293-296 298-300 312-315 499-500",
    "Commerce_Industry": "21 51 105-108 136 230 301-311 316 497-498",
    "Careers_Workplace": "70 103-104 456-457 459-462 464-465 467",
    "Childhood_Family": "17 73 408",
    "Learning_Education": "69 90 145 443-449 453-455 466",
    "Food_Fashion": "24 82 91-92 247",
    "Cultural_Heritage": "52 58-59 84 94-95 141 243-246 248-250 264-267 417",
    "Visual_Arts_Crafts": "42 79 126 258-263 339-341 405",
    "Literature_Performance": "41 43 78 80-81 123-124 255-257 368 385 392 451-452",
    "Speculative_Stories": "11 33 55 166-167 480",
    "Human_Futures": "53 468-472 481-482 489-490 492",
    "Future_Worlds_Systems": "473-479 483-488",
    "Medicine_Healthcare": "15 180-181 281",
    "Mind_Wellness": "16 71 77 101 186",
    "Ancient_Civilizations": "2-3 39-40 150",
    "Historical_People_Cultures": "96 143-144 173 175 177-179",
    "Conflict_Power_Exploration": "35-37 46 49-50",
    "Home_Living": "64 83 102 111 135 393-398 409",
    "Craft_Making": "85-86 137 142 399-404 406-407 410-412",
    "Land_Outdoor": "93 187 191-192",
    "Film_Production": "5 19 125 127 342 369-372 379-380 383-384",
    "Fiction_Worldbuilding": "18 373-378 381-382",
    "Media_Formats_People": "122 146-147 164-165",
    "Hindu_Traditions": "4 268-280 450",
    "World_Religions": "75-76 240 282-289 290-291",
    "Philosophy_Spirituality": "23 54 57 60 292",
    "Space_Astronomy": "12 32 344-347 413",
    "Life_Biology": "26-27 65-68 154 193-204 336 350-355 363",
    "Earth_Environment": "28-30 114-116 152-153 205-217 348 356-357 361-362 415-416",
    "Physical_Sciences": "6 156 343 349 358-360 367 491",
    "Math_Scientific_Methods": "118-121 163 364-366 414",
    "People_Communities": "9 72 148-149 168-172 174 176 317",
    "Government_Geopolitics": "14 97-98 235-239",
    "Crime_Safety_Public_Services": "10 99-100 182-185 493-494 496",
    "Sports_Adventure": "44-45 117 138-140 252-254",
    "Games_Puzzles": "25 56 132-134 251 386-388",
    "Performance_Magic": "389-391",
    "Computing_Software": "61-63 128-131 160 318-325 334-335 463",
    "Cybersecurity_Digital_Systems": "297 326-329 495",
    "Robotics_AI": "1 7 330-333 337-338",
    "Transport_Engineering": "22 31 47-48 109-110 159 418-430",
    "Engineering_Inventions": "13 87-89 155 157 161-162 431-434 442",
    "Energy_Industry": "113 158 435-441",
    "Geography_Places": "20 38 151 218-226 241-242",
    "Travel_Experiences": "34 74 188-190 227-228 232 458",
    "Hospitality_Travel_Systems": "229 231 233-234",
}


def expand(spec):
    result = []
    for part in spec.split():
        if "-" in part:
            start, end = map(int, part.split("-"))
            result.extend(range(start, end + 1))
        else:
            result.append(int(part))
    return result


def mapping():
    groups = {}
    duplicate = []
    for category, spec in GROUPS.items():
        for niche_id in expand(spec):
            if niche_id in groups:
                duplicate.append(niche_id)
            groups[niche_id] = category
    expected = set(range(1, 501))
    if duplicate or set(groups) != expected:
        raise ValueError(f"Duplicate={sorted(duplicate)}; missing={sorted(expected-set(groups))}; extra={sorted(set(groups)-expected)}")
    return groups


def checked(path):
    resolved = path.resolve()
    if resolved == ROOT or not resolved.is_relative_to(ROOT):
        raise ValueError(f"Path escaped workspace: {path}")
    return resolved


def write_csv(path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def apply(rows, groups):
    registry = ROOT / "REGISTRY"
    old_schema_path = registry / "CONFIG_SCHEMA.json"
    old_schema = json.loads(old_schema_path.read_text(encoding="utf-8"))
    if set(old_schema["category_overrides"]) != {r["primary_category"] for r in rows}:
        raise ValueError("Schema does not match pre-migration taxonomy")
    if set(old_schema["category_overrides"]) == set(GROUPS):
        raise ValueError("New category schema already active")
    crosswalk = []
    for row in rows:
        old_category = row["primary_category"]
        new_category = groups[int(row["id"])]
        stem = f"{row['id']}_{row['slug']}"
        old_topic = checked(ROOT / row["current_path"])
        new_topic = checked(registry / "Topics" / new_category / row["slug"])
        old_preset = checked(registry / "Categories" / "Niches" / old_category / f"NICHE_{stem}.md")
        new_preset = checked(registry / "Categories" / "Niches" / new_category / f"NICHE_{stem}.md")
        old_output = checked(ROOT / "OUTPUT" / old_category / "Topics" / stem)
        new_output = checked(ROOT / "OUTPUT" / new_category / "Topics" / stem)
        for source, target in ((old_topic, new_topic), (old_preset, new_preset), (old_output, new_output)):
            if not source.exists() or target.exists():
                raise ValueError(f"Missing source or target collision: {source} -> {target}")
        crosswalk.append({"id": row["id"], "title": row["title"], "old_category": old_category,
                          "new_category": new_category, "old_topic_path": old_topic.relative_to(ROOT).as_posix(),
                          "new_topic_path": new_topic.relative_to(ROOT).as_posix(),
                          "old_niche_preset": old_preset.relative_to(ROOT).as_posix(),
                          "new_niche_preset": new_preset.relative_to(ROOT).as_posix(),
                          "old_output_path": old_output.relative_to(ROOT).as_posix(),
                          "new_output_path": new_output.relative_to(ROOT).as_posix()})
    for command in (("validate_repository.py",), ("populate_niches.py", "--verify-content")):
        subprocess.run([sys.executable, *(str(ROOT / command[0]), *command[1:])], cwd=ROOT, check=True)
    parents = {}
    for category in GROUPS:
        source_counts = Counter(r["primary_category"] for r in rows if groups[int(r["id"])] == category)
        parents[category] = source_counts.most_common(1)[0][0]
    backup = checked(ROOT / "AUDIT" / "Taxonomy_Restructure_2026-10-16")
    if backup.exists():
        raise ValueError(f"Backup already exists: {backup}")
    backup.mkdir(parents=True)
    for source in (TAXONOMY, old_schema_path, registry / "LEGACY_TOPIC_PATHS.csv", registry / "LEGACY_TOPIC_DEFAULTS.csv"):
        shutil.copy2(source, backup / source.name)
    category_backup = backup / "Subject_Presets"
    category_backup.mkdir()
    for path in (registry / "Categories").glob("CAT_*.md"):
        shutil.copy2(path, category_backup / path.name)
    write_csv(registry / "CATEGORY_RESTRUCTURE_PATHS.csv", crosswalk, list(crosswalk[0]))
    for item in crosswalk:
        for old_key, new_key in (("old_topic_path", "new_topic_path"),
                                 ("old_niche_preset", "new_niche_preset"),
                                 ("old_output_path", "new_output_path")):
            source, target = checked(ROOT / item[old_key]), checked(ROOT / item[new_key])
            target.parent.mkdir(parents=True, exist_ok=True)
            source.rename(target)
    old_by_id = {item["id"]: item for item in crosswalk}
    for row in rows:
        row["legacy_secondary_categories"] = row.pop("secondary_categories")
        row["secondary_categories"] = ""
        row["primary_category"] = groups[int(row["id"])]
        row["current_path"] = old_by_id[row["id"]]["new_topic_path"]
        row["review_status"] = "reclassified_from_title_2026_10_16"
    fields = ["id", "title", "current_path", "primary_category", "secondary_categories",
              "legacy_secondary_categories", "slug", "review_status"]
    write_csv(TAXONOMY, rows, fields)
    new_schema = dict(old_schema)
    new_schema["version"] = "4.0"
    new_schema["description"] = "Canonical Q1-Q42 schema for 46 subject categories and 500 stable niche IDs."
    new_schema["category_overrides"] = {category: old_schema["category_overrides"][parents[category]]
                                         for category in sorted(GROUPS)}
    old_schema_path.write_text(json.dumps(new_schema, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Active category files and topic answer blocks are generated from the new schema.
    import reconcile_config_presets
    reconcile_config_presets.main()
    import materialize_niches
    import populate_niches
    for row in rows:
        preset, output = materialize_niches.paths(row)
        preset.write_text(materialize_niches.render_preset(row), encoding="utf-8")
        (output / "README.md").write_text(materialize_niches.render_output(row, preset), encoding="utf-8")
    master = {niche_id: (name, angles) for niche_id, name, angles in populate_niches.parse_master_registry()}
    visuals = populate_niches.parse_visual_style()
    for row in rows:
        niche_id = int(row["id"])
        name, angles = master[niche_id]
        folder = ROOT / row["current_path"]
        for _, angle in angles:
            filename, content = populate_niches.generate_topic_preset(
                niche_id, name, angle, row["primary_category"], row["slug"], visuals[niche_id])
            (folder / filename).write_text(content, encoding="utf-8")
    # Keep the original pre-V6 path map current without erasing its original source paths.
    legacy_map = registry / "LEGACY_TOPIC_PATHS.csv"
    with legacy_map.open(encoding="utf-8", newline="") as fh:
        old_paths = list(csv.DictReader(fh))
    for entry in old_paths:
        entry["new_path"] = old_by_id[entry["id"]]["new_topic_path"]
    write_csv(legacy_map, old_paths, list(old_paths[0]))
    defaults_path = registry / "LEGACY_TOPIC_DEFAULTS.csv"
    with defaults_path.open(encoding="utf-8", newline="") as fh:
        defaults = list(csv.DictReader(fh))
    for entry in defaults:
        old = entry["topic_path"]
        niche_id = Path(old).name[:3]
        item = old_by_id[niche_id]
        entry["topic_path"] = old.replace(item["old_topic_path"], item["new_topic_path"], 1)
    write_csv(defaults_path, defaults, list(defaults[0]))
    # Migrate the text pilots and update existing project CONFIG identity references.
    pilot_old = checked(ROOT / "AUDIT" / "PILOTS" / "Science_Nature" / "Topics" / "343_physics")
    pilot_new = checked(ROOT / "AUDIT" / "PILOTS" / "Physical_Sciences" / "Topics" / "343_physics")
    if not pilot_old.is_dir() or pilot_new.exists():
        raise ValueError("Pilot path state changed during migration")
    pilot_new.parent.mkdir(parents=True, exist_ok=True)
    pilot_old.rename(pilot_new)
    for base in (ROOT / "OUTPUT", ROOT / "AUDIT" / "PILOTS"):
        for config in base.rglob("CONFIG.md"):
            match = re.search(r"^Niche ID: (\d{3})$", config.read_text(encoding="utf-8"), re.M)
            if not match or match.group(1) not in old_by_id:
                continue
            item = old_by_id[match.group(1)]
            text = config.read_text(encoding="utf-8")
            text = text.replace(f"Subject category: {item['old_category']}", f"Subject category: {item['new_category']}")
            text = text.replace(f"| Q1 | Content Category | {item['old_category']} |", f"| Q1 | Content Category | {item['new_category']} |")
            text = text.replace(item["old_topic_path"], item["new_topic_path"])
            text = text.replace(item["old_niche_preset"], item["new_niche_preset"])
            text = text.replace("Question schema version: 3.0", "Question schema version: 4.0")
            config.write_text(text, encoding="utf-8")
    # Remove empty former subject directories only; no recursive deletion occurs.
    old_categories = set(parents.values())
    for category in old_categories:
        for path in (registry / "Topics" / category, registry / "Categories" / "Niches" / category,
                     ROOT / "OUTPUT" / category / "Topics", ROOT / "OUTPUT" / category,
                     ROOT / "AUDIT" / "PILOTS" / category / "Topics", ROOT / "AUDIT" / "PILOTS" / category):
            if path.is_dir() and not any(path.iterdir()):
                checked(path).rmdir()
    print(f"Migrated {len(rows)} niches, 7500 topics, 500 niche presets and output folders to {len(GROUPS)} categories")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    groups = mapping()
    with TAXONOMY.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != 500:
        raise ValueError("Expected 500 taxonomy rows")
    counts = Counter(groups[int(row["id"])] for row in rows)
    print(f"Preflight: {len(rows)} niches across {len(counts)} new categories")
    for category, count in sorted(counts.items()):
        print(category, count)
    if args.apply:
        import json
        schema = json.loads((ROOT / "REGISTRY" / "CONFIG_SCHEMA.json").read_text(encoding="utf-8"))
        if schema["version"] != "3.0":
            raise SystemExit("Historical category migration cannot run against the active schema")
        apply(rows, groups)


if __name__ == "__main__":
    main()
