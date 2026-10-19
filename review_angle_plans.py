"""Audit angle-plan wording and apply the first niche-specific editorial revision.

The report is diagnostic: wording checks are signals, not proof of editorial quality.
Run --revise-448 to replace the Capitals draft while keeping all stable slugs.
"""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HOMES = ROOT / "REGISTRY" / "Niches"
REPORT = ROOT / "AUDIT" / "ANGLE_EDITORIAL_REVIEW.csv"

# slug: (title, episode question, scoped editorial direction)
CAPITALS = {
    "history_origins": ("How a Seat of Government Emerged", "Why did a particular city first become a seat of government?", "Choose one polity and period; separate its initial selection from later stories about national origins."),
    "famous_examples": ("A Capital That Changed the Model", "What does one widely cited capital actually reveal about state power?", "Examine one capital's institutions, design, and reception; test whether it is representative."),
    "hidden_stories": ("Who Built the Capital?", "Whose labor and displacement are absent from a capital's official story?", "Trace documented builders, landholders, and affected residents in one city."),
    "beginner_explainers": ("What Makes a Capital a Capital?", "How is a capital designated, and what functions can sit elsewhere?", "Use one constitution or official designation to distinguish legal status, legislative seat, executive seat, and largest city."),
    "advanced_concepts": ("Capital Status and Sovereignty", "How can rival claims to a capital expose a deeper dispute over sovereignty?", "Bound the case by jurisdiction and date; distinguish legal claims, effective control, and diplomatic practice."),
    "mysteries_unsolved_cases": ("Why Was This Site Chosen?", "Which reasons for a capital's location are documented, and which remain uncertain?", "Compare contemporary decision records with later explanations for one selection."),
    "technology_innovation": ("Infrastructure for Governing", "Which communication or transport change altered where a government could operate?", "Follow a dated technology through the practical constraints of one governing center."),
    "people_personalities": ("The Capital Decision Makers", "Who had authority to choose a capital, and whose interests did the decision serve?", "Reconstruct a named decision using records of the competing proposals and affected communities."),
    "major_events": ("When a Capital Moved", "What event triggered one move of the seat of government?", "Compare the government's stated reasons with the documented sequence of relocation."),
    "how_it_works": ("How a Government Uses Its Capital", "Which institutions must be in a capital, and which can function elsewhere?", "Map the actual locations and duties of institutions for one polity at a fixed date."),
    "rise_fall": ("Losing Capital Status", "What changed for a city after it ceased to be a capital?", "Compare documented administrative, economic, and cultural effects before and after one change."),
    "then_vs_now": ("A Capital Across Two Periods", "How did the role of one capital change between two dated periods?", "Use the same criteria for institutions, population, boundaries, and access in both periods."),
    "future_developments": ("Proposals for a New Capital", "What constraints would determine whether a proposed capital move can happen?", "Examine a current proposal as a conditional scenario; date each claim and avoid predicting adoption."),
    "myths_vs_facts": ("Testing a Capital Origin Story", "Does a popular account of why a capital was chosen match the contemporary record?", "Identify the earliest version of the story and compare it with decision documents."),
    "documentary_stories": ("One Capital Decision in Documents", "How did one capital designation proceed from proposal to implementation?", "Build a sourced timeline of a single decision, including dissent and administrative follow-through."),
    "map_vs_ground": ("Capital on the Map and in Practice", "Does the officially mapped capital match where government actually works?", "Compare legal designation, institutional addresses, and dated records of actual proceedings."),
    "route_choices": ("Why This Location?", "How did access between regions shape the choice of one capital site?", "Compare rival candidate sites with period-appropriate routes, travel times, and political constraints."),
    "seasonality": ("Seasonal Seats of Government", "Why did a government operate from different cities in different seasons?", "Investigate a documented seasonal arrangement and its administrative and climatic reasons."),
    "local_voice": ("Residents and the Capital Project", "How did residents describe the effects of a new capital on their community?", "Use attributed local accounts alongside land, housing, and public-service records."),
    "landscape_process": ("Terrain and Capital Design", "How did terrain or water shape the layout of a chosen capital?", "Compare planning documents and physical constraints for one city; avoid geographic determinism."),
    "accessibility": ("Who Can Reach Government?", "How does a capital's location affect access to national institutions?", "Compare travel cost, disability access, and administrative alternatives for defined groups."),
    "infrastructure": ("Building the Administrative City", "Which systems had to be built before a new capital could function?", "Trace a bounded set of utilities, transport, records, and offices through budgets and completion dates."),
    "environmental_pressure": ("The Environmental Cost of a Capital", "What measurable land or resource changes accompanied a capital project?", "Set a place and time window; compare impact assessments with later observed outcomes."),
    "safety_decision": ("Security and the Capital Site", "How did a documented security concern influence the location or design of a capital?", "Use public planning evidence and avoid operational details that would enable harm."),
    "place_history": ("Before It Was a Capital", "What communities and land uses existed at a capital site before designation?", "Use earlier maps, property records, archaeology where relevant, and community accounts."),
    "comparison_of_places": ("Two Capitals, One Measure", "Why do two capitals distribute government institutions differently?", "Choose two cases and compare the same legal, historical, and practical criteria."),
    "responsible_access": ("Opening the Seat of Government", "Who benefits when public access to capital institutions expands, and who bears the cost?", "Study one access policy with visitor data, security requirements, and local testimony."),
    "field_capital_relocation": ("Relocating a Capital", "Which stated goal of a capital relocation was achieved, and which was not?", "Compare a move's original plan, budget, timetable, and later evidence using dated sources."),
    "field_planned_capitals": ("A Planned Capital Meets Reality", "Where did one planned capital diverge from its original design?", "Compare the approved plan with later population, land-use, and infrastructure records."),
    "field_multiple_capitals": ("More Than One Seat of Government", "How are powers divided when a state uses more than one capital or seat?", "Map the legal roles and actual locations of institutions at one defined date."),
    "field_contested_status": ("A Contested Capital Claim", "How do law, control, and international recognition differ in one contested capital case?", "Attribute each claim to its source and date; avoid treating a disputed position as settled."),
    "field_government_geography": ("Capital, Largest City, and Regions", "What does the distance between political and population centers change in practice?", "Use one state and comparable data for administration, travel, and representation."),
}

