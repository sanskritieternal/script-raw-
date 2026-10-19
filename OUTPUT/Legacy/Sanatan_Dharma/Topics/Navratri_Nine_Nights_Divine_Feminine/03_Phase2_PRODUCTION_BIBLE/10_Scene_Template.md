# Scene Template

## Project: Navratri — The Nine Nights of the Divine Feminine

---

## Standard Scene Structure

Every scene in Phase 3 must follow this template exactly. No fields may be left empty.

```markdown
### Scene {NNN} | दृश्य {NNN}

| Field | Value |
|---|---|
| **Scene Number** | {NNN} (sequential, 3 digits) |
| **Duration** | 8 seconds (FIXED — NO exceptions) |
| **Chapter** | Act {1-5} |
| **TimeOfDay/Period** | {From timeline} |
| **Location** | {Geographic/scene location} |
| **Characters** | {Characters present in scene} |

#### Visual (दृश्य)
{Detailed visual description — what the viewer sees. From Visual Style Guide. Include camera, lighting, color, animation notes.}

#### Audio (ध्वनि)
{Full Hindi (Devanagari) narration text. From Voiceover Guide. Include music/sound note.}

#### On-Screen Text (पर्दे पर लिखित)
{Text that appears on screen — in Devanagari only. Mantras, form names, key facts.}

#### Data Visualization (डेटा विज़ुअल)
{If applicable — chart type, what data is shown, animation style. From Data Viz Specs.}

#### AI Generation Prompt (AI प्रॉम्प्ट)
{Full prompt for AI video generation tool — visual style keywords, scene description, camera, lighting, color.}

#### Source Reference (स्रोत)
{Source citation for any factual claim in narration. Format: Source # from Source_List_with_Links.md}
```

---

## Example Scene (Filled Template)

```markdown
### Scene 001 | दृश्य १

| Field | Value |
|---|---|
| **Scene Number** | 001 |
| **Duration** | 8 seconds |
| **Chapter** | Act 1 — The Cosmic Battle |
| **TimeOfDay/Period** | Cosmic / Pre-creation |
| **Location** | Cosmic realm (Triloka) |
| **Characters** | Mahishasura (demon), Devas (gods) |

#### Visual (दृश्य)
Dark cosmic void. Mahishasura — a towering figure with a buffalo head and human body — looms over a defeated group of Devas. The Devas are shown in light, compressed, looking up at the demon. Volumetric light from above illuminates the defeated gods. Cinematic 24mm wide shot, slow push-in toward Mahishasura. Color: deep indigo background, gold light from above, Mahishasura in dark silhouette.

#### Audio (ध्वनि)
महिषासुर ने कठोर तपस्या की। ब्रह्मा जी ने उसे वर दिया — न कोई मानुष और न कोई देवता ही उसे मार सकता है। (Mahishasura performed intense austerities. Lord Brahma granted him a boon — no human and no god could kill him.)

#### On-Screen Text (पर्दे पर लिखित)
महिषासुर — वर प्राप्त

#### Data Visualization (डेटा विज़ुअल)
None (narrative scene)

#### AI Generation Prompt (AI प्रॉम्प्ट)
Sacred cinematic, Devotional atmosphere, Hindu mythology, dark cosmic void, buffalo demon Mahishasura towering over defeated gods, volumetric divine light from above, deep indigo and gold color palette, 24mm wide cinematic shot, slow push-in, dramatic contrast, reverent composition, traditional Indian mythological art influence

#### Source Reference (स्रोत)
[1] Devī Māhātmya, Chapter 1-2; [8] Coburn, "Encountering the Goddess"
```

---

## Scene Writing Rules

| Rule | Specification |
|---|---|
| Numbering | Sequential, 3 digits (001, 002, ... 108) |
| Duration | Exactly 8 seconds for EVERY scene |
| Narration | Hindi (Devanagari) only — no English in narration |
| Sanskrit terms | Devanagari + transliteration + Hindi explanation on first mention |
| Visuals | Must match Visual Style Guide exactly |
| Placeholders | ZERO — no [TBD], [TODO], [PLACEHOLDER] |
| Sources | Every factual claim must have a source reference |
| Character consistency | Same characters must look consistent across all scenes |
| Color continuity | Must match locked palette (saffron, gold, vermilion, etc.) |
| Music notes | Include for every scene (sacred devotional music, silence, sound effects) |

---

## Batch Structure

- 25 scenes per batch
- Batch files named: `Batch_01_Scenes_001-025.md`, `Batch_02_Scenes_026-050.md`, etc.
- For this project (~108 scenes): 5 batches (01-025, 026-050, 051-075, 076-100, 101-108)

---

## Music/Sound Notes

| Scene Type | Music |
|---|---|
| Opening/Mythological | Sacred instrumental — bansuri, tabla, tanpura |
| Navadurga descriptions | Soft devotional — individual form theme |
| Battle scenes | Dynamic, dramatic — percussive, building |
| Regional celebrations | Region-specific folk music (Bengali, Gujarati, Tamil, North Indian) |
| Philosophy passages | Meditative, ambient — soft instruments |
| Closing | Full devotional — aarti, jai mata di chorus |
