"""Build the browsable niche master list from the active taxonomy and plans."""

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "REGISTRY"
TAXONOMY = REGISTRY / "NICHE_TAXONOMY.csv"
TARGET = REGISTRY / "NICHE_MASTER_LIST.md"
STATUS_LABELS = {
    "editorial_question_reviewed": "Questions reviewed",
    "pilot_for_review": "Pilot for review",
    "deep_pilot_for_review": "Deep pilot for review",
    "generated_editorial_draft": "Draft",
}


def link(label, path):
    return f"[{label}]({path})"


def escape(value):
    return value.replace("|", "\\|").replace("\n", " ").strip()


def main():
    with TAXONOMY.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    ids = [int(row["id"]) for row in rows]
    if ids != list(range(1, len(rows) + 1)) or len(set(row["slug"] for row in rows)) != len(rows):
        raise ValueError("Taxonomy IDs must be ordered, contiguous and have unique slugs")

    counts = Counter(row["primary_category"] for row in rows)
    lines = [
        "# Niche master list", "",
        f"**{len(rows)} niches** across **{len(counts)} subject categories**. "
        "This list is generated from [NICHE_TAXONOMY.csv](NICHE_TAXONOMY.csv) and each niche's `ANGLE_PLAN.json`.",
        "The ID is the stable project identity. The subject is its current Q1 category; "
        "each niche has its own CAT configuration and output folder.", "",
        "Browse by [subject category](CATEGORY_INDEX.md) or see the [niche directory](Niches/README.md). "
        "`Draft` plans need editorial review before an episode is researched.", "",
        "Refresh this file after taxonomy or plan changes with `python build_niche_master_list.py`.", "",
        "Concrete episode proposals live in optional niche idea banks. Browse [IDEA_MASTER_LIST.md](IDEA_MASTER_LIST.md) and read [IDEA_BANK_GUIDE.md](IDEA_BANK_GUIDE.md); an angle is not automatically an episode idea.", "",
        "For optional topic coverage and series planning, browse [DEPTH_MASTER_LIST.md](DEPTH_MASTER_LIST.md) and [DEPTH_PLANNING_GUIDE.md](DEPTH_PLANNING_GUIDE.md). Reusable source leads are in [SOURCE_LIBRARY.md](SOURCE_LIBRARY.md).", "",
        "Each angle has a focus, coverage, evidence directions and limits. See the [angle scope guide](ANGLE_SCOPE_GUIDE.md) for editing and production use.", "",
        "| Status | Plans |", "|---|---:|",
    ]
    status_counts = Counter()
    entries = []
    angle_total = 0
    for row in rows:
        stem = f"{row['id']}_{row['slug']}"
        home = ROOT / row["niche_path"]
        plan_path = home / "ANGLE_PLAN.json"
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        if plan.get("niche_id") != row["id"]:
            raise ValueError(f"Plan ID mismatch: {plan_path}")
        angles = plan.get("angles", [])
        if not angles:
            raise ValueError(f"Plan has no angles: {plan_path}")
        required = [
            home / f"NICHE_{stem}.md",
            home / f"CAT_{stem}.md",
            home / "Angles" / "ALL_TOPICS_BY_NICHE.md",
            ROOT / "OUTPUT" / stem / "README.md",
        ]
        if any(not path.is_file() for path in required):
            raise ValueError(f"Missing niche route: {stem}")
        status = plan.get("status", "unknown")
        status_counts[status] += 1
        angle_total += len(angles)
        subject = row["primary_category"].replace("_", " ")
        files = " · ".join([
            link("NICHE", f"Niches/{stem}/NICHE_{stem}.md"),
            link("CAT", f"Niches/{stem}/CAT_{stem}.md"),
            link("Plan", f"Niches/{stem}/ANGLE_PLAN.json"),
            link("Angles", f"Niches/{stem}/Angles/ALL_TOPICS_BY_NICHE.md"),
            link("OUTPUT", f"../OUTPUT/{stem}/README.md"),
        ])
        entries.append((int(row["id"]),
                        f"| {row['id']} | {escape(row['title'])} | {escape(subject)} | {len(angles)} | "
                        f"{STATUS_LABELS.get(status, escape(status))} | {files} |"))

    for status, count in sorted(status_counts.items()):
        lines.append(f"| {STATUS_LABELS.get(status, escape(status))} | {count} |")
    lines += ["", f"**Total angle choices:** {angle_total:,}.", ""]
    for start in range(1, len(rows) + 1, 100):
        end = min(start + 99, len(rows))
        lines += [f"## IDs {start:03}–{end:03}", "",
                  "| ID | Niche | Subject category | Angles | Editorial status | Files |",
                  "|---:|---|---|---:|---|---|"]
        lines.extend(value for number, value in entries if start <= number <= end)
        lines.append("")
    TARGET.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {TARGET}: {len(rows)} niches, {angle_total} angles, {len(counts)} subjects")


if __name__ == "__main__":
    main()
