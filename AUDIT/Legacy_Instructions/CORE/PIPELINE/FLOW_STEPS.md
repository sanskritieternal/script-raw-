# V6 Flow Step File — Complete Production Pipeline

> Historical detailed flow reference. For current routing, gates, paths and counts use `CORE/PIPELINE/CONTRACT.md` and `REGISTRY/CONFIG_SCHEMA.json`.
> Every step, file, decision point, and mode-specific behavior documented.

---

## MODE LEGEND

| Symbol | Mode | Behavior |
|---|---|---|
| [I] | Interactive | Ask user, wait for answer, show recommended |
| [D] | Domain Preset | Load DOMAIN_PRESETS.md, only ask if topic differs |
| [A] | Autonomous | Auto-answer from metadata + CAT preset, no prompts |

---

## PHASE 0: CONFIGURATION

**Purpose:** Answer Q1-Q42 for the selected topic. Output feeds every downstream phase.

**Input files:**
- `REGISTRY/MASTER_REGISTRY.md` — niche metadata (key facts, sources, visual style)
- `REGISTRY/Categories/CAT_<X>.md` — category preset (Q2-Q42 defaults)
- `MASTER_VISUAL_STYLE.md` row matching Niche ID — palette, lighting, camera, motion
- `CORE/PIPELINE/01_Phase0_Configuration/MASTER_Phase0_Config.md` — 42 questions definition

**Output file:**
- `OUTPUT/<Category>/Topics/<ID>_<TopicName>/01_Phase0_Configuration/CONFIG.md`

### Step 0.1 — Load Niche Metadata

```
Action:  Read niche entry from MASTER_REGISTRY.md
Input:   Niche ID (e.g., D01_Topic01_Kodak)
Extract: Domain, Category, Visual Style, Tone, Target Audience,
         Duration, B-Roll Priority, Music Style, Key Facts,
         Key Sources, Avoid warnings, CAT preset reference
```

| Mode | Behavior |
|---|---|
| [I] | Display niche metadata summary to user before questions |
| [D] | Load DOMAIN_PRESETS.md if exists, show as defaults |
| [A] | Silently extract all metadata fields |

### Step 0.2 — Load Category Preset

```
Action:  Read CAT_<X>.md for the matching category
Input:   CAT name from niche metadata (e.g., CAT_BusinessStories.md)
Extract: Q2-Q42 defaults, Options lists, Applies-to scope
```

| Mode | Behavior |
|---|---|
| [I] | Show CAT defaults as "Recommended" for each question |
| [D] | CAT defaults become domain-level defaults |
| [A] | CAT defaults become the answer unless overridden |

### Step 0.3 — Load Visual Style

```
Action:  Read MASTER_VISUAL_STYLE.md row matching Niche ID
Extract: Primary Visual Style, Visual Language, Palette, Lighting,
         Camera/Lens, Motion, Thumbnail Direction, AI Keywords, Avoid
Override: Q15 (Visual Style Primary), Q40 (Video Generation Method)
```

| Mode | Behavior |
|---|---|
| [I] | Show visual style as recommendation for Q15, Q40 |
| [D] | Visual style locked for entire domain |
| [A] | Auto-apply visual style to Q15, Q40 |

### Step 0.4 — Answer Q1: Content Category

```
Question: What content category does this topic fall under?
Default:  Derived from niche domain
Options:  Business & Money / Sanatan Dharma / Cartoon Animation /
          Documentary / AI Film / Science Future
```

| Mode | Behavior |
|---|---|
| [I] | Ask user, show recommended from niche metadata |
| [D] | Pre-set from domain, confirm once |
| [A] | Auto-set from niche metadata category field |

### Step 0.5 — Answer Q2-Q42

```
For each question (Q2 through Q42):
  1. Start with CAT preset default
  2. Override with sub-niche type rules (if any)
  3. Override with visual style (Q15, Q40)
  4. Present to user or auto-answer

Priority: Static Defaults < CAT Preset < Sub-Niche Override < Visual Style
```

**Sub-niche type overrides (from SUBNICHE_OVERRIDES table):**

