"""Apply the reviewed 2026-10-18 first batch; --write is required.

The batch data is a migration record. Active ANGLE_PLAN.json files remain the
editable source after registration. Never rerun this to overwrite edited plans.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import shutil
import sys
from collections import Counter

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from populate_niches import slugify, parse_visual_style

REG = ROOT / "REGISTRY"
REVIEW = ROOT / "AUDIT/CANDIDATE_REVIEW_2026_10_18"
DATE = "2026-10-18"
BASE = [("history_origins", "History & Origins"), ("famous_examples", "Famous Examples"),
        ("hidden_stories", "Hidden Stories"), ("beginner_explainers", "Beginner Explainers"),
        ("advanced_concepts", "Advanced Concepts"), ("mysteries_unsolved_cases", "Mysteries & Unsolved Cases"),
        ("technology_innovation", "Technology & Innovation"), ("people_personalities", "People & Personalities"),
        ("major_events", "Major Events"), ("how_it_works", "How It Works"), ("rise_fall", "Rise & Fall"),
        ("then_vs_now", "Then vs Now"), ("future_developments", "Future Developments"),
        ("myths_vs_facts", "Myths vs Facts"), ("documentary_stories", "Documentary Stories")]

SOURCES = {
    "agents": ("Anthropic: Building effective agents", "https://www.anthropic.com/engineering/building-effective-agents", "Versioned architectural discussion; historical article with update notice, not a current tool guarantee."),
    "llm": ("Hugging Face Transformers documentation", "https://huggingface.co/docs/transformers/index", "Versioned technical documentation; choose model cards and experiments for episode claims."),
    "lowcode": ("Microsoft Power Apps overview", "https://learn.microsoft.com/en-us/power-apps/powerapps-overview", "Vendor technical entry point, not independent proof of business benefit."),
    "saas": ("Stripe subscription documentation", "https://docs.stripe.com/billing/subscriptions/overview", "Operational vendor reference; financial/business claims need dated case records."),
    "creator": ("UNESCO Diversity of Cultural Expressions", "https://www.unesco.org/creativity/en", "Institutional creative-sector entry point; no creator-income claim is verified here."),
    "seo": ("Google Search Central SEO starter guide", "https://developers.google.com/search/docs/fundamentals/seo-starter-guide", "Provider documentation, not a ranking or traffic guarantee."),
    "mental": ("WHO mental health", "https://www.who.int/health-topics/mental-health", "Institutional evidence entry point, not personal diagnosis or treatment advice."),
    "sleep": ("NHLBI How Sleep Works", "https://www.nhlbi.nih.gov/health/sleep", "Institutional framework; obtain the original study for each episode question."),
    "exercise": ("WHO Physical activity", "https://www.who.int/news-room/fact-sheets/detail/physical-activity", "Dated institutional guidance; not a personal training prescription."),
    "ramayana": ("IGNCA research and archive entry point", "https://ignca.gov.in/", "Institutional homepage/archive entry only; a specific primary edition and passage have not been inspected."),
    "mahabharata": ("Bhandarkar Oriental Research Institute", "https://bori.ac.in/", "Institutional homepage/catalogue entry only; select and inspect exact edition/apparatus in Phase 1."),
    "festivals": ("IGNCA cultural archives", "https://ignca.gov.in/", "Institutional archive entry only; local observance and calendar records remain episode research."),
    "bhakti": ("IGNCA textual and performance archives", "https://ignca.gov.in/", "Institutional archive entry only; exact composition, attribution and recording remain unverified."),
    "egypt": ("Metropolitan Museum Egyptian Art", "https://www.metmuseum.org/departments/egyptian-art", "Institutional collection entry point; individual object provenance and interpretation need verification."),
    "mesopotamia": ("Cuneiform Digital Library Initiative", "https://cdli.earth/", "Primary object-catalogue entry; inspect item, transliteration, restoration and translation before scripting."),
    "cricket": ("ICC playing conditions", "https://www.icc-cricket.com/about/cricket/rules-and-regulations/playing-conditions", "Official conditions index; choose applicable format, season and competition document."),
    "football": ("IFAB Laws of the Game", "https://theifab.com/", "Official edition selector; choose applicable law edition and competition provisions."),
    "design": ("Cooper Hewitt Smithsonian Design Museum", "https://www.cooperhewitt.org/", "Institutional homepage/design-resource entry only; object records and rights still require inspection."),
    "editing": ("Blackmagic Design training", "https://www.blackmagicdesign.com/products/davinciresolve/training", "Vendor workflow entry point; pin actual software version and verify with project evidence."),
    "music": ("EBU R128 publication", "https://tech.ebu.ch/publications/r128", "Original technical standard entry; distinguish its delivery context from other chosen targets.")}


def build_plan(r, curated, titles):
    title, case = r["title"], r["case"]
    common = f"Evidence: {r['evidence']}. Choose a named source, version, period and case before scripting."
    questions = [
        f"Which documented problem led to the development of {case}?",
        f"What does a widely cited example of {case} establish and leave uncertain?",
        f"Whose contribution or experience is missing from the usual account of {case}?",
        f"Which definitions and boundaries are needed to understand {case}?",
        f"Which methodological assumption changes how {case} should be interpreted?",
        f"What specific evidence gap remains unresolved for {case}?",
        f"What changed after a documented technical or material innovation affected {case}?",
        f"How did credited people and institutions shape {case}?",
        f"What changed around a dated turning point involving {case}?",
        f"How do the documented components or stages of {case} connect?",
        f"Which evidence explains increasing or declining use or reception of {case}?",
        f"Are earlier and later accounts of {case} comparable on the same terms?",
        f"Which conditions would need to hold for a proposed future change involving {case}?",
        f"Does the original evidence support a commonly repeated claim about {case}?",
        f"How can a source-led documentary explain {case} without overstating its evidence?"]
    tasks = [
        "Trace dated origin records and distinguish contemporary aims from retrospective explanation.",
        "Examine a named example against its stated aims, evidence and representativeness.",
        f"Investigate documented labor, access and omitted perspectives among {r['people']} without inventing testimony.",
        "Define essential terms, units or textual conventions using one bounded example, not an entire field survey.",
        "Test one difficult assumption, comparison or interpretive choice against an explicit alternative.",
        "Map missing, conflicting or inaccessible evidence and state what could resolve the uncertainty.",
        "Compare the documented change and its limitations; separate a proposed benefit from an observed result.",
        "Attribute decisions and contributions using primary records and avoid heroic or blame-centered simplification.",
        "Reconstruct chronology from records available at each date; sequence alone does not establish cause.",
        "Follow a defined process or argument with traceable inputs, decisions and outputs; avoid unsupported reconstruction.",
        "Define the adoption or reception measure and examine multiple documented explanations for change.",
        "Match periods, definitions, versions and source survival before comparing change over time.",
        "Separate observed evidence, conditional scenarios and unknowns; do not present a forecast as a fact.",
        "Locate the original claim and compare its scope with the evidence, including legitimate interpretive disagreement.",
        "Build a bounded story with attributed sources, clear illustration labels and explicit remaining uncertainty."]
    entries = []
    for (slug, label), question, task in zip(BASE, questions, tasks):
        entries.append({"slug": slug, "angle": f"{title}: {label}", "question": question,
                        "scope": f"For {case}, {task[0].lower()+task[1:]}",
                        "evidence": common + " " + task, "boundary": r["boundary"] + " Niche boundary: " + r["purpose"]})
    for label, question, scope in curated:
        entries.append({"slug": "field_" + slugify(label), "angle": label, "question": question,
                        "scope": scope, "evidence": common + " " + scope,
                        "boundary": r["boundary"] + " Niche boundary: " + r["purpose"]})
    for field in ("slug", "angle", "question", "scope"):
        assert len({a[field] for a in entries}) == len(entries), (r["id"], field)
    source_title, url, role = SOURCES[r["source_key"]]
    return {"niche_id": r["id"], "status": "editorial_question_reviewed", "purpose": r["purpose"],
            "generation_basis": "Reviewed first batch from the external 100-proposal comparison; original stable 15 plus niche-specific lenses.",
            "editorial_principles": [r["boundary"], "Question-design review is not episode fact verification or publication approval."],
            "scope_review": {"date": DATE, "status": "scope_wording_revised", "basis": "Each angle defines a separate research task and evidential limit."},
            "research_sources": [{"title": source_title, "url": url, "checked_date": DATE, "role": role}],
            "related_niches": [{"niche_id": n, "title": titles[n]} for n in r["related"]],
            "editorial_review": {"date": DATE, "angles": len(entries), "checks": ["neighboring niche boundary", "distinct question and scope", "evidence task", "source entry accessibility", "episode-level limits"],
                                 "source_feasibility": role + " No episode claim was verified by registering this niche."},
            "angles": entries}


def main(write=False):
    records = json.loads((REVIEW / "BATCH_531_550.json").read_text(encoding="utf-8"))
    parsed, current = {}, None
    for line in (REVIEW / "CURATED_ANGLES.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("@@"):
            current = line[2:]; parsed[current] = []
        elif line.strip():
            cells = line.split("|"); assert len(cells) == 3
            parsed[current].append(cells)
    with (REG / "NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream); columns = reader.fieldnames; old = list(reader)
    if [int(r["id"]) for r in old] != list(range(1, 531)):
        raise ValueError("Apply once to exactly the preserved 001-530 registry; do not overwrite an expanded registry")
    if any(r["category"] not in {row["primary_category"] for row in old} for r in records):
        raise ValueError("No new category is authorized in this batch")
    titles = {r["id"]: r["title"] for r in old}
    styles = parse_visual_style()
    additions, plans = [], []
    for r in records:
        slug = slugify(r["title"]); home = f"REGISTRY/Niches/{r['id']}_{slug}"
        if slug in {row["slug"] for row in old} or (ROOT / home).exists():
            raise ValueError("Duplicate or existing niche home: " + home)
        additions.append(dict(id=r["id"], title=r["title"], current_path=home+"/Angles", primary_category=r["category"], secondary_categories="", legacy_secondary_categories="", slug=slug, review_status="reviewed_expansion_2026_10_18", niche_path=home))
        plans.append(build_plan(r, parsed[r["id"]], titles))
    if not write:
        print(f"Preview: {len(additions)} niches; {sum(len(p['angles']) for p in plans)} angles; 46 categories unchanged")
        return
    backup = REVIEW / "BEFORE_EXPANSION"; backup.mkdir(exist_ok=True)
    targets = [REG / "NICHE_TAXONOMY.csv", REG / "MASTER_REGISTRY_EXTENSION.md", REG / "MASTER_VISUAL_STYLE_EXTENSION.md", REG / "CATEGORY_INDEX.md", REG / "Niches/README.md", REG / "NICHE_MASTER_LIST.md"]
    for path in targets:
        dest = backup / path.name
        if dest.exists(): raise FileExistsError("Do not overwrite backup " + str(dest))
        shutil.copyfile(path, dest)
    fingerprints = {}
    for row in old:
        home = ROOT / row["niche_path"]
        for path in [home / "ANGLE_PLAN.json", home / f"CAT_{row['id']}_{row['slug']}.md"]:
            fingerprints[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    (backup / "ORIGINAL_CAT_PLAN_HASHES.json").write_text(json.dumps(fingerprints, indent=2)+"\n", encoding="utf-8")
    with (REG / "NICHE_TAXONOMY.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns); writer.writeheader(); writer.writerows(old+additions)
    master = (REG / "MASTER_REGISTRY_EXTENSION.md").read_text(encoding="utf-8").rstrip()+"\n\n"
    visual = (REG / "MASTER_VISUAL_STYLE_EXTENSION.md").read_text(encoding="utf-8").rstrip()+"\n"
    names = ("primary_visual_style", "visual_language", "palette", "lighting", "camera", "motion", "thumbnail_direction", "ai_keywords", "avoid")
    for r, row, plan in zip(records, additions, plans):
        master += f"## {int(r['id'])}. {r['title']}\n\n" + "\n".join(f"{i}. {r['title']} — {label}" for i, (_, label) in enumerate(BASE, 1)) + "\n\n"
        exemplar = next(o for o in old if o["primary_category"] == r["category"])
        style = styles[int(exemplar["id"])]
        visual += "| " + " | ".join([r["id"], r["title"]] + [style[n] for n in names]) + " |\n"
        home = ROOT / row["niche_path"]; home.mkdir(parents=True)
        (home / "ANGLE_PLAN.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    master = master.replace("extension: IDs 501-530", "extension: IDs 501-550", 1)
    visual = visual.replace("extension: IDs 501-530", "extension: IDs 501-550", 1)
    (REG / "MASTER_REGISTRY_EXTENSION.md").write_text(master, encoding="utf-8")
    (REG / "MASTER_VISUAL_STYLE_EXTENSION.md").write_text(visual, encoding="utf-8")
    all_rows = old+additions; counts = Counter(r["primary_category"] for r in all_rows)
    index = ["# Subject category index", "", f"The {len(counts)} subjects group {len(all_rows)} independent niche homes.", "", "See the [complete niche master list](NICHE_MASTER_LIST.md) for IDs, scopes and file routes.", "", "| Subject | Niches | Browse |", "|---|---:|---|"]
    homes = ["# Niche homes", "", "Each stable ID has one CAT, NICHE, editable angle plan and generated angle choices. See the [master list](../NICHE_MASTER_LIST.md).", ""]
    for category in sorted(counts):
        index.append(f"| {category.replace('_', ' ')} | {counts[category]} | [Niches](Niches/README.md#{category.lower().replace('_', '-')}) |")
        homes += ["## " + category.replace('_', ' '), ""]
        for row in all_rows:
            if row["primary_category"] == category:
                stem = f"{row['id']}_{row['slug']}"
                homes.append(f"- [{row['id']} {row['title']}](./{stem}/NICHE_{stem}.md) · [CAT](./{stem}/CAT_{stem}.md) · [Angles](./{stem}/Angles/ALL_TOPICS_BY_NICHE.md) · [Plan](./{stem}/ANGLE_PLAN.json)")
        homes.append("")
    (REG / "CATEGORY_INDEX.md").write_text("\n".join(index)+"\n", encoding="utf-8")
    (REG / "Niches/README.md").write_text("\n".join(homes)+"\n", encoding="utf-8")
    print(f"Registered {len(additions)} bounded niches, {sum(len(p['angles']) for p in plans)} angles; original CAT/plan fingerprints saved")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true")
    main(parser.parse_args().write)
