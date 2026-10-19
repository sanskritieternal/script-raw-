# V6 — File Usage Guide

> Every file in the system, what it contains, when to read it, when to edit it,
> and how it connects to other files. Use this as a reference while working.

---

## REGISTRY FILES (Source Data)

### MASTER_REGISTRY.md

**What it is:** The master index of all 500+ niches. One big file listing every topic
the system can produce content for.

**What it contains:** For each niche — ID, name, domain, category, sub-niche type,
visual style, tone, target audience, duration, B-roll priority, music style, key facts,
key sources, avoid warnings, and which CAT preset to use.

**When to read it:** At session startup, or when searching for a niche to produce.

**When to edit it:** When adding a new niche, updating niche metadata, or marking
a niche as completed (completion date added after Phase 5).

**Who reads it:** The agent at startup, and during Phase 0 when loading niche metadata.

**Connected to:** All phases (Phase 0 reads niche metadata from here). Also read by
`populate_niches.py` during regeneration.

---

### MASTER_VISUAL_STYLE.md

**What it is:** A table with 500 rows — one per niche ID. Each row defines the visual
direction for that niche.

**What it contains:** Niche ID, niche name, primary visual style, visual language,
color palette, lighting, camera/lens, motion style, thumbnail direction, AI prompt keywords,
and an "avoid" list.

**When to read it:** During Phase 0 (to override Q15 and Q40), Phase 2 (to write
the Visual Style Guide), and Phase 3/4 (to write AI generation prompts).

**When to edit it:** When a niche's visual direction needs to change. Changes affect
all future productions of that niche.

**Who reads it:** Phase 0 (config), Phase 2 (visual style guide), Phase 3 (scene visuals),
Phase 4 (AI prompts).

**Connected to:** CONFIG.md (Q15, Q40 overrides), 04_Visual_Style_Guide.md,
Visual_Style_Quick_Reference.md, AI prompts in Production_Package.md.

---

### Categories/CAT_*.md (11 files)

**What they are:** Reusable templates that provide Q2-Q42 answer defaults for different
content styles. One CAT file covers multiple niches that share the same content approach.

**What they contain:**
- Applies-to scope (which niches this CAT covers)
- Q2-Q42 questions with default answers
- Options lists for each question
- A description of the content style

**The 11 CAT presets:**

| File | Covers | Story Angle | Visual Style | Voiceover |
|---|---|---|---|---|
| `CAT_BusinessStories.md` | Company rise/fall, startups, franchises, brand wars | Rise/Fall Narrative | Timeline Visualization | Engaging Storytelling |
| `CAT_PeoplePersonalities.md` | Billionaire biographies, people stories | Rise/Fall Narrative | Documentary + Interview | Engaging Storytelling |
| `CAT_InnovationTech.md` | Crypto, AI, e-commerce, tech giants, VC | Innovation Focus | Animated Explainers / Data Viz | Professional Authoritative |
| `CAT_ScandalsFraud.md` | Corporate scandals, fraud, espionage | Scandal/Controversy | Documentary Realism | Documentary Calm |
| `CAT_IndustryMarkets.md` | Economic history, financial crises, markets | Economic Analysis | Data Visualization Heavy | Critical Analytical |
| `CAT_LuxuryConsumer.md` | Luxury brands, advertising, fashion | Entertainment Focus | Archive Footage + Realism | Engaging Storytelling |
| `CAT_WorkplaceLabor.md` | Workplace culture, labor movements | Economic Analysis | Documentary Realism | Documentary Calm |
| `CAT_SanatanDevotional.md` | Hindu mythology, spirituality, temples | Mythology | Sacred Cinematic Devotional | Sacred Devotional |
| `CAT_CartoonKids.md` | Kids cartoons, animated stories | Entertainment / Education | 2D/3D Animation | Engaging Storytelling |
| `CAT_AIDrama.md` | AI films, cinematic shorts | Innovation / Drama | Cinematic | Professional Authoritative |
| `CAT_ScienceExplainer.md` | Science, space, ocean, documentary | Education Focus | Data Viz + Animation | Professional Authoritative |

**When to read it:** During Phase 0 (to load Q2-Q42 defaults), Phase 1 (to understand
content style), Phase 2 (to lock creative decisions).

**When to edit it:** When you want to change defaults for an entire content style.
For example, changing Q42 in `CAT_BusinessStories.md` from FIXED 8-SECOND to VARIABLE
affects all Business topics using that preset.

