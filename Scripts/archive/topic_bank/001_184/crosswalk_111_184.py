from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

import json
from pathlib import Path
import manage_all_topic_banks as h
# Manually reviewed conceptual matches to NEW individually authored question positions.
# Unmapped starter concepts remain a visible coverage-review checklist, never a completeness claim.
DATA=r'''
111|1:2,2:1,3:9,4:5,5:6,6:7,7:10,8:4,9:11
112|1:9,2:3,3:5,4:4,5:3,6:5,7:7
113|1:3,3:7
114|1:5,4:3,5:11,6:10,9:9
115|2:1,3:5,4:11,8:9,9:10
116|3:1,4:4,6:7,8:9,9:10
117|5:7,6:8
118|1:1,5:11,8:4,9:8
119|1:2,2:4,7:2,9:13
120|1:1,2:2,4:6,6:6,8:7,9:5
121|1:2,3:10,4:5,5:8
122|2:3,4:1,5:4,7:7
123|2:5,3:7,4:4,5:2,8:6,9:11
124|4:7,6:5,9:10
125|1:1,3:1,5:5,6:7,7:4,9:9
126|1:1,2:1,4:11,7:4,8:10,9:9
127|1:2,2:3,4:7,9:11
128|1:2,2:3,3:7,4:3,5:4,6:6,7:10,8:9
129|1:1,2:2,3:3,4:5,7:4,8:9,9:12
130|2:4,4:5,5:1,6:8,7:12,8:2,9:8
131|1:2,2:4,4:5,6:5,7:10,9:11
132|2:1,3:2,4:3,6:4,9:5
133|3:4,6:3,7:5,8:8
134|1:3,2:1,4:6,5:7,8:12,9:9
135|1:2,2:7,3:3,4:9,5:5,7:12,9:11
136|1:2,2:5,3:8,4:4,6:7,7:12,8:7,9:6
137|1:1,2:1,6:5,7:10,9:3
138|1:1,2:4,3:2,4:9,7:3,8:7
139|1:4,2:1,3:7,4:2,5:6
140|1:1,2:2,3:4,4:9,8:8,9:11
141|2:2,3:3,7:6,8:5,9:12
142|1:1,2:2,5:5,6:5,7:11,8:12,9:12
143|5:2,6:3,7:1,8:11,9:8
144|4:4,5:5,6:7,7:5,8:6
145|1:1,2:5,3:4,5:3,6:7
146|4:2,6:5,7:4,8:4,9:12
147|1:1,2:2,4:7,5:7,7:6,9:9
148|4:10,5:10,6:6,7:4,8:4,9:9
149|1:2,3:1,5:4,6:7,7:10,8:9,9:9
150|4:6,7:11,8:8,9:1
151|1:1,2:1,3:1,4:2,5:7,6:3,7:5,8:6,9:10
152|1:1,4:5,5:6,7:9,8:9,9:4
153|1:1,2:4,4:9,5:10,6:10,8:11
154|1:8,4:7,6:5,7:9,8:12,9:10
155|2:9,3:5,4:7,7:9,8:12
156|1:1,4:8,5:7,8:11
157|1:1,3:4,4:3,5:6,7:8
158|3:1,7:4,8:5,9:11
159|1:3,2:4,3:1,4:5,5:9,6:8,8:10,9:3
160|1:2,2:4,5:3,6:8,7:6,8:9,9:12
161|1:1,2:2,3:3,5:5,6:11,7:9,8:9
162|7:1,9:7
163|1:1,3:3,4:6,5:2,6:5,7:9,8:4,9:10
164|1:4,2:4,3:6,7:5,8:5,9:3
165|1:1,3:5,4:2,5:7,6:9,7:1,8:1,9:11
166|3:5,5:8,6:6,7:1,9:1
167|5:7,7:1,8:8,9:11
168|1:3,2:1,3:6,4:5,5:5,6:10
169|1:2,4:9,5:9,7:10,8:10,9:10
170|1:4,4:10,5:4,6:4
171|2:2,4:11,7:1,9:12
172|1:2,2:3,3:10,4:12,5:12,6:12,7:5,8:5,9:1
173|1:1,2:5,3:6,4:3,5:4,6:6,7:9,8:8,9:10
174|1:2,3:8,4:1,6:3,7:5,8:10,9:12
175|1:1,2:2,5:1,7:11,8:8,9:10
176|1:1,2:7,3:2,4:12,7:9,8:2,9:10
177|1:7,4:1,5:2,6:6,7:4,8:1,9:9
178|1:4,2:3,3:7,4:6,6:5,7:1,9:9
179|1:5,2:8,4:5,6:2,8:4,9:11
180|1:3,2:3,3:4,4:2,5:2,8:10,9:11
181|1:1,3:5,4:2,5:7,7:9,8:9
182|1:1,2:2,3:3,4:5,5:7,6:6,7:5,9:12
183|1:2,3:5,4:3,7:6,8:2,9:10
184|1:1,3:3,4:6,7:7,8:9
'''

def main():
 authored=json.loads(Path('Scripts/expansion_002_184.json').read_text(encoding='utf-8')); mapping={line.split('|')[0]:line.split('|')[1] for line in DATA.strip().splitlines()}
 summary=[]
 for n in range(111,185):
  nid=f'{n:03d}';directory=h.home(nid);bp=directory/'IN_DEPTH_TOPIC_BANK.json';b=h.read(bp)
  new_questions=[t['question'] for c in authored[nid] for t in c['topics']];byq={t['question']:t['id'] for c,t in h.records(b)}
  old=[t for c in b['prior_initial_map']['categories'] for t in c['topics']]
  cross={}
  for pair in mapping[nid].split(','):
   a,z=map(int,pair.split(':'));cross[old[a-1]['id']]=[byq[new_questions[z-1]]]
  b['starter_concept_crosswalk']=cross
  unmapped=[t.get('title',t['question']) for t in old if t['id'] not in cross]
  b['open_coverage']=[{'area':'Case and source readiness','next_step':'Select dated jurisdictions, editions, named sites, populations or product versions for the active proposals. Inspect actual sources before making factual claims; no research or production readiness was certified.'}]
  if unmapped:b['open_coverage'].append({'area':'Starter branches requiring a more precise coverage match','next_step':'; '.join(unmapped)+'. These are review leads; inspect preserved local cases before proposing an additional episode so overlapping coverage is not counted twice.'})
  b['open_coverage'].append({'area':'Regional and participant variation','next_step':'Compare less-visible regions, languages, participants and contrary cases within this niche; record substantive distinctions before adding another proposal.'})
  b['coverage_mapping_review']={'date':'2026-10-23','method':'Manual thematic cross-references to authored questions. A link is a navigation aid, not a claim that every aspect of a starter branch has been exhausted.','mapped_starter_concepts':len(cross),'unmapped_starter_concepts':len(unmapped)}
  h.write(bp,b);err=h.check_bank(b,directory);assert not err,err;h.render(b,directory);summary.append(dict(niche_id=nid,mapped=len(cross),open=unmapped))
 Path('Scripts/coverage_review_111_184.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('Mapped',sum(r['mapped'] for r in summary),'starter concepts across74 banks; remaining branches explicitly retained for review.')
if __name__=='__main__':main()
