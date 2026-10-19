# INVOKE_COMMANDS.md — V6 Slash Command Reference

> All commands the AI understands. Each is a single-user message that triggers a structured action.

---

## Navigation

| Command | Purpose |
|---|---|
| `/help` | Show this command list |
| `/mode` | Switch between Interactive / DomainPreset / Autonomous |
| `/list_categories` | List all 6 content categories |
| `/list_niches <category>` | List all niches in a category |
| `/search_niche <query>` | Search across the entire registry for a niche, topic, or keyword |
| `/pick_niche <niche_id>` | Load a niche and auto-generate CONFIG.md |
| `/progress` | Show progress for current category |
| `/progress_all` | Show progress across all 6 categories |

---

## Phase Runners

| Command | Purpose |
|---|---|
| `/run_phase0` | Run Phase 0 — configure the current niche (42 questions) |
| `/run_phase1` | Run Phase 1 — Research Bible (6 files) |
| `/run_phase2` | Run Phase 2 — Production Bible (16 files) |
| `/run_phase3` | Run Phase 3 — Scene Breakdown (Batch 1 first, then 25/batch) |
| `/run_phase4` | Run Phase 4 — Production Package |
| `/run_phase5` | Run Phase 5 — Final Audit (70-point checklist) |
| `/audit` | Shortcut for `/run_phase5` |
| `/run_all` | Run all remaining phases in sequence (auto-mode only) |

---

## File Operations

| Command | Purpose |
|---|---|
| `/view <phase>` | View the output of a phase (e.g., `/view 1` shows Phase 1 output) |
| `/edit <phase>` | Open a phase for user edits before approval |
| `/approve <phase>` | Mark a phase as approved and advance to next |
| `/reject <phase>` | Reject current phase and regenerate with feedback |
| `/skip <phase>` | Skip a phase (auto-mode only — not recommended) |

---

## Registry Operations

| Command | Purpose |
|---|---|
| `/add_niche <category>` | Create a new niche file from scratch |
| `/edit_niche <niche_id>` | Edit a niche's metadata file |
| `/load_preset <category>` | Load Q2-Q42 preset for a category |
| `/save_preset <category>` | Save current Q1-Q42 answers as the category preset |
| `/reload_registry` | Rebuild `MASTER_REGISTRY.md` index from niche files |

---

## Batch Manager

| Command | Purpose |
|---|---|
| `/batch_start` | Start a new batch in Phase 3 |
| `/batch_view <n>` | View scene batch number N |
| `/batch_edit <n>` | Edit batch N |
| `/batch_approve <n>` | Approve batch N (auto-mode: auto-approve after Batch 1) |
| `/batch_resize <n>` | Change batch size (default 25 scenes) |

---

## Autonomous Loop

| Command | Purpose |
|---|---|
| `/start_autonomous` | Switch to autonomous mode and run the full queue |
| `/pause` | Pause the autonomous loop (saves state) |
| `/resume` | Resume the autonomous loop |
| `/stop` | Stop the autonomous loop entirely |
| `/sync` | Sync state across all categories |

---

## Usage Examples

```
/list_categories
→ Lists: Business_Money, Sanatan_Dharma, Cartoon_Animation, Documentary, AI_Film, Science_Future

/list_niches Business_Money
→ Shows all 800 Business_Money niches (40 domains × 20 topics)

/search_niche "Kodak"
→ Finds the Kodak niche in Business_Money and shows its file path

/pick_niche D01_Topic01_Kodak
→ Loads the niche metadata, generates CONFIG.md, opens Phase 0 questions

/run_phase0
→ Runs the 42-question configuration flow for the current niche

/approve 1
→ Approves Phase 1 output and unlocks Phase 2

/run_all
→ Auto-mode: runs Phase 1 → 5 in sequence, batch-approving as it goes
```

---

## Command Parameter Format

- **Niche IDs:** `<DomainCode><TopicNumber>_<Slug>` (e.g., `D01_Topic01_Kodak`, `S03_Topic05_Ramayana`)
- **Categories:** `<CategoryName>` (e.g., `Business_Money`, `Sanatan_Dharma`)
- **Phases:** `0` to `5` (single digit)
- **Batches:** Scene batch number `1`, `2`, `3`, ...

---

## Safe Defaults

If a command is missing parameters, the AI asks for clarification before executing.
If a command would overwrite existing files, the AI prompts for confirmation first.
The `/run_all` command is **only** available in Autonomous mode.
