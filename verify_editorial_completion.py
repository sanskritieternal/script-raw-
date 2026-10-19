"""Check editorial status, question fields, ledger, and one Phase 0 route per niche."""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from create_project import resolve


ROOT = Path(__file__).resolve().parent
NICHE_ROOT = ROOT / "REGISTRY" / "Niches"
LEDGER = ROOT / "AUDIT" / "ANGLE_EDITORIAL_REVIEW.csv"
EXPECTED_PILOTS = {"001": "pilot_for_review", "004": "deep_pilot_for_review"}


def main(original_only=False):
    with (ROOT / "REGISTRY" / "NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as stream:
        taxonomy = [row for row in csv.DictReader(stream) if not original_only or int(row["id"]) <= 500]
    with LEDGER.open(encoding="utf-8", newline="") as stream:
        ledger = {row["niche_id"]: row for row in csv.DictReader(stream) if not original_only or int(row["niche_id"]) <= 500}
    errors = []
    statuses = Counter()
    angle_count = 0
    expected_ids = {f"{i:03}" for i in range(1, (501 if original_only else len(taxonomy) + 1))}
    if {r["id"] for r in taxonomy} != expected_ids or set(ledger) != expected_ids:
        errors.append("Taxonomy and editorial ledger must cover the same contiguous IDs")
    for row in taxonomy:
        niche_id = row["id"]
        stem = f"{niche_id}_{row['slug']}"
        plan_path = NICHE_ROOT / stem / "ANGLE_PLAN.json"
        if not plan_path.is_file():
            errors.append(f"Missing plan: {stem}")
            continue
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        status = plan.get("status")
        statuses[status] += 1
        expected_status = EXPECTED_PILOTS.get(niche_id, "editorial_question_reviewed")
        if plan.get("niche_id") != niche_id or status != expected_status:
            errors.append(f"Identity or editorial status mismatch: {stem}")
        if int(niche_id) >= 501:
            review = plan.get("editorial_review", {})
            sources = plan.get("research_sources", [])
            if (review.get("angles") != len(plan["angles"]) or not review.get("checks")
                    or not sources or any(not all(s.get(k) for k in ("title", "url", "checked_date", "role")) for s in sources)
                    or not plan.get("related_niches")):
                errors.append(f"Missing expansion review, source or overlap record: {stem}")
        ledger_row = ledger.get(niche_id)
        if not ledger_row or ledger_row["status"] != status or int(ledger_row["angles"]) != len(plan["angles"]):
            errors.append(f"Ledger mismatch: {stem}")
        angles = plan["angles"]
        slugs = [entry.get("slug") for entry in angles]
        if len(slugs) != len(set(slugs)) or len(slugs) < 15:
            errors.append(f"Duplicate or missing stable slugs: {stem}")
        required_fields = ("slug", "angle", "question", "scope")
        if status == "editorial_question_reviewed":
            required_fields += ("evidence", "boundary")
        for entry in angles:
            if any(not isinstance(entry.get(key), str) or not entry[key].strip()
                   for key in required_fields):
                errors.append(f"Incomplete question design: {stem}/{entry.get('slug')}")
        angle_count += len(angles)
        if not angles:
            continue
        try:
            resolved_row, topic, values, sources, *_ = resolve(int(niche_id), slugs[-1])
        except (ValueError, KeyError, FileNotFoundError) as exc:
            errors.append(f"Phase 0 route failed: {stem}: {exc}")
            continue
        if (resolved_row["id"] != niche_id or values["Q1"] != row["primary_category"]
                or values["Q3"] != angles[-1]["angle"] or sources["Q3"] != "angle_preset"
                or not topic.is_file()):
            errors.append(f"Phase 0 route mismatch: {stem}")
    if errors:
        raise SystemExit("\n".join(errors[:100]) + f"\n{len(errors)} completion errors")
    print(f"Editorial completion verified: {len(taxonomy)} plans, {angle_count} angles, "
          f"{statuses['editorial_question_reviewed']} reviewed, {sum(statuses[s] for s in EXPECTED_PILOTS.values())} pilots, "
          f"{len(taxonomy)} Phase 0 niche routes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--original-500", action="store_true", help="Verify only the original 500-plan milestone")
    main(parser.parse_args().original_500)