**Who reads it:** Phase 0 (config), Phase 1 (research context), Phase 2 (production decisions).

**Connected to:** CONFIG.md (Q2-Q42 defaults), Phase 2 production files, Domain Presets.

---

### Topics/<Category>/ directories

**What they are:** Per-category topic folders. Each category has a folder containing
niche sub-folders, each with 15 topic-type preset files.

**Structure:**
```
Topics/Business_Money/
├── ALL_TOPICS_BY_NICHE.md          ← index of all niches in this category
├── DOMAIN_PRESETS.md               ← domain-level Q1-Q42 presets (if any)
└── <niche_slug>/
    ├── ALL_TOPICS_BY_NICHE.md      ← index of 15 sub-niche types
    ├── <NNN>_<slug>_<subtype>.md   ← 15 topic presets
    └── ...
```

**What each topic preset file contains:**
- Topic ID (niche ID + sub-niche type)
- Domain, category, visual style ID
- All 42 Q&A answers (merged from CAT preset + sub-niche overrides + visual style)
- Visual style block (palette, lighting, camera, motion, AI keywords, avoid)

**When to read it:** During Phase 0 (to load topic-specific defaults), Phase 1 (to
understand the sub-niche angle), Phase 2 (to apply sub-niche-specific rules).

**When to edit it:** When a specific topic's defaults need adjustment. Edit the single
`.md` file for that (niche × sub-niche) combination.

**Who reads it:** Phase 0 (topic defaults), populate_niches.py (regeneration).

**Connected to:** CONFIG.md (provides Q2-Q42 answers for this specific topic),
CAT_*.md (category-level defaults that feed into these files).

---

## PHASE 0 FILES

### CONFIG.md

**What it is:** The configuration document for a single topic. Contains all 42 answers
that define every aspect of the video.

**What it contains:**
- Q1: Content Category
- Q2: Target Audience
- Q3: Story Angle (LOCKED after Phase 2)
- Q4: Content Depth Level
- Q5: Visual/Media Priority
- Q6: Interview/Documentation Segments
- Q7: Content Sensitivity Level
- Q8: Legal/Accuracy Concern
- Q9: Subject Focus
- Q10: Contested Facts Included
- Q11: Expertise Level Required
- Q12: Comparative Content
- Q13: Monetization Priority
- Q14: Total Duration
- Q15: Visual Style Primary (LOCKED after Phase 2)
- Q16: Voiceover Approach (LOCKED after Phase 2)
- Q17: Delivery Format
- Q18: Primary Language (LOCKED after Phase 2)
- Q19: Additional Languages
- Q20: On-Screen Text Strategy
- Q21: Source/Research Priority
- Q22: Ending Tone
- Q23: Accuracy Priority
- Q24: Source Quality Requirements
- Q25: Update Frequency
- Q26: Platform Distribution
- Q27: Production Quality Level
- Q28: Audience Geographic Focus (LOCKED after Phase 2)
- Q29: Factual Verification Timeline
- Q30: Expert/Access
- Q31: Controversial Content Level
- Q32: Comparative/Fairness Level
- Q33: Current Events Included
- Q34: Bias Prevention Strategy
- Q35: Sponsored Content
- Q36: Monetization Revenue Model
- Q37: Series/Playlist Strategy
- Q38: SEO Keyword Priority
- Q39: Content Warning/Disclaimer Needed
- Q40: Video Generation Method
- Q41: Content Safety Level
- Q42: Scene Duration Strategy (LOCKED after Phase 2)

Each answer includes: the value, which source it came from (CAT preset, visual style,
niche metadata), and any notes.

**When to read it:** Every phase reads CONFIG.md. Phase 0 writes it. Phases 1-5 read it.

**When to edit it:** Only during Phase 0 (before Phase 2 locks apply). After Phase 2,
the locked values (Q3, Q15, Q16, Q42, Q14, Q18, Q28) cannot be changed.

**Who reads it:** All 5 downstream phases. This is the single source of truth for
every creative and technical decision.

**Connected to:** Everything. Every downstream file derives from these 42 answers.

---

## PHASE 1 FILES (Research Bible)

### Research_Summary.md

**What it is:** The executive summary of the topic. The narrative arc — how the story
begins, what happens, why it matters now.

**What it contains:**
- Story summary (2-3 paragraphs)
- Narrative arc (beginning, middle, end)
- Key findings
- Why this story matters today
- Fact density assessment

