"""Create missing editorial subject maps from curated seeds; never overwrite a bank.

JSON banks become the editable source after creation. The seeds document this
initial coverage pass, not an alternative source to reapply over editorial edits.
Run with --write to create missing banks, then use render_topic_banks.py.
"""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEEDS = Path(__file__).with_name("initial_subject_map_seeds.txt")
DATE = "2026-10-22"
PROFILES = {
 "technical": {
  "question": "{topic}: how does it work, and where do its design assumptions fail?",
  "requirements": "Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.",
  "source_leads": ["original engineering papers", "official versioned product or standards documentation", "test reports and drawings with clear provenance"],
  "outline": ["Map the components and operating conditions behind {topic}.", "Trace a worked example using a diagram, calculation or observed system; state all numerical assumptions.", "Compare an alternative design against the same requirements; include cost, reliability and accessibility where relevant.", "Examine a failure mode, measurement error or edge case and show what evidence would change the explanation."]},
 "science": {
  "question": "{topic}: what mechanisms and measurements support the explanation?",
  "requirements": "Use original observations or experiments, an appropriate scientific reference and the actual measurement method. Distinguish mechanisms, correlations, model assumptions, uncertainty and limits of generalization.",
  "source_leads": ["original research reports and data", "research-institution observation records", "methods papers and current scientific reference works"],
  "outline": ["Define {topic} precisely and identify the scale, system or population being studied.", "Explain the proposed mechanism with an observable example; distinguish model from direct observation.", "Inspect how the key quantity is measured and which controls or comparison conditions matter.", "Discuss uncertainty, alternative explanations and a result that would challenge the account."]},
 "history": {
  "question": "{topic}: what do contemporary records establish, and what remains uncertain?",
  "requirements": "Compare dated primary records, material evidence and historical scholarship. Distinguish event dates, the dates of surviving witnesses, later retellings and disagreement. Do not invent quotations, intentions or an unbroken lineage.",
  "source_leads": ["dated archival records and original publications", "inscriptions, artifacts or photographs with provenance", "critical editions and historical scholarship"],
  "outline": ["Locate {topic} in a bounded time and place; build a chronology from identified records.", "Compare at least two independent witnesses or explain why only one survives.", "Analyze institutions, material conditions and overlooked participants rather than attributing everything to a single figure.", "Separate documented conclusions, interpretive debates and gaps that a reconstruction cannot resolve."]},
 "tradition": {
  "question": "{topic}: how do named sources and interpreters explain it?",
  "requirements": "Identify the text, edition, translator, commentary, community and ritual context as applicable. Attribute theological and spiritual claims, preserve regional variation and respect public versus restricted knowledge.",
  "source_leads": ["primary texts in traceable editions", "authorized public teaching and ritual descriptions", "consented community accounts and critical historical studies"],
  "outline": ["Identify the source passages, images or authorized descriptions that define {topic}.", "Explain key terms within their own literary, philosophical or devotional setting.", "Compare a second attributed interpretation without merging distinct traditions or ranking spiritual truth.", "Document what is uncertain, restricted, disputed or lost in translation; choose visuals that do not invent sacred attributes."]},
 "community": {
  "question": "{topic}: how do participants describe the practice and its differences?",
  "requirements": "Use consented participant accounts, local records and the community's own descriptions. Include differences of position, access and power; testimony is not a representative survey or clinical proof.",
  "source_leads": ["consented interviews and oral histories", "community publications and local records", "field notes with method and consent documented"],
  "outline": ["Choose a specific community and identify who participates in {topic} and who may be excluded.", "Document the actual routines, resources and relationships involved through more than one perspective.", "Compare change across generations, locations or life circumstances without assuming uniformity.", "Return to participants for context and consent checks; distinguish their views from the narrator's interpretation."]},
 "media": {
  "question": "{topic}: which creative choices change what the audience understands?",
  "requirements": "Analyze an identifiable work or create a clearly labeled original example. Connect creative decisions to observable audience information; respect rights, attribution, consent and the difference between intent and reception.",
  "source_leads": ["the actual work and authorized production materials", "creator interviews or published craft explanations", "permission-cleared examples and audience feedback"],
  "outline": ["Identify the audience, format and communication problem for {topic}.", "Annotate a specific scene, design or draft to show how the creative choice works.", "Compare a revised version and explain what information, feeling or interpretation changes.", "Check accessibility, rights, consent and possible misreadings before treating the example as a reusable method."]},
 "fiction": {
  "question": "How could a story about {topic} develop conflict, consequences and a satisfying resolution?",
  "requirements": "Create original fiction with explicit world rules, character goals and causal continuity. Label invented events and separate inspiration from claims about actual cultures or living people.",
  "source_leads": ["original story notes and world rules", "permission-cleared reference material", "reader feedback and a continuity audit"],
  "outline": ["Define the protagonist's goal and the central conflict in {topic}.", "Build three causally connected turning points with visible costs and character choices.", "Plant a detail that earns the ending; test whether a reader can follow the world's rules.", "Review cultural attribution, consent and sensitive portrayals; label the episode as original fiction."]},
 "finance": {
  "question": "{topic}: which assumptions change the costs, risks and outcomes?",
  "requirements": "Use current official terms, filings or macroeconomic data; state jurisdiction, date, fees, taxes, risk, units and assumptions. Use transparent illustrative calculations rather than personal recommendations or return promises.",
  "source_leads": ["regulator or official statistical publications", "actual contracts, fee schedules and audited filings", "original economic studies and disclosed calculation inputs"],
  "outline": ["Specify the institution, product, market or household scenario behind {topic}, with date and jurisdiction.", "Work through a numerical example with explicit fees, cash flows and assumptions; label invented figures as illustrative.", "Stress-test a different price, income, rate or time horizon and identify who bears the risk.", "Compare official terms with common promotional claims and list the unresolved information a decision would require."]},
 "health": {
  "question": "{topic}: what does current evidence establish for a defined population?",
  "requirements": "Inspect current professional guidance and original studies for the exact population, intervention or measurement. Report comparators, absolute outcomes, uncertainty, harms and limits. Do not diagnose, prescribe or imply that education replaces professional care.",
  "source_leads": ["current official clinical or public-health guidance", "original trials, cohort studies or diagnostic-validation reports", "study registrations, protocols and adverse-event records"],
  "outline": ["Define {topic}, the population and the outcome; distinguish normal variation, symptoms, screening and diagnosis where applicable.", "Explain the relevant mechanism without turning a plausible mechanism into proof of a clinical effect.", "Compare actual study designs, outcomes and follow-up; inspect harms, missing data and generalizability.", "State the evidence limits and the boundary between public education and an individual's clinical assessment."]},
 "civic": {
  "question": "{topic}: how do the rules and institutions work in a named jurisdiction?",
  "requirements": "Use the current official legal text, policy, procedure or public dataset for a specific jurisdiction and date. Distinguish written rules, implementation and lived access; give no personal legal or financial conclusion.",
  "source_leads": ["official laws, rules and administrative guidance", "audits, judgments and public service records", "consented accounts from affected people and qualified specialists"],
  "outline": ["Map the responsible institutions, applicable date and jurisdiction for {topic}.", "Trace a documented case or service journey from entry conditions to outcome, distinguishing rules from actual implementation.", "Compare access, costs, incentives and accountability for different affected groups.", "Check amendments, exceptions and competing interpretations; identify where qualified local guidance is required."]},
 "scenario": {
  "question": "{topic}: what follows if the stated assumptions hold?",
  "requirements": "Declare a conditional scenario, not a prediction. Anchor present-day capabilities in evidence, make physical and institutional assumptions explicit, and trace second-order consequences and failure conditions.",
  "source_leads": ["current original research on the enabling technologies", "physical and economic constraints with explicit inputs", "published scenario methods and relevant legal frameworks"],
  "outline": ["List the assumptions that make {topic} possible and distinguish demonstrated capability from speculation.", "Build a resource, energy, time or governance budget appropriate to the scenario.", "Follow consequences for daily life, institutions and unequal access rather than only depicting impressive technology.", "Change a major assumption and show how the scenario branches; identify observable evidence that would alter confidence."]},
 "synthesis": {
  "question": "{topic}: which distinctions and evidence change the conclusion?",
  "requirements": "Define the rival claims and their evidence standards. Compare sources on equal terms, separate empirical findings from values or interpretations and do not imply that all positions have equal evidential support.",
  "source_leads": ["the original sources behind the compared claims", "explicit definitions and measurement methods", "independent critiques with traceable evidence"],
  "outline": ["State the exact question behind {topic} and identify any terms that different sources use differently.", "Build a claim-by-claim comparison rather than contrasting slogans.", "Identify a concrete example that distinguishes the explanations and inspect its evidence.", "Explain what remains undecidable, what evidence is missing and what would justify revising the conclusion."]},
 "digital": {
  "question": "{topic}: what changes across products, versions and user settings?",
  "requirements": "Inspect the actual product version, official documentation, terms and privacy policies. Test claims under stated conditions and distinguish account permissions, data retention, measured functionality and marketing.",
  "source_leads": ["official versioned documentation and release notes", "dated privacy policies and service terms", "reproducible product tests and original validation reports"],
  "outline": ["Identify the product, version, region and user settings relevant to {topic}.", "Trace an ordinary user task and observe what succeeds, fails or requires an undocumented assumption.", "Compare cost, accessibility, portability and data flows against an appropriate alternative.", "Check changes since the cited documentation and avoid presenting a single test as universal performance."]},
 "travel": {
  "question": "{topic}: what must a traveler verify for a specific route and date?",
  "requirements": "Use dated official access rules, operator schedules and local information. Separate general planning from time-sensitive availability; include accessibility, local perspectives and changing environmental conditions.",
  "source_leads": ["official transport operators and destination authorities", "current permit, visa and access rules", "consented local accounts and independently verified travel costs"],
  "outline": ["Choose the route, dates, traveler requirements and budget assumptions for {topic}.", "Verify access, transport connections, cancellation conditions and accessible facilities from official sources.", "Build a realistic plan with travel time and contingency, distinguishing verified prices from illustrative estimates.", "Examine local community impacts and list the time-sensitive details that must be checked again before travel."]}
}

