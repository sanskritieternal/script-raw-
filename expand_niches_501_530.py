"""Add thirty distinct niche homes while preserving IDs 001-500 and their sources."""

import csv
import json
from collections import Counter
from pathlib import Path

from populate_niches import slugify


ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "REGISTRY"
TAXONOMY = REGISTRY / "NICHE_TAXONOMY.csv"
MASTER_EXTENSION = REGISTRY / "MASTER_REGISTRY_EXTENSION.md"
VISUAL_EXTENSION = REGISTRY / "MASTER_VISUAL_STYLE_EXTENSION.md"

# ID | title | category | focus | bounded case | outcome measure | affected group |
# evidence | editorial boundary | five additional lenses
ROWS = """501|Public Health|Medicine_Healthcare|population health policy|a named local program|population outcomes|residents and health workers|public-health surveillance and program evaluations|Define place, population and date; educational questions do not provide personal care advice.|disease surveillance;vaccination systems;health communication;community prevention;equity in outcomes
502|Rehabilitation|Medicine_Healthcare|rehabilitation services|a documented care pathway|functional outcomes|patients and therapists|WHO rehabilitation guidance and service data|Name condition, setting and outcome; do not promise individual recovery.|assessment and goals;therapy access;assistive devices;continuity of care;patient-defined function
503|Assistive Technology|Medicine_Healthcare|assistive products and services|a specific device in use|user-defined participation|disabled users and caregivers|WHO assistive-technology reports and user studies|Center user choice and access; a prototype is not a proven benefit for everyone.|fitting and training;repair and support;affordability;accessible design;device abandonment
504|Maternal & Child Health|Medicine_Healthcare|maternal and child health systems|a regional service pathway|health and access outcomes|pregnant people, children and carers|WHO and national health-service data|Specify population and jurisdiction; no individualized medical instruction.|prenatal access;birth safety;newborn care;child development services;care inequity
505|Nutrition Science|Medicine_Healthcare|nutrition evidence|a defined food or dietary pattern|measured health outcome|people in a defined study group|dietary trials, cohort methods and official guidance|Separate association from causation and food claims from medical advice.|diet measurement;nutrient adequacy;food environment;trial versus cohort;claims and labels
506|Housing & Tenancy|Home_Living|housing access and tenancy|a city's rental market|affordability and security|tenants and households|UN-Habitat housing reports and local records|Name jurisdiction and period; tenancy rights vary by place.|rents and income;tenure security;housing quality;eviction pathways;accessible homes
507|Water & Sanitation|Engineering_Inventions|water and sanitation services|a named utility system|safe service coverage|households and utility workers|UN-Habitat sanitation reports and utility data|Distinguish design capacity from delivered safe service.|source to tap;wastewater treatment;service gaps;water quality;utility governance
508|Waste Management|Earth_Environment|waste collection and treatment|a municipal waste stream|collection and recovery outcomes|residents and waste workers|municipal records and material-flow studies|Track the full destination of waste; recycling claims need evidence.|collection access;sorting losses;landfill impacts;informal workers;product redesign
509|Urban Climate Adaptation|Earth_Environment|city adaptation to climate hazards|a named neighborhood|measured risk reduction|exposed residents|IPCC and UN-Habitat city assessments|State hazard, place and timescale; a plan is not delivered protection.|urban heat;flood drainage;coastal risk;green infrastructure;adaptation equity
510|Infrastructure Maintenance|Engineering_Inventions|maintenance of public infrastructure|a bridge, pipe or public facility|reliability and safety|users and maintenance crews|inspection records and engineering standards|Do not infer safety from appearance or give repair instructions.|inspection cycles;deferred repair;asset registers;failure precursors;service interruptions
511|Semiconductors|Engineering_Inventions|semiconductor design and fabrication|a chip supply chain|yield and performance|engineers and downstream users|NIST semiconductor research and industry records|Name process node, device and period; avoid universal performance claims.|chip architecture;fabrication steps;yield loss;packaging;critical supply
512|Quantum Computing|Computing_Software|quantum computing systems|a published hardware demonstration|error and task performance|researchers and users|peer-reviewed experiments and technical benchmarks|Separate physical qubits, logical qubits and useful applications.|qubit platforms;error correction;benchmark design;algorithm limits;hardware scaling
513|Human-Computer Interaction|Computing_Software|interface design and use|a defined user task|task success and accessibility|users with varied abilities|usability studies and accessibility standards|Test with users; interface preference alone is not measured benefit.|user research;interaction errors;accessibility;trust and feedback;design iteration
514|Open-Source Software|Computing_Software|open-source project ecosystems|a named software project|maintenance and adoption|maintainers and users|project repositories, licenses and security records|Name license and version; open code does not guarantee security or support.|license choices;maintainer labor;contribution governance;security response;project sustainability
515|Internet Governance|Computing_Software|internet standards and governance|a named protocol or policy decision|interoperability and access|network operators and users|IETF, ICANN and public policy records|Separate standards bodies, states and platform power.|protocol standards;domain names;network neutrality;cross-border rules;multistakeholder voice
516|Labor Rights|Careers_Workplace|rights at work|a defined sector and jurisdiction|worker protection outcomes|employees and contractors|ILO conventions and local labor law|Name jurisdiction and employment status; prompts are not legal advice.|collective bargaining;pay protections;working time;contractor status;grievance routes
517|Worker Safety|Careers_Workplace|occupational safety systems|a named workplace task|injury and exposure outcomes|workers and safety staff|ILO, OSHA and incident investigations|Use current site rules; do not present an editorial angle as safety certification.|hazard identification;incident investigation;training quality;protective design;worker voice
518|Cooperatives|Commerce_Industry|cooperative ownership|a named cooperative enterprise|member and business outcomes|worker or consumer members|cooperative bylaws and audited reports|Check actual voting and surplus rules; the label alone proves little.|member governance;capital access;surplus distribution;market competition;cooperative failure
519|Poverty & Inequality|People_Communities|poverty and unequal opportunity|a defined place and population|income and service gaps|affected households|World Bank and national household data|Define poverty measure and denominator; avoid stereotypes.|measurement thresholds;housing costs;wealth gaps;social mobility;policy effects
520|Public Budgets|Government_Geopolitics|government revenue and spending|a named public budget|delivered services and costs|taxpayers and service users|official budget and audit documents|Distinguish appropriation, expenditure and outcome; name fiscal year.|revenue sources;budget negotiation;procurement;spending audits;local participation
521|Soil Science|Earth_Environment|soil formation and function|a measured field site|soil properties and change|farmers and ecosystems|soil surveys and peer-reviewed field studies|Name depth, location and method; avoid universal soil prescriptions.|soil horizons;microbial life;erosion;soil carbon;land-use effects
522|Air Quality|Earth_Environment|air pollution and exposure|a named urban or rural airshed|pollutant exposure|residents and outdoor workers|WHO air-quality guidance and monitoring data|State pollutant, monitor location and averaging period.|pollution sources;monitoring gaps;indoor versus outdoor;health burden;clean-air policy
523|Biodiversity Conservation|Earth_Environment|conservation of species and habitats|a protected landscape|species and habitat outcomes|local communities and conservation workers|IUCN assessments and field monitoring|Name species, site and baseline; designation is not proof of recovery.|threat assessment;habitat connectivity;restoration;community stewardship;monitoring bias
524|Food Systems|Land_Outdoor|food production and distribution|a regional food supply chain|affordability and resource use|farmers, workers and eaters|FAO statistics and supply-chain studies|Set system boundary and period; avoid single-cause food narratives.|farm inputs;processing;distribution;food loss;nutrition access
525|Sustainable Fisheries|Land_Outdoor|fisheries management|a named fish stock and fishery|stock and livelihood outcomes|fishers and coastal communities|FAO and regional stock assessments|Name stock, gear, jurisdiction and assessment year.|stock estimates;bycatch;small-scale fishers;traceability;management tradeoffs
526|Indigenous Histories|Historical_People_Cultures|Indigenous communities' histories|a community-authorized account|historical interpretation|source communities|community archives, oral histories and primary records|Use community names and permissions; avoid treating one account as universal.|sovereignty;land records;language continuity;colonial archives;community memory
527|Oral History|Historical_People_Cultures|oral-history practice|a consented interview collection|context and preservation|narrators and communities|oral-history recordings, consent and archival metadata|Distinguish memory from contemporaneous record; honor access conditions.|interview design;memory and time;transcription;consent;archival access
528|Libraries & Archives|Historical_People_Cultures|library and archive systems|a named collection|preservation and public access|readers and archivists|catalogs, collection policies and preservation records|A catalog entry is not full provenance or unrestricted reuse.|collection development;catalog bias;conservation;digital access;rights and restrictions
529|Translation|Literature_Performance|translation across language and culture|a named text and two versions|meaning and reception|authors, translators and readers|source texts, translation notes and critical editions|Name versions and permissions; no translation is culturally neutral.|lexical choices;untranslatable terms;translator credit;localization;reader interpretation
530|Media Literacy|Learning_Education|media and information literacy|a dated public claim or media lesson|source-evaluation skill|learners and media users|UNESCO media-literacy resources and learning studies|Check original evidence and assess learning, not just confidence.|source verification;algorithm awareness;misinformation paths;image context;teaching transfer"""

