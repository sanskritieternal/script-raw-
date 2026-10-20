# Autonomous production rules — schema 5.0

Autonomous mode drafts phases in the order and folders defined by `CORE/PIPELINE/CONTRACT.md`. Use taxonomy Q1, niche CAT defaults, angle Q3, then explicit overrides. Write answer provenance and schema version to CONFIG.

At each gate verify the required output, not just its presence. Phase 1 must provide a source-backed claim ledger; Phase 2 must lock Q3/Q15/Q16/Q42; Phase 3 timing must sum exactly to Q14; Phase 4 must preserve claim citations; Phase 5 must report unresolved blockers. The agent may continue drafting while a review is pending, but must not mark a blocked phase approved or certify completion.

Human review is required before publication status for Q8 High/Critical, Q41 Strict/Critical, living-person allegations, medical or financial advice, or material contested claims. If a source cannot be checked, mark the claim unverified and keep it out of the final factual script. No unsupported statement becomes verified merely because an earlier phase included it.

Track project progress in its ID-first output folder. Never modify historical projects under `OUTPUT/Legacy/` during new production. Do not skip a phase or silently overwrite an approved output.

Expanded production workflow 1.0 uses 26 documents and PRODUCTION_MANIFEST.json. Follow CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md. Draft scaffolds fail Phase 2. Complete applicability/locks before Phase 3 and actual scene/asset/chapter maps before compilation. Use `python -m Tools.projects.production_workflow compile` to preserve citations and input hashes; stale packages must be rebuilt. Explicit adoption of existing documents is internal only and never substitutes for human publication review.