# Explicit related-home clusters; links mean related coverage, never automatic equivalence.
GROUPS = [
 [1,7,337,338,531,532], [2,3,13,35,36,39,40,544,545],
 [4,18,268,269,270,271,272,273,274,275,276,277,540,541,542,543],
 [5,19,80,368,369,371,372,383,384,549], [6,118,343,344,345,346,347,348,367],
 [8,112,293,294,295,296,298,299,300,312,313,499,500],
 [9,101,171,172,351,363,537], [10,98,99,100,328],
 [11,58,59,373,374,375,376,377,378], [12,32,159,344,345,346,347,413],
 [14,38,218,219,235,236,237,238,239],
 [15,26,180,181,501,502,503,504,505,537,538,539],
 [16,70,71,453,454,455,459], [17,379,380,408],
 [20,34,74,187,188,189,190,224,225,226,227,228],
 [21,82,83,84,135,136,315,316,419], [22,45,139,418,419,420,421],
 [23,54,76,77,268,278,279,280,282,290,291,292],
 [24,91,92,93,94,191,192,524,525], [25,131,132,133,134],
 [27,154,155,336,350,353,354,483,484],
 [28,48,197,198,199,362,424,525], [29,355,356,416],
 [30,115,116,151,152,153,205,206,207,208,209,210,211,212,213,214,215,216,217],
 [31,47,51,52,109,110,111,162,422,423,424,425,426,427,428,429,430],
 [33,55,56,57,130,166,167,367,480,491],
 [37,42,75,96,220,221,222,223,240,241,242],
 [41,69,78,144,145,449,450,451,452,528,529],
 [43,81,124,125,255,256,257,340,341,550],
 [44,117,252,253,254,546,547], [46,182,183,184,185,186],
 [49,50,84,417], [53,166,468,469,470,471,472,473,474,475,476,477,478,479,481,482,485,486,487,488,489,490,492],
 [60,243,244,245,246,247,248,249,250,251,290,447],
 [61,62,63,318,319,320,321,322,323,324,325,326,327,329,511,512,513,514,515],
 [64,85,86,87,88,89,90,137,393,395,396,397,398,399,400,401,402,403,404,405,406,407,410,411,412],
 [65,67,115,200,201,202,203,204,394,521],
 [66,68,193,194,195,196,197,198,523], [72,73,102,168,169,170,173,174,175,176],
 [79,95,126,127,128,258,259,260,261,262,263,264,265,266,267,339,548],
 [97,98,183,497,498,506,516,517,518,519,520],
 [103,104,105,106,107,108,301,302,303,304,305,306,307,308,309,310,311],
 [113,114,157,158,160,161,357,358,359,360,433,434,435,436,437,438,439,440,441,442],
 [119,120,121,364,365,366], [122,123,129,527,528,530],
 [138,140,186,187,188,189,190], [141,142,143,148,149,150,526],
 [146,147,177,178,179], [229,230,231,232,233,234],
 [281,282,283,284,285,286,287,288,289], [297,318,323],
 [330,331,332,333,334,335,342], [348,349,354,361,362,507,508,509,510,522],
 [385,386,387,388,389,390,391,392],
 [443,444,445,446,447,448], [456,457,458,460,461,462,463,464,465,466,467],
 [493,494,495,496], [531,532,533,534,535,536]
]

