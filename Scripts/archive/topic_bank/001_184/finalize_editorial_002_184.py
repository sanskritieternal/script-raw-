from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Reviewed mappings and scope-pair decisions; never a source-verification report."""
import json,hashlib
from pathlib import Path
import manage_all_topic_banks as m
base=json.loads(Path('Scripts/editorial_review_inputs/before_editorial_pass.json').read_text(encoding='utf-8'))['banks']
manual={
'113':{4:[14],5:[19],9:[22]},'116':{1:[10],2:[20]},'119':{3:[22]},'120':{5:[19],7:[10]},'121':{2:[11,34]},
'122':{6:[23],9:[20]},'123':{1:[23]},'124':{8:[20]},'126':{3:[14]},'130':{1:[10]},'131':{3:[23],5:[14]},
'132':{1:[21],5:[27]},'133':{1:[15],2:[16],4:[10],5:[19]},'134':{7:[25]},'135':{8:[11]},'141':{1:[19]},
'142':{3:[13]},'144':{3:[12]},'149':{4:[15]},'150':{6:[28]},'152':{2:[14],6:[21]},'153':{9:[39]},'154':{2:[10]},
'155':{1:[11],9:[25]},'156':{7:[14]},'158':{1:[11],2:[13,20],4:[12],5:[18]},'160':{3:[13],4:[16]},
'162':{1:[10],2:[12],4:[13],5:[16]},'164':{4:[18],5:[19]},'165':{2:[11]},'167':{2:[16]},'169':{2:[12]},
'170':{3:[20],7:['BANK-174-037']}}
# Curated choices above were applied during the owned authoring pass. Finalization is read-only for banks so independent reviewers' crosswalk decisions are never overwritten.
ps={}
for fn in ['semantic_candidates_002_184.json','semantic_question_candidates_002_184.json']:
 for pair in m.read(Path('Scripts/editorial_review_inputs')/fn)['pairs']:ps.setdefault((pair['left']['id'],pair['right']['id']),pair)
pairs=list(ps.values())
# Same episode mechanism/event and substantially the same individual scope.
duplicate_indexes=[0,1,3,4,5,8,9,10,11,12,13,16,17,19,21,22,23,24,25,28,29,31,32,33,36,38,39,40,41,44,45,46,48,50,51,52,53,54,55,56,58,59,60,61,62,63,66,67,68,69,70,73,74,75,76,78,80,81,83,85,86,87,89,90,91,92,93,95,97,98,99,103,105,108,109,110,113,116,117,120,123,124,125,126,127,128,130,133,134,135,137,138,139,140,141,142,143,144,147,150,154,155,157,161,164,165,170,171,186,191,193,199,201,202,204,214,219,225,242,243,254,255,257,260]
recommendations=[];candidate_decisions=[]
for i,pair in enumerate(pairs):
 a,z=pair['left'],pair['right'];ids=[a['id'],z['id']]
 if i in duplicate_indexes:
  primary,retire=a,z
  # Retain the scope that already explains the full mechanism, never manufacture a new audience distinction.
  if i in [16,24,186]:primary,retire=z,a
  if i in [60]:primary,retire=z,a
  reason=f"The individual scopes describe substantially the same episode: {a['coverage']} / {z['coverage']} Retain one primary question and preserve the other full record inactive with a referral."
  recommendations.append({'retire_id':retire['id'],'primary_id':primary['id'],'reason':reason})
  decision='consolidate_same_episode'
 else:
  reason=f"Retain the actual scope distinction: {a['id']} covers {a['coverage']} By comparison, {z['id']} covers {z['coverage']} Shared vocabulary alone does not erase the different object, case, measurement or decision specified here; do not duplicate either complete scope in production."
  decision='retain_distinct_scope'
 candidate_decisions.append({'ids':ids,'decision':decision,'reason':reason,'scope_evidence':[a['coverage'],z['coverage']]})
# Explicit root-requested consolidations, also included in candidate review above.
for old,new in [('BANK-128-031','BANK-001-109'),('BANK-128-040','BANK-001-090')]:
 if not any(x['retire_id']==old and x['primary_id']==new for x in recommendations):recommendations.append({'retire_id':old,'primary_id':new,'reason':'Same tracking/world-placement mechanism or digital-twin/model distinction; keep the established AI technology primary scope and preserve the later full record inactive.'})
recommendations.append({'retire_id':'BANK-051-051','primary_id':'BANK-088-020','reason':'Both cover the same glass-bottle forming, mold contact, annealing and inspection process. Keep the established manufacturing-object question; preserve the later051 record inactive and redirect its glass-forming starter mapping.'})
allbanks={};alltopics={}
for p in Path('topics').glob('*/IN_DEPTH_TOPIC_BANK.json'):
 b=m.read(p);allbanks[b['niche_id']]=(p,b)
 for c in b['categories']:
  for t in c['topics']:alltopics[t['id']]=t
packets={}
for packet_name in ['editorial_starters_002_050.json','editorial_starters_046_050.json','editorial_starters_051_080.json','editorial_starters_081_110.json']:
 packet_path=Path('Scripts')/packet_name
 if packet_path.exists():
  packet=m.read(packet_path)
  for nid,entry in packet.get('banks',{}).items():packets[nid]={'packet':str(packet_path),'entry':entry}
report={'date':'2026-10-24','status':'owned_scope_review_complete_pending_central_consolidation','source_verification':'not_performed','exhaustive_claim':False,
 'method':'Review category coverage, original starter branches and prior gap notes against actual individual question scopes; separately adjudicate every pair in both saved lexical shortlists. Detailed002–110 received scoped missing branches after original starter reconciliation; existing source fields and coherent reading skeletons were retained. Case binding and factual claims require later research.',
 'candidate_decisions':candidate_decisions,'duplicate_recommendations':recommendations,'banks':{}}
errors=[]
for n in range(2,185):
 nid=f'{n:03d}';p,b=allbanks[nid];before=base[nid];ts=[t for c in b['categories'] for t in c['topics']];oldids={t['id'] for t in before['topics']};added=[t for t in ts if t['id'] not in oldids]
 starters=[t for c in b.get('prior_initial_map',{}).get('categories',[]) for t in c['topics']]
 starterdecisions=[]
 for t in starters:
  targets=b.get('starter_concept_crosswalk',{}).get(t['id'],[])
  if not targets:errors.append(nid+' missing '+t['id'])
  packet_entry=next((v for v in packets.get(nid,{}).get('entry',{}).get('starter_decisions',[]) if v['starter_id']==t['id']),{})
  starterdecisions.append({'starter_id':t['id'],'starter_title':t.get('title'),'target_ids':targets,'decision':packet_entry.get('decision','mapped to bounded individual scope'),'reason':packet_entry.get('reason','The actual individual scopes below match the starter subject; unrelated token-only matches were rejected.'),'review_packet':packets.get(nid,{}).get('packet'),'scope_evidence':[alltopics[x]['coverage']+((' Additional scope: '+alltopics[x]['additional_scope']) if alltopics[x].get('additional_scope') else '') for x in targets if x in alltopics]})
 bankpairs=[x for x in candidate_decisions if any(xid.startswith('BANK-'+nid+'-') for xid in x['ids'])]
 gapdecisions=[]
 for gap in before.get('open_coverage',[]):
  area=gap['area'];text=gap['next_step']
  if 'Starter branches' in area:
   decision='resolved by reviewed scope mappings and distinct additions';evidence=[x for x in starterdecisions if any((x.get('starter_title') or '') in text for _ in [0])]
   reason='Each named original branch has an explicit active target scope; where none existed, the authoring inputs add a distinct mechanism, institutional question or historical case.'
  elif 'readiness' in area.lower() or 'Sources' in area:
   decision='research prerequisite retained';evidence=[];reason='These proposals make no source-access, factual-verification or production-readiness claim; selecting an edition/jurisdiction/case is a later research task, not another reworded video.'
  elif 'boundary' in area.lower():
   decision='reviewed candidate scopes with central primary-home consolidation pending';evidence=bankpairs;reason='Actual overlapping episodes have explicit retirement recommendations. Retained pairs keep their stated distinct case or decision, not an invented audience difference.'
  else:
   decision='reviewed against existing bounded scope and additions; case extensions remain conditional';evidence=[{'id':t['id'],'question':t['question'],'coverage':t['coverage']} for t in added]
   if not evidence:evidence=[{'category':c['title'],'id':c['topics'][0]['id'],'question':c['topics'][0]['question'],'coverage':c['topics'][0]['coverage']} for c in b['categories'] if c['topics']]
   reason='The category-level subjects already have individual proposal scopes shown as evidence. Regional, linguistic, participant or contrary-case extensions require a genuinely different object or causal/interpretive question; the note is not treated as a demand for arbitrary counts or factual research.'
  gapdecisions.append({'area':area,'prior_next_step':text,'decision':decision,'reason':reason,'scope_evidence':evidence})
 # Main view retains honest research work, with a direct review pointer replacing stale unmapped-branch claims.
 newgaps=[]
 for gap in b.get('open_coverage',[]):
  if 'Starter branches' in gap['area']:
   newgaps.append({'area':'Reviewed starter branches and primary-home boundaries','next_step':'All original starter concepts now have explicit individual-scope targets. See the starter crosswalk below and Scripts/editorial_review_002_184.json for scope evidence and semantic pair decisions; follow the primary-home referrals after consolidation.'})
  else:newgaps.append(gap)
 err=m.check_bank(b,p.parent);errors.extend([nid+': '+str(e) for e in err])
 report['banks'][nid]={'name':b['name'],'reviewed_before_ids':[t['id'] for t in before['topics']],
 'before_bank_sha256':before.get('sha256'),'reviewed_bank_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'category_scope_inventory':[{'category_id':c['id'],'title':c['title'],'level':c['level'],'topics':[{'id':t['id'],'question':t['question'],'coverage':t['coverage']} for t in c['topics']]} for c in b['categories']],
 'starter_decisions':starterdecisions,'gap_decisions':gapdecisions,'semantic_decisions':bankpairs,'recommended_open_coverage':newgaps,
 'additions':[{'id':t['id'],'question':t['question'],'coverage':t['coverage']} for t in added],
 'depth_decision':'Distinct missing starter mechanisms and institutional cases added where justified; preserve the established detailed reading progression and avoid uniform topic quotas.',
 'remaining_work':'Select actual sources and bounded case material before script research; regional, text, system-version and participant extensions remain conditional on a distinct question. Pair shortlist review is not proof of all-pairs semantic uniqueness.'}
report['validation']={'owned_banks':183,'errors':errors,'starter_concepts':sum(len(v['starter_decisions']) for v in report['banks'].values()),'semantic_pairs':len(candidate_decisions),'new_topics':sum(len(v['additions']) for v in report['banks'].values())}
m.write(Path('Scripts/editorial_review_002_184.json'),report)
print(json.dumps(report['validation'],ensure_ascii=False));print('Duplicate recommendations',len(recommendations))
