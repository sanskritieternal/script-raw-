# Source list and access evidence

Research checked: 2026-10-18. Researcher: Codex. Primary sources only. Publisher and version identification are not proof of experimental replication.

## S1 — Architecture and source history

Vaswani et al., *Attention Is All You Need*. Original submission 2017; inspected arXiv v7, 2023.

- [Full HTML](https://arxiv.org/html/1706.03762v7)
- [Version history](https://arxiv.org/abs/1706.03762)
- Inspected: sections 3.1–3.5 and source metadata. Locators for retained claims are in the ledger.
- Evidence role: primary specification for the selected historical architecture. No current-product inference.
- Conflict: section 6.1 running text and abstract/table are inconsistent on one benchmark; all benchmark values excluded.
- Rights: cite the work. No figure reproduction is assumed; original artwork is planned. The manuscript's figure/table permission notice is not treated as a blanket license for unrelated assets.

## S2 — Experiment report on interpretation

Sarthak Jain and Byron C. Wallace, *Attention is not Explanation*. NAACL-HLT 2019, pages 3543–3556. DOI: 10.18653/v1/N19-1357.

- [Publisher record and abstract](https://aclanthology.org/N19-1357/)
- [Paper PDF](https://aclanthology.org/N19-1357.pdf)
- Inspected: abstract, sections 1–2, scope in section 3, and relevant experiment passages in section 4.
- Evidence role: an attributed report, not independent reproduction. Restrict wording to the studied tasks/models; do not transfer a result indiscriminately to Transformer heads or all AI systems.
- No numerical experiment result is imported into this episode.

## S3 — Methodological response

Sarah Wiegreffe and Yuval Pinter, *Attention is not not Explanation*. EMNLP-IJCNLP 2019, pages 11–20. DOI: 10.18653/v1/D19-1002.

- [Publisher record and abstract](https://aclanthology.org/D19-1002/)
- [PDF lead](https://aclanthology.org/D19-1002.pdf)
- Inspected: publisher abstract and bibliographic metadata. The PDF request returned a document listing once, but subsequent retrieval timed out; full methods were not reviewed.
- Evidence role: only the abstract's explicit attributed methodological position is retained. Detailed findings, test implementation and numerical results are excluded.
- If later production needs those details, access and inspect the actual paper before adding claims.

## T1 — Original synthetic arithmetic

[Research_Calculations.json](Research_Calculations.json) and the derivation in [Facts_Documented.md](Facts_Documented.md).

Inputs were authored for this episode and evaluated with Python standard-library math. Exact symbolic expectations supplied a separate comparison for the computed values. This verifies arithmetic, not language understanding or model behavior.

## Reliability, conflicts and refresh rules

S2 and S3 concern an interpretive dispute and are retained together. Their reported positions are not a new adjudication by this episode. No secondary explainer, generated summary or search snippet is used as claim evidence.

Recheck source accessibility/version before Phase 4. Reopen Phase 1 if claims, architecture scope, benchmark content or interpretability scope changes. Preserve historical citations rather than silently substituting a newer paper.

The publisher records identify ACL material from these years as CC BY 4.0, but no asset reuse or adaptation approval is supplied here. Record actual reused material, attribution and conditions in the future asset register. Original artwork remains the preferred plan.
