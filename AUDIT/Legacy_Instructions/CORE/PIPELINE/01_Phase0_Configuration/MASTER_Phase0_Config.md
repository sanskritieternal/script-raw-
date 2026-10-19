---
name: v6-phase0-configuration
description: Universal configuration engine for the V6 Content Factory. Presents 42 content-agnostic configuration questions (Q1-Q42) for any niche across 500+ niches and 6 categories. Supports Interactive, Domain Preset, and Autonomous modes. Generates a CONFIG.md per topic that feeds the full 6-phase pipeline.
version: 2.0 — Phase Split (Phase0_Configuration)
---

# MASTER V6 PHASE 0 — CONFIGURATION ENGINE

This file is the universal configuration engine for the V6 Content Factory. It contains: 42 content-agnostic configuration questions (Q1-Q42), CONFIG.md template, per-category defaults, language mode handling (English/Hindi Devanagari/Hindi Romanised), and visual style integration.

**Schema warning:** Existing category and generated topic presets do not consistently use the same meanings as this master for Q4–Q8 and Q21. Do not merge those fields by Q number until the presets are migrated. Q42 is the scene duration strategy used by Phase 3. See `AUDIT/CONFIGURATION_WIRING.md` for the canonical handoff and migration rule.

For agent orchestration, read `CORE/RULES/CLAUDE.md` and `CORE/RULES/agents.md`. For autonomous defaults, read `CORE/RULES/autonomous.md`. For niche metadata, read `REGISTRY/MASTER_REGISTRY.md`. For visual styles, read `REGISTRY/MASTER_VISUAL_STYLE.md`.

---

## TABLE OF CONTENTS