# Each row is slug | title | question | bounded editorial direction.
RETIREMENT = """history_origins|How Retirement Provision Developed|Which documented change made retirement income possible for a particular group?|Compare the policy or workplace records before and after one dated change.
famous_examples|A Retirement Model Under Scrutiny|What does a widely cited pension or savings model actually demonstrate?|Define the country, cohort, period, and outcomes before drawing lessons.
hidden_stories|Workers Outside the Standard Plan|Whose retirement security was omitted from a celebrated scheme?|Use eligibility records and affected workers' accounts for one system.
beginner_explainers|The Three Retirement Income Sources|How do public benefits, employer plans, and personal savings differ in one jurisdiction?|Explain roles and limits using dated official descriptions rather than a universal formula.
advanced_concepts|The Risk of Outliving Assets|How do different assumptions about lifespan change a retirement projection?|Compare transparent hypothetical scenarios without recommending a withdrawal rate.
mysteries_unsolved_cases|Why Projections Diverge|Why do two retirement calculators produce different results for the same inputs?|Audit assumptions on returns, inflation, taxes, fees, and life expectancy.
technology_innovation|Digital Retirement Planning Tools|Which decision does a planning tool clarify, and where can it mislead?|Compare one tool's disclosed assumptions with its displayed results.
people_personalities|Who Designed the Benefit Rule?|Whose choices shaped a consequential retirement benefit rule?|Use legislative, employer, or plan records to trace one decision and affected groups.
major_events|A Retirement Rule Changed|What changed for a defined group after one dated retirement policy reform?|Compare the rule text with implementation and measured effects.
how_it_works|From Contribution to Retirement Income|How does money move through one named retirement arrangement?|Trace contributions, investment or accrual, fees, payout, and risk allocation.
rise_fall|When a Pension Promise Came Under Strain|What caused a documented retirement plan to become underfunded or curtailed?|Reconstruct funding assumptions, sponsor obligations, and dated disclosures.
then_vs_now|Retirement for Two Cohorts|How did retirement options differ for two comparable cohorts?|Hold occupation and jurisdiction steady while comparing rules and costs.
future_developments|A Conditional Retirement Scenario|Which demographic or policy assumption most changes future retirement provision?|Show competing scenarios and label projections as conditional.
myths_vs_facts|Testing a Retirement Rule of Thumb|Under what assumptions does a familiar retirement rule fail?|Trace its original context and compare hypothetical cases, without personal advice.
documentary_stories|One Worker's Retirement Paper Trail|What do plan documents reveal about one worker's changing options?|Use consented or anonymized records and distinguish individual from typical outcomes.
product_terms|The Clause That Changes the Payout|Which plan or annuity term materially changes the illustrated payout?|Read dated governing documents and compare identical hypothetical inputs.
household_cash_flow|Before and After Paychecks Stop|How does a household budget change when earned income ends?|Use a fictional, labeled budget to show fixed costs, taxes, and uncertainty.
risk_and_time|Different Risks at Different Horizons|Which retirement risk grows or shrinks as the time horizon changes?|Compare sequence, inflation, liquidity, and longevity risks in bounded scenarios.
fee_effect|The Long Run Cost of Fees|How does a fee difference alter an otherwise identical retirement illustration?|Use disclosed fee categories and transparent arithmetic, not product endorsements.
consumer_protection|What a Retirement Protection Covers|Which protection applies to a particular retirement arrangement, and what is excluded?|Specify jurisdiction, provider type, date, and official guarantee limits.
market_vs_household|A Market Headline Meets a Household Budget|Why can the same market move affect two retirees differently?|Compare hypothetical income needs and asset mixes without recommending trades.
historical_policy|A Pension Reform in Practice|Who gained or lost eligibility after one dated reform?|Compare enacted text, implementation data, and distributional effects.
inflation_effect|The Purchasing Power Gap|How does a fixed payment change in real terms under different inflation paths?|Use labeled hypothetical rates and show the arithmetic and uncertainty.
fraud_warning|Checking a Retirement Offer|Which claims in a retirement offer can be checked against official records?|Examine disclosures, registration, guarantees, and reported warning signs without reproducing a scam playbook.
comparison_method|Two Plans on Equal Terms|How do two retirement arrangements compare using the same horizon and assumptions?|List fees, guarantees, tax treatment, liquidity, and risk on one dated basis.
access_gap|Who Cannot Join a Retirement Plan?|Which eligibility or administrative rule blocks a defined group?|Use plan rules, workforce data, and testimony from affected workers.
uncertainty_range|A Range, Not a Target Number|Which assumption drives the widest range in a retirement illustration?|Vary one input at a time and show plausible, clearly hypothetical outcomes.
field_retirement_horizon|The Timing of Retirement|How does the same savings balance support different lengths of retirement?|Compare hypothetical retirement dates and durations with explicit assumptions.
field_withdrawal_risk|Withdrawals During a Downturn|Why does the order of returns matter when withdrawals are being made?|Show a transparent paired example with the same average return and different order.
field_pension_terms|Reading a Pension Promise|What do vesting, indexation, and survivor provisions mean in one plan?|Use governing plan text and dated examples; identify exclusions and contingencies.
field_inflation_exposure|Fixed and Adjusted Income|How do fixed and inflation-adjusted payouts differ across an illustrative period?|Show nominal and real amounts, eligibility terms, and tradeoffs.
field_fee_compounding|Layers of Retirement Fees|Which fees are charged by a plan, product, and adviser, and how do they accumulate?|Read all relevant disclosures and model identical pre-fee returns."""

