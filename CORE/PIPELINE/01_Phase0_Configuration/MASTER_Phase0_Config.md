# Phase 0 — Configuration (schema 5.0)

When an optional niche `Planning/DEPTH_PLAN.json` exists, use its bounded topics and proposed series to select a concrete idea. Follow `REGISTRY/DEPTH_PLANNING_GUIDE.md`; series membership cannot override idea readiness. Planning adds no configuration questions. Select ready ideas through the existing --idea-id route, retaining CONFIG's immutable idea snapshot.

Resolve a stable niche ID through `REGISTRY/NICHE_TAXONOMY.csv`, load `REGISTRY/Niches/<ID>_<Slug>/CAT_<ID>_<Slug>.md`, then the selected topic preset. Explicit project answers have the highest precedence. The canonical machine-readable definitions are in `REGISTRY/CONFIG_SCHEMA.json`; the path and handoff are in `CORE/PIPELINE/CONTRACT.md`.

Use `python -m Tools.projects.create_project --id <ID> --angle <slug> --dry-run` to validate the merge and runtime before writing. A real project also needs `--story-question "...?"` so an angle preset becomes a specific researchable episode. The output is `OUTPUT/<ID>_<Slug>/<ID>_<Slug>_<Angle>_<EpisodeSlug>/01_Phase0_Configuration/CONFIG.md`. Record schema version and answer provenance.

Q14 must be an exact number of seconds. Q42 must specify a fixed number of seconds or a complete variable scene plan. Q21 is Graphics Requirement; Q24 is Source Quality Requirements. Q1 is the subject category, while Q3 is the story angle. Q15 visual style does not determine Q40 generation method.

The selected angle's Editorial scope is copied into new CONFIG files as planning guidance. Read its focus, coverage, evidence directions and limits, then choose the episode's concrete case, source or work and relevant place, population, version or period. The actual story question and Phase 1 research summary record that choice. Scope is metadata alongside Q1-Q42.

| ID | Canonical question | Default |
|---|---|---|
| Q1 | Content Category | From taxonomy |
| Q2 | Target Audience | General Public |
| Q3 | Primary Story Angle | Educational Explainer |
| Q4 | Content Depth Level | Moderate |
| Q5 | Visual/Media Priority | Moderate |
| Q6 | Interview/Documentation Segments | Quotes Only |
| Q7 | Content Sensitivity Level | Moderate |
| Q8 | Legal/Accuracy Concern | Moderate |
| Q9 | Subject Focus | Topic-Driven |
| Q10 | Contested Facts Included | No contested claims |
| Q11 | Expertise Level Required | General knowledge |
| Q12 | Comparative Content | No comparisons |
| Q13 | Monetization Priority | Secondary |
| Q14 | Total Duration | 600 seconds |
| Q15 | Visual Style Primary | Documentary Realism |
| Q16 | Voiceover Approach | Engaging Storytelling |
| Q17 | Delivery Format | Single video |
| Q18 | Primary Language | EN |
| Q19 | Additional Languages | None |
| Q20 | On-Screen Text Strategy | Moderate |
| Q21 | Graphics Requirement | Important |
| Q22 | Ending Tone | Reflective/Thoughtful |
| Q23 | Accuracy Priority | Mixed audience |
| Q24 | Source Quality Requirements | High |
| Q25 | Update Frequency | As-needed |
| Q26 | Platform Distribution | YouTube + Shorts/Reels |
| Q27 | Production Quality Level | Premium |
| Q28 | Audience Geographic Focus | Global |
| Q29 | Factual Verification Timeline | Standard (3-7 days) |
| Q30 | Expert/Access | No interviews |
| Q31 | Controversial Content Level | No controversial claims |
| Q32 | Comparative/Fairness Level | No comparisons |
| Q33 | Current Events Included | Historical only |
| Q34 | Bias Prevention Strategy | Acknowledge limitations, show multiple perspectives, cite sources |
| Q35 | Sponsored Content | No sponsorships |
| Q36 | Monetization Revenue Model | AdSense revenue |
| Q37 | Series/Playlist Strategy | Themed playlist |
| Q38 | SEO Keyword Priority | Specific topic/subject names |
| Q39 | Content Warning/Disclaimer Needed | No warnings |
| Q40 | Video Generation Method | Hybrid |
| Q41 | Content Safety Level | Standard |
| Q42 | Scene Duration Strategy | FIXED 8-SECOND |

High/Critical Q8 or Strict/Critical Q41 requires human review before publication status. An agent may draft further material, but cannot record the review as passed without evidence. Phase 0 defaults are planning decisions, never verified research claims.

## Configurable project output

Read the workspace-root `output.md` before creating a new video project. Its `output_root:` value is the single shared default destination; blank or absent means the system folder's `OUTPUT` directory. The creator resolves it through `Tools.projects.output_location.resolve_output_root`. An explicit destination/`--output-root` overrides it for one project. Relative roots resolve from the system folder. Preserve `<configured root>/<niche ID_slug>/<specific project>/` and all phase subfolders; do not use the niche ID as an episode number.

Once a project exists, use its actual supplied path for every research, production, scene, package, audit, status and review file. Compile/migrate/validate commands receive that actual project path. A later setting change affects new projects and does not relocate or duplicate ongoing work. Project-local citations/links remain relative to the project; templates and registry/catalog files stay in this workspace. `OUTPUT` in older examples/catalog views denotes the default root or an existing location, not an instruction to ignore output.md.

Run `python -m Tools.projects.create_project --id <ID> --angle <registered angle> --dry-run` to inspect the configured destination without writing. Supply `--output-root "<folder>"` only for an intentional one-project override. Unknown/malformed settings report an error; do not silently save somewhere else.
