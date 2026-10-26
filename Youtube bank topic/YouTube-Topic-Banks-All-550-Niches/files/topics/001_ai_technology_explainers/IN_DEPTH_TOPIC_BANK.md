# 001 AI + Technology Explainers: Detailed Topic-Bank Draft

**23 categories · 121 individually authored episode proposals.**

Individually authored episode questions and coverage boundaries for AI + Technology Explainers. The subject progression is organized by concrete content rather than a topic-by-angle multiplication.

[All-niche progress](../DEPTH_COMPLETION_STATUS.md) · [All-niche index](../ALL_NICHE_TOPIC_BANKS.md) · [Editable bank](./IN_DEPTH_TOPIC_BANK.json)

Every question below has its own coverage boundary. All remain proposed; sources and current niche angle scopes have not been verified. Learning levels organize documentary research rather than physical difficulty. The older initial proposals remain in the JSON's prior_initial_map archive and are not counted again.

## 01. Representations and tokenization

**Level:** foundation. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-013 | Why can the same sentence require different token counts in two models? | Compare vocabulary, normalization, byte handling and a fixed multilingual sample; separate tokens from words. |
| BANK-001-014 | How do subword vocabularies handle rare names and spelling mistakes? | Trace segmentation of controlled examples and examine the tradeoff between vocabulary size and sequence length. |
| BANK-001-015 | What changes when text, images and audio share one model interface? | Separate modality encoders, representations, alignment and output tasks; avoid implying identical internal processing. |
| BANK-001-016 | Why does numerical reasoning remain difficult for a text predictor? | Compare number representation, training examples, exact computation and tool-assisted answers on reproducible arithmetic tasks. |
| BANK-001-017 | How does positional information let a transformer distinguish word order? | Explain an identified positional scheme with short examples; compare training context with longer inputs. |

## 02. Training and learning

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-018 | What does next-token training teach beyond memorizing sentences? | Distinguish the prediction objective, learned statistical structure, generalization tests and examples that expose memorization. |
| BANK-001-019 | Why are training, validation and test data kept separate? | Trace a small experiment and show how leakage changes the apparent performance estimate. |
| BANK-001-020 | What happens during gradient descent in a language-model training step? | Follow loss, gradients, parameter updates and learning rate in a toy network rather than claiming access to proprietary training. |
| BANK-001-021 | How do supervised instruction tuning and preference optimization differ? | Compare datasets, objectives, human judgments and evaluation; do not equate preference with factual accuracy. |
| BANK-001-022 | Why can additional training data make an evaluation less trustworthy? | Examine benchmark overlap, near duplicates and the difference between legitimate learning and contaminated measurement. |

## 03. Inference and generation

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-023 | How does a model choose the next token from its output scores? | Work through logits, probabilities and selection using a small hypothetical vocabulary with explicitly illustrative numbers. |
| BANK-001-024 | Why do temperature and top-p produce different kinds of variation? | Compare repeated generations from the same distribution while controlling prompt, model version and sampling settings. |
| BANK-001-025 | What does a key-value cache store during text generation? | Trace repeated attention work, cache growth and memory use; distinguish stored activations from permanent model knowledge. |
| BANK-001-026 | Why does generating the first token often take longer than later tokens? | Separate prompt processing, decoding, batching and network delay using a measured serving trace. |
| BANK-001-027 | Can a model give different answers when sampling is disabled? | Investigate hardware kernels, server settings, version changes and numerical nondeterminism before assigning one cause. |

## 04. Context and external knowledge

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-028 | Why can information in a long context still be overlooked? | Test information placement, distractors, retrieval tasks and answer scoring; distinguish advertised length from effective use. |
| BANK-001-029 | When should an application retrieve documents instead of fine-tuning a model? | Compare update frequency, task adaptation, provenance, privacy and measured answer quality on the same use case. |
| BANK-001-030 | How do document chunk boundaries change retrieval results? | Compare headings, tables, overlap and chunk length against a fixed question set with source-grounded scoring. |
| BANK-001-031 | What makes a retrieved passage relevant but insufficient for an answer? | Separate topical similarity, entailment, missing qualifiers and conflicting sources using annotated examples. |
| BANK-001-032 | How should a system answer when its retrieved documents disagree? | Preserve dates, authority and exact claims; compare abstention and attributed disagreement instead of silently merging answers. |

