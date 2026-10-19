# Resolution of the 11 earlier category presets

> Historical crosswalk for the original 11 format-mixed presets. The current taxonomy has 46 active subject presets; see `ALL_CATEGORY_RESTRUCTURE.md` for the current routing.

The earlier `CAT_*.md` files mixed subject, story angle, visual format and audience. They therefore cannot serve as parallel primary categories. All 11 originals are preserved in `AUDIT/Legacy_Instructions/Category_Presets/`. The root of `REGISTRY/Categories/` contains the 14 schema 3.0 subject presets, while its `Niches/` subtree contains 500 niche presets. `create_project.py` selects a current subject and niche from the 500-ID taxonomy, then reads its topic angle and explicit project answers; it does not load these archived files.

| Earlier preset | Current subject routing or treatment |
|---|---|
| `CAT_BusinessStories` | `Business_Economy`; rise/fall and case-study treatment is an angle, not a subject. |
| `CAT_IndustryMarkets` | Mostly `Business_Economy`; a specific technology, health or historical story follows its niche ID's subject. |
| `CAT_InnovationTech` | Mostly `Technology_Engineering`; business impact can route to `Business_Economy` by niche ID. |
| `CAT_LuxuryConsumer` | `Business_Economy`, `Culture_Arts` or `Lifestyle_Making` according to the niche; luxury is an audience/subject focus. |
| `CAT_PeoplePersonalities` | Biography subjects route by niche ID; personality focus is a project choice, not a primary category. |
| `CAT_WorkplaceLabor` | `Society_Politics` or `Business_Economy` according to niche; labor treatment is an angle. |
| `CAT_ScandalsFraud` | Usually `Business_Economy` or `Society_Politics`; allegations trigger source and human review gates. |
| `CAT_ScienceExplainer` | Usually `Science_Nature`; its earlier `Applies to` list also covered history and crime, which route by their own subjects. Explainer is a format. |
| `CAT_SanatanDevotional` | `Religion_Philosophy`; mythological animation can also use `Media_Creative` or `Children_Education` by niche. Devotional framing is project specific. |
| `CAT_CartoonKids` | `Children_Education` for children's learning; fiction/animation may route to `Media_Creative`. Cartoon style and child audience are project choices. |
| `CAT_AIDrama` | `Media_Creative` for narrative films or `Technology_Engineering` for AI technology subjects. AI video is a generation method. |

The table is a conceptual crosswalk, not a bulk reassignment. The exact primary category for every stable ID is in `REGISTRY/NICHE_TAXONOMY.csv`. Previous topic answer strings are in `REGISTRY/LEGACY_TOPIC_DEFAULTS.csv`; the archived category files retain their full original defaults. Schema 3.0 deliberately does not copy old Q4-Q42 values blindly because several question meanings changed and old duration ranges cannot satisfy the exact timing gate.

For a new episode, choose the niche ID, angle and specific story question, then inspect the resolved CONFIG. Set format, audience, language, visual treatment and duration through explicit Q-ID overrides when the default does not fit. This matters especially for children's animation: the subject preset alone does not imply a cartoon visual style or short runtime. Use `--dry-run` and project validation before production.
