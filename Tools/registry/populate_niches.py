#!/usr/bin/env python3
"""Check or create Q3-only angle choices from base or curated niche plans.

Default is read-only. `--create-missing` creates absent files without overwriting.
`--sync-content` updates generated files from their editable angle plans.
Category routing comes only from NICHE_TAXONOMY.csv.
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "REGISTRY"
SCHEMA = json.loads((REGISTRY / "CONFIG_SCHEMA.json").read_text(encoding="utf-8"))
TAXONOMY = REGISTRY / "NICHE_TAXONOMY.csv"
MASTER = REGISTRY / "MASTER_REGISTRY.md"
VISUALS = REGISTRY / "MASTER_VISUAL_STYLE.md"
MASTER_EXTENSION = REGISTRY / "MASTER_REGISTRY_EXTENSION.md"
VISUALS_EXTENSION = REGISTRY / "MASTER_VISUAL_STYLE_EXTENSION.md"


def expected_ids():
    with TAXONOMY.open(encoding="utf-8", newline="") as fh:
        ids = {int(row["id"]) for row in csv.DictReader(fh)}
    if not ids or ids != set(range(1, max(ids) + 1)) or max(ids) < 500:
        raise ValueError("Taxonomy IDs must be contiguous from 001 and retain the original 500")
    return ids


def slugify(value):
    value = re.sub(r"[^\w\s-]", "", value.lower())
    value = re.sub(r"[\s_/]+", "_", value)
    return re.sub(r"_+", "_", value).strip("_")[:60]


def parse_master_registry():
    niches = []
    current = None
    sources = [MASTER]
    if MASTER_EXTENSION.is_file():
        sources.append(MASTER_EXTENSION)
    for line in "\n".join(path.read_text(encoding="utf-8") for path in sources).splitlines():
        heading = re.match(r"^## (\d+)\. (.+)$", line)
        if heading:
            if current:
                niches.append(current)
            current = (int(heading.group(1)), heading.group(2).strip(), [])
            continue
        angle = re.match(r"^\d+\. (.+?) — (.+)$", line)
        if current and angle:
            current[2].append((angle.group(1).strip(), angle.group(2).strip()))
    if current:
        niches.append(current)
    ids = expected_ids()
    if {niche_id for niche_id, _, _ in niches} != ids or len(niches) != len(ids) or any(len(angles) != 15 for _, _, angles in niches):
        raise ValueError("Master registry must contain every taxonomy ID with 15 base angles each")
    return niches


def parse_visual_style():
    styles = {}
    names = ("niche", "primary_visual_style", "visual_language", "palette", "lighting",
             "camera", "motion", "thumbnail_direction", "ai_keywords", "avoid")
    sources = [VISUALS]
    if VISUALS_EXTENSION.is_file():
        sources.append(VISUALS_EXTENSION)
    for line in "\n".join(path.read_text(encoding="utf-8") for path in sources).splitlines():
        match = re.match(r"^\|\s*(\d+)\s*\|(.+)$", line)
        if match:
            cells = [cell.strip() for cell in match.group(2).split("|")]
            if len(cells) >= len(names):
                styles[int(match.group(1))] = dict(zip(names, cells))
    if set(styles) != expected_ids():
        raise ValueError("Visual style registry must cover every taxonomy ID")
    return styles


def load_taxonomy():
    with TAXONOMY.open(encoding="utf-8", newline="") as fh:
        rows = {int(row["id"]): row for row in csv.DictReader(fh)}
    if set(rows) != expected_ids():
        raise ValueError("Taxonomy IDs are incomplete")
    return rows


def angle_entries(row, master_angles):
    """Return curated niche choices when present, otherwise the master 15."""
    home = REGISTRY / "Niches" / f"{row['id']}_{row['slug']}"
    plan = home / "ANGLE_PLAN.json"
    if not plan.is_file():
        return [dict(slug=slugify(angle), angle=angle, scope="", question="")
                for _, angle in master_angles]
    data = json.loads(plan.read_text(encoding="utf-8"))
    if data.get("niche_id") != row["id"] or not isinstance(data.get("angles"), list):
        raise ValueError(f"Invalid niche angle plan: {plan}")
    entries = data["angles"]
    slugs = [entry.get("slug") for entry in entries]
    if len(entries) < 15 or len(slugs) != len(set(slugs)):
        raise ValueError(f"Angle plan needs at least 15 unique choices: {plan}")
    original_slugs = {slugify(angle) for _, angle in master_angles}
    if not original_slugs.issubset(slugs):
        raise ValueError(f"Angle plan removed a stable original slug: {plan}")
    if (len({entry.get("angle") for entry in entries}) != len(entries)
            or len({entry.get("question") for entry in entries}) != len(entries)
            or len({entry.get("scope", "").strip() for entry in entries}) != len(entries)):
        raise ValueError(f"Angle plan repeats an angle, story question or scope: {plan}")
    for entry in entries:
        if (not re.fullmatch(r"[a-z0-9]+(?:_[a-z0-9]+)*", entry.get("slug", ""))
                or any(not isinstance(entry.get(key), str) or not entry[key].strip()
                       for key in ("angle", "scope", "question", "evidence", "boundary"))
                or not entry["question"].strip().endswith("?")
                or "|" in entry["angle"] or "\n" in entry["angle"]):
            raise ValueError(f"Incomplete curated angle in {plan}")
    return entries


def render_visual(niche_id, style):
    columns = (
        ("Primary Visual Style", "primary_visual_style"),
        ("Visual Language", "visual_language"), ("Palette", "palette"),
        ("Lighting", "lighting"), ("Camera / Lens", "camera"),
        ("Motion", "motion"), ("Thumbnail Direction", "thumbnail_direction"),
        ("AI Prompt Keywords", "ai_keywords"), ("Avoid", "avoid"),
    )
    lines = [f"## Visual Style (MASTER_VISUAL_STYLE.md row {niche_id})", "",
             "| Field | Value |", "|---|---|"]
    lines.extend(f"| {label} | {style[key]} |" for label, key in columns)
    return "\n".join(lines)


def generate_topic_preset(niche_id, niche_name, angle, category, slug, style, entry=None):
    angle_slug = entry["slug"] if entry else slugify(angle)
    topic_id = f"{niche_id:03}_{slug}_{angle_slug}"
    content = (
        f"# {topic_id}: {niche_name} — {angle}\n\n"
        f"> Subject category: {category}\n"
        f"> CAT: ../CAT_{niche_id:03}_{slug}.md\n"
        f"> NICHE: ../NICHE_{niche_id:03}_{slug}.md\n\n"
        "This angle supplies Q3 only. All other defaults come from the niche CAT file.\n\n"
        f"## Q3: {SCHEMA['questions']['Q3']['label']}\n"
        f"**Default:** {angle}\n"
    )
    if entry:
        content += (
            f"\n## Editorial scope\n\n"
            f"**Focus / example question:** {entry['question']}\n\n"
            f"**Coverage:** {entry['scope']}\n\n"
            f"**Evidence to seek:** {entry['evidence']}\n\n"
            f"**Limits:** {entry['boundary']}\n\n"
            "Before Phase 1, narrow this guidance to a specific case, source or work, "
            "and the relevant place, population, version or period. Record that choice in the episode's story question and research summary.\n"
        )
    return topic_id + ".md", content


def generate_index(niche_id, niche_name, entries, curated=False):
    lines = [f"# {niche_name} -- All Topics", "",
             f"> Niche ID: {niche_id} | {len(entries)} topic presets",
             "> Auto-generated from MASTER_REGISTRY.md + MASTER_VISUAL_STYLE.md", "", "---", ""]
    if curated:
        lines[3] = "> Auto-generated from ANGLE_PLAN.json"
        lines += ["Curated niche-specific angle plan: [ANGLE_PLAN.json](../ANGLE_PLAN.json)", ""]
    lines.extend(f"- [{name} ({angle})](./{filename})" for name, angle, filename in entries)
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--create-missing", action="store_true", help="Create absent angle files; never overwrite")
    parser.add_argument("--verify-content", action="store_true", help="Compare existing files with deterministic generated content")
    parser.add_argument("--sync-content", action="store_true", help="Write current angle plans to files, including updated content")
    parser.add_argument("--id", type=int, help="Limit a check or sync to one stable niche ID")
    parser.add_argument("--id-from", type=int, help="Limit a check or sync to IDs at or above this value")
    parser.add_argument("--id-to", type=int, help="Limit a check or sync to IDs at or below this value")
    parser.add_argument("--progress", action="store_true", help="Print progress through the selected niche plans")
    args = parser.parse_args()
    if args.sync_content and args.verify_content:
        parser.error("--sync-content and --verify-content cannot be combined")
    taxonomy = load_taxonomy()
    styles = parse_visual_style()
    niches = parse_master_registry()
    if args.id is not None:
        if args.id not in taxonomy:
            parser.error(f"Unknown niche ID: {args.id}")
        niches = [item for item in niches if item[0] == args.id]
    if args.id_from is not None:
        niches = [item for item in niches if item[0] >= args.id_from]
    if args.id_to is not None:
        niches = [item for item in niches if item[0] <= args.id_to]
    if not niches:
        parser.error("No niches match the selected ID range")
    missing = []
    drift = []
    updates = []
    angle_count = 0
    for niche_id, name, angles in niches:
        if args.progress and niche_id % 25 == 0:
            print(f"Checked through niche {niche_id:03}", file=sys.stderr, flush=True)
        row = taxonomy[niche_id]
        if name != row["title"]:
            raise ValueError(f"Title mismatch for ID {niche_id}")
        category, slug = row["primary_category"], row["slug"]
        if category not in SCHEMA["category_overrides"]:
            raise ValueError(f"Unknown category for ID {niche_id}: {category}")
        folder = REGISTRY / "Niches" / f"{niche_id:03}_{slug}" / "Angles"
        if folder.as_posix() != (ROOT / row["current_path"]).as_posix():
            raise ValueError(f"Taxonomy path mismatch for ID {niche_id}")
        entries = []
        choices = angle_entries(row, angles)
        angle_count += len(choices)
        for entry in choices:
            angle = entry["angle"]
            filename, content = generate_topic_preset(niche_id, name, angle, category, slug, styles[niche_id], entry if entry["scope"] else None)
            target = folder / filename
            entries.append((name, angle, filename))
            if not target.exists():
                missing.append((target, content))
            elif (args.verify_content or args.sync_content) and target.read_text(encoding="utf-8") != content:
                (updates if args.sync_content else drift).append((target, content))
        index = folder / "ALL_TOPICS_BY_NICHE.md"
        index_content = generate_index(niche_id, name, entries, (folder.parent / "ANGLE_PLAN.json").is_file())
        if not index.exists():
            missing.append((index, index_content))
        elif (args.verify_content or args.sync_content) and index.read_text(encoding="utf-8") != index_content:
            (updates if args.sync_content else drift).append((index, index_content))
    if args.create_missing or args.sync_content:
        for target, content in missing:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
    if args.sync_content:
        for target, content in updates:
            target.write_text(content, encoding="utf-8")
    noun = "niche" if len(niches) == 1 else "niches"
    print(f"Checked {len(niches)} {noun} and {angle_count} angles; missing={len(missing)}; drift={len(drift)}; created={len(missing) if args.create_missing or args.sync_content else 0}; updated={len(updates) if args.sync_content else 0}")
    if drift:
        print("\n".join(str(path.relative_to(ROOT)) for path, _ in drift[:20]))
        raise SystemExit("Generated content differs from existing topic files")


if __name__ == "__main__":
    main()
