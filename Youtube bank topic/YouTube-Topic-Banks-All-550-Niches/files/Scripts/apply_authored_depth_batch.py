"""Apply a separately authored depth batch; preserve superseded initial proposals.

Preview by default. JSON becomes authoritative after application. A batch already
recorded on a bank is never reapplied over subsequent editorial changes.
"""
import argparse
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from build_initial_subject_maps import PROFILES

ROOT = Path(__file__).resolve().parents[1]
DATE = datetime.now(ZoneInfo("Asia/Calcutta")).date().isoformat()


def parse(path):
    banks = {}
    nid = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        if line.startswith("@"):
            nid = line[1:]
            assert nid.isdigit() and len(nid) == 3 and nid not in banks
            banks[nid] = []
        elif line.startswith("# "):
            title, level, profile = line[2:].split("|")
            assert level in {"foundation", "intermediate", "advanced"} and profile in PROFILES
            banks[nid].append({"title": title, "level": level, "research_profile": profile, "topics": []})
        else:
            question, coverage = line.split("\t")
            assert question.endswith("?") and coverage.strip()
            banks[nid][-1]["topics"].append({"question": question, "coverage": coverage})
    for nid, categories in banks.items():
        assert categories and all(c["topics"] for c in categories)
        questions = [t["question"].casefold() for c in categories for t in c["topics"]]
        scopes = [t["coverage"].casefold() for c in categories for t in c["topics"]]
        assert len(questions) == len(set(questions)) and len(scopes) == len(set(scopes))
    return banks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("detailed_expansion_batch_01.txt"))
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    batch = parse(args.input)
    batch_id = args.input.stem
    total = changed = skipped = 0
    for nid, categories in sorted(batch.items()):
        paths = list((ROOT/"topics").glob(f"{nid}_*/IN_DEPTH_TOPIC_BANK.json"))
        assert len(paths) == 1, nid
        path = paths[0]
        bank = json.loads(path.read_text(encoding="utf-8"))
        if batch_id in bank.get("applied_depth_batches", []):
            skipped += 1
            continue
        assert bank.get("editorial_depth") == "initial_subject_map", "Review before replacing an existing detailed bank"
        original = json.loads(json.dumps(bank))
        # Retain old IDs in the archive; allocate new IDs for the new questions.
        next_number = max(int(t["id"].rsplit("-", 1)[1]) for c in bank["categories"] for t in c["topics"])
        for pos, category in enumerate(categories, 1):
            category["id"] = f"CATALOG-{nid}-D{pos:02d}"
            category["prerequisites"] = [] if pos == 1 else [f"CATALOG-{nid}-D01"]
            for topic in category["topics"]:
                next_number += 1
                topic.update({"id": f"BANK-{nid}-{next_number:03d}", "angle": None,
                              "status": "proposed", "verified_sources": []})
        count = sum(len(c["topics"]) for c in categories)
        bank.update({"schema_version": "1.2", "bank_type": "detailed_expansion",
                     "editorial_depth": "detailed_authored_draft", "updated": DATE,
                     "categories": categories, "counts": {"categories": len(categories), "proposed_topics": count},
                     "research_profiles": {p: {k:v for k,v in PROFILES[p].items() if k in ("requirements", "source_leads")} for p in {c["research_profile"] for c in categories}},
                     "prior_initial_map": original, "applied_depth_batches": [batch_id],
                     "purpose": f'Individually authored episode questions and coverage boundaries for {bank["name"]}. The subject progression is organized by concrete content rather than a topic-by-angle multiplication.',
                     "coverage_limits": "This is an expanded topic-bank draft, not exhaustive scholarship or a researched episode package. Each question has an individually written boundary. Source access, claim verification, current angle-scope review and publication approval remain pending. Add new branches and cases when they fill a real gap; no numeric topic cap applies.",
                     "depth_review": {"status": "authored_draft_prepared", "basis": "Individually authored questions and scopes; category organization, wording, case specificity and exclusions reviewed during drafting.",
                                      "source_verification": "not_performed", "independent_peer_review": "not_performed",
                                      "structural_review": "run separately; does not certify editorial completeness", "overall_all_niche_request": "still_in_progress"}})
        if args.write:
            path.write_text(json.dumps(bank, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        total += count
        changed += 1
    print(f'{changed} detailed drafts {"written" if args.write else "previewed"}; {total} individually authored active proposals; {skipped} existing batch applications preserved')


if __name__ == "__main__":
    main()
