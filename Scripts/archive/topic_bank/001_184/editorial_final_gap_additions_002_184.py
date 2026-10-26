import json
from pathlib import Path
from editorial_authoring_002_184 import parse
p=Path('Scripts/editorial_pass_002_184.json');d=json.loads(p.read_text(encoding='utf-8'))
for nid,v in parse(r'''
[118]
@Discovery evidence|Independent reproduction|advanced
What had to be independently reproduced before a reported discovery became an accepted explanation?|Compare original observations, methods disclosure, independent groups, failed attempts, revised apparatus and competing interpretations through one named historical research program; distinguish acceptance from unanimity or proof beyond revision.|4
[142]
@Experimental archaeology|Interpreting fire-making reconstructions|advanced
What can a professionally controlled fire-making reconstruction establish about prehistoric technique and what remains uncertain?|Compare archaeological traces, material assumptions, environmental conditions, expertise, replication and negative results through published records; exclude instructions for ignition, fuel preparation or conducting a fire experiment.|4
[164]
@Comparative indicators|Transport efficiency boundaries|advanced
How can the ranking of transport modes change when efficiency is measured per vehicle, passenger or completed journey?|Compare occupancy, distance, transfers, energy boundaries, freight allocation, access and uncertainty with hypothetical comparable journeys; distinguish a transparent indicator from a universal best mode.|6
''').items():d.setdefault(nid,{'groups':[]})['groups'].extend(v['groups'])
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
