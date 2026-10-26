from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Record concrete mapping, breadth and semantic decisions for the recovered pass."""
import hashlib
import json
from pathlib import Path
import manage_all_topic_banks as manager

ROOT=Path(__file__).resolve().parents[4]
S=ROOT/'Scripts'
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
before=read(S/'editorial_review_inputs/before_editorial_pass.json')['banks']
snapshot=read(S/'editorial_read_368_550.json')
payload=read(S/'editorial_pass_368_550.json')
repairs=read(S/'editorial_mapping_repairs_368_550.json')
unique={}
for name in ['semantic_candidates_368_550.json','semantic_question_candidates_368_550.json']:
    for p in read(S/'editorial_review_inputs'/name)['pairs']:
        unique[(p['left']['id'],p['right']['id'])]=p
verdicts={}
for line in (S/'editorial_semantic_verdicts_368_550.txt').read_text(encoding='utf-8-sig').splitlines():
    index,decision,reason=line.split('|');verdicts[int(index)]=(decision,reason)
assert len(unique)==len(verdicts)==89
decisions=[];recommendations=[]
for i,p in enumerate(unique.values()):
    decision,reason=verdicts[i]
    ids=[p['left']['id'],p['right']['id']]
    decisions.append({'ids':ids,'decision':decision,'reason':reason,
                      'scope_evidence':[{k:side[k] for k in ['id','question','coverage']} for side in [p['left'],p['right']]]})
    if decision.startswith('retire_'):
        retire,primary=(ids[1],ids[0]) if decision=='retire_right' else (ids[0],ids[1])
        recommendations.append({'retire_id':retire,'primary_id':primary,'reason':reason})

# Cross-range AI foundation overlaps were separately read against niche 001 by root.
for retire,primary in [
 ('531-030','001-078'),('531-031','001-081'),('531-032','001-046'),('531-033','001-079'),('531-034','001-082'),('531-037','001-080'),
 ('532-030','001-029'),('532-031','001-028'),('532-032','001-034'),('532-033','001-029'),('532-035','001-044'),('532-036','001-028'),('532-037','001-025'),
 ('481-035','001-201'),('546-045','546-044'),
]:
    recommendations.append({'retire_id':'BANK-'+retire,'primary_id':'BANK-'+primary,
        'reason': 'The foundation question is already scoped in the primary proposal; specialist additions in this pass address different system decisions.' if retire.startswith(('531','532')) else
        ('The primary consciousness question already includes negative evidence and competing theories.' if retire.startswith('481') else 'Era-aware cricket statistics already includes differences in schedules and opportunity; the later generic opportunity comparison adds no distinct analytical task.')})
# One retirement per ID; resolve the Gita crisis to the earliest encompassing dialogue proposal.
dedup={}
for rec in recommendations:dedup.setdefault(rec['retire_id'],rec)
recommendations=list(dedup.values())
result={'date':'2026-10-23','range':'368–550','review_type':'Question-and-scope editorial review; proposals only; no factual verification or exhaustive-coverage certification.',
        'candidate_decisions':decisions,'duplicate_recommendations':recommendations,'banks':{}}
errors=[]
for nid,data in snapshot.items():
    path=ROOT/data['path'];bank=read(path)
    byid={t['id']:t for c in bank['categories'] for t in c['topics']}
    byquestion={t['question']:t for t in byid.values()}
    original_ids=[t['id'] for t in before[nid]['topics']]
    assert set(original_ids)=={t['id'] for t in data['active']},nid
    for old in before[nid]['topics']:
        assert old['id'] in byid and byid[old['id']]['question']==old['question'] and byid[old['id']]['coverage']==old['coverage'],(nid,old['id'])
    starter_decisions=[]
    for starter in data['starter_concepts']:
        old_targets=data['starter_concept_crosswalk'].get(starter['id'],[])
        if starter['id'] in repairs:
            targets=[byquestion[repairs[starter['id']]]['id']]
            bank['starter_concept_crosswalk'][starter['id']]=targets
            disposition='repaired_with_individually_scoped_proposal'
            reason='The prior referral did not directly establish '+starter['title']+'. Replaced it with the explicit mechanism question and scope quoted below; the original referral is retained in this audit.'
        else:
            targets=bank['starter_concept_crosswalk'][starter['id']]
            disposition='retained_after_question_and_scope_review'
            reason='The quoted question and scope address '+starter['title']+' as a bounded component or comparison. A shared target may cover connected concepts; it is not a claim to exhaust the branch.'
        evidence=[]
        for tid in targets:
            t=byid.get(tid)
            if t is None:
                targetbank=read(manager.home(tid.split('-')[1])/'IN_DEPTH_TOPIC_BANK.json')
                t=next(t for c in targetbank['categories'] for t in c['topics'] if t['id']==tid)
            evidence.append({k:t[k] for k in ['id','question','coverage']})
        assert evidence,(nid,starter['id'])
        starter_decisions.append({'starter_id':starter['id'],'title':starter['title'],'previous_target_ids':old_targets,
                                  'target_ids':targets,'target_evidence':evidence,'decision':disposition,'reason':reason})
    added=[{'id':byquestion[t['question']]['id'],'subcategory':g['title'],'level':g['level'],'question':t['question'],'coverage':t['coverage']}
           for g in payload[nid]['groups'] for t in g['topics']]
    branches={}
    for t in added:branches.setdefault(t['subcategory'],[]).append({k:t[k] for k in ['id','question','coverage']})
    gaps=[{'prior_gap':gap,'decision':'expanded_with_scoped_proposals','branch_evidence':branches,
           'reason':'The saved gap is expanded into the concrete questions and individual scopes below; actual source, specimen, participant or case choice remains a later decision.'}
          for gap in before[nid]['open_coverage']]
    bank['editorial_review']={'date':'2026-10-23','status':'catalog_scope_reviewed_factual_verification_not_performed',
          'audit':'../../Scripts/editorial_review_368_550.json','starter_mapping_repairs':sum(s['decision'].startswith('repaired') for s in starter_decisions),
          'scope_note':'Reviewed existing proposal scopes, repaired misleading starter referrals, expanded saved subject gaps, and recorded overlap recommendations. Actual research/case selection and further substantive expansion remain possible.'}
    manager.write(path,bank)
    e=manager.check_bank(bank,path.parent);errors.extend(e)
    assert not e,(nid,e)
    manager.render(bank,path.parent)
    result['banks'][nid]={'reviewed_before_ids':original_ids,'baseline_sha256':before[nid]['sha256'],
       'reviewed_before_records':[{'id':t['id'],'question':t['question'],'coverage':t['coverage']} for t in before[nid]['topics']],
       'additions':added,'starter_decisions':starter_decisions,'gap_decisions':gaps,
       'semantic_decisions':[d for d in decisions if any(i.split('-')[1]==nid for i in d['ids'])],
       'remaining_case_decisions':payload[nid]['open_coverage'],
       'reading_order_review':{'levels':{level:sum(c['level']==level for c in bank['categories']) for level in ['foundation','intermediate','advanced']},
          'decision':'Topics remain grouped by subject with linked foundation/intermediate/advanced reading paths; no equal-count quota was imposed.'},
       'active_count_after_additions':len(byid),'reviewed_bank_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
result['summary']={'banks':len(result['banks']),'additions':sum(len(x['additions']) for x in result['banks'].values()),
                  'starter_decisions':sum(len(x['starter_decisions']) for x in result['banks'].values()),
                  'mapping_repairs':len(repairs),'candidate_pairs':len(decisions),'duplicate_recommendations':len(recommendations),'bank_validation_errors':errors}
manager.write(S/'editorial_review_368_550.json',result)
print(json.dumps(result['summary']))
