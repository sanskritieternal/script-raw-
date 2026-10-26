from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

"""Merge explicit reviewer recommendations and expose conflicts before mutation."""
import argparse
from collections import defaultdict
from pathlib import Path
import manage_all_topic_banks as m

ROOT=Path(__file__).resolve().parents[4]
FILES=['editorial_duplicate_recommendations_root.json','editorial_review_002_184.json',
       'editorial_review_185_367.json','editorial_review_368_550.json']


def main():
    choices=defaultdict(dict);missing=[]
    for name in FILES:
        path=ROOT/'Scripts'/name
        if not path.exists():missing.append(name);continue
        obj=m.read(path)
        for d in obj.get('duplicate_recommendations',obj.get('decisions',[])):
            if not all(k in d for k in ('retire_id','primary_id','reason')):continue
            choices[d['retire_id']][d['primary_id']]=d
    conflicts={tid:list(targets.values()) for tid,targets in choices.items() if len(targets)>1}
    decisions=[next(iter(targets.values())) for tid,targets in choices.items() if len(targets)==1]
    report={'decisions':decisions,'conflicts':conflicts,'missing_audits':missing,
            'instruction':'Resolve conflicts and alias cycles by scope review before running consolidation. No automatic lexical retirement.'}
    m.write(ROOT/'Scripts/editorial_duplicate_decisions_draft.json',report)
    records={t['id']:t for nid in m.rows() for c,t in m.records(m.read(m.home(nid)/'IN_DEPTH_TOPIC_BANK.json'))}
    review=[]
    for tid,targets in sorted(choices.items()):
        for primary,decision in targets.items():
            review.append({'retire_id':tid,'primary_id':primary,'reason':decision['reason'],
                          'retire_record':records.get(tid),'primary_record':records.get(primary)})
    m.write(ROOT/'Scripts/editorial_duplicate_scope_review.json',review)
    print(f'{len(decisions)} unambiguous retirements; {len(conflicts)} conflicts; {len(missing)} missing audits.')
    for tid,ds in conflicts.items():print(tid,[(d['primary_id'],d['reason']) for d in ds])


if __name__=='__main__':main()