| Sub-Niche Type | Q3 Override | Q15 Override | Q16 Override |
|---|---|---|---|
| History & Origins | History & Origins | Archive Footage | Professional Authoritative |
| Famous Examples | Famous Examples | Stock Footage + Graphics | Engaging Storytelling |
| Hidden Stories | Hidden Stories | Documentary Realism | Documentary Calm |
| Beginner Explainers | Education Focus | Animated Explainers | Engaging Storytelling |
| Advanced Concepts | Advanced Concepts | Data Viz Heavy | Professional Authoritative |
| Mysteries & Unsolved Cases | Mystery | Documentary Realism | Critical Analytical |
| Technology & Innovation | Innovation Focus | Animation + Data Viz | Enthusiastic |
| People & Personalities | People Focus | Stock Footage + Graphics | Engaging Storytelling |
| Major Events | Major Events | Archive Footage | Professional Authoritative |
| How It Works | Education Focus | Animated Explainers | Engaging Storytelling |
| Rise & Fall | Rise/Fall Narrative | Timeline Visualization | Engaging Storytelling |
| Then vs Now | Then vs Now | Data Viz Heavy | Professional Authoritative |
| Future Developments | Innovation Focus | Animation + Data Viz | Enthusiastic |
| Myths vs Facts | Myths vs Facts | Infographics + Text Overlay | Critical Analytical |
| Documentary Stories | Documentary Focus | Documentary + Interview Hybrid | Documentary Calm |

| Mode | Behavior |
|---|---|
| [I] | Ask 4-5 questions at a time. Show "Recommended" label with merged default. User accepts or overrides. |
| [D] | Show all 42 with domain defaults. Only ask if user wants to change a specific answer. |
| [A] | Auto-answer all 42 silently. No prompts. |

### Step 0.6 — Write CONFIG.md

```
Action:  Write all 42 answers to CONFIG.md
Format:  Q1-Q42 with answers, recommended source, override notes
Output:  OUTPUT/<Category>/Topics/<ID>_<TopicName>/01_Phase0_Configuration/CONFIG.md
```

| Mode | Behavior |
|---|---|
| [I] | Write after user confirms all answers |
| [D] | Write after domain preset confirmation |
| [A] | Write immediately after auto-answering |

### Step 0.7 — Approval Gate

```
Gate: Phase 0 complete
Next:  Phase 1 — Research Bible
```

| Mode | Behavior |
|---|---|
| [I] | "CONFIG.md ready. Approve to proceed to Phase 1?" |
| [D] | Auto-approve after domain preset save |
| [A] | Auto-approve, proceed immediately |

---

## PHASE 1: RESEARCH BIBLE

**Purpose:** Gather verified facts, sources, timeline, key people, and quotes.

**Input files:**
- `CONFIG.md` (from Phase 0) — all 42 answers
- `MASTER_REGISTRY.md` niche entry — Key Facts, Key Sources
- `CORE/PIPELINE/02_Phase1_RESEARCH_BIBLE/MASTER_Phase1_ResearchBible.md` — template + rules

**Output files (6):**

```
OUTPUT/<Category>/Topics/<ID>_<TopicName>/02_Phase1_RESEARCH_BIBLE/
├── Research_Summary.md              ← executive summary, narrative arc
├── Facts_Documented.md              ← core facts, dates, people, events
├── Financial_Figures_Verified.md    ← all financial figures with sources
├── Timeline_Accuracy_Check.md       ← chronological table with date verification
├── Source_List_with_Links.md        ← complete bibliography with URLs + credibility
└── MASTER_CONTEXT_v1.md             ← consolidated context for downstream phases
```

> **MASTER_CONTEXT_v1.md** is the bridge between Phase 1 and all downstream phases. It contains: summary + key facts + locked decisions. It gets updated per batch in Phase 3.

### Step 1.1 — Research Summary

```
Action:  Compile all verified facts about the topic
Output:  Research_Summary.md
Content: Executive summary, key findings, narrative arc, why the story matters now
Rules:   Every significant claim needs a source (Q24)
         No [TBD], [TODO], [PLACEHOLDER] allowed
```

### Step 1.2 — Facts Documented

```
Action:  List core facts, dates, people, companies, key events, cause-and-effect chain
Output:  Facts_Documented.md
Content: Fact entries with source citations, confidence level
Rules:   Every fact needs at least one source
         Conflicting facts flagged for resolution
```

### Step 1.3 — Financial Figures Verified

```
Action:  Compile all financial figures with exact values and sources
Output:  Financial_Figures_Verified.md
Content: Figure, unit, date, source, inflation adjustment, methodology
Rules:   Q4 (Financial Detail Level) controls depth
         Every number needs at least one primary source (SEC filing, annual report)
         Sources that conflict → choose most credible with explanation
```

### Step 1.4 — Timeline Accuracy Check

```
Action:  Build chronological timeline of events
Output:  Timeline_Accuracy_Check.md
Content: Date-stamped events, causal links, gaps flagged
Rules:   Every date must have a source
         Contradictory dates flagged for resolution
```

### Step 1.5 — Source List with Links