**When to read it:** Phase 2 (for context), Phase 3 (for scene narrative), Phase 4
(for master script), Phase 5 (for audit).

**When to edit it:** During Phase 1 (initial creation), or if new facts emerge that
change the narrative. Cannot be edited after Phase 2 without regenerating downstream phases.

---

### Facts_Documented.md

**What it is:** The master fact list. Every claim, date, person, company, and event
that appears in the video — with source citations.

**What it contains:**
- Fact entries organized by topic area
- Each entry: claim, source citation, confidence level
- Conflicting facts flagged with resolution notes
- People: name, role, relevance, key actions
- Companies: founding date, key products, status
- Events: date, description, impact

**When to read it:** Phase 2 (for accuracy checklist), Phase 3 (for scene facts),
Phase 4 (for script accuracy), Phase 5 (for factual accuracy audit).

**When to edit it:** During Phase 1 only. After Phase 2, changes require downstream regen.

---

### Financial_Figures_Verified.md

**What it is:** All financial numbers in the video — market caps, revenues, valuations,
stock prices, damages, investments — with exact sources.

**What it contains:**
- Figure, unit, date, source (SEC filing, annual report, press release)
- Inflation adjustment where relevant
- Methodology note (how the figure was verified)
- Conflicts between sources (with resolution)
- Scope note: Business category only

**When to read it:** Phase 2 (for financial data section), Phase 3 (for data viz scenes),
Phase 4 (for script numbers), Phase 5 (for financial accuracy audit).

**When to edit it:** During Phase 1 only. This file is skipped entirely for non-Business
categories (Sanatan, Cartoon, Science, Documentary).

---

### Timeline_Accuracy_Check.md

**What it is:** A chronological table of every event in the story, with dates and
source verification.

**What it contains:**
- Chronological event table: date, event, source, verification status
- Causal links (Event A caused Event B)
- Gaps in timeline flagged
- Contradictory dates with resolution
- Period markers (era, decade, year)

**When to read it:** Phase 3 (for scene ordering and TimeOfDay/Period fields),
Phase 4 (for script chronology), Phase 5 (for date accuracy audit).

**When to edit it:** During Phase 1 only.

---

### Source_List_with_Links.md

**What it is:** The complete bibliography. Every source used in the video, organized
by credibility tier.

**What it contains:**
- Source title, URL, type, date accessed, credibility rating
- Tier 1: Primary sources (SEC filings, original documents, court records)
- Tier 2: Verified media (major newspapers, peer-reviewed journals)
- Tier 3: General media (blogs, secondary coverage)
- Key claims each source supports
- Sources excluded and why
- Conflicting sources and resolution

**When to read it:** Phase 2 (source credibility guide), Phase 4 (source consolidation),
Phase 5 (source attribution audit).

**When to edit it:** During Phase 1 (add sources found during research), Phase 2
(refine source tiers).

---

### MASTER_CONTEXT_v1.md

**What it is:** The bridge between Phase 1 and all downstream phases. It consolidates
the most important information from Phase 1 into one document that later phases can
reference without re-reading all 6 Research Bible files.

**What it contains:**
- Summary (from Research_Summary.md)
- Key facts (from Facts_Documented.md)
- Locked decisions (from CONFIG.md Q2-Q42)
- Financial highlights (from Financial_Figures_Verified.md)
- Source summary (from Source_List_with_Links.md)

**When to read it:** Phase 2 (primary input for production decisions), Phase 3
(scene context), Phase 4 (script compilation).

**When to edit it:** Phase 1 (initial creation), Phase 3 (updated per batch with
consistency tracking — scene count progress, any deviations from locks).

**Who updates it:** Phase 1 (initial), Phase 3 (per batch).

**Connected to:** Phase 2 (reads for production context), Phase 3 (updates per batch).

---

## PHASE 2 FILES (Production Bible)

### 00_Project_Consistency_Rules.md

**What it is:** The lock file. Contains all values that become PERMANENT after Phase 2.
If any of these need to change later, ALL downstream phases must be regenerated.

**What it contains:**
- Content domain, target audience, story angle
- Accuracy bar and source quality level
- Scene duration strategy (FIXED 8-SECOND or VARIABLE)
- Content safety level
- **Locks:** Q3 (story angle), Q15 (visual style), Q16 (voiceover), Q42 (scene duration),
  Q14 (total duration), Q18 (language), Q28 (audience geo)
