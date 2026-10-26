from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Apply individually reviewed grouping/routes and save the scope review handoff."""
import copy,json,re
from collections import defaultdict
from pathlib import Path
import manage_all_topic_banks as m

HERE=Path(__file__).resolve().parents[3]
BASE=m.read(HERE/'editorial_review_inputs/before_editorial_pass.json')['banks']
OWN=[f'{n:03d}' for n in range(185,368) if n!=281]
banks={n:m.read(m.home(n)/'IN_DEPTH_TOPIC_BANK.json') for n in OWN}

def find(n,phrase):
 hits=[t['id'] for c,t in m.records(banks[n]) if phrase.casefold() in t['question'].casefold()]
 assert len(hits)==1,(n,phrase,hits)
 return hits[0]

def route(n,i,targets):
 banks[n].setdefault('starter_concept_crosswalk',{})[f'BANK-{n}-{i:03d}']=targets

# Every entry in this file was selected against the actual question and scope.
for line in (HERE/'editorial_starter_routes_185_215.txt').read_text(encoding='utf-8-sig').splitlines():
 n,groups=line.split('|')
 for i,g in enumerate(groups.split(';'),1):route(n,i,[f'BANK-{n}-{int(v):03d}' for v in g.split(',')])
route('185',7,['BANK-185-028','BANK-185-036'])
route('194',7,['BANK-194-020','BANK-194-033'])
route('199',2,['BANK-199-012','BANK-199-032'])
route('204',3,['BANK-204-017'])
route('210',1,['BANK-210-030','BANK-210-024'])
route('215',4,['BANK-215-028','BANK-215-031'])

for n,i,phrase in [
 ('221',3,'water-sharing rules'),('246',4,'bridal textile move'),('246',9,'wedding budgets'),
 ('247',8,'same regional garment'),('249',7,'costume and makeup across'),
 ('255',3,'learning a kora repertoire'),('261',9,'restoration record distinguish'),
 ('266',7,'pricked embroidery'),('276',2,"temple's daily timetable"),
 ('282',1,'four noble truths form'),('282',10,'Vinaya texts'),
 ('292',8,'return spiritual-experience findings'),('305',6,'retailer-owned brand'),
 ('309',9,'loss-prevention surveillance'),('335',9,'trace a released performance')]:
 route(n,i,[find(n,phrase)])
route('218',23,['BANK-237-030'])
route('231',9,['BANK-231-039','BANK-230-039'])
route('248',7,['BANK-248-030','BANK-248-032'])
route('264',1,[find('264','hand spinners'),'BANK-264-032'])
route('274',2,['BANK-268-045'])
route('332',8,['BANK-332-039'])
route('340',5,['BANK-340-037'])
route('346',2,['BANK-346-039'])
route('366',9,['BANK-366-030','BANK-366-035'])

# Replace tier-only headings for the preserved local questions with actual subjects.
# Preserve former group metadata and each original proposal unchanged.
for line in (HERE/'editorial_grouping_185_215.txt').read_text(encoding='utf-8-sig').splitlines():
 fields=line.split('|');n=fields[0];b=banks[n]
 if b.get('editorial_grouping_revision')=='subject_and_level_2026_10_23':continue
 original_cats=[c for c in b['categories'] if any(t.get('origin')=='repository_roadmap' for t in c['topics'])]
 original={t['id']:(c,t) for c in original_cats for t in c['topics']}
 assert len(original)==sum(len(f.rsplit(':',1)[1].split(',')) for f in fields[2:]),n
 b['editorial_prior_local_group_metadata']=[{k:v for k,v in c.items() if k!='topics'} for c in original_cats]
 old_ids=[c['id'] for c in original_cats];available=iter(old_ids)
 counter=max(int(c['id'].rsplit('R',1)[1]) for c in b['categories'] if re.search(r'R\d+$',c['id']))
 replacements=[];assigned=[]
 for gi,group in enumerate(fields[2:],1):
  title,indices=group.rsplit(':',1);pid=f'DOMAIN-{n}-{gi:02d}'
  next(p for p in b['parent_categories'] if p['id']==pid)['title']=title
  grouped=defaultdict(list)
  for index in indices.split(','):
   tid=f'BANK-{n}-{int(index):03d}';cat,t=original[tid];grouped[cat['level']].append(copy.deepcopy(t));assigned.append(tid)
  for level in m.LEVELS:
   if level not in grouped:continue
   cid=next(available,None)
   if cid is None:counter+=1;cid=f'CATALOG-{n}-R{counter:02d}'
   replacements.append({'id':cid,'title':title+' — '+level,'parent_id':pid,'level':level,
                        'research_profile':original_cats[0]['research_profile'],'prerequisites':[],
                        'topics':grouped[level]})
 assert sorted(assigned)==sorted(original),n
 b['categories']=replacements+[c for c in b['categories'] if c not in original_cats]
 b['editorial_grouping_revision']='subject_and_level_2026_10_23'

pairs=m.read(HERE/'editorial_review_inputs/semantic_candidates_185_367.json')['pairs']
qpairs=m.read(HERE/'editorial_review_inputs/semantic_question_candidates_185_367.json')['pairs']
decisions={};recommendations=[]
def decide(pair,decision,primary,reason):
 ids=sorted([pair['left']['id'],pair['right']['id']]);key=tuple(ids)
 decisions[key]={'ids':ids,'decision':decision,'reason':reason}
 if primary:
  assert primary in ids
  recommendations.append({'retire_id':next(t for t in ids if t!=primary),'primary_id':primary,'reason':reason})

for line in (HERE/'editorial_semantic_verdicts_185_367.txt').read_text(encoding='utf-8-sig').splitlines():
 i,d,primary,reason=line.split('|',3)
 # Pair78 is a second view of the same generic251 record; direct it to035 here.
 if int(i)==78:primary='BANK-251-035'
 decide(pairs[int(i)],d,primary,reason)
for line in (HERE/'editorial_question_verdicts_185_367.txt').read_text(encoding='utf-8-sig').splitlines():
 i,d,primary,reason=line.split('|',3);decide(qpairs[int(i)],d,primary,reason)

overrides=[('BANK-278-002','BANK-278-024','Both read the same chapter3 meditation triad; preserve the full earlier record inactive and use one close-reading primary.'),
 ('BANK-280-035','BANK-278-024','The same samyama sequence and attributed powers are the actual proposed output; do not invent a distinction from wider context.'),
 ('BANK-279-091','BANK-279-005','Safety framing repeats the same boundary and professional-scope question; preserve one primary and the full original inactive.'),
 ('BANK-280-008','BANK-278-030','The same Shvetashvatara body/breath/contemplation passage is the proposed close reading.'),
 ('BANK-338-033','BANK-001-082','Task-scoped agent permissions repeat the same read/write/external-action privilege map.'),
 (find('206','mountain range contribute to aridity'),'BANK-206-012','The preserved local rain-shadow proposal already covers uplift, moisture loss and atmospheric setting; reject the new redundant explanation.'),
 (find('358','heating alter a magnet'),'BANK-358-031','The existing domains and hysteresis scope already includes temperature; no additional episode is justified.'),
 (find('300','failed and delisted companies'),'BANK-300-033','The existing index-history scope explicitly includes survivorship, dividends and constituent changes; a second dataset version would overlap.')]
for retire,primary,reason in overrides:
 recommendations.append({'retire_id':retire,'primary_id':primary,'reason':reason})
 key=tuple(sorted([retire,primary]));decisions[key]={'ids':list(key),'decision':'duplicate_recommended','reason':reason}

# Same-bank distinct readings stay explicit rather than being retired by a score.
key=tuple(sorted(['BANK-279-023','BANK-279-024']))
decisions[key]={'ids':list(key),'decision':'distinct_with_boundary','reason':'023 reads one Yoga Sutra passage;024 compares sequencing and commentaries across passages. Require the actual single-passage versus cross-passage outputs.'}

expected={tuple(sorted([p['left']['id'],p['right']['id']])) for p in pairs+qpairs}
assert expected<=set(decisions),(expected-set(decisions))

audit={'date':'2026-10-23','status':'owned_editorial_review_complete_duplicate_consolidation_pending',
       'source_verification':'not_performed','exhaustive_claim':False,
       'method':'Individual review of actual before-pass questions, scopes and starter subjects, with saved subject grouping and two lexical candidate shortlists reviewed as triage, not automatic verdicts.',
       'banks':{},'candidate_decisions':list(decisions.values()),'duplicate_recommendations':recommendations}

for n,b in banks.items():
 d=m.home(n);before=BASE[n]
 added=[t['id'] for c,t in m.records(b) if t['id'] not in {t['id'] for t in before['topics']}]
 starters=[t for c in b.get('prior_initial_map',{}).get('categories',[]) for t in c['topics']]
 starter_decisions=[]
 for old in starters:
  targets=b.get('starter_concept_crosswalk',{}).get(old['id'],[])
  assert targets,(n,old['id'])
  evidence=[]
  for tid in targets:
   tn=tid.split('-')[1];targetbank=banks[tn] if tn in banks else m.read(m.home(tn)/'IN_DEPTH_TOPIC_BANK.json')
   t=next(t for c,t in m.records(targetbank) if t['id']==tid)
   evidence.append({'topic_id':tid,'question':t['question'],'coverage':t['coverage']})
  starter_decisions.append({'starter_id':old['id'],'starter_subject':old.get('title',old['question']),
      'decision':'reviewed_primary_home_referral' if any(t.split('-')[1]!=n for t in targets) else 'reviewed_scope_mapping',
      'target_ids':targets,'coverage_evidence':evidence,
      'reason':'The individual scopes above identify the intended treatment. Negative safety, permission and unsupported-guarantee starter headings operate as constraints on the mapped episode, not extra counted videos.'})
 gap_decisions=[]
 for gap in before.get('open_coverage',[]):
  gap_decisions.append({'original_gap':gap,'decision':'retain_primary_home_and_case_research_boundary',
   'target_ids':['BANK-012-030'] if n=='345' else added,
   'reason':'Habitability remains a linked primary012 proposal; mission, spectrum, sampling and competing-model evidence are later case research, not additional counts or a claim of verified coverage.' if n=='345' else 'See the individually scoped additions and remaining case research notes.'})
 bank_decisions=[v for v in decisions.values() if any(i.split('-')[1]==n for i in v['ids'])]
 audit['banks'][n]={'reviewed_before_ids':[t['id'] for t in before['topics']],
    'starter_decisions':starter_decisions,'gap_decisions':gap_decisions,'added_ids':added,
    'organization_decision':'Preserved local questions regrouped by actual subjects and original learning level.' if int(n)<=215 else 'Retained subject subcategories; added bounded missing branches where the review found a distinct output.',
    'depth_decision':{'existing_scoped_questions':len(before['topics']),'additional_scoped_questions':len(added),
       'decision':'Expanded missing subjects and repaired overbroad mappings; no target count was used.' if added else 'Retained the existing subject treatment after review; no paraphrase was added to equalize bank counts.',
       'reviewed_subjects':[c['title'] for c in b['categories']]},
    'semantic_decisions':bank_decisions,
    'remaining_work':[{'kind':'case_and_source_research','question_ids':[t['id'] for c,t in m.records(b)],
      'scope':'Every listed question remains a proposal. Named-case selection where a scope calls for it, actual text/records, current permissions and rules, competing evidence and script-level claim checks remain before production.'}],
    'exhaustive_claim':False}
 b['counts']={'categories':len(b['categories']),'proposed_topics':len(m.records(b))}
 b['coverage_review'].update({'editorial_pass':'2026-10-23 individual scope review','review_record':'Scripts/editorial_review_185_367.json',
   'starter_mapping_review':'all archived starter subjects reviewed against individual scopes; negative constraints remain explicit',
   'semantic_review':'both saved candidate shortlists reviewed; root consolidates retirement recommendations',
   'exhaustive_coverage_claimed':False})
 b['integration_stage']='editorially_reviewed_scoped_proposals_research_pending'
 m.write(d/'IN_DEPTH_TOPIC_BANK.json',b);m.render(b,d)

errors=[e for n,b in banks.items() for e in m.check_bank(b,m.home(n))]
audit['validation']={'banks':len(banks),'errors':errors,'starter_decisions':sum(len(b['starter_decisions']) for b in audit['banks'].values()),
 'reviewed_before_records':sum(len(b['reviewed_before_ids']) for b in audit['banks'].values()),
 'candidate_pairs_reviewed':len(expected),'duplicate_recommendations':len(recommendations),
 'new_active_before_root_retirements':sum(len(b['added_ids']) for b in audit['banks'].values())}
m.write(HERE/'editorial_review_185_367.json',audit)
print(json.dumps(audit['validation'],indent=2))
assert not errors
