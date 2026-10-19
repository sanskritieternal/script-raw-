# Autonomous Mode — Reference & Tuning Manual

> This file documents the autonomous production engine for the V6 Content Factory. Edit values here to change how the agent behaves when running in autonomous mode. The main `agents.md` is the orchestrator — this file is the spec sheet.

---

## 1. ACTIVATING AUTONOMOUS MODE

The agent runs in autonomous mode when:
- The user types `/mode autonomous`
- The session starts with `PROGRESS.md` already present (assumes autonomous)
- The user explicitly asks for bulk/mass/automatic production

If both modes are valid (interactive for one project, autonomous for the queue), the agent asks once at startup: "Interactive (one project with you guiding), Domain Preset (answer once per domain), or Autonomous (run the production queue)?"

---

## 1.5 DOMAIN-LEVEL PRESET MODE

Domain-Level Preset mode is a hybrid between interactive and autonomous. Use it when many topics in the same domain share the same configuration.

**How it works:**
1. The user answers Q1–Q42 **once per domain**.
2. Answers are saved to `DOMAIN_PRESETS.md`.
3. For every topic in that domain, the preset answers become the **Recommended** default in interactive mode.
4. The AI only asks follow-up questions when a specific topic clearly differs from the domain preset.

**When to use:**
- A domain has 10–20 topics that all use the same visual style, duration, audience, and monetization settings.
- You want faster interactive production without fully giving up oversight.

**Note:** If the user has already set `DOMAIN_PRESETS.md`, read it first and use those answers as defaults. If a preset file does not exist, ask the user if they want to create one before starting the first topic in a new domain.

---

## 2. CORE LOOP (Don't Break This)

```
For each topic in ALL_TOPICS_BY_NICHE.md (in order):
    1. Auto-answer 42 config questions from lookup tables
    2. Write 01_Phase0_CONFIG/CONFIG.md
    3. Phase 1 — Research Bible
    4. Phase 2 — Production Bible (16 production bible files)
    5. Phase 3 — Scene Breakdown (Batch 1 interactive; remaining batches autonomously at 25 scenes per batch)
    6. Phase 4 — Production Package
    7. Phase 5 — Final Audit (70-point checklist)
    8. Write Completion Certificate
    9. Update PROGRESS.md
    10. Move to next topic
```

**Never:**
- Skip a phase
- Combine phases
- Reuse a topic's content for another topic
- Stop mid-topic (unless session ends)

---

## 3. CONFIG AUTO-ANSWER (Q1–Q42)

The agent auto-answers all 42 questions by combining a domain lookup (Q1) with a domain-category preset (Q2–Q42). For questions marked **(multi-select)** in `01_Phase0_Configuration/MASTER_Phase0_Config.md`, the default answer may be a comma-separated list.

### 3.1 Domain → Business Category Mapping (Q1)

Use this table to identify the domain category and default risk profile.

