# Topic-bank structure and maintenance

Start with [the all-niche index](ALL_NICHE_TOPIC_BANKS.md). Every niche has one main reading file, `IN_DEPTH_TOPIC_BANK.md`, and one editable catalog, `IN_DEPTH_TOPIC_BANK.json`.

The reading hierarchy is **category → subcategory → specific video question → individual coverage scope**. Learning paths link foundation, intermediate and advanced sections. IDs preserve identity; their numerical order is not a curriculum.

## Connection to existing project documents

The repository README links to the all-niche index. The existing `topics/README.md` links each niche to its main bank and original execution report. Each niche roadmap directs readers to its bank; the extensively edited Ayurveda roadmap retains its original body as well.

Existing `topics_status.json` values remain intact. The added `topic_bank_integration` namespace records catalog counts and links independently of production queues and completion records. Niche 001 retains its already established `catalog_summary` structure.

Banks link to the existing registry planning guide and niche identity. They do not change CAT Q1–Q42, angle definitions, IDEA readiness, DEPTH plans, CONFIG snapshots, research ledgers or production files. Select a bounded question and use the existing [idea workflow](../REGISTRY/IDEA_BANK_GUIDE.md) and [depth-planning workflow](../REGISTRY/DEPTH_PLANNING_GUIDE.md) deliberately before creating an episode.

## Preservation and counts

- Imported detailed BANK records keep their original IDs, questions, scopes and other fields.
- When editorial review establishes that two records propose the same episode, retain the full redundant record in `retired_duplicate_proposals` with its original ID and a `duplicate_of` link. This may include an imported original: preservation means keeping every original field, not counting two copies as active topics. Source subcategory metadata remains intact. The main file keeps the old anchor and directs it to the primary question.
- Superseded starter maps remain under `prior_initial_map`. Their substantive subject headings appear in the main reading file as a coverage checklist; their templated briefs are not counted as extra active proposals.
- Generic local angle frameworks, where found, remain in `archived_local_frameworks`. Their allocated IDs are reserved and never reused.
- Original local roadmap, report and status contents are retained in `local_reconciliation` snapshots. Legacy references are shown separately rather than added again to the active BANK count.
- Specific existing local roadmap proposals may be reconciled into active BANK entries with `origin: repository_roadmap`; their original questions and scopes remain attributed. Their framing is not a verified finding.
- `starter_concept_crosswalk` links a reviewed starter subject to its actual refined BANK coverage. A missing mapping is an open editorial check, not proof that a subject is absent.

Counts describe proposals only. There is no fixed target, cap or claim of exhaustive coverage. No new bank entry is a verified source, completed script, ready idea or published episode.

## Editing and checks

Edit a niche's JSON, preserving existing identities. Add a new ID only for a distinct question or scope. Keep source-verification fields honest. Compare neighboring niche questions before proposing another primary home for the same episode.

For niches 002–550, run from the repository root:

```powershell
python Scripts/manage_all_topic_banks.py render --start 111 --end 111
python Scripts/manage_all_topic_banks.py index
python Scripts/manage_all_topic_banks.py check --report topics/TOPIC_BANK_VALIDATION.json
python Scripts/validate_topic_bank_sources.py
```

Replace the range with the niche IDs actually edited. For niche 001, use `python Scripts/manage_ai_topics.py render` and `python Scripts/manage_ai_topics.py validate`.

The renderer preserves original status values, adds catalog metadata and regenerates the reading views. It checks saved view hashes and stops on unexpected manual view changes rather than silently discarding them. Reconcile intentional manual changes into the JSON before rebuilding. Existing execution-status generators remain separate from catalog editing; their output is not a source of new BANK identities.

Authored expansion inputs under `Scripts/expansion_*.json` support repeatable append operations through `manage_all_topic_banks.py apply --input <path>`. Reapplying an identical question/scope does not create another ID. These inputs do not run automatically during episode production.

Structural validation checks identities, exact normalized duplicates, preservation, counts, prerequisites, view content and local links. It does not verify factual premises, replace semantic review, certify sources or establish that every meaningful subject branch has been covered.

The independent source check reads the unchanged supplied ZIP and its SHA256 manifest. It compares every original BANK record directly with its active or archived counterpart, checks archived starter maps exactly, and verifies preservation of local status values and original production-report bodies.

## Editorial review records

Read [the scope-based editorial review](TOPIC_BANK_EDITORIAL_REVIEW.md) for the second pass. Its linked per-bank audits record starter scope evidence, gap dispositions and overlap decisions. `editorial_cross_references` displays a specific boundary between related proposals without rewriting an imported source record. `legacy_topic_crosswalk` can narrow an old playlist or queue title to actual scopes without counting a format or case variant twice.

Follow later case selection, source checks and idea-workflow work in [the follow-up progress record](TOPIC_BANK_FOLLOW_UP_PROGRESS.md). A topic-level research note is linked from its main bank entry; the BANK proposal and the registered IDEA keep separate identities and readiness states.

Keep the original question and scope when retiring a duplicate. Point `duplicate_of` to an active primary record, preserve the old anchor, and redirect starter/legacy referrals to that primary. Do not manufacture a new distinction in wording merely to retain an active count.

`python Scripts/validate_editorial_review.py` checks recorded review coverage against the saved before-pass baseline and confirms that its questions and scopes remain active or fully archived. This is evidence of a recorded review, not a guarantee that no meaningful future subject or semantic overlap remains.
