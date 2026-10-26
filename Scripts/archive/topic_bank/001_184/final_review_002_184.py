from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

import json,re
from pathlib import Path
from urllib.parse import unquote
import manage_all_topic_banks as h
SPECIAL={
'002':('Archives and regional cases','Further compare underrepresented African, Asian and Indigenous archive traditions, unresolved identifications, and negative findings; avoid duplicating an existing mystery dossier.'),
'003':('Regional and unequal visibility','Deepen site-by-site regional sequences, non-elite households, women\'s labor, and transmission across Prakrit, Tamil and other language corpora only where new cases differ from existing questions.'),
'004':('Textual and living variation','Select exact Sanskrit and regional-language editions, local oral traditions and deity-form interpretations; keep theological disagreements attributed and avoid asserting a single universal canon.'),
'005':('Contributor-led case studies','Build further consented documentary examples involving Deaf or non-speaking contributors, cross-language editing, community-controlled release and long-term correction.'),
'006':('Frontier evidence and competing models','Choose actual experiments, observations and mathematical formulations for the frontier proposals; compare contrary results and uncertainties before extending a broad conceptual question.'),
'007':('Versioned workflow evidence','Choose current named tool versions and real multilingual, screen-reader, export and migration test cases; retain failure cases and maintenance dates.'),
'008':('Jurisdiction and household variation','Choose dated product documents, tax jurisdictions, irregular-income scenarios, disability and caregiving contexts; all calculations remain educational assumptions until checked.'),
'009':('Populations and construct validity','Expand specific non-Western and multilingual study comparisons, measurement invariance, replications and conflicting theories without treating psychological constructs as diagnoses.'),
'010':('Access and affected-community evidence','Assess public court access, privacy restrictions, unresolved evidence disputes, corrections and victim/community participation for each named jurisdiction and case.')}
errors=[];summary=[];local_links=0
for n in range(2,185):
 nid=f'{n:03d}';directory=h.home(nid);bp=directory/'IN_DEPTH_TOPIC_BANK.json';b=h.read(bp)
 if n<=110:
  if nid in SPECIAL:
   area,detail=SPECIAL[nid];b['integration_stage']='preserved_detailed_draft_reviewed_coverage_open'
  else:
   source=[c for c in b['categories'] if c['id'] in b['local_reconciliation']['source_categories']]
   area='Further case and comparison depth';detail='Select distinct named cases, regional and language variants, overlooked participants, and contrary examples within '+', '.join(c['title'] for c in source[:3])+'. Review actual scopes before adding an episode; these are coverage directions rather than a claim that present questions exhaust the niche.'
  b['open_coverage']=[{'area':area,'next_step':detail},{'area':'Sources and readiness','next_step':'Inspect actual source access, dates, editions, versions, methods and competing evidence. No new source verification, research certification or production approval was performed.'},{'area':'Neighboring-niche boundary review','next_step':'Before producing an episode, compare related banks and assign one primary home. A lexical duplicate check does not establish semantic uniqueness across every pair.'}]
  b['coverage_review']={'status':'open_for_further_substantive_expansion','fixed_topic_target':None,'topic_cap':None,'source_verification':'not_performed','exhaustive_coverage_claimed':False}
  h.write(bp,b);h.render(b,directory)
 b=h.read(bp);errors.extend(h.check_bank(b,directory));rs=h.records(b)
 for name in ('IN_DEPTH_TOPIC_BANK.md','TOPIC_BANK_RECONCILIATION.md'):
  md=directory/name;content=md.read_text(encoding='utf-8');anchors=set(re.findall(r'<a id="([^"]+)"',content))
  if name=='IN_DEPTH_TOPIC_BANK.md':
   if f'**{len(rs)} active BANK proposals' not in content:errors.append(nid+': stale count')
   for c,t in rs:
    if t['id'] not in content or t['question'] not in content or t['coverage'] not in content:errors.append(nid+': missing content '+t['id'])
  for target in re.findall(r'\]\(([^)]+)\)',content):
   target=unquote(target)
   if '://' in target or target.startswith('mailto:'):continue
   local_links+=1;filename,_,fragment=target.partition('#')
   if filename:
    linked=md.parent/filename
    if not linked.exists():errors.append(nid+': missing local link '+target)
    elif fragment.startswith('bank-') and linked.suffix=='.md' and f'id="{fragment}"' not in linked.read_text(encoding='utf-8'):errors.append(nid+': missing linked anchor '+target)
   elif fragment not in anchors:errors.append(nid+': missing local anchor '+target)
 summary.append({'niche_id':nid,'proposals':len(rs),'categories':len(b['parent_categories']),'subcategories':len(b['categories']),'source_proposals_preserved':len(b['local_reconciliation']['source_records']),'starter_links':sum(len(v) for v in b.get('starter_concept_crosswalk',{}).values()),'retired_added_duplicates':len(b.get('retired_duplicate_proposals',[])),'stage':b['integration_stage']})
result={'range':'002-184','banks_checked':len(summary),'active_proposals':sum(x['proposals'] for x in summary),'starter_concepts_mapped':sum(x['starter_links'] for x in summary),'retired_added_duplicates':sum(x['retired_added_duplicates'] for x in summary),'local_links_checked':local_links,'errors':errors,'banks':summary,'limits':'Structural and preservation checks passed only if errors is empty. Source verification not performed. Semantic review removed31 overlapping drafted additions, but no exhaustive semantic uniqueness or exhaustive subject coverage is claimed.'}
Path('Scripts/validation_002_184.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='banks'},indent=2));assert not errors