| Domain # | Domain Name | Category | Default Risk |
|---|---|---|---|
| 01 | Company Rise & Fall | Company Stories | Low |
| 02 | Billionaire Stories | People & Personalities | Moderate |
| 03 | Startup Stories | Company Stories | Low |
| 04 | Failed Businesses | Company Stories | Low |
| 05 | Brand Wars | Markets & Competition | Low |
| 06 | Corporate Scandals | Scandals & Fraud | High |
| 07 | Business Mysteries | Scandals & Fraud | Moderate |
| 08 | Famous Product Histories | Innovation & Tech | Low |
| 09 | Luxury Brand History | Luxury & Consumer | Low |
| 10 | Advertising History | Luxury & Consumer | Low |
| 11 | Marketing Psychology | Luxury & Consumer | Low |
| 12 | Economic History | Industry & Markets | Low |
| 13 | Fashion Industry Evolution | Luxury & Consumer | Low |
| 14 | Real Estate Empires | Industry & Markets | Moderate |
| 15 | Franchise Empires | Company Stories | Low |
| 16 | Energy Industry History | Industry & Markets | Low |
| 17 | Cryptocurrency & Blockchain | Innovation & Tech | High |
| 18 | E-Commerce Revolution | Innovation & Tech | Low |
| 19 | Tech Giants Rise | Innovation & Tech | Moderate |
| 20 | Venture Capital Stories | Innovation & Tech | Low |
| 21 | Artificial Intelligence Business Impact | Innovation & Tech | Low |
| 22 | Product Failures | Innovation & Tech | Low |
| 23 | IPO Stories | Innovation & Tech | Low |
| 24 | Mergers & Acquisitions | Markets & Competition | Low |
| 25 | Workplace Culture Evolution | Workplace & Labor | Low |
| 26 | Labor Movements History | Workplace & Labor | Low |
| 27 | Corporate Culture Scandals | Scandals & Fraud | High |
| 28 | Influencer Economy | Workplace & Labor | Low |
| 29 | Financial Crises | Industry & Markets | Moderate |
| 30 | Stock Market History | Industry & Markets | Moderate |
| 31 | Retail Disruption | Industry & Markets | Low |
| 32 | Supply Chain & Logistics | Industry & Markets | Low |
| 33 | Corporate Espionage | Scandals & Fraud | High |
| 34 | Trade Wars & Tariffs | Industry & Markets | Low |
| 35 | Banking Industry History | Industry & Markets | Moderate |
| 36 | Pharmaceutical Industry | Industry & Markets | Moderate |
| 37 | Automotive Evolution | Industry & Markets | Low |
| 38 | Entertainment Business | Industry & Markets | Moderate |
| 39 | Insurance Industry | Industry & Markets | Low |
| 40 | Corporate Fraud & Crime | Scandals & Fraud | Critical |

**To add a new domain:** Add a row to this table. The agent picks up the defaults automatically.

**To change a mapping:** Edit the Category or Default Risk column. All topics in that domain will use the new defaults from the next topic onward.

---

### 3.2 Domain Category Presets (Q2–Q42 Defaults)

Each category has a preset covering Q2–Q42. Edit any preset to change defaults.

#### Company Stories (Rise/Fall, Startups, Failed Businesses, Brand Wars, Franchise, Product History, IPO, M&A)
- Q2: General Public | Q3: Rise/Fall Narrative | Q4: Moderate | Q5: Moderate
- Q6: Quotes Only | Q7: Balanced | Q8: Moderate | Q9: Balanced
- Q10: Some debated facts | Q11: General knowledge | Q12: Multiple competitors analyzed
- Q13: Important | Q14: 8-12 minutes | Q15: Timeline Visualization | Q16: Engaging Storytelling
- Q17: Single video | Q18: English | Q19: None | Q20: Moderate
- Q21: Important | Q22: Bittersweet | Q23: Mixed audience | Q24: High
- Q25: One-off videos | Q26: YouTube + Shorts | Q27: Premium | Q28: Global
- Q29: Standard (3-7 days) | Q30: No interviews | Q31: Minor controversies only
- Q32: Fair comparison | Q33: Historical only | Q34: All three | Q35: No sponsorships
- Q36: AdSense revenue | Q37: Themed playlist | Q38: Specific company names
- Q39: Educational disclaimer | Q40: AI Video | Q41: Standard | Q42: FIXED 8-SECOND

#### People & Personalities (Billionaire Stories)
- Q2: General Public | Q3: Rise/Fall Narrative | Q4: Moderate | Q5: Moderate
- Q6: Documentary Style | Q7: Balanced | Q8: Moderate | Q9: Personality-Driven
- Q10: Some debated facts | Q11: General knowledge | Q12: No competitors
- Q13: Important | Q14: 8-12 minutes | Q15: Documentary + Interview Hybrid | Q16: Engaging Storytelling
- Q17: Single video | Q18: English | Q19: None | Q20: Moderate
- Q21: Important | Q22: Bittersweet | Q23: Mixed audience | Q24: High
- Q25: One-off videos | Q26: YouTube + Shorts | Q27: Premium | Q28: Global
- Q29: Standard | Q30: Some (1-2 interviews) | Q31: Minor controversies only
- Q32: Fair comparison | Q33: Historical only | Q34: All three | Q35: No sponsorships
- Q36: AdSense + Sponsorship | Q37: Themed playlist | Q38: Specific names + trending
- Q39: Educational disclaimer | Q40: AI Video | Q41: Standard | Q42: FIXED 8-SECOND

