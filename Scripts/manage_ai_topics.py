"""Render/validate only niche 001. JSON is editable; --write changes its reading views.

Usage: python Scripts/manage_ai_topics.py [validate|render]
No source lookup, research certification, all-niche sync or production writes.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / 'topics/001_ai_technology_explainers'
REGISTRY = ROOT / 'REGISTRY/Niches/001_ai_technology_explainers'
MAIN = HOME / 'IN_DEPTH_TOPIC_BANK.md'
ROADMAP = HOME / '001_AI_TECHNOLOGY_EXPLAINERS_CHANNEL_TOPIC_ROADMAP.md'
LEVELS = {'foundation': 0, 'intermediate': 1, 'advanced': 2}


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def fingerprint(record, keys=None):
    value = {k: record[k] for k in keys} if keys else record
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def normalize(value):
    return ' '.join(re.findall(r'\w+', unicodedata.normalize('NFKC', value).casefold()))


def topics(bank):
    return [(c, t) for c in bank['categories'] for t in c['topics']]


def legacy_rows(status):
    return status['completed_topics'] + status['pending_topics'] + status['trending_topics']


def totals(bank):
    return {'categories': len(bank['categories']), 'proposed_topics': len(topics(bank))}


def reading_views(bank, status):
    records = topics(bank)
    by_id = {t['id']: t for c, t in records}
    count = len(records)
    intro = ['# 001 — AI + Technology Explainers: main topic bank', '',
        f"Updated: {bank['updated']}. **{count} active proposals · {len(bank['parent_categories'])} categories · {len(bank['categories'])} subcategories.** No topic quota or completeness claim.", '',
        'Each question below is a specific video proposal. Its scope states what that video would cover. Category and subcategory introductions are navigation, not additional episodes.', '',
        '**Proposal status:** sources have not been researched or verified for these bank records. Historical readiness/source notes in the separate registry idea bank retain their original meaning; this expansion does not promote any idea or certify any script.', '',
        '[Status and reconciliation report](TOPICS_COVERED_REPORT.md) · [Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Legacy status data](topics_status.json) · [Registry depth map](../../REGISTRY/Niches/001_ai_technology_explainers/Planning/TOPIC_MAP.md) · [Existing episode ideas](../../REGISTRY/Niches/001_ai_technology_explainers/IDEA_BANK.json)', '',
        '## Reading order', '',
        'Start with foundations in Categories 1–3. Continue through intermediate model, data and deployment explanations; finish with advanced evaluation, governance and frontier questions. Each subcategory lists prerequisites by stable CATALOG ID. Within it, topics run from foundation to advanced. IDs record identity, never learning order.', '',
        '| Category | Foundation | Intermediate | Advanced |', '|---|---:|---:|---:|']
    for p in bank['parent_categories']:
        selected = [(c, t) for c, t in records if c['parent_id'] == p['id']]
        counts = Counter(t.get('level', c['level']) for c, t in selected)
        intro.append(f"| [{p['title']}](#{p['id'].lower()}) | {counts['foundation']} | {counts['intermediate']} | {counts['advanced']} |")
    intro += ['', '**Suggested learning sequence across categories:**', '']
    for stage, refs in bank['reading_paths'].items():
        intro += [f"- **{stage.title()}:** " + ' → '.join(f"[{next(c['title'] for c in bank['categories'] if c['id'] == cid)}](#{cid.lower()})" for cid in refs) + '.']
    intro += ['', 'The legacy roadmap is cross-referenced at the end. Its 27 records and the 12 archived starter records are excluded from the active count, because they are source records or superseded umbrellas. Registry TOP and IDEA IDs remain separate planning references.', '',
        '## Scope of this niche', '', bank['niche_boundary'], '',
        'Topics about robots, agents and specialist systems explain mechanisms for a general viewer. Implementation tutorials, detailed engineering, research replication and medical or legal advice belong in their existing specialist homes. The all-niche index connects those neighboring proposal banks.', '']
    lines = intro
    for number, parent in enumerate(bank['parent_categories'], 1):
        lines += [f"<a id=\"{parent['id'].lower()}\"></a>", f"## Category {number}: {parent['title']}", '', parent['scope'], '']
        children = [c for c in bank['categories'] if c['parent_id'] == parent['id']]
        children.sort(key=lambda c: (min(LEVELS[t.get('level', c['level'])] for t in c['topics']), bank['categories'].index(c)))
        for category in children:
            lines += [f"<a id=\"{category['id'].lower()}\"></a>", f"### {category['title']}", '',
                f"Subcategory `{category['id']}` · Entry level: {category.get('reading_level', category['level'])} · Prerequisites: " + (', '.join(f"[{x}](#{x.lower()})" for x in category['prerequisites']) or 'None') + '.', '']
            ordered = sorted(category['topics'], key=lambda t: LEVELS[t.get('level', category['level'])])
            for t in ordered:
                level = t.get('level', category['level'])
                lines += [f"<a id=\"{t['id'].lower()}\"></a>", f"#### {t['id']} — {t.get('title', t['question'])}", '', f"Level: **{level}** · Status: proposed.", '']
                if t.get('title') and t['title'] != t['question']:
                    lines += [f"**Question:** {t['question']}", '']
                lines += [f"**Individual coverage scope:** {t['coverage']}", '']
                if t.get('additional_scope'):
                    lines += [f"**Scope extension:** {t['additional_scope']}", '']
                if t.get('exclusions'):
                    lines += [f"**Boundary:** {t['exclusions']}", '']
                if t.get('related_ids'):
                    lines += ['**Related coverage:** ' + ', '.join(f"[{x}](#{x.lower()})" for x in t['related_ids']) + '.', '']
                for followup in bank.get('research_followups',[]):
                    if followup['topic_id']==t['id']:
                        lines += [f"**Research follow-up:** [Case and source record]({followup['note_file']}) · `{followup['idea_id']}` in the [existing idea bank](../../REGISTRY/Niches/001_ai_technology_explainers/IDEA_BANK.json).",'']
                for ref in bank.get('editorial_cross_references',[]):
                    if ref['topic_id']==t['id']:
                        target=next((p for p in (ROOT/'topics').glob(ref['related_id'].split('-')[1]+'_*/IN_DEPTH_TOPIC_BANK.md')),None)
                        if target:
                            href='../'+target.parent.name+'/IN_DEPTH_TOPIC_BANK.md#'+ref['related_id'].lower()
                            lines += [f"**Neighboring scope:** [{ref['related_id']}]({href}) — {ref['boundary']}",'']
    if bank.get('starter_concept_crosswalk'):
        lines += ['## Starter subject coverage review','', 'Original starter records stay archived and outside the active count. These links identify the actual refined scopes covering each original subject.','']
        for c in bank['prior_initial_map']['categories']:
            for t in c['topics']:
                lines += [f"- `{t['id']}` — {t.get('title',t['question'])}: "+', '.join(f'[{ref}](#{ref.lower()})' for ref in bank['starter_concept_crosswalk'].get(t['id'],[]))+'.']
        lines += ['']
    lines += ['## Legacy roadmap crosswalk — preserved references, not extra proposals', '',
        'Original integer IDs, titles, slugs, queue/trend fields and questions remain in topics_status.json. Historic titles may assume a conclusion; the linked scopes define the actual inquiry. Old claims about search demand, technological inevitability or commercial outcomes are unverified wording, not findings.', '']
    for old in sorted(legacy_rows(status), key=lambda x: x['id']):
        title = old.get('title', old.get('concept'))
        lines += [f"### Legacy {old['id']:02d}: {title}", '']
        if old.get('question'):
            lines += [f"**Original question (preserved):** {old['question']}", '']
        if old.get('original_key_focus'):
            lines += [f"**Original planning focus:** {old['original_key_focus']}", '']
        lines += ['**Detailed proposals:** ' + ', '.join(f"[{x}](#{x.lower()})" for x in old['bank_ids']) + '.', '',
            f"**Reconciliation:** {old['reconciliation_note']}", '']
    lines += ['## Existing registry planning and questions', '',
        'The registry retains its eight TOP IDs, source references, series and three original IDEA questions. These records are not counted again as bank proposals.', '']
    depth = load(REGISTRY / 'Planning/DEPTH_PLAN.json')
    for t in depth['topics']:
        mapped = bank['registry_crosswalk'][t['topic_id']]
        lines += [f"- `{t['topic_id']}` — {t['title']}: " + ', '.join(f"[{i}](#{i.lower()})" for i in mapped) + '.']
    lines += ['']
    for idea in load(REGISTRY / 'IDEA_BANK.json')['ideas']:
        mapping = bank.get('registry_idea_crosswalk', {}).get(idea['idea_id'])
        suffix = (' Related proposals: ' + ', '.join(f"[{i}](#{i.lower()})" for i in mapping['bank_ids']) + '. ' + mapping['boundary']) if mapping else ''
        lines += [f"- `{idea['idea_id']}` — {idea['story_question']}{suffix}"]
    lines += ['', '[All-niche topic-bank index](../ALL_NICHE_TOPIC_BANKS.md) · [All-niche editorial review](../TOPIC_BANK_EDITORIAL_REVIEW.md)','']
    review=bank.get('editorial_review',{})
    if review:
        lines += ['', '## Editorial coverage review','',review['summary'],'',f"[Review evidence and decisions](../../{review['audit_file']})",'']
    lines += ['', '## Remaining open coverage', '']
    for gap in bank['open_coverage']:
        lines += [f"- **{gap['area']}:** {gap['next_step']}"]
    lines += ['', '## Preserved angle questions and launch proposal', '',
        'These historical planning questions and the launch route are retained for traceability. They do not authorize production or establish evidence. Current CAT defaults and registered angle files control any new project.', '',
        bank['legacy_angle_section'].replace('file:///h:/script-raw-/REGISTRY/Niches/001_ai_technology_explainers/ANGLE_PLAN.json', '../../REGISTRY/Niches/001_ai_technology_explainers/ANGLE_PLAN.json'), '',
        bank['legacy_launch_section'], '',
        '## Maintenance', '',
        'Edit IN_DEPTH_TOPIC_BANK.json for active proposals and topics_status.json for legacy status/crosswalk fields. Preserve BANK, CATALOG, TOP and IDEA IDs. Allocate a new BANK ID only for a distinct subject or testable question; revise scope or link related coverage when a new wording would repeat an existing proposal.', '',
        'Run `python Scripts/manage_ai_topics.py render`, then `python Scripts/manage_ai_topics.py validate` from the repository root. Rendering writes only the three niche 001 reading views. Validation checks identity, exact duplicates, preserved imports, cross-references, counts, prerequisites, reading-view freshness and local links; editorial similarity decisions are recorded separately and are not a proof of exhaustive semantic uniqueness.', '']
    roadmap = ['# 001 — Channel roadmap', '', '**Main reading file: [AI + Technology Explainers topic bank](IN_DEPTH_TOPIC_BANK.md).**', '',
        f"The reconciled bank has {count} active proposals arranged by category, subcategory and level. The original 27 roadmap records, all original questions and the launch proposal are preserved in its legacy crosswalk and in [status data](topics_status.json). They are not counted as additional episodes.", '',
        '[Execution status and reconciliation](TOPICS_COVERED_REPORT.md) · [Registry planning](../../REGISTRY/Niches/001_ai_technology_explainers/Planning/TOPIC_MAP.md)', '',
        'This file remains a compatibility entry point. No scripts, researched sources, production approvals or completed episodes were created by expanding the bank.', '']
    rec = bank['reconciliation']
    report = ['# 001 — Topic-bank status and reconciliation', '', '[Read the main topic bank](IN_DEPTH_TOPIC_BANK.md)', '',
        f"Updated: {bank['updated']}. Status: **proposals; coverage remains open**.", '',
        '| Record family | Count | Treatment |', '|---|---:|---|',
        f"| Active detailed video proposals | {count} | Counted once |",
        f"| Top-level categories / subcategories | {len(bank['parent_categories'])} / {len(bank['categories'])} | Navigation only |",
        f"| Imported active ZIP proposals | {len(rec['imported_records'])} | IDs, questions, scopes and original fields preserved |",
        f"| New proposals in this reconciliation | {count - len(rec['imported_records'])} | Individually scoped additions |",
        '| ZIP starter proposals | 12 | prior_initial_map retained; inactive and excluded |',
        '| Repository legacy roadmap records | 27 | Original IDs and fields preserved; linked to detailed proposals |',
        '| Registry depth topics / ideas / series | 8 / 3 / 1 | Existing records preserved; not extra bank proposals |',
        '| Completed episodes in status data | 0 | Existing completion status retained |',
        '| Sources verified for this expansion | 0 | No research or source verification performed |', '',
        '## Inputs and merge decisions', '',
        f"- Supplied archive: `{rec['archive_path']}`; SHA256 `{rec['archive_sha256']}`.",
        f"- Imported member: `{rec['archive_member']}`; SHA256 `{rec['imported_file_sha256']}`. ZIP member and supplied extracted file matched byte for byte before integration.",
        '- Read the archive instructions and inspected its niche 001 records and both patch path lists. The exported niche 001 bank was absent locally. Integrated its final JSON deliberately; neither broad patch was applied.',
        '- Existing repository roadmap, status data, registry TOP/IDEA/series records and angle definitions were inspected. Kept integer legacy IDs separate from BANK, CATALOG, TOP and IDEA IDs.',
        '- Old roadmap surveys overlap narrower ZIP entries. Linked each survey to detailed questions rather than importing it as an extra active episode. The original 20 roadmap questions and all 20 angle questions are retained. The seven legacy trend candidates retain their original fields with no assertion of current popularity.',
        '- Preserved the ZIP prior_initial_map and every imported active record. Added a category layer, levels, related-topic links and new subcategories without replacing original IDs/questions/scopes.',
        '- Left shared sources, CAT questions, existing ideas, registry depth files, other niches, bundle files and unrelated working-tree changes intact. The shared topics index changes only its niche 001 report cell.', '',
        '## Duplicate and progression review', '', bank['duplicate_review'], '',
        'Exact normalized questions and IDs are checked automatically. Related-but-distinct boundaries are recorded with topic links below each relevant question. Archived starter questions and legacy roadmap references are outside the active duplicate/count set. This does not claim mathematical detection of every semantic overlap.', '',
        '## Validation and limits', '',
        'Run `python Scripts/manage_ai_topics.py validate` for reproducible content checks. The command exits nonzero on errors and prints checked record/link counts. The generated views must match their JSON inputs.', '',
        'The repository-wide validator was run before edits and reported existing `Identity drift: 281_ayurveda` and `Output landing drift: 281_ayurveda`. Those unrelated findings were left unchanged. Existing depth-plan validation passed before this work.', '',
        'Final checks passed for niche-only validation, all five existing depth-planning tests, generated depth-view freshness, Python compilation and whitespace. The final repository-wide check retained the same two Ayurveda findings. In-memory negative checks confirmed rejection of duplicate questions, incorrect counts, missing crosswalk targets and prerequisite cycles. Pre-existing Ayurveda/helper/prompt edits were compared with the initial byte hashes and preserved; only the niche 001 row changed in the shared index.', '',
        'No new production project, research ledger, source-verification status, episode script or GitHub push is included.', '',
        '## Coverage still open', '']
    report += [f"- **{g['area']}:** {g['next_step']}" for g in bank['open_coverage']]
    report += ['', '## Supporting files', '',
        '- [Editable bank](IN_DEPTH_TOPIC_BANK.json): active proposals, archived starters, merge evidence and crosswalks.',
        '- [Legacy status](topics_status.json): original 27 records and bank references; original queue/trend fields are historical planning metadata.',
        '- [Compatibility roadmap](001_AI_TECHNOLOGY_EXPLAINERS_CHANNEL_TOPIC_ROADMAP.md): directs readers to the main file.',
        '- [Registry identity](../../REGISTRY/Niches/001_ai_technology_explainers/NICHE_001_ai_technology_explainers.md): existing supporting structure.', '']
    report += ['## Files changed by this work', '',
        '- [IN_DEPTH_TOPIC_BANK.md](IN_DEPTH_TOPIC_BANK.md) and [IN_DEPTH_TOPIC_BANK.json](IN_DEPTH_TOPIC_BANK.json): new reconciled main reading file and editable catalog.',
        '- [Original roadmap](001_AI_TECHNOLOGY_EXPLAINERS_CHANNEL_TOPIC_ROADMAP.md): compatibility entry point; original text is preserved in the catalog snapshot and main crosswalk.',
        '- [TOPICS_COVERED_REPORT.md](TOPICS_COVERED_REPORT.md) and [topics_status.json](topics_status.json): reconciliation, counts and legacy cross-references.',
        '- [Shared topics index](../README.md): niche 001 cell only; pre-existing changes to other cells retained.',
        '- [Niche 001 render/validator](../../Scripts/manage_ai_topics.py): targeted maintenance command; no all-niche writer was imported.', '']
    return {MAIN: '\n'.join(lines), ROADMAP: '\n'.join(roadmap), HOME / 'TOPICS_COVERED_REPORT.md': '\n'.join(report)}


def validate(bank, status, check_views=True):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
    records = topics(bank)
    ids = [t['id'] for c, t in records]
    by_id = {t['id']: t for c, t in records}
    categories = {c['id']: c for c in bank['categories']}
    parents = {p['id'] for p in bank['parent_categories']}
    require(bank['niche_id'] == status['niche_id'] == '001', 'Wrong niche')
    require(len(ids) == len(set(ids)), 'Duplicate BANK ID')
    require(len(categories) == len(bank['categories']), 'Duplicate subcategory ID')
    require(len(parents) == len(bank['parent_categories']), 'Duplicate parent ID')
    require(bank['counts'] == totals(bank), 'Stale bank counts')
    require(status['catalog_summary'] == {'active_proposals': len(ids), 'categories': len(parents), 'subcategories': len(categories), 'archived_starters': 12, 'legacy_references': 27}, 'Stale catalog summary')
    old = legacy_rows(status)
    require(len(old) == len({r['id'] for r in old}) == 27, 'Legacy ID/count drift')
    require(status['summary'] == {'completed': len(status['completed_topics']), 'pending': len(status['pending_topics']), 'trending': len(status['trending_topics']), 'total': len(old)}, 'Legacy summary mismatch')
    questions = [normalize(t['question']) for c, t in records]
    require(len(questions) == len(set(questions)), 'Duplicate normalized question')
    path_refs = [cid for refs in bank['reading_paths'].values() for cid in refs]
    require(len(path_refs) == len(set(path_refs)) and set(path_refs) == set(categories), 'Learning paths must cover each subcategory once')
    for c, t in records:
        require(bool(re.fullmatch(r'BANK-001-\d{3}', t['id'])), f"Bad topic ID {t['id']}")
        require(t.get('level', c['level']) in LEVELS, f"Bad level {t['id']}")
        require(bool(t['question'].strip()) and bool(t['coverage'].strip()), f"Missing question or scope {t['id']}")
        require(t['status'] == 'proposed' and t['verified_sources'] == [], f"Unsupported verification/status {t['id']}")
        for ref in t.get('related_ids', []):
            require(ref in by_id and ref != t['id'], f"Bad related ID {t['id']}: {ref}")
    for c in categories.values():
        require(bool(re.fullmatch(r'CATALOG-001-[DE]\d{2}', c['id'])), f"Bad subcategory ID {c['id']}")
        require(c['parent_id'] in parents and bool(c['topics']), f"Bad/empty category {c['id']}")
        require(c['research_profile'] in bank['research_profiles'], f"Bad profile {c['id']}")
        for ref in c['prerequisites']:
            require(ref in categories and ref != c['id'], f"Bad prerequisite {c['id']}: {ref}")
    starters={t['id'] for c in bank['prior_initial_map']['categories'] for t in c['topics']}
    for starter_id,refs in bank.get('starter_concept_crosswalk',{}).items():
        require(starter_id in starters and bool(refs) and all(ref in by_id for ref in refs),f'Bad starter crosswalk: {starter_id}')
    for ref in bank.get('editorial_cross_references',[]):
        paths=list((ROOT/'topics').glob(ref.get('related_id','').split('-')[1]+'_*/IN_DEPTH_TOPIC_BANK.json')) if re.fullmatch(r'BANK-\d{3}-\d{3,}',ref.get('related_id','')) else []
        targets={t['id'] for c in load(paths[0])['categories'] for t in c['topics']} if paths else set()
        require(ref.get('topic_id') in by_id and ref.get('related_id') in targets and bool(ref.get('boundary')), 'Bad editorial cross-reference')
    idea_ids={idea['idea_id'] for idea in load(REGISTRY/'IDEA_BANK.json')['ideas']}
    for idea_id, mapping in bank.get('registry_idea_crosswalk',{}).items():
        require(idea_id in idea_ids and bool(mapping.get('bank_ids'))
                and len(mapping['bank_ids'])==len(set(mapping['bank_ids']))
                and all(ref in by_id for ref in mapping['bank_ids'])
                and bool(mapping.get('boundary','').strip()),
                f'Bad registry IDEA crosswalk: {idea_id}')
    for followup in bank.get('research_followups',[]):
        note=HOME/followup.get('note_file','')
        require(followup.get('topic_id') in by_id and followup.get('idea_id') in idea_ids
                and note.resolve().is_relative_to(HOME.resolve()) and note.is_file(),
                'Bad research follow-up reference')
    active, done = set(), set()
    def visit(cid):
        if cid in active:
            errors.append(f'Prerequisite cycle: {cid}')
            return
        if cid in done or cid not in categories:
            return
        active.add(cid)
        for ref in categories[cid]['prerequisites']:
            visit(ref)
        active.remove(cid)
        done.add(cid)
    for cid in categories:
        visit(cid)
    for tid, expected in bank['reconciliation']['imported_records'].items():
        require(tid in by_id and fingerprint(by_id[tid], expected['keys']) == expected['sha256'], f'Imported record changed: {tid}')
    initial = bank['prior_initial_map']
    require(fingerprint(initial) == bank['reconciliation']['prior_initial_map_sha256'], 'Archived starter map changed')
    for r in old:
        expected = bank['reconciliation']['legacy_records'][str(r['id'])]
        require(fingerprint(r, expected['keys']) == expected['sha256'], f"Legacy record changed: {r['id']}")
        require(bool(r['bank_ids']) and len(r['bank_ids']) == len(set(r['bank_ids'])) and all(i in by_id for i in r['bank_ids']), f"Unresolved/duplicate legacy reference {r['id']}")
    require(set(bank['registry_crosswalk']) == {t['topic_id'] for t in load(REGISTRY / 'Planning/DEPTH_PLAN.json')['topics']}, 'Registry TOP crosswalk drift')
    for tid, refs in bank['registry_crosswalk'].items():
        require(bool(refs) and all(i in by_id for i in refs), f'Bad registry crosswalk {tid}')
    for rel, sha in bank['reconciliation']['preserved_registry_files'].items():
        actual=(ROOT/rel).read_bytes()
        if rel=='REGISTRY/Niches/001_ai_technology_explainers/IDEA_BANK.json' and hashlib.sha256(actual).hexdigest()!=sha:
            # A new linked idea is allowed, while every pre-existing idea and
            # the original serialized bank must remain byte-equivalent.
            ideas=load(ROOT/rel)
            additions={x['idea_id'] for x in bank.get('research_followups',[])}
            require(all(i in {idea['idea_id'] for idea in ideas['ideas']} for i in additions), 'Missing linked research idea')
            ideas['ideas']=[idea for idea in ideas['ideas'] if idea['idea_id'] not in additions]
            preserved=(json.dumps(ideas,ensure_ascii=False,indent=2)+'\n').replace('\n','\r\n').encode('utf-8')
            require(hashlib.sha256(preserved).hexdigest()==sha,f'Preserved registry file changed: {rel}')
        else:
            require(hashlib.sha256(actual).hexdigest()==sha,f'Preserved registry file changed: {rel}')
    views = reading_views(bank, status)
    link_count = 0
    for path, content in views.items():
        if check_views:
            require(path.is_file() and path.read_text(encoding='utf-8') == content, f'Stale reading view: {path.name}')
        anchors = set(re.findall(r'<a id="([^"]+)"', content))
        for target in re.findall(r'\]\(([^)]+)\)', content):
            target = unquote(target.split(' "')[0])
            if target.startswith(('https://', 'http://', 'mailto:')):
                continue
            link_count += 1
            filename, _, fragment = target.partition('#')
            if filename:
                target_path = path.parent / filename
                require(target_path.exists() or target_path in views, f'Broken local link in {path.name}: {target}')
            else:
                require(fragment in anchors, f'Broken anchor in {path.name}: {target}')
    return errors, link_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['render', 'validate'], default='validate', nargs='?')
    args = parser.parse_args()
    bank, status = load(HOME / 'IN_DEPTH_TOPIC_BANK.json'), load(HOME / 'topics_status.json')
    errors, links = validate(bank, status, check_views=args.command == 'validate')
    if errors:
        raise SystemExit('\n'.join(errors))
    if args.command == 'render':
        for path, content in reading_views(bank, status).items():
            path.write_text(content, encoding='utf-8')
        print('Rendered 3 reading views for niche 001 only.')
    else:
        print(f"PASS: {len(topics(bank))} active proposals, {len(bank['categories'])} subcategories, {links} local links; preserved 121 imported records, 27 legacy records and registry supporting files. No source verification claimed.")
