# Episode idea banks

## What an idea adds

Optional topic maps and proposed series now link concrete ideas to coverage and learning progression. See [DEPTH_PLANNING_GUIDE.md](DEPTH_PLANNING_GUIDE.md) and [DEPTH_MASTER_LIST.md](DEPTH_MASTER_LIST.md). The source library is a reusable discovery catalog; idea banks retain explicit source snapshots. Rebuild both idea and depth views after editing a mapped idea.

Niche identifies a subject home; topic is a subject within it; angle is a research perspective; an episode idea identifies a concrete question, case, context, audience and purpose. The bank bridges planning angles and creation of an actual CONFIG. It does not duplicate the angle plan or verify episode claims.

Optional path: `REGISTRY/Niches/<ID>_<slug>/IDEA_BANK.json`. Browse [IDEA_MASTER_LIST.md](IDEA_MASTER_LIST.md); field definitions are in [IDEA_BANK_SCHEMA.json](IDEA_BANK_SCHEMA.json). Do not create hundreds of empty banks or populate generic questions automatically. Add entries when concrete proposals exist.

## Identity and fields

Use stable IDs such as `IDEA-531-0001`. The niche segment must match the bank. Preserve IDs when revising or archiving; do not recycle rejected entries. Required fields cover topic, angle slug, working title, research question, case, place/period/version, intended audience, purpose, dates, candidate sources, evidence gaps, blocking gaps, related idea IDs, readiness note and status.

These are idea-level decisions, not new Q numbers. CONFIG's 42 answers still control production. Intent may change during research, but a changed story/angle must be reflected explicitly upstream; do not silently override a selected idea's question at project creation.

## Status and readiness

| Status | Meaning |
|---|---|
| proposed | A concrete question/case exists; feasibility has not been established |
| researching | Preliminary source/scope work is underway; no episode is claimed ready |
| ready_for_project | At least one source-access check is recorded, a readiness note explains feasibility, and blocking gaps are empty |
| rejected | Retained with an explanation in readiness_note; not selectable |
| archived | Retained for reference; not selectable |

A checked source candidate needs an actual ISO check date and a note explaining what was inspected. An unverified lead has a null checked_date. A checked entry means source access/feasibility was reviewed, not that every proposed claim is true. Do not promote an idea simply to get past a validation gate. The software verifies record structure, not the authenticity of a check.

Ready permits project creation only. Phase 1 still requires a verified claim ledger and applicable publication review. Media generation happens externally after the text-package handoff. The current live statuses and counts are in IDEA_MASTER_LIST.md; historical seed status is not an ongoing readiness decision.

## Commands

Preview or create an optional empty bank only when needed:

```powershell
python idea_bank.py init --id 531
python idea_bank.py init --id 531 --write
```

Existing banks are never overwritten by init. To add a concrete idea, prepare a JSON object matching `$defs.idea` in the schema. Its idea_id may be omitted for next-ID allocation; all other required fields must be supplied. Preview then write:

```powershell
python idea_bank.py add --id 531 --file idea.json
python idea_bank.py add --id 531 --file idea.json --write
```

Duplicate IDs or normalized duplicate questions inside one bank are rejected. Related IDs must refer to existing ideas and cannot refer to self. A cross-bank exact-question overlap is reported as a review signal, not automatically proof of duplication. Edit an existing bank deliberately to revise a record or status; keep dates and readiness/gaps accurate. Keep retired entries rather than deleting their IDs.

After editing:

```powershell
python idea_bank.py build-index
python idea_bank.py validate
```

Repository validation also checks optional banks, related references and index freshness. Older niches without banks remain valid. None of these commands creates an episode.

## Create an episode from a ready idea

```powershell
python create_project.py --id 531 --idea-id IDEA-531-0001 --dry-run
python create_project.py --id 531 --idea-id IDEA-531-0001 --mode autonomous
```

These example commands will reject the seeded proposed idea until real feasibility work supports its promotion. The selected idea supplies angle and story question. Conflicting explicit --angle or --story-question values are rejected. You may still create an episode through the existing --angle plus --story-question path without using a bank.

CONFIG retains the idea ID, source bank path, complete creation-time JSON snapshot and canonical SHA-256. Validation checks snapshot integrity and agreement with niche, story and angle. Later edits or archival in the live bank do not rewrite or invalidate a correctly snapshotted project. The bank itself need not remain present to validate an existing snapshot. A deliberate project change requires a reviewed configuration revision and regeneration of downstream content, not changing the bank alone.

The package compiler already includes CONFIG in its source snapshot. Therefore the selected idea travels into the compiled package, and changing CONFIG invalidates its package hash. No separate competing story-question source is introduced.
