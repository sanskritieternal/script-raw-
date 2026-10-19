# MASTER SKILL — Phase3 Scene Breakdown

> Use `CORE/PIPELINE/CONTRACT.md` for current paths, Q meanings and timing. The financial and tool-specific examples below apply only where relevant. Every material factual scene must cite a Phase 1 claim ID.

This phase turns verified research into production-ready scenes. Every scene must be factually accurate, legally safe, visually specific, and properly sourced. Scenes are written in batches and checked with the Production Safeguards Checklist before approval.

**Inputs:** `02_Phase1_RESEARCH_BIBLE/` and `03_Phase2_PRODUCTION_BIBLE/`.
**Outputs:** Batch scene files in `04_Phase3_SCENE_BREAKDOWN/`.
**Quality Gate:** Batch 1 interactive approval; remaining batches run autonomously with internal checklist per batch.

---

## TABLE OF CONTENTS

1. [Phase 3 Goal & Deliverables](#phase-3-goal--deliverables)
2. [Scene Count Formula](#scene-count-formula)
3. [Batch Processing Rules](#batch-processing-rules)
4. [Protected Fields](#protected-fields)
5. [Scene Template](#scene-template)
6. [Production Safeguards Checklist](#production-safeguards-checklist)
7. [Formatting Rules](#formatting-rules)
8. [Vague vs. Specific Direction Examples](#vague-vs-specific-direction-examples)
9. [Common Mistakes (29 Items)](#common-mistakes-29-items)
10. [Timing Troubleshooting](#timing-troubleshooting)
11. [Glossary (100+ Terms)](#glossary-100-terms)
12. [Multi-Language Scene Writing](#multi-language-scene-writing)
13. [Mode Behavior](#mode-behavior)

---

## PHASE 3 GOAL & DELIVERABLES

**Goal:** Write every scene needed for the video, with exact narration, visual direction, data viz specs, source citations, and legal flags.

**Deliverables:**
- `Batch_NN_Scenes_XX_to_YY.md` files (25 scenes per batch default)
- `MASTER_CONTEXT.md` updated per batch (consistency tracker)
- `VOICE_SCRIPT_<lang>.md` files if Q19 (Additional Languages) ≠ None

---

## SCENE COUNT FORMULA

**Default: Scene count = ceil(Q14 runtime seconds ÷ Q42 fixed scene seconds).** Shorten the last scene when the runtime is not divisible by the fixed scene duration. For VARIABLE Q42, list each duration and require their sum to equal Q14.

This matches the default FIXED 8-SECOND scene strategy. For documentary, 8-second clips align with Veo3 limits and provide a professional, data-friendly pacing.

| Video Length | Total Scenes | Estimated Batches (25/batch) |
|---|---|---|
| 5 min (300s) | ~38 scenes | 2 batches |
| 8 min (480s) | ~60 scenes | 3 batches |
| 10 min (600s) | ~75 scenes | 3 batches |
| 12 min (720s) | ~90 scenes | 4 batches |
| 15 min (900s) | ~113 scenes | 5 batches |
| 20 min (1200s) | ~150 scenes | 6 batches |

If Q42 = VARIABLE, use the per-content-type duration rules in `03_Phase2_PRODUCTION_BIBLE/MASTER_Phase2_PRODUCTION_BIBLE.md` and adjust scene count accordingly.

---

## BATCH PROCESSING RULES

1. **Default batch size: 25 scenes.** Content is fact-dense; 25-scene batches balance accuracy with throughput while the safeguards checklist runs per batch.
2. **After Batch 1 in interactive mode, pause and ask for approval. Once Batch 1 is approved, generate all remaining batches autonomously.** Do not present batches 2+ for user approval; run the Production Safeguards Checklist for each batch.
3. **Before presenting each batch, run the Production Safeguards Checklist.** Fix any failures before showing the batch.
4. **Update `MASTER_CONTEXT.md` after each batch.** Track character/company names, locations, time periods, key facts introduced, and any deviations from the production bible locks.
5. **Batch file naming:** `Batch_NN_Scenes_XX_to_YY.md`
6. **Scene numbering:** Sequential, no gaps, starting at Scene 1.
7. **Use the starter `BATCH_TEMPLATE.md`** at `Starter_Project/Phase3_SceneBreakdown/BATCH_TEMPLATE.md` as the canonical batch format.

---

## PROTECTED FIELDS

The following fields are locked after Phase 2 approval. They must not change during Phase 3 without restarting from Phase 2:

| Field | Why It Is Protected | Example |
|-------|---------------------|---------|
| **SceneNumber** | Maintains sequential order and prevents gaps or duplicate scenes. | Scene 1, Scene 2, ... |
| **Duration** | Locked by Q42 scene-duration strategy. Changing it breaks pacing and tool limits. | 8 seconds |
| **Location** | Visual continuity; locations are locked in `04_Locations.md` or production bible. | "Kodak Headquarters, Rochester" |
| **Chapter** | Narrative structure; changing chapters mid-batch breaks story logic. | "Chapter 2 — The Fall Begins" |
| **Characters** | Consistency with research bible and character/company locks. | "Kodak executives, digital camera prototype" |
| **TimeOfDay / Period** | Historical accuracy and visual continuity. | "1997 — Boardroom" |

**Rule:** If a protected field must change, stop the batch. Update the relevant Phase 2 bible file. Then regenerate the affected batches from that point forward. Do not silently edit a protected field in a single scene.

---

## SCENE TEMPLATE

Use this template for EVERY scene. No exceptions.

```markdown
---
**Scene [Number]**
**Chapter:** [Chapter name/number]
**Location:** [Specific location, archive footage, or data viz setting]
**Time of Day / Period:** [Era / Year / Specific date if relevant]
**Characters:** [People, companies, or entities present]
**Duration:** [X seconds — MUST match scene duration strategy]

**Visual Direction:**
[Specific, actionable description. Include: footage type, camera movement, on-screen text, data viz placement, B-roll, transitions.]

**Data Visualization Specs:**
[If applicable: chart type, data points, colors, animation style, source of data.]

**Dialogue / Narration:**
[Exact lines with speaker labels. NARRATOR: ... or ARCHIVE INTERVIEW: ...]

**Voiceover Duration:** [X seconds — must fit within scene duration]

**Source Citation:**
[Source name, URL, date accessed, credibility level.]

**Claim IDs:**
[C001, C002, or "Fictional scene — no factual claim". Every ID must exist in Phase 1 Claim_Ledger.md.]

**Legal Risk Flag:** [None / Low / Moderate / High — note if defamation risk]

**SFX:** [List of sound effects]

**Music Cue:** [Mood/type]

**Transition to Next Scene:** [How this scene ends and connects]

**Notes:** [Any special considerations]
```

### Example Scene

```markdown
---
**Scene 12**
**Chapter:** Chapter 2 — The Fall Begins
**Location:** Kodak boardroom, Rochester, NY
**Time of Day / Period:** 1997 — Digital camera prototype meeting
**Characters:** Kodak executives (anonymous), digital camera prototype
**Duration:** 8 seconds

**Visual Direction:**
Medium shot of boardroom table. An executive's hands place a small digital camera prototype on the table. Other executives lean back, arms crossed. Camera slowly pushes in on the prototype. On-screen text: "1997 — Kodak engineers invent the digital camera." Transition: cut to a 2000s-era retail store with film displays.

**Data Visualization Specs:**
[None for this scene]

**Dialogue / Narration:**
NARRATOR: In 1997, Kodak engineers showed executives the first digital camera. Kodak had invented it. They chose not to sell it.

**Voiceover Duration:** 7 seconds

**Source Citation:**
Source: The New York Times, "What Kodak Could Have Been," 2012. Tier 2. URL: https://www.nytimes.com/...

**Legal Risk Flag:** None

**SFX:** Camera placed on table, muffled boardroom murmur

**Music Cue:** Tense, documentary strings

**Transition to Next Scene:** Cut to retail store with film displays, establishing Kodak's continued film dominance

**Notes:** Keep executives anonymous; no named accusations. Source supports the factual claim that Kodak invented the digital camera in 1975/1997 context.
```

---

## PRODUCTION SAFEGUARDS CHECKLIST

Run this checklist BEFORE presenting any batch of scenes. No batch advances until all checks pass.

### CRITICAL CHECKS
- [ ] **Q42 Duration Strategy confirmed:** FIXED 8-SECOND or VARIABLE. Every scene duration matches strategy.
- [ ] **Voiceover Duration:** Fits within scene duration (max 8s for FIXED, or scene-duration minus 1-2s for VARIABLE).
- [ ] **Protected Fields Locked:** SceneNumber, Duration, Location, Chapter, Characters, TimeOfDay/Period match Phase 2 locks.
- [ ] **Financial Figures Verified:** Every money figure is sourced and cross-checked.
- [ ] **No Defamation:** No unverified accusations against named people/companies.
- [ ] **Sources Cited:** Every significant claim has a source citation in the scene.
- [ ] **Legal Risk Flags:** All Moderate/High risk flags addressed.

### STANDARD CHECKS
- [ ] **Character/Company Lock:** Names and roles match the research bible and production bible.
- [ ] **Voice Consistency:** Tone matches `05_Voiceover_Guide.md`.
- [ ] **Visual Style Consistency:** Matches `04_Visual_Style_Guide.md`.
- [ ] **Data Visualization Specs:** Charts have clear type, data, colors, source, and animation notes.
- [ ] **Animation/Visual Direction Specific:** No vague language like "make it dramatic" or "show something."
- [ ] **Zero Placeholders:** No `[TBD]`, `[TODO]`, `[PLACEHOLDER]`, `[INSERT]` anywhere.
- [ ] **Tone Matches Audience:** Language complexity matches Q2 (target audience).
- [ ] **Story Logic:** Every scene flows logically from the previous scene.
- [ ] **Investment Disclaimer:** Included if financial advice could be implied.
- [ ] **Controversial Claims Balanced:** Multiple perspectives included where applicable.
- [ ] **Company Names Spelled Correctly:** Verify spelling of every company and person.
- [ ] **Inflation Adjustments:** Noted where historical dollar comparisons are made.
- [ ] **AI Safety Filter:** Scene passes content safety rules (no sexual, graphic violence, hate, etc.).

### Plain-Text Scene Formatting Rules (final output)

- [ ] Plain text only inside scene blocks; no Markdown symbols
- [ ] NO Markdown headings (`###`)
- [ ] NO bold formatting (`**`)
- [ ] NO separator lines (`---`)
- [ ] Exactly 3 blank lines between the end of one scene and the beginning of the next scene
- [ ] No extra blank lines anywhere inside a scene
- [ ] No placeholder, template, or instructional text in the final output

**If any check fails:** Fix the scene(s) before presenting the batch. Do not proceed.

---

## FORMATTING RULES

- Scene number in format: `Scene 1`, `Scene 2` (no decimals, no letters).
- Two blank lines between scenes.
- Three hyphens (`---`) on their own line separating major sections within a scene.
- No markdown symbols (*emphasis*, **bold**) within scene content blocks — plain text only.
- All character/company names must match `Facts_Documented.md` and `MASTER_CONTEXT.md` exactly.
- All locations must match the research bible or production bible.
- All data viz specs must reference `06_Data_Visualization_Specs.md`.
- All source citations must be traceable to `Source_List_with_Links.md`.

---

## VAGUE VS. SPECIFIC DIRECTION EXAMPLES

### Vague (Don't Do This)
- "Show the company failing."
- "Make it dramatic."
- "Display the financial data."
- "Show the CEO looking worried."
- "Transition to the next part."

### Specific (Do This)
- "Wide shot of Kodak headquarters at dusk. On-screen text: 'Rochester, NY, 2012.' Camera slowly zooms out as the building lights flicker off one by one."
- "Animated line graph: Kodak stock price from 1990 peak ($90) to 2012 bankruptcy ($0.36). Line turns red after 2000. X-axis labeled by year, Y-axis labeled 'Stock Price (USD).'"
- "Close-up of an anonymous CEO silhouette at a boardroom table, head in hands. Lighting is low-key, documentary style. No face visible."
- "Data viz wipe transition: left-to-right wipe revealing the 2008 S&P 500 crash chart. Chart source: Bloomberg, December 2024."

---

## COMMON MISTAKES (29 ITEMS)

### Mistake 1: Unverified Financial Figures
**Wrong:** "Netflix lost $10 million last quarter" (without checking)
**Correct:** Verify against quarterly earnings report
**Why:** Wrong numbers destroy credibility permanently

### Mistake 2: Confusing Revenue with Profit
**Wrong:** "Company made $1B revenue means they earned $1B"
**Correct:** Explain that revenue comes before expenses
**Why:** These are fundamentally different concepts

### Mistake 3: No Source Attribution
**Wrong:** Claiming facts without saying where from
**Correct:** List sources in description with links
**Why:** Credibility depends on traceable sources

### Mistake 4: Misleading Financial Comparisons
**Wrong:** Comparing 1990s dollars to 2024 dollars (no inflation adjustment)
**Correct:** Adjust for inflation or note the difference
**Why:** Historical comparisons need context

### Mistake 5: Oversimplifying Failure
**Wrong:** "Netflix failed in Australia" (one reason)
**Correct:** Acknowledge multiple factors contributed
**Why:** The subject is complex; single-cause stories are false

### Mistake 6: No Legal Review for Accusations
**Wrong:** Accusing company of fraud without legal review
**Correct:** Get legal review or soften language
**Why:** Defamation liability is real

### Mistake 7: Dated Information Not Disclosed
**Wrong:** Presenting 2020 data as current without noting age
**Correct:** Date all information clearly
**Why:** The subject changes rapidly; context matters

### Mistake 8: Biased Representation
**Wrong:** Only showing negatives of Company A, only positives of Company B
**Correct:** Fair representation (strengths and weaknesses both)
**Why:** Audience loses trust if unfair

### Mistake 9: Sponsored Content Not Disclosed
**Wrong:** Promoting cryptocurrency without noting sponsorship
**Correct:** Clear disclosure at start: "This video is sponsored by..."
**Why:** Legal requirement and ethical responsibility

### Mistake 10: Stock Price Misleading
**Wrong:** Showing graph without noting stock split or wrong date
**Correct:** Annotate what data represents exactly
**Why:** Historic context essential for accuracy

### Mistake 11: No Disclaimer for Financial Information
**Wrong:** Making financial claims without disclaimer
**Correct:** "This is not investment advice" in description
**Why:** Legal protection + audience understanding

### Mistake 12: Conspiracy Theory Presented as Fact
**Wrong:** "The government orchestrated the 2008 crisis" (without evidence)
**Correct:** "Some people theorize..." OR provide actual evidence
**Why:** Separates fact from speculation

### Mistake 13: Celebrity CEO Worship
**Wrong:** Portraying Elon only as genius, ignoring controversies
**Correct:** Balanced (achievements AND failures/controversies)
**Why:** Fair representation > hero worship

### Mistake 14: Market Timing Implications
**Wrong:** "Now is the time to buy [stock]"
**Correct:** Pure historical/educational content
**Why:** Implies investment advice; legal exposure

### Mistake 15: Competitor Defaming
**Wrong:** "Competitor X is inferior/unethical" (without evidence)
**Correct:** Objective comparison or factual criticisms
**Why:** Potential legal liability

### Mistake 16: Not Explaining Financial Concepts
**Wrong:** Using jargon assuming audience understands
**Correct:** "EBITDA, which means earnings before interest, taxes, depreciation and amortization..."
**Why:** Accessibility matters; not everyone knows finance terms

### Mistake 17: Cherry-Picking Data
**Wrong:** Showing best year (2019) to claim success, ignoring 2020 disaster
**Correct:** Show full context (good and bad years)
**Why:** Selective data misleads audience

### Mistake 18: Not Updating Errors
**Wrong:** Video claims are disproven; creator ignores corrections
**Correct:** Promptly update description/video with correction
**Why:** Credibility depends on willingness to correct

### Mistake 19: Equating Correlation with Causation
**Wrong:** "Stock rose after CEO hired; therefore CEO caused rise"
**Correct:** Acknowledge other factors (market, timing, luck, etc.)
**Why:** The subject is multifactorial

### Mistake 20: Exploiting Failure for Entertainment
**Wrong:** Mocking failed startup founder; emphasizing embarrassment
**Correct:** Respectful analysis of what went wrong + learnings
**Why:** Entrepreneurship is hard; failures have real people

### Mistake 21: Ignoring Systemic Issues
**Wrong:** "He failed because he was stupid"
**Correct:** Acknowledge market conditions, timing, regulations
**Why:** Nuance reflects reality

### Mistake 22: Not Crediting Original Investigations
**Wrong:** Presenting findings from detailed journalist report as own research
**Correct:** Credit news organization that did investigation
**Why:** Integrity + legal concerns

### Mistake 23: Vague Criticism
**Wrong:** "[Company] is terrible" (no reasons why)
**Correct:** Specific factual criticisms with evidence
**Why:** Substantive criticism > emotional rants

### Mistake 24: Inconsistent Information Updates
**Wrong:** Updating some facts but not others; mixed timelines
**Correct:** Consistent information date; update all together
**Why:** Confuses audience; damages credibility

### Mistake 25: Not Acknowledging Counterarguments
**Wrong:** Presenting only one perspective on controversial topic
**Correct:** Acknowledge legitimate other perspectives
**Why:** Fair analysis > one-sided advocacy

### Mistake 26: Scene Duration Violation
**Wrong:** Generating a 12-second scene for FIXED 8-SECOND strategy, or a 4-second scene where 8-10s is required.
**Correct:** Check the Content-Type Timing Guidance table before locking scene duration. Veo3 users must enforce the 8s hard clip limit per generated segment.
**Why:** Duration violations break audience rhythm, cause awkward editing, and undermine professional pacing.

### Mistake 27: Safety Filter Bypass
**Wrong:** Allowing AI-generated content to include sexual references, graphic violence, or defamatory statements against named individuals because "the AI suggested it."
**Correct:** Every generated scene passes through the AI Safety & Content Filter Rules checklist before approval. Flagged scenes are held, not included.
**Why:** Safety violations carry legal, reputational, and platform-policy consequences.

### Mistake 28: Audio-Visual Timing Mismatch
**Wrong:** Narration runs 15 words over the visual scene duration, leaving the narrator trailing the visuals or cutting off mid-sentence.
**Correct:** At 140–160 words per minute, a 7-second scene holds about 16–19 spoken words before pauses. Plan narration word count and delivery time before writing.
**Why:** Mismatched audio and visuals create an unprofessional final product and break viewer immersion.

### Mistake 29: Wrong Tone for Audience
**Wrong:** Using casual internet slang ("This company is SO done for") for an investor-focused deep dive, or dry academic language for a general-audience startup story.
**Correct:** Match tone to audience focus (Q2):
  - General Public: Engaging, accessible, storytelling tone
  - Content Professionals: Analytical, precise, data-anchored
  - Entrepreneurs: Energetic, practical, actionable takeaways
  - Investors: Formal, quantified, risk-aware
  - Students: Educational, clear definitions, structured explanation
**Why:** Tone mismatch signals that the creator does not understand their audience.

---

## TIMING TROUBLESHOOTING

Use this section when scene timing, audio sync, or pacing issues arise during Phase 3 or Phase 4.

### Problem 1: Scene exceeds AI video tool clip limit (e.g., Veo3 8s cap)

**Symptom:** AI video generation fails or truncates when scene duration exceeds the tool's hard limit.

**Solution:**
- Split the scene into two clips at a natural narrative break.
- Ensure the audio edit spans both clips seamlessly.
- Mark both clips in the scene breakdown with clip IDs (clip-A, clip-B) and a stitching note.
- If the scene cannot be cleanly split, reduce scene duration to fit the limit or switch to standard animation for that scene.

### Problem 2: Narration runs too long for scene duration

**Symptom:** Voiceover script has more words than the allocated scene seconds can deliver at 140–160 WPM.

**Solution:**
- Trim narration to the word count target (see Audio Block Mapping in Phase 2).
- Remove redundant adjectives and filler phrases — content narration should be lean.
- If the content cannot be compressed without losing meaning, extend the scene duration by 1–2 seconds and re-check against the Content-Type Timing Guidance table.
- Do NOT speed up narration above 170 WPM for content — it undermines the professional tone.

### Problem 3: Pacing feels too fast or too slow for content type

**Symptom:** A 6s scene feels rushed for a billion-dollar acquisition story, or an 8s scene drags for a quick data reveal.

**Solution:**
- Cross-reference the scene's content type against the Content-Type Timing Guidance table in Phase 2.
- If the scene is in the wrong range for its type, adjust duration and re-verify.
- For data-heavy scenes: add 1–2s to give viewers time to read charts. Do not rush data visualization.
- For pure narrative beats (no data): you can trim by 1s without losing impact.
- Consistency within a series matters more than hitting an exact number — aim for the content-type's recommended range.

### Problem 4: File naming inconsistency causes project organization breakdown

**Symptom:** Scene files have inconsistent names across batches (e.g., `scene001.md`, `batch1_scenes.md`, `scenes.md`), making compilation and reference difficult.

**Solution:**
- Apply the file naming convention set in Q42 from Phase 0 onward.
- Batch files: `{domain-slug}-{content-title}-v{version}-batch-{NN}.md`
- Individual scene files: `scene-{NNN}.md` within each batch folder.
- Master script: `{domain-slug}-{content-title}-master-v{version}.md`
- If naming was never locked, default to Q42 default pattern: `[domain]-[title]-v[version].md`.
- Run a naming audit before Phase 4 compilation to catch and rename inconsistent files.

---

### Problem 5: Audio layers collide (dialogue, music, SFX)

**Symptom:** Voiceover is hard to hear because music is too loud, SFX mask the narrator, or the scene feels sonically cluttered. Lip-sync or data-reveal moments are lost.

**Root Cause:** All three audio layers (dialogue, music, SFX) are competing at equal volume. No audio hierarchy was established in the scene or production bible.

**Solution:**
- Establish the hierarchy: **Dialogue > Music > SFX**.
- Dialogue: 100% volume (normalized to -14 LUFS for YouTube).
- Music: 60–70% under dialogue; duck (lower) when narrator speaks, raise between phrases.
- SFX: 30–40% under dialogue; space SFX to avoid overlapping critical narration.
- Leave the final 1–2 seconds of the scene as visual-only breathing room (no new dialogue).
- Limit to 3–4 SFX per scene. If a scene has more, split them across different moments.

**Example (8-second scene):**
- 0:00–0:01: SFX — lab ambience (low, 30%)
- 0:01–0:07: Narrator at 100%, music at 60% underneath
- 0:07–0:08: Visual-only beat; music rises slightly to 70%, no dialogue

---

### Problem 6: Voiceover doesn't fit the 8-second audio block

**Symptom:** The script has 28 words for an 8-second scene, requiring 210 WPM. The narrator sounds rushed and unprofessional.

**Root Cause:** Content narration was written like a paragraph, not a 140–160 WPM audio block.

**Solution:**
- Target 18–20 words per 8-second scene.
- Trim adjectives, adverbs, and filler phrases first.
- Convert compound sentences into two short sentences or a single punchy line.
- If the idea genuinely needs more words, extend the scene to 10 seconds (VARIABLE mode) or split it into two 8-second scenes.
- Read every line aloud at 150 WPM before approving the batch.

**Before (24 words, too long):**
> "In 1975, a young engineer at Kodak built the first digital camera, and his bosses reportedly told him to keep it quiet."

**After (17 words, fits 8s):**
> "In 1975, Kodak invented the first digital camera. Management looked at it and shelved it."

---

### Problem 7: Data visualization narration races ahead of the chart

**Symptom:** The narrator describes a chart's peak while the chart is still animating. Viewers miss the data point.

**Root Cause:** Audio and visual animation are not synchronized. The chart reveal time was not planned.

**Solution:**
- Build the audio block so the narrator names the key number **after** the chart has finished animating.
- Allow 3–5 seconds for the chart animation itself.
- For an 8-second scene with a chart: animate 0–4s, narrate 4–7s, silence 7–8s.
- Use on-screen text to reinforce the number even if the viewer misses the audio.
- Example: chart line rises to the $16B peak at 4s; narrator says "sixteen billion" at 5s.
---

## GLOSSARY (100+ TERMS)

### Financial & Accounting Terms

**Acquisition:** Purchase of company by another company
**Amortization:** Spreading cost over time
**Assets:** Company resources (cash, property, equipment)
**Balance Sheet:** Financial statement of assets/liabilities
**Bankruptcy:** Legal process when company can't pay debts
**Bear Market:** Stock market decline (sustained)
**Bull Market:** Stock market rise (sustained)
**Cash Flow:** Money moving in/out of company
**CAGR:** Compound annual growth rate
**Capitalization:** Company value based on stock price
**Dilution:** Ownership reduced by new stock issuance
**EBITDA:** Earnings before interest, taxes, depreciation
**Equity:** Owner's stake in company (assets - liabilities)
**IPO:** Initial public offering (company goes public)
**Leverage:** Using debt to amplify returns
**Liabilities:** Money company owes
**Liquidity:** Ease of converting to cash
**Merger:** Two companies combine (usually equal)
**Net Income:** Profit (revenue - all expenses)
**Revenue:** Money earned (before expenses)
**Valuation:** Company's estimated worth

### Content Strategy Terms

**Model:** How company makes money
**Competitive Advantage:** What makes company unique
**Disruption:** New company/model overthrowing old
**Ecosystem:** Network of related businesses
**Moat:** Competitive protection (hard to copy)
**Pivot:** Fundamental business direction change
**Scale:** Growing business efficiently
**Supply Chain:** Process from raw materials to customer
**Synergy:** Value created by combining companies
**Vertical Integration:** Owning suppliers/distributors

### Market & Economic Terms

**Arbitrage:** Profiting from price differences
**Bubble:** Inflated asset prices (unsustainable)
**Commodities:** Basic goods (oil, wheat, metals)
**Crash:** Sudden, severe market decline
**Deflation:** General price decline (bad)
**Forex:** Foreign currency exchange
**GDP:** Gross domestic product (national output)
**Inflation:** General price rise (moderate is normal)
**Monopoly:** One company controls market
**Oligopoly:** Few companies control market
**Options:** Right to buy/sell at set price
**Recession:** Economic contraction (GDP decline)
**Short Selling:** Profit from price drop
**Speculation:** Betting on price movements
**Stagnation:** Economy neither growing nor declining

### Investment & Venture Terms

**Angel Investor:** Individual investing in early startups
**Burn Rate:** How fast startup spends money
**Cap Table:** Equity ownership breakdown
**Due Diligence:** Investigation before investment
**Earnout:** Future payment contingent on performance
**Exit Strategy:** How investor makes returns
**Funding Round:** Capital raise (Series A, B, C, etc.)
**Unicorn:** Startup valued at $1B+
**Venture Capital:** Investment in growth-potential companies
**VentureBeat:** Industry publication

### Technology Category Terms

**Agile:** Iterative development method
**API:** Interface allowing apps to communicate
**Beta:** Testing version before full release
**Blockchain:** Distributed ledger technology
**Cloud Computing:** Computing over internet
**Cryptocurrency:** Digital currency (Bitcoin, etc.)
**Disruption:** Overthrowing incumbent business
**IP:** Intellectual property (patents, trademarks)
**MVP:** Minimum viable product
**Pivot:** Business direction change
**Saas:** Software as a service (subscription)
**Tech Stack:** Technologies used in app/product

### Corporate Terms

**Board of Directors:** Company governance body
**CEO:** Chief executive officer
**CFO:** Chief financial officer
**COO:** Chief operating officer
**Corporate Governance:** Company decision-making rules
**Fiduciary Duty:** Legal obligation to act in best interest
**Hostile Takeover:** Unwanted acquisition
**Proxy Fight:** Shareholders voting out board
**Sarbanes-Oxley:** US corporate accounting law
**Shareholder:** Owner of company stock
**Stakeholder:** Anyone affected by company

### Marketing & Sales Terms

**Affiliate Marketing:** Commission-based marketing
**Branding:** Creating company identity
**CAC:** Customer acquisition cost
**Churn:** Customer loss rate
**Conversion Rate:** Percentage of visitors who buy
**CTR:** Click-through rate
**Influencer:** Person with large following promoting products
**LTV:** Lifetime value (total revenue per customer)
**Marketing Mix:** Product, price, place, promotion
**Network Effect:** Value increases as more users join
**ROI:** Return on investment
**Viral Marketing:** Content spreads rapidly organically

### Social & Labor Terms

**DEI:** Diversity, equity, inclusion
**Gig Economy:** Independent contract workers
**HR:** Human resources
**Labor Union:** Worker collective bargaining
**Minimum Wage:** Lowest legal hourly pay
**Outsourcing:** Using external companies/countries
**Remote Work:** Working from home
**Salary:** Fixed annual employee pay
**Stock Options:** Right to buy company stock
**Wage Stagnation:** Wages not rising with inflation
**Whistleblower:** Employee exposing wrongdoing

### Industry-Specific Terms

**Barista:** Coffee shop worker
**Fast Fashion:** Cheap, quickly produced clothes
**Franchise:** Licensed model
**Gig Worker:** Freelance/independent contractor
**Logistics:** Supply chain movement
**Pharma:** Pharmaceutical/drug companies
**Retail:** Direct sale to consumer
**Wholesale:** Sale to businesses (not consumers)
**Vertically Integrated:** Owning suppliers to consumers

---

## MULTI-LANGUAGE SCENE WRITING

If Q19 (Additional Languages) ≠ None:

1. Write the primary scene breakdown in English with English speaker labels (NARRATOR, ARCHIVE INTERVIEW, etc.).
2. At the end of Phase 3, generate one `VOICE_SCRIPT_<lang>.md` file per additional language.
3. In each VOICE_SCRIPT file:
   - Translate all spoken text into the target language.
   - Localize speaker labels (e.g., NARRATOR → कथावाचक in Hindi, कथनकर्ता in Marathi).
   - Transliterate character/company names into the target script when needed.
   - Translate parenthetical directions (e.g., "(excited)" → "(उत्साहित)").
4. Keep timing annotations and SFX/Music Cue references unchanged across languages.
5. Lock the language list at the end of Phase 2. Adding or removing languages after Phase 2 requires restarting from Phase 2.

---

## MODE BEHAVIOR

**Interactive:** After Batch 1, say: "**Batch 1 complete — [X] scenes. Please review and approve. Remaining batches will run autonomously.**" Wait for approval. After all batches: "**Scene Breakdown complete — Batch 1 approved; remaining batches autonomously verified. Proceeding to Phase 4 (Production Package).**"

**Autonomous:** Write all batches sequentially, run the Production Safeguards Checklist per batch, update `MASTER_CONTEXT.md` and `PROGRESS.md`, proceed to Phase 4.

---

**END OF MASTER SKILL — Phase3 Scene Breakdown**


## Expanded production workflow 1.0 handoff

For new/enrolled episodes follow CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md and PRODUCTION_WORKFLOW.json. Preserve the 16 numbered files and add all ten supporting records with explicit applicability/status in PRODUCTION_MANIFEST.json. A scaffold is incomplete. Phase 3 must resolve beat coverage, factual claim IDs, asset IDs and chapter boundaries against actual scenes. Phase 4 uses production_workflow.py compile and Package_Inputs.json; changed inputs invalidate the snapshot. Phase 5 still requires evidence and any genuine human approval; no manifest or compiler closes those gates. Legacy un-enrolled projects retain previous checks.