## 05. Hardware and serving

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-033 | Where does GPU memory go when a model is loaded and used? | Separate weights, activations, caches and runtime overhead; measure one version and workload rather than quoting a universal requirement. |
| BANK-001-034 | How does quantization trade memory savings against output quality? | Compare bit widths, calibration assumptions, tasks and hardware support with matched evaluation conditions. |
| BANK-001-035 | Why can a smaller local model respond faster than a larger remote model? | Measure compute, memory bandwidth, prompt length, network latency and batching instead of attributing speed to parameter count alone. |
| BANK-001-036 | When does batching improve throughput while worsening an individual request's latency? | Use a queueing example and distinguish tokens per second, time to first token and end-to-end completion time. |
| BANK-001-037 | How do speculative decoding and ordinary decoding differ operationally? | Explain draft verification and acceptance behavior; inspect a published implementation without assuming every workload benefits. |

## 06. Reliability and evaluation

**Level:** advanced. **Evidence direction:** Use original observations or experiments, an appropriate scientific reference and the actual measurement method. Distinguish mechanisms, correlations, model assumptions, uncertainty and limits of generalization.

**Source types to locate:** original research reports and data; research-institution observation records; methods papers and current scientific reference works. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-038 | How can an answer sound certain while lacking supporting evidence? | Compare fluency, confidence wording and source support on a labeled set; do not infer internal certainty from tone. |
| BANK-001-039 | What does a useful hallucination evaluation need to count? | Define unsupported claims, contradicted claims, omissions and abstentions; use source-level adjudication and report disagreements. |
| BANK-001-040 | Why can two benchmarks rank the same models differently? | Compare task composition, prompts, scoring, contamination and uncertainty before treating one aggregate as universal capability. |
| BANK-001-041 | How can a model's refusal rate hide both safety gains and usability failures? | Distinguish correctly refused harmful tasks, benign refusals and unsafe completions in an explicitly authorized evaluation. |
| BANK-001-042 | What does calibration mean when a model reports a probability? | Compare claimed likelihood with observed correctness across bins; separate token probabilities from answer-level confidence. |

## 07. Human use and boundaries

**Level:** advanced. **Evidence direction:** Use the current official legal text, policy, procedure or public dataset for a specific jurisdiction and date. Distinguish written rules, implementation and lived access; give no personal legal or financial conclusion.

**Source types to locate:** official laws, rules and administrative guidance; audits, judgments and public service records; consented accounts from affected people and qualified specialists. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-043 | How should an AI interface distinguish a suggestion from an executed action? | Trace preview, authorization, execution and confirmation in a reversible example; record failures without claiming success. |
| BANK-001-044 | What information should accompany an AI-generated citation? | Check source existence, passage location, relevance, quotation accuracy and access date on actual examples. |
| BANK-001-045 | How do AI applications leak sensitive information through ordinary logging? | Map prompts, tool results, traces and retention policies in a documented architecture without exposing real private data. |
| BANK-001-046 | Why is prompt injection a system-boundary problem rather than only a wording problem? | Use benign authorized demonstrations to distinguish trusted instructions, untrusted documents, tool permissions and human review. |
| BANK-001-047 | How can a team compare AI productivity gains without measuring only output volume? | Evaluate task correctness, review effort, rework, costs and participant differences against a defined baseline. |

## 08. Economics and public claims

**Level:** advanced. **Evidence direction:** Define the rival claims and their evidence standards. Compare sources on equal terms, separate empirical findings from values or interpretations and do not imply that all positions have equal evidential support.

**Source types to locate:** the original sources behind the compared claims; explicit definitions and measurement methods; independent critiques with traceable evidence. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-048 | What belongs in the cost of an AI answer beyond token pricing? | Include retrieval, infrastructure, failed requests, review and maintenance using a clearly labeled workload model. |
| BANK-001-049 | How should energy comparisons separate training from serving? | State hardware, utilization, geography, measurement boundaries and workload; avoid assigning one universal footprint per query. |
| BANK-001-050 | When does an impressive AI demonstration fail to establish reliable autonomy? | Inspect hidden assistance, resets, task selection, failure disclosure and repeated trials rather than extrapolating from one edited clip. |
| BANK-001-051 | What evidence would justify calling an AI system open source? | Compare actual licenses and released components; distinguish access to weights, data, training code and modification rights. |
| BANK-001-052 | How can a model comparison remain useful after product versions change? | Publish exact versions, dates, prompts, settings and raw outcomes; define what must be rerun after an update. |

