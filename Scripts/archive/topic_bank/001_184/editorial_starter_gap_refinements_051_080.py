from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

import json
from pathlib import Path
from editorial_authoring_002_184 import parse
import manage_all_topic_banks as m
p=Path('Scripts/editorial_pass_002_184.json');d=m.read(p)
extra=parse(r'''
[055]
@Cosmological time|Model coordinates and clocks|advanced
How can a cosmological model assign a cosmic time without establishing one universal present for every observer?|Compare idealized comoving observers, expansion, proper time, homogeneity assumptions and local clock readings; distinguish a model coordinate from settling a philosophical debate about what exists.|4
[060]
@Commercial marks|Ownership and authentication|intermediate
How did merchant marks help identify goods or ownership when several traders shared a route?|Compare a dated set of marks on objects and records, reuse, copying, literacy, custody and commercial institutions; distinguish a claim of ownership from proof that a specific merchant made the object.|6
[062]
@Computer firmware|Version compatibility and recovery|advanced
What should a firmware-update explanation establish about compatibility and recovery before describing a change?|Compare exact model, supported version, release notes, configuration retention, recovery documentation and vendor responsibilities; exclude flashing instructions, bypasses or a guarantee that updating fixes an observed fault.|7
[067]
@Field ethics|Patience and staged animal action|advanced
How can a nature documentary show behavior without inducing it merely to obtain a shot?|Compare remote observation, waiting, existing footage, disclosure, baiting risks, location disturbance and professional ethical review; do not provide baiting methods or treat an altered scene as spontaneous evidence.|5,6
[070]
@Labor-market evidence|Informal work and survey categories|advanced
How can employment statistics count informal work differently from a survey of people who hold formal jobs?|Compare reference period, hours, paid and unpaid family work, self-employment, multiple jobs and survey coverage; distinguish a statistical category from an individual's legal employment status.|8
[075]
@Pilgrimage institutions|Festival crowd governance|advanced
How do festival institutions coordinate access, service and communication when a pilgrimage town's population changes sharply?|Compare dated public planning records, transport, vendors, volunteers, disability access, warnings and evaluation with participant accounts; exclude tactical crowd-control plans or actual capacity certification.|7
[079]
@Mixed-media processes|Surface compatibility|intermediate
Why can a mixed-media layer fail even when the materials looked compatible in the first photograph?|Compare support, absorbency, adhesion, drying, flexibility, aging and documented manufacturer limits through nonhazardous labeled samples; exclude solvent recipes or promises of conservation permanence.|7
[080]
@Sound and viewpoint|Auditory perspective|intermediate
How can a film's sound place viewers inside a character's perception without changing the camera's viewpoint?|Compare level, filtering, reverberation, selective audibility, transitions and the scene's established sound world through a rights-cleared sequence; distinguish a supported interpretation from claims about creator intent.|4
''')
for nid,v in extra.items():d.setdefault(nid,{'groups':[]})['groups'].extend(v['groups'])
m.write(p,d);m.write(Path('Scripts/editorial_pass_051_080.json'),{k:v for k,v in d.items() if 51<=int(k)<=80})
# Add precise boundaries to existing scopes without changing any original fields.
notes={
'BANK-069-051':'For randomized studies, identify the assignment unit, comparison group, noncompliance, classroom spillovers and what causal claim the design permits; keep observational adaptation evidence distinct.',
'BANK-071-034':'Include outstanding commitments, next obligations, renegotiated deadlines and capacity in the review; a completed-work inventory alone cannot establish whether future promises remain feasible.',
'BANK-077-013':'Route detailed meditation-method, tradition and research questions to niche278; the local topic concerns participating in a wellness service and evaluating its stated outcomes.'}
for tid,note in notes.items():
 nid=tid.split('-')[1];p=next(Path('topics').glob(nid+'*/IN_DEPTH_TOPIC_BANK.json'));b=m.read(p)
 t=next(t for c in b['categories'] for t in c['topics'] if t['id']==tid);t['additional_scope']=note;m.write(p,b);m.render(b,p.parent)
