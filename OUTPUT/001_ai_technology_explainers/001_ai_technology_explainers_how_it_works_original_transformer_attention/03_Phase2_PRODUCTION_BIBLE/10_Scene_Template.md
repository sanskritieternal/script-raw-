# Episode scene format
Phase 3 instantiates 75 actual scenes in three batches of 25. The entries in PRODUCTION_MANIFEST.json (narration_plan) are planned cue/scene slots, not completed scene records.

## Required fields and source of values
| Field | Episode decision |
|---|---|
| Scene number / duration | Planned slot number; 8 seconds |
| Chapter | Matching STORY_BEAT_MAP.md section |
| Location | WORLD-01 editorial workspace; BOARD-01 for numbers |
| Time of Day / Period | Timeless explanatory set; source history and later research attributed separately |
| Characters | Abstract A/B/C markers when applicable; narrator off-screen |
| Visual Direction | One primary operation, defined continuity and reference asset IDs |
| Data Visualization Specs | Exact applicable stage from 06_Data_Visualization_Specs.md, or a justified absence of numerical graphics |
| Dialogue / Narration | Exact matching cue from 11_Dialogue_Script.md |
| Voiceover Duration | Planned fit within 8 seconds; actual measurement Pending generation |
| Claim IDs / Source Citation | Cue claim IDs and exact ledger source locator; editorial-only question explicitly identified |
| Legal Risk Flag | Attribution/interpretation scope when relevant; human release review remains Pending |
| SFX / Music Cue | Sparse and subordinate to speech, with silent arithmetic holds |
| Transition to Next Scene | Continuity-preserving cut or simple reveal |
| AI generation prompt | Scene-linked prompt, reference IDs, motion, exclusions, intended start/end state |
| Asset IDs | Planned register references, later mapped in manifest |

Editorial-only scenes must state that they add no factual assertion; do not invent a claim ID. Factual overlays must carry the same evidence references as narration.

## Worked planned slot 33
Eight-second BOARD-01 shot; A/B/C remain ordered. Highlight B value (0,4) and weight 1/4, then reveal its contribution (0,1). Keep A's prior contribution visible and C unchanged. Narration uses cue 33. Claims C011/C012, S1 equation 1 plus local arithmetic. Use G03, G04 and V01 references. No camera move during the equation; transition to the sum. This is a filled planning example, not rendered scene evidence.

## AI prompt recipe
“WORLD-01, BOARD-01, original abstract vector markers, fixed overhead framing, one controlled reveal, high contrast, stable empty overlay zones. Preserve A square / B circle / C triangle positions. No lettering, numerals, researcher likeness, logos, photographic evidence or interface screenshots. Start and finish in the states defined by this scene's editorial layer.”

At generation, adapt duration/input syntax to the selected provider's current capabilities. Record actual tool/version/settings; split clips if needed while preserving the parent scene's eight-second editorial timing.
