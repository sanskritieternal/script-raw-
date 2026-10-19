"""Structural validation gates for a schema-5.0 production project.

This checks files, IDs, timing and citations. It cannot establish that a source
supports a claim or that the finished video was rendered or published.
"""
import argparse
import csv
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCHEMA = json.loads((ROOT / "REGISTRY" / "CONFIG_SCHEMA.json").read_text(encoding="utf-8"))
PHASES = (
    "01_Phase0_Configuration", "02_Phase1_RESEARCH_BIBLE",
    "03_Phase2_PRODUCTION_BIBLE", "04_Phase3_SCENE_BREAKDOWN",
    "05_Phase4_PRODUCTION_PACKAGE", "06_Phase5_FINAL_AUDIT",
)
RESEARCH = (
    "Research_Summary.md", "Facts_Documented.md", "Financial_Figures_Verified.md",
    "Timeline_Accuracy_Check.md", "Source_List_with_Links.md",
    "MASTER_CONTEXT_v1.md", "Claim_Ledger.md",
)
PRODUCTION = tuple(sorted(p.name for p in (ROOT / "CORE" / "PIPELINE" / "03_Phase2_PRODUCTION_BIBLE").glob("[0-1][0-9]_*.md")))
PLACEHOLDER = re.compile(r"\[(?:TBD|TODO|PLACEHOLDER|INSERT)\]", re.I)


def read_required(path, errors):
    if not path.is_file():
        errors.append(f"Missing {path}")
        return ""
    text = path.read_text(encoding="utf-8")
    if not text.strip() or PLACEHOLDER.search(text):
        errors.append(f"Empty or placeholder content: {path}")
    return text


def config_gate(project, errors):
    text = read_required(project / PHASES[0] / "CONFIG.md", errors)
    if not text:
        return None
    from idea_bank import validate_snapshot
    validate_snapshot(text, project, errors)
    version = re.search(r"^Question schema version: (.+)$", text, re.M)
    if not version or version.group(1) != SCHEMA["version"]:
        errors.append("CONFIG schema version mismatch")
    story = re.search(r"^Story question: (.+)$", text, re.M)
    if not story or len(story.group(1).strip()) < 15 or not story.group(1).strip().endswith("?"):
        errors.append("CONFIG needs a specific researchable story question")
    episode = re.search(r"^Episode slug: ([a-z0-9]+(?:_[a-z0-9]+)*)$", text, re.M)
    niche_ref = re.search(r"^Niche identity: `([^`]+\.md)`$", text, re.M)
    cat_ref = re.search(r"^CAT preset: `([^`]+\.md)`$", text, re.M)
    topic_ref = re.search(r"^Angle preset: `([^`]+\.md)`$", text, re.M)
    if not episode or not topic_ref or not niche_ref or not cat_ref:
        errors.append("CONFIG needs episode, NICHE, CAT and angle references")
    answers = re.findall(r"^\| (Q\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$", text, re.M)
    if [qid for qid, *_ in answers] != list(SCHEMA["questions"]):
        errors.append("CONFIG must contain Q1-Q42 exactly once in order")
        return None
    values = {}
    for qid, label, answer, source in answers:
        if label.strip() != SCHEMA["questions"][qid]["label"] or not answer.strip() or not source.strip():
            errors.append(f"Invalid CONFIG answer: {qid}")
        values[qid] = answer.strip()
    risk_match = re.search(r"^- Risk flags: (.+)$", text, re.M)
    required_match = re.search(r"^- Human review required before publication: (Yes|No)$", text, re.M)
    status_match = re.search(r"^- Human review status: (.+)$", text, re.M)
    if not risk_match or not required_match or not status_match:
        errors.append("CONFIG must record risk flags, review requirement and review status")
    else:
        flags = risk_match.group(1) != "None"
        contested = values["Q10"].lower() not in {"no contested claims", "no"} or values["Q31"].lower() not in {"no controversial claims", "no"}
        required = values["Q8"] in {"High", "Critical"} or values["Q41"] in {"Strict", "Critical"} or contested or flags
        if required_match.group(1) != ("Yes" if required else "No"):
            errors.append("CONFIG review requirement is inconsistent with risk answers and flags")
        if not required and status_match.group(1) != "Not required":
            errors.append("Unexpected human review status for low-risk CONFIG")
    with (ROOT / "REGISTRY" / "NICHE_TAXONOMY.csv").open(encoding="utf-8", newline="") as fh:
        taxonomy = {r["id"]: r for r in csv.DictReader(fh)}
    match = re.match(r"^(\d{3})_", project.name)
    if not match or match.group(1) not in taxonomy:
        errors.append("Project directory must start with a stable niche ID")
        return None
    row = taxonomy[match.group(1)]
    expected_niche = f"{row['id']}_{row['slug']}"
    if project.parent.name != expected_niche:
        errors.append("Project niche folder does not match taxonomy")
    expected_preset = f"REGISTRY/Niches/{expected_niche}/NICHE_{expected_niche}.md"
    if not niche_ref or niche_ref.group(1) != expected_preset or not (ROOT / expected_preset).is_file():
        errors.append("CONFIG niche identity does not match taxonomy")
    expected_cat = f"REGISTRY/Niches/{expected_niche}/CAT_{expected_niche}.md"
    if not cat_ref or cat_ref.group(1) != expected_cat or not (ROOT / expected_cat).is_file():
        errors.append("CONFIG CAT preset does not match taxonomy")
    if values["Q1"] != row["primary_category"]:
        errors.append("CONFIG identity does not match taxonomy")
    if episode and topic_ref:
        if Path(topic_ref.group(1)).parent.as_posix() != row["current_path"] or not (ROOT / topic_ref.group(1)).is_file():
            errors.append("CONFIG angle path does not match taxonomy")
        topic_name = Path(topic_ref.group(1)).name
        prefix = f"{row['id']}_{row['slug']}_"
        if not topic_name.startswith(prefix) or not topic_name.endswith(".md"):
            errors.append("CONFIG topic preset does not match taxonomy ID and slug")
        else:
            angle = topic_name[len(prefix):-3]
            expected_project = f"{prefix}{angle}_{episode.group(1)}"
            if project.name != expected_project:
                errors.append(f"Project directory must be {expected_project}")
    runtime = re.fullmatch(r"(\d+) seconds", values["Q14"])
    if not runtime:
        errors.append("Q14 must be exact seconds for automated validation")
        return None
    total = int(runtime.group(1))
    if values["Q42"] == "VARIABLE":
        plan = re.search(r"^- Variable scene durations: ([\d, ]+) seconds$", text, re.M)
        if not plan:
            errors.append("VARIABLE Q42 requires a complete scene duration plan in CONFIG")
            return None
        durations = [int(part.strip()) for part in plan.group(1).split(",")]
        if not durations or any(n <= 0 for n in durations) or sum(durations) != total:
            errors.append("Variable scene plan must contain positive durations summing to Q14")
            return None
    else:
        scene = re.fullmatch(r"FIXED (\d+)-SECOND", values["Q42"])
        if not scene:
            errors.append("Q42 must be FIXED n-SECOND or VARIABLE")
            return None
        duration = int(scene.group(1))
        if total <= 0 or duration <= 0 or duration > total:
            errors.append("Invalid Q14/Q42 timing")
            return None
        count = math.ceil(total / duration)
        durations = [duration] * (count - 1) + [total - duration * (count - 1)]
    return values, total, durations


