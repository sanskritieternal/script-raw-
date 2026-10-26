"""Record measured tokenizer evidence while retaining the research gate."""
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
PATH = ROOT / 'REGISTRY/Niches/001_ai_technology_explainers/IDEA_BANK.json'


def main():
    bank = json.loads(PATH.read_text(encoding='utf-8'))
    idea = next(x for x in bank['ideas'] if x['idea_id'] == 'IDEA-001-0004')
    assert idea['status'] == 'researching'
    idea['evidence_gaps'] = [
        'Choose the exact on-screen examples and check each scripted factual sentence against the pre-production claim worksheet in Phase 1.',
        'If the script discusses pricing or current hosted models, obtain separate dated primary documentation before making those claims.'
    ]
    idea['blocking_gaps'] = [
        'No Phase 1 project claim ledger or scripted-claim review has been completed. The saved measurements verify only fixed strings and a pinned package version.'
    ]
    idea['readiness_note'] = (
        'Pinned official code checked. Token counts, byte spans and round trips were measured with tiktoken 0.14.0; '
        'a controlled pattern/rank comparison and a pre-production claim worksheet are saved under '
        'topics/001_ai_technology_explainers/RESEARCH_NOTES/. Phase 1 scripted-claim review remains open. '
        'Keep researching status; no episode created.'
    )
    for source in idea['source_candidates']:
        if source['title'] == 'tiktoken encoding constructors at pinned commit':
            source['check_note'] = (
                'Opened the pinned constructors and inspected the separate gpt2 and cl100k_base definitions, '
                'regex rules and vocabulary files. Sample outputs were measured separately in the linked research note.'
            )
    formatted = (json.dumps(bank, ensure_ascii=False, indent=2) + '\n').replace('\n', '\r\n')
    PATH.write_bytes(formatted.encode('utf-8'))
    print('Updated IDEA-001-0004 measured evidence and retained researching status.')


if __name__ == '__main__':
    main()
