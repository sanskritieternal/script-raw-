# Angle scope review

Checked **550 niche plans** and **17,069 angle scopes** against the active taxonomy. Plans needing structural attention: **0**.

The [per-niche ledger](ANGLE_SCOPE_REVIEW.csv) checks every angle's question, coverage, evidence direction and limit. It also checks for repeated scopes within a plan and the broad templates used by the original expansion draft. A short coverage instruction is assessed together with its angle question and limit; length alone is not treated as a defect.

**1,053 scopes in IDs 501–530 were rewritten** with angle-specific research tasks and comparisons. The [change ledger](ANGLE_SCOPE_CHANGES.csv) retains the previous and revised wording. The [focus-question ledger](ANGLE_FOCUS_CHANGES.csv) also records 150 field-angle questions aligned with the new scopes. The other 16,016 existing scopes retain their curated coverage instructions and are now displayed with their focus, evidence and limits. The 80 AI and Sanatan pilot angles also received explicit evidence and limit fields.

## Use in production

Edit scope wording in the niche's `ANGLE_PLAN.json`, then regenerate its angle files. Each angle file displays Focus / example question, Coverage, Evidence to seek and Limits. New Phase 0 configurations snapshot that section so Phase 1 can use it after the registry changes. Choose the concrete case, source or work and relevant place, population, version or period in the episode story question and research summary.

Scope checks do not change a plan's editorial status or verify sources and claims. Current inventory: 548 plans with reviewed question designs, 0 editorial drafts and 2 pilots. See the [expansion editorial review](EXPANSION_EDITORIAL_REVIEW.md) for the later source and overlap checks on IDs 501–530. Existing episode configurations are preserved; their original angle references remain available.

## Refresh

```powershell
python review_angle_plans.py --scope-audit
python populate_niches.py --id <ID> --sync-content
python populate_niches.py --id <ID> --verify-content
```