## 09. Classical machine learning and data problems

**Level:** foundation. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-053 | When does a decision tree suit a problem better than a language model? | Compare structured inputs, explainability and task-specific validation; do not generalize from one dataset. |
| BANK-001-054 | How does linear regression differ from predicting a category? | Trace targets, loss functions and assumptions using labeled illustrative data. |
| BANK-001-055 | What makes a dataset imbalanced rather than merely small? | Compare class frequencies, error costs and evaluation choices in a bounded classification task. |
| BANK-001-056 | How can missing values change a machine-learning result? | Inspect missingness patterns, preprocessing and leakage using a reproducible synthetic example. |
| BANK-001-057 | Why can a model fail after deployment even when its original test score was strong? | Distinguish distribution shift, label changes and implementation defects through documented measurements. |
| BANK-001-058 | What does clustering reveal without supplying verified real-world categories? | Compare distance choices, scaling and interpretation; avoid treating algorithmic groups as natural social identities. |
| BANK-001-059 | How does a recommendation system learn from feedback that its own rankings helped create? | Trace exposure, interaction and evaluation bias using original recommender research. |

## 10. Computer vision

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-060 | How do image classification, detection and segmentation answer different questions? | Compare outputs and annotation requirements on rights-cleared images. |
| BANK-001-061 | Why can an image classifier learn a background instead of the intended object? | Investigate spurious correlations with controlled image changes and held-out environments. |
| BANK-001-062 | What makes optical character recognition harder for tables than for plain paragraphs? | Separate recognition, reading order, cell structure and evaluation against source documents. |
| BANK-001-063 | How does an image embedding support similarity search without understanding every visual relationship? | Compare retrieval tasks, training objectives and documented failure cases. |
| BANK-001-064 | Why can depth estimation from one image remain ambiguous? | Inspect geometric assumptions, learned priors and ground-truth comparisons. |
| BANK-001-065 | How do video models represent change across time rather than only a sequence of pictures? | Compare temporal sampling, motion information and bounded benchmark tasks. |

## 11. Speech and audio intelligence

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-066 | How do speech recognition and speaker identification use different evidence? | Compare targets, enrollment and evaluation; exclude identification of unconsenting people. |
| BANK-001-067 | Why does separating overlapping voices remain difficult? | Inspect source overlap, recording conditions and task-specific separation metrics. |
| BANK-001-068 | How can an automatic transcript preserve code-switching between Hindi and English? | Evaluate aligned reference transcripts, language switches and named entities; report model version. |
| BANK-001-069 | What does a speech model's word-error rate hide about practical transcription quality? | Compare punctuation, speaker turns, names and meaning-changing errors. |
| BANK-001-070 | How can emotion recognition from speech confuse recording conditions with emotion? | Review primary validation studies, labels and population limits; avoid personal psychological inference. |

## 12. Robotics and embodied systems

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-071 | How does a robot turn sensor readings into an estimate of its location? | Explain a documented localization pipeline and uncertainty without providing hazardous deployment instructions. |
| BANK-001-072 | What distinguishes a robot's planned path from its actual movement? | Compare sensing, dynamics, control and obstacle uncertainty in a safe simulation. |
| BANK-001-073 | Why is grasping an unfamiliar object difficult even when recognition is accurate? | Separate shape, contact, friction and action feedback using published robotics experiments. |
| BANK-001-074 | How can simulation help robot training while introducing a reality gap? | Compare modeled physics, variation and measured transfer performance. |
| BANK-001-075 | What does shared control mean when a person and a robot both influence an action? | Inspect role allocation, overrides and user-study evidence in a defined application. |
| BANK-001-076 | How do warehouse robots differ from general-purpose household robots in task requirements? | Compare environments, objects, human presence and failure recovery; avoid universal autonomy rankings. |
| BANK-001-077 | Why does a robot demonstration require evidence about resets and human assistance? | Record interventions, retries, conditions and actual success definitions. |

## 13. Agents, tools and action systems