```
Action:  List all primary reference sources
Output:  Source_List_with_Links.md
Content: Source name, URL, type, date accessed, credibility rating
Rules:   No Wikipedia as primary source
         Prefer original documents over secondary coverage
         Tier 1 (primary) / Tier 2 (verified media) / Tier 3 (general media)
```

### Step 1.6 — MASTER_CONTEXT_v1.md

```
Action:  Compile the consolidated context document for downstream phases
Output:  MASTER_CONTEXT_v1.md
Content: Summary + key facts + locked decisions from Phase 0 CONFIG.md
Rules:   This is the bridge between Phase 1 and all downstream phases
         Gets updated per batch in Phase 3 with consistency tracking
```

### Step 1.7 — Approval Gate

```
Gate: Phase 1 complete (6 files written)
Gate Check: All facts sourced, no placeholders, timeline verified
Next:  Phase 2 — Production Bible
```

| Mode | Behavior |
|---|---|
| [I] | "Research Bible ready. Review files, then approve for Phase 2?" |
| [D] | User reviews once per domain, approves all topics under it |
| [A] | Self-check passes → auto-approve |

---

## PHASE 2: PRODUCTION BIBLE

**Purpose:** Lock all creative and technical decisions. 16 production files.

**Input files:**
- `CONFIG.md` (Phase 0) — all 42 answers now LOCKED
- `02_Phase1_RESEARCH_BIBLE/` (6 files) — verified facts and sources
- `CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/` (17 template files)

**Output files (16):**

```
OUTPUT/<Category>/Topics/<ID>_<TopicName>/03_Phase2_PRODUCTION_BIBLE/
├── 00_Project_Consistency_Rules.md   ← locks Q3, Q15, Q16, Q42
├── 01_Research_Sources.md            ← consolidated source list
├── 02_Financial_Data_Verified.md     ← Business only
├── 03_Accuracy_Verification_Checklist.md
├── 04_Visual_Style_Guide.md          ← from Q15 + MASTER_VISUAL_STYLE.md
├── 05_Voiceover_Guide.md             ← from Q16 + CAT preset
├── 06_Data_Visualization_Specs.md    ← from Q5, Q15
├── 07_YouTube_Strategy.md            ← from Q26, Q28, Q37
├── 08_Legal_Liability_Guide.md       ← from Q8, Q7, Q31
├── 09_Ethical_Storytelling_Guide.md
├── 10_Scene_Template.md              ← from Q15, Q17, Q42
├── 11_Dialogue_Script.md             ← from Q16, Q18
├── 12_Monetization_Strategy.md       ← from Q13, Q36, Q35
├── 13_Source_Credibility_Guide.md    ← from Q24, Q23
├── 14_Bias_Prevention_Checklist.md
└── 15_Project_Summary.md

Total: 16 files (the Visual Style Quick Reference is embedded in 04_Visual_Style_Guide.md, not a separate file)
```

### Step 2.1 — Project Consistency Rules (LOCK FILE)

```
Action:  Write the lock file — these values cannot change after Phase 2
Locks:   Q3  (Story Angle)
         Q15 (Visual Style Primary)
         Q16 (Voiceover Approach)
         Q42 (Scene Duration Strategy)
         Q14 (Total Duration)
         Q18 (Primary Language)
         Q28 (Audience Geographic Focus)
Rule:    If any locked value needs to change → regenerate Phase 2 entirely
```

### Step 2.2 — Research Sources

```
Action:  Consolidate all sources from Research Bible into one reference
Source:  02_Phase1_RESEARCH_BIBLE/Primary_Sources.md
         02_Phase1_RESEARCH_BIBLE/Quotes_Sources.md
Content: Organized source list by type (primary, secondary, quotes)
Rules:   Q24 source quality standards applied
         Format: [Name] | [Type] | [URL] | [Date Accessed] | [Rating]
```

### Step 2.3 — Financial Data Verified

```
Action:  Final verified financial figures for production
Scope:   Business category only — skip for others
Source:  02_Phase1_RESEARCH_BIBLE/Financial_Data.md
Content: All figures cross-checked, inflation-adjusted, sourced
```

### Step 2.4 — Accuracy Verification Checklist

```
Action:  Build category-specific accuracy rules
Source:  CONFIG.md Q23 (accuracy priority), Q24 (source quality)
Content: Verification rules per claim type, source hierarchy,
         minimum source count per section, red flags
Rules:   Q23=Expert → peer-reviewed sources required
         Q23=General → credible media acceptable
```

### Step 2.5 — Visual Style Guide

