# V6 — How The Process Works

> Read this first. It explains the entire video production pipeline from start to finish,
> how all the files connect, and what happens at each step.

---

## THE BIG PICTURE

You have 500+ content niches (topics) organized into 6 categories. For each topic, the system
produces a complete YouTube video package — ~28 files covering research, script, scenes,
visual style, AI prompts, and audit. Everything follows the same 6-phase pipeline.

```
NICHE (topic idea)
  → PHASE 0: Answer 42 questions → CONFIG.md
    → PHASE 1: Research → 6 files of verified facts
      → PHASE 2: Lock creative decisions → 16 production files
        → PHASE 3: Break into scenes → batch files (~75 scenes)
          → PHASE 4: Compile everything → Production_Package.md
            → PHASE 5: 70-point audit → Certificate
              → DONE: Ready for video generation
```

You run this pipeline in one of three modes (Interactive, Domain Preset, or Autonomous).
The mode controls how much you interact vs. how much runs on its own.

---

## THE 6 PHASES — WHAT EACH ONE DOES

### PHASE 0: CONFIGURATION

**What it does:** Answers 42 questions that define every creative and technical decision
for the video. These answers become the DNA of the entire project — every downstream phase
reads from them.

**Where the answers come from:**

1. **Niche metadata** — loaded from `REGISTRY/MASTER_REGISTRY.md`. Each niche entry has
   pre-written metadata: visual style, tone, target audience, key facts, key sources.

2. **Category preset** — loaded from `REGISTRY/Categories/CAT_<X>.md`. These are reusable
   templates that provide Q2-Q42 defaults for 11 content styles. For example:
   - `CAT_BusinessStories.md` → "Rise/Fall Narrative" story angle, timeline visualization
   - `CAT_SanatanDevotional.md` → "Mythology" angle, sacred cinematic visual, devotional voiceover
   - `CAT_ScienceExplainer.md` → "Education Focus" angle, data-heavy, professional voiceover

3. **Visual style** — loaded from `MASTER_VISUAL_STYLE.md` row matching the niche ID.
   Overrides Q15 (visual style) and Q40 (video generation method).

**Priority chain:** Static defaults < CAT preset < Sub-niche type < Visual style.
Each layer can override the one before it.

**Output:** `OUTPUT/<Category>/Topics/<ID>_<TopicName>/01_Phase0_Configuration/CONFIG.md`

**Mode behavior:**
- Interactive: Ask 42 questions in small groups (4-5 at a time), show recommended answers
- Domain Preset: Answer once per domain, save to DOMAIN_PRESETS.md, inherit for all topics
- Autonomous: Auto-answer from metadata + CAT preset, no prompts

---

### PHASE 1: RESEARCH BIBLE

**What it does:** Builds the factual foundation. Research only — no scenes, no visuals,
no voiceover. Every claim needs a source. Every number needs verification.

**Input:** CONFIG.md (all 42 answers) + niche metadata (key facts, key sources)

**6 output files:**

| File | Purpose |
|---|---|
| `Research_Summary.md` | Executive summary, narrative arc, why the story matters |
| `Facts_Documented.md` | Core facts, dates, people, events, cause-and-effect chain |
| `Financial_Figures_Verified.md` | All financial figures with exact values, sources, inflation notes |
| `Timeline_Accuracy_Check.md` | Chronological table, every date source-verified |
| `Source_List_with_Links.md` | Complete bibliography, URLs, credibility ratings |
| `MASTER_CONTEXT_v1.md` | Bridge file — summary + key facts + locked decisions for downstream phases |

**Rules:**
- Every significant claim needs a source
- Financial figures need at least two credible sources or one primary source
- Dates must be cross-checked
- No defamation — use "was accused of" not "committed fraud" unless convicted
- Mark uncertain claims as [UNVERIFIED — NEED SOURCE]
- No [TBD], [TODO], [PLACEHOLDER] allowed

**Mode behavior:**
- Interactive: Generate, present for fact-check, wait for approval
- Domain Preset: Generate, user reviews per domain
- Autonomous: Generate, self-verify, auto-approve