HEALTH = """history_origins|How a Health Message Changed|Which evidence led to a change in a specific public health message?|Trace dated guidance and the studies or surveillance behind one revision.
famous_examples|A Health Campaign Under Review|What did a widely cited education campaign achieve and fail to achieve?|Compare its stated goal, design, and measured outcomes in one setting.
hidden_stories|Who Was Left Out of the Message?|Whose language or accessibility needs were omitted from a health education effort?|Use campaign materials, reach data, and affected community accounts.
beginner_explainers|Reading a Health Claim|What should a reader check before trusting a health claim?|Explain population, outcome, comparator, study design, and source using one example.
advanced_concepts|Absolute and Relative Risk|How can two accurate risk figures give different impressions?|Use a labeled numerical example with a clear baseline and time period.
mysteries_unsolved_cases|When Evidence Is Inconclusive|Why has a specific health question remained unresolved?|Map study limits, conflicting outcomes, and what future evidence would help.
technology_innovation|A Tool for Understanding Health|Does a digital health education tool improve understanding for its intended audience?|Compare accessibility, evaluation results, and privacy limits in one deployment.
people_personalities|Who Shapes Public Guidance?|Who contributed to one health recommendation, and whose perspective was missing?|Review committee records, evidence summaries, and public consultation.
major_events|A Turning Point in Health Communication|What changed in public messaging after one documented event?|Compare guidance before and after, including evidence available at each date.
how_it_works|From Study to Health Guidance|How does a finding become a public recommendation?|Trace evidence appraisal, review, drafting, and revision for one guideline.
rise_fall|Why a Health Message Lost Trust|Which documented failures reduced trust in one health campaign?|Compare message claims, later evidence, and audience feedback without guessing motives.
then_vs_now|A Health Recommendation Across Time|Why does current guidance differ from an earlier version?|Compare dated recommendations and the quality of evidence behind each.
future_developments|What Would Change the Guidance?|Which new result would justify revising a current health recommendation?|State the existing evidence gap and the kind of study needed.
myths_vs_facts|One Viral Health Claim Checked|What does the best available evidence say about a widely shared health claim?|Find the original claim, assess study quality, and state uncertainty.
documentary_stories|One Health Message's Journey|How did a specific health message move from research to public use?|Build a dated record of publication, adaptation, reception, and correction.
claim_evidence|Testing One Wellness Claim|What outcome was actually measured in studies of a wellness claim?|Compare study design, participants, endpoints, and harms rather than slogans.
care_pathway|Finding the Right Care Door|Where does a defined group encounter delays along one care pathway?|Map referral, cost, travel, language, and follow-up with published service data.
benefit_harm|Benefits and Harms in the Same Frame|How do researchers weigh benefits and harms for one preventive intervention?|Use absolute numbers, a defined population, and a fixed time horizon.
mechanism_vs_outcome|Plausible Mechanism, Measured Result|Does a proposed biological mechanism translate into a patient-important outcome?|Separate laboratory evidence from controlled clinical outcomes.
population_difference|Who Was Studied?|Can results from one study population be applied to another?|Examine inclusion criteria, subgroup evidence, and uncertainty without assuming equivalence.
quality_of_guidance|Why Guidelines Differ|Why do two reputable guidelines disagree on a health question?|Compare dates, evidence thresholds, target populations, and values.
access_to_care|An Unequal Route to Care|Which documented barrier prevents one group from accessing a service?|Use service availability, cost, travel, and language data with local context.
patient_experience|One Patient's Account in Context|What can one consented patient account show about a care process?|Pair the account with system evidence and avoid treating it as typical.
misinformation_path|How a Health Rumor Spread|What allowed one incorrect health claim to persist after correction?|Trace dated messages and corrections without amplifying harmful instructions.
prevention_boundary|What Prevention Evidence Supports|For whom has a preventive measure shown benefit, and what remains unknown?|Use current guidance and evidence for a defined population; avoid personal recommendations.
system_pressure|When Capacity Changes Care|How does a staffing or supply constraint affect a documented care pathway?|Compare service data before and during one bounded period.
historical_revision|When Evidence Overturned Advice|Which new studies led experts to revise a health recommendation?|Trace the timeline and explain why earlier evidence appeared persuasive.
field_clinical_evidence|What a Clinical Study Can Establish|Does one study answer the public claim being made from it?|Compare the claim with design, comparator, outcomes, and uncertainty.
field_care_quality|Measuring Care Quality|Which measure captures a meaningful outcome for patients in one service?|Compare process metrics with outcomes and missing data.
field_patient_safety|A Preventable Safety Failure|Which system conditions contributed to a documented safety incident?|Use a published investigation and focus on prevention rather than individual blame.
field_health_equity|A Measured Health Gap|How large is a documented care or outcome gap between defined groups?|Specify denominator, context, confounders, and affected voices.
field_service_capacity|Capacity and Waiting Time|How does service capacity relate to waiting time in one place and period?|Use dated staffing, demand, and wait-time data, noting other drivers."""