```
Action:  Write the definitive visual style document
Source:  CONFIG.md Q15 (visual style), Q40 (video method)
         MASTER_VISUAL_STYLE.md row for this niche
Content: Full visual direction, scene-by-scene style notes,
         color palette, lighting references, camera movements,
         transition rules, thumbnail concept
Rules:   Every scene must follow Q15 style — no exceptions
         Q40 method applies to all scenes uniformly
```

### Step 2.6 — Voiceover Guide

```
Action:  Define voiceover style, pacing, tone rules
Source:  CONFIG.md Q16 (voiceover approach), Q18 (language)
         CAT preset voiceover defaults
Content: Voice profile (gender, age, accent if applicable),
         pacing (words/min), tone rules per scene type,
         language handling (EN / HI_DEV / HI_ROM / BILINGUAL)
Rules:   Same voice throughout entire video
         Q16 locked — cannot change after this phase
```

### Step 2.7 — Data Visualization Specs

```
Action:  Define what data viz appears and how
Source:  CONFIG.md Q5 (data viz priority), Q15 (visual style)
Content: Chart types per data point, animation style,
         color scheme, on-screen labels, data sources
Rules:   Q5=Heavy → every major claim has a visual
         Q5=Minimal → only key numbers visualized
```

### Step 2.8 — YouTube Strategy

```
Action:  Plan the YouTube-specific elements
Source:  CONFIG.md Q26 (platform), Q28 (geography), Q37 (series)
Content: Title (3 variants), description template, tags (20+),
         thumbnail concept, playlist strategy, premiere timing
Rules:   Q26=YouTube+Shorts → plan short-form clips from scenes
         Q28=India-first → Hindi options in metadata
```

### Step 2.9 — Legal Liability Guide

```
Action:  Flag legal risk areas and required disclaimers
Source:  CONFIG.md Q8 (legal concern), Q7 (controversy), Q31 (contested claims)
Content: Risk level, specific risk areas, required disclaimers,
         review checklist, distribution restrictions
Rules:   Q8=High/Critical → legal review mandatory before publish
         Q31=Contested → include multiple perspectives
         Q39 disclaimer text finalized here
```

### Step 2.10 — Ethical Storytelling Guide

```
Action:  Define fairness and representation rules
Source:  CONFIG.md Q7, Q9, Q34 (bias prevention)
Content: Representation rules, balance requirements,
         sensitive topic handling, disclosure requirements
Rules:   Acknowledge successes of criticized subjects
         Acknowledge failures of praised subjects
```

### Step 2.11 — Scene Template

```
Action:  Define the template every scene follows
Source:  CONFIG.md Q42 (scene duration), Q14 (total duration),
         Q15 (visual style), Q17 (delivery format)
Content: Scene structure template (Visual + Audio + Text + Duration),
         scene numbering scheme, batch size rules
Rules:   Q42=FIXED 8-SECOND → every scene = 8s
         Q42=VARIABLE → scene type determines duration
         Total scenes = Total Duration ÷ Scene Duration
```

### Step 2.12 — Dialogue Script

```
Action:  Define script style and narration rules
Source:  CONFIG.md Q16 (voiceover), Q18 (language), Q20 (text strategy)
Content: Narration style (first person / third person / documentary),
         language mixing rules (EN + HI snippets), text overlay rules,
         profanity policy, citation style in script
Rules:   Q16 locked — script must match voiceover profile
         Q18 locked — language cannot change mid-script
```

### Step 2.13 — Monetization Strategy

```
Action:  Plan revenue streams and sponsor integration
Source:  CONFIG.md Q13 (priority), Q36 (revenue model), Q35 (sponsored)
Content: Revenue mix, sponsor integration points,
         affiliate placement, Patreon pitch, merch potential
Rules:   Q35=No → no sponsor reads in script
         Q35=Sponsored → disclosure required in description
```

### Step 2.14 — Source Credibility Guide

```
Action:  Define source hierarchy and credibility ratings
Source:  CONFIG.md Q24 (source quality), Q23 (accuracy priority)
Content: Source tier list (Tier 1 = primary, Tier 2 = verified media,
         Tier 3 = general media), minimum tier per claim type
Rules:   Q24=Critical → only Tier 1 sources allowed
         Q24=Standard → Tier 2 acceptable for most claims
```

### Step 2.15 — Bias Prevention Checklist

```
Action:  Create checklist for fairness verification
Source:  CONFIG.md Q34 (bias strategy)
Content: 5-7 specific checks for this topic's bias risks
Rules:   Applied during Phase 5 audit as well
```

### Step 2.16 — Project Summary

```
Action:  One-page summary of all Phase 2 decisions
Content: All locked values, key creative decisions,
         production specs summary, risk flags
```

### Step 2.17 — Visual Style Quick Reference

