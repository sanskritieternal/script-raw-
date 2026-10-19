# Shared production workflow 1.0

For this user's external AI media generation workflow, follow [AI_GENERATION_HANDOFF.md](AI_GENERATION_HANDOFF.md). Deliver the researched scene/prompt package; audiovisual generation is outside the current planning task. Planned asset status remains valid and does not assert that media exists.

Reusable across all registered niches. Configuration question schema remains 5.0; production workflow versioning is separate. The shared templates contain no episode 501 medical story.

## 1. Shared templates

Preserve outputs 00-15. Ten supporting documents are now standard: YOUTUBE_METADATA.md, STORY_BEAT_MAP.md, CHARACTER_WORLD_GUIDE.md, CAMERA_ANIMATION_GUIDE.md, MUSIC_SOUND_GUIDE.md, ASSET_REGISTER.md, DELIVERY_CHECKLIST.md, REVIEW_REVISION_LOG.md, VIEWER_GLOSSARY.md and ORIGINALITY_REVIEW.md. PRODUCTION_WORKFLOW.json defines applicability, supporting field checks and placement in the compiled package.

## 2. Applicability by episode

Each enrolled episode has all 26 files plus PRODUCTION_MANIFEST.json. Each document has status `draft`, `complete` or `not_applicable`. Drafts fail Phase 2. Allowed not_applicable entries need an episode-specific reason of at least 15 characters and matching “Not applicable” text in the document; remove scaffold content. Core identity, evidence, narration, asset, delivery and review records cannot be waived.

Documentary character/world records describe narrator, sourced entities, periods and depiction limits; fiction records character design, relationships and world continuity. Clearly separate invention from factual assertions. Financial, visualization, glossary or distribution documents may be inapplicable with a justified reason. Beat count fits the episode; it is not fixed at 25. Factual claims still need evidence inside fiction. Niche registry entries are not completed episodes.

## 3. Pipeline connections

Phase 0 supplies identity/language/risk/timing; Phase 1 supplies checked evidence; Phase 2 completes decisions and locks; Phase 3 supplies actual scene and asset references; Phase 4 compiles the snapshot; Phase 5 audits findings and actual review evidence. No command creates research conclusions, media licenses, human approvals or publication details.

New CONFIG files include `Production workflow version: 1.0`. Older episodes without that marker or a manifest retain their former checks. Adding a manifest enrolls an old episode; removing the manifest from a marked new episode does not bypass validation. No existing episode is silently bulk-migrated.

## 4. Generation and safe migration

`create_project.py` now writes Phase 0 and all 26 draft production files, using the selected niche's actual configuration. Each scaffold is explicitly unfinished and cannot pass production validation. Complete Phase 1 evidence before accepting Phase 2.

Preview an existing episode without writing:

```powershell
python production_workflow.py migrate "OUTPUT/<niche>/<episode>"
```

Write missing files and manifest explicitly:

```powershell
python production_workflow.py migrate "OUTPUT/<niche>/<episode>" --write
```

`scaffold` has the same safe missing-file behavior. Existing editorial documents and CONFIG are preserved byte-for-byte. On initial enrollment only, `--adopt-existing` explicitly marks preserved documents internally complete after your review; new files remain draft. It does not approve evidence, rights, rendering or publication. Existing manifests cannot be reset by migration. Historical OUTPUT/Legacy projects are excluded.

### Structured mappings

The manifest records all 26 statuses, exact Q3/Q15/Q16/Q42 locks, and these arrays once scenes are available:

```json
{
  "beats": [{"start": 1, "end": 2, "claims": ["C001"]}],
  "assets": [{"id": "G01", "scenes": [1, 2], "status": "planned", "file": "graphics/G01.svg"}],
  "chapters": [{"start_seconds": 0, "title": "The question"}]
}
```

This illustrates the field structure, not any real episode's scene count. Beat ranges cover actual scenes exactly once, in order, and list the union of their claim IDs. Asset IDs must appear in ASSET_REGISTER.md and mappings cover all scenes; this explicitly links assets without rewriting legacy scene fields. Planned assets need not exist. Created/reviewed assets require actual in-episode files; reviewed entries require review evidence.

Applicable YouTube chapters start at zero and use unique actual scene boundaries; time/title lines in YOUTUBE_METADATA.md must agree exactly with the manifest. If distribution makes YouTube inapplicable, record the reason and leave chapters empty. Unknown actual URL/date/license/reviewer values may honestly remain Pending; unfinished editorial content may not be disguised as complete.

## 5. Compilation and validation

```powershell
python validate_project.py "OUTPUT/<niche>/<episode>" --through 3
python production_workflow.py compile "OUTPUT/<niche>/<episode>"
python production_workflow.py compile "OUTPUT/<niche>/<episode>" --write
python validate_project.py "OUTPUT/<niche>/<episode>" --through 4
```

Compilation requires Phase 0-3 validation. It retains scenes verbatim, extracts narration and source citations, includes all research Markdown and all 26 production documents in eleven canonical sections, and records asset mappings and hashes. AI prompts are episode-specific if applicable; no tool is chosen automatically.

Package_Inputs.json fingerprints CONFIG, research, production/manifest, scene files, shared workflow specification, compiler implementation and package output. Upstream changes, compiler changes or manual package edits invalidate Phase 4 until rebuilding. Previous packages are retained under `05_Phase4_PRODUCTION_PACKAGE/History/<hash>/`.

The dedicated AI generation section collects supplied scene prompts, overlay instructions, reference inputs, start/end states, asset IDs and execution records. Inline and multiline prompt fields are supported. It invents no prompt for a scene that has none and selects no provider. The complete original scene records are still preserved in the scene section. Older packages without the compiler fingerprint require rebuilding before passing current Phase 4 freshness checks.

Validation checks status, placeholders, links, locks, fields, claim/scene references, beat coverage, assets, chapter timing and package freshness. It cannot establish source truth, originality, real rights, actual audiovisual quality, platform eligibility or reviewer authenticity. Required human-review/certification gates remain unchanged.

## 6. Existing-project rollout and tests

Preview migration per episode, preserve existing work, assess applicability, finish missing content and fill actual mappings before compilation. The earlier 501 episode folder is absent in the current workspace; it cannot be migrated here. Do not reconstruct its evidence or approvals from chat memory. Existing episode copies are used to test migration without rewriting historical pilots.

Run `python -m unittest test_contract.py test_production_workflow.py -v`. Coverage includes fresh scaffolds, safe migration, applicability, fixed/variable timing, scene/metadata/assets, package invalidation/rebuild and retained human-review gates. Registry topics remain unchanged.