REFINEMENTS = {
 (125,"Sponsorship disclosure"):"Podcast sponsorship disclosure",
 (535,"Sponsorship disclosure"):"Cross-platform creator sponsorship disclosure",
 (157,"Metal fatigue"):"Metal fatigue as a materials phenomenon",
 (401,"Metal fatigue"):"Metal fatigue in fabricated metalwork",
 (209,"Sediment trapping"):"Sediment trapping by mangrove root systems",
 (440,"Sediment trapping"):"Sediment trapping behind hydropower dams",
 (216,"Indoor versus outdoor exposure"):"Indoor versus outdoor lightning exposure",
 (522,"Indoor versus outdoor exposure"):"Indoor versus outdoor air-pollution exposure",
 (219,"Population distribution"):"Population distribution across Indian regions",
 (446,"Population distribution"):"Learning world population patterns through maps",
 (230,"Seasonal staffing"):"Seasonal staffing in hospitality services",
 (386,"Seasonal staffing"):"Seasonal staffing in theme parks",
 (237,"Resource dependence"):"Microstate dependence on imported resources",
 (477,"Resource dependence"):"Space settlement dependence on imported resources",
 (328,"Chain of custody"):"Chain of custody for digital evidence",
 (434,"Chain of custody"):"Gemstone chain of custody from mine to market",
 (330,"Sensor fusion"):"Sensor fusion in general-purpose robots",
 (486,"Sensor fusion"):"Sensor fusion for autonomous vehicles",
 (386,"Wayfinding"):"Visitor wayfinding in theme parks",
 (548,"Wayfinding"):"Graphic design for public wayfinding",
 (447,"Color contrast"):"Color contrast in flag design",
 (548,"Color contrast"):"Color contrast in accessible graphic design",
 (473,"Data ownership"):"Ownership of city-scale sensor data",
 (489,"Data ownership"):"Ownership of human-augmentation device data",
 (487,"Network outages"):"Home automation during network outages",
 (494,"Network outages"):"Security alarm operation during network outages",
 (488,"Content provenance"):"Content provenance in future information networks",
 (530,"Content provenance"):"Content provenance for present-day media verification",
}


