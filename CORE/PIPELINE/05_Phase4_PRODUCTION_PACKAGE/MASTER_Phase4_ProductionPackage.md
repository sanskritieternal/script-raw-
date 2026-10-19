# MASTER SKILL — Phase4 Production Package

> Use `CORE/PIPELINE/CONTRACT.md` for current output paths and gates. Compile claim IDs and their source locations from Phase 1. Financial checks apply when the selected topic actually contains financial claims.

This phase compiles all approved scenes, sources, specs, and assets into a single production-ready document. This is the **SINGLE SOURCE OF TRUTH** for the final video.

**Inputs:** All approved `04_Phase3_SCENE_BREAKDOWN/` batch files and all `03_Phase2_PRODUCTION_BIBLE/` files.
**Outputs:** `05_Phase4_PRODUCTION_PACKAGE/Production_Package.md`.
**Quality Gate:** User approval (interactive) / internal checklist pass (autonomous) before proceeding to Phase 5.

---

## TABLE OF CONTENTS

1. [Production Package Structure](#production-package-structure)
2. [Project Summary Section](#project-summary-section)
3. [All Scenes Section](#all-scenes-section)
4. [Master Script Section](#master-script-section)
5. [Company / Person Reference Sheet](#company--person-reference-sheet)
6. [Data Visualization Specifications](#data-visualization-specifications)
7. [Source Citations Section](#source-citations-section)
8. [YouTube Metadata Section](#youtube-metadata-section)
9. [Legal Review Summary](#legal-review-summary)
10. [AI Generation Prompts (if applicable)](#ai-generation-prompts-if-applicable)
11. [Final Pre-Generation Checklist](#final-pre-generation-checklist)
12. [Mode Behavior](#mode-behavior)

---

## PRODUCTION PACKAGE STRUCTURE

The `Production_Package.md` file must contain the following sections in this order:

```markdown
# Production Package: [Topic Title]

## 1. Project Summary
## 2. All Scenes (Complete)
## 3. Master Voiceover / Dialogue Script
## 4. Company / Person Reference Sheet
## 5. Data Visualization Specifications
## 6. Source Citations by Scene
## 7. YouTube Metadata
## 8. Legal Review Summary
## 9. AI Generation Prompts (if using AI video tools)
## 10. Final Pre-Generation Checklist
## 11. Production Notes
```

---

## PROJECT SUMMARY SECTION

One-page summary at the top of the file for quick reference.

```markdown
## 1. Project Summary

**Title:** [Topic Title]
**Content Domain:** [Domain name]
**Target Audience:** [General / Professionals / Entrepreneurs / Investors / Students]
**Story Angle:** [Rise/Fall / Scandal / Innovation / Economic Analysis / Entertainment]
**Total Duration:** [X minutes X seconds]
**Total Scenes:** [Count]
**Average Scene Duration:** [X seconds]
**Visual Style:** [Chosen style from Q15]
**Voiceover Tone:** [Chosen tone from Q16]
**Primary Language:** [English / Hindi / etc.]
**Additional Languages:** [None / list]
**Video Generation Method:** [AI Video / Animation / Live Action / Hybrid]
**Content Safety Level:** [Standard / Strict / Platform-specific]
**Monetization Focus:** [Yes / Secondary / No]
**Legal Review Required:** [Yes / No — reason]
**Key Legal Flags:** [List any remaining flags]
**File Naming Pattern:** [domain]-[title]-v[version].md
```

---

## ALL SCENES SECTION

Paste every approved scene from Phase 3 into this section. Maintain the exact scene format from `03_Phase2_PRODUCTION_BIBLE/10_Scene_Template.md`.

Rules:
- Two blank lines between scenes.
- Scene order must be sequential and match the running order.
- Do not edit scene content without updating source citations and legal flags.
- If a scene was split into multiple clips for Veo3, note the clip IDs and stitching instructions.

---

## MASTER VOICEOVER / DIALOGUE SCRIPT

Extract all narration from the scenes into a clean, readable script.

```markdown
## 3. Master Voiceover / Dialogue Script

### Scene 1 — [Chapter Name]
**Duration:** 8 seconds
**Voiceover:** "[Exact narration text]"

### Scene 2 — [Chapter Name]
**Duration:** 8 seconds
**Voiceover:** "[Exact narration text]"

[Continue for all scenes...]
```

Include:
- Scene number and chapter
- Duration
- Exact voiceover text
- Speaker labels (NARRATOR, ARCHIVE INTERVIEW, etc.)
- Word count per scene (to verify WPM fit)
- Total word count and estimated runtime at 150 WPM

---

## COMPANY / PERSON REFERENCE SHEET

For quick lookup during production. Include only the key entities that appear in the video.

```markdown
## 4. Company / Person Reference Sheet

### [Company Name]
- **Full legal name:** [if different from common name]
- **Industry:** [Sector]
- **Founded:** [Year]
- **Key figures:** [CEO / Founder names]
- **Status:** [Active / Bankrupt / Acquired / etc.]
- **Stock ticker:** [if applicable]
- **Spelling notes:** [e.g., "eBay, not Ebay"]
- **Logo usage notes:** [Fair use for commentary, etc.]
- **Pronunciation notes:** [if needed for voiceover]

### [Person Name]
- **Role:** [CEO / Founder / Investor / Whistleblower]
- **Years active:** [range]
- **Pronunciation:** [if needed]
- **Living/deceased:** [status]
- **Legal risk notes:** [if any]
```

---

## DATA VISUALIZATION SPECIFICATIONS

Compile all data viz specs from the scenes into a single reference section. Include the actual data points and source information.

```markdown
## 5. Data Visualization Specifications

### Chart 1: [Title]
- **Scene(s):** [Scene numbers]
- **Chart type:** [Line / Bar / Pie / Stacked / etc.]
- **Data points:**
  - [Label]: [Value]
  - [Label]: [Value]
- **Color coding:** [Red/green/blue/gold]
- **Animation style:** [Count up / Grow / Wipe / etc.]
- **Source:** [Name + URL + date]
- **Notes:** [Any special rendering instructions]
```

---

## SOURCE CITATIONS BY SCENE

Organize all sources by scene so fact-checkers can quickly verify every claim.

```markdown
## 6. Source Citations by Scene

### Scene 1
- [Source name, URL, date, credibility tier]

### Scene 2
- [Source name, URL, date, credibility tier]

[Continue for all scenes...]
```

Also include a consolidated bibliography at the end:

```markdown
### Consolidated Bibliography

**Tier 1 — Primary Sources**
1. [Title]. [Organization]. [URL]. [Date].

**Tier 2 — Credible News/Analysis**
1. [Title]. [Publication]. [URL]. [Date].

**Tier 3 — Reputable but Verified**
1. [Title]. [Publication]. [URL]. [Date].
```

---

## YOUTUBE METADATA SECTION

```markdown
## 7. YouTube Metadata

### Title Options
**Primary:** [Title]
**Alternate 1:** [Title]
**Alternate 2:** [Title]

### Description
[200+ words. Include hook, summary, timestamps, sources, disclaimer, and CTAs.]

### Tags (15-20)
[tag1, tag2, tag3, ...]

### Hashtags
[#hashtag1 #hashtag2 #hashtag3]

### Thumbnail Concept
- **Main image:** [Describe]
- **Text overlay:** [Text]
- **Color palette:** [Colors]
- **Numbers/faces:** [What to include]

### Category
[Education / News & Politics / Entertainment / etc.]

### Monetization Settings
- [ ] Ad-friendly content confirmed
- [ ] Sponsored content disclosed (if applicable)
- [ ] Affiliate links disclosed (if applicable)
- [ ] Investment disclaimer included (if applicable)
```

---

## LEGAL REVIEW SUMMARY

```markdown
## 8. Legal Review Summary

**Legal Liability Level (Q8):** [No / Moderate / High / Critical]
**Legal Review Required:** [Yes / No]
**Legal Review Completed:** [Yes / No / N/A]
**Reviewer:** [Name or "AI preliminary review"]

### High-Risk Claims
| Scene | Claim | Risk Level | Mitigation |
|---|---|---|---|
| [X] | [Claim] | [High] | [Softened language / sourced / legal review] |

### Disclaimers Included
- [ ] Educational disclaimer (not investment advice)
- [ ] Controversy warning
- [ ] Sponsored content disclosure
- [ ] Affiliate link disclosure
- [ ] Other: [specify]

### Language Softening Log
- [Original wording] → [Revised wording] → [Reason]
```

---

## AI GENERATION PROMPTS (IF APPLICABLE)

If the video uses AI video/image generation (Q40 = AI Video), provide ready-to-copy prompts per scene.

```markdown
## 9. AI Generation Prompts

### Scene 1 — [Title]
**Tool:** [Veo3 / Seedance / Kling / etc.]
**Duration:** [8 seconds]
**Prompt:**
"[Detailed, specific prompt matching the visual direction. Include style, lighting, camera movement, characters, mood, and any text/graphics.]"

**Negative prompt:** [What to avoid]
**Style reference:** [Matches Visual Style Guide]
**Notes:** [Any special instructions]
```

Prompt rules:
- Reference the visual style guide from Phase 2.
- Avoid vague language.
- Include camera direction where applicable.
- Do not include defamatory, sexual, violent, or hateful content.
- For scenes with named public figures, follow the AI safety rules (describe generically or use archival footage instead of generation if risky).

---

## FINAL PRE-GENERATION CHECKLIST

Run this checklist before declaring the package complete:

```markdown
## 10. Final Pre-Generation Checklist

- [ ] All 42 config questions reviewed and locked
- [ ] Scene duration strategy locked (Q42)
- [ ] All scene durations verified
- [ ] Research Bible approved
- [ ] Production Bible approved
- [ ] Batch 1 approved; remaining batches autonomously verified
- [ ] All scenes in correct order, no gaps
- [ ] Character/company names spelled consistently
- [ ] No placeholders remaining ([TBD], [TODO], [PLACEHOLDER])
- [ ] Voiceover durations fit within scene durations
- [ ] Master script generated and reviewed
- [ ] All applicable financial figures verified and sourced; otherwise marked not applicable with reason
- [ ] All sources cited with URLs and dates
- [ ] Legal review completed (if required)
- [ ] Required disclaimers included in metadata
- [ ] Data visualization specs finalized with source data
- [ ] Thumbnail concept and title finalized
- [ ] YouTube description, tags, and hashtags ready
- [ ] AI generation prompts ready (if applicable)
- [ ] File naming convention applied to all outputs
- [ ] Production notes included for tricky scenes
```

---

## PRODUCTION NOTES

```markdown
## 11. Production Notes

[Any last-minute guidance: priority scenes, tricky scenes, style references, known challenges, revision history, etc.]
```

---

## MODE BEHAVIOR

**Interactive Mode:** Present the completed Production Package. Say: "**Production Package complete — please review and approve to proceed to Phase 5 (Final Audit).**" Wait for user approval.

**Autonomous Mode:** Write the Production Package, run the internal checklist, mark Phase 4 complete in `PROGRESS.md`, proceed to Phase 5.

---

**END OF MASTER SKILL — Phase4 Production Package**


### Plain-Text Scene Formatting Rules (final output)

- [ ] Plain text only inside scene blocks; no Markdown symbols
- [ ] NO Markdown headings (`###`)
- [ ] NO bold formatting (`**`)
- [ ] NO separator lines (`---`)
- [ ] Exactly 3 blank lines between the end of one scene and the beginning of the next scene
- [ ] No extra blank lines anywhere inside a scene
- [ ] No placeholder, template, or instructional text in the final output


## Expanded production workflow 1.0 handoff

For new/enrolled episodes follow CORE/PIPELINE/03_Phase2_PRODUCTION_BIBLE/WORKFLOW_GUIDE.md and PRODUCTION_WORKFLOW.json. Preserve the 16 numbered files and add all ten supporting records with explicit applicability/status in PRODUCTION_MANIFEST.json. A scaffold is incomplete. Phase 3 must resolve beat coverage, factual claim IDs, asset IDs and chapter boundaries against actual scenes. Phase 4 uses production_workflow.py compile and Package_Inputs.json; changed inputs invalidate the snapshot. Phase 5 still requires evidence and any genuine human approval; no manifest or compiler closes those gates. Legacy un-enrolled projects retain previous checks.


## Idea snapshot handoff

If CONFIG includes a selected episode idea, use its frozen question/case/source leads as planning context, not as a verified claim ledger. The live bank may change independently. Complete Phase 1 evidence before factual scripting and preserve the CONFIG snapshot during package compilation. Its hash and angle/story consistency are checked by project validation; later bank edits alone do not invalidate a correct episode snapshot.