**Level:** advanced. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-078 | How does a tool-calling model obtain information that is absent from its context? | Trace schemas, arguments, execution and returned evidence in an original harmless task. |
| BANK-001-079 | What separates an agent's plan from a verified completed action? | Compare intended steps, tool outcomes and persistent state checks. |
| BANK-001-080 | How can a tool failure propagate into an agent's later decisions? | Use a sandboxed missing-file example; inspect retries, stale assumptions and stop conditions. |
| BANK-001-081 | Why does a long-running agent need checkpoints outside its conversational memory? | Compare recovery, progress records and duplicate-action prevention. |
| BANK-001-082 | How can permissions be narrowed to the task an AI agent actually needs? | Map read, write and external-action privileges using placeholder resources. |
| BANK-001-083 | What makes a human approval useful at an agent's decision boundary? | Compare reviewable evidence, scope and reversibility; avoid asking users to approve unspecified future actions. |
| BANK-001-084 | How can an agent recover after another process changes the same file? | Explain version guards, conflict detection and preservation using disposable local records. |

## 14. AI systems beyond neural text generation

**Level:** intermediate. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-085 | What does a knowledge graph represent differently from a text embedding? | Compare entities, relations, provenance and query behavior on an original small dataset. |
| BANK-001-086 | How can a rule engine outperform a learned model on a tightly specified task? | Compare coverage, maintenance, uncertainty and explicit exceptions. |
| BANK-001-087 | What do constraint solvers contribute to planning problems? | Model an illustrative timetable with declared constraints; distinguish feasibility from optimality. |
| BANK-001-088 | How does reinforcement learning define feedback differently from supervised labels? | Trace state, action, reward and evaluation in a safe toy environment. |
| BANK-001-089 | Why can a reward function encourage behavior its designer did not intend? | Compare objective specification and observed behavior in published or simulated examples. |
| BANK-001-090 | How does a digital twin differ from a visually accurate 3D model? | Inspect data connections, update rules, validation and the intended decision. |

## 15. Infrastructure and distributed computing

**Level:** advanced. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-091 | Why can network communication limit distributed model training? | Compare compute, synchronization, bandwidth and documented workload measurements. |
| BANK-001-092 | How do edge and cloud inference divide latency, privacy and maintenance responsibilities? | Map actual data flows and update mechanisms for a bounded application. |
| BANK-001-093 | What does an accelerator's advertised operation count omit about usable AI speed? | Compare precision, memory movement, software and realistic measured tasks. |
| BANK-001-094 | How do checkpoint formats affect moving a model between runtimes? | Inspect documented architectures, tensor formats, tokenizer dependencies and compatibility limits. |
| BANK-001-095 | Why can serving many model versions become an operational problem? | Trace routing, reproducibility, rollback and monitoring in an illustrative deployment. |

## 16. Security, privacy and governance

**Level:** advanced. **Evidence direction:** Inspect the actual product version, official documentation, terms and privacy policies. Test claims under stated conditions and distinguish account permissions, data retention, measured functionality and marketing.

**Source types to locate:** official versioned documentation and release notes; dated privacy policies and service terms; reproducible product tests and original validation reports. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-096 | How can training-data membership be studied without claiming access to a model's full dataset? | Review original privacy research and limits; exclude targeting private individuals. |
| BANK-001-097 | What does federated learning keep local and what can still be disclosed? | Trace parameters, updates, aggregation and documented threat assumptions. |
| BANK-001-098 | How does differential privacy define a protection differently from removing names? | Use primary definitions and clearly illustrative examples; do not certify a real dataset. |
| BANK-001-099 | Why can red-team findings fail to establish the overall safety of a system? | Inspect attack coverage, sampling, reproducibility and untested conditions. |
| BANK-001-100 | What does a model card disclose that marketing often leaves implicit? | Compare intended uses, training disclosures, evaluations and limitations in an actual versioned card. |
| BANK-001-101 | How can an organization trace responsibility when an AI component is supplied by another company? | Map contracts, controls, monitoring and applicable official requirements; avoid legal conclusions about a specific deployment. |

## 17. Data labor, language and access

**Level:** advanced. **Evidence direction:** Use consented participant accounts, local records and the community's own descriptions. Include differences of position, access and power; testimony is not a representative survey or clinical proof.

**Source types to locate:** consented interviews and oral histories; community publications and local records; field notes with method and consent documented. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-102 | How do annotation instructions shape what a dataset calls correct? | Compare guidelines, disagreement and adjudication using consented or public research records. |
| BANK-001-103 | Why do low-resource languages need evaluation beyond translating an English benchmark? | Inspect dialect, script, tasks, cultural context and qualified reference judgments. |
| BANK-001-104 | How can an AI dataset document permission without implying every ethical question is settled? | Trace licenses, consent scope, provenance and withdrawal limits. |
| BANK-001-105 | What does accessibility testing reveal that a general AI benchmark can miss? | Use consented assistive tasks, error consequences and actual user requirements. |
| BANK-001-106 | How can annotation work be described without erasing annotators' expertise? | Use attributed accounts of decisions, working conditions and compensation where documented. |

