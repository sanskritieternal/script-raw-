"""Show final lexical candidates with both full scopes for editorial review."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('start', type=int)
    parser.add_argument('end', type=int)
    args = parser.parse_args()
    path = Path(__file__).resolve().parents[3] / 'editorial_review_inputs/final_new_semantic_candidates.json'
    pairs = json.loads(path.read_text(encoding='utf-8'))['pairs']
    for i, pair in enumerate(pairs[args.start:args.end], args.start):
        print(f'\n{i} {pair["score"]}')
        for side in ('left', 'right'):
            item = pair[side]
            print(f'{item["id"]}: {item["question"]} | {item["coverage"]}')


if __name__ == '__main__':
    main()