BASE = [
    ("history_origins", "History & Origins"), ("famous_examples", "Famous Examples"),
    ("hidden_stories", "Hidden Stories"), ("beginner_explainers", "Beginner Explainers"),
    ("advanced_concepts", "Advanced Concepts"),
    ("mysteries_unsolved_cases", "Mysteries & Unsolved Cases"),
    ("technology_innovation", "Technology & Innovation"),
    ("people_personalities", "People & Personalities"),
    ("major_events", "Major Events"), ("how_it_works", "How It Works"),
    ("rise_fall", "Rise & Fall"), ("then_vs_now", "Then vs Now"),
    ("future_developments", "Future Developments"),
    ("myths_vs_facts", "Myths vs Facts"),
    ("documentary_stories", "Documentary Stories"),
]


def records():
    parsed = []
    for line in ROWS.splitlines():
        cells = line.split("|")
        if len(cells) != 10:
            raise ValueError(f"Expected 10 fields: {line}")
        number, title, category, focus, case, metric, people, evidence, boundary, lenses = cells
        parsed.append(dict(id=number, title=title, category=category, focus=focus,
                           case=case, metric=metric, people=people, evidence=evidence,
                           boundary=boundary, lenses=lenses.split(";")))
    if [int(record["id"]) for record in parsed] != list(range(501, 531)) or any(len(r["lenses"]) != 5 for r in parsed):
        raise ValueError("Expansion must have IDs 501-530 and five field lenses each")
    return parsed