## 18. Emerging technology and claim testing

**Level:** advanced. **Evidence direction:** Define the rival claims and their evidence standards. Compare sources on equal terms, separate empirical findings from values or interpretations and do not imply that all positions have equal evidential support.

**Source types to locate:** the original sources behind the compared claims; explicit definitions and measurement methods; independent critiques with traceable evidence. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-107 | How can quantum-computing claims separate a demonstration from a useful application? | Compare problem, baseline, error conditions and primary experimental evidence. |
| BANK-001-108 | What does a brain-computer-interface demonstration actually establish about communication? | Inspect population, hardware, calibration and independently measured outcomes; exclude medical promises. |
| BANK-001-109 | How can an augmented-reality system align digital objects with a moving environment? | Compare tracking, mapping, latency and documented failure conditions. |
| BANK-001-110 | Why can a synthetic dataset reproduce biases from its generating system? | Inspect generation assumptions, diversity checks and downstream evaluation. |
| BANK-001-111 | What evidence distinguishes genuine on-device AI from a cloud-backed interface? | Use official architecture, permissions and controlled offline tests without inferring unseen backend behavior. |

## 19. Causal questions and identification

**Level:** foundation. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-112 | How does intervening on a variable differ from observing it in a causal model? | Build a synthetic three-variable graph and compare conditioning with a defined intervention; consult original causal-model formulations and keep the illustration separate from a real causal finding. |
| BANK-001-113 | Why can adjusting for an extra variable introduce bias rather than remove it? | Contrast a common cause with a collider in two explicit causal diagrams; show which paths are opened under stated assumptions rather than recommending adjustment by correlation strength. |
| BANK-001-114 | What makes a causal effect identifiable from the available data? | Use two causal explanations compatible with one observational distribution and specify what intervention or assumption would distinguish them; exclude the claim that more samples always resolve identification. |
| BANK-001-115 | How can a causal-discovery algorithm produce several equally compatible graphs? | Inspect equivalence classes, conditional-independence tests and hidden-variable assumptions using an original paper and synthetic data; separate graph recovery under assumptions from discovery of real-world mechanisms. |
| BANK-001-116 | What must be assumed before answering a counterfactual about one individual? | Contrast population intervention effects with an individual counterfactual in a structural model; expose unobservable assumptions and avoid personal medical or legal predictions. |

## 20. Interpreting model internals and testing explanations

**Level:** advanced. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-117 | What does a feature-attribution map explain when two input features encode the same information? | Compare correlated synthetic features, background distributions and attribution choices; distinguish allocation of predictive credit from causal importance in the world. |
| BANK-001-118 | How can a saliency map be tested for dependence on the model it claims to explain? | Plan parameter- and label-randomization controls from original interpretability research; assess changes in the explanation rather than judging only whether a picture looks plausible. |
| BANK-001-119 | What evidence is needed before calling a model component a circuit for a behavior? | Trace activation observations, intervention tests, controls and generalization across inputs in a published mechanistic study; distinguish a useful local hypothesis from a complete algorithmic account. |
| BANK-001-120 | Why can probing a hidden representation fail to show that the model uses the decoded information? | Compare probe capacity, baselines and causal intervention on a bounded representation task; do not equate decodability with functional reliance. |
| BANK-001-121 | How can an explanation remain stable while a model's decision changes? | Specify input perturbations, prediction differences and explanation similarity in a reproducible evaluation; separate explanation robustness from prediction correctness or user satisfaction. |

## 21. Compilers, kernels and measured inference

**Level:** advanced. **Evidence direction:** Use the actual system documentation, a worked implementation and measurements. Identify inputs, outputs, constraints, tolerances, failure conditions and the limits of the example. Do not provide hazardous construction or unauthorized access procedures.