- Tone/mood lock
- Controversy handling rules
- Protected fields (SceneNumber, Duration, Location, Chapter, Characters, TimeOfDay/Period)
- What MUST stay identical across all scenes

**When to read it:** Phase 3 (before generating scenes — must follow locks),
Phase 4 (consistency verification), Phase 5 (consistency audit).

**When to edit it:** NEVER after Phase 2 approval. Only during Phase 2 creation.

---

### 01_Research_Sources.md

**What it is:** The consolidated, organized source list for this specific topic.
A refined version of Source_List_with_Links.md organized for production use.

**What it contains:**
- All Tier 1, 2, and 3 sources
- Each source: title, URL, date, credibility tier, key claims it supports
- Conflicting sources and how they were resolved
- Sources excluded and why

**When to read it:** Phase 3 (for scene source citations), Phase 4 (for production
package sources section), Phase 5 (for source attribution audit).

---

### 02_Financial_Data_Verified.md

**What it is:** The final verified financial figures for production.
A production-ready version of Financial_Figures_Verified.md.

**What it contains:**
- All figures cross-checked and confirmed
- Inflation-adjusted values
- Methodology notes
- Business category only — skipped for Sanatan, Cartoon, Science, Documentary

**When to read it:** Phase 3 (for data viz scenes with financial data),
Phase 4 (for script numbers).

---

### 03_Accuracy_Verification_Checklist.md

**What it is:** Category-specific accuracy rules that govern what level of verification
each type of claim needs.

**What it contains:**
- Verification rules per claim type (financial, biographical, scientific, scriptural)
- Source hierarchy (what level of source is required for what type of claim)
- Minimum source count per section
- Red flags (claims that need extra verification)
- Category-specific standards (peer-reviewed for Science, SEC filings for Business,
  scriptural for Sanatan)

**When to read it:** Phase 3 (fact-checking scenes), Phase 5 (accuracy audit).

---

### 04_Visual_Style_Guide.md

**What it is:** The definitive visual direction document. Every scene in Phase 3 must
follow these rules exactly.

**What it contains:**
- Primary visual style (from Q15 + MASTER_VISUAL_STYLE.md)
- Scene-by-scene style notes
- Color palette (hex codes if applicable)
- Lighting references
- Camera movements and angles
- Transition rules between scenes
- Thumbnail concept
- Style do's and don'ts
- AI prompt template (style keywords, palette, lighting, camera, motion, avoid list)

**When to read it:** Phase 3 (every scene must match this), Phase 4 (AI prompts),
Phase 5 (visual consistency audit).

**When to edit it:** NEVER after Phase 2 approval.

---

### 05_Voiceover_Guide.md

**What it is:** The voiceover specification. Defines who speaks, how they speak,
and what rules govern the narration.

**What it contains:**
- Voice profile (gender, age, accent if applicable)
- Pacing (words per minute)
- Tone rules per scene type (intro = engaging, data = authoritative, conclusion = inspirational)
- Language handling (English only / Hindi Devanagari / Hindi Romanised / Bilingual)
- Mixing rules (when to switch languages mid-script)
- Profanity policy
- Citation style in script ("according to..." vs. direct attribution)

**When to read it:** Phase 3 (writing scene narration), Phase 4 (compiling master script),
Phase 5 (voiceover consistency audit).

**When to edit it:** NEVER after Phase 2 approval.

---

### 06_Data_Visualization_Specs.md

**What it is:** Defines what data visualizations appear in the video and how they look.

**What it contains:**
- Chart types per data point (bar, line, pie, infographic, animated number)
- Animation style (fade in, slide, pop, build)
- Color scheme (from visual style palette)
- On-screen labels and font style
- Data sources (referencing Research Bible)
- Placement rules (where charts appear in the scene timeline)

**When to read it:** Phase 3 (writing data viz scenes), Phase 4 (production package),
Phase 5 (data viz completeness audit).

---

### 07_YouTube_Strategy.md

**What it is:** The YouTube-specific production plan. Everything needed to publish
the video effectively.

**What it contains:**
- Title (3 variants, each under 100 characters)
- Description template (with timestamps, sources, disclaimer)
- Tags (20+ keywords, mix of broad and long-tail)
- Thumbnail concept (visual description for designer)
- Playlist assignment
- Premiere timing recommendation
- Shorts clip plan (if Q26 includes Shorts)

**When to read it:** Phase 4 (production package compilation), Phase 5 (YouTube optimization audit).

---

### 08_Legal_Liability_Guide.md

