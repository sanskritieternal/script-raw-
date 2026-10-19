# V6 flow steps — schema 5.0

Use `CORE/PIPELINE/CONTRACT.md` for the authoritative file tree, counts and gates. Use `REGISTRY/CONFIG_SCHEMA.json` for Q1–Q42.

| Step | Read | Produce | Check before advancing |
|---|---|---|---|
| Select niche | `NICHE_TAXONOMY.csv`, niche index, visual style row | Stable ID, subject, angle | Category and topic path resolve |
| Phase 0 | Subject CAT preset, niche preset, topic preset, explicit answers | `01_Phase0_Configuration/CONFIG.md` | All 42 values and provenance; exact Q14; parseable Q42; risk gate |
| Phase 1 | CONFIG and credible primary/secondary sources | Research Bible and `Claim_Ledger.md` | Material claims sourced and disputes qualified; approval in interactive/domain preset mode |
| Phase 2 | CONFIG, claim ledger, Phase 1 outputs, 16 numbered templates | Production Bible | Q3/Q15/Q16/Q42 locked; approval in interactive/domain preset mode |
| Phase 3 | Phase 1 evidence and Phase 2 locks | 25-scene batches plus language scripts as needed | Sequential IDs, claim citations, duration sum equals Q14; first batch approved in interactive mode |
| Phase 4 | All scenes, research and locks | `Production_Package.md` | Complete script, production instructions and source references; approval in interactive/domain preset mode |
| Phase 5 | All project outputs | `Audit_Report.md`, then certificate only if passing | No blockers, placeholders, citation gaps, timing mismatch or unresolved review flags |

The default 600-second runtime and fixed eight-second scenes produce 75 scenes in three batches. For other fixed lengths use `ceil(Q14 seconds / Q42 seconds)` and shorten the last scene if needed. Variable timing requires a scene-by-scene sum. Changing Phase 2 locks invalidates downstream phases. Autonomous drafting never waives human review for high-risk content.
