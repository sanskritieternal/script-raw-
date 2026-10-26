from pathlib import Path as _archive_script_path_
import sys as _archive_sys_
_archive_sys_.path.insert(0, str(_archive_script_path_(__file__).resolve().parents[3]))

import argparse
import manage_all_topic_banks as m
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('start',type=int);ap.add_argument('end',type=int);args=ap.parse_args()
    values=m.read(m.ROOT/'Scripts/editorial_duplicate_scope_review.json')
    for i,d in enumerate(values[args.start:args.end],args.start):
        print('\n',i,d['retire_id'],'->',d['primary_id'])
        for key in ('retire_record','primary_record'):
            t=d[key]
            print(t['question'],'|',t['coverage']) if t else print('Already inactive or missing; inspect archive')
