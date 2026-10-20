"""Validate optional niche depth plans and build their Markdown reading views."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from Tools.projects.idea_bank import catalog, taxonomy, valid_date


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_and_validate():
    errors = []
    plans = []
    sources = {}
    try:
        library = read(ROOT / "REGISTRY/SOURCE_LIBRARY.json")
        if library.get("schema_version") != "1.0":
            errors.append("Unknown source library version")
        for s in library["sources"]:
            sid = s["source_id"]
            if sid in sources or not re.fullmatch(r"SRC-\d{4}", sid):
                errors.append(f"Invalid/duplicate source ID: {sid}")
            sources[sid] = s
            for field in ("title", "publisher", "url", "edition", "locator", "access_note", "limitations", "rights_note", "refresh_trigger"):
                if not isinstance(s.get(field), str) or not s[field].strip():
                    errors.append(f"{sid}: missing {field}")
            if not re.match(r"https?://[^/\s]+", s.get("url", "")) or not valid_date(s.get("last_attempt_date")):
                errors.append(f"{sid}: invalid URL/access attempt date")
            if s.get("status") not in {"checked", "unverified"}:
                errors.append(f"{sid}: invalid access status")
            if s.get("status") == "checked" and (not valid_date(s.get("checked_date")) or s["checked_date"] > s["last_attempt_date"]):
                errors.append(f"{sid}: checked source needs a valid check date")
            if s.get("status") == "unverified" and s.get("checked_date") is not None:
                errors.append(f"{sid}: unverified source must have null checked_date")
        entries, idea_errors = catalog()
        ideas = {iid: idea for iid, (row, idea) in entries.items()}
        errors.extend(idea_errors)
        rows = taxonomy()
        for path in sorted((ROOT / "REGISTRY/Niches").glob("*/Planning/DEPTH_PLAN.json")):
            p = read(path)
            nid = p["niche_id"]
            if p.get("schema_version") != "1.0" or nid not in rows or path.parent.parent != ROOT / rows[nid]["niche_path"]:
                errors.append(f"Invalid depth plan identity: {path}")
                continue
            for field in ("audience", "boundary", "production_handoff"):
                if not isinstance(p.get(field), str) or not p[field].strip():
                    errors.append(f"{nid}: missing {field}")
            if not valid_date(p.get("updated_date")):
                errors.append(f"{nid}: invalid update date")
            topics = {t["topic_id"]: t for t in p["topics"]}
            if not topics or len(topics) != len(p["topics"]):
                errors.append(f"{nid}: missing/duplicate topics")
            angles = {a["slug"] for a in read(path.parent.parent / "ANGLE_PLAN.json")["angles"]}
            mapped = set()
            for tid, t in topics.items():
                if not re.fullmatch(rf"TOP-{nid}-\d{{3}}", tid):
                    errors.append(f"{nid}: invalid topic ID {tid}")
                for f in ("title", "coverage", "evidence_required", "exclusions", "next_action"):
                    if not isinstance(t.get(f), str) or not t[f].strip():
                        errors.append(f"{tid}: missing {f}")
                if t.get("level") not in {"foundation", "intermediate", "advanced"}:
                    errors.append(f"{tid}: invalid level")
                if not t["angle_slugs"] or any(a not in angles for a in t["angle_slugs"]):
                    errors.append(f"{tid}: unregistered angle")
                if any(x not in topics or x == tid for x in t["prerequisites"]):
                    errors.append(f"{tid}: invalid prerequisite")
                if any(s not in sources for s in t["source_ids"]):
                    errors.append(f"{tid}: unknown source")
                for iid in t["idea_ids"]:
                    idea = ideas.get(iid)
                    if not idea or idea["niche_id"] != nid or idea["topic"] != t["title"] or idea["angle_slug"] not in t["angle_slugs"]:
                        errors.append(f"{tid}: idea/topic/angle mismatch: {iid}")
                        continue
                    if iid in mapped:
                        errors.append(f"{iid}: mapped to multiple primary topics")
                    mapped.add(iid)
                    for candidate in idea["source_candidates"]:
                        matches = [sources[s] for s in t["source_ids"] if s in sources and sources[s]["url"] == candidate["url"]]
                        if not matches or (candidate["status"] == "checked" and not any(s["status"] == "checked" for s in matches)):
                            errors.append(f"{iid}: source not represented by topic library references")
            active, done = set(), set()
            def visit(tid):
                if tid in active:
                    errors.append(f"{nid}: prerequisite cycle at {tid}")
                    return
                if tid in done or tid not in topics:
                    return
                active.add(tid)
                for dependency in topics[tid]["prerequisites"]:
                    visit(dependency)
                active.remove(tid)
                done.add(tid)
            for tid in topics:
                visit(tid)
            series_ids = set()
            for series in p["series"]:
                sid = series["series_id"]
                if sid in series_ids or not re.fullmatch(rf"SER-{nid}-\d{{3}}", sid):
                    errors.append(f"{nid}: duplicate/invalid series ID")
                series_ids.add(sid)
                for f in ("title", "learning_outcome", "ordering_reason", "entry_requirement"):
                    if not isinstance(series.get(f), str) or not series[f].strip():
                        errors.append(f"{sid}: missing {f}")
                order = series["idea_ids"]
                if not order or len(order) != len(set(order)) or any(i not in mapped for i in order):
                    errors.append(f"{sid}: missing/duplicate/unmapped idea")
            plans.append((path, p))
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        errors.append(f"Depth planning data error: {exc}")
    return plans, sources, errors


def outputs(plans, sources):
    views = {}
    index = ["# Content depth pilot", "", f"{len(plans)} niches with depth plans; optional planning can be extended after editorial review. These maps describe planned coverage, not researched completeness.", "", "[Planning guide](DEPTH_PLANNING_GUIDE.md) · [Source library](SOURCE_LIBRARY.md) · [Idea index](IDEA_MASTER_LIST.md)", "", "| Niche | Topics | Ideas mapped | Series | Planning views |", "|---|---:|---:|---:|---|"]
    entries, _ = catalog()
    ideas = {iid: idea for iid, (row, idea) in entries.items()}
    rows = taxonomy()
    for path, p in plans:
        nid = p["niche_id"]
        home = rows[nid]["niche_path"].removeprefix("REGISTRY/")
        topics = p["topics"]
        index.append(f"| {nid} {rows[nid]['title']} | {len(topics)} | {sum(len(t['idea_ids']) for t in topics)} | {len(p['series'])} | [Topics]({home}/Planning/TOPIC_MAP.md) · [Series]({home}/Planning/SERIES_PLAN.md) |")
        lines = [f"# {nid} topic coverage map", "", "Generated from DEPTH_PLAN.json. Topic IDs are planning references; they add no CONFIG question and do not replace registered angles.", "", f"Audience: {p['audience']}", "", f"Niche boundary: {p['boundary']}", "", f"Production handoff: {p['production_handoff']}", ""]
        for t in topics:
            lines += [f"## {t['topic_id']} — {t['title']}", "", f"Level: {t['level']}. Prerequisites: {', '.join(t['prerequisites']) or 'None'}.", "", f"Coverage: {t['coverage']}", "", f"Exclusions: {t['exclusions']}", "", f"Evidence required: {t['evidence_required']}", "", f"Registered angles: {', '.join(t['angle_slugs'])}.", "", f"Sources: {', '.join(t['source_ids']) or 'Discovery required'}; see [shared library](../../../SOURCE_LIBRARY.md).", "", "Ideas: " + (", ".join(f"{i} ({ideas[i]['status']})" for i in t["idea_ids"]) or "No concrete idea recorded; coverage remains open."), "", f"Next action: {t['next_action']}", ""]
        views[path.parent / "TOPIC_MAP.md"] = "\n".join(lines) + "\n"
        lines = [f"# {nid} series plan", "", "Proposed editorial order only. An idea's live status controls project eligibility; series membership cannot bypass readiness.", ""]
        for s in p["series"]:
            lines += [f"## {s['series_id']} — {s['title']}", "", f"Entry requirement: {s['entry_requirement']}", "", f"Learning outcome: {s['learning_outcome']}", "", f"Ordering reason: {s['ordering_reason']}", ""]
            for number, iid in enumerate(s["idea_ids"], 1):
                idea = ideas[iid]
                lines += [f"{number}. **{iid}** — {idea['working_title']} ({idea['status']}). {idea['story_question']}"]
            lines += ["", "Create eligible episodes through the existing --idea-id route; claim ledgers and risk review still apply. AI generation happens after the scene/prompt package handoff.", ""]
        views[path.parent / "SERIES_PLAN.md"] = "\n".join(lines) + "\n"
    views[ROOT / "REGISTRY/DEPTH_MASTER_LIST.md"] = "\n".join(index) + "\n"
    lines = ["# Shared source library", "", "Source discovery and access feasibility only. No library entry verifies an episode claim or grants media reuse rights. Edit SOURCE_LIBRARY.json, then rebuild this view.", ""]
    for sid, s in sorted(sources.items()):
        lines += [f"## {sid} — {s['title']}", "", f"Publisher: {s['publisher']}. Edition/context: {s['edition']}.", "", f"[Source]({s['url']})", "", f"Access: {s['status']}; checked: {s['checked_date'] or 'not confirmed'}; last attempt: {s['last_attempt_date']}.", "", f"Inspected/attempted: {s['access_note']}", "", f"Research locator: {s['locator']}", "", f"Limits: {s['limitations']}", "", f"Rights: {s['rights_note']}", "", f"Recheck when: {s['refresh_trigger']}", ""]
    views[ROOT / "REGISTRY/SOURCE_LIBRARY.md"] = "\n".join(lines) + "\n"
    return views


def validate():
    plans, sources, errors = load_and_validate()
    if not errors:
        for path, content in outputs(plans, sources).items():
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                errors.append(f"Missing/stale depth view: {path.relative_to(ROOT)}; run Tools/depth_planning.py build-index")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate", "build-index"])
    args = parser.parse_args()
    if args.command == "build-index":
        plans, sources, errors = load_and_validate()
        if errors:
            raise SystemExit("\n".join(errors))
        for path, content in outputs(plans, sources).items():
            path.write_text(content, encoding="utf-8")
        print(f"Built depth views for {len(plans)} niches and {len(sources)} source references")
    else:
        errors = validate()
        if errors:
            raise SystemExit("\n".join(errors))
        print("Depth topic, idea, series, source references and generated views agree")