#### Innovation & Tech (Crypto, AI, E-commerce, Tech Giants, VC, Product Failures)
- Q2: General Public | Q3: Innovation Focus | Q4: Moderate | Q5: Heavy
- Q6: Quotes Only | Q7: Balanced | Q8: Moderate | Q9: Business-Driven
- Q10: Some debated facts | Q11: Some industry background | Q12: Multiple competitors
- Q13: Important | Q14: 10-15 minutes | Q15: Animated Explainers or Data Visualization Heavy
- Q16: Professional Authoritative | Q17: Single video or Series | Q18: English | Q19: None
- Q20: Heavy | Q21: Essential | Q22: Forward-looking | Q23: Mixed audience
- Q24: High | Q25: One-off videos | Q26: YouTube + Shorts | Q27: Premium
- Q28: Global | Q29: Standard | Q30: No interviews | Q31: Minor controversies only
- Q32: Fair comparison | Q33: Some recent updates | Q34: All three | Q35: No sponsorships
- Q36: AdSense + Sponsorship | Q37: Themed playlist | Q38: Trending terms + specific names
- Q39: Investment disclaimer | Q40: AI Video | Q41: Standard | Q42: FIXED 8-SECOND

#### Scandals & Fraud (Corporate Scandals, Fraud, Culture Scandals, Espionage, Business Mysteries)
- Q2: Business Professionals | Q3: Scandal/Controversy | Q4: Deep Analysis
- Q5: Moderate | Q6: Documentary Style | Q7: Investigative | Q8: High
- Q9: Business-Driven | Q10: Contested claims | Q11: Significant expertise
- Q12: Multiple competitors analyzed | Q13: Secondary | Q14: 12-15 minutes
- Q15: Documentary Realism | Q16: Documentary Calm | Q17: Single video
- Q18: English | Q19: None | Q20: Moderate | Q21: Important
- Q22: Failure/Cautionary | Q23: Industry professionals | Q24: Critical (SEC filings, court docs)
- Q25: One-off videos | Q26: YouTube + LinkedIn | Q27: Documentary professional
- Q28: Global | Q29: Thorough (1-2 weeks) | Q30: Some (1-2 interviews)
- Q31: Include major controversies | Q32: Fair comparison | Q33: Historical only
- Q34: All three | Q35: No sponsorships | Q36: AdSense
- Q37: Themed playlist | Q38: Specific names + trending | Q39: Controversy warning
- Q40: AI Video | Q41: Strict | Q42: FIXED 8-SECOND

**Note:** For Corporate Fraud & Crime (Domain 40), Q8 = Critical and Q39 = Investment disclaimer + Controversy warning.

#### Industry & Markets (Economic History, Financial Crises, Stock Market, Banking, Insurance, Pharma, Trade, Real Estate, Energy, etc.)
- Q2: General Public | Q3: Economic Analysis | Q4: Moderate | Q5: Heavy
- Q6: Quotes Only | Q7: Balanced | Q8: Low | Q9: Not Applicable
- Q10: No controversial claims | Q11: General knowledge | Q12: Multiple competitors
- Q13: Important | Q14: 12-15 minutes | Q15: Data Visualization Heavy | Q16: Critical Analytical
- Q17: Single video or Series | Q18: English | Q19: None | Q20: Heavy
- Q21: Essential | Q22: Forward-looking | Q23: Mixed audience | Q24: High
- Q25: One-off videos | Q26: YouTube + LinkedIn | Q27: Premium | Q28: Global
- Q29: Standard | Q30: No interviews | Q31: No controversial claims
- Q32: Fair comparison | Q33: Historical only | Q34: All three | Q35: No sponsorships
- Q36: AdSense | Q37: Themed playlist | Q38: Specific names + long-tail
- Q39: Educational disclaimer | Q40: AI Video | Q41: Standard | Q42: FIXED 8-SECOND

**Note:** For Financial Crises, Stock Market, Banking, Trade Wars, and Real Estate, Q39 = Investment disclaimer.

