from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Apply manually authored missing proposals and explicit, reviewed starter choices."""
import hashlib
import json
from pathlib import Path
import manage_all_topic_banks as manager

ROOT=Path(__file__).resolve().parents[4]
S=ROOT/'Scripts'
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
baseline=read(S/'editorial_review_inputs/before_editorial_pass.json')['banks']
authored={}
payload={}
for name in ['editorial_starter_authored_081_090.txt','editorial_starter_authored_091_100.txt','editorial_starter_authored_101_110.txt','editorial_starter_authored_final_081_110.txt']:
    for line in (S/name).read_text(encoding='utf-8-sig').splitlines():
        if not line.strip():continue
        sid,parent,title,level,question,coverage=line.split('|')
        sid='BANK-'+sid;nid=sid.split('-')[1]
        assert sid not in authored,sid
        authored[sid]={'question':question,'coverage':coverage}
        payload.setdefault(nid,[]).append({'parent':parent,'title':title,'level':level,'topics':[{'question':question,'coverage':coverage,'covers_starter_ids':[sid]}]})
maps={}
for line in (S/'editorial_starter_manual_maps_081_110.txt').read_text(encoding='utf-8-sig').splitlines():
    if line.strip():
        nid,codes=line.split('|');maps[nid]=codes.split(',')
assert set(maps)=={f'{n:03d}' for n in range(81,111)}

input_path=S/'editorial_starter_gap_additions_081_110.json'
manager.write(input_path,payload)
captured={}
for nid in maps:
    p=manager.home(nid)/'IN_DEPTH_TOPIC_BANK.json';b=read(p)
    captured[nid]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                   'records':{t['id']:dict(t) for c in b['categories'] for t in c['topics']},
                   'prior_crosswalk':b.get('starter_concept_crosswalk',{})}
manager.apply(input_path)

global_topics={}
for path in (ROOT/'topics').glob('*/IN_DEPTH_TOPIC_BANK.json'):
    bank=read(path)
    for cat in bank['categories']:
        for t in cat['topics']:global_topics[t['id']]=t

packet={'date':'2026-10-24','banks':{},'method':'Manual review of every archived starter title and actual candidate question/scope. Lexical rankings were only a triage aid; explicit choices are saved in editorial_starter_manual_maps_081_110.txt. No source or factual verification performed.'}
errors=[]
for nid,codes in maps.items():
    path=manager.home(nid)/'IN_DEPTH_TOPIC_BANK.json';bank=read(path)
    starters=[t for c in bank['prior_initial_map']['categories'] for t in c['topics']]
    assert len(codes)==len(starters),(nid,len(codes),len(starters))
    current={t['id']:t for c in bank['categories'] for t in c['topics']}
    for tid,old in captured[nid]['records'].items():
        assert tid in current and current[tid]['question']==old['question'] and current[tid]['coverage']==old['coverage'],(nid,tid)
    decisions=[];new=[]
    for starter,code in zip(starters,codes):
        sid=starter['id']
        if code=='NEW':
            proposal=authored[sid]
            target=next(t for t in current.values() if t['question']==proposal['question'] and t['coverage']==proposal['coverage'])
            targets=[target['id']];new.append(dict(target))
            decision='added_missing_individually_scoped_proposal'
            reason='The existing proposals did not directly cover '+starter['title']+'. The new question and scope below name the missing mechanism, tradition or bounded case rather than map the starter to a generic method.'
        else:
            assert sid not in authored,(sid,'authored but not selected')
            targets=['BANK-'+(nid+'-'+codepart if '-' not in codepart else codepart) for codepart in code.split('+')]
            decision='mapped_existing_scope_after_manual_review'
            reason='The selected existing question and individual scope directly address '+starter['title']+'. Multiple targets denote explicit complementary parts; cross-niche targets reuse the primary coverage instead of adding a paraphrase.'
        evidence=[]
        for tid in targets:
            t=global_topics[tid]
            evidence.append({k:t[k] for k in ['id','question','coverage']})
        bank.setdefault('starter_concept_crosswalk',{})[sid]=targets
        decisions.append({'starter_id':sid,'starter_title':starter['title'],'target_ids':targets,
                          'scope_evidence':[t['coverage'] for t in evidence],
                          'target_evidence':evidence,'previous_target_ids':captured[nid]['prior_crosswalk'].get(sid,[]),
                          'decision':decision,'reason':reason})
    bank['starter_mapping_review']={'date':'2026-10-24','status':'all_archived_starters_reviewed_against_individual_scopes',
                'audit':'../../Scripts/editorial_starters_081_110.json','factual_verification':'not_performed'}
    manager.write(path,bank)
    e=manager.check_bank(bank,path.parent);errors.extend(e)
    assert not e,(nid,e)
    manager.render(bank,path.parent)
    packet['banks'][nid]={'reviewed_before_ids':[t['id'] for t in baseline[nid]['topics']],
         'reviewed_current_before_additions_ids':list(captured[nid]['records']),
         'before_starter_audit_sha256':captured[nid]['sha256'],'starter_decisions':decisions,
         'new_proposals':new,'reviewed_bank_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
packet['validation']={'banks':len(packet['banks']),'starters':sum(len(b['starter_decisions']) for b in packet['banks'].values()),
                     'new_proposals':sum(len(b['new_proposals']) for b in packet['banks'].values()),'errors':errors,'verified_sources':'not_performed'}
manager.write(S/'editorial_starters_081_110.json',packet)
print(json.dumps(packet['validation']))
