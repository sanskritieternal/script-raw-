# Topic coverage, ideas and series

## Where these fit

Niche → topic coverage → registered angle → bounded episode idea → CONFIG → research → production bible → scenes → compiled package → text audit.

A topic describes what to learn about. An angle describes the perspective. An idea binds a question to a case, audience and evidence plan. A series proposes an order for ideas. None of these planning records verifies the factual claims of an episode.

Browse [DEPTH_MASTER_LIST.md](DEPTH_MASTER_LIST.md), [IDEA_MASTER_LIST.md](IDEA_MASTER_LIST.md) and [SOURCE_LIBRARY.md](SOURCE_LIBRARY.md).

## Files and editing

Optional niche path: `REGISTRY/Niches/<ID>_<slug>/Planning/DEPTH_PLAN.json`.

The JSON is the editable source. `TOPIC_MAP.md` and `SERIES_PLAN.md` beside it are generated reading views. Planning lives inside the existing niche home; it introduces no new subject folder or competing CAT defaults. Existing niches without a depth plan remain supported.

Each topic records a stable `TOP-<niche>-<number>` ID, title, level, prerequisite topic IDs, coverage, exclusions, evidence required, registered angle slugs, shared source IDs, concrete idea IDs and next action. Empty idea/source lists honestly identify open coverage. Foundation/intermediate/advanced refer to learning progression, not content verification.

Each series records a stable `SER-<niche>-<number>` ID, title, entry requirement, learning outcome, ordering reason and ordered idea IDs. The order is editorial guidance, not a scheduler or production gate. The validator checks references and prerequisite cycles; editors assess whether the sequence makes sense. There is no fixed topic, idea or series limit.

Retain IDs when revising. An idea maps to one primary topic within a plan; use `related_ideas` for connections. Its `topic` title and selected angle must match the map. Add a related cross-niche idea deliberately rather than copying a question into several homes.

## Sources and readiness

Edit `REGISTRY/SOURCE_LIBRARY.json` to maintain reusable source metadata: stable `SRC-<number>` ID, publisher, URL, edition/context, research locator, access status, check/attempt dates, inspection note, limitations, rights note and refresh trigger. This library stores references, not downloaded copyrighted content or a global ledger of verified claims.

`checked` records what was actually accessible and inspected. It does not mean every passage, calculation or claim has been verified. Failed access is `unverified`, with null `checked_date` and an honest attempted-access note. A library reference does not grant translation, figure, music, voice or footage permissions.

Idea banks retain their existing source snapshots. Refresh them deliberately when a source changes; a library edit does not silently update an idea or existing CONFIG. A ready idea requires the existing readiness gate. Ideas in inaccessible-source research stay `researching`. Phase 1 must inspect the relevant passages and create its own claim ledger with exact locators and evidence. A source check is not a substitute for this work.

## Commands

From the repository root, after editing plans, source records or mapped ideas:

```powershell
python -m Tools.projects.idea_bank build-index
python -m Tools.depth_planning build-index
python -m Tools.depth_planning validate
python -m Tools.validation.validate_repository
```

The depth builder validates before writing and updates only generated reading views. Repository validation includes source identities, topic/angle/idea/source references, prerequisite cycles, series membership and view freshness. It does not assess truth, semantic duplication, full topic coverage or review authenticity.

Select a ready idea using the existing `python -m Tools.projects.create_project --id <ID> --idea-id <ID> --dry-run` route before creating an episode. CONFIG snapshots the existing idea record; it does not automatically snapshot the whole topic map or series. Copy relevant coverage/exclusions into the research summary and identify the series/topic IDs there for traceability. Q1–Q42 meanings and production locks remain unchanged.

## Current pilot and next expansion

Five niches have eight initial topics and one three-idea series each: 001, 004, 008, 343 and 501. This is a depth pilot, not comprehensive coverage of those subjects. Twelve ideas have source-feasibility readiness; three sacred-text ideas remain researching because source access/edition selection is unresolved. The unrelated 531 idea stays proposed.

Before extending to other niches, review the five maps for coverage and boundaries, resolve the three source-access blockers, and perform claim-level research on a selected ready idea. New topics should solve a specific coverage gap. Do not generate empty maps for every niche as a measure of completion.

The user will generate media with external AI tools. Follow [AI generation handoff](../CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/AI_GENERATION_HANDOFF.md); this depth pilot requires no audiovisual generation or rendering demonstration.
