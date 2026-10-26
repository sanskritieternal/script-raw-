"""Reconcile, render and check local topic banks without changing production records.

bootstrap: import missing ZIP banks and capture current local files before any edits.
apply --input PATH: append authored {niche:[{parent,title,level,topics}]} groups.
render --start N --end N: regenerate targeted reading views.
check: validate all available banks; --report PATH saves machine-readable findings.
index: rebuild the bank index and change only bank links in existing niche index rows.
"""
import argparse
from collections import Counter, defaultdict
import copy
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import time
import unicodedata
import uuid
from urllib.parse import unquote
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / 'topics'
BUNDLE = ROOT / 'Youtube bank topic/YouTube-Topic-Banks-All-550-Niches'
ARCHIVE = Path(str(BUNDLE) + '.zip')
LEVELS = {'foundation': 0, 'intermediate': 1, 'advanced': 2}


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, value):
    save_bytes(path,(json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8'))


def save_bytes(path,content):
    """Atomic writes with brief retry for transient Windows volume/open-handle errors."""
    error=None
    for attempt in range(6):
        temporary=path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp')
        try:
            temporary.write_bytes(content)
            os.replace(temporary,path)
            return
        except OSError as exc:
            error=exc
            temporary.unlink(missing_ok=True)
            time.sleep(0.1*(attempt+1))
    raise error


def sha(value):
    return hashlib.sha256(value).hexdigest()


def fingerprint(value):
    return sha(json.dumps(value, sort_keys=True, ensure_ascii=False).encode())


def norm(value):
    return ' '.join(re.findall(r'\w+', unicodedata.normalize('NFKC', value).casefold()))


def table(value):
    return str(value).replace('|', '&#124;').replace('\r', '').replace('\n', ' ')


def rows():
    with (ROOT / 'REGISTRY/NICHE_TAXONOMY.csv').open(encoding='utf-8', newline='') as handle:
        return {r['id']: r for r in csv.DictReader(handle)}


def home(nid):
    row = rows()[nid]
    return TOPICS / f"{nid}_{row['slug']}"


def records(bank):
    return [(c, t) for c in bank['categories'] for t in c['topics']]


def topic_href(nid,topic_id):
    other=topic_id.split('-')[1]
    return '#'+topic_id.lower() if other==nid else f'../{home(other).name}/IN_DEPTH_TOPIC_BANK.md#{topic_id.lower()}'


def snapshot(path):
    raw = path.read_bytes()
    return {'sha256': sha(raw), 'original_text': raw.decode('utf-8-sig')}


def legacy_records(status):
    """Preserve source containers, including nonstandard local catalog structures."""
    found = []
    def walk(value, route):
        if isinstance(value, dict):
            if any(isinstance(value.get(k), str) and value[k].strip() for k in ('title', 'concept', 'question', 'story_question')):
                found.append((route, value))
            for key, child in value.items():
                if isinstance(child, (dict, list)):
                    walk(child, route + '/' + key)
        elif isinstance(value, list):
            for i, child in enumerate(value):
                walk(child, route + f'/{i}')
        elif isinstance(value,str) and re.search(r'/topics/\d+$',route):
            found.append((route,{'title':value,'source_kind':'existing_topic_title'}))
    for key, value in status.items():
        if isinstance(value, list):
            walk(value, key)
    return found


def roadmap_questions(text):
    found = {}
    pattern = r'(\d+)\.\s+\*\*([^\n]+?)\*\*\s*\n\s*-\s*\*Question:\*\s*([^\n]+)\n\s*-\s*\*Key Focus:\*\s*([^\n]+)'
    for number, title, question, focus in re.findall(pattern, text):
        found[int(number)] = {'title': title.strip(), 'question': question.strip(), 'coverage': focus.strip()}
    return found


def bootstrap(start, end):
    tax = rows()
    archive_sha = sha(ARCHIVE.read_bytes())
    count = 0
    with zipfile.ZipFile(ARCHIVE) as archive:
        manifest = json.loads(archive.read('SHA256.json'))
        for number in range(max(2, start), end + 1):
            nid = f'{number:03d}'
            directory = home(nid)
            path = directory / 'IN_DEPTH_TOPIC_BANK.json'
            if path.exists():
                existing = read(path)
                if existing.get('local_reconciliation'):
                    continue
                raise ValueError(f'Reconcile existing unrecognized bank deliberately: {path}')
            member = f'files/topics/{directory.name}/IN_DEPTH_TOPIC_BANK.json'
            raw = archive.read(member)
            assert sha(raw) == manifest[member.removeprefix('files/')], member
            assert raw == (BUNDLE / member).read_bytes(), f'Extracted/ZIP mismatch: {nid}'
            bank = json.loads(raw)
            assert bank['niche_id'] == nid and bank['slug'] == tax[nid]['slug']
            local_files = {}
            for local in directory.iterdir():
                if local.is_file() and local.suffix in {'.md', '.json'}:
                    local_files[local.name] = snapshot(local)
            bank['local_reconciliation'] = {
                'date': '2026-10-23', 'archive_path': ARCHIVE.relative_to(ROOT).as_posix(),
                'archive_sha256': archive_sha, 'member': member, 'member_sha256': sha(raw),
                'source_kind': bank.get('bank_type','detailed_pilot'),
                'source_records': {t['id']: {'keys': list(t), 'sha256': fingerprint(t)} for c, t in records(bank)},
                'source_categories': {c['id']: {'keys': [k for k in c if k != 'topics'], 'sha256': fingerprint({k:v for k,v in c.items() if k != 'topics'})} for c in bank['categories']},
                'source_initial_archive_sha256': fingerprint(bank['prior_initial_map']) if 'prior_initial_map' in bank else None,
                'local_files': local_files,
                'local_status_original': read(directory / 'topics_status.json'),
                'merge_policy': 'Preserve source detailed records and existing local status fields. Archive boilerplate starter maps before authored expansion. Legacy proposal counts remain a separate family; no source or completion certification is added.'
            }
            bank.setdefault('bank_type','detailed_pilot')
            bank['integration_stage'] = 'imported_detailed_draft' if bank['bank_type'] != 'subject_map' else 'initial_map_awaiting_authored_expansion'
            bank['local_authored_inputs'] = []
            ensure_parents(bank)
            write(path, bank)
            count += 1
    print(f'Imported {count} missing banks; no legacy files overwritten.')


def ensure_parents(bank):
    if bank.get('parent_categories'):
        return
    bank['parent_categories'] = []
    for number, c in enumerate(bank['categories'], 1):
        pid = f"DOMAIN-{bank['niche_id']}-{number:02d}"
        bank['parent_categories'].append({'id':pid, 'title':c['title'], 'scope':'Subject coverage grouped for learning; topic scopes below define the individual video boundaries.'})
        c['parent_id'] = pid
        c['reading_subcategory'] = 'Core questions and distinctions'


def max_topic_id(bank):
    values = [int(t['id'].rsplit('-', 1)[1]) for c, t in records(bank)]
    if bank.get('prior_initial_map'):
        values += [int(t['id'].rsplit('-', 1)[1]) for c in bank['prior_initial_map']['categories'] for t in c['topics']]
    values += [int(t['id'].rsplit('-',1)[1]) for key in ('archived_local_frameworks','retired_duplicate_proposals') for t in bank.get(key,[])]
    return max(values, default=0)


def apply(input_path):
    updates = read(input_path)
    changed = []
    for nid, payload in updates.items():
        groups=payload.get('groups',[]) if isinstance(payload,dict) else payload
        assert nid != '001' and nid in rows(), nid
        directory = home(nid)
        path = directory / 'IN_DEPTH_TOPIC_BANK.json'
        bank = read(path)
        assert bank.get('local_reconciliation'), f'Bootstrap first: {nid}'
        if not groups:
            continue
        next_id = max_topic_id(bank) + 1
        if bank['bank_type'] == 'subject_map':
            original = copy.deepcopy(bank)
            for key in ('local_reconciliation','integration_stage','local_authored_inputs','parent_categories'):
                original.pop(key, None)
            for c in original['categories']:
                c.pop('parent_id', None)
                c.pop('reading_subcategory', None)
            # Reconstruct the immutable ZIP source, preserving its exact original data.
            with zipfile.ZipFile(ARCHIVE) as archive:
                original = json.loads(archive.read(bank['local_reconciliation']['member']))
            bank['prior_initial_map'] = original
            bank['categories'] = []
            bank['parent_categories'] = []
            bank['bank_type'] = 'detailed_expansion'
        ensure_parents(bank)
        existing = {norm(t['question']): t for c,t in records(bank)}
        retired_questions={norm(t['question']):t for t in bank.get('retired_duplicate_proposals',[])}
        parents = {p['title']: p['id'] for p in bank['parent_categories']}
        for group in groups:
            assert group['level'] in LEVELS and group['topics'], (nid, group)
            parent_title = group['parent']
            if parent_title not in parents:
                parent_number=max((int(re.search(r'\d+$',p['id']).group()) for p in bank['parent_categories'] if re.search(r'\d+$',p['id'])),default=0)+1
                pid = f"DOMAIN-{nid}-{parent_number:02d}"
                parents[parent_title] = pid
                bank['parent_categories'].append({'id':pid, 'title':parent_title, 'scope':group.get('parent_scope', 'Individual proposals below define the subjects and limits of this branch.')})
            identity = fingerprint([parent_title, group['title'], group['level']])
            category = next((c for c in bank['categories'] if c.get('local_group_identity') == identity), None)
            if category is None:
                used = {c['id'] for c in bank['categories']}
                index = 1
                while f'CATALOG-{nid}-R{index:02d}' in used:
                    index += 1
                profiles = bank['research_profiles']
                profile = group.get('research_profile') or ('synthesis' if 'synthesis' in profiles else next(iter(profiles)))
                assert profile in profiles
                category = {'id':f'CATALOG-{nid}-R{index:02d}', 'title':group['title'], 'level':group['level'],
                    'parent_id':parents[parent_title], 'research_profile':profile, 'prerequisites':[],
                    'local_group_identity':identity, 'topics':[]}
                bank['categories'].append(category)
            for proposal in group['topics']:
                assert proposal['question'].strip() and proposal['coverage'].strip()
                key = norm(proposal['question'])
                if key in retired_questions:
                    continue
                if key in existing:
                    assert existing[key]['coverage'] == proposal['coverage'], f'Differing duplicate question: {nid}: {key}'
                    if proposal.get('covers_starter_ids'):
                        existing[key]['covers_starter_ids']=list(dict.fromkeys(existing[key].get('covers_starter_ids',[])+proposal['covers_starter_ids']))
                    continue
                topic = dict(proposal)
                topic.update(id=f'BANK-{nid}-{next_id:03d}', angle=None, status='proposed', verified_sources=[])
                category['topics'].append(topic)
                existing[key] = topic
                next_id += 1
        protected_categories=set(bank['local_reconciliation']['source_categories']) if bank['local_reconciliation']['source_kind']!='subject_map' else set()
        bank['categories'] = [c for c in bank['categories'] if c['topics'] or c['id'] in protected_categories]
        if isinstance(payload,dict) and payload.get('open_coverage') is not None:
            bank['open_coverage']=payload['open_coverage']
        crosswalk=bank.setdefault('starter_concept_crosswalk',{})
        for c,t in records(bank):
            for old_id in t.get('covers_starter_ids',[]):
                targets=crosswalk.setdefault(old_id,[])
                if t['id'] not in targets:targets.append(t['id'])
        used_parents = {c['parent_id'] for c in bank['categories']}
        bank['parent_categories'] = [p for p in bank['parent_categories'] if p['id'] in used_parents]
        bank['counts'] = {'categories':len(bank['categories']), 'proposed_topics':len(records(bank))}
        bank['updated'] = '2026-10-23'
        bank['integration_stage'] = 'authored_expansion_prepared_coverage_open'
        bank['editorial_depth'] = 'individually_scoped_authored_proposals'
        bank['coverage_review'] = {'status':'open_for_further_substantive_expansion', 'fixed_topic_target':None,
            'topic_cap':None, 'source_verification':'not_performed', 'exhaustive_coverage_claimed':False}
        marker = {'input':str(input_path.relative_to(ROOT)) if input_path.is_relative_to(ROOT) else input_path.name, 'sha256':fingerprint(groups)}
        if marker not in bank['local_authored_inputs']:
            bank['local_authored_inputs'].append(marker)
        write(path, bank)
        errors = check_bank(bank, directory)
        assert not errors, '\n'.join(errors)
        render(bank, directory)
        changed.append(nid)
    print(f'Applied/rendered authored input for {len(changed)} niches: ' + ', '.join(changed))


def adopt_legacy(start,end):
    """Reconcile stronger existing local proposals before adding fresh subject coverage."""
    pending={};routes={};no_questions=[]
    for number in range(max(start,2),end+1):
        nid=f'{number:03d}';directory=home(nid);b=read(directory/'IN_DEPTH_TOPIC_BANK.json')
        rec=b['local_reconciliation']
        if rec['source_kind']!='subject_map' or b.get('local_roadmap_adoptions'):
            continue
        # Only pre-agent starter banks are eligible; never reorder an active authored bank.
        if b['bank_type']!='subject_map':continue
        name=next((n for n in rec['local_files'] if n.endswith('_CHANNEL_TOPIC_ROADMAP.md')),None)
        qs=roadmap_questions(rec['local_files'][name]['original_text']) if name else {}
        if not qs:
            no_questions.append(nid);continue
        original_status=rec['local_status_original']
        old_by_id={t['id']:t for route,t in legacy_records(original_status) if isinstance(t.get('id'),int)}
        groups={}
        for number,q in qs.items():
            old=old_by_id.get(number,{})
            tier=old.get('tier','Original subject progression')
            match=re.search(r'Tier\s*(\d)',tier,re.I)
            depth=int(match.group(1)) if match else (1 if number<=4 else 2 if number<=14 else 4)
            level='foundation' if depth==1 else 'intermediate' if depth in (2,3) else 'advanced'
            # The original tier name supplies a subject-specific curriculum branch where available.
            key=(tier,level)
            group=groups.setdefault(key,{'parent':tier,'title':'Original bounded cases and mechanisms','level':level,'topics':[]})
            group['topics'].append({**q,'origin':'repository_roadmap','legacy_source_id':number,
                'framing_note':'Original proposal wording preserved. Investigate its premises; no factual verification or current trend assessment is implied.'})
        pending[nid]=list(groups.values());routes[nid]=set(qs)
    scratch=ROOT/'Scripts/topic_expansion_inputs'
    scratch.mkdir(exist_ok=True)
    path=scratch/'adopt_existing_local_roadmaps.json'
    write(path,pending)
    apply(path)
    for nid in pending:
        directory=home(nid);path=directory/'IN_DEPTH_TOPIC_BANK.json';b=read(path)
        b['local_roadmap_adoptions']=[t['id'] for c,t in records(b) if t.get('origin')=='repository_roadmap']
        b['integration_stage']='local_roadmap_reconciled_additional_expansion_pending'
        write(path,b);render(b,directory)
    print(f'Adopted existing bounded local proposals for {len(pending)} niches; manual cases {no_questions}.')


def check_bank(bank, directory):
    errors = []
    def need(ok, message):
        if not ok:
            errors.append(f"{bank['niche_id']}: {message}")
    nid = bank['niche_id']
    need(directory.name == f"{nid}_{bank['slug']}", 'identity/path mismatch')
    rs = records(bank)
    need(bool(rs),'no active scoped proposals yet')
    ids = [t['id'] for c,t in rs]
    questions = [norm(t['question']) for c,t in rs]
    need(len(ids) == len(set(ids)), 'duplicate BANK ID')
    need(len(questions) == len(set(questions)), 'duplicate normalized question')
    archived_ids=[t['id'] for key in ('archived_local_frameworks','retired_duplicate_proposals') for t in bank.get(key,[])]
    need(len(archived_ids)==len(set(archived_ids)) and not(set(archived_ids)&set(ids)),'archived framework ID reused')
    need(bank['counts'] == {'categories':len(bank['categories']), 'proposed_topics':len(rs)}, 'count mismatch')
    cs = {c['id']: c for c in bank['categories']}
    need(len(cs) == len(bank['categories']), 'duplicate subcategory ID')
    ps = {p['id']:p for p in bank['parent_categories']}
    need(len(ps) == len(bank['parent_categories']), 'duplicate parent ID')
    angles = {a['slug'] for a in read(ROOT / 'REGISTRY/Niches' / directory.name / 'ANGLE_PLAN.json')['angles']}
    for c,t in rs:
        need(c['level'] in LEVELS and c['parent_id'] in ps, f"bad level/parent {c['id']}")
        need(t.get('level',c['level']) in LEVELS, f"bad topic level {t['id']}")
        need(bool(re.fullmatch(rf'BANK-{nid}-\d{{3,}}',t['id'])), f"invalid topic ID {t['id']}")
        need(bool(t['question'].strip()) and bool(t['coverage'].strip()), f"missing question/scope {t['id']}")
        need(t['status']=='proposed' and t['verified_sources']==[], f"unsupported readiness/sources {t['id']}")
        need(t.get('angle') is None or t['angle'] in angles, f"unregistered angle {t['id']}")
        for ref in t.get('related_ids',[]):
            need(ref in ids+archived_ids and ref!=t['id'],f"bad related reference {t['id']}")
    old_ids={t['id'] for c in bank.get('prior_initial_map',{}).get('categories',[]) for t in c['topics']}
    def target_exists(tid):
        if tid in ids:return True
        match=re.fullmatch(r'BANK-(\d{3})-\d{3,}',tid)
        if not match or match.group(1)==nid or match.group(1) not in rows():return False
        target=home(match.group(1))/'IN_DEPTH_TOPIC_BANK.json'
        return target.exists() and any(t['id']==tid for c,t in records(read(target)))
    for old,targets in bank.get('starter_concept_crosswalk',{}).items():
        need(old in old_ids and bool(targets) and all(target_exists(t) for t in targets),f'bad starter coverage crosswalk {old}')
    for ref in bank.get('editorial_cross_references',[]):
        need(ref.get('topic_id') in ids and target_exists(ref.get('related_id',''))
             and ref.get('topic_id')!=ref.get('related_id') and bool(ref.get('boundary','').strip()),
             'invalid editorial cross-reference')
    for followup in bank.get('research_followups',[]):
        relative=followup.get('note_file','')
        if not isinstance(relative,str) or not relative:
            need(False,'invalid research follow-up path')
            continue
        note=directory/relative
        need(followup.get('topic_id') in ids and isinstance(relative,str)
             and note.resolve().is_relative_to(directory.resolve()) and note.is_file(),
             'invalid research follow-up')
        if note.is_file():
            for href in re.findall(r'\]\(([^)]+)\)',note.read_text(encoding='utf-8')):
                if href.startswith(('https://','http://','mailto:','#')):
                    continue
                local=note.parent/unquote(href.partition('#')[0])
                need(local.exists(),f'broken research-note link: {relative}: {href}')
    legacy_routes={route for route,t in legacy_records(bank['local_reconciliation']['local_status_original'])}
    for route,review in bank.get('legacy_topic_crosswalk',{}).items():
        need(route in legacy_routes and bool(review.get('reason')) and bool(review.get('decision'))
             and all(target_exists(t) for t in review.get('bank_ids',[])), 'invalid legacy editorial crosswalk')
    for t in bank.get('retired_duplicate_proposals',[]):
        need(t.get('duplicate_of')!=t['id'] and target_exists(t.get('duplicate_of','')),f"bad duplicate primary {t['id']}")
    active,done=set(),set()
    def visit(cid):
        if cid in active:
            errors.append(f'{nid}: prerequisite cycle at {cid}')
            return
        if cid in done or cid not in cs:
            return
        active.add(cid)
        for ref in cs[cid]['prerequisites']:
            need(ref in cs and ref!=cid,f'bad prerequisite {cid}: {ref}')
            visit(ref)
        active.remove(cid);done.add(cid)
    for cid in cs:visit(cid)
    rec = bank['local_reconciliation']
    original_topics = {t['id']:t for c,t in rs}
    original_topics.update({t['id']:t for t in bank.get('retired_duplicate_proposals',[])})
    if rec['source_kind']=='subject_map' and bank['bank_type']!='subject_map':
        archived=bank['prior_initial_map']
        original_topics={t['id']:t for c in archived['categories'] for t in c['topics']}
        original_categories={c['id']:c for c in archived['categories']}
    else:
        original_categories=cs
    for tid, expected in rec['source_records'].items():
        t=original_topics.get(tid)
        need(t is not None and all(k in t for k in expected['keys']) and fingerprint({k:t[k] for k in expected['keys']})==expected['sha256'],f'imported record changed {tid}')
    for cid,expected in rec['source_categories'].items():
        c=original_categories.get(cid)
        need(c is not None and fingerprint({k:c[k] for k in expected['keys']})==expected['sha256'],f'imported category metadata changed {cid}')
    if rec['source_initial_archive_sha256']:
        need(fingerprint(bank['prior_initial_map'])==rec['source_initial_archive_sha256'],'prior source archive changed')
    status=read(directory/'topics_status.json')
    original=rec['local_status_original']
    need(all(k in status and status[k]==v for k,v in original.items()),'original local status field changed')
    for name,snap in rec['local_files'].items():
        # Snapshot data itself is preserved and can reconstruct original local files.
        text=snap['original_text']
        raw=text.encode('utf-8')
        need(sha(raw)==snap['sha256'] or sha(b'\xef\xbb\xbf'+raw)==snap['sha256'],f'local file snapshot changed {name}')
    return errors


def render(bank,directory):
    nid=bank['niche_id'];count=len(records(bank));rec=bank['local_reconciliation']
    original_status=rec['local_status_original']
    live_status=read(directory/'topics_status.json')
    assert all(live_status.get(k)==v for k,v in original_status.items()), f'Local status changed since snapshot; reconcile before rendering: {nid}'
    for name,expected in bank.get('rendered_view_hashes',{}).items():
        live=directory/name
        assert live.exists() and sha(live.read_bytes())==expected, f'View changed since rendering; preserve/reconcile before writing: {nid}/{name}'
    legacy=legacy_records(original_status)
    emitted_bank_anchors={t['id'] for c,t in records(bank)}
    roadmap_name=next((n for n in rec['local_files'] if n.endswith('_CHANNEL_TOPIC_ROADMAP.md')),None)
    roadmap_text=rec['local_files'][roadmap_name]['original_text'] if roadmap_name else ''
    original_questions=roadmap_questions(roadmap_text)
    lines=[f"# {nid} — {bank['name']}: main topic bank",'',
        f"Updated: {bank.get('updated','2026-10-23')} · **{count} active BANK proposals · {len(bank['parent_categories'])} categories · {len(bank['categories'])} subcategories.**",'',
        'Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.', '',
        '[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)', '',
        '## Learning progression','',
        'Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.', '']
    for level in LEVELS:
        sequence=[c for c in bank['categories'] if c['level']==level]
        if sequence:
            lines += [f"- **{level.title()}:** " + ' → '.join(f"[{c['title']}](#{c['id'].lower()})" for c in sequence)+'.']
    lines += ['', '| Category | Foundation | Intermediate | Advanced |','|---|---:|---:|---:|']
    for p in bank['parent_categories']:
        counts=Counter(t.get('level',c['level']) for c,t in records(bank) if c['parent_id']==p['id'])
        lines.append(f"| [{table(p['title'])}](#{p['id'].lower()}) | {counts['foundation']} | {counts['intermediate']} | {counts['advanced']} |")
    for p in bank['parent_categories']:
        lines += ['',f'<a id="{p["id"].lower()}"></a>',f"## Category: {p['title']}",'']
        children=[c for c in bank['categories'] if c['parent_id']==p['id']]
        children.sort(key=lambda c:min((LEVELS[t.get('level',c['level'])] for t in c['topics']),default=LEVELS[c['level']]))
        for c in children:
            lines += [f'<a id="{c["id"].lower()}"></a>',f"### {c.get('reading_subcategory',c['title'])}",'',
                f"Subcategory `{c['id']}` · {c['level']}.",'']
            if not c['topics']:
                lines += ['Original subcategory metadata is preserved. Its overlapping proposal records are retained with primary-question referrals below and excluded from the active count.','']
            if c['prerequisites']:
                lines += ['Prerequisites: '+', '.join(f'[{ref}](#{ref.lower()})' for ref in c['prerequisites'])+'.','']
            for t in sorted(c['topics'],key=lambda t:LEVELS[t.get('level',c['level'])]):
                lines += [f'<a id="{t["id"].lower()}"></a>',f"#### {t['id']} — {t.get('title',t['question'])}",'']
                if t.get('title') and t['title']!=t['question']:
                    lines += [f"**Video question:** {t['question']}",'']
                lines += [f"**Individual coverage scope:** {t['coverage']}",'']
                if t.get('additional_scope'):
                    lines += [f"**Scope extension:** {t['additional_scope']}",'']
                if t.get('related_ids'):
                    lines += ['**Related questions:** '+', '.join(f'[{ref}]({topic_href(nid,ref)})' for ref in t['related_ids'])+'.','']
                for followup in bank.get('research_followups',[]):
                    if followup['topic_id']==t['id']:
                        lines += [f"**Research follow-up:** [Bounded case and source-access note]({followup['note_file']}). This does not change proposal or production status.",'']
                for ref in bank.get('editorial_cross_references',[]):
                    if ref['topic_id']==t['id']:
                        lines += [f"**Neighboring scope:** [{ref['related_id']}]({topic_href(nid,ref['related_id'])}) — {ref['boundary']}",'']
                if t.get('origin')=='repository_roadmap':
                    lines += ['Source: preserved local roadmap proposal. Its original framing is not a verified finding.','']
                if t.get('exclusions'):lines += [f"**Boundary:** {t['exclusions']}",'']
    lines += ['## Preserved local roadmap and queue references','',
        f'The following {len(legacy)} source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.', '']
    for route,t in legacy:
        title=t.get('title') or t.get('concept') or t.get('question') or t.get('story_question')
        for archived in bank.get('archived_local_frameworks',[]):
            if archived.get('legacy_source_id')==t.get('id') and archived['id'] not in emitted_bank_anchors:
                lines += [f'<a id="{archived["id"].lower()}"></a>']
                emitted_bank_anchors.add(archived['id'])
        lines += [f"### {route} — {title}",'']
        numeric=t.get('id');q=original_questions.get(numeric) if isinstance(numeric,int) else None
        question=t.get('question') or t.get('story_question') or (q['question'] if q else None)
        focus=t.get('key_focus') or t.get('coverage') or (q['coverage'] if q else None)
        if question:lines += [f'**Original question:** {question}','']
        if focus:lines += [f'**Original planning scope:** {focus}','']
        reviewed=bank.get('legacy_topic_crosswalk',{}).get(route)
        if reviewed:
            lines += [f"**Editorial disposition:** {reviewed['decision']}. {reviewed['reason']}",'']
            if reviewed.get('bank_ids'):
                lines += ['**Scoped proposals:** '+', '.join(f'[{ref}]({topic_href(nid,ref)})' for ref in reviewed['bank_ids'])+'.','']
        elif not focus:lines += ['**Scope status:** original source record retained; an individual coverage boundary still needs editorial refinement.','']
    if bank.get('prior_initial_map'):
        lines += ['## Preserved starter subject map — coverage checklist, not extra proposals','',
            'These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.','']
        for old_category in bank['prior_initial_map']['categories']:
            if old_category['id'] not in {c['id'] for c in bank['categories']}:
                lines += [f'<a id="{old_category["id"].lower()}"></a>']
            lines += [f"### {old_category['title']}",'']
            for old in old_category['topics']:
                if old['id'] not in emitted_bank_anchors:
                    lines += [f'<a id="{old["id"].lower()}"></a>']
                    emitted_bank_anchors.add(old['id'])
                mapped=bank.get('starter_concept_crosswalk',{}).get(old['id'],[])
                suffix=' → '+', '.join(f'[{ref}]({topic_href(nid,ref)})' for ref in mapped) if mapped else ' — compare with active scopes; individual mapping remains open.'
                lines.append(f"- `{old['id']}` — {old.get('title',old['question'])}"+suffix)
            lines.append('')
    lines += ['## Neighboring niche boundaries','',bank.get('overlap_policy','Retain one primary niche for a specific question; cross-link related subject matter rather than copy an episode.'),'']
    for n in bank.get('neighboring_niches',[]):
        target=TOPICS/n['directory']/'IN_DEPTH_TOPIC_BANK.md'
        lines.append(f"- [{n['id']} {n['title']}](../{n['directory']}/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.")
    referrals={r['topic_id']:r for r in bank.get('duplicate_referrals',[]) if r.get('topic_id')}
    retired_by_id={t['id']:t for t in bank.get('retired_duplicate_proposals',[])}
    for retired in retired_by_id.values():
        referrals.setdefault(retired['id'],{'topic_id':retired['id'],'primary_topic_id':retired['duplicate_of'],
            'reason':retired.get('retirement_reason','Same question and scope; keep one primary proposal.')})
    if referrals:
        lines += ['','### Retired overlaps and primary questions','']
        for referral in referrals.values():
            primary=referral['primary_topic_id']
            target=referral.get('primary_directory') or home(primary.split('-')[1]).name
            if referral.get('topic_id'):
                lines += [f'<a id="{referral["topic_id"].lower()}"></a>']
            lines.append(f"- `{referral.get('topic_id','Retired local draft')}` → [{primary}](../{target}/IN_DEPTH_TOPIC_BANK.md#{primary.lower()}): {referral.get('reason','Same question and scope; retain one primary home instead of counting another proposal.')}")
            retired=retired_by_id.get(referral.get('topic_id'))
            if retired:
                lines += ['',f"  Preserved inactive question: {retired['question']}",'']
                lines += [f"  Preserved inactive scope: {retired['coverage']}",'']
    review=bank.get('editorial_review',{})
    if review:
        lines += ['','## Editorial coverage review','',review.get('summary','Question scopes, source concepts and documented gaps reviewed.'),'']
        if review.get('audit_file'):
            lines += [f"[Review decisions and evidence](../../{review['audit_file']})",'']
    lines += ['','## Coverage remaining open','']
    gaps=bank.get('open_coverage',[])
    if gaps:
        for g in gaps:lines.append('- '+(f"**{g['area']}:** {g['next_step']}" if isinstance(g,dict) else str(g)))
    else:
        lines += ['- Exact cases, places, time periods, editions, populations and source availability still need selection for the proposals above.',
            '- Review regional and linguistic variation, overlooked participants, contrary cases and neighboring-niche overlap before adding another episode.',
            '- Category coverage is an editorial draft. Further substantive branches remain open; no count establishes exhaustive coverage.']
    lines += ['','## Connection to the production documents','',
        f"This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/{directory.name}/NICHE_{directory.name}.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.",'',
        'Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.','']
    save_bytes(directory/'IN_DEPTH_TOPIC_BANK.md','\n'.join(lines).encode('utf-8'))
    # Preserve every existing top-level status value; add only a new independent namespace.
    status=copy.deepcopy(live_status)
    status['topic_bank_integration']={'main_reading_file':'IN_DEPTH_TOPIC_BANK.md','editable_bank':'IN_DEPTH_TOPIC_BANK.json',
        'reconciliation_report':'TOPIC_BANK_RECONCILIATION.md','active_bank_proposals':count,'categories':len(bank['parent_categories']),
        'subcategories':len(bank['categories']),'legacy_source_records':len(legacy),'updated':'2026-10-23',
        'verification':'not_performed','integration_stage':bank['integration_stage']}
    write(directory/'topics_status.json',status)
    if roadmap_name:
        pointer=f"# {nid} — Channel roadmap\n\n**Main reading file: [{bank['name']} topic bank](IN_DEPTH_TOPIC_BANK.md).**\n\nThe bank organizes {count} active proposals by category, subcategory and learning level. Original roadmap questions and queue records are preserved in its source-reference section and JSON snapshots. They are not counted twice.\n\n[Existing production report](TOPICS_COVERED_REPORT.md) · [Reconciliation and open coverage](TOPIC_BANK_RECONCILIATION.md)\n"
        if nid=='281':
            # Extensive user-authored roadmap remains intact; add a navigation banner only.
            pointer='**Main reconciled topic bank: [read here](IN_DEPTH_TOPIC_BANK.md). Existing roadmap content below is preserved.**\n\n'+roadmap_text
        save_bytes(directory/roadmap_name,pointer.encode('utf-8'))
    report_name='TOPICS_COVERED_REPORT.md'
    report_original=rec['local_files'].get(report_name,{}).get('original_text','')
    if report_original:
        save_bytes(directory/report_name,(report_original.rstrip()+'\n\n## Reconciled topic-bank connection\n\n[Main topic bank](IN_DEPTH_TOPIC_BANK.md) · [Reconciliation, counts and remaining coverage](TOPIC_BANK_RECONCILIATION.md). The original execution report above is preserved; its production/trend claims were not independently re-verified by this topic-bank work.\n').encode('utf-8'))
    source_active=sum(t['id'] in rec['source_records'] for c,t in records(bank)) if rec['source_kind']!='subject_map' else 0
    adopted=sum(t.get('origin')=='repository_roadmap' for c,t in records(bank))
    report=[f"# {nid} — Topic-bank reconciliation",'', '[Main reading file](IN_DEPTH_TOPIC_BANK.md) · [Editable catalog](IN_DEPTH_TOPIC_BANK.json)','',
        f"Status: **{bank['integration_stage']}**. Subject coverage remains open; sources are unverified.",'',
        '| Record family | Count | Treatment |','|---|---:|---|',
        f'| Active BANK proposals | {count} | Counted once |',
        f"| Categories / subcategories | {len(bank['parent_categories'])} / {len(bank['categories'])} | Navigation |",
        f'| Preserved imported detailed proposals | {source_active} | Original fields, IDs and questions retained |',
        f'| Reconciled local roadmap proposals | {adopted} | Original questions/scopes reused without a second count |',
        f"| Archived generic local framework records | {len(bank.get('archived_local_frameworks',[]))} | IDs and wording preserved; inactive |",
        f'| Newly authored BANK proposals | {count-source_active-adopted} | Individually scoped additions |',
        f'| Local legacy source records | {len(legacy)} | Original status values retained; excluded from active BANK count |','',
        '## Preservation and integration','',
        f"- ZIP: `{rec['archive_path']}`; SHA256 `{rec['archive_sha256']}`.",
        f"- Source member: `{rec['member']}`; SHA256 `{rec['member_sha256']}`. Checked against the bundle manifest and extracted copy before import.",
        '- Neither all-niche patch was applied. Final niche data was imported selectively and reconciled with current local files.',
        '- Source detailed BANK questions/scopes/IDs and category metadata remain intact. Superseded starter maps remain exactly archived under prior_initial_map and are excluded from active counts.',
        '- Original local status fields, completed/queued/trend records and all original roadmap/report text are preserved in the catalog snapshots. The live status file receives only topic_bank_integration metadata.',
        '- Existing production report remains present with a bank link. The original roadmap routes to the main bank; the extensively edited Ayurveda roadmap retains its full body.',
        '- Registry, CAT questions, sources, ideas, DEPTH plans, CONFIG and episode production files are unchanged. Main topics index links to the bank.','',
        '## Validation and remaining work','',
        'Run `python Scripts/manage_all_topic_banks.py check` for ID, question-duplicate, source preservation, category prerequisite, count, local status and Markdown-link checks. These checks do not prove exhaustive semantic uniqueness or factual correctness.',
        'All questions require case selection, source inspection, overlap review and the existing production readiness process. Existing popularity and completion claims were retained as source metadata and are not new certifications.','',
        'Files for this niche: IN_DEPTH_TOPIC_BANK.json, IN_DEPTH_TOPIC_BANK.md, topics_status.json, the existing roadmap, TOPICS_COVERED_REPORT.md and this reconciliation report.','']
    save_bytes(directory/'TOPIC_BANK_RECONCILIATION.md','\n'.join(report).encode('utf-8'))
    view_names=['IN_DEPTH_TOPIC_BANK.md','TOPIC_BANK_RECONCILIATION.md','TOPICS_COVERED_REPORT.md']+([roadmap_name] if roadmap_name else [])
    bank['rendered_view_hashes']={name:sha((directory/name).read_bytes()) for name in view_names if (directory/name).exists()}
    write(directory/'IN_DEPTH_TOPIC_BANK.json',bank)


def index():
    lines=['# All-niche topic banks','',
        '[Reconciliation report](ALL_NICHE_RECONCILIATION_REPORT.md) · [Editorial review](TOPIC_BANK_EDITORIAL_REVIEW.md) · [Open coverage](TOPIC_BANK_OPEN_COVERAGE.md) · [Maintenance guide](TOPIC_BANK_GUIDE.md) · [Changed files](TOPIC_BANK_CHANGED_FILES.json)','',
        'One main reading file per niche. Counts are active BANK proposals, not scripts, verified facts, ready ideas, completed videos or a quota. Initial-map and expansion stages are reported honestly. Local legacy roadmap/queue records remain separate and are visible in each main file.','',
        '| Niche | Active BANK proposals | Categories | Subcategories | Stage | Main reading file |','|---|---:|---:|---:|---|---|']
    entries=[]
    path=TOPICS/'README.md';raw=path.read_bytes();text=raw.decode('utf-8')
    for nid,row in rows().items():
        directory=home(nid);bank_path=directory/'IN_DEPTH_TOPIC_BANK.json'
        if not bank_path.exists():continue
        b=read(bank_path);n=len(records(b))
        stage=b.get('integration_stage','reconciled_niche_001')
        entry={'niche_id':nid,'title':row['title'],'active_bank_proposals':n,'categories':len(b['parent_categories']),
            'subcategories':len(b['categories']),'stage':stage,'main_file':f'{directory.name}/IN_DEPTH_TOPIC_BANK.md'}
        entries.append(entry)
        lines.append(f"| {nid} {table(row['title'])} | {n} | {entry['categories']} | {entry['subcategories']} | {stage} | [Read]({entry['main_file']}) |")
        pattern=rf'(?m)^\| \*\*{nid}\*\* \|[^\r\n]+'
        match=re.search(pattern,text)
        if match and nid!='001':
            old=match.group(0);cells=old.rsplit('|',2)
            new=cells[0]+f'| [Main bank: {n} proposals](./{directory.name}/IN_DEPTH_TOPIC_BANK.md) · [Original status](./{directory.name}/TOPICS_COVERED_REPORT.md) |'
            text=text[:match.start()]+new+text[match.end():]
    save_bytes(path,text.encode('utf-8'))
    save_bytes(TOPICS/'ALL_NICHE_TOPIC_BANKS.md',('\n'.join(lines)+'\n').encode('utf-8'))
    progress={'updated':'2026-10-23','niches_with_banks':len(entries),'active_bank_proposals':sum(e['active_bank_proposals'] for e in entries),
        'stages':dict(Counter(e['stage'] for e in entries)),'exhaustive_coverage_claimed':False,'verified_sources_added':0,'niches':entries}
    write(TOPICS/'TOPIC_BANK_PROGRESS.json',progress)
    print(f"Indexed {len(entries)} banks, {progress['active_bank_proposals']} active proposals; stages {progress['stages']}")


def check(report=None):
    errors=[];question_map=defaultdict(list);local_links=0;count=0;stages=Counter()
    for nid in rows():
        directory=home(nid);path=directory/'IN_DEPTH_TOPIC_BANK.json'
        if not path.exists():errors.append(f'{nid}: missing bank');continue
        b=read(path);count+=1;stages[b.get('integration_stage','reconciled_niche_001')]+=1
        if nid=='001':
            import manage_ai_topics
            failures,_=manage_ai_topics.validate(b,read(directory/'topics_status.json'))
            errors.extend(failures)
        else:
            errors.extend(check_bank(b,directory))
        for c,t in records(b):question_map[norm(t['question'])].append(t['id'])
        for name in ('IN_DEPTH_TOPIC_BANK.md','TOPIC_BANK_RECONCILIATION.md'):
            md=directory/name
            if nid=='001' and name=='TOPIC_BANK_RECONCILIATION.md':continue
            if not md.exists():errors.append(f'{nid}: missing view {name}');continue
            content=md.read_text(encoding='utf-8')
            if name=='IN_DEPTH_TOPIC_BANK.md' and nid!='001' and f"**{len(records(b))} active BANK proposals" not in content:
                errors.append(f'{nid}: stale main-file proposal count')
            if name=='IN_DEPTH_TOPIC_BANK.md':
                for c,t in records(b):
                    if t['id'] not in content or t['question'] not in content or t['coverage'] not in content:
                        errors.append(f"{nid}: missing/truncated question or scope in main file: {t['id']}")
            expected=b.get('rendered_view_hashes',{}).get(name)
            if expected and sha(md.read_bytes())!=expected:
                errors.append(f'{nid}: edited/stale generated view {name}')
            anchors=set(re.findall(r'<a id="([^"]+)"',content))
            for target in re.findall(r'\]\(([^)]+)\)',content):
                target=unquote(target)
                if '://' in target or target.startswith('mailto:'):continue
                local_links+=1
                filename,_,fragment=target.partition('#')
                if filename:
                    linked=md.parent/filename
                    if not linked.exists():errors.append(f'{nid}: broken local link {target}')
                    elif fragment.startswith('bank-') and linked.suffix=='.md' and f'id="{fragment}"' not in linked.read_text(encoding='utf-8'):
                        errors.append(f'{nid}: broken linked BANK anchor {target}')
                elif fragment not in anchors:errors.append(f'{nid}: broken anchor {target}')
    for index_path in (TOPICS/'ALL_NICHE_TOPIC_BANKS.md', TOPICS/'ALL_NICHE_RECONCILIATION_REPORT.md',
                       TOPICS/'TOPIC_BANK_OPEN_COVERAGE.md', TOPICS/'TOPIC_BANK_GUIDE.md', TOPICS/'TOPIC_BANK_EDITORIAL_REVIEW.md'):
        if index_path.exists():
            for target in re.findall(r'\]\(([^)]+)\)',index_path.read_text(encoding='utf-8')):
                if '://' not in target and not target.startswith('#'):
                    local_links+=1
                    if not (index_path.parent/unquote(target.split('#')[0])).exists():
                        errors.append(f'Index broken local link: {target}')
    duplicates={q:ids for q,ids in question_map.items() if len(ids)>1}
    result={'updated':'2026-10-23','niches_checked':count,'active_bank_proposals':sum(len(ids) for ids in question_map.values()),
        'integration_stages':dict(stages),'errors':errors,'exact_cross_niche_duplicate_questions':duplicates,
        'local_links_checked':local_links,'semantic_review':'Human/agent editorial review required; exact matches do not detect all semantic overlap.',
        'source_verification':'not_performed','remote_changes':'none'}
    if report:write(report,result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('errors','exact_cross_niche_duplicate_questions')},indent=2))
    if errors:print('\n'.join(errors[:60]))
    if duplicates:print(f'Exact cross-niche question collisions: {len(duplicates)}; inspect report.')
    return not errors and not duplicates


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['bootstrap','adopt-legacy','apply','render','index','check'])
    parser.add_argument('--start',type=int,default=2)
    parser.add_argument('--end',type=int,default=550)
    parser.add_argument('--input',type=Path)
    parser.add_argument('--report',type=Path)
    args=parser.parse_args()
    if args.command=='bootstrap':bootstrap(args.start,args.end)
    elif args.command=='adopt-legacy':adopt_legacy(args.start,args.end)
    elif args.command=='apply':
        assert args.input
        apply(args.input.resolve())
    elif args.command=='index':index()
    elif args.command=='check':raise SystemExit(0 if check(args.report) else 1)
    else:
        for n in range(max(2,args.start),args.end+1):
            d=home(f'{n:03d}');render(read(d/'IN_DEPTH_TOPIC_BANK.json'),d)
        print('Rendered targeted banks only.')