def research_gate(project, errors):
    folder = project / PHASES[1]
    for name in RESEARCH:
        read_required(folder / name, errors)
    ledger = read_required(folder / "Claim_Ledger.md", errors)
    claims = set()
    claim_rows = [line for line in ledger.splitlines() if re.match(r"^\| C\d{3,} \|", line)]
    if not claim_rows:
        errors.append("Claim ledger has no claim rows")
    for line in claim_rows:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 9:
            errors.append(f"Claim ledger row needs nine fields: {line[:90]}")
            continue
        claim_id, claim, source, accessed, evidence, confidence, status, dispute, scenes = cells
        if claim_id in claims:
            errors.append(f"Duplicate claim ID: {claim_id}")
        if not claim or not evidence or confidence not in {"High", "Medium", "Low"}:
            errors.append(f"Incomplete claim evidence or confidence: {claim_id}")
        if not re.search(r"https?://|doi:|archive:", source, re.I):
            errors.append(f"Claim lacks a locatable source: {claim_id}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", accessed):
            errors.append(f"Claim lacks an exact access date: {claim_id}")
        if status != "Verified":
            errors.append(f"Material claim is not verified: {claim_id} ({status})")
        if not dispute or not scenes:
            errors.append(f"Claim lacks dispute assessment or scene mapping: {claim_id}")
        claims.add(claim_id)
    return claims


def production_gate(project, values, errors):
    folder = project / PHASES[2]
    if len(PRODUCTION) != 16:
        errors.append("Source Phase 2 template set is not 16 numbered files")
    for name in PRODUCTION:
        read_required(folder / name, errors)
    locks = read_required(folder / "00_Project_Consistency_Rules.md", errors)
    for qid in ("Q3", "Q15", "Q16", "Q42"):
        if values[qid] not in locks:
            errors.append(f"Phase 2 lock missing CONFIG {qid} value")