---

### PHASE 2: PRODUCTION BIBLE

**What it does:** Locks all creative and technical decisions. This is the point of no return.
After Phase 2 approval, key decisions cannot change without regenerating everything downstream.

**Input:** CONFIG.md (Phase 0) + all 6 Research Bible files (Phase 1)

**16 output files:**

| # | File | Purpose |
|---|---|---|
| 00 | `Project_Consistency_Rules.md` | **LOCK FILE** — Q3, Q15, Q16, Q42 locked here |
| 01 | `Research_Sources.md` | Consolidated source list (Tier 1/2/3) |
| 02 | `Financial_Data_Verified.md` | Verified financial figures (Business only) |
| 03 | `Accuracy_Verification_Checklist.md` | Category-specific accuracy rules |
| 04 | `Visual_Style_Guide.md` | Full visual direction per scene |
| 05 | `Voiceover_Guide.md` | Voice profile, pacing, tone, language rules |
| 06 | `Data_Visualization_Specs.md` | What charts/graphics appear and how |
| 07 | `YouTube_Strategy.md` | Titles, description, tags, thumbnail, playlist |
| 08 | `Legal_Liability_Guide.md` | Risk areas, disclaimers, legal flags |
| 09 | `Ethical_Storytelling_Guide.md` | Fairness and representation rules |
| 10 | `Scene_Template.md` | Template every scene follows |
| 11 | `Dialogue_Script.md` | Script style, narration rules, language mixing |
| 12 | `Monetization_Strategy.md` | Revenue streams, sponsor integration |
| 13 | `Source_Credibility_Guide.md` | Source hierarchy, tier definitions |
| 14 | `Bias_Prevention_Checklist.md` | Fairness verification checks |
| 15 | `Project_Summary.md` | One-page summary of all Phase 2 decisions |

**What gets LOCKED after Phase 2:**

| Lock | Question | Why |
|---|---|---|
| Story Angle | Q3 | Changes everything downstream |
| Visual Style | Q15 | Must be identical across all scenes |
| Voiceover | Q16 | Same voice throughout entire video |
| Scene Duration | Q42 | Affects scene count and batch calculation |
| Total Duration | Q14 | Affects scene count |
| Language | Q18 | Cannot change mid-script |
| Audience Geo | Q28 | Affects language, tone, references |

**Mode behavior:**
- Interactive: Generate 16 files, present all for review, ask for approval
- Domain Preset: User reviews per domain, approves all topics under it
- Autonomous: Internal consistency check → auto-approve, locks applied

---

### PHASE 3: SCENE BREAKDOWN

**What it does:** Turns the research and production decisions into individual scenes.
Each scene is an 8-second clip (or variable duration) with exact narration, visual direction,
data viz, AI generation prompt, and timing.

**Input:** CONFIG.md + Phase 1 Research Bible + Phase 2 Production Bible

**Scene count formula:**

```
Total Scenes = Total Duration (seconds) ÷ Scene Duration (Q42)
Default:     600s ÷ 8s = 75 scenes
Batch size:  25 scenes per batch
```

| Video Length | Scenes | Batches |
|---|---|---|
| 5 min | ~38 | 2 |
| 8 min | ~60 | 3 |
| 10 min | ~75 | 3 |
| 12 min | ~90 | 4 |
| 15 min | ~113 | 5 |

**Each scene contains:**
- Scene Number, Duration, Chapter, TimeOfDay/Period, Location, Characters
- Visual description (from Q15 visual style)
- Narration text (from Q16 voiceover style)
- On-screen text (from Q20)
- Data visualization (from Q5)
- Music/sound note
- AI generation prompt (for video tool)

**Output:** `Batch_01_Scenes_001-025.md`, `Batch_02_Scenes_026-050.md`, etc.

**Also during Phase 3:**
- `MASTER_CONTEXT_v1.md` gets updated per batch with consistency tracking
- `VOICE_SCRIPT_<lang>.md` files generated if Q19 (additional languages) ≠ None