```
Action:  Condensed visual catalog for scene generation
Source:  MASTER_VISUAL_STYLE.md row for this niche
Content: One-page visual cheat sheet (palette, lighting, camera,
         motion, AI keywords, avoid list)
```

### Step 2.18 — Approval Gate (CRITICAL)

```
Gate: Phase 2 complete (16 files written)
Gate Check: All locked values set, no contradictions between files
Next:  Phase 3 — Scene Breakdown
WARNING: After approval, Q3, Q15, Q16, Q42 are PERMANENT.
         Changing them requires regenerating ALL downstream phases.
```

| Mode | Behavior |
|---|---|
| [I] | "Production Bible ready (16 files). Review and approve to lock creative decisions?" |
| [D] | User reviews per domain, approves all topics under it |
| [A] | Internal consistency check passes → auto-approve. Locks applied. |

---

## PHASE 3: SCENE BREAKDOWN

**Purpose:** Break the video into individual scenes. Batch-produced (25 scenes per batch).

**Input files:**
- `CONFIG.md` — Q14 (duration), Q42 (scene duration)
- `03_Phase2_PRODUCTION_BIBLE/10_Scene_Template.md` — scene structure
- `02_Phase1_RESEARCH_BIBLE/` — facts, timeline, people, quotes

**Output files (batch files):**

```
OUTPUT/<Category>/Topics/<ID>_<TopicName>/04_Phase3_SCENE_BREAKDOWN/
├── Batch_01_Scenes_001-025.md    ← first batch (interactive approval)
├── Batch_02_Scenes_026-050.md    ← subsequent batches (autonomous)
├── ... (more batches as needed)
```

> **MASTER_CONTEXT_v1.md** (from Phase 1) is updated per batch with consistency tracking.
> **VOICE_SCRIPT_<lang>.md** files are generated if Q19 (Additional Languages) ≠ None.

### Step 3.1 — Calculate Scene Count

```
Formula: Total Scenes = Total Duration (seconds) ÷ Scene Duration (Q42)
Default: 600s ÷ 8s = 75 scenes

Q42 = FIXED 8-SECOND  →  every scene = 8 seconds
Q42 = VARIABLE        →  scene type determines duration
                         (Action: 8s, Dialogue: 10s, Data Viz: 6s, etc.)

Batch size = 25 scenes per batch
```

| Video Length | Scenes | Batches |
|---|---|---|
| 5 min (300s) | ~38 | 2 |
| 8 min (480s) | ~60 | 3 |
| 10 min (600s) | ~75 | 3 |
| 12 min (720s) | ~90 | 4 |
| 15 min (900s) | ~113 | 5 |

### Step 3.2 — Generate Scenes (Batch 1 First)

```
Action:  Generate first 25 scenes using scene template from Phase 2
Output:  Batch_01_Scenes_001-025.md
Each scene: Scene Number, Duration, Chapter, Location, Characters,
            Visual description (Q15 style), Narration (Q16 voice),
            On-screen text (Q20), Data viz (Q5), AI prompt, Music note
```

| Mode | Behavior |
|---|---|
| [I] | Generate Batch 1, present to user, wait for approval |
| [D] | Generate Batch 1, user reviews, approves for this domain |
| [A] | Generate Batch 1, internal quality check, then auto-approve |

### Step 3.3 — Generate Remaining Batches

```
Action:  Generate remaining batches (25 scenes each)
Output:  Batch_NN_Scenes_XX_to_YY.md
Pacing:  1 batch at a time, each following Batch 1's approved style
```

| Mode | Behavior |
|---|---|
| [I] | Generate next batch, ask for approval, repeat |
| [D] | Generate all remaining batches after Batch 1 approval |
| [A] | Generate all remaining batches without stopping |

### Step 3.4 — Update MASTER_CONTEXT_v1.md

```
Action:  Update Phase 1's MASTER_CONTEXT_v1.md per batch
Updates: Scene count progress, consistency notes, any deviations from Phase 2 locks
Rules:   Must not contradict Phase 2 locked values (Q3, Q15, Q16, Q42)
```

### Step 3.5 — Generate VOICE_SCRIPT Files (if needed)

```
Action:  If Q19 (Additional Languages) ≠ None, generate voice scripts
Output:  VOICE_SCRIPT_<lang>.md per additional language
Content: Full narration translated/adapted per language setting
```

### Step 3.6 — Approval Gate

```
Gate: Phase 3 complete (all batches generated)
Gate Check: Scene count matches, no gaps in numbering,
            every scene has all required fields
Next:  Phase 4 — Production Package
```