**What it is:** The legal risk assessment. Flags what could go wrong and what
disclaimers are needed.

**What it contains:**
- Risk level (from Q8: Low / Moderate / High / Critical)
- Specific risk areas (defamation, copyright, financial advice, etc.)
- Required disclaimers (text finalized here)
- Review checklist
- Distribution restrictions (if any)
- High-risk flag (if Q8 = High/Critical, legal review is mandatory before publishing)

**When to read it:** Phase 3 (scene legal flags), Phase 4 (legal summary),
Phase 5 (legal compliance audit).

**When to act on it:** If High/Critical risk, pause for manual legal review before publishing.

---

### 09_Ethical_Storytelling_Guide.md

**What it is:** The fairness and representation rulebook. Ensures the video doesn't
exploit, misrepresent, or show bias.

**What it contains:**
- Representation rules (who must be represented fairly)
- Balance requirements (both sides of contested issues)
- Sensitive topic handling (layoffs, failures, victim impact)
- Disclosure requirements (sponsored content, conflicts of interest)
- Specific rules for this topic's sensitive areas

**When to read it:** Phase 3 (scene fairness), Phase 4 (ethical review section),
Phase 5 (bias/fairness audit).

---

### 10_Scene_Template.md

**What it is:** The template that every scene in Phase 3 must follow.
Defines the structure of a single scene file.

**What it contains:**
- Scene structure template (Visual + Audio + Text + Duration fields)
- Scene numbering scheme (scene-001, scene-002, etc.)
- Required fields per scene (all must be filled, no placeholders)
- Batch structure (25 scenes per batch)
- Naming convention for batch files
- Transition rules between scenes
- Music cue placement

**When to read it:** Phase 3 (every scene written using this template).

---

### 11_Dialogue_Script.md

**What it is:** The script style guide. Defines how narration is written —
perspective, tense, citation style, language mixing.

**What it contains:**
- Narration perspective (first person / third person / documentary omniscient)
- Tense rules (past tense for history, present for current events)
- Language mixing rules (how to handle EN + HI snippets in same script)
- Citation style in narration ("according to..." / "studies show..." / direct quotes)
- Profanity policy
- Character dialogue rules (if applicable)
- How to handle numbers, dates, and names in narration

**When to read it:** Phase 3 (writing scene narration), Phase 4 (compiling master script),
Phase 5 (script consistency audit).

---

### 12_Monetization_Strategy.md

**What it is:** The revenue plan. How the video makes money.

**What it contains:**
- Revenue mix (AdSense, sponsorship, affiliate, Patreon)
- Sponsor integration points (where sponsor reads appear in script)
- Affiliate placement (which products/services are linked)
- Patreon pitch angle
- Merch potential
- Sponsorship disclosure text (if Q35 = Sponsored)

**When to read it:** Phase 4 (production package monetization section),
Phase 5 (monetization compliance check).

---

### 13_Source_Credibility_Guide.md

**What it is:** The source quality rulebook. Defines what sources are acceptable
for what type of claim.

**What it contains:**
- Tier 1: Primary sources (SEC filings, original documents, peer-reviewed papers)
- Tier 2: Verified media (Reuters, BBC, major newspapers, established journals)
- Tier 3: General media (blogs, social media, unverified reports)
- Minimum tier per claim type (financial = Tier 1, background = Tier 2, etc.)
- How to handle conflicting sources
- Wikipedia policy (never as primary, acceptable for background only)

**When to read it:** Phase 3 (scene source verification), Phase 5 (source quality audit).

---

### 14_Bias_Prevention_Checklist.md

**What it is:** The fairness checklist. Specific checks for this topic's bias risks.

**What it contains:**
- 5-7 specific bias checks tailored to this topic
- E.g., for scandals: "Does the video acknowledge the company's successes?"
- E.g., for biographies: "Does the video acknowledge the subject's failures?"
- E.g., for comparisons: "Is the comparison fair (same time period, same metrics)?"
- Representation check (are all relevant perspectives included?)
- One-sided narrative check

**When to read it:** Phase 5 (bias/fairness audit — 10th audit category).

---

### 15_Project_Summary.md

**What it is:** One-page summary of every Phase 2 decision. The quick reference
for anyone who needs to understand the project without reading all 16 files.

**What it contains:**
- All locked values (Q3, Q15, Q16, Q42, etc.)
- Key creative decisions (why each was chosen)
- Production specs summary
- Risk flags (legal, accuracy, bias)
- File inventory
- Next steps