#### Luxury & Consumer (Luxury Brands, Advertising, Marketing Psychology, Fashion)
- Q2: General Public | Q3: Entertainment Focus | Q4: Simple | Q5: Moderate
- Q6: Quotes Only | Q7: Avoid Controversy | Q8: No | Q9: Business-Driven
- Q10: No controversial claims | Q11: General knowledge | Q12: Multiple competitors
- Q13: Important | Q14: 10-15 minutes | Q15: Archive Footage + Documentary Realism
- Q16: Engaging Storytelling | Q17: Single video or Series | Q18: English | Q19: None
- Q20: Moderate | Q21: Important | Q22: Forward-looking | Q23: General audience
- Q24: Standard | Q25: One-off videos | Q26: YouTube + Shorts | Q27: Premium
- Q28: Global | Q29: Standard | Q30: No interviews | Q31: No controversial claims
- Q32: Fair comparison | Q33: Historical only | Q34: All three | Q35: No sponsorships
- Q36: AdSense + Sponsorship | Q37: Themed playlist | Q38: Specific brand names
- Q39: Educational disclaimer | Q40: AI Video | Q41: Standard | Q42: FIXED 8-SECOND

#### Workplace & Labor (Workplace Culture, Labor Movements, Influencer Economy)
- Q2: General Public | Q3: Economic Analysis / Entertainment Focus | Q4: Moderate
- Q5: Moderate | Q6: Quotes Only | Q7: Balanced | Q8: Moderate
- Q9: Not Applicable | Q10: Some debated facts | Q11: Some industry background
- Q12: Multiple competitors | Q13: Secondary | Q14: 10-15 minutes
- Q15: Documentary Realism | Q16: Documentary Calm | Q17: Single video
- Q18: English | Q19: None | Q20: Moderate | Q21: Important
- Q22: Bittersweet | Q23: Mixed audience | Q24: High | Q25: One-off videos
- Q26: YouTube + LinkedIn | Q27: Premium | Q28: Global | Q29: Standard
- Q30: No interviews | Q31: Minor controversies only | Q32: Fair comparison
- Q33: Some recent updates | Q34: All three | Q35: No sponsorships
- Q36: AdSense | Q37: Themed playlist | Q38: Trending terms
- Q39: Educational disclaimer | Q40: AI Video | Q41: Standard | Q42: FIXED 8-SECOND

---

## 4. LOCKS (Cannot Be Changed Mid-Project)

These are locked at the end of Phase 2. The agent enforces them automatically.

### 4.1 Scene Duration Strategy (Q42)

**Default:** `FIXED 8-SECOND` for ALL domains in autonomous mode.

**To switch to VARIABLE:** Edit every category preset above to set Q42: VARIABLE. This will require recalculating all scene durations.

**To set per-domain:** Change Q42 in the domain-specific preset row. Mixed durations across domains is allowed but breaks consistency for cross-domain projects.

### 4.2 Protected Fields (After Phase 2)
- SceneNumber
- Duration
- Location
- Chapter
- Characters
- TimeOfDay / Period
- DataVisualizationType (if set)

If any of these change after Phase 2, all downstream phases must be regenerated. The agent will refuse to change these in autonomous mode — fix upstream and restart.

### 4.3 Story Angle Lock (After Phase 2)
Q3 (story angle) is locked in `00_Project_Consistency_Rules.md`. Changes require Phase 2 revision.

### 4.4 Visual Style Lock (After Phase 2)
Q15 (visual style) is locked in `04_Visual_Style_Guide.md`. Same style for every scene.

### 4.5 Voiceover Tone Lock (After Phase 2)
Q16 (voiceover approach) is locked in `05_Voiceover_Guide.md`.

### 4.6 Accuracy Bar Lock (After Phase 2)
Q23/Q24 (accuracy priority and source quality) are locked in `03_Accuracy_Verification_Checklist.md` and `13_Source_Credibility_Guide.md`.

### 4.7 Legal Review Flag Lock (After Phase 2)
Q8 (legal liability) is locked in `08_Legal_Liability_Guide.md`. If Critical, legal review is mandatory before publishing.