| Mode | Behavior |
|---|---|
| [I] | "Scene breakdown complete (N scenes in B batches). Approve?" |
| [D] | Auto-approve after Batch 1 |
| [A] | Auto-approve after quality check |

---

## PHASE 4: PRODUCTION PACKAGE

**Purpose:** Compile everything into one master file ready for video production.

**Input files:**
- `CONFIG.md` (Phase 0)
- `02_Phase1_RESEARCH_BIBLE/` (6 files)
- `03_Phase2_PRODUCTION_BIBLE/` (16 files)
- `04_Phase3_SCENE_BREAKDOWN/` (all batch files)

**Output files:**

```
OUTPUT/<Category>/Topics/<ID>_<TopicName>/05_Phase4_PRODUCTION_PACKAGE/
└── Production_Package.md
```

### Step 4.1 — Compile Scenes

```
Action:  Merge all batch files into one scene sequence
Source:  04_Phase3_SCENE_BREAKDOWN/Master_Scene_List.md
Content: Full scene-by-scene breakdown with all details
```

### Step 4.2 — Write Master Script

```
Action:  Compile full narration text from all scenes
Source:  Scene narration fields
Content: Complete voiceover script, timed to scene durations
Rules:   Matches Q16 voiceover style
         Matches Q18 language
         Every fact matches Phase 1 Research Bible
```

### Step 4.3 — Consolidate Sources

```
Action:  Combine all sources into one reference section
Source:  02_Phase1_RESEARCH_BIBLE/Primary_Sources.md
         02_Phase1_RESEARCH_BIBLE/Quotes_Sources.md
         03_Phase2_PRODUCTION_BIBLE/13_Source_Credibility_Guide.md
```

### Step 4.4 — YouTube Metadata

```
Action:  Generate final YouTube metadata
Source:  03_Phase2_PRODUCTION_BIBLE/07_YouTube_Strategy.md
Content: Title (3 options), Description (full), Tags (20+),
         Thumbnail concept, Category, Playlist assignment
```

### Step 4.5 — Legal Review Summary

```
Action:  Summarize all legal flags and required disclaimers
Source:  03_Phase2_PRODUCTION_BIBLE/08_Legal_Liability_Guide.md
Content: Risk level, specific warnings, disclaimer text,
         review status
```

### Step 4.6 — AI Generation Prompts

```
Action:  Write AI video generation prompts for each scene
Source:  Scene visual descriptions + Q40 (video method)
         MASTER_VISUAL_STYLE.md AI keywords
Content: Per-scene AI prompt for video generation tool
         (e.g., Runway, Pika, Midjourney + voiceover)
Rules:   Every prompt includes: style, palette, lighting, camera,
         motion, avoid list from visual style guide
```

### Step 4.7 — Final Production Checklist

```
Action:  Create final pre-publish checklist
Content: All 70 audit points from Phase 5 (pre-checked),
         file inventory, delivery specs
```

### Step 4.8 — Approval Gate

```
Gate: Phase 4 complete (Production_Package.md written)
Next:  Phase 5 — Final Audit
```

| Mode | Behavior |
|---|---|
| [I] | "Production Package ready. Review and approve for final audit?" |
| [D] | Auto-approve after Phase 2 |
| [A] | Auto-approve after compilation check |

---

## PHASE 5: FINAL AUDIT

**Purpose:** 70-point quality check. Issue Completion Certificate.

**Input files:**
- `Production_Package.md` (Phase 4) — everything
- `CORE/PIPELINE/06_Phase5_FINAL_AUDIT/MASTER_Phase5_FinalAudit.md` — audit rules

**Output files:**

```
OUTPUT/<Category>/Topics/<ID>_<TopicName>/06_Phase5_FINAL_AUDIT/
├── Audit_Report.md
└── Completion_Certificate.md
```

### Step 5.1 — Factual Accuracy Check

```
Check:   Every significant claim has a source
         Every date is verified
         Every number is cross-checked
         No contradictory facts
Source:  02_Phase1_RESEARCH_BIBLE/ (all 6 files)
Rules:   Category-specific standards (scriptural for Sanatan,
         peer-reviewed for Science, SEC filings for Business)
Max failures allowed: 0
```

### Step 5.2 — Source Attribution Check

```
Check:   Every quote is attributed
         Every data point has a source citation
         Source credibility matches Q24 standards
Max failures allowed: 0
```

### Step 5.3 — Legal/Liability Check

```
Check:   All Q8 risk areas addressed
         Disclaimers present where required (Q39)
         No defamation, no unverified accusations
         High-risk topics flagged for manual review
Source:  03_Phase2_PRODUCTION_BIBLE/08_Legal_Liability_Guide.md
Max failures allowed: 0 (any failure → manual review required)
```

