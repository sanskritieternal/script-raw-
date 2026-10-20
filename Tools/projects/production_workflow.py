"""Scaffold, migrate, validate and compile versioned episode production documents.

No command invents research, asset rights or human review. Migration is a preview
unless --write is supplied. Existing editorial documents are never overwritten.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = ROOT / "CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE"
SPEC_PATH = TEMPLATES / "PRODUCTION_WORKFLOW.json"
PHASE = "03_Phase2_PRODUCTION_BIBLE"
MANIFEST = "PRODUCTION_MANIFEST.json"
VERSION = "1.1"
MARKER = f"Production workflow version: {VERSION}"
SUPPORTED_VERSIONS = ("1.0", VERSION)
SCENE_MASTER = "Scene_Breakdown.md"
PLACEHOLDERS = re.compile(r"\[(?:TBD|TODO|PLACEHOLDER|INSERT)\]|\{\{[^}]+\}\}", re.I)


def specification(version=None):
    version = version or VERSION
    if version not in SUPPORTED_VERSIONS:
        raise ValueError(f"Unsupported production workflow version: {version}")
    path = TEMPLATES / "PRODUCTION_WORKFLOW_V1.json" if version == "1.0" else SPEC_PATH
    return json.loads(path.read_text(encoding="utf-8"))


def draft_document(project, answers, name):
    template = (TEMPLATES / name).read_text(encoding="utf-8")
    context = (f"\n\n## Episode context\n\nProject: {project.name}\n"
               f"Subject: {answers['Q1']}\nRuntime: {answers['Q14']}\n"
               f"Language: {answers['Q18']}\nStyle: {answers['Q15']}\n"
               "\nThis is an unfinished scaffold. Replace the instructions with episode decisions.\n[TBD]\n")
    return template.rstrip() + context


def upgrade(project, *, write=False):
    """Add new draft records without changing existing content, locks or decisions."""
    project = Path(project).resolve()
    if any(part.lower() == "legacy" for part in project.parts):
        raise ValueError("Historical OUTPUT/Legacy projects are not migration targets")
    _, answers = identity(project)
    manifest = load_manifest(project)
    old = specification(manifest.get("version", "unknown"))
    if manifest.get("project") != project.name or set(manifest.get("documents", {})) != set(old["documents"]):
        raise ValueError("Existing manifest identity/document list is invalid; repair before upgrade")
    added = [name for name in specification()["documents"] if name not in old["documents"]]
    result = {"project": project.name, "from_version": manifest["version"], "to_version": VERSION,
              "add_draft_records": added, "write": write}
    if not write or manifest["version"] == VERSION:
        return result
    folder = project / PHASE
    for name in added:
        path = folder / name
        if not path.exists():
            path.write_text(draft_document(project, answers, name), encoding="utf-8")
        manifest["documents"][name] = {"status": "draft", "reason": ""}
    manifest["version"] = VERSION
    json_write(folder / MANIFEST, manifest)
    return result


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def identity(project):
    path = project / "01_Phase0_Configuration/CONFIG.md"
    text = path.read_text(encoding="utf-8")
    answers = dict(re.findall(r"^\| (Q\d+) \| [^|]+ \| ([^|]+) \| [^|]+ \|$", text, re.M))
    answers = {k: v.strip() for k, v in answers.items()}
    if len(answers) != 42:
        raise ValueError("A complete Phase 0 CONFIG is required")
    return text, answers


def scaffold(project, *, write=False, adopt=False):
    """Create only missing files; adoption is an explicit internal document decision."""
    project = Path(project).resolve()
    if any(part.lower() == "legacy" for part in project.parts):
        raise ValueError("Historical OUTPUT/Legacy projects are not migration targets")
    config, answers = identity(project)
    spec = specification()
    folder = project / PHASE
    target = folder / MANIFEST
    if target.exists():
        raise FileExistsError("Manifest already exists; edit/review it rather than resetting status")
    existing = {name for name in spec["documents"] if (folder / name).is_file()}
    missing = [name for name in spec["documents"] if name not in existing]
    result = {"project": project.name, "preserved": sorted(existing), "create": missing,
              "manifest": MANIFEST, "write": write, "adopt_existing": adopt}
    if not write:
        return result
    folder.mkdir(parents=True, exist_ok=True)
    documents = {}
    for name in spec["documents"]:
        path = folder / name
        if name not in existing:
            path.write_text(draft_document(project, answers, name), encoding="utf-8")
        documents[name] = {"status": "complete" if adopt and name in existing else "draft", "reason": ""}
    manifest = {"version": VERSION, "project": project.name, "documents": documents,
                "locks": {q: answers[q] for q in ("Q3", "Q15", "Q16", "Q42")},
                "beats": [], "assets": [], "chapters": []}
    json_write(target, manifest)
    return result


def load_manifest(project):
    value = json.loads((project / PHASE / MANIFEST).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Production manifest must be an object")
    return value


def scene_paths(project):
    """Use the single master by default; accept older batch-only episodes."""
    folder = Path(project) / "04_Phase3_SCENE_BREAKDOWN"
    master = folder / SCENE_MASTER
    batches = sorted(folder.glob("Batch_*_Scenes_*.md"))
    if master.is_file() and batches:
        raise ValueError("Phase 3 has both Scene_Breakdown.md and batch scene files; keep one authoritative format")
    return [master] if master.is_file() else batches


def scene_records(project):
    records = []
    for path in scene_paths(project):
        for block in re.split(r"(?=\*\*Scene \d+\*\*)", path.read_text(encoding="utf-8"))[1:]:
            number = re.match(r"\*\*Scene (\d+)\*\*", block)
            duration = re.search(r"\*\*Duration:\*\* (\d+) seconds", block)
            refs = re.search(r"\*\*Claim IDs:\*\* (.+)", block)
            if not number or not duration or not refs:
                raise ValueError(f"Incomplete scene in {path}")
            records.append({"id": int(number[1]), "duration": int(duration[1]),
                            "claims": re.findall(r"C\d{3,}", refs[1]), "text": block.rstrip()})
    return records


def local_links(path, text, project, errors):
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            continue
        # IDE line references are not part of the file name.
        target = re.sub(r":\d+$", "", target.split("#", 1)[0]).strip("<>")
        if target and not (path.parent / target).exists():
            errors.append(f"Broken local link in {path.name}: {target}")


def check_production(project, answers, durations, errors, *, mappings=False):
    """Strict checks apply only after explicit enrollment or a new CONFIG marker."""
    folder = project / PHASE
    path = folder / MANIFEST
    config = (project / "01_Phase0_Configuration/CONFIG.md").read_text(encoding="utf-8")
    if not path.exists():
        if "Production workflow version:" in config:
            errors.append("New production workflow requires PRODUCTION_MANIFEST.json; run scaffold")
        return
    try:
        manifest = load_manifest(project)
        spec = specification(manifest.get("version", "unknown"))
        configured = re.search(r"Production workflow version: ([\d.]+)", config)
        if configured and configured[1] not in SUPPORTED_VERSIONS:
            errors.append("Unsupported CONFIG production workflow version")
        if configured and configured[1] == VERSION and manifest.get("version") != VERSION:
            errors.append("CONFIG requires the current production manifest version; run upgrade")
        if manifest.get("project") != project.name:
            errors.append("Production manifest version/project mismatch")
        docs = manifest.get("documents")
        if not isinstance(docs, dict) or set(docs) != set(spec["documents"]):
            errors.append(f"Production manifest must declare all {len(spec['documents'])} canonical/supporting documents exactly once")
            return
        for name, rule in spec["documents"].items():
            entry = docs[name]
            if not isinstance(entry, dict):
                errors.append(f"Invalid document status: {name}")
                continue
            status = entry.get("status")
            document = folder / name
            if not document.is_file():
                errors.append(f"Missing production document: {name}")
                continue
            text = document.read_text(encoding="utf-8")
            if not text.strip() or PLACEHOLDERS.search(text) or "This is an unfinished scaffold." in text:
                errors.append(f"Unfinished production document: {name}")
            if status == "not_applicable":
                reason = entry.get("reason", "")
                if not rule["allow_na"] or not isinstance(reason, str) or len(reason.strip()) < 15 or "not applicable" not in text.lower():
                    errors.append(f"Unjustified or disallowed Not applicable: {name}")
            elif status != "complete":
                errors.append(f"Production document is not complete: {name}")
            elif text.strip() == (TEMPLATES / name).read_text(encoding="utf-8").strip():
                errors.append(f"Unfilled shared template: {name}")
            if status == "complete":
                for pattern in rule.get("field_patterns", []):
                    if not re.search(pattern, text, re.I | re.M):
                        errors.append(f"Required production field missing in {name}: {pattern}")
            local_links(document, text, project, errors)
        if manifest.get("locks") != {q: answers[q] for q in ("Q3", "Q15", "Q16", "Q42")}:
            errors.append("Production manifest locks differ from CONFIG")
        if mappings:
            check_mappings(project, manifest, durations, errors)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        errors.append(f"Invalid production manifest: {exc}")


def check_mappings(project, manifest, durations, errors):
    records = scene_records(project)
    ids = [r["id"] for r in records]
    expected = list(range(1, len(durations) + 1))
    if ids != expected:
        errors.append("Workflow mapping requires complete sequential scene records")
        return
    if [r["duration"] for r in records] != durations:
        errors.append("Workflow scene durations differ from CONFIG timing")
    for record in records:
        for field in ("Chapter", "Location", "Time of Day / Period", "Characters", "Visual Direction",
                      "Data Visualization Specs", "Dialogue / Narration", "Voiceover Duration",
                      "Source Citation", "Legal Risk Flag", "SFX", "Music Cue", "Transition to Next Scene"):
            if not re.search(r"\*\*" + re.escape(field) + r":\*\*\s*\S", record["text"]):
                errors.append(f"Scene {record['id']} missing production field: {field}")
    claims = set(re.findall(r"^\| (C\d{3,}) \|", (project / "02_Phase1_RESEARCH_BIBLE/Claim_Ledger.md").read_text(encoding="utf-8"), re.M))
    beats = manifest.get("beats")
    if not isinstance(beats, list):
        errors.append("Manifest beats must be a list")
        return
    beat_entry = manifest["documents"]["STORY_BEAT_MAP.md"]
    if beat_entry["status"] != "not_applicable":
        covered = []
        for beat in beats:
            if not isinstance(beat, dict) or type(beat.get("start")) is not int or type(beat.get("end")) is not int:
                errors.append("Beat ranges must be whole-number start/end objects")
                continue
            first, last = beat["start"], beat["end"]
            if first < 1 or last < first or last > len(ids):
                errors.append("Beat range outside scene plan")
                continue
            covered += list(range(first, last + 1))
            refs = beat.get("claims", [])
            if not isinstance(refs, list) or set(refs) - claims:
                errors.append("Beat cites unknown claim IDs")
            actual = {c for r in records[first-1:last] for c in r["claims"]}
            if set(refs) != actual:
                errors.append("Beat claim references do not match its scenes")
        if covered != expected:
            errors.append("Beats must cover each scene exactly once in order; beat count is not fixed")
    assets = manifest.get("assets")
    if not isinstance(assets, list):
        errors.append("Manifest assets must be a list")
        return
    seen, used = set(), set()
    for asset in assets:
        if not isinstance(asset, dict) or not isinstance(asset.get("id"), str) or not asset["id"].strip() or asset["id"] in seen:
            errors.append("Asset IDs must be nonempty and unique")
            continue
        seen.add(asset["id"])
        uses = asset.get("scenes", [])
        if not isinstance(uses, list) or any(type(n) is not int or n not in ids for n in uses):
            errors.append(f"Invalid scene references for asset {asset['id']}")
        else:
            used.update(uses)
        if asset.get("status") not in {"planned", "created", "reviewed"}:
            errors.append(f"Invalid asset state: {asset['id']}")
        if asset.get("status") in {"created", "reviewed"}:
            target = asset.get("file", "")
            resolved = (project / target).resolve()
            if not target or not resolved.is_relative_to(project.resolve()) or not resolved.is_file():
                errors.append(f"Created asset file missing/outside episode: {asset['id']}")
            if asset.get("status") == "reviewed" and not asset.get("review_evidence"):
                errors.append(f"Asset review evidence missing: {asset['id']}")
    if used != set(ids):
        errors.append("Asset register mappings must cover every scene; planned assets are allowed")
    # Factual scene identifiers may use the manifest mapping without altering old scene text.
    register = (project / PHASE / "ASSET_REGISTER.md").read_text(encoding="utf-8")
    if any(not re.search(r"(?<!\w)" + re.escape(n) + r"(?!\w)", register) for n in seen):
        errors.append("Manifest asset IDs must exist in ASSET_REGISTER.md")
    chapters = manifest.get("chapters")
    metadata_status = manifest["documents"]["YOUTUBE_METADATA.md"]["status"]
    if metadata_status != "not_applicable":
        boundaries = [0]
        for duration in durations:
            boundaries.append(boundaries[-1] + duration)
        if not isinstance(chapters, list) or not chapters:
            errors.append("Applicable YouTube metadata needs chapter time mappings")
        else:
            starts = [c.get("start_seconds") if isinstance(c, dict) else None for c in chapters]
            if any(type(t) is not int or t not in boundaries[:-1] for t in starts) or starts[0] != 0 or starts != sorted(set(starts)):
                errors.append("Metadata chapters must start at zero and follow unique scene boundaries")
            else:
                text = (project / PHASE / "YOUTUBE_METADATA.md").read_text(encoding="utf-8")
                for chapter in chapters:
                    t = chapter["start_seconds"]
                    label = chapter.get("title", "")
                    if not label or f"{t//60:02d}:{t%60:02d} {label}" not in text:
                        errors.append("Chapter mapping is absent from metadata text")
                written = re.findall(r"^(\d+):(\d\d) (.+)$", text, re.M)
                written = [(int(m)*60 + int(s), title.strip()) for m, s, title in written]
                planned = [(c["start_seconds"], c.get("title", "")) for c in chapters]
                if written != planned:
                    errors.append("Metadata chapter list differs from the manifest timeline")


def input_paths(project):
    version = load_manifest(project)["version"]
    spec = specification(version)
    paths = [project / "01_Phase0_Configuration/CONFIG.md"]
    paths += sorted((project / "02_Phase1_RESEARCH_BIBLE").rglob("*"))
    paths += [project / PHASE / name for name in spec["documents"]]
    spec_path = TEMPLATES / "PRODUCTION_WORKFLOW_V1.json" if version == "1.0" else SPEC_PATH
    paths += [project / PHASE / MANIFEST, spec_path, Path(__file__).resolve()]
    paths += [project / PHASE / 'GENERATOR_PROFILE.md', Path(__file__).with_name('planning_records.py')]
    paths += sorted((project / "04_Phase3_SCENE_BREAKDOWN").glob("*.md"))
    return [path for path in paths if path.is_file()]


def input_key(project, path):
    return path.relative_to(project).as_posix() if path.is_relative_to(project) else "@system/" + path.relative_to(ROOT).as_posix()


def package_snapshot_errors(project):
    snapshot = project / "05_Phase4_PRODUCTION_PACKAGE/Package_Inputs.json"
    if not (project / PHASE / MANIFEST).exists():
        return []
    if not snapshot.exists():
        return ["Versioned workflow requires Package_Inputs.json; rebuild with python -m Tools.projects.production_workflow compile"]
    try:
        data = json.loads(snapshot.read_text(encoding="utf-8"))
        expected = {input_key(project, p): digest(p) for p in input_paths(project)}
        errors = []
        if data.get("version") != VERSION or data.get("inputs") != expected:
            errors.append("Production package is stale: input files changed; rebuild package")
        package = project / "05_Phase4_PRODUCTION_PACKAGE/Production_Package.md"
        if not package.exists() or data.get("package_sha256") != digest(package):
            errors.append("Compiled package changed outside the compiler; rebuild from sources")
        return errors
    except (ValueError, TypeError, OSError) as exc:
        return [f"Invalid package input snapshot: {exc}"]


def rebase(text, source, destination):
    import os
    def replace(match):
        target = match[1]
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            return match[0]
        path, sep, fragment = target.partition("#")
        rel = Path(os.path.relpath(source.parent / path, destination.parent)).as_posix()
        return "](" + rel + (sep + fragment if sep else "") + ")"
    result = re.sub(r"\]\(([^)]+)\)", replace, text)
    return re.sub(r"^(#{1,5}) ", lambda m: "##" + m[1] + " ", result, flags=re.M)


def scene_field(text, name):
    """Read an inline or multiline scene field without consuming the next field."""
    match = re.search(r"^\*\*" + re.escape(name) + r":\*\*[ \t]*(.*?)(?=^\*\*[^*\n]+:\*\*|^---[ \t]*$|\Z)",
                      text, re.M | re.S)
    return match[1].strip() if match else ""


def compile_package(project, *, write=False):
    from Tools.validation import validate_project
    project = Path(project).resolve()
    errors = validate_project.validate(project, 3)
    if errors:
        raise ValueError("Cannot compile before Phase 0-3 passes:\n" + "\n".join(errors))
    if not (project / PHASE / MANIFEST).is_file():
        raise ValueError("Enroll the episode with migrate before using the compiler")
    destination = project / "05_Phase4_PRODUCTION_PACKAGE/Production_Package.md"
    records = scene_records(project)
    manifest = load_manifest(project)
    spec = specification(manifest["version"])
    parts = ["# Production Package\n\nCompiled by production_workflow.py. Text package only; no rights, human approval, rendered video or publication is certified."]
    compiled = set()
    for section in spec["package_sections"]:
        parts.append("## " + section["title"])
        if section["title"].startswith("1."):
            parts.append(rebase((project / "01_Phase0_Configuration/CONFIG.md").read_text(encoding="utf-8"), project / "01_Phase0_Configuration/CONFIG.md", destination))
        if section["title"].startswith("2."):
            for name in ('SCENE_PLANNER.md', 'MASTER_SCENES_INDEX.md'):
                source = project / '04_Phase3_SCENE_BREAKDOWN' / name
                if source.is_file():
                    parts.append(rebase(source.read_text(encoding='utf-8'), source, destination))
            parts.append("\n\n\n\n".join(r["text"] for r in records))
        if section["title"].startswith("3."):
            for record in records:
                line = re.search(r"\*\*Dialogue / Narration:\*\* (.+)", record["text"])
                if not line:
                    raise ValueError(f"Scene {record['id']} lacks narration")
                parts.append(f"### Narration scene {record['id']}\n\n{line[1]}")
        if section["title"].startswith("5."):
            parts.append("### Asset-to-scene mapping\n\n" + "\n".join(f"- {a['id']}: scenes {', '.join(map(str, a['scenes']))}; {a['status']}" for a in manifest["assets"]))
        if section["title"].startswith("6."):
            for record in records:
                citation = re.search(r"\*\*Source Citation:\*\* (.+)", record["text"])
                if not citation:
                    raise ValueError(f"Scene {record['id']} lacks source locator")
                parts.append(f"### Citations scene {record['id']}\n\n" + citation[1])
            for source in sorted((project / "02_Phase1_RESEARCH_BIBLE").glob("*.md")):
                parts.append(rebase(source.read_text(encoding="utf-8"), source, destination))
        if section["title"].startswith("9."):
            profile = project / PHASE / 'GENERATOR_PROFILE.md'
            if profile.is_file():
                parts.append(rebase(profile.read_text(encoding='utf-8'), profile, destination))
            provided = [r for r in records if scene_field(r["text"], "AI Generation Prompt")]
            if provided:
                parts.append("Scene-supplied prompts and handoff instructions are collected below without selecting a provider or generating media. Exact editorial overlays remain separate from generated plates. Scene records above remain authoritative for narration, source citations and timing; these instructions do not certify created assets or rights.")
                for record in provided:
                    parts.append(f"### Generation prompt — scene {record['id']:03}")
                    for field in ("Generation Prompt ID", "AI Generation Prompt", "Editorial Overlay Instructions",
                                  "Reference Inputs", "Start State", "End State", "Asset IDs", "Execution Record"):
                        value = scene_field(record["text"], field)
                        if value:
                            parts.append(f"**{field}:** {value}")
                if len(provided) != len(records):
                    parts.append("Scenes without a supplied generation prompt retain their scene-level asset method. No prompt is invented for them.")
            else:
                parts.append("No scene-level generation prompt was supplied. Follow the episode's actual asset method and CAMERA_ANIMATION_GUIDE.md; no provider or media output is selected by the compiler. Do not treat scene text as proof that a media asset was generated.")
        for name in section["documents"]:
            source = project / PHASE / name
            parts.append(rebase(source.read_text(encoding="utf-8"), source, destination))
            compiled.add(name)
    if compiled != set(spec["documents"]):
        raise ValueError("Compiler section map must include every production document")
    inputs = {input_key(project, path): digest(path) for path in input_paths(project)}
    parts.append("### Input fingerprints\n\n| Input | SHA-256 |\n|---|---|\n" + "\n".join(f"| `{key}` | `{value}` |" for key, value in inputs.items()))
    text = "\n\n".join(parts) + "\n"
    if write:
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            backup = destination.parent / "History" / digest(destination) / destination.name
            backup.parent.mkdir(parents=True, exist_ok=True)
            if not backup.exists():
                shutil.copyfile(destination, backup)
        destination.write_text(text, encoding="utf-8")
        json_write(destination.parent / "Package_Inputs.json", {"version": VERSION,
                   "compiled_at_utc": datetime.now(timezone.utc).isoformat(),
                   "inputs": inputs, "package_sha256": digest(destination)})
    return {"project": project.name, "scenes": len(records), "inputs": len(inputs), "write": write}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["scaffold", "migrate", "upgrade", "compile", "prepare-planning", "scene-index", "sync-guides"])
    parser.add_argument("project", type=Path)
    parser.add_argument("--write", action="store_true", help="Without this flag, preview only")
    parser.add_argument("--adopt-existing", action="store_true", help="Explicitly mark preserved documents internally complete; does not approve research/publication")
    args = parser.parse_args()
    if args.adopt_existing and args.command not in ("scaffold", "migrate"):
        parser.error("--adopt-existing applies only to initial scaffold/migrate")
    if args.command in ('prepare-planning', 'scene-index', 'sync-guides'):
        from Tools.projects import planning_records
        action = {'prepare-planning': planning_records.prepare, 'scene-index': planning_records.build_index,
                  'sync-guides': planning_records.sync_guides}[args.command]
        result = action(args.project, write=args.write)
    elif args.command == "upgrade":
        result = upgrade(args.project, write=args.write)
    elif args.command == "compile":
        result = compile_package(args.project, write=args.write)
    else:
        result = scaffold(args.project, write=args.write, adopt=args.adopt_existing)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