---

## 5. BATCH SIZES & FILE COUNTS

### 5.1 Scene Batch Size (Phase 3)

**Default:** 25 scenes per batch.

Content is fact-dense; 25-scene batches balance accuracy with throughput while the safeguards checklist runs per batch.

| Batch Size | Use When |
|---|---|
| 5 scenes | High-risk / scandal / fraud topics |
| 25 scenes | Default — balanced accuracy and speed |
| 20 scenes | Low-risk / evergreen topics with simple facts |

### 5.2 Scene Count Formula

**Default: Total Scenes = Total Duration (seconds) ÷ 8**

For default 10-minute projects: 600s ÷ 8 = 75 scenes.

| Video Length | Total Scenes | Batches (at 25/batch) |
|---|---|---|
| 5 min (300s) | ~38 scenes | 2 batches |
| 8 min (480s) | ~60 scenes | 3 batches |
| 10 min (600s) | ~75 scenes | 3 batches |
| 12 min (720s) | ~90 scenes | 4 batches |
| 15 min (900s) | ~113 scenes | 5 batches |
| 20 min (1200s) | ~150 scenes | 6 batches |

### 5.3 Per-Project File Count

For a 10-minute project:
- 1 CONFIG.md
- 1 Research Bible file (or 6 sub-files)
- 16 Production Bible files
- 3 scene batch files (75 scenes ÷ 25)
- 1 Production Package file
- 1 Audit Report
- 1 Completion Certificate
- **= ~28 files per topic**

### 5.4 Total Production Volume

For 40 domains × 20 topics = 800 topics: ~19,200 files.

---

## 6. PROGRESS TRACKING

### 6.1 PROGRESS.md Location

`OUTPUT/<Category>/PROGRESS.md`

### 6.2 PROGRESS.md Format

```markdown
# Production Progress Tracker

Last Updated: [YYYY-MM-DD]

## Domain Status

| Domain | Name | Category | Status | Topics Done | Total Topics |
|---|---|---|---|---|---|
| 01 | Company Rise & Fall | Company Stories | pending | 0 | 20 |
| 02 | Billionaire Stories | People & Personalities | pending | 0 | 20 |
| ... | ... | ... | ... | ... | ... |

## Completed Topics

| Domain | Topic # | Topic Title | Date Completed |
|---|---|---|---|
| 01 | 01 | Kodak: The Film Empire That Missed Digital | 2026-08-16 |
| 01 | 02 | Blockbuster: The Last Late Fee | 2026-08-16 |
| ... | ... | ... | ... |
```

### 6.3 Update Protocol

After every completed topic:
1. Mark the topic as completed in the "Completed Topics" table.
2. Increment the "Topics Done" count for that domain.
3. If Topics Done == Total Topics, mark the domain as `COMPLETE`.
4. Update "Last Updated" date.

### 6.4 Resume Protocol

At session start, the agent:
1. Reads `PROGRESS.md`.
2. Finds the first topic NOT in the Completed Topics table.
3. Checks if a partial project exists for that topic (some phase folders present).
4. If yes: resumes from the first missing phase.
5. If no: starts from Phase 0.

---

## 7. SESSION CONTROL

### 7.1 Session Start

```bash
/mode autonomous
# or
PROGRESS.md found at <path>. Resuming production at [Domain X, Topic Y, Phase Z].
```

The agent:
1. Reads `PROGRESS.md`.
2. Announces resume position.
3. Continues production.

### 7.2 Session End

When the user says "stop", context runs out, or natural break:
1. Finish current topic if within 1 phase of completion.
2. Otherwise stop at current phase boundary.
3. Update `PROGRESS.md` with completed work.
4. Announce: "Session complete. Next session starts at [Domain X, Topic Y, Phase Z]."

**Never:** start a new topic in the same session unless the current one is fully complete.

### 7.3 Interrupted Topic Recovery

If a topic has some phases completed:
- Check which phase folders exist.
- Resume from the first missing phase.
- Do NOT redo completed phases (unless they have errors).

---

## 8. FOLDER STRUCTURE

### 8.1 Universal Structure