**Mode behavior:**
- Interactive: Generate Batch 1, ask for approval, then each subsequent batch
- Domain Preset: Batch 1 approved for domain, rest auto-generated
- Autonomous: All batches generated without stopping, internal quality check per batch

---

### PHASE 4: PRODUCTION PACKAGE

**What it does:** Compiles everything into one master file. This is the single document
that contains everything needed to produce the video — full script, all scenes, all sources,
AI prompts, YouTube metadata, legal summary.

**Input:** All outputs from Phases 0-3

**Output:** `Production_Package.md`

**Sections in order:**
1. All scenes merged (from all batch files)
2. Master script (full narration text, timed to scenes)
3. All sources consolidated
4. YouTube metadata (title, description, tags, thumbnail)
5. Legal review summary
6. AI generation prompts (per scene)
7. Final production checklist

**Mode behavior:**
- Interactive: Present for review, ask for approval
- Domain Preset: Auto-approve after Phase 2
- Autonomous: Compilation check → auto-approve

---

### PHASE 5: FINAL AUDIT

**What it does:** 70-point quality check. Issues the Completion Certificate.
This is the final gate before the video is ready for production.

**Input:** Production_Package.md (everything)

**10 audit categories:**

| # | Check | Max Failures |
|---|---|---|
| 1 | Factual accuracy (every claim sourced, dates verified) | 0 |
| 2 | Source attribution (every quote attributed, every number cited) | 0 |
| 3 | Legal/liability (disclaimers present, no defamation) | 0 |
| 4 | Bias/fairness (both sides presented, balanced narrative) | 1 |
| 5 | Consistency (locked values unchanged from Phase 2) | 0 |
| 6 | Scene count (matches Q14 ÷ Q42 calculation) | 0 |
| 7 | No placeholders (zero [TBD], [TODO], etc.) | 0 |
| 8 | Format compliance (all files present, correct structure) | 0 |
| 9 | Category-specific (scriptural for Sanatan, peer-reviewed for Science) | 0 |
| 10 | YouTube optimization (title, tags, thumbnail) | 0 |

**Output:**
- `Audit_Report.md` — per-check: PASS / FAIL / WARNING
- `Completion_Certificate.md` — topic officially marked complete

**After audit:**
- `PROGRESS.md` updated (topic marked complete)
- `MASTER_REGISTRY.md` updated (completion date added)

**Mode behavior:**
- Interactive: Present results, user reviews certificate
- Domain Preset: Auto-audit, user reviews certificate per domain
- Autonomous: Auto-audit, auto-issue certificate, update PROGRESS.md

---

## THE COMPLETE FILE INVENTORY (per topic)

```
OUTPUT/<Category>/Topics/<ID>_<TopicName>/
├── 01_Phase0_Configuration/
│   └── CONFIG.md                                              (1 file)
├── 02_Phase1_RESEARCH_BIBLE/
│   ├── Research_Summary.md                                    (1)
│   ├── Facts_Documented.md                                    (1)
│   ├── Financial_Figures_Verified.md                          (1)
│   ├── Timeline_Accuracy_Check.md                             (1)
│   ├── Source_List_with_Links.md                              (1)
│   └── MASTER_CONTEXT_v1.md                                   (1)
├── 03_Phase2_PRODUCTION_BIBLE/
│   ├── 00_Project_Consistency_Rules.md                        (1)
│   ├── 01_Research_Sources.md                                 (1)
│   ├── 02_Financial_Data_Verified.md                          (1, Business only)
│   ├── 03_Accuracy_Verification_Checklist.md                  (1)
│   ├── 04_Visual_Style_Guide.md                               (1)
│   ├── 05_Voiceover_Guide.md                                  (1)
│   ├── 06_Data_Visualization_Specs.md                         (1)
│   ├── 07_YouTube_Strategy.md                                 (1)
│   ├── 08_Legal_Liability_Guide.md                            (1)
│   ├── 09_Ethical_Storytelling_Guide.md                       (1)
│   ├── 10_Scene_Template.md                                   (1)
│   ├── 11_Dialogue_Script.md                                  (1)
│   ├── 12_Monetization_Strategy.md                            (1)
│   ├── 13_Source_Credibility_Guide.md                         (1)
│   ├── 14_Bias_Prevention_Checklist.md                        (1)
│   └── 15_Project_Summary.md                                  (1)
├── 04_Phase3_SCENE_BREAKDOWN/
│   ├── Batch_01_Scenes_001-025.md                             (~3 for 10min)
│   ├── Batch_02_Scenes_026-050.md
│   └── Batch_03_Scenes_051-075.md
├── 05_Phase4_PRODUCTION_PACKAGE/
│   └── Production_Package.md                                  (1)
└── 06_Phase5_FINAL_AUDIT/
    ├── Audit_Report.md                                         (1)
    └── Completion_Certificate.md                              (1)

Total: ~27-28 files per topic
```