### Step 5.4 — Bias/Fairness Check

```
Check:   Both sides of contested issues presented
         Successes of criticized subjects included
         Failures of praised subjects included
         No one-sided narratives
Source:  03_Phase2_PRODUCTION_BIBLE/14_Bias_Prevention_Checklist.md
Max failures allowed: 1
```

### Step 5.5 — Consistency Check

```
Check:   Q3, Q15, Q16, Q42 unchanged from Phase 2 locks
         Visual style consistent across all scenes
         Voiceover tone consistent
         Scene count matches Q14 ÷ Q42 calculation
Max failures allowed: 0
```

### Step 5.6 — Scene Count Check

```
Check:   Total scenes = Total Duration (Q14) ÷ Scene Duration (Q42)
         Scene numbers are sequential, no gaps
         Every scene has all required fields
Max failures allowed: 0
```

### Step 5.7 — No Placeholder Check

```
Check:   Zero [TBD], [TODO], [PLACEHOLDER], [INSERT], [ADD LATER]
         Every scene has narration text
         Every scene has visual description
         Every scene has AI prompt
Max failures allowed: 0
```

### Step 5.8 — Format Compliance

```
Check:   All 42 questions answered in CONFIG.md
         All 6 Phase 1 files present
         All 16 Phase 2 files present
         All batch files present with correct scene count
         Production_Package.md complete
Max failures allowed: 0
```

### Step 5.9 — Category-Specific Requirements

```
Business:     Financial figures match SEC filings / annual reports
Sanatan:      Scriptural references verified against primary texts
Cartoon:      Character consistency, moral themes coherent
AI Film:      Technology references plausible, futures grounded
Science:      Claims match peer-reviewed consensus
Documentary:  Interview subjects verified, archival footage sourced
```

### Step 5.10 — YouTube Optimization Check

```
Check:   Title under 100 chars, includes key search term
         Description has timestamps, sources, disclaimer
         Tags cover primary + long-tail keywords
         Thumbnail concept is clear and clickable
```

### Step 5.11 — Write Audit Report

```
Action:  Compile all 70 check results
Output:  Audit_Report.md
Format:  Per-check: PASS / FAIL / WARNING
         Summary: Pass count, Fail count, Warnings
```

### Step 5.12 — Issue Completion Certificate

```
Action:  If all critical checks pass (0 failures on P0 checks)
Output:  Completion_Certificate.md
Content: Topic name, category, date, all phases confirmed,
         total files produced, scene count, duration
```

### Step 5.13 — Update PROGRESS.md

```
Action:  Mark topic as completed
File:    OUTPUT/<Category>/PROGRESS.md
Updates: Increment Topics Done for domain
         If domain complete → mark COMPLETE
         Update Last Updated date
         Add to Completed Topics table
```

### Step 5.14 — Update MASTER_REGISTRY.md

```
Action:  Mark niche as completed in registry
File:    REGISTRY/MASTER_REGISTRY.md
Update:  Add completion date to niche entry
```

### Step 5.15 — Done

```
Status:  Topic complete
Output:  28+ files ready for video production
Next:    Move to next topic in queue
```

| Mode | Behavior |
|---|---|
| [I] | Present audit results, user reviews certificate |
| [D] | Auto-audit, user reviews certificate per domain |
| [A] | Auto-audit, auto-issue certificate, update PROGRESS.md |

---

## COMPLETE FILE INVENTORY (per topic)

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
│   └── MASTER_CONTEXT_v1.md                                   (1, updated per batch in Phase 3)
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
│   ├── Master_Scene_List.md                                   (1)
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

## APPROVAL GATES SUMMARY

| Gate | Phase | What's Locked | Can Change Later? |
|---|---|---|---|
| 0 | Phase 0 | CONFIG.md (all 42 answers) | Yes — until Phase 2 |
| 1 | Phase 1 | Research Bible (facts, sources) | Yes — until Phase 2 |
| 2 | Phase 2 | **Q3, Q15, Q16, Q42** + all 16 production files | **No — locked permanently** |
| 3 | Phase 3 | Scene breakdown (batches) | Yes — but requires Phase 2 regen |
| 4 | Phase 4 | Production Package | Yes — but requires Phase 2 regen |
| 5 | Phase 5 | Audit + Certificate | Final — topic complete |

**After Phase 2 approval:** Q3 (Story Angle), Q15 (Visual Style), Q16 (Voiceover), Q42 (Scene Duration) are PERMANENT. Changing any of them requires regenerating ALL downstream phases (3, 4, 5).

---