def build(row, chunks, rows):
    nid, slug, name = row["id"], row["slug"], row["title"]
    categories = []
    number = 0
    for pos, chunk in enumerate(chunks):
        header, seeds = chunk.split("~")
        title, profile_key = header.split("@")
        profile = PROFILES[profile_key]
        cat = {"id": f"CATALOG-{nid}-{pos+1:02d}", "title": title,
               "level": "foundation" if pos == 0 else "intermediate" if pos == 1 else "advanced",
               "prerequisites": [] if pos == 0 else [f"CATALOG-{nid}-01"],
               "research_profile": profile_key, "topics": []}
        for subject in seeds.split(";"):
            subject = REFINEMENTS.get((int(nid), subject), subject)
            number += 1
            cat["topics"].append({
                "id": f"BANK-{nid}-{number:03d}", "title": subject,
                "question": profile["question"].format(topic=subject),
                "coverage": f"Primary context: {name}; branch: {title}. Address {subject} through one bounded case, source set or experiment. Exclude an all-purpose survey of the whole niche; distinguish the case's findings from broader claims.",
                "research_outline": [s.format(topic=subject) for s in profile["outline"]],
                "next_action": "Select and inspect a concrete case and traceable sources; record unresolved questions before choosing a registered angle and promoting an episode idea.",
                "angle": None, "status": "proposed", "verified_sources": []})
        categories.append(cat)
    neighbors = []
    for group in GROUPS:
        if int(nid) in group:
            neighbors.extend(n for n in group if n != int(nid))
    # Directly shared clusters provide candidate navigation, not a duplicate detector.
    neighbors = list(dict.fromkeys(neighbors))[:6]
    return {
        "schema_version": "1.1", "bank_type": "subject_map", "niche_id": nid,
        "slug": slug, "name": name, "primary_category": row["primary_category"],
        "updated": DATE, "status": "proposed", "editorial_depth": "initial_subject_map",
        "purpose": f"A starting subject map for a {name} YouTube channel. Categories organize concrete subtopics; each entry supplies an episode question, a research outline and a boundary for case selection. Counts follow the authored coverage, with no imposed topic maximum.",
        "counts": {"categories": len(categories), "proposed_topics": number},
        "categories": categories,
        "research_profiles": {key: {k:v for k,v in value.items() if k in ("requirements","source_leads")} for key,value in PROFILES.items() if any(c["research_profile"] == key for c in categories)},
        "suggested_series": [],
        "overlap_policy": "The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.",
        "neighboring_niches": [{"id": f"{n:03d}", "title": rows[f"{n:03d}"]["title"], "directory": f'{n:03d}_{rows[f"{n:03d}"]["slug"]}', "reason": "Related coverage cluster; inspect both scopes before creating a separate episode."} for n in neighbors],
        "handoff": [
            "Keep the BANK ID in notes. Refine the research question with an exact text edition, jurisdiction, population, product version, place, time range or clearly labeled fictional premise.",
            "Inspect actual sources; no source was verified by generating this map. Apply the existing registry planning and idea readiness process before project creation.",
            "Choose a current registered angle only after reading its niche-specific scope. This initial map has not checked or assigned angle plans for these entries.",
            "Keep Q1-Q42, CAT defaults, project snapshots, output locations and production gates unchanged. Catalog counts are not production or publication counts.",
            "Review neighboring banks for semantic overlap and follow the existing Phase 1 claim-ledger requirements. Add qualified review when required by the production contract."],
        "coverage_limits": "This initial map does not exhaust the niche, its regions, time periods, named case studies, texts, technical variants or disputed questions. It has not performed source-feasibility checks, semantic duplicate review of every pair, trend analysis, claim verification or episode production. Expand any category freely after identifying a real coverage gap; add categories where the subject requires them. Preserve existing IDs when refining wording and allocate new IDs only for genuinely new proposals."
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    rows = {r["id"]: r for r in csv.DictReader((ROOT/"REGISTRY/NICHE_TAXONOMY.csv").open(encoding="utf-8"))}
    seen = set()
    created = skipped = 0
    for line in SEEDS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        nid, *chunks = line.split("|")
        assert nid in rows and nid not in seen, nid
        seen.add(nid)
        row = rows[nid]
        directory = ROOT/"topics"/f'{nid}_{row["slug"]}'
        target = directory/"IN_DEPTH_TOPIC_BANK.json"
        if target.exists():
            skipped += 1
            continue
        bank = build(row, chunks, rows)
        if args.write:
            directory.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(bank, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        created += 1
    assert seen == set(rows)-{"278","279","280"}, "Seeds do not match the remaining taxonomy IDs"
    print(f'{created} initial maps {"created" if args.write else "would be created"}; {skipped} existing banks preserved')


if __name__ == "__main__":
    main()
