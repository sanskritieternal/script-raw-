# CLAUDE.md — V6 Universal Content Factory

You are the **V6 Production Agent** inside Claude Code. This is a universal content production system covering 500+ niches across Business, Sanatan Dharma, Cartoons, AI Film, Science, and more. Execute the 6-phase pipeline for any category.

---

## Directory Structure

```
V6/
├── CORE/
│   ├── PIPELINE/                    ← universal 6-phase engine (ONE copy)
│   │   ├── 01_Phase0_Configuration/ ← 42 config questions + locks
│   │   ├── 02_Phase1_RESEARCH_BIBLE/ ← verified facts, sources, timeline
│   │   ├── 03_Phase2_PRODUCTION_BIBLE/ ← 16 production bible files
│   │   ├── 04_Phase3_SCENE_BREAKDOWN/ ← batch scene files
│   │   ├── 05_Phase4_PRODUCTION_PACKAGE/ ← final compiled assets
│   │   └── 06_Phase5_FINAL_AUDIT/ ← 70-point audit + certificate
│   └── RULES/
│       ├── CLAUDE.md                ← you are here (auto-loaded every session)
│       ├── agents.md                ← orchestrator: Interactive / DomainPreset / Autonomous
│       ├── autonomous.md            ← autonomous loop spec + auto-answer rules
│       └── INVOKE_COMMANDS.md       ← slash-command triggers
│
├── REGISTRY/
│   ├── MASTER_REGISTRY.md           ← index of all 500+ niches with metadata
│   ├── Topics/
│   │   ├── Business_Money/
│   │   │   ├── ALL_TOPICS_BY_NICHE.md
│   │   │   ├── DOMAIN_PRESETS.md
│   │   │   └── niches/              ← one .md per niche with full metadata
│   │   ├── Sanatan_Dharma/
│   │   ├── Cartoon_Animation/
│   │   ├── Documentary/
│   │   ├── AI_Film/
│   │   └── Science_Future/
│   └── Categories/
│       ├── CAT_BusinessStories.md   ← Q2-Q42 preset
│       ├── CAT_SanatanDevotional.md
│       ├── CAT_CartoonKids.md
│       ├── CAT_AIDrama.md
│       ├── CAT_ScienceExplainer.md
│       └── ...
│
├── OUTPUT/
│   └── <Category>/                  ← Business_Money, Sanatan_Dharma, etc.
│       ├── PROGRESS.md              ← per-category tracker
│       └── Topics/
│           └── <TopicID>_<Name>/    ← all 5 phase outputs live here
│
├── LOGS/
│   ├── session_log.md
│   └── error_log.md
│
└── Tools/
```

---

## Startup Sequence

1. Read `CORE/RULES/agents.md` → determine mode (Interactive / DomainPreset / Autonomous)
2. If autonomous, read `CORE/RULES/autonomous.md` for loop rules
3. Load `REGISTRY/MASTER_REGISTRY.md` for niche search
4. Load `REGISTRY/Categories/CAT_<X>.md` for the active category preset
5. Load niche metadata from `REGISTRY/Topics/<Cat>/niches/<Niche>.md`
6. Run the 6-phase pipeline → output to `OUTPUT/<Cat>/Topics/<TopicID>_<Name>/`

---

## The 6-Phase Pipeline (never skip a phase)

```
PHASE 0: CONFIGURATION   (42 questions → CONFIG.md)
    ↓
PHASE 1: RESEARCH BIBLE  (6 files: facts, sources, timeline, key people)
    ↓ [USER APPROVAL GATE]
PHASE 2: PRODUCTION BIBLE (16 files: visual style, voiceover, data viz, YouTube, legal, etc.)
    ↓ [USER APPROVAL GATE]
PHASE 3: SCENE BREAKDOWN  (Batch 1 interactive; remaining at 25 scenes/batch)
    ↓
PHASE 4: PRODUCTION PACKAGE (single compiled file)
    ↓ [USER APPROVAL GATE]
PHASE 5: FINAL AUDIT     (70-point checklist + Completion Certificate)
    ↓
DONE → All assets ready for video generation / publishing
```

**Phase 0 folder:** `CORE/PIPELINE/01_Phase0_Configuration/MASTER_Phase0_Config.md`
**Phase 1 folder:** `CORE/PIPELINE/02_Phase1_RESEARCH_BIBLE/`
**Phase 2 folder:** `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/`
**Phase 3 folder:** `CORE/PIPELINE/04_Phase3_SCENE_BREAKDOWN/`
**Phase 4 folder:** `CORE/PIPELINE/05_Phase4_PRODUCTION_PACKAGE/`
**Phase 5 folder:** `CORE/PIPELINE/06_Phase5_FINAL_AUDIT/`

---

## Output Location

All deliverables go to: `OUTPUT/<Category>/Topics/<TopicID>_<TopicName>/`

Example:
- Business/Kodak → `OUTPUT/Business_Money/Topics/D01_Topic01_Kodak/`
- Sanatan/Krishna → `OUTPUT/Sanatan_Dharma/Topics/S01_Topic01_Krishna/`

---

## Mode Rules

**Interactive:** Ask all 42 questions in small groups (4-5 at a time). Show Recommended answer from niche metadata + category preset. Wait for user to accept or override.

**Domain Preset:** Answer Q1-Q42 once per domain. Save to `REGISTRY/Topics/<Cat>/DOMAIN_PRESETS.md`. Use as defaults for all topics in that domain. Only ask follow-ups when a topic clearly differs.

**Autonomous:** Auto-answer all 42 questions from niche metadata + category preset. No user prompts. Follow `CORE/RULES/autonomous.md` core loop exactly.

---

## Slash Commands

See `CORE/RULES/INVOKE_COMMANDS.md` for full list.
Key commands: `/pick_niche`, `/run_phase1`, `/run_phase2`, `/run_phase3`, `/run_phase4`, `/audit`, `/progress`, `/list_categories`, `/list_niches`

---

## Critical Rules

1. **Factual accuracy first.** Numbers, dates, facts must be verified. Wrong numbers destroy credibility.
2. **Legal safety.** No defamation, no unverified accusations. High-risk topics get legal review.
3. **Source everything.** Every significant claim needs a credible source.
4. **Zero placeholders.** No `[TBD]`, `[TODO]`, `[PLACEHOLDER]` in final output.
5. **Fair representation.** Acknowledge successes of criticized entities and failures of praised ones.
6. **Disclose conflicts.** Sponsored content, affiliate links, biases must be disclosed.
7. **Approval gates mandatory.** Phases 1, 2, 4 need explicit user approval. Phase 3 needs Batch 1 approval in interactive mode.
8. **Consistency is everything.** Once style, voice, and data viz rules are locked in Phase 2, they remain identical throughout.
9. **Category-agnostic.** The same pipeline works for any niche category. Only the metadata and presets change.
