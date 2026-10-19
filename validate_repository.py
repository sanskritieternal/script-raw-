"""Validate independent CAT/NICHE homes, angles, output and routing."""
import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

from create_project import resolve, render, parse_duration
from materialize_niches import paths, render_identity, render_output
from populate_niches import load_taxonomy, parse_master_registry, parse_visual_style, generate_topic_preset, generate_index, angle_entries
from restructure_categories import mapping as category_mapping

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "REGISTRY"
SCHEMA = json.loads((REGISTRY / "CONFIG_SCHEMA.json").read_text(encoding="utf-8"))


def defaults(path):
    return re.findall(r"^## (Q\d+): ([^\n]+)\n\*\*Default:\*\* ([^\n]+)", path.read_text(encoding="utf-8"), re.M)


def main(progress=False):
    errors = []
    rows = load_taxonomy()
    expected_stems = {f"{r['id']}_{r['slug']}" for r in rows.values()}
    assignments = category_mapping()
    counts = Counter(r["primary_category"] for r in rows.values())
    from idea_bank import catalog, index_text
    _, idea_errors = catalog()
    errors.extend(idea_errors)
    from Tools.depth_planning import validate as validate_depth
    errors.extend(validate_depth())
    if not idea_errors:
        idea_index = REGISTRY / "IDEA_MASTER_LIST.md"
        if not idea_index.is_file() or idea_index.read_text(encoding="utf-8") != index_text():
            errors.append("Idea master list is absent or stale; run python idea_bank.py build-index")
    if len(counts) != 46 or set(counts) != set(SCHEMA["category_overrides"]):
        errors.append("Subject taxonomy or schema category overrides differ")
    actual_homes = {p.name for p in (REGISTRY / "Niches").iterdir() if p.is_dir()}
    actual_output = {p.name for p in (ROOT / "OUTPUT").iterdir() if p.is_dir() and p.name != "Legacy"}
    if actual_homes != expected_stems:
        errors.append("Niche home folders differ from taxonomy")
    if actual_output != expected_stems:
        errors.append("Output folders differ from taxonomy")
    for obsolete in (REGISTRY / "Categories", REGISTRY / "Topics"):
        if obsolete.exists():
            errors.append(f"Obsolete active registry directory remains: {obsolete}")
    styles = parse_visual_style()
    topics = {n: (title, angles) for n, title, angles in parse_master_registry()}
    angle_count = 0
    for niche_id, row in rows.items():
        if progress and niche_id % 25 == 0:
            print(f"Validated through niche {niche_id:03}", file=sys.stderr, flush=True)
        stem = f"{row['id']}_{row['slug']}"
        if niche_id <= 500 and row["primary_category"] != assignments[niche_id]:
            errors.append(f"Category assignment mismatch: {stem}")
        cat, identity, output = paths(row)
        home = cat.parent
        if not (home / "ANGLE_PLAN.json").is_file():
            errors.append(f"Missing editable angle plan: {stem}")
            continue
        if {p.name for p in home.glob("*.md")} != {cat.name, identity.name}:
            errors.append(f"CAT/NICHE file set mismatch: {stem}")
        if row.get("niche_path") != home.relative_to(ROOT).as_posix():
            errors.append(f"Niche path mismatch: {stem}")
        if not cat.is_file() or not identity.is_file():
            errors.append(f"Missing CAT or NICHE: {stem}")
            continue
        if identity.read_text(encoding="utf-8") != render_identity(row):
            errors.append(f"Identity drift: {stem}")
        if not (output / "README.md").is_file() or (output / "README.md").read_text(encoding="utf-8") != render_output(row):
            errors.append(f"Output landing drift: {stem}")
        found = defaults(cat)
        if [qid for qid, _, _ in found] != list(SCHEMA["questions"]):
            errors.append(f"CAT needs Q1-Q42 in order: {stem}")
        else:
            values = {qid: value for qid, _, value in found}
            for qid, label, value in found:
                if label != SCHEMA["questions"][qid]["label"] or not value.strip():
                    errors.append(f"CAT question invalid: {stem} {qid}")
            if values["Q1"] != row["primary_category"]:
                errors.append(f"CAT Q1 mismatch: {stem}")
            try:
                parse_duration(values)
            except ValueError as exc:
                errors.append(f"CAT timing invalid: {stem}: {exc}")
            if values["Q8"] not in {"Low", "Moderate", "High", "Critical"} or values["Q41"] not in {"Standard", "Strict", "Critical"}:
                errors.append(f"CAT risk values invalid: {stem}")
        folder = home / "Angles"
        if row["current_path"] != folder.relative_to(ROOT).as_posix() or not folder.is_dir():
            errors.append(f"Angle path mismatch: {stem}")
            continue
        title, angles = topics[niche_id]
        if title != row["title"]:
            errors.append(f"Title mismatch: {stem}")
        entries = []
        for entry in angle_entries(row, angles):
            angle = entry["angle"]
            name, content = generate_topic_preset(niche_id, title, angle, row["primary_category"], row["slug"], styles[niche_id], entry if entry["scope"] else None)
            path = folder / name
            entries.append((title, angle, name))
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                errors.append(f"Missing or drifted angle: {path}")
            angle_count += 1
        if {p.name for p in folder.glob("*.md")} != {name for _, _, name in entries} | {"ALL_TOPICS_BY_NICHE.md"}:
            errors.append(f"Angle file set mismatch: {stem}")
        index = folder / "ALL_TOPICS_BY_NICHE.md"
        if not index.is_file() or index.read_text(encoding="utf-8") != generate_index(niche_id, title, entries, (home / "ANGLE_PLAN.json").is_file()):
            errors.append(f"Angle index drift: {stem}")
    if angle_count < 7500:
        errors.append(f"Angle total fell below the 7500-base set: {angle_count}")
    pilots = 0
    for category in sorted(counts):
        row = next(r for r in rows.values() if r["primary_category"] == category)
        try:
            resolved = resolve(int(row["id"]), "history_origins")
            config = render(*resolved, "interactive")
            if "CAT preset:" not in config or "Niche identity:" not in config:
                errors.append(f"Phase 0 refs missing: {category}")
            pilots += 1
        except ValueError as exc:
            errors.append(f"Phase 0 pilot failed: {category}: {exc}")
    for category in ("Medicine_Healthcare", "Finance_Banking", "Government_Geopolitics"):
        row = next(r for r in rows.values() if r["primary_category"] == category)
        if "Human review status: Pending" not in render(*resolve(int(row["id"]), "history_origins"), "autonomous"):
            errors.append(f"High-risk review gate missing: {category}")
    if errors:
        print("\n".join(errors[:100]))
        raise SystemExit(f"Validation failed with {len(errors)} errors")
    print(f"Validated {len(rows)} CAT files, {len(rows)} NICHE files, {angle_count} angles, {len(rows)} output folders, {len(counts)} subject tags and {pilots} Phase 0 pilots")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--progress", action="store_true", help="Report progress every 25 niches on stderr")
    main(parser.parse_args().progress)
