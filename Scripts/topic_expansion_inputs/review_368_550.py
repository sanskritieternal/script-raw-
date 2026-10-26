import json
from pathlib import Path
p=Path('Scripts/expansion_368_550.json'); data=json.loads(p.read_text(encoding='utf-8'))
rejected={'BANK-379-005','BANK-383-007','BANK-420-004'}
for payload in data.values():
    for group in payload['groups']:
        for t in group['topics']:
            if 'covers_starter_ids' in t:
                t['covers_starter_ids']=[x for x in t['covers_starter_ids'] if x not in rejected]
flat={}
for line in Path('Scripts/topic_expansion_inputs/368_550_authored.txt').read_text(encoding='utf-8-sig').splitlines():
    if line.strip():
        nid,title,level,q,scope=line.split('|');flat.setdefault(nid,[]).append(q)
manual={
'540':[1,2,3,4,5,6,8,7,9,10,11,12,13,14,15,16,18,17,19,20],
'541':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,16,17],
'542':[2,3,4,5,6,7,8,9,10,11,1,14,12,13],
'543':[1,2,3,4,5,6,7,8,2,10,11,12,4,13],
**{str(n):list(range(1,13)) for n in range(544,551)}}
opens={
'540':('Regional and performance traditions','Commission distinct proposals on oral-performance lineages, women-centered regional retellings and regional reception of the Uttara Kanda; avoid treating versions as interchangeable.'),
'541':('Teaching, reception and less familiar parvas','Add bounded proposals on Anushasana Parva, ritual narratives, named regional performance traditions and commentarial disagreements beyond the selected character dilemmas.'),
'542':('Further seasonal and regional observances','Add named harvest festivals, regional new-year traditions, local temple calendars and specific community accounts of public-festival administration.'),
'543':('Further bhakti languages and poets','Extend beyond the selected poets to named Alvar, Nayanmar, Kannada and Bengali traditions with attributed texts and individual interpretive questions.'),
'544':('Households and regional Egyptian histories','Add Nubian-Egyptian relations, craft production, domestic religion and regional archaeology beyond royal-period overviews.'),
'545':('Languages and everyday Mesopotamia','Add multilingual administration, food production, nonelite households, urban archaeology and later Babylonian scholarship as separate bounded proposals.'),
'546':('Cricket disciplines and participation','Add wicketkeeping, running, fielding, domestic pathways, accessibility and specific regional cricket histories with distinct analytical scopes.'),
'547':('Football beyond elite match analysis','Add grassroots development, referee pathways, youth protection, disability football and region-specific supporter histories.'),
'548':('Further design media and users','Add packaging systems, multilingual typography, motion graphics and public-information testing with defined audiences and production constraints.'),
'549':('Further finishing disciplines','Add documentary transcript editing, visual-effects turnovers, conform troubleshooting and localization workflows through concrete project constraints.'),
'550':('Recording, acoustics and musical traditions','Add microphone selection, room acoustics, synthesis, recording-session organization and culturally situated production methods beyond the current mix-and-delivery focus.')}
for nid,indices in manual.items():
    lookup={t['question']:t for g in data[nid]['groups'] for t in g['topics']}
    for oldindex,newindex in enumerate(indices,1):
        oldid=f'BANK-{nid}-{oldindex:03d}';t=lookup[flat[nid][newindex-1]]
        for g in data[nid]['groups']:
            for x in g['topics']:
                if oldid in x.get('covers_starter_ids',[]): x['covers_starter_ids'].remove(oldid)
        t.setdefault('covers_starter_ids',[]).append(oldid)
    area,next_step=opens[nid];data[nid]['open_coverage']=[{'area':area,'next_step':next_step}]
# Restore false-match concepts to the explicit crosswalk review queue.
for nid,concept in [('379','Rigging constraints'),('383','Retention by episode'),('420','AC versus DC charging')]:
    data[nid]['open_coverage'].append({'area':concept,'next_step':'Author a dedicated proposal or map an explicitly bounded treatment; similar vocabulary alone does not establish coverage.'})
p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('Reviewed exact-term mappings; rejected3; explicitly mapped all starter concepts540–550.')