**When to read it:** Phase 4 (production package compilation), Phase 5 (audit overview).

---

## PHASE 3 FILES (Scene Breakdown)

### Batch_NN_Scenes_XX_to_YY.md

**What it is:** A batch of 25 scenes. Each scene is a timed, scripted, visually-directed
unit ready for video production.

**What each scene contains:**
- Scene Number (sequential, no gaps)
- Duration (8 seconds default, or variable per Q42)
- Chapter (from story angle Q3)
- TimeOfDay / Period (from timeline)
- Location
- Characters present
- Visual description (from Q15 visual style guide)
- Narration text (from Q16 voiceover style)
- On-screen text / graphics (from Q20)
- Data visualization (from Q5)
- Music / sound note
- AI generation prompt (for video generation tool)
- Source citation (if fact is stated)

**Naming convention:** `Batch_01_Scenes_001-025.md`, `Batch_02_Scenes_026-050.md`, etc.

**When to read it:** Phase 4 (compiling all scenes into Production Package).

**When to edit it:** Phase 3 only. After Phase 2 approval, scene structure is locked
but scene content can be refined until Phase 3 approval.

---

### MASTER_CONTEXT_v1.md (updated)

**What it is:** The Phase 1 bridge file, updated per batch in Phase 3.

**What gets added per batch:**
- Scene count progress (scenes written / total scenes)
- Consistency notes (any deviations from Phase 2 locks)
- New facts discovered during scene writing
- Source additions found during scene research

**When to read it:** Phase 4 (final context for production package).

---

### VOICE_SCRIPT_<lang>.md

**What it is:** The narration script translated/adapted for each additional language
(from Q19: Additional Languages).

**What it contains:**
- Full narration text in the additional language
- Same scene structure and timing as the original
- Language-specific notes (pronunciation, cultural adaptation)

**When it's generated:** Only if Q19 ≠ "None".

**When to read it:** Phase 4 (production package), voice recording stage.

---

## PHASE 4 FILES (Production Package)

### Production_Package.md

**What it is:** The single master file containing everything needed to produce the video.
This is the final output that a video editor or AI tool uses.

**What it contains (in order):**

1. **All Scenes** — merged from all batch files, in sequence
2. **Master Script** — full narration text, timed to scene durations
3. **All Sources** — consolidated from Research Bible + production files
4. **YouTube Metadata** — title (3 variants), description, tags, thumbnail concept
5. **Legal Review Summary** — risk level, disclaimers, review status
6. **AI Generation Prompts** — per-scene prompts for video generation tools
7. **Final Production Checklist** — all 70 audit points pre-checked

**When to read it:** Phase 5 (audit), and then by the video production team.

**When to edit it:** Phase 4 only (during compilation). After Phase 4 approval,
only Phase 5 audit can flag issues.

---

## PHASE 5 FILES (Final Audit)

### Audit_Report.md

**What it is:** The 70-point quality check results.

**What it contains:**
- Per-check result: PASS / FAIL / WARNING
- Check reference code (e.g., F1 for factual accuracy, L3 for legal)
- Failure details (file, line, explanation, required fix)
- Summary: Pass count, Fail count, Warnings count
- Verdict: PUBLISH-READY or REQUIRES FIXES

**When to read it:** After Phase 5, before publishing.

**When to act on it:** Any FAIL must be fixed before publishing. Warnings are advisory.

---

### Completion_Certificate.md

**What it is:** The official completion document. Marks the topic as done.

**What it contains:**
- Topic name, category, project folder path
- Auditor name, audit date
- Total checklist items (70), verdict
- Summary of all phases confirmed
- Total files produced, scene count, duration
- Auditor signature

**When to read it:** After Phase 5, to confirm the topic is complete.

**When to edit it:** Never. This is generated, not edited.

---

## PROGRESS TRACKING FILES

### OUTPUT/<Category>/PROGRESS.md

**What it is:** The per-category production tracker.

**What it contains:**
- Progress summary (total topics, completed, in progress, pending, failed)
- Domain status table (40 domains × 20 topics each)
- Completed topics table (domain, topic number, title, completion date)

**When to read it:** Session startup (to resume where you left off), after each
completed topic (to update progress).

**When to edit it:** After every Phase 5 completion. Increment Topics Done for the domain.
If all topics in a domain are done, mark domain as COMPLETE.

**Who uses it:** Autonomous mode reads it to find the next incomplete topic.
User reads it to see overall progress.

---