**Source types to locate:** original engineering papers; official versioned product or standards documentation; test reports and drawings with clear provenance. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-122 | What does kernel fusion remove from an AI inference workload? | Trace intermediate tensors, memory transfers and launch overhead in a documented small computation; benchmark matched precision and shapes without promising universal acceleration. |
| BANK-001-123 | Why can a faster attention implementation leave end-to-end response time almost unchanged? | Separate attention time, other operators, queueing and networking in a measured profile; apply an explicit bottleneck calculation rather than attributing all latency to one kernel. |
| BANK-001-124 | How do static and dynamic tensor shapes change compilation choices? | Compare tracing, recompilation, padding and graph specialization for a versioned runtime; distinguish compile time from steady-state execution and include irregular workloads. |
| BANK-001-125 | What does a roofline model reveal about a memory-bound inference operation? | Relate arithmetic intensity, measured bandwidth and attainable compute using an illustrative operator; document hardware and precision rather than treating peak specifications as observed performance. |
| BANK-001-126 | How can changing numerical precision alter both speed and reproducibility? | Compare tolerances, accumulation, supported operators and task outputs under controlled settings; exclude declaring numerical agreement proof of equal downstream quality. |

## 22. Scientific models and domain-specific evaluation

**Level:** advanced. **Evidence direction:** Use original observations or experiments, an appropriate scientific reference and the actual measurement method. Distinguish mechanisms, correlations, model assumptions, uncertainty and limits of generalization.

**Source types to locate:** original research reports and data; research-institution observation records; methods papers and current scientific reference works. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-127 | What does a protein-structure prediction fail to establish about a protein's biological function? | Plan comparison of coordinates, confidence, conformations, interactions and experimental assays using original structure papers; exclude inferring drug efficacy from an attractive model. |
| BANK-001-128 | How can a learned weather forecast be evaluated when extreme events are rare? | Inspect hindcast separation, lead times, spatial scales and tail-event metrics in original evaluations; distinguish average skill from reliable local emergency guidance. |
| BANK-001-129 | Why can a scientific surrogate model violate a conservation law despite a small average error? | Compare pointwise fit with mass or energy balance in a documented simulation task; test out-of-domain inputs without claiming the surrogate replaces all physical validation. |
| BANK-001-130 | What changes when an AI system proposes a molecule rather than demonstrating that it can be made? | Trace generation, synthesis feasibility, actual laboratory validation and selection bias from original reports; exclude chemical synthesis instructions or medical benefit claims. |

## 23. Assistive systems and clinical evaluation boundaries

**Level:** advanced. **Evidence direction:** Inspect current professional guidance and original studies for the exact population, intervention or measurement. Report comparators, absolute outcomes, uncertainty, harms and limits. Do not diagnose, prescribe or imply that education replaces professional care.

**Source types to locate:** current official clinical or public-health guidance; original trials, cohort studies or diagnostic-validation reports; study registrations, protocols and adverse-event records. These are requirements, not sources already inspected.

| ID | Specific episode question | Individually written scope and exclusions |
|---|---|---|
| BANK-001-131 | How should a screen-description model be evaluated with blind users rather than image-caption scores alone? | Define task completion, navigation, dangerous omissions and consented user feedback; use original assistive-technology studies and avoid treating sighted reviewers as substitutes for intended users. |
| BANK-001-132 | Why does retrospective medical-image accuracy not establish improved patient outcomes? | Separate dataset selection, external validation, prospective workflow, clinician behavior and clinical endpoints using original studies; exclude diagnostic advice or a deployment endorsement. |
| BANK-001-133 | How can an assistive speech interface accommodate people whose speech differs from its training sample? | Specify speaker-consented evaluation, personalization data, error recovery and task-level success; do not infer a person's competence or medical condition from recognition errors. |

## Coverage limits and next step

This is an expanded topic-bank draft, not exhaustive scholarship or a researched episode package. Each question has an individually written boundary. Source access, claim verification, current angle-scope review and publication approval remain pending. Add new branches and cases when they fill a real gap; no numeric topic cap applies.

Select an exact case, edition, population, jurisdiction or product version, inspect sources and refine the question before using the existing registry idea/depth planning workflow. These BANK IDs are catalog identities, not approved IDEA IDs. Existing Q1-Q42 defaults, production queues and approval gates are unchanged.

## Related niche homes

- [007 AI Tools / AI Tutorials](../007_ai_tools_ai_tutorials/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [337 AI Research](../337_ai_research/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [338 Developer AI](../338_developer_ai/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [531 AI Software Agents](../531_ai_software_agents/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
- [532 Large Language Model Systems](../532_large_language_model_systems/IN_DEPTH_TOPIC_BANK.md). Compare actual questions and keep one primary home for an episode.