def angle_plan(record):
    focus, case, metric, people = (record[key] for key in ("focus", "case", "metric", "people"))
    designs = [
        ("history_origins", f"How {record['title']} Developed", f"Which changes made {focus} possible in {case}?", "Trace a dated development and earlier conditions."),
        ("famous_examples", f"A Documented {record['title']} Case", f"What does {case} demonstrate about {focus}?", "Compare the case with its stated limitations."),
        ("hidden_stories", f"People behind {record['title']}", f"Whose contribution to {focus} is missing from the usual account?", f"Seek records and accounts from {people}."),
        ("beginner_explainers", f"Understanding {record['title']}", f"What are the key parts of {focus} in {case}?", "Define terms using a bounded example."),
        ("advanced_concepts", f"Tradeoffs in {record['title']}", f"Which mechanisms make {focus} difficult to measure or manage?", f"Compare methods against {metric}."),
        ("mysteries_unsolved_cases", f"An Open {record['title']} Question", f"Which evidence is missing about {focus} in {case}?", "State competing explanations and a feasible test."),
        ("technology_innovation", f"A Tool for {record['title']}", f"Did a new tool change {metric} in {case}?", "Separate prototype, deployment and measured effect."),
        ("people_personalities", f"Decisions in {record['title']}", f"Who shaped one decision about {focus} and whose voice was absent?", f"Use attributed accounts from {people}."),
        ("major_events", f"A Turning Point in {record['title']}", f"What changed for {people} after a dated decision or event?", "Compare before and after evidence."),
        ("how_it_works", f"How {record['title']} Works", f"How do inputs, decisions and outcomes connect in {case}?", "Map the full chain and responsible actors."),
        ("rise_fall", f"When a {record['title']} Approach Faltered", f"Why did a specific approach to {focus} grow or decline?", "Test multiple explanations with dated records."),
        ("then_vs_now", f"{record['title']} across Two Periods", f"How did {metric} change for {people} across comparable periods?", "Align definitions and denominators."),
        ("future_developments", f"Possible Next Steps in {record['title']}", f"Which assumptions would have to hold for {focus} to change?", "Present conditional scenarios and evidence gaps."),
        ("myths_vs_facts", f"Testing a {record['title']} Claim", f"Does a common claim about {focus} match evidence from {case}?", "Trace the claim to its original source."),
        ("documentary_stories", f"One {record['title']} Evidence Trail", f"How did one case move from proposal to an observed outcome?", "Build a dated, sourced sequence."),
    ]
    for lens in record["lenses"]:
        designs.append((f"field_{slugify(lens).replace('-', '_')}", lens.title(),
                        f"How does {lens} shape {metric} in {case}?",
                        f"Use a bounded example and include the perspective of {people}."))
    if len({slug for slug, *_ in designs}) != 20 or len({question for _, _, question, _ in designs}) != 20:
        raise ValueError(f"Repeated angle in {record['id']}")
    return {
        "niche_id": record["id"], "status": "generated_editorial_draft",
        "purpose": f"Explore {focus} through {case}, measured outcomes, and affected people.",
        "generation_basis": "501-530 expansion candidate grid; editorial review pending",
        "editorial_principles": ["Choose a specific case and date before production.",
                                 "Verify each source and factual claim for the selected episode.", record["boundary"]],
        "review_note": "Twenty distinct candidate questions per niche. Editorial wording, source feasibility, and factual claims still require review.",
        "angles": [dict(slug=slug, angle=title, question=question, scope=scope,
                        evidence=record["evidence"], boundary=record["boundary"])
                   for slug, title, question, scope in designs],
    }