## DECISION FLOW: WHICH MODE?

```
START
  │
  ├─ User types /mode interactive
  │   → INTERACTIVE MODE
  │   → Ask all 42 questions, one at a time
  │   → Approval gate after each phase
  │
  ├─ User types /mode domainpreset
  │   → DOMAIN PRESET MODE
  │   → Answer 42 questions once per domain
  │   → Save to DOMAIN_PRESETS.md
  │   → All topics in domain inherit defaults
  │   → Only ask if topic clearly differs
  │
  ├─ PROGRESS.md exists at startup
  │   → AUTONOMOUS MODE (resume)
  │   → Read PROGRESS.md, find next incomplete topic
  │   → Auto-answer all 42 questions
  │   → Run all 6 phases without stopping
  │   → Auto-approve all gates
  │
  └─ User asks for bulk/mass/automatic production
      → AUTONOMOUS MODE (fresh start)
      → Process full production queue
      → Track in PROGRESS.md
```

---

## DECISION FLOW: WHICH CATEGORY PRESET?

```
Niche loaded from MASTER_REGISTRY.md
  │
  ├─ Category = Business_Money
  │   ├─ Domain = Company Rise & Fall / Startups / Failed / Brand Wars / Franchise
  │   │   → CAT_BusinessStories
  │   ├─ Domain = Billionaire Stories
  │   │   → CAT_PeoplePersonalities
  │   ├─ Domain = Crypto / AI Business / E-commerce / Tech Giants / VC / Products / IPO / M&A
  │   │   → CAT_InnovationTech
  │   ├─ Domain = Corporate Scandals / Business Mysteries / Fraud / Espionage
  │   │   → CAT_ScandalsFraud
  │   ├─ Domain = Economic History / Financial Crises / Stock Market / Banking / Pharma / Energy / Trade
  │   │   → CAT_IndustryMarkets
  │   ├─ Domain = Luxury Brands / Advertising / Marketing / Fashion
  │   │   → CAT_LuxuryConsumer
  │   └─ Domain = Workplace Culture / Labor Movements / Influencer Economy
  │       → CAT_WorkplaceLabor
  │
  ├─ Category = Sanatan_Dharma
  │   → CAT_SanatanDevotional
  │
  ├─ Category = Cartoon_Animation
  │   → CAT_CartoonKids
  │
  ├─ Category = AI_Film
  │   → CAT_AIDrama
  │
  ├─ Category = Science_Future
  │   → CAT_ScienceExplainer
  │
  └─ Category = Documentary
      → CAT_ScienceExplainer
```

---

## DECISION FLOW: WHICH VISUAL STYLE?

```
Niche ID loaded
  │
  → Read MASTER_VISUAL_STYLE.md row matching Niche ID
  → Extract: Primary Visual Style, Palette, Lighting, Camera, Motion, AI Keywords
  │
  → Override Q15 (Visual Style Primary) with: Primary Visual Style
  → Override Q40 (Video Generation Method) with: Primary Visual Style
  │
  → Write to 04_Visual_Style_Guide.md + Visual_Style_Quick_Reference.md
```

---

## MODE COMPARISON TABLE

| Aspect | Interactive | Domain Preset | Autonomous |
|---|---|---|---|
| User input | All 42 questions | Once per domain | Zero |
| Speed | Slow (one topic) | Medium (domain batch) | Fast (full queue) |
| Control | Full | High (per domain) | None |
| Approval gates | Every phase | Every phase | Auto |
| Best for | Custom content, sensitive topics | Batch within one category | Bulk production |
| Typical output | 1 topic at a time | 10-20 topics per domain | 800 topics |
| Progress tracking | Manual | Per domain | PROGRESS.md auto-updated |

---

## KEY CONCEPTS

1. **Categories are templates, Topics are instances.** A CAT file defines defaults for a content style. A topic preset merges CAT defaults + sub-niche overrides + visual style into a final answer set.

2. **Phase 2 is the point of no return.** After Phase 2 approval, Q3, Q15, Q16, Q42 are locked. Changing them requires regenerating everything downstream.

3. **Scene count = Duration ÷ Scene Duration.** A 10-minute video at 8 seconds/scene = 75 scenes = 3 batches of 25.

4. **Priority chain for defaults:** Static < CAT Preset < Sub-Niche Override < Visual Style. Each layer can override the previous.

5. **Approval gates exist for a reason.** Skipping them means propagating errors downstream. In autonomous mode, internal quality checks replace user approval.

6. **The 6 phases are universal.** The same pipeline works for Business documentaries, Sanatan explainers, Cartoon scripts, AI films, and Science videos. Only the metadata and presets change.