def revise_domain(niche_id, home_name, specification, purpose, evidence, boundary):
    path = HOMES / home_name / "ANGLE_PLAN.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    revisions = {}
    for line in specification.splitlines():
        slug, title, question, scope = line.split("|", 3)
        revisions[slug] = title, question, scope
    if data["niche_id"] != niche_id or {a["slug"] for a in data["angles"]} != set(revisions):
        raise ValueError(f"Stable angle slugs differ: {path}")
    for entry in data["angles"]:
        title, question, scope = revisions[entry["slug"]]
        entry.update(angle=title, question=question, scope=scope, evidence=evidence, boundary=boundary)
    data["status"] = "editorial_question_reviewed"
    data["purpose"] = purpose
    data["review_note"] = f"All {len(data['angles'])} question designs and scopes reviewed for niche fit. Case selection, local applicability, source feasibility, and factual claims remain episode-level tasks."
    data["editorial_principles"] = [
        "Use a named jurisdiction, population, and date where applicable.",
        "Present comparisons on equal terms and label illustrative scenarios.",
        "Verify primary sources and current guidance before production.",
        boundary,
    ]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def revise_capitals():
    path = HOMES / "448_capitals" / "ANGLE_PLAN.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    existing = {a["slug"] for a in data["angles"]}
    if existing != set(CAPITALS):
        raise ValueError("Capitals slugs differ from review map; inspect before editing")
    for entry in data["angles"]:
        title, question, scope = CAPITALS[entry["slug"]]
        entry.update(angle=title, question=question, scope=scope)
        entry["evidence"] = "dated government records, legal texts, historical maps, planning documents, and attributed local accounts as relevant"
        entry["boundary"] = "Date and attribute disputed status, borders, and sovereignty claims; verify current institutional locations before production."
    data["status"] = "editorial_question_reviewed"
    data["purpose"] = "How governments designate, build, move, contest, and use capitals; distinguish legal status from the location of institutions and from the largest city."
    data["review_note"] = "All 32 question designs and scopes reviewed for Capitals. Case selection, source feasibility, and factual claims remain episode-level tasks."
    data["editorial_principles"] = [
        "Use a named jurisdiction and date for every capital status claim.",
        "Separate legal designation, effective institutional location, and population size.",
        "Attribute contested claims and give affected communities a sourced voice.",
        "Select a bounded case and verify primary sources before production.",
    ]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def audit():
    with (ROOT / "REGISTRY" / "NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as fh:
        taxonomy = {row["id"]: row for row in csv.DictReader(fh)}
    sensitive = {"Finance_Banking", "Medicine_Healthcare", "Mind_Wellness", "World_Religions", "Hindu_Traditions", "Government_Geopolitics", "Crime_Safety_Public_Services"}
    rows = []
    for path in sorted(HOMES.glob("*/ANGLE_PLAN.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        angles = data["angles"]
        row = taxonomy[data["niche_id"]]
        title = row["title"]
        generic = sum(bool(re.search(r"\b(in|of|about|for) (?:a case of )?" + re.escape(title) + r"\b", a["question"], re.I)) for a in angles)
        boilerplate = sum("Ground the episode in" in a.get("scope", "") or "Investigate " in a.get("scope", "") and "through one bounded case" in a.get("scope", "") for a in angles)
        signals = []
        if generic >= 10:
            signals.append("generic_questions")
        if boilerplate >= 5:
            signals.append("template_scopes")
        if data.get("status") == "generated_editorial_draft":
            signals.append("unreviewed_draft")
        risk = row["primary_category"] in sensitive
        score = (100 if risk else 0) + generic + boilerplate
        rows.append(dict(niche_id=data["niche_id"], niche=title, category=row["primary_category"],
                         status=data.get("status", ""), angles=len(angles), generic_questions=generic,
                         template_scopes=boilerplate, sensitive_category=risk,
                         priority_score=score if data.get("status") == "generated_editorial_draft" else 0,
                         signals=";".join(signals), plan=path.relative_to(ROOT).as_posix()))
    REPORT.parent.mkdir(exist_ok=True)
    with REPORT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return rows


def audit_scopes():
    """Check every scope in the context of its question, evidence and boundary.

    Completeness and duplication checks do not establish editorial or factual approval.
    """
    boilerplate = {
        "Trace a dated development and earlier conditions.",
        "Compare the case with its stated limitations.",
        "Define terms using a bounded example.",
        "State competing explanations and a feasible test.",
        "Separate prototype, deployment and measured effect.",
        "Compare before and after evidence.",
        "Map the full chain and responsible actors.",
        "Test multiple explanations with dated records.",
        "Align definitions and denominators.",
        "Present conditional scenarios and evidence gaps.",
        "Trace the claim to its original source.",
        "Build a dated, sourced sequence.",
    }
    with (ROOT / "REGISTRY/NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as stream:
        taxonomy = list(csv.DictReader(stream))
    records, errors = [], []
    revised = 0
    for row in taxonomy:
        path = ROOT / row["niche_path"] / "ANGLE_PLAN.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        entries = data["angles"]
        scopes = [a.get("scope", "").strip() for a in entries]
        complete = sum(all(isinstance(a.get(k), str) and a[k].strip()
                           for k in ("slug", "angle", "question", "scope", "evidence", "boundary"))
                       and a["question"].strip().endswith("?") for a in entries)
        repeated = len(scopes) - len(set(scopes))
        generic = sum(s in boilerplate or s.startswith("Use a bounded example and include the perspective of ") for s in scopes)
        rewritten = data.get("scope_review", {}).get("status") == "scope_wording_revised"
        revised += len(entries) if rewritten else 0
        signals = []
        if complete != len(entries): signals.append("incomplete_scope_context")
        if repeated: signals.append("repeated_scope_within_plan")
        if generic: signals.append("broad_expansion_template")
        if signals: errors.append(f"{row['id']}: {', '.join(signals)}")
        records.append(dict(niche_id=row["id"], niche=row["title"], angles=len(entries),
                            complete_scope_contexts=complete, distinct_scopes=len(set(scopes)),
                            repeated_scopes=repeated, broad_templates=generic,
                            scope_wording="revised" if rewritten else "existing",
                            plan_status=data.get("status", ""),
                            structural_result="pass" if not signals else "needs_attention",
                            plan=path.relative_to(ROOT).as_posix()))
    destination = ROOT / "AUDIT/ANGLE_SCOPE_REVIEW.csv"
    with destination.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    total = sum(r["angles"] for r in records)
    summary = [
        "# Angle scope review", "",
        f"Checked **{len(records)} niche plans** and **{total:,} angle scopes** against the active taxonomy. "
        f"Plans needing structural attention: **{len(errors)}**.", "",
        "The [per-niche ledger](ANGLE_SCOPE_REVIEW.csv) checks every angle's question, coverage, evidence direction and limit. "
        "It also checks for repeated scopes within a plan and the broad templates used by the original expansion draft. "
        "A short coverage instruction is assessed together with its angle question and limit; length alone is not treated as a defect.", "",
        f"**{revised:,} scopes in IDs 501–530 were rewritten** with angle-specific research tasks and comparisons. "
        "The [change ledger](ANGLE_SCOPE_CHANGES.csv) retains the previous and revised wording. "
        "The [focus-question ledger](ANGLE_FOCUS_CHANGES.csv) also records 150 field-angle questions aligned with the new scopes. "
        f"The other {total-revised:,} existing scopes retain their curated coverage instructions and are now displayed with their focus, evidence and limits. "
        "The 80 AI and Sanatan pilot angles also received explicit evidence and limit fields.", "",
        "## Use in production", "",
        "Edit scope wording in the niche's `ANGLE_PLAN.json`, then regenerate its angle files. "
        "Each angle file displays Focus / example question, Coverage, Evidence to seek and Limits. "
        "New Phase 0 configurations snapshot that section so Phase 1 can use it after the registry changes. "
        "Choose the concrete case, source or work and relevant place, population, version or period in the episode story question and research summary.", "",
        "Scope checks do not change a plan's editorial status or verify sources and claims. "
        f"Current inventory: {sum(r['plan_status'] == 'editorial_question_reviewed' for r in records)} plans with reviewed question designs, "
        f"{sum(r['plan_status'] == 'generated_editorial_draft' for r in records)} editorial drafts and "
        f"{sum(r['plan_status'] in ('pilot_for_review', 'deep_pilot_for_review') for r in records)} pilots. "
        "See the [expansion editorial review](EXPANSION_EDITORIAL_REVIEW.md) for the later source and overlap checks on IDs 501–530. "
        "Existing episode configurations are preserved; their original angle references remain available.", "",
        "## Refresh", "", "```powershell",
        "python review_angle_plans.py --scope-audit",
        "python populate_niches.py --id <ID> --sync-content",
        "python populate_niches.py --id <ID> --verify-content",
        "```", "",
    ]
    if errors: summary += ["## Findings", ""] + [f"- {error}" for error in errors] + [""]
    (ROOT / "AUDIT/ANGLE_SCOPE_REVIEW.md").write_text("\n".join(summary), encoding="utf-8")
    print(f"Scope audit: {len(records)} plans, {total} angles, {revised} revised scopes, {len(errors)} flagged plans")
    if errors:
        raise SystemExit("\n".join(errors))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--revise-448", action="store_true")
    parser.add_argument("--revise-500", action="store_true")
    parser.add_argument("--revise-015", action="store_true")
    parser.add_argument("--scope-audit", action="store_true", help="Check all angle scope contexts and write the scope ledger")
    args = parser.parse_args()
    if args.revise_448:
        revise_capitals()
    if args.revise_500:
        revise_domain(
            "500", "500_retirement_education", RETIREMENT,
            "Education about retirement systems, plan terms, illustrative scenarios, and the limits of generalized financial rules.",
            "dated plan documents, regulator publications, policy records, and transparent hypothetical calculations",
            "Explain uncertainty, jurisdiction, fees, and risks; do not give individualized financial advice.",
        )
    if args.revise_015:
        revise_domain(
            "015", "015_health_wellness_education", HEALTH,
            "Health literacy, evidence appraisal, care access, and communication of health findings for defined populations.",
            "current clinical guidance, systematic reviews, study methods, public health records, and consented accounts",
            "Do not present an education angle as diagnosis or treatment advice; check current guidance and population fit.",
        )
    rows = audit()
    print(f"Reviewed inventory: {len(rows)} plans, {sum(r['angles'] for r in rows)} angles")
    print("Statuses:", dict(Counter(r["status"] for r in rows)))
    print("Report:", REPORT)
    if args.scope_audit:
        audit_scopes()
