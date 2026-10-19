"""Align generated topic headers with the primary subject category map.

Preserves the original production preset as a separate field. Idempotent.
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TAXONOMY = ROOT / "REGISTRY" / "NICHE_TAXONOMY.csv"


def main():
    with TAXONOMY.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    changed = 0
    checked = 0
    for row in rows:
        directory = ROOT / row["current_path"]
        for path in directory.glob(f"{row['id']}_*.md"):
            data = path.read_text(encoding="utf-8")
            original_data = data
            expected = f"> Category: {row['primary_category']} | Topic Folder: {row['slug']}"
            match = re.search(r"^> Category: ([^|\n]+) \| Topic Folder: ([^\n]+)$", data, re.M)
            if match:
                original = match.group(1).strip()
                if original != row["primary_category"]:
                    replacement = expected + f"\n> Production Preset: CAT_{original}.md"
                    data = data[:match.start()] + replacement + data[match.end():]
                elif match.group(0) != expected:
                    data = data[:match.start()] + expected + data[match.end():]
                # An earlier version appended the production preset on each run.
                lines = data.splitlines(keepends=True)
                seen = False
                clean = []
                for line in lines:
                    if line.startswith("> Production Preset:"):
                        if seen:
                            continue
                        seen = True
                    clean.append(line)
                result = "".join(clean)
                if result != original_data:
                    path.write_text(result, encoding="utf-8")
                    changed += 1
            else:
                if expected not in data or "> Production Preset:" not in data:
                    raise ValueError(f"Unexpected topic header: {path}")
            checked += 1
    if checked != 7500:
        raise ValueError(f"Expected 7500 topics, checked {checked}")
    print(f"Checked {checked} topic files; updated {changed} headers")


if __name__ == "__main__":
    main()