```
V6/
├── CORE/
│   ├── PIPELINE/             ← universal 6-phase engine
│   │   ├── 01_Phase0_Configuration/      MASTER_Phase0_Config.md
│   │   ├── 02_Phase1_RESEARCH_BIBLE/     MASTER_Phase1_ResearchBible.md
│   │   ├── 03_Phase2_PRODUCTION_BIBLE/   MASTER_Phase2_ProductionBible.md + 16 files
│   │   ├── 04_Phase3_SCENE_BREAKDOWN/    MASTER_Phase3_SceneBreakdown.md
│   │   ├── 05_Phase4_PRODUCTION_PACKAGE/ MASTER_Phase4_ProductionPackage.md
│   │   └── 06_Phase5_FINAL_AUDIT/        MASTER_Phase5_FinalAudit.md
│   └── RULES/
│       ├── CLAUDE.md         ← system entrypoint
│       ├── agents.md         ← orchestrator
│       ├── autonomous.md     ← this file (tuning manual)
│       └── INVOKE_COMMANDS.md ← slash commands
├── REGISTRY/
│   ├── MASTER_REGISTRY.md    ← all 500+ niches index
│   ├── Topics/<Category>/    ← per-category topic list + presets + niches/
│   └── Categories/CAT_*.md  ← Q2-Q42 presets per category type
└── OUTPUT/<Category>/
    ├── PROGRESS.md           ← per-category tracker
    └── Topics/<ID>_Topic/    ← all 6 phases written here
```

### 8.2 Per-Topic Structure (Autonomous Mode)

```
OUTPUT/<Category>/
└── Topics/
    └── <ID>_<TopicName>/
        ├── 01_Phase0_CONFIG/
        │   └── CONFIG.md
        ├── 02_Phase1_RESEARCH_BIBLE/
        │   ├── Research_Summary.md
        │   ├── Timeline_Accuracy_Check.md
        │   ├── Key_People.md
        │   ├── Financial_Data.md
        │   ├── Primary_Sources.md
        │   └── Quotes_Sources.md
        ├── 03_Phase2_PRODUCTION_BIBLE/  (16 files)
        ├── 04_Phase3_SCENE_BREAKDOWN/   (batch files)
        ├── 05_Phase4_PRODUCTION_PACKAGE/
        │   └── Production_Package.md
        └── 06_Phase5_FINAL_AUDIT/
    │   │       ├── Audit_Report.md
    │   │       └── Completion_Certificate.md
    │   ├── 02_Next_Topic_Title/
    │   └── ... (20+ topics per domain)
    └── ... (40+ domains)
```

### 8.3 Naming Rules

- Domain folders: `NN_Domain_Name` (NN = 2-digit number, underscores for spaces)
- Topic folders: `NN_Topic_Title` (NN = 2-digit topic position, underscores for spaces)
- Phase folders: `01_Phase0_CONFIG`, `02_Phase1_RESEARCH_BIBLE`, `03_Phase2_PRODUCTION_BIBLE`, `04_Phase3_SCENE_BREAKDOWN`, `05_Phase4_PRODUCTION_PACKAGE`, `06_Phase5_FINAL_AUDIT`
- Batch files: `Batch_NN_Scenes_XX_to_YY.md`
- All filenames: ONLY letters, numbers, underscores

---

## 9. QUALITY GATES

### 9.1 Production Safeguards Checklist

Run before EVERY batch in Phase 3:

- [ ] Q42 Duration Strategy confirmed (FIXED 8-SEC or VARIABLE)
- [ ] Every scene duration matches Q42 strategy
- [ ] Voiceover durations within limits (max 8s or scene-duration minus 1-2s)
- [ ] Protected fields match Phase 2: SceneNumber, Duration, Location, Chapter, Characters, TimeOfDay
- [ ] All financial figures verified against credible sources
- [ ] No defamatory statements or unverified accusations
- [ ] Sources cited per scene (name, URL, date)
- [ ] Tone matches target audience (Q2)
- [ ] Legal risk flags addressed
- [ ] Controversial claims balanced with evidence
- [ ] ZERO placeholders anywhere ([TBD], [TODO], [PLACEHOLDER], [INSERT])
- [ ] Company/person names spelled correctly
- [ ] Inflation adjustments noted where applicable
- [ ] Investment disclaimer included if financial advice implied

