"""Validate a depth checkpoint against its unchanged canonical input archive.

This checks preservation and structure, not factual verification or exhaustive
subject coverage. Run after applying the authored batch, rendering and indexing.
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
    authored = parse(args.batch)
    changed = set(authored)
    questions, identities, scopes = set(), set(), set()
    new_topics = new_categories = preserved = links = 0
    with zipfile.ZipFile(args.previous_archive) as archive:
        old_status = json.loads(archive.read('files/topics/DEPTH_COMPLETION_STATUS.json'))
        assert changed <= set(old_status['pending_niche_ids']), 'Do not overwrite a detailed draft'
        names = [n for n in archive.namelist()
                 if n.startswith('files/') and n.endswith('/IN_DEPTH_TOPIC_BANK.json')]
        seen = set()
        for name in names:
            relative = Path(name[6:])
            old = json.loads(archive.read(name))
            path = ROOT / relative
            bank = json.loads(path.read_text())
            nid = bank['niche_id']
            seen.add(nid)
            if nid not in changed:
                assert path.read_bytes() == archive.read(name), f'Untargeted bank changed: {nid}'
                preserved += 1
            else:
                assert bank['prior_initial_map'] == old, f'Initial-map archive differs: {nid}'
                assert bank['editorial_depth'] == 'detailed_authored_draft'
                assert args.batch.stem in bank['applied_depth_batches']
                old_ids = {t['id'] for c in old['categories'] for t in c['topics']}
                actual = [(c['title'], c['level'], c['research_profile'],
                           [(t['question'], t['coverage']) for t in c['topics']])
                          for c in bank['categories']]
                expected = [(c['title'], c['level'], c['research_profile'],
                             [(t['question'], t['coverage']) for t in c['topics']])
                            for c in authored[nid]]
                assert actual == expected, f'Authored input differs from bank: {nid}'
                new_categories += len(bank['categories'])
                for category in bank['categories']:
                    for topic in category['topics']:
                        assert topic['id'] not in old_ids
                        assert topic['angle'] is None
                        assert topic['status'] == 'proposed' and topic['verified_sources'] == []
                        scope = topic['coverage'].casefold()
                        assert scope not in scopes, 'Repeated new coverage boundary'
                        scopes.add(scope)
                        new_topics += 1
            for category in bank['categories']:
                for topic in category['topics']:
                    question = topic['question'].casefold()
                    assert topic['id'] not in identities, 'Repeated active ID'
                    assert question not in questions, 'Repeated active question'
                    identities.add(topic['id'])
                    questions.add(question)
        assert changed <= seen
        assert seen == {json.loads(p.read_text())['niche_id']
                        for p in ROOT.glob('topics/*/IN_DEPTH_TOPIC_BANK.json')}
        for name in archive.namelist():
            if name.startswith('files/Scripts/detailed_expansion_batch_'):
                assert (ROOT / name[6:]).read_bytes() == archive.read(name), name
        status = json.loads((ROOT / 'topics/DEPTH_COMPLETION_STATUS.json').read_text())
        progress = json.loads((ROOT / 'topics/TOPIC_BANK_PROGRESS.json').read_text())
        prepared = set(old_status['prepared_niche_ids']) | changed
        pending = set(old_status['pending_niche_ids']) - changed
        assert set(status['prepared_niche_ids']) == prepared
        assert set(status['pending_niche_ids']) == pending
        assert status['detailed_topic_drafts_prepared'] == len(prepared)
        assert status['pending_depth_expansion'] == len(pending)
        assert status['next_pending_niche_id'] == (min(pending) if pending else None)
        assert prepared.isdisjoint(pending) and prepared | pending == seen
        assert status['all_niches_completed_in_depth'] == (not pending)
        assert progress['totals']['proposed_topics'] == len(identities)
    paths = [next(ROOT.glob(f'topics/{nid}_*/IN_DEPTH_TOPIC_BANK.md')) for nid in sorted(changed)]
    paths += [ROOT / 'topics/ALL_NICHE_TOPIC_BANKS.md', ROOT / 'topics/DEPTH_COMPLETION_STATUS.md']
    for path in paths:
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' not in target and not target.startswith('#'):
                assert (path.parent / target.split('#')[0]).exists(), (path, target)
                links += 1
    report = {
        'batch': args.batch.stem, 'niche_ids': sorted(changed),
        'authored_proposals': new_topics, 'authored_categories': new_categories,
        'previous_canonical_sha256': hashlib.sha256(args.previous_archive.read_bytes()).hexdigest(),
        'checks': {
            'untargeted_bank_json_files_byte_for_byte_preserved': preserved,
            'initial_maps_preserved_exactly': len(changed), 'prior_authored_inputs': 'unchanged',
            'authored_input_matches_changed_banks': True,
            'active_ids_and_questions': 'globally unique', 'new_scopes': 'distinct within batch',
            'new_angle_assignments': 'none', 'new_sources_verified': 0,
            'local_markdown_link_targets_checked': links,
            'prepared_detailed_drafts': len(prepared), 'pending_depth_expansion': len(pending),
            'next_pending_niche': status['next_pending_niche_id']},
        'limits': ['Topic planning only; source verification and production are separate.',
                   'Structural checks do not certify truth, exhaustive coverage or all semantic overlap.',
                   'Full repository tests not claimed; GitHub unchanged.']}
    args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
