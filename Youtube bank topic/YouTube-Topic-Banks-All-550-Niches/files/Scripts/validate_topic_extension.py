"""Check an append-only authored extension against an unchanged input archive.

Checks preservation, authored correspondence and structure, not factual truth or
exhaustive coverage. Run after rendering and indexing.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path
from apply_authored_depth_batch import parse

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous-archive', type=Path, required=True)
    parser.add_argument('--batch', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    batch = parse(args.batch)
    ids, questions, new_scopes = set(), set(), set()
    new_count = new_categories = unchanged = old_topics = links = 0
    with zipfile.ZipFile(args.previous_archive) as z:
        old_status = json.loads(z.read('files/topics/DEPTH_COMPLETION_STATUS.json'))
        assert set(batch) <= set(old_status['prepared_niche_ids'])
        for name in z.namelist():
            if not name.startswith('files/') or not name.endswith('/IN_DEPTH_TOPIC_BANK.json'):
                continue
            old = json.loads(z.read(name))
            path = ROOT / name[6:]
            bank = json.loads(path.read_text())
            nid = bank['niche_id']
            old_topics += old['counts']['proposed_topics']
            if nid not in batch:
                assert path.read_bytes() == z.read(name), ('untargeted bank changed', nid)
                unchanged += 1
            else:
                prefix = len(old['categories'])
                assert bank['categories'][:prefix] == old['categories'], ('prior records changed', nid)
                assert bank.get('prior_initial_map') == old.get('prior_initial_map')
                assert bank.get('applied_depth_batches') == old.get('applied_depth_batches')
                assert bank.get('suggested_series') == old.get('suggested_series')
                assert bank['applied_extension_batches'] == old.get('applied_extension_batches', []) + [args.batch.stem]
                added = bank['categories'][prefix:]
                def content(categories):
                    return [(c['title'], c['level'], c['research_profile'],
                             [(t['question'], t['coverage']) for t in c['topics']]) for c in categories]
                assert content(added) == content(batch[nid])
                allowed = {'categories', 'counts', 'applied_extension_batches', 'updated', 'coverage_review', 'research_profiles'}
                assert {k:v for k,v in bank.items() if k not in allowed} == {k:v for k,v in old.items() if k not in allowed}
                for key, value in old['research_profiles'].items():
                    assert bank['research_profiles'][key] == value
                highest = max(int(t['id'].rsplit('-', 1)[1]) for c in old['categories'] for t in c['topics'])
                new_categories += len(added)
                for c in added:
                    for t in c['topics']:
                        highest += 1
                        assert t['id'] == f'BANK-{nid}-{highest:03d}'
                        assert t['angle'] is None and t['status'] == 'proposed' and t['verified_sources'] == []
                        assert t['coverage'].casefold() not in new_scopes
                        new_scopes.add(t['coverage'].casefold())
                        new_count += 1
            for c in bank['categories']:
                for t in c['topics']:
                    assert t['id'] not in ids and t['question'].casefold() not in questions
                    ids.add(t['id'])
                    questions.add(t['question'].casefold())
        for name in z.namelist():
            if name.startswith('files/Scripts/') and name.endswith('.txt'):
                assert (ROOT / name[6:]).read_bytes() == z.read(name), ('prior authored input changed', name)
        status = json.loads((ROOT/'topics/DEPTH_COMPLETION_STATUS.json').read_text())
        for key in ('prepared_niche_ids', 'pending_niche_ids', 'detailed_topic_drafts_prepared', 'pending_depth_expansion', 'next_pending_niche_id'):
            assert status[key] == old_status[key], ('extension changed preparation stage', key)
        progress = json.loads((ROOT/'topics/TOPIC_BANK_PROGRESS.json').read_text())
        assert len(ids) == progress['totals']['proposed_topics'] == old_topics + new_count
        focus = json.loads((ROOT/'topics/FIRST_TEN_EXPANSION_STATUS.json').read_text())
        assert focus['current_proposals'] == sum(focus['counts'][nid]['current_proposals'] for nid in focus['niche_priority'])
        assert focus['status'] == 'open_for_substantive_expansion_not_complete'
        assert focus['topic_cap'] is None and focus['fixed_topic_target'] is None
    paths = [next(ROOT.glob(f'topics/{nid}_*/IN_DEPTH_TOPIC_BANK.md')) for nid in batch]
    paths += [ROOT/'topics/ALL_NICHE_TOPIC_BANKS.md', ROOT/'topics/DEPTH_COMPLETION_STATUS.md']
    for path in paths:
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' not in target and not target.startswith('#'):
                assert (path.parent/target.split('#')[0]).exists(), (path, target)
                links += 1
    report = {'batch':args.batch.stem, 'niche_ids':sorted(batch), 'new_proposals':new_count,
              'new_categories':new_categories, 'preserved_prior_active_topics':old_topics,
              'untargeted_bank_json_files_byte_for_byte_preserved':unchanged,
              'prior_target_records_and_initial_archives':'exactly preserved',
              'prior_authored_inputs':'unchanged', 'new_input_matches_appended_records':True,
              'active_ids_and_questions':'globally unique', 'new_scopes':'distinct within extension',
              'new_angle_assignments':0, 'new_verified_sources':0, 'local_links_checked':links,
              'previous_archive_sha256':hashlib.sha256(args.previous_archive.read_bytes()).hexdigest(),
              'prepared_detailed_drafts':status['detailed_topic_drafts_prepared'],
              'pending_initial_map_expansion':status['pending_depth_expansion'],
              'current_priority':'Continue substantive expansion of 001-010; count is not completion.',
              'limits':['Planning only; no factual verification or production completed.',
                        'Structural checks do not establish exhaustive or semantically disjoint coverage.',
                        'Full repository tests not claimed; remote repository unchanged.']}
    args.report.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
