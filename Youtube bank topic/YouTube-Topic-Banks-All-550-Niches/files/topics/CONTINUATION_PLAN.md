# Automatic continuation of the in-depth topic work

The user has authorized continuing through all 550 niches without requesting approval for each batch. An hourly continuation is enabled. Use the current machine-readable status rather than any count in a past chat response.

The canonical deliverable is the latest version of the existing `YouTube-Topic-Banks-All-550-Niches.zip` item. Preserve its Library identity and use version guards on replacement. Do not rely on a scratch directory surviving. Do not request access tokens in chat or block content authoring on GitHub writes.

## Start each run

1. Read the Library skill. Locate and materialize the latest canonical archive. Preserve that input archive unchanged for patch generation.
2. Extract to a fresh workspace, rejecting absolute paths and parent traversal. The `files/` tree contains edited topic work; `reference/` contains unchanged source context and the original patch baseline.
3. Run `python3 files/Scripts/restore_reference_context.py --reference-root reference --write`. Matching existing references are preserved; differing references require reconciliation.
4. Read `files/topics/DEPTH_COMPLETION_STATUS.json`. Select pending IDs in order. Preserve already detailed banks and any work saved by other runs.

## Complete meaningful work

### User correction: depth is not a quota

The user explicitly rejected treating 40 topics as sufficient and said there is no boundary: a niche may need 100, 200, 500, 1,000 or more useful topics. These numbers are examples, not targets. The current priority is deeper expansion of niches 001–010 before progressing through the other niches. `authored_draft_prepared` means a draft exists; it does not establish exhaustive or adequate final coverage. Preserve the original draft and append new questions with new IDs using `Scripts/extend_detailed_topic_banks.py`; do not use the initial-map replacement script on an already detailed bank. Read `FIRST_TEN_EXPANSION_STATUS.json` for open branches. Close a branch only after inspecting its actual question coverage, not because a count has been reached. Keep distinct case studies, methods, regional traditions and advanced questions when they supply genuinely different coverage. Never mechanically multiply a subject by generic angles.

Author topic-specific questions and individual coverage boundaries in a new `Scripts/detailed_expansion_batch_<number>.txt` input. The existing batches show the format. Allocate the next batch number from current files, not a hardcoded chat instruction.

Cover the subject's important branches, concrete cases, source or evidence issues, practical interpretation and advanced questions as appropriate. No uniform quota or topic cap applies. Do not mechanically cross every seed with generic narrative angles, pad counts with outline bullets, or rename a starter map as completed depth. A large niche may need more content than a narrow one.

Run the batch applier in preview, inspect the intended targets, then use `--write` once the authored work is substantive. Existing initial proposals are retained under `prior_initial_map`; new questions get new IDs. Reapplying the same batch does not overwrite later editorial changes. New angle assignments remain null unless the actual niche angle scope has been inspected.

Only use genuine sources if performing factual verification. A topic proposal is not a verified answer; medical, financial, legal, technical and contested historical or religious claims require appropriate current/primary evidence before scripting. No research, publication approval or video production status should be manufactured to mark a bank ready.

## Validate and save

From `files/`, run:

```bash
python3 Scripts/render_topic_banks.py --write --require-all-niches
python3 Scripts/render_topic_banks.py --check --require-all-niches
python3 Scripts/index_topic_banks.py
```

Check actual changed questions and scopes, duplicate IDs and questions, preserved prior banks, link targets, archived starter records and honest prepared-versus-pending counts. Structural checks do not replace editorial judgment.

The bundled `Scripts/validate_depth_checkpoint.py` can check the new batch against the unchanged input archive after rendering and indexing. Pass `--previous-archive <input zip> --batch <new authored batch file> --report topics/DEPTH_BATCH_<number>_VALIDATION.json`. It compares every untargeted bank byte for byte, verifies exact archival preservation and correspondence to the authored input, checks globally unique active IDs/questions and local generated-view links, and derives expected progress from the previous tracker. It does not certify facts, semantic uniqueness or exhaustive coverage. Preserve its report in the next package.

Build a separate updated archive with `Scripts/bundle_topic_work.py --previous-archive <unchanged input zip> --reference-root <extracted reference directory> --output <new output zip>`. It verifies both incremental and original-main patches and includes all continuation context. Do not include credentials or unrelated private files.

Replace the same canonical Library item using the current observed version. If a conflict occurs, read the latest version and rebase; do not remove the version guard or discard another run's work.

## Continue or finish

If pending IDs remain, keep the hourly continuation enabled and save quietly. The user does not need a next-batch approval request. Send a notification only for genuine completion or a real blocker that prevents further progress or saving.

When the pending queue is empty, verify all 550 detailed banks and the final package, distinguish topic-planning completion from research/media production, give the saved deliverable and pause the continuation. Never mark all work complete while initial maps remain.
