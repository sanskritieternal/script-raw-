"""Build the all-niche browsing index and honest editorial progress summary."""
import csv
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
DATE = datetime.now(ZoneInfo("Asia/Calcutta")).date().isoformat()


def refresh_priority(records):
    """Keep the focus tracker derived from records, with no count threshold."""
    path = ROOT/'topics/FIRST_TEN_EXPANSION_STATUS.json'
    if not path.exists():
        return None
    focus = json.loads(path.read_text())
    rows = {r['niche_id']:r for r in records}
    batches = {}
    for nid in focus['niche_priority']:
        row = rows[nid]
        bank = json.loads((ROOT/'topics'/row['directory']/'IN_DEPTH_TOPIC_BANK.json').read_text())
        count = focus['counts'][nid]
        count['current_proposals'] = row['proposed_topics']
        count['new_proposals'] = row['proposed_topics'] - count['previous_proposals']
        count['categories'] = row['categories']
        for name in bank.get('applied_extension_batches', []):
            batches.setdefault(name, []).append(nid)
    focus['current_proposals'] = sum(focus['counts'][n]['current_proposals'] for n in focus['niche_priority'])
    focus['added_proposals'] = focus['current_proposals'] - focus['previous_proposals']
    focus['updated'] = DATE
    focus['applied_extension_batches'] = sorted(batches)
    focus['latest_extension'] = max(batches) if batches else None
    focus['latest_extension_niche_ids'] = batches.get(focus['latest_extension'], [])
    focus['branch_review_note'] = 'Listed branches remain open. Applied extensions add specific coverage but do not certify that any broad branch is exhausted.'
    path.write_text(json.dumps(focus, ensure_ascii=False, indent=2)+'\n')
    return focus


