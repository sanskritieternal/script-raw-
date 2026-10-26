# BANK-001-013 — pre-production claim worksheet

**Scope:** Five fixed input strings, two encodings in `tiktoken==0.14.0`, and two controlled mixed encodings. This worksheet supports case selection. It does not approve a script or replace a Phase 1 project claim ledger.

| ID | Bounded statement available for a future script | Evidence | Limit |
|---|---|---|---|
| C1 | At pinned revision `4e71bbe0c078468e00fefbf94b39849389f346e5`, the library maps GPT-2 to `gpt2` and GPT-4 to `cl100k_base`. | [Pinned model mapping](https://github.com/openai/tiktoken/blob/4e71bbe0c078468e00fefbf94b39849389f346e5/tiktoken/model.py); [release](https://github.com/openai/tiktoken/releases/tag/0.14.0). | Historical library mapping only; no statement about current hosted endpoints. |
| C2 | The two encoding constructors specify different pre-tokenization patterns and merge-rank resources. | [Pinned constructors](https://github.com/openai/tiktoken/blob/4e71bbe0c078468e00fefbf94b39849389f346e5/tiktoken_ext/openai_public.py). | Source inspection, not a claim that every input's count differs. |
| C3 | For the five literal strings, the two official encodings produced the counts in the [research note](BANK-001-013.md#reproduced-sample-counts). | [Measurement JSON](BANK-001-013_MEASUREMENT.json); [measurement script](../../../Scripts/archive/topic_bank/001_184/measure_tokenizer_case_001.py). | Exact bytes and installed package version; round trips checked. |
| C4 | The controlled 2×2 comparison isolates a rank-set count difference for the Japanese and accent inputs, and a pattern/rank interaction for the Hindi input. | [Factorial JSON](BANK-001-013_FACTORIAL.json); [factor script](../../../Scripts/archive/topic_bank/001_184/analyze_tokenizer_factors_001.py). | Mixed encodings are analytical constructs, not real model mappings; no general-language conclusion. |
| C5 | The composed and combining accent samples have distinct recorded code-point sequences and UTF-8 hashes; no normalization was applied. | [Measurement JSON](BANK-001-013_MEASUREMENT.json); [measurement script](../../../Scripts/archive/topic_bank/001_184/measure_tokenizer_case_001.py). | No inference about visual equivalence, semantics or comprehension. |

**Excluded claims:** tokenizer count as a measure of intelligence or language quality; present API billing or pricing; behavior of hosted GPT-2 or GPT-4 services; a universal ranking across languages. Each would require a different source and test design.

**Review gate:** Before a production script, select its exact examples, reproduce those results in the Phase 1 project and attach evidence to each sentence that makes a factual claim. `IDEA-001-0004` stays `researching`.
