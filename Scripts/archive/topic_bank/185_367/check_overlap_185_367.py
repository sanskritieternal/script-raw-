from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

import json
from collections import defaultdict
from pathlib import Path
import manage_all_topic_banks as m
q=defaultdict(list)
for d in (m.ROOT/'topics').iterdir():
 p=d/'IN_DEPTH_TOPIC_BANK.json'
 if not p.exists():continue
 b=m.read(p)
 for c,t in m.records(b):q[m.norm(t['question'])].append((t['id'],t['question']))
dups=[v for v in q.values() if len(v)>1 and any(185<=int(tid.split('-')[1])<=367 and tid.split('-')[1]!='281' for tid,_ in v)]
print(json.dumps(dups,ensure_ascii=False,indent=2))
