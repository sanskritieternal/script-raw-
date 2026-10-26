"""Retire a duplicate Sabha Parva proposal while preserving its full record."""

import json
from pathlib import Path

path = Path(__file__).resolve().parents[4] / "topics/541_mahabharata/IN_DEPTH_TOPIC_BANK.json"
data = json.loads(path.read_text(encoding="utf-8"))
topic_id = "BANK-541-063"
owner = "BANK-004-074"
retired = data.setdefault("retired_duplicate_proposals", [])
if not any(t["id"] == topic_id for t in retired):
    for category in data["categories"]:
        for index, topic in enumerate(category["topics"]):
            if topic["id"] == topic_id:
                record = category["topics"].pop(index)
                retired.append({
                    **record,
                    "duplicate_of": owner,
                    "retirement_reason": "The active 004 question already asks how the dice-hall episode frames Draupadi's authority question, reading speakers and legal vocabulary within one edition. The 541 Sabha Parva 2.60–61 phrasing and source note specify the same scene and method; keep one owner and preserve this record inactive.",
                    "editorial_retirement_pass": "cross_bank_followup_2026_10_24",
                    "original_subcategory_id": category["id"],
                })
                break
        else:
            continue
        break
assert any(t["id"] == topic_id for t in retired)
data["counts"]["proposed_topics"] = sum(len(c["topics"]) for c in data["categories"])
for route in data["legacy_topic_crosswalk"].values():
    if topic_id in route.get("bank_ids", []):
        route["decision"] = "cross_niche_overlap"
        route["bank_ids"] = [owner]
        route["reason"] = "The preserved Sabha Parva/Draupadi pitch belongs to active BANK-004-074, which already asks the same dice-hall authority question within a named edition. BANK-541-063 is retained as a retired duplicate; no second episode is approved here."
data["research_followups"] = [x for x in data.get("research_followups", []) if x.get("topic_id") != topic_id]
data["semantic_overlap_review"] = {
    "date": "2026-10-24",
    "retired_id": topic_id,
    "owner_id": owner,
    "note_file": "SELECTED_SOURCE_NOTE.md",
    "finding": "The newly researched BORI Sabha Parva 2.60–61 question duplicates the earlier active BANK-004-074 dice-hall authority question. Preserve the 541 source research and retired ID, and route the case to 004 for any future production review.",
}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
