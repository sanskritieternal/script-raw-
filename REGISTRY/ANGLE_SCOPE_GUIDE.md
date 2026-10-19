# Using an angle's scope

An angle chooses which part of a niche to explore. Its scope defines the research work and its limits. Every angle in the active niche registry has a question, coverage instruction, evidence direction and boundary.

| Field in `ANGLE_PLAN.json` | Purpose |
|---|---|
| `slug` | Stable identifier used by angle files and episode paths |
| `angle` | Human-readable angle label; supplies Q3 |
| `question` | Example question that gives the angle its focus |
| `scope` | What to examine, trace, compare or evaluate |
| `evidence` | Types of records or studies to seek |
| `boundary` | Limits on interpretation, application or coverage |

For example, Media Literacy's Teaching Transfer angle asks whether a taught checking method is used on unfamiliar claims after a delay. Its scope requires comparing demonstrated performance with confidence or recall. An actual episode then selects a particular classroom program, learners and assessment period.

## Where to edit

Edit the selected entry inside `REGISTRY/Niches/<ID>_<Slug>/ANGLE_PLAN.json`. Give each angle a distinct coverage instruction. A brief instruction can work when its question and boundary provide the necessary context. Use concrete objects and comparisons, such as a named study's population and outcomes or a product's repair and replacement costs.

The `Angles/*.md` files are generated views of that plan. They display **Focus / example question**, **Coverage**, **Evidence to seek** and **Limits**. After editing a plan, regenerate and verify its files:

```powershell
python populate_niches.py --id 530 --sync-content
python populate_niches.py --id 530 --verify-content
python review_angle_plans.py --scope-audit
```

The scope audit checks all plans for complete fields, repeated scopes within a niche and the broad templates used in the original expansion draft. These checks support editorial review; they do not verify sources or factual claims.

## Where to use it

1. Before creating an episode, use the angle's scope to choose a concrete case, source or work and its relevant place, population, version or period. Express the actual investigation in `--story-question`.
2. Newly created Phase 0 `CONFIG.md` files include a **Selected angle scope** snapshot. Scope is planning guidance alongside Q1-Q42, and its angle label supplies Q3.
3. In Phase 1, state the episode's coverage and exclusions in `Research_Summary.md`, select evidence that addresses the question and record material claims in `Claim_Ledger.md`.
4. During scripting and final audit, check whether each section serves the selected question and whether conclusions stay within the evidence and scope.

Registry edits regenerate angle files. They do not rewrite an existing episode's configuration or research. If an episode changes its scope, review its existing research and downstream work against the new question.

The [scope review report](../AUDIT/ANGLE_SCOPE_REVIEW.md) and [per-niche ledger](../AUDIT/ANGLE_SCOPE_REVIEW.csv) record the current scope checks.