---

## THE 3 OPERATING MODES

### Interactive Mode

```
User: /mode interactive
  → Select a niche
  → Answer 42 questions (4-5 at a time), see recommended answers
  → Approve CONFIG.md
  → Review Phase 1 (Research Bible), approve
  → Review Phase 2 (16 production files), approve → LOCKS APPLIED
  → Review Batch 1 of scenes, approve
  → Review remaining batches
  → Review Production Package, approve
  → Review Audit + Certificate
  → One topic complete
```

**Use when:** Custom content, creative control, sensitive topics, new categories.
**Speed:** Slow. One topic at a time with full control.

### Domain Preset Mode

```
User: /mode domainpreset
  → Select a domain (e.g., "Company Rise & Fall")
  → Answer 42 questions ONCE
  → Save to DOMAIN_PRESETS.md
  → For each topic in domain:
      → Load domain preset as defaults
      → Only ask if topic clearly differs
      → Run through all 6 phases
      → User reviews per phase (not per topic)
```

**Use when:** 10-20 topics in the same category share settings.
**Speed:** Medium. One domain at a time.

### Autonomous Mode

```
User: /mode autonomous (or PROGRESS.md exists)
  → System reads PROGRESS.md
  → Finds next incomplete topic
  → Auto-answers all 42 questions from metadata + CAT preset
  → Runs Phases 0-5 without stopping
  → Auto-approves all gates (internal quality checks)
  → Writes Completion Certificate
  → Updates PROGRESS.md
  → Moves to next topic
  → Repeats until queue is empty
```

**Use when:** Bulk production across many topics.
**Speed:** Fast. Processes entire queue without stopping.

---

## HOW THE FILES CONNECT (data flow)

```
REGISTRY/                          SOURCE DATA (read-only templates)
├── MASTER_REGISTRY.md             → Niche metadata (500+ entries)
├── MASTER_VISUAL_STYLE.md         → Visual style per niche ID
├── Categories/CAT_*.md            → Q2-Q42 defaults per content style
└── Topics/<Cat>/niches/           → Per-niche metadata files

        ↓ [Phase 0 reads these]

OUTPUT/<Cat>/Topics/<ID>_<Name>/01_Phase0_Configuration/
└── CONFIG.md                      → ALL 42 ANSWERS (feeds everything downstream)

        ↓ [Phase 1 reads CONFIG.md + niche metadata]

OUTPUT/.../02_Phase1_RESEARCH_BIBLE/   (6 files)
└── MASTER_CONTEXT_v1.md               → BRIDGE FILE (updated through Phase 3)

        ↓ [Phase 2 reads CONFIG.md + Phase 1 files]

OUTPUT/.../03_Phase2_PRODUCTION_BIBLE/  (16 files)
└── 00_Project_Consistency_Rules.md     → LOCKS (Q3, Q15, Q16, Q42 permanent)

        ↓ [Phase 3 reads CONFIG.md + Phase 1 + Phase 2]

OUTPUT/.../04_Phase3_SCENE_BREAKDOWN/   (batch files)
└── Updates MASTER_CONTEXT_v1.md per batch

        ↓ [Phase 4 reads ALL previous phases]

OUTPUT/.../05_Phase4_PRODUCTION_PACKAGE/
└── Production_Package.md               → ONE FILE with everything

        ↓ [Phase 5 reads Production_Package.md]

OUTPUT/.../06_Phase5_FINAL_AUDIT/
├── Audit_Report.md
└── Completion_Certificate.md           → TOPIC COMPLETE

        ↓ [After Phase 5]

OUTPUT/<Cat>/PROGRESS.md                → Updated with completion
REGISTRY/MASTER_REGISTRY.md            → Niche marked complete
```

