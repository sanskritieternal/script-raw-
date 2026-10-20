"""Create missing ID-first niche records without overwriting edited CAT defaults."""
import argparse
import csv
import json
from pathlib import Path

from Tools.registry.niche_home_templates import render_cat, render_identity, render_output
from Tools.registry.populate_niches import parse_visual_style, expected_ids

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "REGISTRY"
SCHEMA = json.loads((REGISTRY / "CONFIG_SCHEMA.json").read_text(encoding="utf-8"))


def paths(row):
    stem = f"{row['id']}_{row['slug']}"
    home = REGISTRY / "Niches" / stem
    return home / f"CAT_{stem}.md", home / f"NICHE_{stem}.md", ROOT / "OUTPUT" / stem


def seed_cat(row, styles):
    values = {qid: entry["default"] for qid, entry in SCHEMA["questions"].items()}
    values.update(SCHEMA["category_overrides"][row["primary_category"]])
    values["Q1"] = row["primary_category"]
    values["Q15"] = styles[int(row["id"])]["primary_visual_style"]
    return render_cat(row, values, SCHEMA)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-content", action="store_true")
    args = parser.parse_args()
    with (REGISTRY / "NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if len(rows) != len(expected_ids()) or {int(r["id"]) for r in rows} != expected_ids():
        raise ValueError("Taxonomy IDs are incomplete")
    styles = parse_visual_style()
    created = 0
    drift = []
    for row in rows:
        cat, identity, output = paths(row)
        expected = ((cat, seed_cat(row, styles)), (identity, render_identity(row)),
                    (output / "README.md", render_output(row)))
        for path, content in expected:
            if not path.exists() and not args.verify_content:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
                created += 1
            elif args.verify_content and (not path.exists() or (path != cat and path.read_text(encoding="utf-8") != content)):
                drift.append(path)
    print(f"Checked {len(rows)} CAT, NICHE and output homes; created={created}; drift={len(drift)}")
    if drift:
        raise SystemExit("\n".join(map(str, drift[:20])))


if __name__ == "__main__":
    main()