## CONFIGURATION FILES (CORE/PIPELINE)

### MASTER_Phase0_Config.md

**What it is:** The 42-question definition file. Contains the questions, options,
and rules for Phase 0.

**What it contains:**
- All 42 questions with full text and options
- Mode behavior (interactive vs. autonomous)
- CONFIG.md template
- Category preset lookup table
- Visual style integration rules
- Domain default config answers
- Language mode handling (EN, HI_DEV, HI_ROM, BILINGUAL)

**When to read it:** Phase 0 (to know what questions to ask/answer).

**When to edit it:** When adding/modifying questions, changing options, or adjusting
domain defaults.

---

### MASTER_Phase1_ResearchBible.md

**What it is:** The research phase master. Contains rules, methodology, and templates
for all 6 Phase 1 output files.

**What it contains:**
- Research rules (6 rules: sources, financials, dates, defamation, fairness, speculation)
- 6 file templates (one per output file)
- Research methodology (source hierarchy, verification protocol)
- Financial verification protocol
- Timeline accuracy rules
- Legal liability assessment framework
- Bias detection guidelines
- Research safety gate (checklist before Phase 2)

**When to read it:** Phase 1 (to know how to produce each research file).

**When to edit it:** When research methodology changes, or when adding/removing output files.

---

### MASTER_Phase2_ProductionBible.md

**What it is:** The production phase master. Contains rules, templates, and specifications
for all 16 Phase 2 output files.

