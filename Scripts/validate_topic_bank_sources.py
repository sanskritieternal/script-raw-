"""Independently compare the current catalog records with the supplied unchanged ZIP."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

from manage_all_topic_banks import ARCHIVE, TOPICS, read, records, rows, home, write


def validate(archive_path,report_path):
    errors=[];entries=[];preserved_records=0;prior_archives=0;retired_source_records=0
    with zipfile.ZipFile(archive_path) as archive:
        manifest=json.loads(archive.read('SHA256.json'))
        for nid,row in rows().items():
            directory=home(nid)
            member=f'files/topics/{directory.name}/IN_DEPTH_TOPIC_BANK.json'
            raw=archive.read(member)
            if hashlib.sha256(raw).hexdigest()!=manifest[member.removeprefix('files/')]:
                errors.append(f'{nid}: ZIP manifest mismatch')
            source=json.loads(raw)
            current=read(directory/'IN_DEPTH_TOPIC_BANK.json')
            kind=source.get('bank_type','detailed_pilot')
            if kind=='subject_map':
                archived=current.get('prior_initial_map')
                if archived!=source:errors.append(f'{nid}: source starter map not exactly archived')
                source_target=archived or current
                treatment='source_starter_exactly_archived'
            else:
                source_target=current
                treatment='source_detailed_records_preserved_active_or_retired_with_primary_referral'
                if source.get('prior_initial_map') is not None:
                    prior_archives+=1
                    if current.get('prior_initial_map')!=source['prior_initial_map']:
                        errors.append(f'{nid}: prior source archive changed')
                if current['research_profiles']!=source['research_profiles']:
                    errors.append(f'{nid}: source research-profile metadata changed')
            actual_topics={t['id']:t for c,t in records(source_target)}
            if kind!='subject_map':
                actual_topics.update({t['id']:t for t in current.get('retired_duplicate_proposals',[])})
            actual_categories={c['id']:c for c in source_target['categories']}
            for category,topic in records(source):
                actual=actual_topics.get(topic['id'])
                if actual is None or any(actual.get(k)!=v for k,v in topic.items()):
                    errors.append(f"{nid}: original record changed or missing {topic['id']}")
                else:preserved_records+=1
                if kind!='subject_map' and topic['id'] in {t['id'] for t in current.get('retired_duplicate_proposals',[])}:
                    retired_source_records+=1
            for category in source['categories']:
                actual=actual_categories.get(category['id'])
                if actual is None or any(actual.get(k)!=v for k,v in category.items() if k!='topics'):
                    errors.append(f"{nid}: source category metadata changed {category['id']}")
            if nid!='001':
                rec=current['local_reconciliation']
                live=read(directory/'topics_status.json')
                if any(live.get(k)!=v for k,v in rec['local_status_original'].items()):
                    errors.append(f'{nid}: pre-existing local status data changed')
                name=next((n for n in rec['local_files'] if n.endswith('_CHANNEL_TOPIC_ROADMAP.md')),None)
                if nid=='281' and name:
                    if not (directory/name).read_bytes().endswith(rec['local_files'][name]['original_text'].encode('utf-8')):
                        errors.append('281: original extensive roadmap body changed')
                report_original=rec['local_files'].get('TOPICS_COVERED_REPORT.md',{}).get('original_text')
                if report_original and not (directory/'TOPICS_COVERED_REPORT.md').read_bytes().startswith(report_original.rstrip().encode('utf-8')):
                    errors.append(f'{nid}: original production report body changed')
            entries.append({'niche_id':nid,'original_record_count':sum(len(c['topics']) for c in source['categories']),
                'treatment':treatment,'current_active_count':len(records(current))})
    result={'archive_path':str(archive_path),'archive_sha256':hashlib.sha256(archive_path.read_bytes()).hexdigest(),
        'niches_checked':len(entries),'original_records_preserved':preserved_records,'original_detailed_records_preserved_inactive':retired_source_records,'prior_source_archives_checked':prior_archives,
        'errors':errors,'checks':'ZIP manifest; exact starter archive; all original topic fields; source category metadata; local status; original report bodies; Ayurveda roadmap body',
        'source_factual_verification':'not_performed','niches':entries}
    if report_path:write(report_path,result)
    print(f'Checked {len(entries)} niches; {preserved_records} original ZIP records preserved; {len(errors)} errors.')
    if errors:print('\n'.join(errors[:50]))
    return not errors


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive',type=Path,default=ARCHIVE)
    parser.add_argument('--report',type=Path,default=TOPICS/'TOPIC_BANK_SOURCE_PRESERVATION.json')
    args=parser.parse_args()
    raise SystemExit(0 if validate(args.archive,args.report) else 1)