---

## APPROVAL GATES

| Gate | Phase | What's Locked | Can Change Later? |
|---|---|---|---|
| 0 | Phase 0 | CONFIG.md (all 42 answers) | Yes — until Phase 2 |
| 1 | Phase 1 | Research Bible (facts, sources) | Yes — until Phase 2 |
| 2 | Phase 2 | **Q3, Q15, Q16, Q42** + 16 production files | **No — locked permanently** |
| 3 | Phase 3 | Scene breakdown (batches) | Requires Phase 2 regen |
| 4 | Phase 4 | Production Package | Requires Phase 2 regen |
| 5 | Phase 5 | Audit + Certificate | Final |

**After Phase 2 approval:** Q3 (Story Angle), Q15 (Visual Style), Q16 (Voiceover),
Q42 (Scene Duration) are PERMANENT. Changing any requires regenerating ALL downstream phases.

---

## THE 6 CATEGORIES AND THEIR PRESETS

| Category Folder | Content Type | CAT Preset |
|---|---|---|
| `Business_Money` | Company stories, startups, scandals, markets, luxury | `CAT_BusinessStories` (or sub-preset) |
| `Sanatan_Dharma` | Hindu mythology, spirituality, temples, philosophy | `CAT_SanatanDevotional` |
| `Cartoon_Animation` | Kids cartoons, animated stories | `CAT_CartoonKids` |
| `Documentary` | History, biographies, investigations | `CAT_ScienceExplainer` |
| `AI_Film` | AI drama, cinematic shorts | `CAT_AIDrama` |
| `Science_Future` | Science, space, future tech | `CAT_ScienceExplainer` |

Within Business_Money, 8 sub-presets handle different domains:
Company Stories, People & Personalities, Innovation & Tech, Scandals & Fraud,
Industry & Markets, Luxury & Consumer, Workplace & Labor.

---

## SCENE DURATION AND BATCHING

The scene count determines how many batch files Phase 3 produces:

```
Scene Duration = Q42 (from CONFIG.md)
  - FIXED 8-SECOND → every scene = 8 seconds
  - VARIABLE → scene type determines duration

Total Scenes = Q14 (Total Duration in seconds) ÷ Q42 (Scene Duration)
Batch Size = 25 scenes
Batches = ceil(Total Scenes / 25)
```

Example: 10-minute video at 8s/scene = 600 ÷ 8 = 75 scenes = 3 batches.

---

## WHAT HAPPENS AT THE END

After Phase 5 completes:

1. **Completion Certificate** issued — topic marked done
2. **PROGRESS.md** updated — domain counter incremented
3. **MASTER_REGISTRY.md** updated — niche marked with completion date
4. **All 27-28 files** in the topic folder are ready for:
   - AI video generation (using the AI prompts in Production_Package.md)
   - Voiceover recording (using the script in Production_Package.md)
   - YouTube upload (using the metadata in Production_Package.md)
   - Thumbnail design (using the concept in YouTube_Strategy.md)

The output is a complete production package — everything a video editor or AI tool needs
to produce the final video without any additional research or decision-making.
# Repository audit and migration notes

Before generating or relocating topics, read [the improvement plan](AUDIT/IMPROVEMENT_PLAN.md), [category migration design](AUDIT/CATEGORY_MIGRATION.md), and [configuration wiring contract](AUDIT/CONFIGURATION_WIRING.md). Run `python audit_repository.py` to refresh the checkmarked file inventory and structural report.

