# V6 production agent — schema 5.0

Follow the repository-root [CLAUDE.md](../../CLAUDE.md). Read the current [production contract](../PIPELINE/CONTRACT.md) first. The taxonomy has 46 subject categories and the production pipeline has six phases, numbered 0–5. Historical agent instructions are kept under `AUDIT/Legacy_Instructions/`.

Resolve every new project by stable niche ID from `REGISTRY/NICHE_TAXONOMY.csv`, its CAT file in `REGISTRY/Niches/<ID>_<Slug>/`, and a Q3 angle file in its `Angles/` folder. Its NICHE file records identity and planning links. `REGISTRY/CONFIG_SCHEMA.json` defines Q1–Q42.

## Modes

- Interactive: ask only for decisions not already supplied, show the resolved 42 answers, and request approval after Phases 1, 2 and 4 and after the first Phase 3 batch.
- Domain preset: use the current subject preset as defaults, show overrides to the user, and use the same approval gates.
- Autonomous: resolve defaults and generate drafts without routine questions. It cannot certify unsourced claims or bypass human review for High/Critical Q8, Strict/Critical Q41, sensitive living-person allegations, medical or financial advice, or material contested claims.

## Operating sequence

1. `python -m Tools.validation.validate_repository` checks the source registry. Choose an ID from `REGISTRY/NICHE_TAXONOMY.csv` and preview with `python -m Tools.projects.create_project --id <ID> --angle <angle_slug> --dry-run`; then supply a specific `--story-question "...?"` when creating CONFIG. It never overwrites an existing CONFIG.
2. Execute Phases 0 through 5 in order using `CORE/PIPELINE/CONTRACT.md` and the corresponding `MASTER_Phase*.md` source. Keep the project under `OUTPUT/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/`.
3. Use `Claim_Ledger.md` to connect material research claims to sources and scenes. A topic preset contains planning defaults, not verified facts.
4. Lock Q3, Q15, Q16 and Q42 after Phase 2 approval. If a lock changes, regenerate affected downstream work.
5. Issue a completion certificate only after Phase 5 has no blocking findings. A completed text package does not prove assets were rendered or published.

Preserve legacy outputs under `OUTPUT/Legacy/`. Do not treat them as schema 5.0 projects.
