# Case-source note: JSONSchemaBench feature-coverage test

Checked 2026-10-24. The original [2025 JSONSchemaBench paper](https://arxiv.org/abs/2501.10868) describes an evaluation of constrained structured-output generation on efficiency, coverage of JSON Schema constraints and output quality, using roughly 10,000 schemas and six then-tested frameworks. The [authors' repository](https://github.com/guidance-ai/jsonschemabench) lists 9,558 current catalogue entries and documents a known subset of unsatisfiable schemas; its README separates schema-feature support and runtime measures. The publication and repository landing page were accessible.

Limits: Paper-version results and current repository counts may differ; no fresh benchmark run, per-framework ranking, code audit or schema-level replication was performed. A JSON object conforming to a supported schema does not by itself satisfy a downstream business rule, ground its content in evidence, or prove an LLM application safe. Tests cover selected schemas, engines and model configurations rather than every product version. Do not turn this into a current vendor recommendation.

Overlap: `BANK-532-040` covers business-rule validity after schema validation; `BANK-531-044` covers AgentDojo security testing; retired 532 foundation IDs remain retired. This is the named constrained-decoding feature-coverage benchmark.
