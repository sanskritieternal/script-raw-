"""Controlled 2x2 tokenizer analysis for BANK-001-013.

The two hybrids are analytical constructs, not released model tokenizers.
Run with: uv run --no-project --python 3.11 --with tiktoken==0.14.0 python Scripts/archive/topic_bank/001_184/analyze_tokenizer_factors_001.py
"""
from importlib.metadata import version
import json
from pathlib import Path

import regex
import tiktoken
from tiktoken_ext import openai_public


ROOT = Path(__file__).resolve().parents[4]
NOTES = ROOT / 'topics/001_ai_technology_explainers/RESEARCH_NOTES'


def main():
    assert version('tiktoken') == '0.14.0'
    measured = json.loads((NOTES / 'BANK-001-013_MEASUREMENT.json').read_text(encoding='utf-8'))
    original = {'gpt2': openai_public.gpt2(), 'cl100k_base': openai_public.cl100k_base()}
    combinations = {}
    for pattern_name, pattern in original.items():
        for ranks_name, ranks in original.items():
            key = f'{pattern_name}_pattern__{ranks_name}_ranks'
            combinations[key] = tiktoken.Encoding(
                name=f'analysis_{key}',
                pat_str=pattern['pat_str'],
                mergeable_ranks=ranks['mergeable_ranks'],
                special_tokens={},
            )
    rows = []
    for sample in measured['samples']:
        text = sample['text']
        pretoken_chunks = {
            name: regex.findall(spec['pat_str'], text) for name, spec in original.items()
        }
        counts = {}
        for key, encoding in combinations.items():
            ids = encoding.encode(text, disallowed_special=())
            assert encoding.decode(ids) == text
            counts[key] = len(ids)
        assert counts['gpt2_pattern__gpt2_ranks'] == sample['encodings']['gpt2']['token_count']
        assert counts['cl100k_base_pattern__cl100k_base_ranks'] == sample['encodings']['cl100k_base']['token_count']
        rows.append({'sample': sample['sample'], 'utf8_sha256': sample['utf8_sha256'],
                     'pretoken_chunks': pretoken_chunks, 'token_counts': counts})
    report = {
        'bank_topic_id': 'BANK-001-013',
        'measurement_input': 'BANK-001-013_MEASUREMENT.json',
        'package_version': version('tiktoken'),
        'design': 'Cross the two official pre-tokenization regex patterns with the two official merge-rank sets. Each hybrid is an analytical encoding, not a model encoding.',
        'interpretation_limit': 'Count differences are conditional on the fixed input. Pattern and rank effects may interact; this is not a model-quality or language-quality comparison.',
        'rows': rows,
    }
    path = NOTES / 'BANK-001-013_FACTORIAL.json'
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for row in rows:
        print(row['sample'], row['token_counts'])


if __name__ == '__main__':
    main()
