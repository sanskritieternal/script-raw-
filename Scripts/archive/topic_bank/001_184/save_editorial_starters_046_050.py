from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Save the individually selected starter mappings for five detailed banks."""
from pathlib import Path
import manage_all_topic_banks as m

HERE=Path(__file__).resolve().parents[3]
BASE=m.read(HERE/'editorial_review_inputs/before_editorial_pass.json')['banks']
banks={f'{n:03d}':m.read(m.home(f'{n:03d}')/'IN_DEPTH_TOPIC_BANK.json') for n in range(46,51)}
def find(n,phrase):
 hits=[t['id'] for c,t in m.records(banks[n]) if phrase.casefold() in t['question'].casefold()]
 assert len(hits)==1,(n,phrase,hits)
 return hits[0]
def local(n,*nums):return [f'BANK-{n}-{i:03d}' for i in nums]

routes={
 '046':[
  [find('046','post-earthquake building surveys')],
  [find('046',"warning's usable lead time")],
  [find('046','uncertain rainfall')],
  [find('046','wildfire evacuation bottleneck')],
  ['BANK-185-034'],
  [find('046','disabled evacuee')],
  [find('046','supplies accumulate')],
  local('046',37,48),
  local('046',24),
  [find('046','2011 Tohoku')],
  [find('046','shelters in Bangladesh')],
  local('046',32,36)],
 '047':[
  ['BANK-047-013','BANK-422-030'],
  [find('047','recover from a disturbance')],
  [find('047',"around a jet engine's core")],
  local('047',45),local('047',22),
  [find('047','weather-related route decision')],
  local('047',30),['BANK-234-031'],local('047',17),local('047',26),local('047',27,29),
  [find('047','general-aviation accident totals')]],
 '048':[
  [find('048','ship that floats adequately')],
  [find('048','ship that floats adequately'),'BANK-048-045'],
  [find('048','celestial navigation connect')],
  [find('048','modern bridge displays')],local('048',29),
  [find('048','shipping lines share vessel capacity')],local('048',31),
  [find('048',"ship's flag state")],local('048',17),local('048',13,37),local('048',45),
  [find('048','resident migrant neighborhood')]],
 '049':[
  local('049',18),local('049',13,17),local('049',26),
  [find('049','captive-redemption')],local('049',29),
  [find('049',"Australia's convict system")],
  [find('049','separate Robin Hood stories')],local('049',31),local('049',21),local('049',23,39),local('049',16,41),local('049',42)],
 '050':[
  ['BANK-050-025','BANK-048-040'],local('050',21,22),
  [find('050','settlement disappear from later survey records')],local('050',17),
  [find('050','magnetic survey detect')],
  [find('050','side-scan sonar image')],
  [find('050',"detector's discrimination label")],
  ['BANK-050-041','BANK-002-046'],
  [find('050','heritage authority evaluate')],local('050',27),local('050',39),local('050',34,48)]}

case_focus={
 'BANK-046-024':'Selected case boundary: use the 2004 Indian Ocean tsunami to investigate source, propagation and local coastline effects through later-identified scientific records. This is an editorial case selection; no record has been researched or verified here.',
 'BANK-046-032':'Selected case boundary: choose one documented urban-flood response and follow how resident initiatives and spontaneous volunteers connected with formal coordination. Preserve disagreement and role limits; the case and records remain to be researched.',
 'BANK-046-036':'Related case boundary: in the same selected urban-flood setting, distinguish immediate volunteer coordination in032 from household and community recovery networks over subsequent months.',
 'BANK-049-031':'Selected case boundary: investigate dacoity classifications in a clearly identified colonial jurisdiction and period. Compare recorded acts, administrative terminology and community accounts without presuming either fabricated charges or resistance from the label alone.',
 'BANK-050-039':'Selected case boundary: examine filming access to a legally protected wreck, distinguishing site entry, filming, research, artifact disturbance and recovery permissions. Actual status and permit requirements remain for dated jurisdiction-specific official research.'}

audit={'date':'2026-10-24','source_verification':'not_performed','exhaustive_claim':False,'banks':{}}
errors=[]
for n,b in banks.items():
 d=m.home(n);rs={t['id']:t for c,t in m.records(b)}
 for tid,text in case_focus.items():
  if tid in rs:rs[tid]['additional_scope']=text
 starters=[t for c in b['prior_initial_map']['categories'] for t in c['topics']]
 assert len(starters)==len(routes[n])==12
 decisions=[]
 for old,targets in zip(starters,routes[n]):
  b.setdefault('starter_concept_crosswalk',{})[old['id']]=targets
  evidence=[]
  for tid in targets:
   tn=tid.split('-')[1];tb=banks.get(tn)
   if tb is None:tb=m.read(m.home(tn)/'IN_DEPTH_TOPIC_BANK.json')
   t=next(t for c,t in m.records(tb) if t['id']==tid)
   evidence.append({'topic_id':tid,'question':t['question'],'coverage':t['coverage'],
                    **({'additional_scope':t['additional_scope']} if t.get('additional_scope') else {})})
  decisions.append({'starter_id':old['id'],'starter_title':old.get('title',old['question']),
   'target_ids':targets,'scope_evidence':evidence,
   'decision':'reviewed_primary_home_referral' if any(t.split('-')[1]!=n for t in targets) else 'mapped_to_individually_reviewed_scope',
   'reason':'Selected against the actual question and coverage, including the explicit named-case boundary where present. Weak lexical matches were rejected; a shared title alone was not treated as coverage.'})
  for tid in targets:
   if tid.split('-')[1]!=n:
    # Starter links themselves supply navigation to the existing primary; no duplicate episode is added.
    pass
 before=BASE[n];before_ids={t['id'] for t in before['topics']}
 audit['banks'][n]={'reviewed_before_ids':[t['id'] for t in before['topics']],
   'starter_decisions':decisions,'added_ids':[tid for tid in rs if tid not in before_ids],
   'gap_decisions':[{'original_gap':g,'decision':'reviewed_against_scoped_proposals','reason':'See the explicit starter mappings and additions; source verification remains pending.'} for g in before.get('open_coverage',[])],
   'depth_decision':'Reviewed every original starter against all current question/scope pairs; added missing mechanisms and institutions, used existing primary homes, and selected named cases within existing scope where that avoids a name-only clone.',
   'remaining_work':'Actual case records, current permissions and rules, competing evidence and script-level claims remain to be researched; these mappings do not certify factual findings.'}
 m.write(d/'IN_DEPTH_TOPIC_BANK.json',b);m.render(b,d);errors.extend(m.check_bank(b,d))
 # All baseline original fields remain byte-for-value equivalent, apart from the snapshot category tag.
 live={t['id']:t for c,t in m.records(b)}
 live.update({t['id']:t for t in b.get('retired_duplicate_proposals',[])})
 for old in before['topics']:
  assert old['id'] in live
  assert all(live[old['id']].get(k)==v for k,v in old.items() if k!='category_id'),old['id']

audit['validation']={'banks':len(banks),'starter_decisions':sum(len(b['starter_decisions']) for b in audit['banks'].values()),
 'added_since_editorial_baseline':sum(len(b['added_ids']) for b in audit['banks'].values()),
 'new_proposals_in_this_starter_repair':sum(len(g['topics']) for gs in m.read(HERE/'editorial_starter_gap_additions_046_050.json').values() for g in gs),
 'errors':errors}
m.write(HERE/'editorial_starters_046_050.json',audit)
print(audit['validation'])
assert not errors
