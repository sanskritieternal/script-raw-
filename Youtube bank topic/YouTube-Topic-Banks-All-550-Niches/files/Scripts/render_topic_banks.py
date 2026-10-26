"""Validate and render editorial topic banks; these are not executable depth plans.

Run from the repository root:
    python Scripts/render_topic_banks.py --check
    python Scripts/render_topic_banks.py --write
Only IN_DEPTH_TOPIC_BANK.md views are generated. JSON remains the editable source.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEVELS = {"foundation", "intermediate", "advanced"}


def validate(bank, directory):
    nid = bank["niche_id"]
    assert directory.name == f'{nid}_{bank["slug"]}', "Niche/path mismatch"
    assert bank["status"] == "proposed", "Banks describe proposed editorial coverage"
    angle_path = ROOT / "REGISTRY" / "Niches" / directory.name / "ANGLE_PLAN.json"
    assigned = [t for c in bank["categories"] for t in c["topics"] if t.get("angle")]
    angles = set()
    if assigned:
        assert angle_path.exists(), f"Missing angle plan for assigned angles: {nid}"
        angles = {a["slug"] for a in json.loads(angle_path.read_text(encoding="utf-8"))["angles"]}
    category_ids = [c["id"] for c in bank["categories"]]
    assert len(category_ids) == len(set(category_ids)), "Duplicate category IDs"
    categories = {c["id"]: c for c in bank["categories"]}
    topic_ids, titles = set(), set()
    for c in bank["categories"]:
        assert c["level"] in LEVELS
        assert c["research_profile"] in bank["research_profiles"]
        assert all(x in categories and x != c["id"] for x in c["prerequisites"])
        assert c["topics"], "Empty category"
        for t in c["topics"]:
            assert t["id"].startswith(f"BANK-{nid}-")
            assert t["id"] not in topic_ids, "Duplicate topic ID"
            assert t["question"].casefold() not in titles, "Duplicate question"
            assert t["question"].endswith("?") and t["coverage"].strip()
            assert t["angle"] is None or t["angle"] in angles, f'Unregistered angle: {t["angle"]}'
            if bank.get("bank_type") == "subject_map":
                assert t["title"].strip() and len(t["research_outline"]) >= 3
                assert t["angle"] is None, "Initial maps must not imply an angle-scope review"
            assert t["status"] == "proposed" and t["verified_sources"] == []
            topic_ids.add(t["id"])
            titles.add(t["question"].casefold())
    def visit(cid, active, done):
        assert cid not in active, "Cyclic category prerequisites"
        if cid in done:
            return
        for parent in categories[cid]["prerequisites"]:
            visit(parent, active | {cid}, done)
        done.add(cid)
    done = set()
    for cid in categories:
        visit(cid, set(), done)
    for series in bank["suggested_series"]:
        assert series["topic_ids"] and len(series["topic_ids"]) == len(set(series["topic_ids"]))
        assert set(series["topic_ids"]) <= topic_ids
        assert series["learning_outcome"].strip()
    assert bank["counts"] == {"categories": len(categories), "proposed_topics": len(topic_ids)}


def render(bank):
    if bank.get("bank_type") == "detailed_expansion":
        return render_authored_bank(bank)
    if bank.get("bank_type") == "subject_map":
        return render_subject_map(bank)
    nid = bank["niche_id"]
    title = bank["name"]
    lines = [f"# {nid} {title}: In-Depth YouTube Topic Bank", "",
             f'Updated: {bank["updated"]} · Status: **Proposed editorial coverage**', "",
             f'**{bank["counts"]["categories"]} categories · {bank["counts"]["proposed_topics"]} specific episode questions.**', "",
             bank["purpose"], "", "## How to use this bank", "",
             "Choose a category, then a bounded question. The coverage column supplies the intended subtopics and exclusions. Select a named text edition, teaching institution, community, study, or product before research. A question is a proposal, not a claim that its premise or outcome has been established.", "",
             "Foundation, intermediate, and advanced indicate learning depth rather than physical difficulty. Advanced entries are documentary research subjects, not instructions to attempt advanced practices.", "",
             "The existing 20-item production queue and seven legacy trend candidates remain separate. The bank does not certify trends, evidence, production completion, or publication readiness. It is not an IDEA_BANK.json or DEPTH_PLAN.json and cannot be passed to the project creator. Promote selected entries deliberately through the existing registry planning/idea workflow.", "",
             "[Existing roadmap](./" + bank["roadmap"] + ") · [Production report](./TOPICS_COVERED_REPORT.md) · [Editable bank](./IN_DEPTH_TOPIC_BANK.json) · [Batch guide and source leads](../DEPTH_EXPANSION.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)", "",
             "## Scope and neighboring niches", "", "| Primary home | Coverage rule |", "|---|---|"]
    for route in bank["scope_routing"]:
        lines.append(f'| [{route["name"]}](../{route["directory"]}/{route["roadmap"]}) | {route["boundary"]} |')
    lines += ["", "## Category map", "", "| Category | Learning level | Prerequisites | Episode proposals |", "|---|---|---|---:|"]
    names = {c["id"]: c["title"] for c in bank["categories"]}
    for c in bank["categories"]:
        pre = "; ".join(names[x] for x in c["prerequisites"]) or "None"
        lines.append(f'| {c["id"]}: {c["title"]} | {c["level"]} | {pre} | {len(c["topics"])} |')
    lines += ["", "## Detailed subject categories and video questions", ""]
    for number, c in enumerate(bank["categories"], 1):
        profile = bank["research_profiles"][c["research_profile"]]
        lines += [f'### {number:02d}. {c["title"]}', "",
                  f'**Level:** {c["level"]}. **Research direction:** {profile["requirements"]}', "",
                  f'**Source leads:** {"; ".join(profile["source_leads"])}. Leads require topic-specific inspection; no entry has verified episode sources yet.', "",
                  "| ID | Specific YouTube episode question | Detailed subtopics and coverage boundary | Suggested registered angle |",
                  "|---|---|---|---|"]
        for t in c["topics"]:
            lines.append(f'| {t["id"]} | {t["question"]} | {t["coverage"]} | `{t["angle"]}` |')
        lines.append("")
    lines += ["## Suggested learning series", "",
              "These are editorial sequences of bank proposals. They are not registered SER records, ready ideas, or scheduled episodes.", ""]
    topics = {t["id"]: t for c in bank["categories"] for t in c["topics"]}
    for series in bank["suggested_series"]:
        lines += [f'### {series["title"]}', "", f'**Learning outcome:** {series["learning_outcome"]}', "",
                  f'**Ordering reason:** {series["ordering_reason"]}', ""]
        for tid in series["topic_ids"]:
            lines.append(f'1. **{tid}** — {topics[tid]["question"]}')
        lines.append("")
    lines += ["## Research and production handoff", ""]
    for item in bank["handoff"]:
        lines.append(f"- {item}")
    lines += ["", "## Coverage limits and next expansion", "", bank["coverage_limits"], "",
              "IDs remain stable when wording changes. Add new IDs for new questions. Avoid copying an existing question to another niche; link to its primary home and define the new episode's distinct question. Counts describe catalog entries, not a claim of exhaustive subject coverage.", ""]
    return "\n".join(lines)


def render_authored_bank(bank):
    lines = [f'# {bank["niche_id"]} {bank["name"]}: Detailed Topic-Bank Draft', "",
             f'**{bank["counts"]["categories"]} categories · {bank["counts"]["proposed_topics"]} individually authored episode proposals.**', "",
             bank["purpose"], "",
             '[All-niche progress](../DEPTH_COMPLETION_STATUS.md) · [All-niche index](../ALL_NICHE_TOPIC_BANKS.md) · [Editable bank](./IN_DEPTH_TOPIC_BANK.json)', "",
             "Every question below has its own coverage boundary. All remain proposed; sources and current niche angle scopes have not been verified. Learning levels organize documentary research rather than physical difficulty. The older initial proposals remain in the JSON's prior_initial_map archive and are not counted again.", ""]
    for i, c in enumerate(bank["categories"], 1):
        profile = bank["research_profiles"][c["research_profile"]]
        lines += [f'## {i:02d}. {c["title"]}', "", f'**Level:** {c["level"]}. **Evidence direction:** {profile["requirements"]}', "",
                  '**Source types to locate:** ' + '; '.join(profile['source_leads']) + '. These are requirements, not sources already inspected.', "",
                  '| ID | Specific episode question | Individually written scope and exclusions |', '|---|---|---|']
        for t in c["topics"]:
            lines.append(f'| {t["id"]} | {t["question"]} | {t["coverage"]} |')
        lines.append("")
    lines += ['## Coverage limits and next step', '', bank['coverage_limits'], '',
              'Select an exact case, edition, population, jurisdiction or product version, inspect sources and refine the question before using the existing registry idea/depth planning workflow. These BANK IDs are catalog identities, not approved IDEA IDs. Existing Q1-Q42 defaults, production queues and approval gates are unchanged.', '',
              '## Related niche homes', '']
    for n in bank.get('neighboring_niches', []):
        lines.append(f'- [{n["id"]} {n["title"]}](../{n["directory"]}/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.')
    lines.append('')
    return '\n'.join(lines)


def render_subject_map(bank):
    lines = [f'# {bank["niche_id"]} {bank["name"]}: Subject Coverage and Episode Proposals', "",
             f'Updated: {bank["updated"]} · **Initial subject map; proposed, not researched**', "",
             f'**{bank["counts"]["categories"]} subject categories · {bank["counts"]["proposed_topics"]} topic proposals.**', "",
             bank["purpose"], "",
             '[All-niche index](../ALL_NICHE_TOPIC_BANKS.md) · [Editable JSON](./IN_DEPTH_TOPIC_BANK.json) · [Expansion method](../ALL_NICHE_EXPANSION_GUIDE.md)', "",
             "This is a first coverage pass with concrete subject headings and research briefs. It has less editorial depth than the 120-question Meditation, Pranayama and Yoga pilots. It is not exhaustive, and has no fixed topic limit. The suggested research questions and outlines use domain-specific editorial patterns; they are proposals to refine against actual sources, not evidence that the research has been done.", "",
             "The IDs refer to catalog entries, not episodes produced. Angles are deliberately unassigned until the actual niche angle scope and selected case are reviewed. No topic is ready_for_project or verified. The research outline is not a follow-along lesson, treatment plan, legal instruction, investment recommendation or hazardous procedure.", "",
             "## Subject map", "", "| Category | Research mode | Topic proposals |", "|---|---|---:|"]
    for c in bank["categories"]:
        lines.append(f'| {c["id"]}: {c["title"]} | {c["research_profile"]} | {len(c["topics"])} |')
    lines += ["", "## Detailed proposals", ""]
    for c in bank["categories"]:
        profile = bank["research_profiles"][c["research_profile"]]
        lines += [f'### {c["title"]}', "", f'**Research standard:** {profile["requirements"]}', "",
                  f'**Source types to locate:** {"; ".join(profile["source_leads"])}. These source types are not topic-specific sources already inspected.', ""]
        for t in c["topics"]:
            lines += [f'#### {t["id"]} — {t["title"]}', "", f'**Video question:** {t["question"]}', "",
                      f'**Coverage boundary:** {t["coverage"]}', "", "**Deep-dive research outline:**", ""]
            lines += [f"- {x}" for x in t["research_outline"]]
            lines += ["", f'**Next action:** {t["next_action"]}', ""]
    lines += ["## Relationship to neighboring niches", "", bank["overlap_policy"], ""]
    for n in bank["neighboring_niches"]:
        lines.append(f'- [{n["id"]} {n["title"]}](../{n["directory"]}/IN_DEPTH_TOPIC_BANK.md) — {n["reason"]}')
    lines += ["", "## Production handoff", ""]
    lines += [f"- {x}" for x in bank["handoff"]]
    lines += ["", "## Open coverage", "", bank["coverage_limits"], ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    parser.add_argument("--require-all-niches", action="store_true", help="Check bank identities against the taxonomy")
    args = parser.parse_args()
    paths = sorted((ROOT / "topics").glob("*/IN_DEPTH_TOPIC_BANK.json"))
    if not paths:
        raise SystemExit("No topic banks found")
    if args.require_all_niches:
        import csv
        expected = {r["id"] for r in csv.DictReader((ROOT / "REGISTRY/NICHE_TAXONOMY.csv").open(encoding="utf-8"))}
        actual = [json.loads(p.read_text(encoding="utf-8"))["niche_id"] for p in paths]
        assert len(actual) == len(set(actual)), "Duplicate niche banks"
        assert set(actual) == expected, f"Bank/taxonomy mismatch: {expected.symmetric_difference(actual)}"
    total = 0
    for path in paths:
        bank = json.loads(path.read_text(encoding="utf-8"))
        validate(bank, path.parent)
        rendered = render(bank)
        target = path.with_suffix(".md")
        if args.write:
            target.write_text(rendered, encoding="utf-8")
        elif not target.exists() or target.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"Stale generated view: {target.relative_to(ROOT)}")
        total += bank["counts"]["proposed_topics"]
        print(f'{bank["niche_id"]}: {bank["counts"]["categories"]} categories, {bank["counts"]["proposed_topics"]} proposed topics; valid')
    print(f"{len(paths)} banks; {total} proposals; views {'written' if args.write else 'current'}")


if __name__ == "__main__":
    main()