**What it contains:**
- 13 production rules (accuracy, data viz, voiceover, YouTube, legal, etc.)
- 16 file templates (one per output file)
- Scene template
- Timing specifications and audio block mapping
- Visual styles catalog (13 categories)
- YouTube optimization rules
- Voiceover rules
- Data visualization guidelines
- Thumbnail design specs
- AI safety rules
- Production bible locks (what's permanent after Phase 2)
- Quality gate checklist (before Phase 3)

**When to read it:** Phase 2 (to know how to produce each production file).

**When to edit it:** When production standards change, or when adding/removing output files.

---

### MASTER_Phase3_SceneBreakdown.md

**What it is:** The scene breakdown master. Contains rules, templates, and specifications
for Phase 3.

**What it contains:**
- Scene count formula and batch table
- Batch processing rules (25 scenes per batch)
- Scene template (every field a scene must have)
- Production Safeguards Checklist (run before each batch)
- Scene writing guidelines per category
- Interactive mode dialogue (what to say to user)
- Autonomous mode rules
- MASTER_CONTEXT update rules
- VOICE_SCRIPT generation rules

**When to read it:** Phase 3 (to know how to write scenes and run batches).

**When to edit it:** When batch sizes change, scene template changes, or batch rules change.

---

### MASTER_Phase4_ProductionPackage.md

**What it is:** The production package master. Defines the structure and content
of the final Production_Package.md.

**What it contains:**
- Required sections (in order)
- Section specifications (what each section must contain)
- Compilation rules (how to merge scenes, scripts, sources)
- Quality checklist before writing the package

**When to read it:** Phase 4 (to know how to compile everything into one file).

**When to edit it:** When the production package structure changes.

---

### MASTER_Phase5_FinalAudit.md

**What it is:** The audit master. Contains the 70-point checklist, audit rules,
and Completion Certificate template.

**What it contains:**
- 70 audit items organized into 10 categories
- Per-item: what to check, how to check, max failures allowed
- Audit rules (one auditor, any FAIL = STOP, fix and re-audit)
- Completion Certificate template
- Auditor signature block

**When to read it:** Phase 5 (to run the audit).

**When to edit it:** When audit criteria change, or when adding/removing checklist items.

---

## RULE FILES (CORE/RULES)

### CLAUDE.md

**What it is:** The system entrypoint. Auto-loaded every session. Tells the agent
what the V6 system is, how it works, and what rules to follow.

**What it contains:**
- Directory structure
- Startup sequence (what to read first)
- The 6-phase pipeline overview
- Output location rules
- Mode rules (Interactive, Domain Preset, Autonomous)
- Slash commands
- 9 critical rules (accuracy, legal, sources, no placeholders, fairness, etc.)

**When to read it:** Every session startup (auto-loaded).

**When to edit it:** When system architecture changes, or when core rules change.

---

### agents.md

**What it is:** The orchestrator. Defines the agent's role, what files to read at
startup, and the detailed behavior for each phase in each mode.

**What it contains:**
- Agent definition and purpose
- Mode directive (how to determine mode)
- Files to read at startup
- Output folder structure
- Niche metadata format
- Detailed phase instructions for each mode
- Category mapping (which CAT preset for which domain)
- Critical rules

**When to read it:** Every session startup.

**When to edit it:** When agent behavior, phase instructions, or category mapping changes.

---

### autonomous.md

**What it is:** The autonomous mode tuning manual. The spec sheet for how the agent
behaves when running without user input.

**What it contains:**
- How to activate autonomous mode
- Domain-level preset mode (hybrid between interactive and autonomous)
- Core loop (exact steps the agent follows for each topic)
- Config auto-answer rules (Q1-Q42 default values per domain)
- Domain → category mapping table (40 domains)
- Domain category presets (Q2-Q42 defaults per content style)
- Locks (what's permanent after Phase 2)
- Batch sizes and file counts
- Progress tracking rules
- Session control (start, end, resume, interrupted topic recovery)
- Folder structure

**When to read it:** When running in autonomous mode, or when tuning autonomous behavior.

**When to edit it:** When domain mappings change, default answers change, batch sizes change,
or autonomous behavior rules change.

---

### INVOKE_COMMANDS.md

**What it is:** The slash command reference. All commands the AI understands.

**What it contains:**
- Navigation commands (/list_categories, /list_niches, /search_niche, /pick_niche)
- Phase runners (/run_phase0 through /run_phase5, /run_all)
- File operations (/view, /edit, /approve, /reject, /skip)
- Registry operations (/add_niche, /edit_niche, /load_preset, /save_preset)
- Batch manager (/batch_start, /batch_view, /batch_edit, /batch_approve, /batch_resize)
- Autonomous loop (/start_autonomous, /pause, /resume, /stop, /sync)
- Usage examples for each command

**When to read it:** When using slash commands, or when adding new commands.

**When to edit it:** When adding/removing commands, or changing command parameters.

---

## PYTHON SCRIPTS

### populate_niches.py

**What it does:** The master generator. Reads MASTER_REGISTRY.md, MASTER_VISUAL_STYLE.md,
and CAT_*.md files, then generates all topic preset files in Topics/<Category>/.

**What it produces:**
- 7,500 topic preset files (500 niches × 15 sub-niche types)
- 500 ALL_TOPICS_BY_NICHE.md index files
- Total: 8,000 files across 6 category folders

**When to run it:** After editing MASTER_REGISTRY.md, MASTER_VISUAL_STYLE.md, or
any CAT_*.md file. Regenerates all topic presets to reflect changes.

**What it reads:**
- `REGISTRY/MASTER_REGISTRY.md` — niche list and metadata
- `REGISTRY/MASTER_VISUAL_STYLE.md` — visual style per niche ID
- `REGISTRY/Categories/CAT_*.md` — category presets
- `CORE/PIPELINE/01_Phase0_Configuration/MASTER_Phase0_Config.md` — 42 questions

**Priority chain in generation:** Static defaults < CAT preset < Sub-niche type < Visual style.

**When to edit it:** When the topic folder structure changes, when adding new sub-niche
types, or when changing how topic presets are generated.

---

### generate_niche_files.py

**What it does:** Generates individual niche metadata files.

**When to run it:** When creating new niche entries.

---

## FLOW_STEPS.md

**What it is:** The step-by-step pipeline reference. Documents every step across all
6 phases, with mode-specific behavior for each step.

**What it contains:**
- Mode legend ([I]nteractive, [D]omain Preset, [A]utonomous)
- 15 steps per phase (Phase 0 through Phase 5)
- Sub-niche override table
- Scene count formula and batch table
- Complete file inventory per topic
- 5 approval gates with lock rules
- Decision flowcharts (mode selection, category preset selection, visual style)
- Mode comparison table

**When to read it:** When you need to understand what happens at a specific step,
or when debugging why something happened the way it did.

**When to edit it:** When pipeline steps change, when adding/removing phases,
or when mode behavior changes.

---

## HOW IT WORKS.md

**What it is:** The big-picture overview. Explains the entire system for someone
new to the project.

**What it contains:**
- The 6 phases and what each does
- The 3 operating modes and when to use each
- How files connect (data flow diagram)
- Approval gates table
- Category and preset mapping
- Scene duration and batching
- What happens at the end (delivery)

**When to read it:** First file to read when learning the system. Or when you need
to explain the system to someone else.

**When to edit it:** When the overall system architecture changes.
