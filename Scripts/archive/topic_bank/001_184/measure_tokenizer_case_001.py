"""Reproduce BANK-001-013's selected comparison with tiktoken 0.14.0.

Run from the repository root:
uv run --no-project --python 3.11 --with tiktoken==0.14.0 python Scripts/archive/topic_bank/001_184/measure_tokenizer_case_001.py
"""
import hashlib
from importlib.metadata import version
import json
from pathlib import Path
import platform
import unicodedata

import tiktoken


ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / 'topics/001_ai_technology_explainers/RESEARCH_NOTES/BANK-001-013_MEASUREMENT.json'
SAMPLES = [
    ('English', 'Hello, world!'),
    ('Hindi', 'नमस्ते दुनिया'),
    ('Japanese', '東京へ行く'),
    ('Composed accent', 'café'),
    ('Combining accent', 'cafe\u0301'),
]


def measure(name, text, encodings):
    row = {
        'sample': name,
        'text': text,
        'unicode_codepoints': [f'U+{ord(ch):04X}' for ch in text],
        'utf8_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest(),
        'is_nfc': unicodedata.normalize('NFC', text) == text,
        'encodings': {},
    }
    for encoding_name, encoding in encodings.items():
        ids = encoding.encode(text, disallowed_special=())
        pieces = [encoding.decode_single_token_bytes(tid) for tid in ids]
        assert b''.join(pieces) == text.encode('utf-8')
        assert encoding.decode(ids) == text
        row['encodings'][encoding_name] = {
            'token_count': len(ids),
            'token_ids': ids,
            'token_bytes_hex': [piece.hex() for piece in pieces],
            'round_trip_verified': True,
        }
    return row


def main():
    actual_version = version('tiktoken')
    assert actual_version == '0.14.0', actual_version
    assert tiktoken.encoding_name_for_model('gpt-2') == 'gpt2'
    assert tiktoken.encoding_name_for_model('gpt-4') == 'cl100k_base'
    encodings = {name: tiktoken.get_encoding(name) for name in ('gpt2', 'cl100k_base')}
    output = {
        'bank_topic_id': 'BANK-001-013',
        'idea_id': 'IDEA-001-0004',
        'measurement_date_local': '2026-10-24',
        'source_revision': 'https://github.com/openai/tiktoken/tree/4e71bbe0c078468e00fefbf94b39849389f346e5',
        'package_version': actual_version,
        'python_version': platform.python_version(),
        'platform': platform.platform(),
        'input_policy': 'Literal code points; no normalization or case conversion before either encoding.',
        'model_mapping_checked': {'gpt-2': 'gpt2', 'gpt-4': 'cl100k_base'},
        'samples': [measure(name, text, encodings) for name, text in SAMPLES],
        'limit': 'Measured encoder outputs for these strings only; no model capability, price, hosted-API or language-quality conclusion.',
    }
    OUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for row in output['samples']:
        print(row['sample'], row['encodings']['gpt2']['token_count'], row['encodings']['cl100k_base']['token_count'])


if __name__ == '__main__':
    main()