def scenes_gate(project, claims, total, planned_durations, errors):
    folder = project / PHASES[3]
    batches = sorted(folder.glob("Batch_*_Scenes_*.md"))
    if not batches:
        errors.append("No Phase 3 scene batches")
        return set()
    scenes = []
    used_claims = set()
    for batch in batches:
        text = read_required(batch, errors)
        blocks = re.split(r"(?=\*\*Scene \d+\*\*)", text)
        for block in blocks:
            start = re.match(r"\*\*Scene (\d+)\*\*", block)
            if not start:
                continue
            duration = re.search(r"\*\*Duration:\*\* (\d+) seconds", block)
            citation = re.search(r"\*\*Claim IDs:\*\* ([^\n]+)", block)
            if not duration or not citation:
                errors.append(f"Scene {start.group(1)} missing duration or Claim IDs: {batch}")
                continue
            ids = set(re.findall(r"\bC\d{3,}\b", citation.group(1)))
            if not ids and "fictional" not in citation.group(1).lower():
                errors.append(f"Scene {start.group(1)} lacks claim IDs or fictional designation")
            if ids - claims:
                errors.append(f"Scene {start.group(1)} cites unknown claims: {sorted(ids-claims)}")
            used_claims |= ids
            scenes.append((int(start.group(1)), int(duration.group(1))))
    if [n for n, _ in scenes] != list(range(1, len(planned_durations) + 1)):
        errors.append(f"Scene IDs/count mismatch: expected 1-{len(planned_durations)}, found {len(scenes)}")
    if sum(d for _, d in scenes) != total:
        errors.append(f"Scene duration sum mismatch: expected {total}, found {sum(d for _, d in scenes)}")
    if [duration for _, duration in scenes] != planned_durations:
        errors.append(f"Scene durations do not follow the CONFIG plan: {planned_durations}")
    return used_claims


def package_gate(project, used_claims, errors):
    text = read_required(project / PHASES[4] / "Production_Package.md", errors)
    for claim in used_claims:
        if claim not in text:
            errors.append(f"Production package dropped scene claim {claim}")


def audit_gate(project, errors):
    folder = project / PHASES[5]
    config = (project / PHASES[0] / "CONFIG.md").read_text(encoding="utf-8")
    if "- Human review required before publication: Yes" in config:
        if not re.search(r"^- Human review status: Approved by .+ on \d{4}-\d{2}-\d{2}$", config, re.M):
            errors.append("Human review approval with reviewer and date is required before final certificate")
    report = read_required(folder / "Audit_Report.md", errors)
    items = re.findall(r"^\| ([A-G](?:10|[1-9])) \| (PASS|N/A|FAIL) \| ([^|]+) \|$", report, re.M)
    expected = {f"{section}{number}" for section in "ABCDEFG" for number in range(1, 11)}
    if len(items) != 70 or {code for code, _, _ in items} != expected:
        errors.append("Final audit must record A1-G10 exactly once with evidence or N/A reasons")
    if any(status == "FAIL" for _, status, _ in items):
        errors.append("Final audit contains a failed check")
    if "Blocking findings: 0" not in report:
        errors.append("Final audit must explicitly record zero blocking findings")
    certificate = read_required(folder / "Completion_Certificate.md", errors)
    if "text package complete" not in certificate.lower():
        errors.append("Certificate must identify a completed text package")


def validate(project, through):
    errors = []
    result = config_gate(project, errors)
    if result is None or through == 0:
        return errors
    values, total, planned_durations = result
    claims = research_gate(project, errors) if through >= 1 else set()
    if through >= 2:
        production_gate(project, values, errors)
        from production_workflow import check_production
        check_production(project, values, planned_durations, errors, mappings=through >= 3)
    used = scenes_gate(project, claims, total, planned_durations, errors) if through >= 3 else set()
    if through >= 4:
        package_gate(project, used, errors)
        from production_workflow import package_snapshot_errors
        errors.extend(package_snapshot_errors(project))
    if through >= 5:
        audit_gate(project, errors)
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--through", type=int, choices=range(6), default=0)
    args = parser.parse_args()
    project = args.project.resolve()
    if not project.is_dir():
        raise SystemExit(f"Missing project directory: {project}")
    errors = validate(project, args.through)
    if errors:
        print("\n".join(errors[:100]))
        raise SystemExit(f"Phase 0-{args.through} structural validation failed with {len(errors)} issue(s)")
    print(f"Phase 0-{args.through} structural validation passed for {project}")


if __name__ == "__main__":
    main()
