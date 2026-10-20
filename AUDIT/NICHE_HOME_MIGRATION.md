# ID-first niche home migration — schema 5.0

> This records the 7,500-angle base migration. The later all-niche expansion brings the current total to 16,016; see `AUDIT/ALL_NICHE_ANGLE_EXPANSION.md`.

## Decision and active layout

Every one of the 500 stable niche IDs now has one independent home:

```text
REGISTRY/Niches/<ID>_<Slug>/
  CAT_<ID>_<Slug>.md          editable Q1–Q42 defaults
  NICHE_<ID>_<Slug>.md        identity and planning links; no Q answers
  Angles/
    ALL_TOPICS_BY_NICHE.md
    <ID>_<Slug>_<Angle>.md    15 Q3-only angle choices
OUTPUT/<ID>_<Slug>/
  README.md
  <ID>_<Slug>_<Angle>_<EpisodeSlug>/
```

The 46 subject categories remain taxonomy tags and schema seed overrides. They are useful for browsing but have no competing active CAT files. Runtime precedence is taxonomy Q1, niche CAT Q defaults, selected angle Q3, explicit episode override. `create_project.py` records provenance in CONFIG.

## Migration and preservation

The old 500 niche Q files became 500 CAT files; identity files were created separately. The 7,500 angle files were reduced to Q3-only choices, with their earlier complete content preserved in `AUDIT/Niche_Home_Migration_2026-10-16/Schema4_Files.zip`. The backup directory also holds pre-migration taxonomy, schema, path maps and category index. `REGISTRY/NICHE_HOME_PATHS.csv` maps every old topic, niche and output path to its new home. `REGISTRY/LEGACY_TOPIC_PATHS.csv` and `REGISTRY/LEGACY_TOPIC_DEFAULTS.csv` point to current angle paths.

Existing projects were moved to ID-first parents and their CONFIG references were updated to schema 5. The full physics pilot remains under `AUDIT/PILOTS/343_physics/`; the Shaktism Phase 0 project remains under `OUTPUT/275_shaktism/`. Historical `OUTPUT/Legacy/` content was left intact.

## Rebuild and checks

- `python -m Tools.registry.materialize_niches` creates missing CAT, NICHE and output landing files. It never overwrites an edited CAT. `--verify-content` checks identities and landing files; the repository validator checks CAT labels and values.
- `python -m Tools.registry.populate_niches --verify-content` verifies 7,500 Q3 choices and 500 angle indexes. `--create-missing` creates absent files only.
- `python -m Tools.validation.validate_repository` checks counts, stable IDs, taxonomy mapping, CAT structure, angle content, output landings and 46 Phase 0 routing pilots.
- `python -m Tools.validation.validate_project <project> --through 5` checks a project's completed phase structure.
- `python -m Tools.validation.audit_repository` refreshes byte-read verification and the structural audit.

The former `reconcile_config_presets.py` and `restructure_categories.py --apply` are historical schema migrations and are guarded against running on schema 5. Earlier audit reports are historical snapshots. The active contract is `CORE/PIPELINE/CONTRACT.md`.

## Remaining editorial work

The 15 angles per niche are generic planning patterns, not 7,500 researched, distinct episode ideas. A producer should choose a specific researchable story question, confirm sources and refine CAT values for that niche. The 46 subject tags are a reviewed structural grouping; judgment about topic boundaries and overlapping niches still needs editorial review. The validators establish file and routing consistency, not factual accuracy or finished video assets.