def write_if_changed(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8")


def main():
    additions = records()
    with TAXONOMY.open(encoding="utf-8", newline="") as stream:
        old = list(csv.DictReader(stream))
        columns = list(old[0])
    if len(old) not in (500, 530) or len({row["id"] for row in old}) != len(old):
        raise ValueError("Unexpected taxonomy state")
    existing_names = {slugify(row["title"]) for row in old if int(row["id"]) <= 500}
    if any(slugify(record["title"]) in existing_names for record in additions):
        raise ValueError("A proposed niche duplicates an existing title")
    existing_categories = {row["primary_category"] for row in old}
    if any(record["category"] not in existing_categories for record in additions):
        raise ValueError("Unknown category in expansion")
    new_rows = []
    for record in additions:
        number = record["id"]
        slug = slugify(record["title"])
        home = f"REGISTRY/Niches/{number}_{slug}"
        new_rows.append(dict(id=number, title=record["title"], current_path=f"{home}/Angles",
                             primary_category=record["category"], secondary_categories="",
                             legacy_secondary_categories="", slug=slug,
                             review_status="new_expansion_2026_10_16", niche_path=home))
    if len(old) == 530 and old[500:] != new_rows:
        raise ValueError("Existing 501-530 rows differ; inspect before overwrite")
    if len(old) == 500:
        with TAXONOMY.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=columns)
            writer.writeheader()
            writer.writerows(old + new_rows)
    master_lines = ["# Niche master registry extension: IDs 501-530", "", "The original 500-entry master is preserved separately. These entries supply stable base angle slugs.", ""]
    for record in additions:
        master_lines += [f"## {int(record['id'])}. {record['title']}", ""]
        master_lines += [f"{index}. {record['title']} — {label}" for index, (_, label) in enumerate(BASE, 1)]
        master_lines.append("")
    write_if_changed(MASTER_EXTENSION, "\n".join(master_lines) + "\n")
    from populate_niches import parse_visual_style
    # The base 500 styles are still the visual source. A similar category is a
    # starting palette, while each niche keeps its own editable CAT and plan.
    visual_lines = ["# Visual style extension: IDs 501-530", "", "| ID | Niche | Primary Visual Style | Visual Language | Palette | Lighting | Camera | Motion | Thumbnail Direction | AI Keywords | Avoid |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    with (REGISTRY / "MASTER_VISUAL_STYLE.md").open(encoding="utf-8") as stream:
        original_lines = stream.readlines()
    by_category = {}
    for row in old[:500]:
        by_category.setdefault(row["primary_category"], int(row["id"]))
    base_styles = {}
    names = ("niche", "primary_visual_style", "visual_language", "palette", "lighting", "camera", "motion", "thumbnail_direction", "ai_keywords", "avoid")
    for line in original_lines:
        if line.startswith("| ") and line.split("|")[1].strip().isdigit():
            cells = [cell.strip() for cell in line.split("|")[2:-1]]
            base_styles[int(line.split("|")[1])] = dict(zip(names, cells))
    for record in additions:
        style = base_styles[by_category[record["category"]]]
        cells = [record["id"], record["title"]] + [style[name] for name in names[1:]]
        visual_lines.append("| " + " | ".join(cells) + " |")
    write_if_changed(VISUAL_EXTENSION, "\n".join(visual_lines) + "\n")
    for record, row in zip(additions, new_rows):
        path = ROOT / row["niche_path"] / "ANGLE_PLAN.json"
        if path.exists():
            existing = json.loads(path.read_text(encoding="utf-8"))
            if existing.get("niche_id") != record["id"]:
                raise ValueError(f"Plan ID mismatch: {path}")
        else:
            write_if_changed(path, json.dumps(angle_plan(record), ensure_ascii=False, indent=2) + "\n")
    schema_path = REGISTRY / "CONFIG_SCHEMA.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    schema["description"] = "Q1-Q42 schema for independent niche CAT configurations; subject overrides seed new CAT files but are not parallel runtime presets."
    write_if_changed(schema_path, json.dumps(schema, ensure_ascii=False, indent=2) + "\n")
    all_rows = old[:500] + new_rows
    counts = Counter(row["primary_category"] for row in all_rows)
    index = ["# Subject category index", "", f"The {len(counts)} subjects group {len(all_rows)} independent niche homes. Each niche has one CAT, one NICHE, and Q3-only angle choices.", "", "See the [complete niche master list](NICHE_MASTER_LIST.md) for IDs, subject assignments, editorial status, and file links.", "", "| Subject | Niches | Browse |", "|---|---:|---|"]
    for category, count in sorted(counts.items()):
        label = category.replace("_", " ")
        index.append(f"| {label} | {count} | [Niches](Niches/README.md#{category.lower().replace('_', '-')}) |")
    write_if_changed(REGISTRY / "CATEGORY_INDEX.md", "\n".join(index) + "\n")
    readme = ["# Niche homes", "", "Each stable ID has one CAT for Q1-Q42 defaults, one NICHE identity, one editable ANGLE_PLAN.json, and Q3-only angle choices. Current editorial status is recorded in each plan and in the master list.", "", "See the [complete niche master list](../NICHE_MASTER_LIST.md) for all IDs, status, and file routes.", ""]
    for category in sorted(counts):
        readme += [f"## {category.replace('_', ' ')}", ""]
        for row in all_rows:
            if row["primary_category"] != category:
                continue
            stem = f"{row['id']}_{row['slug']}"
            readme.append(f"- [{row['id']} {row['title']}](./{stem}/NICHE_{stem}.md) · [CAT](./{stem}/CAT_{stem}.md) · [Angles](./{stem}/Angles/ALL_TOPICS_BY_NICHE.md) · [Plan](./{stem}/ANGLE_PLAN.json)")
        readme.append("")
    write_if_changed(REGISTRY / "Niches" / "README.md", "\n".join(readme) + "\n")
    print(f"Registered IDs 501-530: {len(all_rows)} taxonomy rows, {sum(counts.values())} subject assignments")


if __name__ == "__main__":
    main()