def main():
    taxonomy = list(csv.DictReader((ROOT/"REGISTRY/NICHE_TAXONOMY.csv").open(encoding="utf-8")))
    records = []
    for row in taxonomy:
        directory = f'{row["id"]}_{row["slug"]}'
        path = ROOT/"topics"/directory/"IN_DEPTH_TOPIC_BANK.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        records.append({"niche_id": row["id"], "name": row["title"],
                        "category": row["primary_category"], "directory": directory,
                        "editorial_depth": data.get("editorial_depth", "detailed_pilot"),
                        "depth_batch": data.get("applied_depth_batches", [None])[-1],
                        "categories": data["counts"]["categories"],
                        "proposed_topics": data["counts"]["proposed_topics"],
                        "verified_episode_sources": sum(len(t["verified_sources"]) for c in data["categories"] for t in c["topics"]),
                        "publication_status": "not_assessed"})
    focus = refresh_priority(records)
    depth = Counter(r["editorial_depth"] for r in records)
    totals = {"niches_with_banks": len(records), "subject_categories": sum(r["categories"] for r in records),
              "proposed_topics": sum(r["proposed_topics"] for r in records),
              "detailed_pilot_banks": depth["detailed_pilot"], "initial_subject_map_banks": depth["initial_subject_map"],
              "detailed_authored_draft_banks": depth["detailed_authored_draft"],
              "detailed_banks_prepared": depth["detailed_pilot"] + depth["detailed_authored_draft"],
              "pending_depth_expansion": depth["initial_subject_map"],
              "individually_authored_batch_topics": sum(r["proposed_topics"] for r in records if r["editorial_depth"] == "detailed_authored_draft"),
              "initial_map_topics": sum(r["proposed_topics"] for r in records if r["editorial_depth"] == "initial_subject_map"),
              "verified_episode_sources": sum(r["verified_episode_sources"] for r in records)}
    progress = {"updated": DATE, "base_repository_commit": "751dc234534e9eea18fe022b831ed0da5630fe53",
                "coverage_status": "all_niches_have_proposed_subject_coverage_not_exhaustive",
                "remote_delivery_status": "not_written_connection_previously_returned_403",
                "topic_limit": None, "totals": totals, "niches": records,
                "limitations": ["Initial subject maps are shallower than the three detailed pilots.",
                                "Initial-map questions and outlines use editorial patterns; detailed authored drafts have individual coverage boundaries. Neither implies per-episode research.",
                                "No remaining-niche angle plan has been assigned or certified.",
                                "Structural validation does not assess truth, exhaustive coverage or all semantic overlap."]}
    (ROOT/"topics/TOPIC_BANK_PROGRESS.json").write_text(json.dumps(progress, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    lines = ["# All-niche YouTube subject and topic banks", "",
             f'**{totals["niches_with_banks"]} niches · {totals["subject_categories"]:,} subject categories · {totals["proposed_topics"]:,} topic proposals.**', "",
             f"Updated: {DATE}. [Expansion method and limitations](./ALL_NICHE_EXPANSION_GUIDE.md) · [Machine-readable progress](./TOPIC_BANK_PROGRESS.json)", "",
             f'Three banks are detailed 120-question pilots; {depth["detailed_authored_draft"]} more have individually authored detailed drafts. {depth["initial_subject_map"]} remain initial maps pending depth expansion. [Exact remaining-work tracker](./DEPTH_COMPLETION_STATUS.md). All are proposed editorial coverage, not verified scripts or completed videos. There is no topic cap and no claim that any field is exhausted.', "",
             "## By niche ID", "", "| ID | Niche | Taxonomy category | Subject categories | Proposed topics | Editorial depth |",
             "|---|---|---|---:|---:|---|"]
    if focus:
        lines[8:8] = [f'**Current priority:** expand niches 001–010 substantively before continuing the other niches. Their {focus["current_proposals"]:,} proposals are an open checkpoint, not a completion threshold. [Priority tracker](./FIRST_TEN_EXPANSION_STATUS.json)', '']
    for r in records:
        depth_label = {"detailed_pilot": "Detailed pilot", "detailed_authored_draft": "Authored detailed draft", "initial_subject_map": "Initial map — depth pending"}[r["editorial_depth"]]
        lines.append(f'| {r["niche_id"]} | [{r["name"]}](./{r["directory"]}/IN_DEPTH_TOPIC_BANK.md) | {r["category"]} | {r["categories"]} | {r["proposed_topics"]} | {depth_label} |')
    lines += ["", "## Taxonomy category totals", "", "| Taxonomy category | Niches | Proposed topics |", "|---|---:|---:|"]
    for category in sorted({r["category"] for r in records}):
        rr = [r for r in records if r["category"] == category]
        lines.append(f'| {category} | {len(rr)} | {sum(r["proposed_topics"] for r in rr)} |')
    lines += ["", "Counts refer to topic-bank proposals only. They exclude the pre-existing production queues and legacy trend candidates; those may overlap these proposals. No completion or publication status is inferred.", ""]
    (ROOT/"topics/ALL_NICHE_TOPIC_BANKS.md").write_text("\n".join(lines), encoding="utf-8")
    prepared = [r for r in records if r["editorial_depth"] != "initial_subject_map"]
    pending = [r for r in records if r["editorial_depth"] == "initial_subject_map"]
    batches = {r['depth_batch'] for r in records if r['depth_batch']}
    last_batch = max(batches, key=lambda s: int(s.rsplit('_', 1)[-1])) if batches else None
    last_rows = [r for r in records if r['depth_batch'] == last_batch] if last_batch else []
    latest_summary = (f'Latest batch {last_batch}: niches ' + ', '.join(r['niche_id'] for r in last_rows)
                      + f'; {sum(r["proposed_topics"] for r in last_rows)} individually authored questions in {sum(r["categories"] for r in last_rows)} subject categories. '
                      + f'{len(pending)} initial maps remain pending. Earlier starter records remain archived and excluded from active counts.')
    completion = {"updated": DATE, "overall_request": "pending" if pending else "topic_drafts_prepared",
                  "detailed_topic_drafts_prepared": len(prepared), "pending_depth_expansion": len(pending),
                  "all_niches_completed_in_depth": not pending,
                  "next_pending_niche_id": pending[0]["niche_id"] if pending else None,
                  "prepared_niche_ids": [r["niche_id"] for r in prepared],
                  "pending_niche_ids": [r["niche_id"] for r in pending],
                  "latest_authored_batch": last_batch,
                  "latest_batch_niche_ids": [r['niche_id'] for r in last_rows],
                  "distinction": "Detailed topic drafts are proposal catalogs; source verification, scripts and video production are not completed by this status."}
    if focus:
        completion['current_priority_niche_ids'] = focus['niche_priority']
        completion['current_priority_status'] = focus['status']
        completion['latest_extension'] = focus['latest_extension']
        completion['next_pending_niche_note'] = 'Lowest remaining initial map; not a direction to skip the open 001-010 priority expansion.'
    (ROOT/"topics/DEPTH_COMPLETION_STATUS.json").write_text(json.dumps(completion, indent=2)+"\n", encoding="utf-8")
    status_lines = ['# In-depth completion progress', '', '**Overall request: PENDING.**' if pending else '**All topic-bank drafts prepared; research and publication remain separate.**', '',
                    f'- Detailed topic drafts prepared: **{len(prepared)} / {len(records)}**.',
                    f'- Still pending in-depth expansion: **{len(pending)}**.',
                    f'- Next pending niche: **{completion["next_pending_niche_id"]}**.', '',
                    'Prepared means an organized topic-bank draft with specific questions and individual coverage boundaries. It does not mean exhaustive subject coverage, researched claims, ready project ideas, completed scripts or published videos. No fixed topic quota defines depth.', '',
                    '## Latest authored batch', '',
                    latest_summary, '',
                    '## Prepared banks', '', '| ID | Niche | Active proposed topics | Stage |', '|---|---|---:|---|']
    if focus:
        status_lines[2:2] = [f'**Current user priority:** further expansion of 001–010. Latest extension: {focus["latest_extension"]}; current first-ten proposals: {focus["current_proposals"]:,}. No numeric threshold defines completion. [Open branches](./FIRST_TEN_EXPANSION_STATUS.json).', '']
    for r in prepared:
        status_lines.append(f'| {r["niche_id"]} | [{r["name"]}](./{r["directory"]}/IN_DEPTH_TOPIC_BANK.md) | {r["proposed_topics"]} | {r["editorial_depth"]} |')
    status_lines += ['', '## Remaining queue', '', 'Continue from the lowest pending ID, preserving earlier IDs and avoiding subject-by-angle filler. Expand concrete branches, named cases, evidence questions and clear exclusions; inspect neighboring banks before duplicating a question.', '', ', '.join(r['niche_id'] for r in pending), '',
                     '[All-niche index](./ALL_NICHE_TOPIC_BANKS.md) · [Machine-readable status](./DEPTH_COMPLETION_STATUS.json)', '']
    (ROOT/"topics/DEPTH_COMPLETION_STATUS.md").write_text('\n'.join(status_lines), encoding='utf-8')
    summary = f'**Current depth progress:** [{len(prepared)} detailed topic drafts prepared; {len(pending)} pending](./DEPTH_COMPLETION_STATUS.md). Current active totals are in the generated index; earlier coverage totals below are historical.'
    p = ROOT/'topics/README.md'
    p.write_text(re.sub(r'^\*\*Current depth progress:\*\*.*$', summary, p.read_text(encoding='utf-8'), flags=re.M), encoding='utf-8')
    p = ROOT/'topics/ALL_NICHE_EXPANSION_GUIDE.md'
    text = p.read_text(encoding='utf-8')
    text = re.sub(r'^\*\*Current depth progress supersedes.*$', summary, text, flags=re.M)
    text = re.sub(r'^\*\*Current depth progress:\*\*.*$', summary, text, flags=re.M)
    p.write_text(text, encoding='utf-8')
    print(json.dumps(totals))


if __name__ == "__main__":
    main()