1. [How to Use This File](#how-to-use-this-file)
2. [Mode Behavior](#mode-behavior)
3. [The 42 Configuration Questions (Q1-Q42)](#the-42-configuration-questions-q1q42)
4. [Language Mode (Q18-Q19)](#language-mode-q18-q19)
5. [CONFIG.md Template](#configmd-template)
6. [Category Preset Lookup](#category-preset-lookup)
7. [Visual Style Integration](#visual-style-integration)
8. [Domain Default Config Answers](#domain-default-config-answers)
9. [Folder Structure](#folder-structure)

---

## HOW TO USE THIS FILE

**Three modes:**
- **Interactive** → ask all 42 questions (with 3-language options), write CONFIG.md
- **Domain Preset** → load the relevant `CAT_<X>.md` preset, confirm with user, write CONFIG.md
- **Autonomous** → auto-answer using `autonomous.md`, write CONFIG.md without user input

**Required inputs:**
- `CATEGORY` — one of the 10 category presets in `REGISTRY/Categories/`
- `NICHE_ID` — numeric ID (1-500) from `REGISTRY/MASTER_REGISTRY.md`
- `NICHE_NAME` — topic label (e.g. "Kodak")
- `LANGUAGE` — `EN` / `HI_DEV` / `HI_ROM` / `BILINGUAL`

**Output:** a complete `CONFIG.md` at `OUTPUT/<Category>/Topics/<NN>_<NicheName>/01_Phase0_CONFIG/CONFIG.md`

### How to Use This System

Start with the agent orchestration files (`agents.md` / `CLAUDE.md`) for full operating instructions. This file provides the configuration layer.

In **interactive mode**, ask the user the 42 configuration questions below. Present a recommended answer for each question based on the selected content category (Q1). In **autonomous mode**, auto-answer all questions using `autonomous.md` and write the CONFIG.md directly.

### Invoke Command Reference (10 Category Presets + 490 Niche Families)

```
/invoke sanatan-devotional    → CAT_SanatanDevotional
/invoke cartoon-kids          → CAT_CartoonKids
/invoke ai-drama              → CAT_AIDrama
/invoke business-stories      → CAT_BusinessStories
/invoke people-personalities  → CAT_PeoplePersonalities
/invoke innovation-tech       → CAT_InnovationTech
/invoke scandals-fraud        → CAT_ScandalsFraud
/invoke industry-markets      → CAT_IndustryMarkets
/invoke luxury-consumer       → CAT_LuxuryConsumer
/invoke workplace-labor       → CAT_WorkplaceLabor

+ 490 more via CAT_\<NicheID\>_\<Slug\> in REGISTRY/Categories/
```

Each invoke auto-detects the matching category preset from `REGISTRY/Categories/CAT_<X>.md`, loads the 42 Q answers, loads the visual style from `REGISTRY/MASTER_VISUAL_STYLE.md` row matching `NICHE_ID`, and creates:

```
OUTPUT/<Category>/Topics/<NN>_<Slug>/01_Phase0_CONFIG/CONFIG.md
```

**Custom Invoke:**

```
/invoke [CUSTOM_TOPIC]
→ Creates project folder with custom name
→ Asks: content type (Narrative / Educational / Investigation / Entertainment)
→ Smart-matches to nearest category preset in REGISTRY/Categories/
→ User confirms recommendations or customizes
→ Proceeds to Phase 0 CONFIG
```

---
---


## 5-PHASE WORKFLOW OVERVIEW

```
PHASE 0: CONFIGURATION
  ↓
PHASE 1: RESEARCH BIBLE      ← User approval gate (interactive)
  ↓
PHASE 2: PRODUCTION BIBLE    ← User approval gate (interactive)
  ↓
PHASE 3: SCENE BREAKDOWN     ← Batch 1 interactive approval, then 25 scenes per batch autonomously
  ↓
PHASE 4: PRODUCTION PACKAGE  ← User approval gate (interactive)
  ↓
PHASE 5: FINAL AUDIT         ← 70-point accuracy audit (language, visuals, legal, consistency)
  ↓
DONE → Ready for video generation / publishing
```

### Autonomy Modes

**Mode 1: FULL AUTONOMOUS**
- Best for: Quick turnaround, high-volume content, non-controversial topics
- Time to publishable: 15-30 minutes per topic
- NOT allowed for: High-legal-risk topics (Q8 = High/Critical)

**Mode 2: BALANCED** (RECOMMENDED)
- Phase 0: User answers 42 questions (or auto-answered)
- Phase 1: AI generates research; user reviews for accuracy
- Phase 2: AI generates production bible; user verifies data, sources, legal compliance
- Phase 3: AI generates scenes; user customizes narrative, visuals, tone
- Phase 4-5: AI compiles; user verifies final accuracy
- Time to scene creation: 1-2 hours per topic

**Mode 3: FULL CONTROL**
- All phases user-driven with complete ownership
- Required for: Deep investigations, sensitive topics, premium content
- Time to scene creation: 4-8 hours per topic

---

## CORE PHILOSOPHY & PRINCIPLES

### Highest Priority Rules

Priority order (always follow this):

1. **Factual Accuracy** - All facts, dates, figures must be VERIFIED
2. **Legal Protection** - No defamation, libel, or legal exposure
3. **Source Verification** - Credible sources only, proper attribution
4. **Fair Representation** - No unfair bias; balanced perspectives
5. **Transparency** - Disclose conflicts, sponsorships, affiliations
6. **Context & Nuance** - Complex topics need proper context; avoid oversimplification
7. **Ethical Storytelling** - Respect subjects; do not exploit suffering for entertainment
8. **Narrative Clarity** - Engaging AND accurate (not opposing)
9. **Data Integrity** - Charts/graphics accurately represent data
10. **Language Fidelity** - Hindi (Devanagari), Hindi (Romanised), and English must be factually identical

**Conflict Resolution:** If priorities conflict, preserve in order: factual accuracy > legal protection > source verification > fair representation > transparency > context > ethics > clarity > data integrity > language fidelity.

### Core Philosophy Statement

Regenerated content is powerful. It educates audiences across languages and formats. But with reach comes responsibility: facts matter, sources must be verified, and false claims have consequences across all language versions.

Great regenerated content is not translation-by-algorithm. It is culturally adapted stories across Hindi (Devanagari), Hindi (Romanised), and English that are factually identical, contextually appropriate, and linguistically natural in each language.

---
## CONTENT CATEGORY CATALOG (12 CATEGORIES + 500+ NICHES)

Each category maps to a preset file in `REGISTRY/Categories/`. Full niche list with IDs is in `REGISTRY/MASTER_REGISTRY.md`. Use `/invoke [category]` or `/invoke [niche-id]_[slug]` to auto-load the preset.

### CATEGORY 1: COMPANY STORIES (CAT_CompanyStories)
Organization narratives, rise-and-fall sagas, turnaround stories.
**Example niches:** Kodak, Nokia, Blockbuster, Uber, Airbnb, Tesla, Apple turnaround, WeWork
**Invoke:** `/invoke company-stories` · `/invoke 001_kodak`
**AI Recommends:** Timeline Visualization + Documentary Realism

### CATEGORY 2: PEOPLE & PERSONALITIES (CAT_PeoplePersonalities)
Founder journeys, celebrity profiles, influential individuals, leadership analysis.
**Example niches:** Elon Musk, Jeff Bezos, Steve Jobs, Ratan Tata, Oprah Winfrey, Mukesh Ambani
**Invoke:** `/invoke people-personalities` · `/invoke 002_elon-musk`
**AI Recommends:** Documentary + Interview Hybrid

### CATEGORY 3: SCANDALS & FRAUD (CAT_ScandalsFraud)
Corporate crime, fraud investigations, ethical breaches, legal controversies.
**Example niches:** Enron, Wirecard, Theranos, FTX, 2008 Financial Crisis, Madoff
**Invoke:** `/invoke scandals-fraud` · `/invoke 006_enron`
**AI Recommends:** Documentary Realism
**⚠ CRITICAL:** Factual accuracy essential; legal review mandatory for High-risk topics.

### CATEGORY 4: INDUSTRY & MARKETS (CAT_IndustryMarkets)
Economic trends, industry evolution, market analysis, sector deep dives.
**Example niches:** Indian IT Industry, Global EV Market, Retail Disruption, Supply Chain, Real Estate
**Invoke:** `/invoke industry-markets` · `/invoke 012_indian-it-industry`
**AI Recommends:** Data Visualization Heavy + Infographics

### CATEGORY 5: INNOVATION & TECH (CAT_InnovationTech)
Technology history, scientific breakthroughs, invention stories, digital transformation.
**Example niches:** AI Revolution, Cryptocurrency, E-Commerce, Venture Capital, IPO Stories, Product Failures
**Invoke:** `/invoke innovation-tech` · `/invoke 017_cryptocurrency`
**AI Recommends:** Animated Explainers or Data Visualization Heavy

### CATEGORY 6: LUXURY & CONSUMER (CAT_LuxuryConsumer)
Luxury brands, consumer behavior, advertising, fashion, lifestyle evolution.
**Example niches:** LVMH History, Gucci Brand Evolution, Fast Fashion, Marketing Psychology, Advertising History
**Invoke:** `/invoke luxury-consumer` · `/invoke 009_lvmh`
**AI Recommends:** Archive Footage + Documentary Realism

### CATEGORY 7: WORKPLACE & LABOR (CAT_WorkplaceLabor)
Work culture, labor movements, employment trends, creator economy, HR evolution.
**Example niches:** Remote Work Evolution, Labor Unions, Creator Economy, Toxic Workplace Culture, Gig Economy
**Invoke:** `/invoke workplace-labor` · `/invoke 025_remote-work`
**AI Recommends:** Documentary Realism

### CATEGORY 8: MARKETS & CRISES (CAT_MarketsCrises)
Financial crises, market crashes, economic disasters, systemic risk analysis.
**Example niches:** 2008 Crisis, 1929 Depression, Dot-com Bubble, GameStop, Black Monday, Flash Crash
**Invoke:** `/invoke markets-crises` · `/invoke 029_2008-crisis`
**AI Recommends:** Data Visualization Heavy + Timeline

### CATEGORY 9: FINANCIAL SYSTEMS (CAT_FinancialSystems)
Banking, insurance, pharma, automotive, entertainment business, corporate fraud deep dives.
**Example niches:** Federal Reserve History, Pharmaceutical Pricing, EV Revolution, Netflix Business Model, Insurance Industry
**Invoke:** `/invoke financial-systems` · `/invoke 035_banking-history`
**AI Recommends:** Data Visualization + Documentary

### CATEGORY 10: SANATAN & DEVOTIONAL (CAT_SanatanDevotional)
Hindu dharma, vedic knowledge, spiritual biographies, temple histories, philosophical teachings.
**Example niches:** Mahabharata Stories, Shiva Puran, Ramayana, Guru Nanak, Vedanta Philosophy, Temple Architecture
**Invoke:** `/invoke sanatan-devotional` · `/invoke sanatan-001`
**AI Recommends:** Animated Epic + Sacred Aesthetic

### CATEGORY 11: CARTOON & KIDS (CAT_CartoonKids)
Animated stories, educational kids content, cartoon character histories, nursery rhymes with stories.
**Example niches:** Tom & Jerry History, Disney Animation Evolution, Cartoon Network Classics, Kids Science Stories
**Invoke:** `/invoke cartoon-kids` · `/invoke kids-001`
**AI Recommends:** 2D Animation + Bright Minimalist

### CATEGORY 12: AI DRAMA (CAT_AIDrama)
AI-generated dramatic narratives, sci-fi stories, futuristic scenarios, tech-thriller content.
**Example niches:** AI Consciousness Stories, Future City Dramas, Robot Uprising Narratives, Time Travel Dramas
**Invoke:** `/invoke ai-drama` · `/invoke ai-drama-001`
**AI Recommends:** AI Video (Veo3/Seedance) + Cinematic Lighting

## THE 42 CONFIGURATION QUESTIONS (Q1–Q42)

All 42 questions must be answered before writing begins. In interactive mode, present them in groups of 4-5. In autonomous mode, auto-answer using `autonomous.md` § 3.2.

**Multi-select questions:** Questions marked with **(multi-select)** allow more than one answer. Record them as comma-separated values in `CONFIG.md` (e.g., `Documentary Realism, Animated Explainers`).

### Content Configuration Questions (Q1–Q42)

These questions are answered automatically by AI when a category preset is loaded, or manually by the user for custom content. Each answer directly maps to a config rule — see Rules Section above.

#### Core Questions (Q1–Q12)

**Q1: Content Category?**
- Company Stories (organization narratives, rise/fall sagas)
- People & Personalities (biographies, celebrity profiles)
- Scandals & Fraud (investigations, corporate crime)
- Industry & Markets (economic trends, sector analysis)
- Innovation & Tech (technology history, scientific breakthroughs)
- Luxury & Consumer (brands, consumer behavior, fashion)
- Workplace & Labor (culture, labor movements, creator economy)
- Markets & Crises (financial crises, market crashes)
- Financial Systems (banking, insurance, pharma, automotive)
- Sanatan & Devotional (Hindu dharma, spiritual stories, temple history)
- Cartoon & Kids (animated stories, educational kids content)
- AI Drama (sci-fi narratives, futuristic scenarios, tech-thriller)
- AI maps category to the matching preset in `REGISTRY/Categories/`.

**Q2: Target Audience?**
- General Public (casual viewers)
- Students & Learners (educational, academic)
- Enthusiasts (hobbyists, fans of the subject)
- Professionals (industry knowledge)
- Investors & Business Leaders (financial/strategic focus)
- Spiritual Seekers (for devotional content)
- Children & Families (for kids/cartoon content)
- AI Recommends based on category + topic selection

**Q3: Primary Story Angle?**
- Biographical Profile (focus on one person's journey)
- Investigative Narrative (factual investigation, uncover truth)
- Documentary Style (journalistic, on-location realism)
- Historical Narrative (chronological, context-driven)
- Educational Explainer (concept clarity, teach)
- Dramatic Storytelling (tension, emotional arcs)
- Data-Driven Analysis (numbers, charts, trends)
- Cultural Exploration (meaning, symbolism, tradition)
- Light Entertainment (fun, accessible, shareable)
- AI Recommends voiceover tone + visual style

**Q4: Content Depth Level?**
- Simple (accessible to all, minimal jargon)
- Moderate (some specifics, general education)
- Deep Analysis (detailed, nuanced, sourced)
- Expert-Level (advanced, assumes background knowledge)
- AI Note: "Higher depth = more credible with experts, narrower audience"

**Q5: Visual/Media Priority?**
- Heavy (charts, data viz, graphics dominate 40%+)
- Moderate (balanced 20-30%)
- Light (minimal graphics, storytelling focus)
- None (pure voiceover + archival footage)
- AI Recommends based on category preset + story angle

**Q6: Interview/Documentation Segments?**
- Include Interviews (talking heads, expert views, real voices)
- Quotes Only (text/super of expert opinions)
- Archival Footage (documentary clips, historical footage)
- No Interviews (pure narration)
- AI Note: "Interviews add credibility but require access; archival adds authenticity"

**Q7: Content Sensitivity Level?**
- Low (safe, positive, non-controversial)
- Moderate (acknowledges complexity, balanced)
- High (controversial claims, sensitive topics)
- Critical (defamation risk, legal review MANDATORY)
- AI Triggers: "High sensitivity → trigger content warnings; legal review before publishing"

**Q8: Legal/Accuracy Concern?**
- Low (historical, well-documented, no living targets)
- Moderate (some debated claims, but defensible)
- High (specific accusations about organizations/people)
- Critical (active legal risk, ongoing litigation)
- AI Triggers: "High concern → Legal review + source documentation required"

**Q9: Subject Focus?**
- Character-Driven (focus on person, their journey)
- Topic-Driven (focus on subject matter, systems)
- Balanced (both person and context)
- Concept-Driven (focus on idea, innovation, theory)
- AI Recommends: "Character-driven = more engaging; topic-driven = more educational"

**Q10: Contested Facts Included?**
- No contested claims
- Some debated facts (acknowledge debate)
- Multiple perspectives presented
- Major contested claims (significant disagreement)
- AI Requires: "Contested content = cite sources, present all sides fairly"

**Q11: Expertise Level Required?**
- General knowledge (explainable to anyone)
- Some background (basics assumed)
- Significant expertise (industry/domain knowledge)
- Highly specialized (expert-only)
- AI Recommends: "Simpler = wider audience; expert = niche credibility"

**Q12: Comparative Content?**
- No comparisons (single subject)
- One reference/context
- Multiple subjects compared
- Ranking/competition narrative
- AI Note: "Comparisons = potential bias; must be fair and transparent"

#### Production Specifications (Q13–Q20)

**Q13: Monetization Priority?**
- Not important (educational/artistic focus)
- Secondary (nice to monetize, not critical)
- Important (need revenue)
- Critical (channel depends on this)
- AI Provides: "Category affects monetization; devotional/kids content has different revenue patterns"

**Q14: Total Duration?**
- Short: 5-8 minutes (key story)
- Medium: 8-12 minutes (balanced)
- Long: 12-15 minutes (detailed narrative)
- Very Long: 15-25+ minutes (deep investigation/encyclopedia)
- AI Recommends: "Longer = more depth possible; shorter = higher engagement"

**Q15: Visual Style Primary?** *(multi-select)*
- Stock Footage + Graphics (professional aesthetic)
- Data Visualization Heavy (charts, graphs dominant)
- Archive Footage (historical, old footage)
- Documentary Realism (interviews, on-location)
- Animated Explainers (simple animations teaching)
- Timeline Visualization (evolution/chronology)
- Infographics + Text Overlay (educational, clean)
- Documentary + Interview Hybrid
- 2D Animation (stylized, narrative)
- Sacred/Epic Aesthetic (devotional: mandalas, temples)
- Bright Minimalist (kids: colorful, clean shapes)
- Cinematic/Glitch (AI drama: futuristic, dramatic)
- AI Recommends based on category preset

**Q16: Voiceover Approach?**
- Professional Authoritative (expert, knowledgeable)
- Engaging Storytelling (narrative tension, emotional arcs)
- Documentary Calm (investigation, journalistic)
- Enthusiastic Energetic (innovation, success stories)
- Reflective Spiritual (devotional, philosophical)
- Playful Animated (kids, cartoon tone)
- Dramatic Suspenseful (AI drama, thriller)
- Critical Analytical (data-heavy analysis)
- AI Recommends: "Tone must match story angle + category"

**Q17: Delivery Format?**
- Single video (one complete story)
- Series (episodic, 3-5 videos)
- Season format (10+ videos)
- Documentary series (deep investigation)
- AI Recommends: "Series favors algorithm; binge-worthy categories benefit most"

**Q18: Primary Language?**
- English
- Hindi (Devanagari)
- Hindi (Romanised)
- Bilingual (specify pair)
- Other (specify)
- If multilingual: generate `VOICE_SCRIPT_<lang>.md` files at end of Phase 3. Scene breakdown keeps English labels for cross-reference.

**Q19: Additional Languages?**
- None
- One secondary language
- Multiple languages (list all)
- If not None: generate `VOICE_SCRIPT_<lang>.md` at Phase 3 end. Speaker labels localized per target language.

**Q20: On-Screen Text Strategy?**
- Minimal (voiceover + visuals)
- Moderate (key facts, names, dates)
- Heavy (quotes, data, statistics, subtitles)
- Accessibility-focused (captions + graphics)
- AI Note: "More text = slower pacing but higher information density"

#### Content Specifics (Q21–Q25)

**Q21: Graphics Requirement?**
- Essential (complex topics, need visual explanation)
- Important (supports narrative)
- Secondary (nice to have)
- Minimal (voiceover + footage)
- AI Recommends per category preset + complexity

**Q22: Ending Tone?**
- Inspiring/Motivational (uplifting conclusion)
- Reflective/Thoughtful (leaves viewer thinking)
- Cautionary (lessons, warnings)
- Celebratory (achievement, success)
- Unresolved/Mysterious (questions remaining)
- Forward-looking (implications for future)
- Spiritual/Devotional (blessing, teaching, mantra)
- AI Note: "Endings affect viewer takeaway and shareability"

**Q23: Accuracy Priority?**
- General audience (can simplify, explain basics)
- Practitioners watching (accuracy critical)
- Mixed audience (balance clarity + accuracy)
- Expert-focused (assume knowledge)
- AI Recommends: "Higher accuracy = more credible; lower = wider reach"

**Q24: Source Quality Requirements?**
- Standard (reputable sources OK)
- High (academic/peer-reviewed preferred)
- Critical (primary documents, official records)
- Academic (scholarly sources only)
- AI Note: "Higher quality = more credible, harder to source; required for High-risk categories"

**Q25: Update Frequency?**
- One-off videos
- Weekly releases
- Bi-weekly
- Monthly
- As-needed (when story breaks)
- AI Recommends: "Consistent schedule favors algorithm; plan content pipeline accordingly"

#### Meta & Distribution (Q26–Q37)

**Q26: Platform Distribution?** *(multi-select)*
- YouTube only
- YouTube + Shorts/Reels (edited versions)
- YouTube + multiple platforms
- YouTube + LinkedIn/Twitter (professional focus)
- YouTube + Kids platform (for kids content)
- AI Recommends: "Category determines optimal platforms"

**Q27: Production Quality Level?**
- Standard (clear, well-edited, acceptable)
- Premium (broadcast quality)
- Cinema (theatrical quality)
- AI Note: "Quality expectations vary by category; kids/sanatan content often values polish over rawness"

**Q28: Audience Geographic Focus?**
- Global
- India focus
- US focus
- Other (specify)
- AI Recommends: "Affects topic selection, cultural context, language choices"

**Q29: Factual Verification Timeline?**
- Quick turnaround (24-48 hours)
- Standard (3-7 days)
- Thorough (1-2 weeks)
- Investigative (2-4 weeks)
- AI Note: "More time = higher accuracy; Critical-risk categories require thorough verification"

**Q30: Expert/Access?**
- No interviews (pure research)
- Some (1-2 sources)
- Extensive (3+ sources/expert commentary)
- Celebrity/Famous person access
- AI Reality: "Access affects timeline and credibility"

**Q31: Controversial Content Level?**
- No controversial claims
- Minor debates only (acknowledge debate)
- Include major controversies
- Focus on controversial elements
- AI Warns: "Each controversy needs citation + balanced framing"

**Q32: Comparative/Fairness Level?**
- No comparisons
- Fair comparison (acknowledge strengths/weaknesses both)
- Ranking/Hierarchy
- Critical comparison (pointing out failures)
- AI Reality: "Fair = trusted; unfair = audience skepticism"

**Q33: Current Events Included?**
- Historical only
- Some recent updates
- Very current (last 6 months)
- Breaking news focus
- AI Caution: "Recent = verify constantly; facts change rapidly"

**Q34: Bias Prevention Strategy?** *(multi-select)*
- Acknowledge limitations
- Show multiple perspectives
- Cite sources for verification
- All three above
- AI Requirement: "Bias awareness = credibility; mandatory for investigative/controversial categories"

**Q35: Sponsored Content?**
- No sponsorships
- Sponsored by relevant brand/entity
- Affiliate links included
- AI Requirement: "Must disclose sponsorship transparently"

**Q36: Monetization Revenue Model?** *(multi-select)*
- AdSense revenue
- Sponsorship revenue
- Membership/Patronage
- Merchandise
- Multiple revenue streams
- AI Reality: "Revenue model depends on category, platform, and audience"

**Q37: Series/Playlist Strategy?**
- Standalone video
- Part of growing series
- Themed playlist (5+ videos)
- Channel-wide universe
- AI Tip: "Playlists boost watch time; series build audience loyalty"

#### SEO & Technical (Q38–Q42)

**Q38: SEO Keyword Priority?**
- General category keywords
- Specific topic/subject names
- Trending terms
- Long-tail educational keywords
- AI Generates: Keyword recommendations per Q1 + Q38

**Q39: Content Warning/Disclaimer Needed?**
- No warnings (positive, uncontroversial content)
- Educational disclaimer (not professional/legal advice)
- Sensitivity warning (controversial/disturbing content)
- Investment disclaimer (financial claims — only for finance categories)
- Spiritual disclaimer (devotional content: subjective interpretation)
- AI Requires: "Disclaimers = category + content dependent; always include for High-risk"

**Q40: Video Generation Method?**
- AI Video (Veo3 / Seedance / Kling / etc.)
- Standard animation (2D/3D, pre-rendered)
- Live action (filmed footage)
- Data visualization + narration
- Hybrid (AI video + animation overlays)
- AI Note: "AI Video = fast output; watch for clip limits per tool. Live action = highest quality but slowest."

**Q41: Content Safety Level?**
- Standard (ordinary content review)
- Strict (additional review for child-directed, health, civic, or sensitive claims)
- Critical (human specialist review required before publication)

**Q42: Scene Duration Strategy?**
- FIXED 8-SECOND (8 seconds per scene; shorten the final scene if needed)
- VARIABLE (record every scene duration and require the sum to equal Q14)
- Other fixed duration in whole seconds (state the number explicitly)
- Q14 must be an exact runtime in seconds before Phase 3. Ranges such as "8-12 minutes" are planning estimates, not valid scene-calculation inputs.

## CONFIG.md TEMPLATE

```markdown
# Phase 0: CONFIGURATION

Project: [Domain Name] — [Topic Title]

## Configuration Answers

**Q1: Content Category:** [answer]
**Q2: Target Audience:** [answer]
**Q3: Story Angle:** [answer]
**Q4: Content Depth Level:** [answer]
**Q5: Visual/Media Priority:** [answer]
**Q6: Interview/Documentation Segments:** [answer]
**Q7: Content Sensitivity Level:** [answer]
**Q8: Legal/Accuracy Concern:** [answer]
**Q9: Subject Focus:** [answer]
**Q10: Contested Facts Included:** [answer]
**Q11: Expertise Level Required:** [answer]
**Q12: Comparative Content:** [answer]
**Q13: Monetization Priority:** [answer]
**Q14: Total Duration:** [answer]
**Q15: Visual Style Primary:** [answer] *(multi-select: comma-separated)*
**Q16: Voiceover Approach:** [answer]
**Q17: Delivery Format:** [answer]
**Q18: Primary Language:** [answer]
**Q19: Additional Languages:** [answer]
**Q20: On-Screen Text Strategy:** [answer]
**Q21: Source/Research Priority:** [answer]
**Q22: Ending Tone:** [answer]
**Q23: Accuracy Priority:** [answer]
**Q24: Source Quality Requirements:** [answer]
**Q25: Update Frequency:** [answer]
**Q26: Platform Distribution:** [answer] *(multi-select: comma-separated)*
**Q27: Production Quality Level:** [answer]
**Q28: Audience Geographic Focus:** [answer]
**Q29: Factual Verification Timeline:** [answer]
**Q30: Expert/Access:** [answer]
**Q31: Controversial Content Level:** [answer]
**Q32: Comparative/Fairness Level:** [answer]
**Q33: Current Events Included:** [answer]
**Q34: Bias Prevention Strategy:** [answer] *(multi-select: comma-separated)*
**Q35: Sponsored Content:** [answer]
**Q36: Monetization Revenue Model:** [answer] *(multi-select: comma-separated)*
**Q37: Series/Playlist Strategy:** [answer]
**Q38: SEO Keyword Priority:** [answer]
**Q39: Content Warning/Disclaimer Needed:** [answer]
**Q40: Video Generation Method:** [answer]
**Q41: Content Safety Level:** [answer]
**Q42: Scene Duration Strategy:** [answer in seconds, or variable with a per-scene duration plan]

## Project Locks

**Scene Duration Strategy:** [FIXED 8-SECOND / VARIABLE]
**Batch Size:** [25 scenes per batch — standard]
**Source Verification Level:** [Standard / High / Critical]
**Legal Review Required:** [Yes / No — Reason]
**Monetization Focus:** [Yes / Secondary / No]
**Accuracy Bar:** [General / Mixed / Professional / Expert]
**Protected Fields (locked after Phase 2):** SceneNumber, Duration, Location, Chapter, Characters, TimeOfDay/Period

[If FIXED: Every scene in this project is exactly 8 seconds. No exceptions.]
[If VARIABLE: Per-scene duration rules as defined in Phase 2 Production Bible.]

These settings are LOCKED for the entire project. They cannot be changed after Phase 2 without restarting from Phase 2.

## Accuracy Checkpoint

- [ ] Target audience and story angle aligned
- [ ] Financial accuracy requirement set
- [ ] Legal liability review required/optional
- [ ] Video generation method confirmed
- [ ] Content safety level set
- [ ] File naming convention applied
- [ ] Autonomy mode selected
- [ ] User confirms proceed to Phase 1
```

---

## DOMAIN DEFAULT CONFIG ANSWERS

For a full auto-answer lookup table, see `autonomous.md` § 3.2. Below is a quick reference summary by content category.

### Company Stories (CAT_CompanyStories: 01, 03, 04, 05, 15)
- Q2: General Public | Q3: Historical Narrative | Q4: Moderate | Q5: Moderate
- Q6: Quotes Only | Q7: Balanced | Q8: Moderate | Q9: Balanced
- Q13: Important | Q14: 8–12 minutes | Q15: Timeline Visualization | Q16: Engaging Storytelling
- Q23: Mixed audience | Q24: High | Q39: Educational disclaimer | Q40: AI Video
- Q41: Standard | Q42: Default

### People & Personalities (CAT_PeoplePersonalities: 02)
- Q2: General Public | Q3: Biographical Narrative | Q4: Moderate
- Q9: Personality-Driven
- Q14: 8–12 minutes | Q15: Documentary + Interview Hybrid | Q16: Engaging Storytelling
- Q30: Some (1–2 interviews) | Q39: Educational disclaimer
- Q41: Standard | Q42: Default

### Scandals & Fraud (CAT_ScandalsFraud: 06, 07, 27, 33, 40)
- Q2: Professionals | Q3: Investigation Narrative | Q4: Deep Analysis
- Q7: Investigative | Q8: High (Critical for Topic 40) | Q9: Subject-Driven
- Q14: 12–15 minutes | Q15: Documentary Realism | Q16: Documentary Calm
- Q24: Critical | Q39: Legal disclaimer + controversy warning | Q40: AI Video
- Q41: Strict | Q42: Default

### Innovation & Tech (CAT_InnovationTech: 17, 18, 19, 20, 21, 22, 23)
- Q3: Innovation Focus | Q5: Heavy | Q9: Topic-Driven
- Q14: 10–15 minutes | Q15: Animated Explainers or Data Visualization Heavy
- Q16: Professional Authoritative | Q39: Investment disclaimer (for crypto, IPO, stock)
- Q41: Standard | Q42: Default

### Industry & Markets (CAT_IndustryMarkets: 12, 14, 16, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39)
- Q3: Economic Analysis | Q5: Heavy | Q8: Low
- Q14: 12–15 minutes | Q15: Data Visualization Heavy | Q16: Critical Analytical
- Q23: Mixed audience | Q24: High | Q39: Educational disclaimer (+ Investment disclaimer for finance/stock/insurance)
- Q41: Standard | Q42: Default

### Luxury & Consumer (CAT_LuxuryConsumer: 09, 10, 11, 13)
- Q3: Entertainment Focus | Q4: Simple | Q7: Avoid Controversy
- Q14: 10–15 minutes | Q15: Archive Footage + Documentary Realism
- Q16: Engaging Storytelling | Q39: Educational disclaimer
- Q41: Standard | Q42: Default

### Workplace & Labor (CAT_WorkplaceLabor: 25, 26, 28)
- Q3: Economic Analysis / Entertainment Focus | Q8: Moderate
- Q14: 10–15 minutes | Q15: Documentary Realism | Q16: Documentary Calm
- Q39: Educational disclaimer | Q41: Standard | Q42: Default

---

## DECISION TREES

Use these trees to speed up configuration and reduce errors.

### Decision Tree 1: Category Selection

```
START: What is the main subject?

1. Is it about an organization, company, or entity's story?
   YES → Select from Company Stories category
   NO → Go to 2

2. Is it about a notable individual's life, career, or impact?
   YES → Select from People & Personalities category
   NO → Go to 3

3. Is it about a system, market, industry, or economy?
   YES → Select from Industry & Markets category
   NO → Go to 4

4. Is it about a discovery, invention, technology, or innovation?
   YES → Select from Innovation & Tech category
   NO → Go to 5

5. Is it about workplace, labor, employment, or culture?
   YES → Select from Workplace & Labor category
   NO → Go to 6

6. Is it about a crisis, crash, or market event?
   YES → Select from Markets & Crises category
   NO → Go to 7

7. Is it about fraud, scandal, crime, or controversy?
   YES → Select from Scandals & Fraud category
   NO → Go to 8

8. Is it about luxury, consumer behavior, branding, or fashion?
   YES → Select from Luxury & Consumer category
   NO → Go to 9

9. Is it about finance, banking, insurance, or policy?
   YES → Select from Financial Systems category
   NO → 10

10. Does not fit above or cross-category?
    YES → See ALL_TOPICS_BY_NICHE.md for full category catalog
    Assign to closest category. If multi-category, note in CONFIG.md.

END: Content category identified. Use Q1 in CONFIG.md to record. Language selection (Q18–Q19) and all 42 questions apply next.
```

### Decision Tree 2: Visual Style Selection

```
START: What is the primary storytelling need?

A. Heavy use of historical footage, archival material, or real locations?
   → Archive Footage or Documentary Realism

B. Need to explain numbers, trends, or quantitative concepts?
   → Data Visualization Heavy or Infographics + Text Overlay

C. Need to teach a concept, system, or model from scratch?
   → Animated Explainers or Animation + Data Visualization Hybrid

D. Story spans decades or follows a clear chronological arc?
   → Timeline Visualization

E. Need expert credibility, testimony, or personal narratives?
   → Documentary + Interview Hybrid

F. Fast, platform-native short-form content (Shorts/Reels/TikTok)?
   → Minimalist Aesthetic or Stock Footage + Graphics

G. Complex competition, strategy, or comparative analysis?
   → Stock Footage + Graphics or Data Visualization Heavy

END: Document chosen style in 04_Visual_Style_Guide.md and lock it.
```

### Decision Tree 3: Legal / Safety Gating Check

Run this for every topic before proceeding to Phase 1.

```
START: Does this topic touch any sensitive area?

1. Does it involve a current lawsuit, active criminal investigation, or unproven allegations?
   YES → Mark legal risk High. Require legal review. Soft language only.
   NO → Go to 2

2. Does it involve financial advice, predictions, or buy/sell recommendations?
   YES → Add financial disclaimer. Remove all advice. Required for finance topics.
   NO → Go to 3

3. Does it involve named individuals who are not public figures?
   YES → Describe generically or obtain consent. Flag defamation risk.
   NO → Go to 4

4. Does it involve tragic events (deaths, suicides, severe harm)?
   YES → Handle with dignity. Add content warning if needed. Avoid sensationalism.
   NO → Go to 5

5. Does it involve politics, regulation, or controversial policy?
   YES → Maintain neutral framing. Avoid partisan language.
   NO → Go to 6

6. Does it involve sponsorship, affiliate links, or financial conflicts of interest?
   YES → Disclose in video and description in all language versions.
   NO → Go to 7

7. Does it involve figures or data that could be misinterpreted across languages?
   YES → Verify source. Add context notes. Ensure Hindi + English versions present identical figures.
   NO → Topic passes safety gate. Proceed.

END: Record all flags in CONFIG.md and 08_Legal_Compliance_Guide.md.
```

---

## FOLDER STRUCTURE & PROJECT ORGANIZATION

### Main Project Hierarchy

```
UniversalContentReGen/
│
├── agents.md
├── CLAUDE.md
├── autonomous.md
├── ALL_TOPICS_BY_NICHE.md
├── PROGRESS.md
├── Structure.txt
│
├── 01_Phase0_Configuration/
├── 02_Phase1_RESEARCH_BIBLE/
├── 03_Phase2_PRODUCTION_BIBLE/
├── 04_Phase3_SCENE_BREAKDOWN/
├── 05_Phase4_PRODUCTION_PACKAGE/
├── 06_Phase5_FINAL_AUDIT/
│
└── Topics/
    └── CAT_<CategorySlug>/
        └── <NN>_<TopicSlug>/
```
```

### Per-Topic Folder Structure

```
Topics/CAT_CompanyStories/01_<topic_slug>/
│
├── 01_Phase0_CONFIG/
│   └── CONFIG.md
│
├── 02_Phase1_RESEARCH_BIBLE/
│   ├── Research_Summary.md
│   ├── Facts_Documented.md
│   ├── Figures_Verified.md
│   ├── Accuracy_Check.md
│   ├── Source_List_with_Links.md
│   ├── Language_Fidelity_Notes.md
│   └── MASTER_CONTEXT_v1.md
│
├── 03_Phase2_PRODUCTION_BIBLE/
│   ├── 00_Project_Consistency_Rules.md
│   ├── 01_Research_Sources.md
│   ├── 02_Language_Fidelity_Check.md
│   ├── 03_Accuracy_Verification_Checklist.md
│   ├── 04_Visual_Style_Guide.md
│   ├── 05_Voiceover_Guide.md
│   ├── 06_Language_Localization_Guide.md
│   ├── 07_Distribution_Strategy.md
│   ├── 08_Legal_Compliance_Guide.md
│   ├── 09_Cultural_Adaptation_Guide.md
│   ├── 10_Scene_Template.md
│   ├── 11_MultiLanguage_Script.md
│   ├── 12_Monetization_Strategy.md
│   ├── 13_Source_Credibility_Guide.md
│   ├── 14_Regeneration_Consistency_Checklist.md
│   └── 15_Project_Summary.md
│
├── 04_Phase3_SCENE_BREAKDOWN/
│   ├── Batch_01_Scenes_01_to_25.md
│   ├── Batch_02_Scenes_11_to_20.md
│   └── ...
│   (VOICE_SCRIPT_<lang>.md if Q19 ≠ None)
│
├── 05_Phase4_PRODUCTION_PACKAGE/
│   └── Production_Package.md
│
└── 06_Phase5_FINAL_AUDIT/
    ├── Audit_Report.md
    └── Completion_Certificate.md
```

### Naming Rules

- Niche folders: `NN_Domain_Name` (two-digit number, underscores for spaces)
- Topic folders: `NN_Topic_Title` (two-digit number, underscores for spaces)
- Phase folders: `01_Phase0_CONFIG`, `02_Phase1_RESEARCH_BIBLE`, `03_Phase2_PRODUCTION_BIBLE`, `04_Phase3_SCENE_BREAKDOWN`, `05_Phase4_PRODUCTION_PACKAGE`, `06_Phase5_FINAL_AUDIT`
- Batch files: `Batch_NN_Scenes_XX_to_YY.md`
- All content files: use ONLY letters, numbers, and underscores in filenames
- Default file pattern: `[domain]-[title]-v[version].md`

---

## CONTENT-TYPE TIMING GUIDANCE

**This table applies only when Q42 = VARIABLE.** When Q42 = FIXED 8-SECOND (the default), every scene is exactly 8 seconds with no exceptions. In VARIABLE mode, use this table as the authoritative reference for scene duration and pacing decisions.

| Content Type | Scene Duration | Pacing | Notes |
|---|---|---|---|
| Historical Narrative | 7–8s | Medium, narrative | Story beats, emotional moments |
| Biographical Profile | 8s | Slow, biographical | Personal journey pacing |
| Innovation/Discovery | 6–7s | Fast, energetic | Innovation energy, growth pacing |
| Economic Analysis | 7–8s | Medium-slow | Data-heavy, serious tone |
| Comparison/Competition | 6–7s | Fast, competitive | Action, confrontation pacing |
| Educational Explainer | 6s | Fast, focused | Concept clarity, hold attention |
| Short Reels (1–3 min) | 5–6s | Very fast | Hook quickly, visual storytelling |
| Long-form Deep Dive | 8–10s | Deliberate | Time for analysis, data viz |

**How to Use:**
- **AI Video (Veo3 / Seedance / Kling):** Stay within 5–8s per scene; clip limits vary by tool. Plan scene length per tool specs before Phase 3.
- **Standard animation / Live action:** Full range applies freely; pacing is fully under creative control.
- **Data viz + interview clips:** Favor the longer end (8–10s) for deep dives where chart reveal time and quote pauses matter.
- **Multi-language consistency:** Scene durations must be matched across Hindi (Devanagari), Hindi (Romanised), and English voice scripts.
- **Series consistency:** Once a pacing profile is locked per series, apply it consistently across episodes.

**Default Scene Count Formula:** Total Duration (seconds) ÷ 8 = Scene count. For a 10-minute (600s) project, this is ~75 scenes. For a 12-minute project, ~90 scenes.

---

**VERSION:** MASTER_UNIVERSAL_CONTENT_REGEN_v3_0

**STATUS:** Production-Ready with Agent Orchestration + Multi-Language Regeneration

**READY FOR USE:**
- Start with: `/invoke [category]` or pick from `ALL_TOPICS_BY_NICHE.md`
- Default autonomy: Balanced (recommended for all domains)
- Accuracy: Mandatory fact verification, applied equally to ALL language versions
- Language fidelity: Hindi (Devanagari) + Hindi (Romanised) + English must be factually identical
- Safety: Content safety and legal compliance filters apply to all generated scenes
- Timing: Consult Content-Type Timing Guidance table before locking scene duration
- File Naming: Apply Q42 default pattern `[domain]-[title]-v[version].md` from Phase 0 onward

**END OF MASTER UNIVERSAL CONTENT REGEN — Phase0 Configuration**
