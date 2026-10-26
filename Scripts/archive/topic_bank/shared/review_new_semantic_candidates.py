"""Isolate lexical review pairs introduced by the second-pass additions.

Use after `editorial_review_tools.py candidates --tag final` and its
question-only counterpart. This is a triage list, never an automatic verdict.
"""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / 'Scripts/editorial_review_inputs'


def pair_ids(pair):
    return tuple(sorted((pair['left']['id'], pair['right']['id'])))


def main():
    old = set()
    for name in ('semantic_candidates_all.json', 'semantic_question_candidates_all.json'):
        old.update(pair_ids(p) for p in json.loads((SOURCE / name).read_text(encoding='utf-8'))['pairs'])
    fresh = {}
    for name in ('final_semantic_candidates_all.json', 'final_semantic_question_candidates_all.json'):
        for pair in json.loads((SOURCE / name).read_text(encoding='utf-8'))['pairs']:
            ids = pair_ids(pair)
            if ids not in old and (ids not in fresh or pair['score'] > fresh[ids]['score']):
                fresh[ids] = pair
    values = sorted(fresh.values(), key=lambda p: p['score'], reverse=True)
    path = SOURCE / 'final_new_semantic_candidates.json'
    path.write_text(json.dumps({'note': 'Manual comparison of full question and scope required; lexical candidates are not duplicate findings.',
                                'pairs': values}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(values)} new lexical pairs to review in {path.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