### 9.2 Final Audit (70 checks)

Full checklist lives in `06_Phase5_FINAL_AUDIT/MASTER_Phase5_FinalAudit.md`.

Categories:
- Factual Accuracy & Verification (18)
- Legal & Liability Protection (12)
- Financial Accuracy & Explanations (12)
- Fair Representation & Balance (8)
- Source Attribution & Documentation (8)
- Content & Ethical Storytelling (6)
- YouTube Optimization (6)

**All must PASS** for the topic to be marked complete.

### 9.3 Failure Handling

If audit fails:
1. Identify the failed check.
2. Return to the relevant phase.
3. Fix the issue.
4. Re-run all downstream phases (everything after the fix point).
5. Re-run audit.
6. Only mark complete when ALL PASS.

---

### Plain-Text Scene Formatting Rules (final output)

- [ ] Plain text only inside scene blocks; no Markdown symbols
- [ ] NO Markdown headings (`###`)
- [ ] NO bold formatting (`**`)
- [ ] NO separator lines (`---`)
- [ ] Exactly 3 blank lines between the end of one scene and the beginning of the next scene
- [ ] No extra blank lines anywhere inside a scene
- [ ] No placeholder, template, or instructional text in the final output

## 10. GOLDEN RULES (Non-Negotiable)

1. **FACTUAL ACCURACY FIRST.** Numbers, dates, and claims must be verified. Wrong numbers destroy credibility.
2. **LEGAL SAFETY.** No defamation, no unverified accusations, no illegal content. High-risk topics get legal review.
3. **SOURCE EVERYTHING.** Every significant claim needs a credible source cited in the production package.
4. **NO PLACEHOLDER CONTENT.** No `[PLACEHOLDER]`, `[TBD]`, `[TODO]`, `[DESCRIBE]`, or generic descriptions anywhere.
5. **NEVER SKIP A PHASE.** All 5 phases for every topic.
6. **LOCKS ARE LOCKED.** After Phase 2 approval, protected fields do not change without restarting from Phase 2.
7. **FAIR REPRESENTATION.** Acknowledge successes of criticized companies and failures of praised founders.
8. **DISCLOSE CONFLICTS.** Sponsored content, affiliate links, stock ownership, and biases must be disclosed.
9. **NOT INVESTMENT ADVICE.** Financial disclaimers mandatory for investment-related content.
10. **UPDATE PROGRESS AFTER EVERY TOPIC.** `PROGRESS.md` is the continuity lifeline in autonomous mode.

---

## 11. TUNING QUICK REFERENCE

| What to Change | Where to Edit | Effect |
|---|---|---|
| Domain → category mapping | § 3.1 table | Changes defaults for all topics in that domain |
| Default config for a category | § 3.2 preset block | Changes Q2–Q42 for all topics using that category |
| Scene duration strategy | § 4.1 (every preset) | Switches all projects to FIXED or VARIABLE |
| Batch size (Phase 3) | § 5.1 | Accuracy/speed trade-off |
| Scene count formula | § 5.2 | Changes scene duration math |
| PROGRESS.md format | § 6.2 | Changes how progress is tracked |
| Folder structure | § 8 | Changes where files go |
| Production safeguards | § 9.1 | Adds/removes pre-batch checks |
| Golden rules | § 10 | Adds/removes agent constraints |

---

## 12. WHAT YOU EDIT VS WHAT THE AGENT EDITS

**You edit (tuning):**
- Domain mappings (§ 3.1)
- Category presets (§ 3.2)
- Q42 strategy (§ 4.1)
- Batch sizes (§ 5.1)
- Folder structure (§ 8)
- Quality gate thresholds (§ 9)
- Golden rules (§ 10)

**The agent edits (output):**
- All CONFIG.md files
- All Research Bible files
- All 16 Production Bible files
- All scene batch files
- All Production Packages
- All Audit Reports
- All Completion Certificates
- `PROGRESS.md` (status updates only, never the format)

---

END OF autonomous.md
