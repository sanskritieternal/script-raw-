# Niche expansion: IDs 501–530

The registry now includes 30 new subject niches, each with a stable ID, taxonomy route, one CAT configuration, one NICHE identity file, an editable 20-angle plan, generated angle choices, and its own OUTPUT landing folder. The original IDs 001–500 and their curated angle plans remain in place. The 46 top-level subject tags remain unchanged; every new niche has its own category configuration through its CAT file.

## Added niches

| IDs | Areas |
|---|---|
| 501–505 | Public Health; Rehabilitation; Assistive Technology; Maternal & Child Health; Nutrition Science |
| 506–510 | Housing & Tenancy; Water & Sanitation; Waste Management; Urban Climate Adaptation; Infrastructure Maintenance |
| 511–515 | Semiconductors; Quantum Computing; Human-Computer Interaction; Open-Source Software; Internet Governance |
| 516–520 | Labor Rights; Worker Safety; Cooperatives; Poverty & Inequality; Public Budgets |
| 521–525 | Soil Science; Air Quality; Biodiversity Conservation; Food Systems; Sustainable Fisheries |
| 526–530 | Indigenous Histories; Oral History; Libraries & Archives; Translation; Media Literacy |

The additions address subjects with distinct source bases and audience questions. Similar existing niches, such as Health & Wellness Education and Sustainable Living, remain separate: the new plans define a narrower system, method, population, or discipline. The 30 exact titles and slugs were checked against the first 500 before registration.

## Wiring

- [Taxonomy](../REGISTRY/NICHE_TAXONOMY.csv) holds IDs, subjects, and paths. [Category index](../REGISTRY/CATEGORY_INDEX.md) and [niche directory](../REGISTRY/Niches/README.md) browse all 530 homes.
- The [registry extension](../REGISTRY/MASTER_REGISTRY_EXTENSION.md) and [visual extension](../REGISTRY/MASTER_VISUAL_STYLE_EXTENSION.md) supply source rows for IDs 501–530 while preserving the original 500-row files.
- [Expansion generator](../expand_niches_501_530.py) records the 30 research directions and creates their editable plans. [Materializer](../materialize_niches.py) and [angle generator](../populate_niches.py) create the CAT, NICHE, OUTPUT, and angle files. [Repository validator](../validate_repository.py) checks all registered IDs without a 500-ID ceiling.
- Historical one-time migration scripts still describe the original 500-ID transformation. They are retained as migration history and are not part of the active generation sequence.

## Editorial state

The subsequent [scope review](ANGLE_SCOPE_REVIEW.md) rewrote all 600 expansion scopes, aligned 150 field-angle questions and added a scope snapshot to new Phase 0 configurations. The later [editorial review](EXPANSION_EDITORIAL_REVIEW.md) refined the 450 base questions, checked primary source entry points and recorded neighboring-niche boundaries. The 30 plans now have `editorial_question_reviewed` status. See the [scope guide](../REGISTRY/ANGLE_SCOPE_GUIDE.md) for editing and episode use.

Each new plan has 15 stable base angles and five subject lenses: 600 candidate angles altogether. Each has a question, scope, evidence method and boundary, with a primary institutional source entry point in the plan. These directions support case research; they do not establish episode claims. The [completion checker](../verify_editorial_completion.py) now checks all 530 registered plans; `--original-500` checks the original milestone separately.

## Reproduction and checks

Run `python expand_niches_501_530.py` to reconcile the extension sources and plans, `python materialize_niches.py` for the three home files per niche, and `python populate_niches.py --sync-content` for derived angles. Then run `python populate_niches.py --verify-content`, `python validate_repository.py --progress`, `python test_contract.py`, and `python audit_repository.py`. The [production contract](../CORE/PIPELINE/CONTRACT.md) governs the resulting Phase 0 route.

The completed audit read and hashed 19,601 files. It found 530 topic directories, zero incomplete grids, and zero misnamed angle files. Full content verification found 16,616 angles with zero missing files or drift. Repository validation passed 530 CAT files, 530 NICHE files, 530 OUTPUT folders, 46 subject tags, and 46 Phase 0 pilots. All nine contract tests and both project pilots passed. A dry run of ID 530's `field_teaching_transfer` angle resolved its Phase 0 configuration without creating an episode directory.
