# 007 — AI Tools / AI Tutorials: main topic bank

Updated: 2026-10-22 · **110 active BANK proposals · 4 categories · 21 subcategories.**

Category → subcategory → specific video question → individual coverage scope. These are proposals, not researched scripts, verified sources or production approvals. Counts have no quota or implied maximum. Existing local queue/completion/trend fields remain separate historical tracking records.

[Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Status and reconciliation](TOPIC_BANK_RECONCILIATION.md) · [Existing production report](TOPICS_COVERED_REPORT.md) · [All-niche bank index](../ALL_NICHE_TOPIC_BANKS.md) · [Registry planning guide](../../REGISTRY/DEPTH_PLANNING_GUIDE.md)

## Learning progression

Read foundation questions first, then intermediate mechanisms and context, then advanced comparisons, uncertainty and disputed interpretations. Within each category the subcategories follow that progression. BANK IDs preserve identity and do not imply learning order. Prerequisite links are retained where provided by the original bank.

- **Foundation:** [Choosing and testing tools](#catalog-007-d01) → [Local model installation and environment checks](#catalog-007-e01) → [Named local-runtime tutorial plans](#catalog-007-e09).
- **Intermediate:** [Writing and document workflows](#catalog-007-d02) → [Image-generation workflows](#catalog-007-d03) → [Video generation and continuity](#catalog-007-d04) → [Voice, transcription and music](#catalog-007-d05) → [Coding and automation](#catalog-007-d06) → [Local workflow quality and resource limits](#catalog-007-e02) → [Retrieval and personal-document workflows](#catalog-007-e03) → [Research, spreadsheets and data workflows](#catalog-007-e04) → [Creator pipelines from brief to delivery](#catalog-007-e05) → [Coding assistants and development projects](#catalog-007-e06) → [Document and spreadsheet failure test sets](#catalog-007-e10) → [Audio, video and creator export diagnostics](#catalog-007-e11).
- **Advanced:** [Data, privacy and portability](#catalog-007-d07) → [Reliability and tutorial maintenance](#catalog-007-d08) → [Automation, connectors and persistent work](#catalog-007-e07) → [Evaluation, exports and switching tools](#catalog-007-e08) → [Reproducible migrations and changing providers](#catalog-007-e12) → [Accessibility and multilingual end-to-end validation](#catalog-007-e13).

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [Tool choice, local setup and maintenance](#domain-007-g01) | 16 | 5 | 14 |
| [Documents, data and retrieval](#domain-007-g02) | 0 | 22 | 5 |
| [Creative media workflows](#domain-007-g03) | 0 | 27 | 0 |
| [Code, automation and inclusive validation](#domain-007-g04) | 0 | 10 | 11 |

<a id="domain-007-g01"></a>
## Category: Tool choice, local setup and maintenance

<a id="catalog-007-d01"></a>
### Choosing and testing tools

Subcategory `CATALOG-007-D01` · foundation.

<a id="bank-007-013"></a>
#### BANK-007-013 — How can a creator turn an AI tool comparison into a repeatable test?

**Individual coverage scope:** Define the task, input set, success criteria, versions, settings and failure log before selecting attractive examples.

<a id="bank-007-014"></a>
#### BANK-007-014 — What does a free AI plan actually allow a complete workflow to finish?

**Individual coverage scope:** Test quotas, exports, watermarks, commercial terms and repeat attempts on a dated plan rather than comparing only advertised access.

<a id="bank-007-015"></a>
#### BANK-007-015 — When is a local AI tool a practical alternative to a cloud service?

**Individual coverage scope:** Compare actual hardware, setup effort, privacy, quality, maintenance and end-to-end time on the same task.

<a id="bank-007-016"></a>
#### BANK-007-016 — How should a tutorial record model and application versions?

**Individual coverage scope:** Preserve settings, dates, interface changes and reproducible inputs so viewers can identify why their results differ.

<a id="bank-007-017"></a>
#### BANK-007-017 — What makes an AI-generated example cherry-picked?

**Individual coverage scope:** Report attempts, rejected outputs and selection criteria; distinguish illustrative success from representative performance.

<a id="bank-007-117"></a>
#### BANK-007-117 — Which prompt changes improve a fixed task across repeated runs rather than one cherry-picked answer?

**Individual coverage scope:** Choose a named model version, task set and scoring rubric, then compare instruction wording, examples and output constraints one variable at a time. Record failures, costs and run-to-run variation; do not promise a universal list of techniques that always works.

<a id="catalog-007-e01"></a>
### Local model installation and environment checks

Subcategory `CATALOG-007-E01` · foundation.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-053"></a>
#### BANK-007-053 — How can a tutorial verify that a local model server is actually running?

**Individual coverage scope:** Inspect official versioned setup instructions and a harmless health check; distinguish process startup from successful inference.

<a id="bank-007-054"></a>
#### BANK-007-054 — What should be recorded before troubleshooting a local AI installation?

**Individual coverage scope:** Capture operating system, runtime, application version and redacted error messages.

<a id="bank-007-055"></a>
#### BANK-007-055 — How can model download failure be separated from insufficient memory at inference time?

**Individual coverage scope:** Compare logs, file integrity and resource observations using official diagnostics.

<a id="bank-007-056"></a>
#### BANK-007-056 — What does a model's runtime compatibility require beyond its filename?

**Individual coverage scope:** Verify architecture, format, tokenizer and supported features in current documentation.

<a id="bank-007-057"></a>
#### BANK-007-057 — How can a creator test CPU-only inference before buying hardware?

**Individual coverage scope:** Use a bounded representative task and measured latency; leave purchase decisions to dated comparisons.

<a id="bank-007-058"></a>
#### BANK-007-058 — What must be checked before exposing a local AI server to another device?

**Individual coverage scope:** Inspect authentication, network scope and official security guidance; exclude public unauthenticated deployment.

<a id="catalog-007-e09"></a>
### Named local-runtime tutorial plans

Subcategory `CATALOG-007-E09` · foundation.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-096"></a>
#### BANK-007-096 — How can an Ollama tutorial test model availability separately from chat-template behavior?

**Individual coverage scope:** At production, record the actual Ollama version, official model documentation, local list and a minimal request using harmless text; plan separate checks for model loading and role formatting rather than assuming every model supports identical options.

<a id="bank-007-097"></a>
#### BANK-007-097 — How can a llama.cpp tutorial verify that its selected backend is actually doing the computation?

**Individual coverage scope:** Pin the tested release, build options, hardware and official logs; compare a small controlled run and resource evidence without using a GPU usage screenshot alone as proof of complete offload.

<a id="bank-007-098"></a>
#### BANK-007-098 — What should an LM Studio model-import lesson verify before declaring a downloaded file compatible?

**Individual coverage scope:** Record application version, model architecture, file provenance and official supported-runtime guidance; keep the proposed steps provisional until executed on the specified system.

<a id="bank-007-099"></a>
#### BANK-007-099 — How can a Whisper transcription lesson expose errors that a fluent paragraph conceals?

**Individual coverage scope:** Use licensed or consented audio with an aligned reference including names, numbers and overlapping speech; record the exact implementation, model and language settings without claiming a successful test before running it.

<a id="catalog-007-e02"></a>
### Local workflow quality and resource limits

Subcategory `CATALOG-007-E02` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-059"></a>
#### BANK-007-059 — How can context length be increased without misreading a memory-allocation failure?

**Individual coverage scope:** Record runtime settings, model variant and resource use on an actual supported setup.

<a id="bank-007-060"></a>
#### BANK-007-060 — How should a local-model tutorial compare several quantized files?

**Individual coverage scope:** Use the same prompts, precision disclosures and task-specific review; avoid size-only quality rankings.

<a id="bank-007-061"></a>
#### BANK-007-061 — What does a controlled batch test reveal about a local model's usability?

**Individual coverage scope:** Measure failures, latency and review effort rather than displaying only successful answers.

<a id="bank-007-062"></a>
#### BANK-007-062 — How can a workflow resume after a local model process restarts?

**Individual coverage scope:** Preserve external task state, inputs and completed outputs in a disposable example.

<a id="bank-007-063"></a>
#### BANK-007-063 — Why can an application show a model as connected while a specific feature still fails?

**Individual coverage scope:** Check endpoint compatibility, authentication and supported tool or image capabilities.

<a id="catalog-007-d08"></a>
### Reliability and tutorial maintenance

Subcategory `CATALOG-007-D08` · advanced.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-048"></a>
#### BANK-007-048 — How can a tutorial remain useful after the product interface changes?

**Individual coverage scope:** Explain underlying decisions, preserve versioned screenshots or notes and define the steps that need rechecking.

<a id="bank-007-049"></a>
#### BANK-007-049 — What belongs in the total cost of an AI content workflow?

**Individual coverage scope:** Include retries, rendering, storage, review, correction and licensing using a transparent project budget.

<a id="bank-007-050"></a>
#### BANK-007-050 — How can a team measure whether AI reduced work rather than moved it to review?

**Individual coverage scope:** Compare completed-task quality, human time, rework and failure handling against the previous process.

<a id="bank-007-051"></a>
#### BANK-007-051 — Why should a tool-ranking video report uncertainty instead of one universal winner?

**Individual coverage scope:** Compare different tasks, users, hardware and constraints; show when the ranking reverses.

<a id="bank-007-052"></a>
#### BANK-007-052 — What is a responsible way to publish an AI workflow with known failure cases?

**Individual coverage scope:** Document limitations, recovery steps, suitable uses and updates without presenting the workflow as universally reliable.

<a id="catalog-007-e08"></a>
### Evaluation, exports and switching tools

Subcategory `CATALOG-007-E08` · advanced.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-091"></a>
#### BANK-007-091 — How can a creator compare image tools when each produces different random outputs?

**Individual coverage scope:** Use multiple controlled trials, explicit criteria and uncertainty instead of one best image.

<a id="bank-007-092"></a>
#### BANK-007-092 — What should an AI workflow export include so another person can reproduce it?

**Individual coverage scope:** Preserve prompts, versions, assets, permissions and execution settings without exposing credentials.

<a id="bank-007-093"></a>
#### BANK-007-093 — How can a tool's claimed time saving be measured across setup, review and correction?

**Individual coverage scope:** Record all work stages on comparable tasks rather than timing generation alone.

<a id="bank-007-094"></a>
#### BANK-007-094 — What should a creator test before moving a content pipeline to a new provider?

**Individual coverage scope:** Compare required features, output compatibility, rights and complete representative runs.

<a id="bank-007-095"></a>
#### BANK-007-095 — How can an AI tutorial be corrected when a previously free capability becomes paid?

**Individual coverage scope:** Date the change, update the workflow and distinguish historical instructions from current availability.

<a id="catalog-007-e12"></a>
### Reproducible migrations and changing providers

Subcategory `CATALOG-007-E12` · advanced.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-109"></a>
#### BANK-007-109 — How can an embedding-index migration be tested when the new vectors have a different dimension?

**Individual coverage scope:** Keep original documents, chunk IDs, retrieval questions and reference passages; build a separate index using versioned official interfaces and compare results without mixing incompatible vector spaces.

<a id="bank-007-110"></a>
#### BANK-007-110 — What should a tool-calling migration test verify about optional and missing arguments?

**Individual coverage scope:** Use a fictional local service with explicit schemas, nulls and omitted fields; check validated calls and returned outcomes rather than assuming matching function names imply equivalent behavior.

<a id="bank-007-111"></a>
#### BANK-007-111 — How can a structured-output migration detect silent changes to dates and decimal numbers?

**Individual coverage scope:** Build an original fixture with ambiguous dates, locale-specific separators and required types; compare parsed values with the answer key under both providers' documented contracts.

<a id="bank-007-112"></a>
#### BANK-007-112 — What data must be preserved before retiring a provider-specific conversation store?

**Individual coverage scope:** Inventory user-owned source messages, attachments, tool results, access restrictions and export capabilities; distinguish available export evidence from a promise of full portability.


<a id="domain-007-g02"></a>
## Category: Documents, data and retrieval

<a id="catalog-007-d02"></a>
### Writing and document workflows

Subcategory `CATALOG-007-D02` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-018"></a>
#### BANK-007-018 — How reliably can an AI tool extract a table with merged cells?

**Individual coverage scope:** Use known reference tables and score headers, units, spans and omissions separately from visual resemblance.

<a id="bank-007-019"></a>
#### BANK-007-019 — When does OCR fail before the language model even sees the document?

**Individual coverage scope:** Compare scans, rotation, handwriting, scripts and layout; trace errors to extraction rather than blaming every failure on reasoning.

<a id="bank-007-020"></a>
#### BANK-007-020 — How can a summarization workflow preserve exceptions and qualifications?

**Individual coverage scope:** Compare the summary with labeled source claims, dates and exclusions rather than judging only readability.

<a id="bank-007-021"></a>
#### BANK-007-021 — What checks should an AI-assisted citation workflow perform before export?

**Individual coverage scope:** Verify source existence, passage support, quote accuracy and bibliographic fields using an auditable source list.

<a id="bank-007-022"></a>
#### BANK-007-022 — How can document question answering handle a later revision of the same policy?

**Individual coverage scope:** Track version, date, superseded text and retrieval filters; test whether answers cite the applicable edition.

<a id="bank-007-120"></a>
#### BANK-007-120 — How can a document-to-audio AI workflow keep claims traceable to the uploaded pages?

**Individual coverage scope:** Use a rights-cleared PDF set with known corrections, page references and contradictions. Compare the generated audio and transcript against the source pages, record omissions and invented dialogue, and test whether a listener can reach the supporting passage; do not promise that every PDF can become a studio-quality factual podcast.

<a id="catalog-007-e03"></a>
### Retrieval and personal-document workflows

Subcategory `CATALOG-007-E03` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-064"></a>
#### BANK-007-064 — How can a creator build a test set for document retrieval before uploading a whole archive?

**Individual coverage scope:** Select permission-cleared questions with known passages and explicit missing-answer cases.

<a id="bank-007-065"></a>
#### BANK-007-065 — What should happen when scanned pages enter a retrieval index with incorrect reading order?

**Individual coverage scope:** Compare original pages, OCR output and corrected ingestion before evaluating answers.

<a id="bank-007-066"></a>
#### BANK-007-066 — How can duplicate document versions distort a retrieval demonstration?

**Individual coverage scope:** Track identity, dates and superseded records; preserve the authoritative version.

<a id="bank-007-067"></a>
#### BANK-007-067 — What does a citation click-through test reveal about an AI document assistant?

**Individual coverage scope:** Verify the exact supporting passage, file version and displayed claim.

<a id="bank-007-068"></a>
#### BANK-007-068 — How can a local document assistant handle sensitive files without accidental telemetry exposure?

**Individual coverage scope:** Inspect current app settings, data flows and official policies; do not claim unobserved backend isolation.

<a id="bank-007-121"></a>
#### BANK-007-121 — What should a no-code custom assistant test before using private domain documents and tools?

**Individual coverage scope:** Pin the builder and model version, define an instruction boundary, attach a small permissioned document set, and test source citation, stale-version handling, tool permissions, refusal and export. Distinguish a configured assistant from a trained domain-specific model.

<a id="catalog-007-e04"></a>
### Research, spreadsheets and data workflows

Subcategory `CATALOG-007-E04` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-069"></a>
#### BANK-007-069 — How can an AI spreadsheet helper be checked for formulas that merely look plausible?

**Individual coverage scope:** Use original test inputs, independent calculations and recalculation in the actual spreadsheet engine.

<a id="bank-007-070"></a>
#### BANK-007-070 — What should a chart-generation tutorial verify before presenting an AI-created graph?

**Individual coverage scope:** Compare source values, units, aggregation and labels against the plotted data.

<a id="bank-007-071"></a>
#### BANK-007-071 — How can a research assistant distinguish a search snippet from a source it actually read?

**Individual coverage scope:** Track retrieval, access and supporting text; mark inaccessible sources rather than inventing findings.

<a id="bank-007-072"></a>
#### BANK-007-072 — What makes AI extraction of invoices require more than correct-looking totals?

**Individual coverage scope:** Check document identity, currencies, tax fields and exceptions with permission-cleared samples.

<a id="bank-007-073"></a>
#### BANK-007-073 — How can a tool turn a structured topic bank into a readable document without losing IDs?

**Individual coverage scope:** Compare exported rows, scopes and source records with automated count checks.

<a id="catalog-007-e10"></a>
### Document and spreadsheet failure test sets

Subcategory `CATALOG-007-E10` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-100"></a>
#### BANK-007-100 — How can an invoice-extraction test distinguish a credit note from a normal invoice?

**Individual coverage scope:** Author fictional paired documents with signed totals, taxes, currency and explicit document type; score extracted fields and downstream sign handling rather than only readable text.

<a id="bank-007-101"></a>
#### BANK-007-101 — What should an AI table-extraction test do with a total split across two scanned pages?

**Individual coverage scope:** Construct an original multipage fixture with carried subtotals, repeated headers and reading-order traps; compare cell structure and arithmetic against an independent answer key.

<a id="bank-007-102"></a>
#### BANK-007-102 — How can a spreadsheet assistant be tested on percentages stored as text?

**Individual coverage scope:** Use a disposable workbook containing numeric percentages, localized text and blanks; inspect formula results and type conversion against manual calculations without altering real financial records.

<a id="bank-007-103"></a>
#### BANK-007-103 — What can a hidden-row test reveal about an AI-generated spreadsheet summary?

**Individual coverage scope:** Create an original workbook with filters, hidden rows and clearly labeled totals; require the tool to state its inclusion rule and compare results with the intended view.

<a id="bank-007-104"></a>
#### BANK-007-104 — How can a document-conversion workflow preserve footnote qualifiers attached to a claim?

**Individual coverage scope:** Build a short original source with endnotes, tables and a qualified statement; verify rendered pages and claim-footnote links rather than judging only extracted body text.

<a id="catalog-007-d07"></a>
### Data, privacy and portability

Subcategory `CATALOG-007-D07` · advanced.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-043"></a>
#### BANK-007-043 — Where can a supposedly private AI workflow still send user data?

**Individual coverage scope:** Trace uploads, prompts, telemetry, integrations and logs using actual policies and network or architecture documentation.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTES/BANK-007-043.md). This does not change proposal or production status.

<a id="bank-007-044"></a>
#### BANK-007-044 — What should be exported before changing AI providers?

**Individual coverage scope:** Inventory source files, references, prompts, configuration and editable outputs; test that the replacement can read them.

<a id="bank-007-045"></a>
#### BANK-007-045 — How can an app's privacy policy differ from settings visible in its interface?

**Individual coverage scope:** Compare policy scope, account tier, retention, training use and deletion terms at a recorded date.

<a id="bank-007-046"></a>
#### BANK-007-046 — What does an AI tool's commercial-use claim leave unresolved?

**Individual coverage scope:** Inspect input rights, output terms, likeness, music, trademarks and jurisdiction rather than treating one label as complete clearance.

<a id="bank-007-047"></a>
#### BANK-007-047 — How should a tutorial disclose an affiliate relationship or sponsored access?

**Individual coverage scope:** Separate compensation, preferential access, test design and conclusions; keep failures visible alongside benefits.


<a id="domain-007-g03"></a>
## Category: Creative media workflows

<a id="catalog-007-d03"></a>
### Image-generation workflows

Subcategory `CATALOG-007-D03` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-023"></a>
#### BANK-007-023 — How can a reference board improve consistency across generated images?

**Individual coverage scope:** Separate character identity, costume, palette, composition and lighting; test changes one variable at a time.

<a id="bank-007-024"></a>
#### BANK-007-024 — Why does full-body framing not require every limb to be visible?

**Individual coverage scope:** Compare complete pose framing, plausible concealment and anatomy; avoid forcing an extra hand or foot into view.

<a id="bank-007-025"></a>
#### BANK-007-025 — How can animal-faced characters remain visually consistent with human characters?

**Individual coverage scope:** Test linework, shading, facial design and rendering vocabulary rather than assuming one style label controls every subject.

<a id="bank-007-026"></a>
#### BANK-007-026 — What should be checked when editing one object in a generated image?

**Individual coverage scope:** Inspect surrounding geometry, shadows, texture, identity and unintended changes against the original reference.

<a id="bank-007-027"></a>
#### BANK-007-027 — How can a creator evaluate text rendering in generated thumbnails?

**Individual coverage scope:** Score spelling, script shape, hierarchy and mobile-size readability; distinguish editable typography from baked-in image text.

<a id="catalog-007-d04"></a>
### Video generation and continuity

Subcategory `CATALOG-007-D04` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-028"></a>
#### BANK-007-028 — What makes a source image suitable for a restrained image-to-video shot?

**Individual coverage scope:** Check pose stability, depth cues, moving elements and camera intent before selecting the generation settings.

<a id="bank-007-029"></a>
#### BANK-007-029 — How can a static-camera ambient scene retain believable movement?

**Individual coverage scope:** Specify local motions, loop boundaries and stable geometry; evaluate flicker, drifting objects and unintended camera changes.

<a id="bank-007-030"></a>
#### BANK-007-030 — Why do generated characters change appearance between adjacent shots?

**Individual coverage scope:** Compare references, seeds, prompts, lighting and model versions while documenting which controls actually affect identity.

<a id="bank-007-031"></a>
#### BANK-007-031 — How can an editor assemble usable coverage from imperfect generated clips?

**Individual coverage scope:** Plan shot purpose, continuity, cut points and sound bridges without hiding factual reconstruction as real footage.

<a id="bank-007-032"></a>
#### BANK-007-032 — What does a good loop test reveal beyond matching the first and last frame?

**Individual coverage scope:** Inspect motion direction, timing, light, audio and objects across repeated playback cycles.

<a id="catalog-007-d05"></a>
### Voice, transcription and music

Subcategory `CATALOG-007-D05` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-033"></a>
#### BANK-007-033 — How should a transcription tool be tested on accented and multilingual speech?

**Individual coverage scope:** Use consented recordings and reference transcripts; score names, code-switching, omissions and speaker attribution separately.

<a id="bank-007-034"></a>
#### BANK-007-034 — What makes a synthetic voice's pronunciation controllable across a series?

**Individual coverage scope:** Compare pronunciation dictionaries, phonetic hints, text normalization and voice settings on recurring names.

<a id="bank-007-035"></a>
#### BANK-007-035 — How can a voice-cloning workflow document meaningful authorization?

**Individual coverage scope:** Verify the speaker, permitted uses, retention and withdrawal terms without treating possession of a recording as consent.

<a id="bank-007-036"></a>
#### BANK-007-036 — How can AI-generated music be evaluated for a seamless meditation loop?

**Individual coverage scope:** Inspect structure, abrupt transitions, changing intensity, clipping and repetition fatigue; do not infer therapeutic effects from genre.

<a id="bank-007-037"></a>
#### BANK-007-037 — When does stem separation help an edit, and when do artifacts make it worse?

**Individual coverage scope:** Compare isolated and recombined stems using controlled listening, phase checks and the actual delivery requirement.

<a id="bank-007-118"></a>
#### BANK-007-118 — What should a real-time voice-agent tutorial measure before placing a live call?

**Individual coverage scope:** Use a consented test environment to log speech recognition errors, response latency, interruptions, handoff, synthetic-voice disclosure and failure recovery across a named stack version. Keep real contacts and production phone lines out of the demonstration until the workflow is reviewed.

<a id="bank-007-122"></a>
#### BANK-007-122 — How can a family rehearse verification when a caller sounds like a relative?

**Individual coverage scope:** Use a harmless consented role-play to test pausing a money request and calling the person back through a previously known number or another trusted contact. Explain that a familiar-sounding voice and caller ID are not sufficient identity proof; do not clone a real relative's voice for the demonstration without permission or claim any single trick prevents every scam.

**Research follow-up:** [Bounded case and source-access note](RESEARCH_NOTES/BANK-007-122.md). This does not change proposal or production status.

<a id="catalog-007-e05"></a>
### Creator pipelines from brief to delivery

Subcategory `CATALOG-007-E05` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-074"></a>
#### BANK-007-074 — How can a devotional image workflow separate iconography checks from stylistic consistency?

**Individual coverage scope:** Use authorized attributes and a designated visual guide; do not treat generated detail as source evidence.

<a id="bank-007-075"></a>
#### BANK-007-075 — What should a thumbnail workflow compare before choosing a final image?

**Individual coverage scope:** Inspect composition, legibility, claim accuracy, crop and actual export size.

<a id="bank-007-076"></a>
#### BANK-007-076 — How can a long ambient-video workflow avoid repeating an obvious visual defect?

**Individual coverage scope:** Review loop seams, motion continuity and representative samples before full rendering.

<a id="bank-007-077"></a>
#### BANK-007-077 — What does multilingual subtitle export need beyond a translated transcript?

**Individual coverage scope:** Check timing, script shaping, names, speaker identity and source-language review.

<a id="bank-007-078"></a>
#### BANK-007-078 — How can generated music be combined with a nature recording while preserving provenance?

**Individual coverage scope:** Track licenses, levels, edits and the original recordings; avoid commercial-rights assumptions.

<a id="bank-007-079"></a>
#### BANK-007-079 — How can an AI video tool's export be tested for the platform format actually needed?

**Individual coverage scope:** Verify dimensions, frame rate, duration, codec and visible artifacts in the delivered file.

<a id="catalog-007-e11"></a>
### Audio, video and creator export diagnostics

Subcategory `CATALOG-007-E11` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-105"></a>
#### BANK-007-105 — How can a subtitle workflow detect timing drift in a long recording?

**Individual coverage scope:** Use consented or original audio with timed markers near the beginning, middle and end; compare exported cues with the exact media timebase and separate transcription errors from synchronization errors.

<a id="bank-007-106"></a>
#### BANK-007-106 — What should an AI video-export test measure when frame rate is variable?

**Individual coverage scope:** Record source timestamps, output metadata and visible synchronization markers using official tool documentation; avoid assuming a nominal frame-rate label proves uniform timing.

<a id="bank-007-107"></a>
#### BANK-007-107 — How can an ambient-loop test distinguish a seamless image transition from an audible seam?

**Individual coverage scope:** Render an original short loop and inspect the boundary in both waveform and frame sequence; assess repeated listening and viewing without declaring a long export verified from one still image.

<a id="bank-007-108"></a>
#### BANK-007-108 — How can a generated Hindi voiceover be checked for devotional names and honorifics?

**Individual coverage scope:** Use a source-language reviewer, an approved word list and actual audio rather than transcript-only scoring; verify voice-use permission and avoid cloning an identifiable person's voice without consent.


<a id="domain-007-g04"></a>
## Category: Code, automation and inclusive validation

<a id="catalog-007-d06"></a>
### Coding and automation

Subcategory `CATALOG-007-D06` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-038"></a>
#### BANK-007-038 — How can an AI coding tutorial prove that its generated program works?

**Individual coverage scope:** Run meaningful task checks, inspect dependencies and show failures rather than relying on a successful-looking explanation.

<a id="bank-007-039"></a>
#### BANK-007-039 — What should happen when a coding assistant names an unavailable library function?

**Individual coverage scope:** Check official versioned documentation, reproduce the error and repair the implementation without inventing a second unsupported API.

<a id="bank-007-040"></a>
#### BANK-007-040 — How can a file-renaming automation preview its effects safely?

**Individual coverage scope:** Separate selection, proposed changes, collision checks, execution and recovery in a reversible local example.

<a id="bank-007-041"></a>
#### BANK-007-041 — When should an automated workflow stop for a human decision?

**Individual coverage scope:** Identify consequential ambiguity, authority boundaries and recoverability using a concrete process rather than approval at every step.

<a id="bank-007-042"></a>
#### BANK-007-042 — How can tool execution logs distinguish a proposed action from a completed one?

**Individual coverage scope:** Capture inputs, results, errors and postconditions; require evidence before reporting that a file or external record changed.

<a id="catalog-007-e06"></a>
### Coding assistants and development projects

Subcategory `CATALOG-007-E06` · intermediate.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-080"></a>
#### BANK-007-080 — How can a coding assistant propose a reviewable change before modifying a project?

**Individual coverage scope:** Inspect the actual repository, scope, diff and existing tests using a disposable example.

<a id="bank-007-081"></a>
#### BANK-007-081 — What should a generated website be checked for beyond its first screenshot?

**Individual coverage scope:** Test navigation, forms, mobile layout, accessibility and actual stored state.

<a id="bank-007-082"></a>
#### BANK-007-082 — How can an AI assistant repair an error without silently replacing unrelated work?

**Individual coverage scope:** Use isolated edits, version history and explicit preservation checks.

<a id="bank-007-083"></a>
#### BANK-007-083 — What does a dependency-installation tutorial need to verify before running suggested commands?

**Individual coverage scope:** Check official package identity, versions, permissions and actual project requirements.

<a id="bank-007-084"></a>
#### BANK-007-084 — How can an AI coding workflow distinguish an existing repository issue from a new regression?

**Individual coverage scope:** Compare baseline behavior, changed scope and appropriate reproducible checks.

<a id="catalog-007-e07"></a>
### Automation, connectors and persistent work

Subcategory `CATALOG-007-E07` · advanced.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-085"></a>
#### BANK-007-085 — How can an automation be tested without sending real messages or changing real records?

**Individual coverage scope:** Use drafts, sandbox data and explicit action boundaries.

<a id="bank-007-086"></a>
#### BANK-007-086 — What should a connector disclose before an AI tool reads a cloud account?

**Individual coverage scope:** Inspect permissions, selected resources, retention and current official documentation.

<a id="bank-007-087"></a>
#### BANK-007-087 — How can a scheduled AI task avoid repeating work after an interrupted run?

**Individual coverage scope:** Use stable IDs, saved checkpoints and completion evidence outside transient memory.

<a id="bank-007-088"></a>
#### BANK-007-088 — What happens when two AI workflows try to update the same saved artifact?

**Individual coverage scope:** Demonstrate guarded writes, conflict detection and reconciliation using placeholder content.

<a id="bank-007-089"></a>
#### BANK-007-089 — How can an automation report a genuine blocker without implying partial work is complete?

**Individual coverage scope:** Define observable progress, missing requirements and an honest remaining-work tracker.

<a id="bank-007-090"></a>
#### BANK-007-090 — How can a workflow distinguish private saving from public publication?

**Individual coverage scope:** Verify actual access settings and deployment state rather than relying on a success message.

<a id="bank-007-119"></a>
#### BANK-007-119 — How can a tool-using assistant tutorial test prompt injection without exposing a real account?

**Individual coverage scope:** Build an authorized sandbox with a lower-trust retrieved page or document, a canary instruction and a harmless mock action. Record whether the assistant separates source content from user authority, whether permissions prevent side effects and what appears in the tool log; distinguish this workflow test from a general explanation of the attack.

<a id="catalog-007-e13"></a>
### Accessibility and multilingual end-to-end validation

Subcategory `CATALOG-007-E13` · advanced.

Prerequisites: [CATALOG-007-D01](#catalog-007-d01).

<a id="bank-007-113"></a>
#### BANK-007-113 — How can a keyboard-only user complete an AI image-generation workflow from prompt to saved file?

**Individual coverage scope:** Plan a consented task test covering focus order, labels, progress, error recovery and download; inspect the actual versioned interface rather than assuming keyboard access from general accessibility claims.

<a id="bank-007-114"></a>
#### BANK-007-114 — How can a screen-reader test reveal missing information in an AI tool's image choices?

**Individual coverage scope:** Compare spoken labels, card selection, generation status and alternative descriptions in a named version; use intended-user feedback and do not infer accessibility from visual layout alone.

<a id="bank-007-115"></a>
#### BANK-007-115 — What can a Hindi-English mixed-script test reveal about a search-and-summary workflow?

**Individual coverage scope:** Create public or original paired documents, preserve transliteration variants and score retrieval and source attribution separately; avoid generalizing from one dialect or script convention.

<a id="bank-007-116"></a>
#### BANK-007-116 — How should an AI tutorial distinguish a tested workflow from a planned one?

**Individual coverage scope:** Publish a version-and-environment ledger with actual commands, observed failures and reproducibility limits after execution; label every unexecuted step and do not fabricate a success screenshot or timing result.

## Preserved local roadmap and queue references

The following 27 source records remain in their original status containers and are not added to the active BANK count. Existing completion claims, dates and popularity language are preserved metadata; this work has not independently certified them. Overlapping surveys are references rather than additional counted episodes. The original roadmap, report and status text are preserved in the JSON local_reconciliation snapshot.

### pending_topics/0 — Prompt Engineering in 2026: The Only 5 Techniques That Actually Work

**Original question:** How do modern reasoning models respond to role priming, few-shot examples, and chain-of-thought?

**Original planning scope:** Eliminating fluff prompts, structured JSON output formatting, context window management.

**Editorial disposition:** reframe_as_repeated_prompt_test. The 'only five' and year-specific claim is untested. Compare controlled prompt changes on fixed tasks and report failures rather than guaranteeing universal techniques.

**Scoped proposals:** [BANK-007-117](#bank-007-117), [BANK-007-017](#bank-007-017).

### pending_topics/1 — ChatGPT vs Claude vs Gemini: The Complete Real-World Benchmark Test

**Original question:** Which leading AI model wins for coding, creative writing, data analysis, and long documents?

**Original planning scope:** Claude 3.5 Sonnet Artifacts, ChatGPT o1 reasoning chains, Gemini 2M context window.

**Editorial disposition:** route_to_existing_scopes. A named-version comparison needs the same tasks, scoring and uncertainty; there is no universal product winner.

**Scoped proposals:** [BANK-007-013](#bank-007-013), [BANK-007-051](#bank-007-051), [BANK-007-091](#bank-007-091).

### pending_topics/2 — Perplexity AI Masterclass: How to Replace Traditional Google Search

**Original question:** How can students and researchers synthesize sourced academic papers with live web citations?

**Original planning scope:** Pro search queries, collections organization, focus modes (Academic, YouTube, Reddit).

**Editorial disposition:** route_to_existing_scopes. Source access and citation click-through are testable research-workflow questions. Replacing search generally is a dated promotional claim, not an established outcome.

**Scoped proposals:** [BANK-007-071](#bank-007-071), [BANK-007-067](#bank-007-067), [BANK-007-021](#bank-007-021).

### pending_topics/3 — NotebookLM: How to Turn Any Pile of PDFs into a Studio-Quality Podcast

**Original question:** How does Google's source-grounded notebook generate multi-speaker audio discussions?

**Original planning scope:** Grounded source ingestion, avoiding hallucinations, audio overview generation, study guides.

**Editorial disposition:** reframe_as_document_to_audio_test. The distinct workflow is whether generated audio retains the PDF evidence and corrections; 'any pile' and 'studio-quality' are not guaranteed.

**Scoped proposals:** [BANK-007-120](#bank-007-120), [BANK-007-020](#bank-007-020).

### pending_topics/4 — Midjourney v6 & Flux.1: The Definitive Photorealism Prompting Guide

**Original question:** How do camera parameters, lighting styles, and raw parameters create hyper-realistic images?

**Original planning scope:** Aspect ratios, style references (--sref), inpainting, Flux open-weight prompting comparisons.

**Editorial disposition:** route_to_existing_scopes. Compare current named image-model versions on reference consistency, edits and repeated outcomes; the archived v6/Flux.1 label is not a current-specification claim.

**Scoped proposals:** [BANK-007-023](#bank-007-023), [BANK-007-026](#bank-007-026), [BANK-007-091](#bank-007-091).

### pending_topics/5 — AI Video Generation: Runway Gen-3 vs Kling vs Luma Dream Machine

**Original question:** How can creators generate consistent cinematic camera moves without unnatural morphing?

**Original planning scope:** Camera motion controls, motion brush painting, keyframe-to-keyframe consistency, text-to-video.

**Editorial disposition:** route_to_existing_scopes. A video-tool comparison should use matching input shots, continuity criteria and export checks, with versions recorded at test time.

**Scoped proposals:** [BANK-007-028](#bank-007-028), [BANK-007-030](#bank-007-030), [BANK-007-079](#bank-007-079).

### pending_topics/6 — ElevenLabs & AI Audio: Cloning Your Voice and Generating Expressive Speech

**Original question:** How do professional creators clone voice timbre, dynamic emotion, and multi-lingual dubbing?

**Original planning scope:** Voice design, audio isolation, latency reduction, pacing, ethical voice verification.

**Editorial disposition:** route_to_existing_scopes. Authorization and pronunciation consistency are separate voice-cloning tests; the product-name hook adds no independent question.

**Scoped proposals:** [BANK-007-035](#bank-007-035), [BANK-007-034](#bank-007-034).

### pending_topics/7 — Canva & Adobe Firefly: Practical Graphic Design Workflows for Non-Designers

**Original question:** How can small business owners create social graphics, posters, and pitch decks with generative fill?

**Original planning scope:** Generative expand, text effects, vector recoloring, brand kit automation.

**Editorial disposition:** route_to_existing_scopes. A non-designer workflow can test text rendering, final thumbnails and commercial-use claims without declaring a universal design tool.

**Scoped proposals:** [BANK-007-027](#bank-007-027), [BANK-007-075](#bank-007-075), [BANK-007-046](#bank-007-046).

### pending_topics/8 — Building Your First Custom GPT / Claude Project: Domain-Specific AI Assistants

**Original question:** How do you configure instructions, knowledge files, and API actions for specialized tasks?

**Original planning scope:** System instructions framing, uploading clean reference data, preventing knowledge leakage.

**Editorial disposition:** reframe_as_configured_assistant_test. A no-code assistant configured with instructions and files is not a newly trained model; test current builder version, document scope and connector permissions.

**Scoped proposals:** [BANK-007-121](#bank-007-121), [BANK-007-064](#bank-007-064), [BANK-007-086](#bank-007-086).

### pending_topics/9 — Automate Everything with Make & n8n: Zero-Code AI Workflows

**Original question:** How can you trigger AI summaries from incoming Gmail, update Notion, and post to Slack?

**Original planning scope:** Webhooks, API connectors, error handling, token cost optimization in automated loops.

**Editorial disposition:** route_to_existing_scopes. Automation must be dry-run, permissioned and able to report a genuine blocker; 'automate everything' is unsupported.

**Scoped proposals:** [BANK-007-085](#bank-007-085), [BANK-007-086](#bank-007-086), [BANK-007-089](#bank-007-089).

### pending_topics/10 — RAG Demystified: How to Chat with Thousands of Company Documents Accurately

**Original question:** How do vector embeddings and semantic search feed exact text chunks into language models?

**Original planning scope:** Chunking strategies, vector databases (Pinecone, Chroma), cosine similarity, context limits.

**Editorial disposition:** route_to_existing_scopes_and_neighbor. Niche 001 BANK-001-029 owns the retrieval-versus-training concept. Niche 007 covers test-set construction, document-version conflict and citation click-through; accuracy needs measured evidence.

**Scoped proposals:** [BANK-007-064](#bank-007-064), [BANK-007-066](#bank-007-066), [BANK-007-067](#bank-007-067).

### pending_topics/11 — AI for Data Analysis: Turning Messy Spreadsheets into Interactive Dashboards

**Original question:** How can non-coders clean dirty CSV data, run Python statistical regressions, and plot charts?

**Original planning scope:** Code Interpreter / Advanced Data Analysis, pivot tables, correlation heatmaps, trend forecasts.

**Editorial disposition:** route_to_existing_scopes. Formula correctness and chart grounding, including text percentages and hidden rows, are distinct data-workflow tests.

**Scoped proposals:** [BANK-007-069](#bank-007-069), [BANK-007-070](#bank-007-070), [BANK-007-102](#bank-007-102), [BANK-007-103](#bank-007-103).

### pending_topics/12 — Run AI Locally with Ollama & LM Studio: 100% Private, Free, and Offline

**Original question:** How can you download Llama 3.3, Mistral, and DeepSeek to run on your laptop without the internet?

**Original planning scope:** Quantization levels (Q4_K_M vs Q8), memory allocation, CPU vs GPU offloading, local privacy.

**Editorial disposition:** reframe_as_versioned_local_data_path. Current vendor docs distinguish local inference, model downloads, optional cloud processing and network exposure. No runtime was installed or tested here; the linked note records the source-only boundary.

**Scoped proposals:** [BANK-007-015](#bank-007-015), [BANK-007-043](#bank-007-043), [BANK-007-053](#bank-007-053), [BANK-007-098](#bank-007-098).

### pending_topics/13 — Cursor AI & GitHub Copilot: The 10x Developer Coding Workflow

**Original question:** How do AI-native code editors index your entire repository to refactor code and fix bugs?

**Original planning scope:** Multi-file edits, codebase chat, generating automated test suites, debugging compiler errors.

**Editorial disposition:** route_to_existing_scopes. Coding-assistant speed claims need a working program, reviewable diff and regression check; '10x' is unverified.

**Scoped proposals:** [BANK-007-038](#bank-007-038), [BANK-007-080](#bank-007-080), [BANK-007-084](#bank-007-084).

### pending_topics/14 — ComfyUI Masterclass: Node-Based Image Generation for Complete Creative Control

**Original question:** How do professional AI artists build modular node workflows for ControlNet, LoRA, and upscaling?

**Original planning scope:** VAE loaders, sampling steps, ControlNet pose tracking, ultimate SD upscale nodes.

**Editorial disposition:** route_to_existing_scopes. Node-graph creative control can be tested through reference consistency, isolated edits, repeatability and exported workflow state on a pinned tool version.

**Scoped proposals:** [BANK-007-023](#bank-007-023), [BANK-007-026](#bank-007-026), [BANK-007-091](#bank-007-091), [BANK-007-092](#bank-007-092).

### pending_topics/15 — Voice Agents & Real-Time AI: Building Conversational Call Bots with LiveKit & Vapi

**Original question:** How do sub-500ms voice-to-voice pipelines handle customer bookings and phone interviews?

**Original planning scope:** WebRTC audio streaming, whisper speech-to-text, fast LLM inference, text-to-speech synthesis.

**Editorial disposition:** reframe_as_consented_voice_agent_test. The distinct real-time workflow needs latency, interruption, disclosure and human handoff checks before any live calling; named service versions remain to be chosen.

**Scoped proposals:** [BANK-007-118](#bank-007-118), [BANK-007-035](#bank-007-035), [BANK-007-085](#bank-007-085).

### pending_topics/16 — AI Prompt Injection & Security: How to Protect Your Tools from Jailbreaks

**Original question:** How do hackers use hidden prompt injections inside web pages and PDFs to hijack AI tools?

**Original planning scope:** Direct vs indirect injection, data exfiltration attacks, input sanitization defense layers.

**Editorial disposition:** route_to_neighboring_concept_and_sandbox_test. Niche 001 BANK-001-046 is the conceptual home for prompt injection. Niche 007 adds a harmless lower-trust document and mock-action tutorial with no live account exposure.

**Scoped proposals:** [BANK-007-119](#bank-007-119), [BANK-007-085](#bank-007-085).

### pending_topics/17 — Building Autonomous Agents: LangChain, CrewAI & AutoGen Explained

**Original question:** How do multi-agent frameworks assign roles (Researcher, Writer, Editor) to complete complex projects?

**Original planning scope:** Agent coordination, tool calling, shared memory, infinite loop recovery.

**Editorial disposition:** route_to_existing_scopes_and_neighbor. Niche 001 covers agent mechanisms; niche 007 tests a current framework through human decision gates, truthful tool logs and restart recovery rather than promising autonomy.

**Scoped proposals:** [BANK-007-041](#bank-007-041), [BANK-007-042](#bank-007-042), [BANK-007-087](#bank-007-087).

### pending_topics/18 — Fine-Tuning vs RAG: Which Strategy Should Your Business Actually Choose?

**Original question:** When does teaching a model new facts require LoRA fine-tuning versus retrieval augmentation?

**Original planning scope:** Cost comparisons, catastrophic forgetting, style adaptation vs knowledge recall.

**Editorial disposition:** route_to_neighboring_concept_and_workflow. Niche 001 BANK-001-029 owns the retrieval-versus-fine-tuning decision. Niche 007 can test retrieval quality and source-version handling for an actual business document set.

**Scoped proposals:** [BANK-007-064](#bank-007-064), [BANK-007-066](#bank-007-066).

### pending_topics/19 — The Best Free AI Tool Stack for Solopreneurs in 2026

**Original question:** How can a single founder run marketing, customer service, coding, and legal for under $50/month?

**Original planning scope:** Essential tool stack, free tiers, API cost-slashing tricks, maximum leverage workflows.

**Editorial disposition:** route_to_existing_scopes. A free stack is versioned and task-dependent; finish a full workflow, count hidden costs and record when a previously free feature moves behind a paywall.

**Scoped proposals:** [BANK-007-014](#bank-007-014), [BANK-007-049](#bank-007-049), [BANK-007-095](#bank-007-095).

### trending_topics/0 — DeepSeek V3 & R1 Explained: Why Open-Source China AI Is Shocking Silicon Valley

**Editorial disposition:** route_to_existing_scopes. The geopolitical and performance headline is unverified. A model comparison would pin versions, tests and uncertainty without treating open weights as the same thing as open-source licensing.

**Scoped proposals:** [BANK-007-013](#bank-007-013), [BANK-007-016](#bank-007-016), [BANK-007-051](#bank-007-051).

### trending_topics/1 — Sora & Gen-3 Video Prompting: 10 Cinematic Secrets Nobody Tells You

**Editorial disposition:** route_to_existing_scopes. The 'ten secrets' hook is an unverified count. Test named video versions on source-shot suitability, continuity and export requirements.

**Scoped proposals:** [BANK-007-028](#bank-007-028), [BANK-007-030](#bank-007-030), [BANK-007-079](#bank-007-079).

### trending_topics/2 — How to Build a Second Brain with Notion AI and Obsidian

**Editorial disposition:** route_to_existing_scopes. A second-brain claim becomes a data-portability and retrieval-version test, not a promise of improved memory or productivity.

**Scoped proposals:** [BANK-007-044](#bank-007-044), [BANK-007-064](#bank-007-064), [BANK-007-066](#bank-007-066), [BANK-007-092](#bank-007-092).

### trending_topics/3 — The Complete Guide to AI Music: Suno v4 vs Udio for Producers

**Editorial disposition:** route_to_existing_scopes. Compare current music-tool versions through usable loop quality, stem artifacts, rights and provenance; archived product versions are not current facts.

**Scoped proposals:** [BANK-007-036](#bank-007-036), [BANK-007-037](#bank-007-037), [BANK-007-078](#bank-007-078).

### trending_topics/4 — Are Paid AI Subscriptions Still Worth It? ChatGPT Plus vs Claude Pro in 2026

**Editorial disposition:** route_to_existing_scopes. Subscription value depends on current plan limits, total workflow cost and task-specific uncertainty, not one universal paid-versus-free answer.

**Scoped proposals:** [BANK-007-014](#bank-007-014), [BANK-007-049](#bank-007-049), [BANK-007-051](#bank-007-051).

### trending_topics/5 — Build a Full-Stack Web App in 10 Minutes with v0.dev and Supabase

**Editorial disposition:** route_to_existing_scopes. A generated app needs functional, dependency, state and regression checks; the ten-minute production claim is an unverified promotional target.

**Scoped proposals:** [BANK-007-081](#bank-007-081), [BANK-007-083](#bank-007-083), [BANK-007-084](#bank-007-084).

### trending_topics/6 — The Dark Side of AI Voice Cloning: Protecting Your Family from Phone Scams

**Editorial disposition:** reframe_as_family_verification_rehearsal. A distinct consumer-safety tutorial is supported by FTC guidance on independently verifying emergency requests; voice-clone authorization remains a separate creator workflow.

**Scoped proposals:** [BANK-007-122](#bank-007-122), [BANK-007-035](#bank-007-035).

## Preserved starter subject map — coverage checklist, not extra proposals

These original subject headings and IDs are retained from the ZIP. Their templated question briefs remain in prior_initial_map. Compare them with the active scopes above when identifying missing branches; do not count the old starters as additional episodes.

<a id="catalog-007-01"></a>
### Practical workflows

<a id="bank-007-001"></a>
- `BANK-007-001` — Comparing transcription tools on accented speech → [BANK-007-033](#bank-007-033), [BANK-007-099](#bank-007-099)
<a id="bank-007-002"></a>
- `BANK-007-002` — Testing document extraction on complex tables → [BANK-007-101](#bank-007-101)
<a id="bank-007-003"></a>
- `BANK-007-003` — Image generation with consistent references → [BANK-007-023](#bank-007-023), [BANK-007-025](#bank-007-025)
<a id="bank-007-004"></a>
- `BANK-007-004` — Evaluating text-to-video continuity → [BANK-007-028](#bank-007-028), [BANK-007-030](#bank-007-030), [BANK-007-031](#bank-007-031)

<a id="catalog-007-02"></a>
### Tool selection

<a id="bank-007-005"></a>
- `BANK-007-005` — Local versus cloud AI workflows → [BANK-007-015](#bank-007-015)
<a id="bank-007-006"></a>
- `BANK-007-006` — Free tiers and total workflow cost → [BANK-007-049](#bank-007-049), [BANK-007-095](#bank-007-095)
<a id="bank-007-007"></a>
- `BANK-007-007` — Export formats and vendor lock-in → [BANK-007-044](#bank-007-044), [BANK-007-112](#bank-007-112)
<a id="bank-007-008"></a>
- `BANK-007-008` — Data retention in AI applications → [BANK-007-043](#bank-007-043), [BANK-007-045](#bank-007-045)

<a id="catalog-007-03"></a>
### Verification

<a id="bank-007-009"></a>
- `BANK-007-009` — Checking AI-generated citations → [BANK-007-067](#bank-007-067), [BANK-007-071](#bank-007-071)
<a id="bank-007-010"></a>
- `BANK-007-010` — Measuring coding-assistant regressions → [BANK-007-038](#bank-007-038), [BANK-007-084](#bank-007-084)
<a id="bank-007-011"></a>
- `BANK-007-011` — Evaluating speech-cloning consent controls → [BANK-007-035](#bank-007-035)
<a id="bank-007-012"></a>
- `BANK-007-012` — Reproducing an AI tutorial across versions → [BANK-007-016](#bank-007-016), [BANK-007-048](#bank-007-048), [BANK-007-092](#bank-007-092)

## Neighboring niche boundaries

The following homes have deliberately related subject matter. They are navigation leads, not proof that the same question belongs in every bank. Choose one primary home for an actual episode and link it elsewhere. Where a subject appears in more than one context, retain the distinct case, population, system or interpretive question.

- [001 AI + Technology Explainers](../001_ai_technology_explainers/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [337 AI Research](../337_ai_research/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [338 Developer AI](../338_developer_ai/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [531 AI Software Agents](../531_ai_software_agents/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.
- [532 Large Language Model Systems](../532_large_language_model_systems/IN_DEPTH_TOPIC_BANK.md): compare actual questions and select one primary home.

## Editorial coverage review

Question scopes, source concepts and documented gaps reviewed.


## Coverage remaining open

- **Versioned workflow evidence:** Choose current named tool versions and run the proposed prompt, document-to-audio, local-server, voice-agent, prompt-injection, screen-reader, multilingual, export and migration tests; retain failure cases and maintenance dates. No live local-runtime test was possible in the current environment.
- **Sources and readiness:** Vendor documentation on Ollama and LM Studio data paths and FTC voice-scam guidance were inspected in bounded notes; most proposals still need actual versioned runs, independent observation and source checks. No research certification or production approval was performed.
- **Neighboring-niche boundary review:** The legacy RAG, prompt-injection and agent-framework pitches now name niche 001 as their conceptual home, while niche 007 retains hands-on workflow tests. Compare further related banks before production; lexical duplicate checks do not establish semantic uniqueness across every pair.

## Connection to the production documents

This bank links through [the main topics index](../README.md), the existing niche roadmap and [the existing registry identity](../../REGISTRY/Niches/007_ai_tools_ai_tutorials/NICHE_007_ai_tools_ai_tutorials.md). It supplies candidate topics; it does not change CAT Q1–Q42, registered angles, IDEA readiness, DEPTH plans, existing CONFIG snapshots, episode files or production gates.

Select a bounded question, inspect actual sources, choose a registered angle and deliberately promote the selected idea through the existing registry workflow. No bank record is automatically ready_for_project.
