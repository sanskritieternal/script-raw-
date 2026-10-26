"""Append authored coverage to existing detailed banks without replacing records.

There is no topic target or completion threshold. Existing records and IDs remain
unchanged. Preview is the default. Input uses the authored depth-batch format.
"""
import argparse
import copy
import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from apply_authored_depth_batch import parse
from build_initial_subject_maps import PROFILES

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    batch = parse(args.input)
    existing_questions = {t['question'].casefold() for p in ROOT.glob('topics/*/IN_DEPTH_TOPIC_BANK.json')
                          for c in json.loads(p.read_text())['categories'] for t in c['topics']}
    pending = []
    new_questions = set()
    for nid, authored in batch.items():
        path = next(ROOT.glob(f'topics/{nid}_*/IN_DEPTH_TOPIC_BANK.json'))
        bank = json.loads(path.read_text())
        if args.input.stem in bank.get('applied_extension_batches', []):
            continue
        assert bank['editorial_depth'] == 'detailed_authored_draft', nid
        old_categories = copy.deepcopy(bank['categories'])
        old_archive = copy.deepcopy(bank.get('prior_initial_map'))
        categories = copy.deepcopy(authored)
        highest = max(int(t['id'].rsplit('-', 1)[1]) for c in bank['categories'] for t in c['topics'])
        existing_category_ids = {c['id'] for c in bank['categories']}
        ordinal = 1
        for category in categories:
            while f'CATALOG-{nid}-E{ordinal:02d}' in existing_category_ids:
                ordinal += 1
            category['id'] = f'CATALOG-{nid}-E{ordinal:02d}'
            existing_category_ids.add(category['id'])
            ordinal += 1
            category['prerequisites'] = [bank['categories'][0]['id']]
            profile = category['research_profile']
            bank['research_profiles'][profile] = {k:v for k,v in PROFILES[profile].items()
                                                   if k in ('requirements','source_leads')}
            for topic in category['topics']:
                q = topic['question'].casefold()
                assert q not in existing_questions and q not in new_questions, topic['question']
                new_questions.add(q)
                highest += 1
                topic.update(id=f'BANK-{nid}-{highest:03d}', angle=None,
                             status='proposed', verified_sources=[])
        bank['categories'].extend(categories)
        assert bank['categories'][:len(old_categories)] == old_categories
        assert bank.get('prior_initial_map') == old_archive
        bank['counts'] = {'categories':len(bank['categories']),
                          'proposed_topics':sum(len(c['topics']) for c in bank['categories'])}
        bank.setdefault('applied_extension_batches', []).append(args.input.stem)
        bank['updated'] = datetime.now(ZoneInfo('Asia/Calcutta')).date().isoformat()
        bank['coverage_review'] = {
            'status':'open_for_further_substantive_expansion', 'topic_cap':None,
            'completion_basis':'Coverage of real subject branches, never a uniform topic count.',
            'exhaustive_coverage_claimed':False, 'source_verification':'not_performed',
            'latest_extension':args.input.stem}
        pending.append((path, bank))
    for path, bank in pending:
        if args.write:
            path.write_text(json.dumps(bank, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'banks':len(pending),'new_proposals':len(new_questions),'write':args.write,
                      'resulting_counts':{b['niche_id']:b['counts'] for _,b in pending}}))


if __name__ == '__main__':
    main()
