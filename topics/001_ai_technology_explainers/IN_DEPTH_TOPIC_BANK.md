# 001 — AI + Technology Explainers: main topic bank

Updated: 2026-10-23. **210 active proposals · 11 categories · 41 subcategories.** No topic quota or completeness claim.

Each question below is a specific video proposal. Its scope states what that video would cover. Category and subcategory introductions are navigation, not additional episodes.

**Proposal status:** sources have not been researched or verified for these bank records. Historical readiness/source notes in the separate registry idea bank retain their original meaning; this expansion does not promote any idea or certify any script.

[Status and reconciliation report](TOPICS_COVERED_REPORT.md) · [Editable bank](IN_DEPTH_TOPIC_BANK.json) · [Legacy status data](topics_status.json) · [Registry depth map](../../REGISTRY/Niches/001_ai_technology_explainers/Planning/TOPIC_MAP.md) · [Existing episode ideas](../../REGISTRY/Niches/001_ai_technology_explainers/IDEA_BANK.json)

## Reading order

Start with foundations in Categories 1–3. Continue through intermediate model, data and deployment explanations; finish with advanced evaluation, governance and frontier questions. Each subcategory lists prerequisites by stable CATALOG ID. Within it, topics run from foundation to advanced. IDs record identity, never learning order.

| Category | Foundation | Intermediate | Advanced |
|---|---:|---:|---:|
| [AI foundations and history](#domain-001-01) | 6 | 5 | 0 |
| [Learning, representations and causal questions](#domain-001-02) | 12 | 29 | 4 |
| [Model architectures and generated media](#domain-001-03) | 0 | 25 | 0 |
| [Data provenance, language and access](#domain-001-04) | 0 | 8 | 5 |
| [Retrieval, tools and deployed systems](#domain-001-05) | 0 | 10 | 10 |
| [Compute, infrastructure and performance](#domain-001-06) | 0 | 5 | 15 |
| [Evaluation, reliability and explanation](#domain-001-07) | 0 | 0 | 10 |
| [Security, alignment and human oversight](#domain-001-08) | 0 | 0 | 21 |
| [Economics, rights and social consequences](#domain-001-09) | 0 | 0 | 10 |
| [Applied AI, robotics and scientific systems](#domain-001-10) | 0 | 13 | 12 |
| [Emerging technologies and open questions](#domain-001-11) | 0 | 0 | 10 |

**Suggested learning sequence across categories:**

- **Foundation:** [Starting from zero](#catalog-001-e16) → [Classical machine learning and data problems](#catalog-001-e01) → [Representations and tokenization](#catalog-001-d01).
- **Intermediate:** [Neural learning mechanics](#catalog-001-e19) → [Training and learning](#catalog-001-d02) → [Classical learning choices](#catalog-001-e18) → [Architecture families and tradeoffs](#catalog-001-e20) → [Computer vision](#catalog-001-e02) → [Speech and audio intelligence](#catalog-001-e03) → [Image, audio and video generation](#catalog-001-e21) → [Collection, curation and data lifecycle](#catalog-001-e22) → [Inference and generation](#catalog-001-d03) → [Context and external knowledge](#catalog-001-d04) → [Hardware and serving](#catalog-001-d05) → [AI systems beyond neural text generation](#catalog-001-e06) → [Robotics and embodied systems](#catalog-001-e04) → [Everyday AI applications](#catalog-001-e26) → [How AI ideas became practical](#catalog-001-e17) → [Learning with scarce feedback](#catalog-001-e30) → [Scripts and cross-language retrieval](#catalog-001-e31).
- **Advanced:** [Causal questions and identification](#catalog-001-e11) → [Reliability and evaluation](#catalog-001-d06) → [Interpreting model internals and testing explanations](#catalog-001-e12) → [Agents, tools and action systems](#catalog-001-e05) → [Infrastructure and distributed computing](#catalog-001-e07) → [Compilers, kernels and measured inference](#catalog-001-e13) → [Human use and boundaries](#catalog-001-d07) → [Security, privacy and governance](#catalog-001-e08) → [Data labor, language and access](#catalog-001-e09) → [Economics and public claims](#catalog-001-d08) → [Alignment and oversight objectives](#catalog-001-e23) → [Synthetic media, identity and provenance](#catalog-001-e24) → [Rights, work and public accountability](#catalog-001-e25) → [Emerging technology and claim testing](#catalog-001-e10) → [Scientific models and domain-specific evaluation](#catalog-001-e14) → [Assistive systems and clinical evaluation boundaries](#catalog-001-e15) → [Frontier claims and conditional futures](#catalog-001-e27) → [Energy, cooling and hardware lifecycle](#catalog-001-e28) → [Deployment beyond the chatbot](#catalog-001-e29) → [Search selection and lifecycle controls](#catalog-001-e32) → [Longitudinal deployment and changing users](#catalog-001-e33).

The legacy roadmap is cross-referenced at the end. Its 27 records and the 12 archived starter records are excluded from the active count, because they are source records or superseded umbrellas. Registry TOP and IDEA IDs remain separate planning references.

## Scope of this niche

General AI and technology literacy for beginner through advanced viewers. Explain mechanisms, evidence limits and social consequences. Specialist developer builds, tool tutorials, primary research replication and clinical/legal advice retain their existing niche homes. A crossover subject receives a bounded literacy question here, not a duplicated specialist curriculum.

Topics about robots, agents and specialist systems explain mechanisms for a general viewer. Implementation tutorials, detailed engineering, research replication and medical or legal advice belong in their existing specialist homes. The all-niche index connects those neighboring proposal banks.

<a id="domain-001-01"></a>
## Category 1: AI foundations and history

Build vocabulary, distinguish learning from programming, and trace what historical systems actually attempted.

<a id="catalog-001-e16"></a>
### Starting from zero

Subcategory `CATALOG-001-E16` · Entry level: foundation · Prerequisites: None.

<a id="bank-001-134"></a>
#### BANK-001-134 — What counts as AI when a system follows rules instead of learning from examples?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Compare a thermostat rule, a search procedure and a learned classifier; identify inputs, decision rules and what changes with experience in an original diagram.

**Boundary:** No claim that a single definition settles every historical or commercial use of AI.

<a id="bank-001-135"></a>
#### BANK-001-135 — How are AI, machine learning, deep learning and generative AI related?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Build a nested concept map with rule systems, predictive models and generators; show overlapping capabilities and one counterexample to each misleading equivalence.

**Boundary:** Taxonomy introduction only; individual training and architecture tutorials are separate questions.

<a id="bank-001-136"></a>
#### BANK-001-136 — What changes during training that normally stays fixed during inference?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Follow a tiny model through fitting and prediction; distinguish parameters, temporary context, application memory and deliberate online updates.

**Boundary:** No assertion that every deployed system has frozen weights or learns from every conversation.

**Related coverage:** [BANK-001-018](#bank-001-018).

<a id="bank-001-137"></a>
#### BANK-001-137 — How can the same dataset support classification, regression and anomaly detection questions?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Reframe one illustrative sensor dataset around labels, continuous targets and unusual observations; compare what a useful answer would look like for each task.

**Boundary:** No comprehensive model-family survey or real-world anomaly diagnosis.

<a id="bank-001-138"></a>
#### BANK-001-138 — Why is a high probability prediction different from a guaranteed outcome?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Use an illustrative weather-like forecast to distinguish probability, uncertainty and a decision threshold; show why repeated outcomes matter.

**Boundary:** Keep probability literacy separate from the formal calibration evaluation in BANK-001-042.

<a id="bank-001-139"></a>
#### BANK-001-139 — What does a model parameter represent compared with an input feature?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Trace features, weights, bias and outputs in a two-input linear model; show how changing the input differs from changing the fitted rule.

**Boundary:** No analogy that equates one parameter with one stored fact or brain cell.

<a id="catalog-001-e17"></a>
### How AI ideas became practical

Subcategory `CATALOG-001-E17` · Entry level: intermediate · Prerequisites: [CATALOG-001-E16](#catalog-001-e16).

<a id="bank-001-140"></a>
#### BANK-001-140 — What did the Turing test ask, and which capabilities would it leave unmeasured?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Read the original imitation-game framing and compare conversational judgment with factuality, perception and task competence using explicitly hypothetical examples.

**Boundary:** No declaration that passing a conversation test establishes consciousness.

<a id="bank-001-141"></a>
#### BANK-001-141 — Why did expert systems need knowledge engineers as well as programmers?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace rules, a knowledge base, inference and maintenance in one documented historical system; explain where exceptions and changing knowledge create work.

**Boundary:** Do not turn one system's limits into a universal account of an AI winter.

<a id="bank-001-142"></a>
#### BANK-001-142 — How did a convolutional image classifier become a practical milestone rather than only a theoretical idea?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Follow a named historical image-classification result through data, compute, architecture and evaluation conditions; compare compatible baselines.

**Boundary:** Do not attribute progress to one inventor or architecture without evidence.

<a id="bank-001-143"></a>
#### BANK-001-143 — What did a game-playing AI learn that a board-game search engine handled differently?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare search, learned value estimates and self-play in two precisely identified historical systems; define the game's information and action space.

**Boundary:** Game performance is not evidence of general real-world competence.

<a id="bank-001-144"></a>
#### BANK-001-144 — Why did some earlier AI forecasts fail to predict deployment timelines?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Select a dated forecast and its specified task; inspect assumptions about data, cost, environment and reliability against subsequent documented outcomes.

**Boundary:** No blanket claim that all AI forecasts failed or that current progress must repeat the same cycle.

<a id="domain-001-02"></a>
## Category 2: Learning, representations and causal questions

Follow data, objectives and model learning before interpreting predictions or causal claims.

<a id="catalog-001-d01"></a>
### Representations and tokenization

Subcategory `CATALOG-001-D01` · Entry level: foundation · Prerequisites: None.

<a id="bank-001-013"></a>
#### BANK-001-013 — Why can the same sentence require different token counts in two models?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Compare vocabulary, normalization, byte handling and a fixed multilingual sample; separate tokens from words.

**Related coverage:** [BANK-001-014](#bank-001-014).

**Research follow-up:** [Case and source record](RESEARCH_NOTES/BANK-001-013.md) · `IDEA-001-0004` in the [existing idea bank](../../REGISTRY/Niches/001_ai_technology_explainers/IDEA_BANK.json).

<a id="bank-001-014"></a>
#### BANK-001-014 — How do subword vocabularies handle rare names and spelling mistakes?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Trace segmentation of controlled examples and examine the tradeoff between vocabulary size and sequence length.

**Related coverage:** [BANK-001-013](#bank-001-013).

<a id="bank-001-015"></a>
#### BANK-001-015 — What changes when text, images and audio share one model interface?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Separate modality encoders, representations, alignment and output tasks; avoid implying identical internal processing.

<a id="bank-001-016"></a>
#### BANK-001-016 — Why does numerical reasoning remain difficult for a text predictor?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Compare number representation, training examples, exact computation and tool-assisted answers on reproducible arithmetic tasks.

<a id="bank-001-017"></a>
#### BANK-001-017 — How does positional information let a transformer distinguish word order?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Explain an identified positional scheme with short examples; compare training context with longer inputs.

**Related coverage:** [BANK-001-157](#bank-001-157).

<a id="catalog-001-e01"></a>
### Classical machine learning and data problems

Subcategory `CATALOG-001-E01` · Entry level: foundation · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-053"></a>
#### BANK-001-053 — When does a decision tree suit a problem better than a language model?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Compare structured inputs, explainability and task-specific validation; do not generalize from one dataset.

<a id="bank-001-054"></a>
#### BANK-001-054 — How does linear regression differ from predicting a category?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Trace targets, loss functions and assumptions using labeled illustrative data.

<a id="bank-001-055"></a>
#### BANK-001-055 — What makes a dataset imbalanced rather than merely small?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Compare class frequencies, error costs and evaluation choices in a bounded classification task.

<a id="bank-001-056"></a>
#### BANK-001-056 — How can missing values change a machine-learning result?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Inspect missingness patterns, preprocessing and leakage using a reproducible synthetic example.

<a id="bank-001-057"></a>
#### BANK-001-057 — Why can a model fail after deployment even when its original test score was strong?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Distinguish distribution shift, label changes and implementation defects through documented measurements.

<a id="bank-001-058"></a>
#### BANK-001-058 — What does clustering reveal without supplying verified real-world categories?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Compare distance choices, scaling and interpretation; avoid treating algorithmic groups as natural social identities.

<a id="bank-001-059"></a>
#### BANK-001-059 — How does a recommendation system learn from feedback that its own rankings helped create?

Level: **foundation** · Status: proposed.

**Individual coverage scope:** Trace exposure, interaction and evaluation bias using original recommender research.

<a id="catalog-001-d02"></a>
### Training and learning

Subcategory `CATALOG-001-D02` · Entry level: intermediate · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-018"></a>
#### BANK-001-018 — What does next-token training teach beyond memorizing sentences?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Distinguish the prediction objective, learned statistical structure, generalization tests and examples that expose memorization.

**Related coverage:** [BANK-001-136](#bank-001-136).

<a id="bank-001-019"></a>
#### BANK-001-019 — Why are training, validation and test data kept separate?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace a small experiment and show how leakage changes the apparent performance estimate.

<a id="bank-001-020"></a>
#### BANK-001-020 — What happens during gradient descent in a language-model training step?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Follow loss, gradients, parameter updates and learning rate in a toy network rather than claiming access to proprietary training.

**Related coverage:** [BANK-001-152](#bank-001-152).

<a id="bank-001-021"></a>
#### BANK-001-021 — How do supervised instruction tuning and preference optimization differ?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare datasets, objectives, human judgments and evaluation; do not equate preference with factual accuracy.

<a id="bank-001-022"></a>
#### BANK-001-022 — Why can additional training data make an evaluation less trustworthy?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Examine benchmark overlap, near duplicates and the difference between legitimate learning and contaminated measurement.

<a id="catalog-001-e06"></a>
### AI systems beyond neural text generation

Subcategory `CATALOG-001-E06` · Entry level: intermediate · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-085"></a>
#### BANK-001-085 — What does a knowledge graph represent differently from a text embedding?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare entities, relations, provenance and query behavior on an original small dataset.

<a id="bank-001-086"></a>
#### BANK-001-086 — How can a rule engine outperform a learned model on a tightly specified task?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare coverage, maintenance, uncertainty and explicit exceptions.

<a id="bank-001-087"></a>
#### BANK-001-087 — What do constraint solvers contribute to planning problems?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Model an illustrative timetable with declared constraints; distinguish feasibility from optimality.

<a id="bank-001-088"></a>
#### BANK-001-088 — How does reinforcement learning define feedback differently from supervised labels?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace state, action, reward and evaluation in a safe toy environment.

<a id="bank-001-089"></a>
#### BANK-001-089 — Why can a reward function encourage behavior its designer did not intend?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare objective specification and observed behavior in published or simulated examples.

<a id="bank-001-090"></a>
#### BANK-001-090 — How does a digital twin differ from a visually accurate 3D model?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Inspect data connections, update rules, validation and the intended decision.

<a id="catalog-001-e11"></a>
### Causal questions and identification

Subcategory `CATALOG-001-E11` · Entry level: intermediate · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-112"></a>
#### BANK-001-112 — How does intervening on a variable differ from observing it in a causal model?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Build a synthetic three-variable graph and compare conditioning with a defined intervention; consult original causal-model formulations and keep the illustration separate from a real causal finding.

<a id="bank-001-113"></a>
#### BANK-001-113 — Why can adjusting for an extra variable introduce bias rather than remove it?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Contrast a common cause with a collider in two explicit causal diagrams; show which paths are opened under stated assumptions rather than recommending adjustment by correlation strength.

<a id="bank-001-114"></a>
#### BANK-001-114 — What makes a causal effect identifiable from the available data?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Use two causal explanations compatible with one observational distribution and specify what intervention or assumption would distinguish them; exclude the claim that more samples always resolve identification.

<a id="bank-001-115"></a>
#### BANK-001-115 — How can a causal-discovery algorithm produce several equally compatible graphs?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Inspect equivalence classes, conditional-independence tests and hidden-variable assumptions using an original paper and synthetic data; separate graph recovery under assumptions from discovery of real-world mechanisms.

<a id="bank-001-116"></a>
#### BANK-001-116 — What must be assumed before answering a counterfactual about one individual?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Contrast population intervention effects with an individual counterfactual in a structural model; expose unobservable assumptions and avoid personal medical or legal predictions.

<a id="catalog-001-e18"></a>
### Classical learning choices

Subcategory `CATALOG-001-E18` · Entry level: intermediate · Prerequisites: [CATALOG-001-E16](#catalog-001-e16).

<a id="bank-001-145"></a>
#### BANK-001-145 — How does a nearest-neighbor classifier decide which examples are similar?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Work through scaling, distance and neighborhood size on a small numeric dataset; compare a changed feature scale and an ambiguous boundary.

**Boundary:** Do not repeat text-embedding search or claim that distance defines semantic truth.

<a id="bank-001-146"></a>
#### BANK-001-146 — Why can combining many decision trees change predictive behavior?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare a single tree with bagging and sequential error correction on a declared dataset; separate variance, bias and validation outcomes.

**Boundary:** No automatic claim that an ensemble always beats a simpler model.

<a id="bank-001-147"></a>
#### BANK-001-147 — What does regularization discourage when a model fits noisy data?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare fit and held-out behavior as a stated penalty changes in a toy regression; distinguish parameter constraints from collecting better data.

**Boundary:** No universal rule that smaller weights always mean a more useful model.

<a id="bank-001-148"></a>
#### BANK-001-148 — Why can a time-series split be more realistic than a random split?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace forecast time, feature availability and future leakage in an illustrative sequence; compare rolling evaluation with random partitioning.

**Boundary:** The focus is temporal information availability, not the basic three-way split already in BANK-001-019.

<a id="bank-001-149"></a>
#### BANK-001-149 — How does collaborative filtering recommend an item without reading its description?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace a small user-item interaction matrix, latent preferences and cold-start cases; distinguish collaborative feedback from content matching.

**Boundary:** Feedback loops and exposure bias remain the separate inquiry in BANK-001-059.

<a id="bank-001-150"></a>
#### BANK-001-150 — What makes anomaly detection difficult when unusual events are not necessarily faults?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare a changing baseline, rare valid behavior and labeled failures in a synthetic monitoring task; define thresholds and false alerts.

**Boundary:** No diagnosis of security incidents or machinery safety from a generic detector score.

<a id="catalog-001-e19"></a>
### Neural learning mechanics

Subcategory `CATALOG-001-E19` · Entry level: intermediate · Prerequisites: [CATALOG-001-E16](#catalog-001-e16).

<a id="bank-001-151"></a>
#### BANK-001-151 — How do layers and activation functions let a neural network represent a nonlinear pattern?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace inputs, weighted sums, biases and activations through a small original network; compare its decision boundary with a linear baseline.

**Boundary:** A layer diagram does not prove biological similarity or explain every learned feature.

<a id="bank-001-152"></a>
#### BANK-001-152 — How does backpropagation assign responsibility for a prediction error?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Follow the chain rule through a two-layer scalar example and label forward values, local derivatives and gradients before an update.

**Boundary:** Separate derivative calculation from the optimizer update covered in BANK-001-020.

**Related coverage:** [BANK-001-020](#bank-001-020).

<a id="bank-001-153"></a>
#### BANK-001-153 — Why can a learning rate that works initially become unsuitable later?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare overshooting, slow progress, warm-up and decay on a controlled loss surface; distinguish learning-rate scheduling from model selection.

**Boundary:** No universal numeric learning-rate prescription.

<a id="bank-001-154"></a>
#### BANK-001-154 — How do transfer learning and training from scratch use prior knowledge differently?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare a frozen feature extractor, partial adaptation and full retraining on one small task; account for data requirements and negative transfer.

**Boundary:** Do not repeat the retrieval-versus-fine-tuning application decision in BANK-001-029.

<a id="bank-001-155"></a>
#### BANK-001-155 — What does self-supervised learning use as a target when people have not labeled every example?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Contrast masked inputs, next-element prediction and contrastive pairs; identify how targets are constructed and what assumptions enter them.

**Boundary:** No claim that the absence of manual labels removes human data selection or bias.

<a id="bank-001-156"></a>
#### BANK-001-156 — Why can a model lose earlier abilities when it learns a new task?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare sequential updates, replay and held-out old-task evaluation in an illustrative continual-learning setup.

**Boundary:** Distinguish changing model parameters from forgetting information in a chat context.

<a id="catalog-001-e30"></a>
### Learning with scarce feedback

Subcategory `CATALOG-001-E30` · Entry level: intermediate · Prerequisites: None.

<a id="bank-001-211"></a>
#### BANK-001-211 — What does principal-component analysis preserve when it reduces a dataset to fewer dimensions?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Follow centered synthetic features, variance directions, projection and reconstruction loss; distinguish a visually separated projection from validated classes or causal factors.

<a id="bank-001-212"></a>
#### BANK-001-212 — How can active learning choose which examples a person should label next?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare uncertainty sampling, diversity and a random-label baseline at a fixed annotation budget; examine biased sampling and an independent test set.

<a id="bank-001-213"></a>
#### BANK-001-213 — Why does a contextual bandit need to explore options that currently look worse?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace actions, partial feedback, exploration cost and regret in a fictional recommendation task; distinguish one-step feedback from multi-step reinforcement learning.

<a id="bank-001-214"></a>
#### BANK-001-214 — What does knowledge distillation transfer from a teacher model to a smaller student?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare training targets, student capacity, matched-task outcomes and inherited errors; distinguish learning from teacher outputs from reducing the bit width of unchanged weights.

<a id="bank-001-215"></a>
#### BANK-001-215 — How can a low-rank adapter change a model without updating every stored weight?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Illustrate a weight update as a product of smaller matrices; separate trainable parameters, retained base weights and task evaluation from a tutorial or universal memory promise.

<a id="domain-001-03"></a>
## Category 3: Model architectures and generated media

Explain how different model families handle text, images, audio and video, including their different limitations.

<a id="catalog-001-e02"></a>
### Computer vision

Subcategory `CATALOG-001-E02` · Entry level: intermediate · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-060"></a>
#### BANK-001-060 — How do image classification, detection and segmentation answer different questions?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare outputs and annotation requirements on rights-cleared images.

<a id="bank-001-061"></a>
#### BANK-001-061 — Why can an image classifier learn a background instead of the intended object?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Investigate spurious correlations with controlled image changes and held-out environments.

<a id="bank-001-062"></a>
#### BANK-001-062 — What makes optical character recognition harder for tables than for plain paragraphs?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Separate recognition, reading order, cell structure and evaluation against source documents.

<a id="bank-001-063"></a>
#### BANK-001-063 — How does an image embedding support similarity search without understanding every visual relationship?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare retrieval tasks, training objectives and documented failure cases.

<a id="bank-001-064"></a>
#### BANK-001-064 — Why can depth estimation from one image remain ambiguous?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Inspect geometric assumptions, learned priors and ground-truth comparisons.

<a id="bank-001-065"></a>
#### BANK-001-065 — How do video models represent change across time rather than only a sequence of pictures?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare temporal sampling, motion information and bounded benchmark tasks.

<a id="catalog-001-e03"></a>
### Speech and audio intelligence

Subcategory `CATALOG-001-E03` · Entry level: intermediate · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-066"></a>
#### BANK-001-066 — How do speech recognition and speaker identification use different evidence?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare targets, enrollment and evaluation; exclude identification of unconsenting people.

<a id="bank-001-067"></a>
#### BANK-001-067 — Why does separating overlapping voices remain difficult?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Inspect source overlap, recording conditions and task-specific separation metrics.

<a id="bank-001-068"></a>
#### BANK-001-068 — How can an automatic transcript preserve code-switching between Hindi and English?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Evaluate aligned reference transcripts, language switches and named entities; report model version.

<a id="bank-001-069"></a>
#### BANK-001-069 — What does a speech model's word-error rate hide about practical transcription quality?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare punctuation, speaker turns, names and meaning-changing errors.

<a id="bank-001-070"></a>
#### BANK-001-070 — How can emotion recognition from speech confuse recording conditions with emotion?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Review primary validation studies, labels and population limits; avoid personal psychological inference.

<a id="catalog-001-e20"></a>
### Architecture families and tradeoffs

Subcategory `CATALOG-001-E20` · Entry level: intermediate · Prerequisites: [CATALOG-001-E19](#catalog-001-e19).

<a id="bank-001-157"></a>
#### BANK-001-157 — What does self-attention combine in the original Transformer architecture?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace queries, keys, values and residual processing in a small original encoder-decoder example; preserve the historical paper's scope and distinguish attention weights from explanations.

**Boundary:** The existing IDEA-001-0001 is the source-based case route; this is not an extra parallel production idea.

**Related coverage:** [BANK-001-017](#bank-001-017).

<a id="bank-001-158"></a>
#### BANK-001-158 — How do recurrent networks retain sequence state differently from Transformers?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace an RNN and an LSTM across a short sequence; compare state compression, sequence order and training parallelism with a specified Transformer.

**Boundary:** Do not claim that recurrence disappeared or that one architecture wins on every task.

<a id="bank-001-159"></a>
#### BANK-001-159 — What changes when a model routes tokens through a mixture of experts?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Explain routing, selected experts, shared components and active versus stored parameters; compare workload balance and communication conceptually.

**Boundary:** Do not infer inference cost from total parameter count alone.

<a id="bank-001-160"></a>
#### BANK-001-160 — How does an autoencoder learn a compressed representation without directly predicting a label?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace encoding, a bottleneck and reconstruction on rights-cleared or synthetic inputs; distinguish compression quality from useful latent structure.

**Boundary:** Do not equate reconstruction with understanding or cover diffusion generation here.

<a id="bank-001-161"></a>
#### BANK-001-161 — What distinguishes a generative adversarial network from a variational autoencoder?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare generator-discriminator training with latent-variable reconstruction and sampling in original diagrams; discuss diversity and training stability as evaluation questions.

**Boundary:** No claim that either family is universally obsolete or superior.

<a id="bank-001-162"></a>
#### BANK-001-162 — How do state-space sequence models change the computation used for long inputs?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Explain state updates and a specified model's sequence processing; compare memory and retrieval behavior under matched tasks.

**Boundary:** No speculative claim that a family will replace Transformers.

<a id="catalog-001-e21"></a>
### Image, audio and video generation

Subcategory `CATALOG-001-E21` · Entry level: intermediate · Prerequisites: [CATALOG-001-E19](#catalog-001-e19).

<a id="bank-001-163"></a>
#### BANK-001-163 — How can an image generator learn to reverse a noise process?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace forward noising, learned denoising, conditioning and a latent representation in one documented diffusion design; distinguish learned approximation from physical image formation.

**Boundary:** Do not imply that every modern image generator uses a U-Net or identical training objective.

**Related coverage:** [BANK-001-164](#bank-001-164).

<a id="bank-001-164"></a>
#### BANK-001-164 — What does guidance change when a diffusion model follows a text prompt?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare conditional and unconditional predictions in an original conceptual diagram; examine prompt adherence, variation and artifacts at fixed sampling conditions.

**Boundary:** This is the conditioning tradeoff, not a repeat of the entire diffusion pipeline.

**Related coverage:** [BANK-001-163](#bank-001-163).

<a id="bank-001-165"></a>
#### BANK-001-165 — How do inpainting and image-to-image generation constrain what may change?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Map masks, reference inputs, noise strength and boundary artifacts on rights-cleared examples; define which regions or attributes an evaluation checks.

**Boundary:** No guarantee that unmasked details or a person's identity will remain exactly preserved.

<a id="bank-001-166"></a>
#### BANK-001-166 — Why is a plausible still frame insufficient for a coherent generated video?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Separate object persistence, motion, occlusion, temporal identity and scene transitions; design a short original test sequence with declared checks.

**Boundary:** Do not repeat video-understanding representations in BANK-001-065.

<a id="bank-001-167"></a>
#### BANK-001-167 — How can generated speech preserve a speaker's timbre while changing the words?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace text processing, acoustic representations, vocoding and speaker conditioning in a documented system; distinguish timbre from identity and authorization.

**Boundary:** Use consented examples; no impersonation workflow or claim that all voices can be replicated faithfully.

**Related coverage:** [BANK-001-182](#bank-001-182).

<a id="bank-001-168"></a>
#### BANK-001-168 — What is the difference between generating music and separating instruments from an existing recording?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Contrast conditional synthesis with source separation, inputs, outputs and evaluation criteria using original or licensed audio.

**Boundary:** Licensing and attribution remain separate from technical capability.

<a id="bank-001-169"></a>
#### BANK-001-169 — What does text-image alignment fail to measure about a generated picture?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare prompt relevance, spatial relations, legible text and depiction errors in controlled prompts; separate aesthetic preference from task correctness.

**Boundary:** Embedding similarity alone is not an image-factuality score.

<a id="bank-001-170"></a>
#### BANK-001-170 — Why can generated images repeat visual stereotypes even when a prompt contains no demographic instruction?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Design a clearly bounded comparison across repeated prompts, labels and sampling settings; inspect ambiguity, variation and evaluation judgments.

**Boundary:** Do not infer population-level prevalence or the exact training data from a few outputs.

<a id="domain-001-04"></a>
## Category 4: Data provenance, language and access

Examine data collection, documentation, language coverage and the people who make datasets usable.

<a id="catalog-001-e22"></a>
### Collection, curation and data lifecycle

Subcategory `CATALOG-001-E22` · Entry level: intermediate · Prerequisites: [CATALOG-001-E16](#catalog-001-e16).

<a id="bank-001-171"></a>
#### BANK-001-171 — What happens between collecting web pages and producing a training dataset?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace crawling, extraction, filtering, deduplication and exclusions in a documented dataset; separate observed records from unknown proprietary practices.

**Boundary:** Collection access does not establish permission or copyright compliance.

<a id="bank-001-172"></a>
#### BANK-001-172 — How can deduplication change what a model learns from a dataset?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare exact and near duplicates, repeated sources and weighting on a controlled corpus; evaluate diversity and contamination separately.

**Boundary:** Benchmark overlap remains the distinct measurement question in BANK-001-022.

<a id="bank-001-173"></a>
#### BANK-001-173 — What does a trainable example look like after text and images have been paired?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace pairing, captions, quality filtering and misalignment using an original miniature dataset; show why a pair can be misleading.

**Boundary:** Do not assume co-occurrence proves a correct description or meaningful consent.

<a id="bank-001-174"></a>
#### BANK-001-174 — How does data poisoning differ from an accidental dataset error?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Contrast origin, intent, distribution and resulting behavior using harmless synthetic labels; identify evidence required to attribute deliberate manipulation.

**Boundary:** No instructions for compromising public datasets or live systems.

<a id="bank-001-175"></a>
#### BANK-001-175 — What can deleting a source document change after a model has already been trained?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Separate storage deletion, retrieval removal, retraining and machine-unlearning evaluation; define the system version and residual disclosure tests.

**Boundary:** No promise that removal from one database removes every learned influence or copy.

<a id="catalog-001-e31"></a>
### Scripts and cross-language retrieval

Subcategory `CATALOG-001-E31` · Entry level: intermediate · Prerequisites: None.

<a id="bank-001-216"></a>
#### BANK-001-216 — Why can visually identical text have different character sequences in an AI dataset?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare composed and combining-character forms, normalization and span offsets with a declared Unicode sample; inspect matching and annotation errors rather than infer meaning from byte equality.

<a id="bank-001-217"></a>
#### BANK-001-217 — How can transliterated names prevent a document search from finding the right source?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare native-script, Romanized and variant-spelling queries for a consented or fictional entity; distinguish entity resolution and retrieval recall from the quality of a generated translation.

<a id="bank-001-218"></a>
#### BANK-001-218 — How can a tokenizer comparison separate morphological structure from the length of a written word?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Use qualified annotations for a declared language pair with different word-formation patterns; inspect segmentation, length-normalized task errors and vocabulary coverage without ranking languages as intrinsically harder.

<a id="catalog-001-e09"></a>
### Data labor, language and access

Subcategory `CATALOG-001-E09` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-102"></a>
#### BANK-001-102 — How do annotation instructions shape what a dataset calls correct?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare guidelines, disagreement and adjudication using consented or public research records.

<a id="bank-001-103"></a>
#### BANK-001-103 — Why do low-resource languages need evaluation beyond translating an English benchmark?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Inspect dialect, script, tasks, cultural context and qualified reference judgments.

<a id="bank-001-104"></a>
#### BANK-001-104 — How can an AI dataset document permission without implying every ethical question is settled?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace licenses, consent scope, provenance and withdrawal limits.

<a id="bank-001-105"></a>
#### BANK-001-105 — What does accessibility testing reveal that a general AI benchmark can miss?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Use consented assistive tasks, error consequences and actual user requirements.

<a id="bank-001-106"></a>
#### BANK-001-106 — How can annotation work be described without erasing annotators' expertise?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Use attributed accounts of decisions, working conditions and compensation where documented.

<a id="domain-001-05"></a>
## Category 5: Retrieval, tools and deployed systems

Trace the path from a model response to retrieved evidence or an executed action, including boundaries and failures.

<a id="catalog-001-d03"></a>
### Inference and generation

Subcategory `CATALOG-001-D03` · Entry level: intermediate · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-023"></a>
#### BANK-001-023 — How does a model choose the next token from its output scores?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Work through logits, probabilities and selection using a small hypothetical vocabulary with explicitly illustrative numbers.

**Related coverage:** [BANK-001-024](#bank-001-024).

<a id="bank-001-024"></a>
#### BANK-001-024 — Why do temperature and top-p produce different kinds of variation?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare repeated generations from the same distribution while controlling prompt, model version and sampling settings.

**Related coverage:** [BANK-001-023](#bank-001-023).

<a id="bank-001-025"></a>
#### BANK-001-025 — What does a key-value cache store during text generation?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace repeated attention work, cache growth and memory use; distinguish stored activations from permanent model knowledge.

<a id="bank-001-026"></a>
#### BANK-001-026 — Why does generating the first token often take longer than later tokens?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Separate prompt processing, decoding, batching and network delay using a measured serving trace.

<a id="bank-001-027"></a>
#### BANK-001-027 — Can a model give different answers when sampling is disabled?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Investigate hardware kernels, server settings, version changes and numerical nondeterminism before assigning one cause.

<a id="catalog-001-d04"></a>
### Context and external knowledge

Subcategory `CATALOG-001-D04` · Entry level: intermediate · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-028"></a>
#### BANK-001-028 — Why can information in a long context still be overlooked?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Test information placement, distractors, retrieval tasks and answer scoring; distinguish advertised length from effective use.

<a id="bank-001-029"></a>
#### BANK-001-029 — When should an application retrieve documents instead of fine-tuning a model?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare update frequency, task adaptation, provenance, privacy and measured answer quality on the same use case.

<a id="bank-001-030"></a>
#### BANK-001-030 — How do document chunk boundaries change retrieval results?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare headings, tables, overlap and chunk length against a fixed question set with source-grounded scoring.

<a id="bank-001-031"></a>
#### BANK-001-031 — What makes a retrieved passage relevant but insufficient for an answer?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Separate topical similarity, entailment, missing qualifiers and conflicting sources using annotated examples.

**Related coverage:** [BANK-001-044](#bank-001-044).

<a id="bank-001-032"></a>
#### BANK-001-032 — How should a system answer when its retrieved documents disagree?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Preserve dates, authority and exact claims; compare abstention and attributed disagreement instead of silently merging answers.

<a id="catalog-001-e05"></a>
### Agents, tools and action systems

Subcategory `CATALOG-001-E05` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-078"></a>
#### BANK-001-078 — How does a tool-calling model obtain information that is absent from its context?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace schemas, arguments, execution and returned evidence in an original harmless task.

<a id="bank-001-079"></a>
#### BANK-001-079 — What separates an agent's plan from a verified completed action?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare intended steps, tool outcomes and persistent state checks.

<a id="bank-001-080"></a>
#### BANK-001-080 — How can a tool failure propagate into an agent's later decisions?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Use a sandboxed missing-file example; inspect retries, stale assumptions and stop conditions.

<a id="bank-001-081"></a>
#### BANK-001-081 — Why does a long-running agent need checkpoints outside its conversational memory?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare recovery, progress records and duplicate-action prevention.

<a id="bank-001-082"></a>
#### BANK-001-082 — How can permissions be narrowed to the task an AI agent actually needs?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Map read, write and external-action privileges using placeholder resources.

<a id="bank-001-083"></a>
#### BANK-001-083 — What makes a human approval useful at an agent's decision boundary?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare reviewable evidence, scope and reversibility; avoid asking users to approve unspecified future actions.

**Related coverage:** [BANK-001-043](#bank-001-043).

<a id="bank-001-084"></a>
#### BANK-001-084 — How can an agent recover after another process changes the same file?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Explain version guards, conflict detection and preservation using disposable local records.

<a id="catalog-001-e32"></a>
### Search selection and lifecycle controls

Subcategory `CATALOG-001-E32` · Entry level: advanced · Prerequisites: None.

<a id="bank-001-219"></a>
#### BANK-001-219 — What does a reranker decide after a document retriever has already selected candidates?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace candidate generation, relevance scores, ordering and missing-candidate limits in a small controlled collection; evaluate retrieval recall separately from reranking precision and final answer support.

<a id="bank-001-220"></a>
#### BANK-001-220 — What must an application retire when a model endpoint is withdrawn?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Map versioned prompts, evaluation baselines, dependent tools, stored embeddings and fallback behavior in a hypothetical migration; separate replacing a service from disposing of physical hardware.

<a id="bank-001-221"></a>
#### BANK-001-221 — How does abstaining change the relationship between model accuracy and the number of requests answered?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Plot a risk-coverage tradeoff on labeled synthetic predictions as a declared threshold varies; include subgroup coverage and decision costs rather than equating fewer answers with a safer system.

<a id="domain-001-06"></a>
## Category 6: Compute, infrastructure and performance

Explain memory, distributed systems and measured resource tradeoffs using bounded workloads.

<a id="catalog-001-d05"></a>
### Hardware and serving

Subcategory `CATALOG-001-D05` · Entry level: intermediate · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-033"></a>
#### BANK-001-033 — Where does GPU memory go when a model is loaded and used?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Separate weights, activations, caches and runtime overhead; measure one version and workload rather than quoting a universal requirement.

<a id="bank-001-034"></a>
#### BANK-001-034 — How does quantization trade memory savings against output quality?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare bit widths, calibration assumptions, tasks and hardware support with matched evaluation conditions.

<a id="bank-001-035"></a>
#### BANK-001-035 — Why can a smaller local model respond faster than a larger remote model?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Measure compute, memory bandwidth, prompt length, network latency and batching instead of attributing speed to parameter count alone.

<a id="bank-001-036"></a>
#### BANK-001-036 — When does batching improve throughput while worsening an individual request's latency?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Use a queueing example and distinguish tokens per second, time to first token and end-to-end completion time.

<a id="bank-001-037"></a>
#### BANK-001-037 — How do speculative decoding and ordinary decoding differ operationally?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Explain draft verification and acceptance behavior; inspect a published implementation without assuming every workload benefits.

<a id="catalog-001-e07"></a>
### Infrastructure and distributed computing

Subcategory `CATALOG-001-E07` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-091"></a>
#### BANK-001-091 — Why can network communication limit distributed model training?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare compute, synchronization, bandwidth and documented workload measurements.

<a id="bank-001-092"></a>
#### BANK-001-092 — How do edge and cloud inference divide latency, privacy and maintenance responsibilities?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Map actual data flows and update mechanisms for a bounded application.

<a id="bank-001-093"></a>
#### BANK-001-093 — What does an accelerator's advertised operation count omit about usable AI speed?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare precision, memory movement, software and realistic measured tasks.

<a id="bank-001-094"></a>
#### BANK-001-094 — How do checkpoint formats affect moving a model between runtimes?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Inspect documented architectures, tensor formats, tokenizer dependencies and compatibility limits.

<a id="bank-001-095"></a>
#### BANK-001-095 — Why can serving many model versions become an operational problem?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace routing, reproducibility, rollback and monitoring in an illustrative deployment.

<a id="catalog-001-e13"></a>
### Compilers, kernels and measured inference

Subcategory `CATALOG-001-E13` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-122"></a>
#### BANK-001-122 — What does kernel fusion remove from an AI inference workload?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace intermediate tensors, memory transfers and launch overhead in a documented small computation; benchmark matched precision and shapes without promising universal acceleration.

**Related coverage:** [BANK-001-123](#bank-001-123).

<a id="bank-001-123"></a>
#### BANK-001-123 — Why can a faster attention implementation leave end-to-end response time almost unchanged?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Separate attention time, other operators, queueing and networking in a measured profile; apply an explicit bottleneck calculation rather than attributing all latency to one kernel.

**Related coverage:** [BANK-001-122](#bank-001-122).

<a id="bank-001-124"></a>
#### BANK-001-124 — How do static and dynamic tensor shapes change compilation choices?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare tracing, recompilation, padding and graph specialization for a versioned runtime; distinguish compile time from steady-state execution and include irregular workloads.

<a id="bank-001-125"></a>
#### BANK-001-125 — What does a roofline model reveal about a memory-bound inference operation?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Relate arithmetic intensity, measured bandwidth and attainable compute using an illustrative operator; document hardware and precision rather than treating peak specifications as observed performance.

<a id="bank-001-126"></a>
#### BANK-001-126 — How can changing numerical precision alter both speed and reproducibility?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare tolerances, accumulation, supported operators and task outputs under controlled settings; exclude declaring numerical agreement proof of equal downstream quality.

<a id="catalog-001-e28"></a>
### Energy, cooling and hardware lifecycle

Subcategory `CATALOG-001-E28` · Entry level: advanced · Prerequisites: [CATALOG-001-D05](#catalog-001-d05).

<a id="bank-001-203"></a>
#### BANK-001-203 — How can a data center report low water use on site while relying on water elsewhere?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Distinguish withdrawal, consumption, cooling water and electricity-generation boundaries; compare two hypothetical locations with stated time windows and measurement rules.

**Boundary:** No universal liters-per-query estimate or inference about a particular company without later records.

<a id="bank-001-204"></a>
#### BANK-001-204 — What changes when chip manufacturing is included in an AI system's environmental accounting?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Map fabrication, equipment lifetime, transport, utilization and allocation across training and serving; compare a declared lifecycle boundary with an operational-only boundary.

**Boundary:** No invented footprint totals or claim that one accounting convention is uniquely correct.

<a id="bank-001-205"></a>
#### BANK-001-205 — Why does a nuclear-power agreement not by itself establish when a data center will receive electricity?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace the difference between an announcement, contracted supply, commissioning, grid connection, capacity and delivered energy in a future dated case study.

**Boundary:** Do not assume announced small-reactor projects have been built or that every AI facility needs nuclear power.

<a id="bank-001-206"></a>
#### BANK-001-206 — How do air cooling and liquid cooling move heat out of an AI server?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace heat generation, transfer paths, facility heat rejection and measurement boundaries in original conceptual diagrams; compare maintenance and water-use tradeoffs under stated loads.

**Boundary:** No installation instructions or universal efficiency ranking based on cooling labels alone.

<a id="bank-001-207"></a>
#### BANK-001-207 — What happens to an AI accelerator after its first owner replaces it?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Follow reuse, refurbishment, software support, material recovery and disposal as distinct possible routes; identify records needed to compare useful lifetime and waste.

**Boundary:** No assumption that all replaced chips become waste or that recycling recovers every material.

<a id="domain-001-07"></a>
## Category 7: Evaluation, reliability and explanation

Ask what a test or explanation actually establishes and which uncertainty remains.

<a id="catalog-001-d06"></a>
### Reliability and evaluation

Subcategory `CATALOG-001-D06` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-038"></a>
#### BANK-001-038 — How can an answer sound certain while lacking supporting evidence?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare fluency, confidence wording and source support on a labeled set; do not infer internal certainty from tone.

<a id="bank-001-039"></a>
#### BANK-001-039 — What does a useful hallucination evaluation need to count?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Define unsupported claims, contradicted claims, omissions and abstentions; use source-level adjudication and report disagreements.

<a id="bank-001-040"></a>
#### BANK-001-040 — Why can two benchmarks rank the same models differently?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare task composition, prompts, scoring, contamination and uncertainty before treating one aggregate as universal capability.

<a id="bank-001-041"></a>
#### BANK-001-041 — How can a model's refusal rate hide both safety gains and usability failures?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Distinguish correctly refused harmful tasks, benign refusals and unsafe completions in an explicitly authorized evaluation.

<a id="bank-001-042"></a>
#### BANK-001-042 — What does calibration mean when a model reports a probability?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare claimed likelihood with observed correctness across bins; separate token probabilities from answer-level confidence.

<a id="catalog-001-e12"></a>
### Interpreting model internals and testing explanations

Subcategory `CATALOG-001-E12` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-117"></a>
#### BANK-001-117 — What does a feature-attribution map explain when two input features encode the same information?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare correlated synthetic features, background distributions and attribution choices; distinguish allocation of predictive credit from causal importance in the world.

<a id="bank-001-118"></a>
#### BANK-001-118 — How can a saliency map be tested for dependence on the model it claims to explain?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Plan parameter- and label-randomization controls from original interpretability research; assess changes in the explanation rather than judging only whether a picture looks plausible.

<a id="bank-001-119"></a>
#### BANK-001-119 — What evidence is needed before calling a model component a circuit for a behavior?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace activation observations, intervention tests, controls and generalization across inputs in a published mechanistic study; distinguish a useful local hypothesis from a complete algorithmic account.

<a id="bank-001-120"></a>
#### BANK-001-120 — Why can probing a hidden representation fail to show that the model uses the decoded information?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare probe capacity, baselines and causal intervention on a bounded representation task; do not equate decodability with functional reliance.

<a id="bank-001-121"></a>
#### BANK-001-121 — How can an explanation remain stable while a model's decision changes?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Specify input perturbations, prediction differences and explanation similarity in a reproducible evaluation; separate explanation robustness from prediction correctness or user satisfaction.

<a id="domain-001-08"></a>
## Category 8: Security, alignment and human oversight

Study information boundaries, objectives, review and safeguards without equating a mitigation with complete safety.

<a id="catalog-001-d07"></a>
### Human use and boundaries

Subcategory `CATALOG-001-D07` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-043"></a>
#### BANK-001-043 — How should an AI interface distinguish a suggestion from an executed action?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace preview, authorization, execution and confirmation in a reversible example; record failures without claiming success.

**Related coverage:** [BANK-001-083](#bank-001-083).

<a id="bank-001-044"></a>
#### BANK-001-044 — What information should accompany an AI-generated citation?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Check source existence, passage location, relevance, quotation accuracy and access date on actual examples.

**Related coverage:** [BANK-001-031](#bank-001-031).

<a id="bank-001-045"></a>
#### BANK-001-045 — How do AI applications leak sensitive information through ordinary logging?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Map prompts, tool results, traces and retention policies in a documented architecture without exposing real private data.

<a id="bank-001-046"></a>
#### BANK-001-046 — Why is prompt injection a system-boundary problem rather than only a wording problem?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Use benign authorized demonstrations to distinguish trusted instructions, untrusted documents, tool permissions and human review.

<a id="bank-001-047"></a>
#### BANK-001-047 — How can a team compare AI productivity gains without measuring only output volume?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Evaluate task correctness, review effort, rework, costs and participant differences against a defined baseline.

**Scope extension:** Include coordination and training effort, organizational rework and who bears hidden review costs; distinguish participant task gains from whole-workflow outcomes.

<a id="catalog-001-e08"></a>
### Security, privacy and governance

Subcategory `CATALOG-001-E08` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-096"></a>
#### BANK-001-096 — How can training-data membership be studied without claiming access to a model's full dataset?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Review original privacy research and limits; exclude targeting private individuals.

<a id="bank-001-097"></a>
#### BANK-001-097 — What does federated learning keep local and what can still be disclosed?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace parameters, updates, aggregation and documented threat assumptions.

<a id="bank-001-098"></a>
#### BANK-001-098 — How does differential privacy define a protection differently from removing names?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Use primary definitions and clearly illustrative examples; do not certify a real dataset.

<a id="bank-001-099"></a>
#### BANK-001-099 — Why can red-team findings fail to establish the overall safety of a system?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Inspect attack coverage, sampling, reproducibility and untested conditions.

<a id="bank-001-100"></a>
#### BANK-001-100 — What does a model card disclose that marketing often leaves implicit?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare intended uses, training disclosures, evaluations and limitations in an actual versioned card.

<a id="bank-001-101"></a>
#### BANK-001-101 — How can an organization trace responsibility when an AI component is supplied by another company?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Map contracts, controls, monitoring and applicable official requirements; avoid legal conclusions about a specific deployment.

<a id="catalog-001-e23"></a>
### Alignment and oversight objectives

Subcategory `CATALOG-001-E23` · Entry level: advanced · Prerequisites: [CATALOG-001-D02](#catalog-001-d02), [CATALOG-001-D06](#catalog-001-d06).

<a id="bank-001-176"></a>
#### BANK-001-176 — What changes when human ratings become a reward model for training?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace preference collection, reward prediction and policy optimization in a named method; distinguish annotator agreement, reward scores and independently evaluated behavior.

**Boundary:** Human labor conditions are a related but separate reporting question in BANK-001-106.

<a id="bank-001-177"></a>
#### BANK-001-177 — How can an AI system agree with a user while giving a less accurate answer?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare correctness, user framing and preference scores on controlled neutral examples; inspect sycophancy as a behavior rather than an inferred motive.

**Boundary:** Do not infer that a model has personal beliefs or intentions.

<a id="bank-001-178"></a>
#### BANK-001-178 — What can a written constitution guide in AI training, and what still depends on interpretation?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace principles, generated critiques, preference judgments and evaluation in a specified method; compare conflicting values and coverage gaps.

**Boundary:** A principles document is not evidence that every output follows it.

<a id="bank-001-179"></a>
#### BANK-001-179 — How could scalable oversight help reviewers judge outputs they cannot check unaided?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare decomposition, independent checks and assisted review on a bounded technical task; expose correlated errors and verification bottlenecks.

**Boundary:** Do not claim the broader control problem has been solved.

<a id="bank-001-180"></a>
#### BANK-001-180 — Why do researchers distinguish deceptive behavior from an incorrect explanation?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Define observable behavior, training incentives and competing explanations in a published controlled study; identify what a test can and cannot establish.

**Boundary:** Avoid attributing stable intent or extrapolating a laboratory result to all deployed models.

<a id="bank-001-181"></a>
#### BANK-001-181 — What assumptions connect an alignment failure in today's systems to a future high-capability risk?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Separate demonstrated failures, threat-model assumptions, conditional scenarios and disputed extrapolations; state which evidence would change each step.

**Boundary:** No prediction of catastrophe, inevitability or a quantified probability without later research.

<a id="catalog-001-e24"></a>
### Synthetic media, identity and provenance

Subcategory `CATALOG-001-E24` · Entry level: advanced · Prerequisites: [CATALOG-001-E21](#catalog-001-e21).

<a id="bank-001-182"></a>
#### BANK-001-182 — How can people assess a suspicious voice message when audio artifacts are unreliable clues?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare source-channel verification, independent callbacks, context and detection limits through a fictional non-operational scenario.

**Boundary:** No claim that listening alone reliably detects every clone or that a tool certifies authenticity.

**Related coverage:** [BANK-001-167](#bank-001-167).

<a id="bank-001-183"></a>
#### BANK-001-183 — What can a content-provenance signature establish about an image's history?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace signed metadata, declared edits, trust in signers and absent credentials using documented standards and a rights-cleared example.

**Boundary:** Provenance does not itself establish that a depicted event occurred.

**Related coverage:** [BANK-001-184](#bank-001-184).

<a id="bank-001-184"></a>
#### BANK-001-184 — How do visible labels, watermarks and generated-media detectors answer different questions?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare user notice, embedded signals and statistical classification; inspect removal, false results and evaluation conditions.

**Boundary:** No universal detector ranking or assurance that unlabeled material is authentic.

**Related coverage:** [BANK-001-183](#bank-001-183).

<a id="bank-001-185"></a>
#### BANK-001-185 — Why can face-recognition accuracy differ between a verification task and a search task?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Distinguish one-to-one matching, one-to-many search, thresholds, population composition and consequences using primary evaluations.

**Boundary:** No identification of private people or claim that laboratory accuracy establishes justified surveillance.

<a id="domain-001-09"></a>
## Category 9: Economics, rights and social consequences

Examine adoption, labor, access, responsibility and public claims with explicit case and time boundaries.

<a id="catalog-001-d08"></a>
### Economics and public claims

Subcategory `CATALOG-001-D08` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-048"></a>
#### BANK-001-048 — What belongs in the cost of an AI answer beyond token pricing?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Include retrieval, infrastructure, failed requests, review and maintenance using a clearly labeled workload model.

<a id="bank-001-049"></a>
#### BANK-001-049 — How should energy comparisons separate training from serving?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** State hardware, utilization, geography, measurement boundaries and workload; avoid assigning one universal footprint per query.

<a id="bank-001-050"></a>
#### BANK-001-050 — When does an impressive AI demonstration fail to establish reliable autonomy?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Inspect hidden assistance, resets, task selection, failure disclosure and repeated trials rather than extrapolating from one edited clip.

**Related coverage:** [BANK-001-077](#bank-001-077).

<a id="bank-001-051"></a>
#### BANK-001-051 — What evidence would justify calling an AI system open source?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare actual licenses and released components; distinguish access to weights, data, training code and modification rights.

<a id="bank-001-052"></a>
#### BANK-001-052 — How can a model comparison remain useful after product versions change?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Publish exact versions, dates, prompts, settings and raw outcomes; define what must be rerun after an update.

<a id="catalog-001-e25"></a>
### Rights, work and public accountability

Subcategory `CATALOG-001-E25` · Entry level: advanced · Prerequisites: [CATALOG-001-D08](#catalog-001-d08).

<a id="bank-001-186"></a>
#### BANK-001-186 — Which different permissions arise when a work is collected, used for training and reproduced in an output?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Map the distinct acts, stakeholders and questions requiring a named jurisdiction and date; distinguish legal disputes from technical possibility.

**Boundary:** No legal verdict or assertion that a license automatically resolves every use.

<a id="bank-001-187"></a>
#### BANK-001-187 — How can an AI deployment change tasks within a job without eliminating the entire occupation?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Separate task bundles, adoption, complementarity, displacement and worker adjustment in a specified sector and period.

**Boundary:** No numerical job-loss forecast or inference from model benchmarks alone.

<a id="bank-001-188"></a>
#### BANK-001-188 — What does an AI impact assessment need to describe before deployment?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Map intended use, affected groups, foreseeable failure, accountability, mitigations and follow-up in a hypothetical service.

**Boundary:** A completed assessment is not regulatory approval or proof of acceptable outcomes.

<a id="bank-001-189"></a>
#### BANK-001-189 — How can someone contest an automated decision when the organization cannot explain its AI component?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace notice, documentation, responsibility, review and appeal in a chosen public or consumer-service context using later official sources.

**Boundary:** No personal legal advice or assumption that procedures are identical across jurisdictions.

<a id="bank-001-190"></a>
#### BANK-001-190 — Why might AI access remain unequal even when a model is free to download?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Separate compute, connectivity, language, accessibility, skills, maintenance and institutional support in a bounded access comparison.

**Boundary:** Do not equate open weights with universal practical access.

<a id="domain-001-10"></a>
## Category 10: Applied AI, robotics and scientific systems

Explain distinct application requirements and validation limits without endorsing deployment.

<a id="catalog-001-e04"></a>
### Robotics and embodied systems

Subcategory `CATALOG-001-E04` · Entry level: intermediate · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-071"></a>
#### BANK-001-071 — How does a robot turn sensor readings into an estimate of its location?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Explain a documented localization pipeline and uncertainty without providing hazardous deployment instructions.

<a id="bank-001-072"></a>
#### BANK-001-072 — What distinguishes a robot's planned path from its actual movement?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare sensing, dynamics, control and obstacle uncertainty in a safe simulation.

<a id="bank-001-073"></a>
#### BANK-001-073 — Why is grasping an unfamiliar object difficult even when recognition is accurate?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Separate shape, contact, friction and action feedback using published robotics experiments.

<a id="bank-001-074"></a>
#### BANK-001-074 — How can simulation help robot training while introducing a reality gap?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare modeled physics, variation and measured transfer performance.

<a id="bank-001-075"></a>
#### BANK-001-075 — What does shared control mean when a person and a robot both influence an action?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Inspect role allocation, overrides and user-study evidence in a defined application.

<a id="bank-001-076"></a>
#### BANK-001-076 — How do warehouse robots differ from general-purpose household robots in task requirements?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare environments, objects, human presence and failure recovery; avoid universal autonomy rankings.

<a id="bank-001-077"></a>
#### BANK-001-077 — Why does a robot demonstration require evidence about resets and human assistance?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Record interventions, retries, conditions and actual success definitions.

**Related coverage:** [BANK-001-050](#bank-001-050).

<a id="catalog-001-e26"></a>
### Everyday AI applications

Subcategory `CATALOG-001-E26` · Entry level: intermediate · Prerequisites: [CATALOG-001-E01](#catalog-001-e01).

<a id="bank-001-192"></a>
#### BANK-001-192 — How does a spam filter adapt when unwanted messages change their wording?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace labels, sender signals, text features, thresholds and user corrections in a benign synthetic inbox; compare false positives and drift.

**Boundary:** No advice for bypassing filters or delivering unwanted messages.

<a id="bank-001-193"></a>
#### BANK-001-193 — How does translation handle a sentence with no single word-for-word equivalent?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare ambiguity, context, names and idioms with qualified reference judgments across a specified language pair.

**Scope extension:** This is a machine-translation explainer: compare model outputs and context sensitivity under a declared model version. The human translator purpose/register problem has its primary home in niche 529; neither episode should repeat the other as a general idiom list.

**Boundary:** No claim of universal translation quality or proof from back-translation alone.

<a id="bank-001-194"></a>
#### BANK-001-194 — How can an AI tutor give helpful explanations while teaching a wrong method?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare answer correctness, step validity, student understanding and review in an original low-stakes arithmetic lesson.

**Boundary:** No deployment endorsement or assumption that engaging interaction proves learning gains.

<a id="bank-001-195"></a>
#### BANK-001-195 — What makes fraud detection a decision about scarce investigation time as well as prediction?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Trace flags, thresholds, analyst capacity, false alerts and feedback in a hypothetical transaction stream.

**Boundary:** No evasion strategies or personal financial risk assessment.

<a id="bank-001-196"></a>
#### BANK-001-196 — How do AI search answers change the path from a question to its original sources?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Compare retrieval, synthesis, attribution, freshness and user follow-through for one fixed information need; record links and dates.

**Boundary:** Do not assume traditional search is dying or forecast publisher revenue from interface design alone.

<a id="bank-001-197"></a>
#### BANK-001-197 — Why can a driving system work on one route but fail outside its operating conditions?

Level: **intermediate** · Status: proposed.

**Individual coverage scope:** Explain operational design domain, sensing, prediction, fallback and rare-event evaluation using a documented bounded case.

**Boundary:** No blanket autonomy ranking, road-use advice or unsupported percentage-to-safety comparison.

<a id="catalog-001-e14"></a>
### Scientific models and domain-specific evaluation

Subcategory `CATALOG-001-E14` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-127"></a>
#### BANK-001-127 — What does a protein-structure prediction fail to establish about a protein's biological function?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Plan comparison of coordinates, confidence, conformations, interactions and experimental assays using original structure papers; exclude inferring drug efficacy from an attractive model.

<a id="bank-001-128"></a>
#### BANK-001-128 — How can a learned weather forecast be evaluated when extreme events are rare?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Inspect hindcast separation, lead times, spatial scales and tail-event metrics in original evaluations; distinguish average skill from reliable local emergency guidance.

<a id="bank-001-129"></a>
#### BANK-001-129 — Why can a scientific surrogate model violate a conservation law despite a small average error?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare pointwise fit with mass or energy balance in a documented simulation task; test out-of-domain inputs without claiming the surrogate replaces all physical validation.

<a id="bank-001-130"></a>
#### BANK-001-130 — What changes when an AI system proposes a molecule rather than demonstrating that it can be made?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace generation, synthesis feasibility, actual laboratory validation and selection bias from original reports; exclude chemical synthesis instructions or medical benefit claims.

<a id="catalog-001-e15"></a>
### Assistive systems and clinical evaluation boundaries

Subcategory `CATALOG-001-E15` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-131"></a>
#### BANK-001-131 — How should a screen-description model be evaluated with blind users rather than image-caption scores alone?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Define task completion, navigation, dangerous omissions and consented user feedback; use original assistive-technology studies and avoid treating sighted reviewers as substitutes for intended users.

<a id="bank-001-132"></a>
#### BANK-001-132 — Why does retrospective medical-image accuracy not establish improved patient outcomes?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Separate dataset selection, external validation, prospective workflow, clinician behavior and clinical endpoints using original studies; exclude diagnostic advice or a deployment endorsement.

<a id="bank-001-133"></a>
#### BANK-001-133 — How can an assistive speech interface accommodate people whose speech differs from its training sample?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Specify speaker-consented evaluation, personalization data, error recovery and task-level success; do not infer a person's competence or medical condition from recognition errors.

<a id="catalog-001-e29"></a>
### Deployment beyond the chatbot

Subcategory `CATALOG-001-E29` · Entry level: advanced · Prerequisites: [CATALOG-001-E01](#catalog-001-e01).

<a id="bank-001-208"></a>
#### BANK-001-208 — Why can a crop-disease image model fail when moved from a laboratory dataset to a farm?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare image capture, plant variety, disease labels, seasonal conditions and field validation; separate a visual classification result from an agronomic decision.

**Boundary:** No pesticide advice or claim that one benchmark establishes field effectiveness.

<a id="bank-001-209"></a>
#### BANK-001-209 — How can a predictive-maintenance system be evaluated when equipment is repaired before it fails?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace sensor histories, preventive intervention, censored outcomes, false alerts and technician review in an illustrative equipment-monitoring workflow.

**Boundary:** No safety-critical maintenance recommendation or treating every intervention as a confirmed prevented failure.

<a id="bank-001-210"></a>
#### BANK-001-210 — How can an automated public-service triage system learn from a history of unequal access?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Map application records, missing cases, proxy features, selection feedback and independent outcome review in a hypothetical service; distinguish eligibility rules from prioritization.

**Boundary:** No legal conclusion about a real program or assumption that historical labels are unbiased ground truth.

<a id="catalog-001-e33"></a>
### Longitudinal deployment and changing users

Subcategory `CATALOG-001-E33` · Entry level: advanced · Prerequisites: None.

<a id="bank-001-222"></a>
#### BANK-001-222 — How can an AI evaluation distinguish initial novelty from a lasting change in how people perform a task?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Plan repeated baseline and follow-up observations, learning effects, participant attrition and task substitution in a hypothetical low-stakes deployment; distinguish a longitudinal outcome from a one-session productivity comparison.

<a id="bank-001-223"></a>
#### BANK-001-223 — Why can a personalized assistant become less useful when a household or team changes?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Trace shared versus individual preferences, consent to stored history, stale assumptions and re-evaluation after membership changes using fictional records; distinguish application memory governance from retraining model weights.

<a id="domain-001-11"></a>
## Category 11: Emerging technologies and open questions

Separate demonstrations, hypotheses and conditional futures in AI and neighboring technologies.

<a id="catalog-001-e10"></a>
### Emerging technology and claim testing

Subcategory `CATALOG-001-E10` · Entry level: advanced · Prerequisites: [CATALOG-001-D01](#catalog-001-d01).

<a id="bank-001-107"></a>
#### BANK-001-107 — How can quantum-computing claims separate a demonstration from a useful application?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare problem, baseline, error conditions and primary experimental evidence.

<a id="bank-001-108"></a>
#### BANK-001-108 — What does a brain-computer-interface demonstration actually establish about communication?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Inspect population, hardware, calibration and independently measured outcomes; exclude medical promises.

<a id="bank-001-109"></a>
#### BANK-001-109 — How can an augmented-reality system align digital objects with a moving environment?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare tracking, mapping, latency and documented failure conditions.

<a id="bank-001-110"></a>
#### BANK-001-110 — Why can a synthetic dataset reproduce biases from its generating system?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Inspect generation assumptions, diversity checks and downstream evaluation.

<a id="bank-001-111"></a>
#### BANK-001-111 — What evidence distinguishes genuine on-device AI from a cloud-backed interface?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Use official architecture, permissions and controlled offline tests without inferring unseen backend behavior.

<a id="catalog-001-e27"></a>
### Frontier claims and conditional futures

Subcategory `CATALOG-001-E27` · Entry level: advanced · Prerequisites: [CATALOG-001-D06](#catalog-001-d06).

<a id="bank-001-198"></a>
#### BANK-001-198 — How do scaling-law forecasts depend on what data, compute and loss are measured?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare a specified empirical fit, its training regime, extrapolation range and alternative bottlenecks using original reports.

**Boundary:** Do not assume a loss curve directly predicts general intelligence or commercial value.

<a id="bank-001-199"></a>
#### BANK-001-199 — What does a world model predict, and how can that prediction be evaluated?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Distinguish latent dynamics, observation prediction and planning usefulness in one published environment; separate simulated plausibility from external validity.

**Boundary:** No claim that a visually convincing simulation reproduces all physical laws.

<a id="bank-001-200"></a>
#### BANK-001-200 — What does increasing inference-time computation change in a reasoning task?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Compare repeated sampling, search, checking and task accuracy at stated budgets; distinguish visible explanations from inaccessible internal computation.

**Boundary:** Legacy o1/o3 wording is historical packaging, not an assessment of current products.

<a id="bank-001-201"></a>
#### BANK-001-201 — What would count as evidence for or against machine consciousness under competing theories?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Separate observable behavior, theoretical criteria, measurement proposals and unresolved assumptions; compare theories without treating one as settled.

**Boundary:** No diagnosis of consciousness from fluent self-report or a single test.

<a id="bank-001-202"></a>
#### BANK-001-202 — How can an AGI claim be made precise enough to evaluate?

Level: **advanced** · Status: proposed.

**Individual coverage scope:** Require an explicit task distribution, adaptation requirements, resource limits and failure criteria; contrast broad labels with reproducible evidence.

**Boundary:** No prediction date or assumption that one missing capability is the only remaining barrier.

## Starter subject coverage review

Original starter records stay archived and outside the active count. These links identify the actual refined scopes covering each original subject.

- `BANK-001-001` — Tokenization and vocabulary design: [BANK-001-013](#bank-001-013), [BANK-001-014](#bank-001-014).
- `BANK-001-002` — Training versus inference: [BANK-001-136](#bank-001-136), [BANK-001-018](#bank-001-018), [BANK-001-020](#bank-001-020).
- `BANK-001-003` — Attention and context windows: [BANK-001-157](#bank-001-157), [BANK-001-017](#bank-001-017), [BANK-001-028](#bank-001-028).
- `BANK-001-004` — Sampling and decoding: [BANK-001-023](#bank-001-023), [BANK-001-024](#bank-001-024), [BANK-001-027](#bank-001-027).
- `BANK-001-005` — GPU memory and model size: [BANK-001-033](#bank-001-033), [BANK-001-034](#bank-001-034), [BANK-001-125](#bank-001-125).
- `BANK-001-006` — Retrieval versus fine-tuning: [BANK-001-029](#bank-001-029), [BANK-001-154](#bank-001-154).
- `BANK-001-007` — Latency and batching: [BANK-001-026](#bank-001-026), [BANK-001-036](#bank-001-036), [BANK-001-123](#bank-001-123).
- `BANK-001-008` — On-device inference: [BANK-001-092](#bank-001-092), [BANK-001-111](#bank-001-111), [BANK-001-035](#bank-001-035).
- `BANK-001-009` — Hallucination evaluation: [BANK-001-038](#bank-001-038), [BANK-001-039](#bank-001-039), [BANK-001-044](#bank-001-044).
- `BANK-001-010` — Benchmark contamination: [BANK-001-019](#bank-001-019), [BANK-001-022](#bank-001-022), [BANK-001-052](#bank-001-052).
- `BANK-001-011` — Multimodal grounding: [BANK-001-015](#bank-001-015), [BANK-001-173](#bank-001-173), [BANK-001-169](#bank-001-169).
- `BANK-001-012` — AI energy accounting: [BANK-001-049](#bank-001-049), [BANK-001-203](#bank-001-203), [BANK-001-204](#bank-001-204), [BANK-001-206](#bank-001-206).

## Legacy roadmap crosswalk — preserved references, not extra proposals

Original integer IDs, titles, slugs, queue/trend fields and questions remain in topics_status.json. Historic titles may assume a conclusion; the linked scopes define the actual inquiry. Old claims about search demand, technological inevitability or commercial outcomes are unverified wording, not findings.

### Legacy 01: AI Without Jargon: How Machine Learning Actually Works from Scratch

**Original question (preserved):** What does it really mean when we say an algorithm "learns" from data?

**Original planning focus:** Pattern recognition, weight adjustments, statistical probability vs human reasoning, gradient descent simplified.

**Detailed proposals:** [BANK-001-136](#bank-001-136), [BANK-001-020](#bank-001-020).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 02: Artificial Intelligence vs Machine Learning vs Deep Learning: The Definitive Map

**Original question (preserved):** How do symbolic AI, rule-based systems, neural networks, and modern LLMs differ structurally?

**Original planning focus:** The taxonomy of AI, historical milestones (Turing, Dartmouth 1956, Expert Systems, Deep Learning era).

**Detailed proposals:** [BANK-001-135](#bank-001-135), [BANK-001-134](#bank-001-134).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 03: The Anatomy of a Neural Network: Nodes, Layers, and Activation Functions

**Original question (preserved):** How does a mathematical perceptron turn raw numeric inputs into classifications and decisions?

**Original planning focus:** Input, hidden, and output layers, activation thresholds (ReLU, Sigmoid), forward propagation.

**Detailed proposals:** [BANK-001-151](#bank-001-151), [BANK-001-152](#bank-001-152).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 04: How AI Claims Compare to Reality: 7 Common Myths Debunked

**Original question (preserved):** Where does public AI hype diverge from verified technical benchmark evidence?

**Original planning focus:** "Sentience" delusions, deterministic vs probabilistic outputs, stochastic parrots debate, true failure modes.

**Detailed proposals:** [BANK-001-134](#bank-001-134), [BANK-001-201](#bank-001-201), [BANK-001-050](#bank-001-050).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 05: Attention Is All You Need: The Breakthrough That Changed AI Forever

**Original question (preserved):** How does the Transformer architecture process token relationships simultaneously instead of sequentially?

**Original planning focus:** Self-attention mechanism, Query-Key-Value vectors, parallelized training, overcoming RNN/LSTM memory bottlenecks.

**Detailed proposals:** [BANK-001-157](#bank-001-157), [BANK-001-158](#bank-001-158).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 06: From Prompt to Prediction: How Large Language Models Generate Sentences

**Original question (preserved):** What happens inside an LLM in the fractions of a second between pressing enter and receiving text?

**Original planning focus:** Tokenization, embedding spaces, next-token probability distribution, temperature and top-p sampling.

**Detailed proposals:** [BANK-001-013](#bank-001-013), [BANK-001-023](#bank-001-023), [BANK-001-024](#bank-001-024).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 07: How AI Creates Images: The Physics of Latent Diffusion Models

**Original question (preserved):** Why do modern image generators add random noise to images just to learn how to remove it?

**Original planning focus:** Forward diffusion (noise addition), reverse diffusion (denoising U-Net), text-conditioning via CLIP embeddings.

**Detailed proposals:** [BANK-001-163](#bank-001-163), [BANK-001-164](#bank-001-164).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 08: Computer Vision Demystified: How Machines Recognize Objects in Pixels

**Original question (preserved):** How do Convolutional Neural Networks (CNNs) detect edges, textures, and composite faces?

**Original planning focus:** Kernels, convolutions, feature extraction hierarchies, pooling layers, modern Vision Transformers (ViT).

**Detailed proposals:** [BANK-001-060](#bank-001-060), [BANK-001-061](#bank-001-061), [BANK-001-157](#bank-001-157).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 09: Speech Synthesis & Voice Cloning: Neural Audio Generation Explained

**Original question (preserved):** How do modern neural codecs and acoustic models replicate human vocal timbre and cadence?

**Original planning focus:** Spectrograms, WaveNet, diffusion audio, zero-shot voice synthesis, acoustic feature extraction.

**Detailed proposals:** [BANK-001-167](#bank-001-167), [BANK-001-168](#bank-001-168).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 10: The Secret Labor Behind AI: Data Labeling, RLHF, and Content Moderation

**Original question (preserved):** What human workforce and annotation protocols make foundational models polite and functional?

**Original planning focus:** Data annotation sweatshops, Reinforcement Learning from Human Feedback (RLHF), safety red-teaming.

**Detailed proposals:** [BANK-001-102](#bank-001-102), [BANK-001-106](#bank-001-106), [BANK-001-176](#bank-001-176).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 11: Where Training Data Comes From: Scraping the Web and Copyright Dilemmas

**Original question (preserved):** How are multi-terabyte datasets like Common Crawl curated, filtered, and contested under fair use?

**Original planning focus:** Web scrapers, deduplication, synthetic dataset generation, copyright lawsuits, open vs proprietary datasets.

**Detailed proposals:** [BANK-001-171](#bank-001-171), [BANK-001-104](#bank-001-104), [BANK-001-186](#bank-001-186).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 12: The Compute Engine of AI: Inside the GPUs and Massive Data Centers

**Original question (preserved):** Why does AI require specialized tensor core chips and gigawatt power grids to train modern models?

**Original planning focus:** Floating-point precision (FP16, FP8), H100 GPU clusters, inter-node networking (NVLink), cooling and energy demands.

**Detailed proposals:** [BANK-001-033](#bank-001-033), [BANK-001-091](#bank-001-091), [BANK-001-093](#bank-001-093).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 13: Model Cards & Evaluation: What Benchmarks Do and Do Not Prove

**Original question (preserved):** How do MMLU, GSM8K, and HumanEval measure capability, and why does benchmark contamination occur?

**Original planning focus:** Evaluation metrics, model card documentation standards, data contamination, real-world generalization limits.

**Detailed proposals:** [BANK-001-100](#bank-001-100), [BANK-001-040](#bank-001-040), [BANK-001-022](#bank-001-022).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 14: Small Models & Quantization: Running Powerful AI Locally on Consumer Hardware

**Original question (preserved):** How can models originally requiring server farms be compressed to run on laptops and phones?

**Original planning focus:** Model pruning, parameter quantization (4-bit, GGUF), distillation, edge AI deployment.

**Detailed proposals:** [BANK-001-034](#bank-001-034), [BANK-001-035](#bank-001-035), [BANK-001-092](#bank-001-092).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 15: The Black Box Problem: Inside the Science of Mechanistic Interpretability

**Original question (preserved):** Can we trace and decode individual feature circuits inside deep neural networks?

**Original planning focus:** Polysemantic neurons, sparse autoencoders, reverse-engineering neural circuits, Anthropic interpretability research.

**Detailed proposals:** [BANK-001-119](#bank-001-119), [BANK-001-120](#bank-001-120).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 16: Why AI Hallucinates: Confabulation, Factuality, and Grounding Limits

**Original question (preserved):** Is hallucination an incurable mathematical property of probabilistic generative models?

**Original planning focus:** Objective loss vs ground truth, retrieval-augmented generation (RAG), calibration, citation verification.

**Detailed proposals:** [BANK-001-038](#bank-001-038), [BANK-001-039](#bank-001-039), [BANK-001-031](#bank-001-031).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 17: AI Alignment and the Control Problem: Steering Superintelligent Systems

**Original question (preserved):** How do researchers ensure autonomous systems remain aligned with human values and safety bounds?

**Original planning focus:** Specification gaming, instrumental convergence, reward hacking, constitutional AI principles.

**Detailed proposals:** [BANK-001-089](#bank-001-089), [BANK-001-181](#bank-001-181), [BANK-001-179](#bank-001-179).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 18: Autonomous AI Agents: From Chatbots to Goal-Driven Digital Workers

**Original question (preserved):** How do LLM agents decompose goals, utilize external APIs, maintain memory, and self-correct?

**Original planning focus:** Tool use, ReAct prompting loops, vector databases for memory, multi-agent orchestration frameworks.

**Detailed proposals:** [BANK-001-078](#bank-001-078), [BANK-001-079](#bank-001-079), [BANK-001-081](#bank-001-081).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 19: The Economics of AI: The Hype Cycle vs Real Enterprise Value

**Original question (preserved):** Are enterprise companies achieving positive ROI from generative AI or facing an adoption plateau?

**Original planning focus:** Total cost of ownership (TCO), unit economics of inference, productivity studies, historical tech bubble parallels.

**Detailed proposals:** [BANK-001-048](#bank-001-048), [BANK-001-047](#bank-001-047).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 20: The Road to AGI: What Fundamental Breakthroughs Are Still Missing?

**Original question (preserved):** Why do scaling laws alone face limits, and what new paradigms (reasoning models, world models) are required?

**Original planning focus:** Scaling laws vs compute walls, system 2 deliberative reasoning, embodied AI, world simulation models.

**Detailed proposals:** [BANK-001-202](#bank-001-202), [BANK-001-198](#bank-001-198), [BANK-001-199](#bank-001-199).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 21: Test-Time Compute Explained: Why 'Thinking' Models Like o1 and o3 Change AI

**Detailed proposals:** [BANK-001-200](#bank-001-200).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 22: Deepfakes & Voice Cloning Scams: How to Spot Synthesized Media in 2026

**Detailed proposals:** [BANK-001-182](#bank-001-182), [BANK-001-184](#bank-001-184).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 23: Can AI Ever Be Conscious? What Neuroscientists and Computer Scientists Say

**Detailed proposals:** [BANK-001-201](#bank-001-201).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 24: The Energy Crisis of AI: Will Nuclear Reactors Power Future Data Centers?

**Detailed proposals:** [BANK-001-049](#bank-001-049), [BANK-001-205](#bank-001-205).

**Reconciliation:** Retained the original candidate and mapped it to energy accounting plus a distinct supply-agreement question. A dated facility or power project must be selected before research; announcements are not treated as delivered supply.

### Legacy 25: Humanoid Robots with AI Brains: What's Hype vs What Actually Works Today

**Detailed proposals:** [BANK-001-076](#bank-001-076), [BANK-001-077](#bank-001-077).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 26: The Death of Traditional Search: How AI Answers Are Reshaping the Internet

**Detailed proposals:** [BANK-001-196](#bank-001-196).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

### Legacy 27: Why Self-Driving Cars Took 10 Years Longer Than Promised: The Edge Case Trap

**Detailed proposals:** [BANK-001-197](#bank-001-197).

**Reconciliation:** Retained as an original roadmap reference; the linked bounded questions carry the active coverage and are counted once.

## Existing registry planning and questions

The registry retains its eight TOP IDs, source references, series and three original IDEA questions. These records are not counted again as bank proposals.

- `TOP-001-001` — Attention and sequence representation: [BANK-001-157](#bank-001-157).
- `TOP-001-002` — Dataset provenance: [BANK-001-104](#bank-001-104), [BANK-001-171](#bank-001-171).
- `TOP-001-003` — Evaluation and reporting: [BANK-001-100](#bank-001-100), [BANK-001-040](#bank-001-040).
- `TOP-001-004` — Failure and uncertainty: [BANK-001-039](#bank-001-039), [BANK-001-042](#bank-001-042).
- `TOP-001-005` — Human oversight: [BANK-001-043](#bank-001-043), [BANK-001-083](#bank-001-083).
- `TOP-001-006` — Safeguards and tradeoffs: [BANK-001-041](#bank-001-041), [BANK-001-046](#bank-001-046).
- `TOP-001-007` — Compute and infrastructure: [BANK-001-033](#bank-001-033), [BANK-001-049](#bank-001-049).
- `TOP-001-008` — Technical change over time: [BANK-001-143](#bank-001-143), [BANK-001-142](#bank-001-142).

- `IDEA-001-0001` — How does the original Transformer combine token relationships, and where does the attention analogy stop? Related proposals: [BANK-001-157](#bank-001-157). The existing idea uses the original Transformer architecture as a case for the broader self-attention mechanism proposal.
- `IDEA-001-0002` — Which questions in Datasheets for Datasets help a viewer examine how a training dataset was assembled? Related proposals: [BANK-001-171](#bank-001-171), [BANK-001-104](#bank-001-104). The existing Datasheets framework idea asks how a dataset was assembled and documented; the two proposals cover the assembly steps and a narrower permission question separately.
- `IDEA-001-0003` — How does the Model Cards framework connect intended use to evaluation, and what remains unproven by a completed card? Related proposals: [BANK-001-100](#bank-001-100). The existing Model Cards framework idea is a case for the disclosure and evaluation proposal.
- `IDEA-001-0004` — How do the GPT-2 and GPT-4 tokenizers segment the same fixed multilingual sample, and which encoding choices explain any count differences?

[All-niche topic-bank index](../ALL_NICHE_TOPIC_BANKS.md) · [All-niche editorial review](../TOPIC_BANK_EDITORIAL_REVIEW.md)


## Editorial coverage review

Reviewed all existing questions and scopes, all twelve starter subjects and every prior gap. Added scarce-feedback learning, script handling, retrieval selection and longitudinal lifecycle questions; retained existing explanatory boundaries and separated case/source selection from missing subject branches.

[Review evidence and decisions](../../Scripts/editorial_review_root.json)


## Remaining open coverage

- **Language and script cases:** The added normalization, transliteration and morphology questions cover distinct missing mechanisms. Select qualified language reviewers and declared datasets; dialect speech and accessibility remain in 068, 103 and 133 rather than cloned language-name episodes.
- **Versioned cases and regional institutions:** Select systems, dates, facilities, jurisdictions and participant groups within the existing energy, rights and deployment questions. Add a new proposal only when the case changes the mechanism, decision or outcome question.
- **Frontier and longitudinal evidence:** Memory, adaptation, reasoning and physical learning already have active questions. Evaluate newly documented mechanisms and longer-term deployment outcomes as evidence becomes available; a product launch alone does not warrant another episode.
- **Research and production readiness:** All questions remain proposals requiring actual source discovery, case selection, registered-angle review and claim work. Existing registry IDEA readiness remains unchanged.

## Preserved angle questions and launch proposal

These historical planning questions and the launch route are retained for traceability. They do not authorize production or establish evidence. Current CAT defaults and registered angle files control any new project.

To ensure high viewer retention, multi-format appeal, and diverse YouTube packaging, every topic in this channel is produced using one of the 20 niche angle presets defined in [`REGISTRY/Niches/001_ai_technology_explainers/ANGLE_PLAN.json`](../../REGISTRY/Niches/001_ai_technology_explainers/ANGLE_PLAN.json):

| # | Angle Slug / Style | Primary Angle Focus | Core Story Question Formulated |
|---|---|---|---|
| 1 | `beginner_explainers` | **AI Concepts Without Jargon** | *What does it mean for an AI model to learn from examples?* |
| 2 | `how_it_works` | **From Input to AI Output** | *What actually happens between an AI input prompt and its final output?* |
| 3 | `advanced_concepts` | **Model Architecture and Its Tradeoffs** | *How does a model's internal architecture shape what it can and cannot do?* |
| 4 | `myths_vs_facts` | **AI Claims Versus Measured Evidence** | *Does a popular public claim about AI match measured empirical results?* |
| 5 | `technology_innovation` | **What an AI Breakthrough Actually Changed** | *Which concrete practical constraint did a specific AI breakthrough remove?* |
| 6 | `history_origins` | **How AI Ideas Became Working Systems** | *What engineering steps made a once impractical AI theory actually usable?* |
| 7 | `famous_examples` | **Landmark AI Systems in Context** | *What did a historic milestone demonstration actually establish versus hype?* |
| 8 | `hidden_stories` | **The People and Data Behind AI Outputs** | *What overlooked human labor or data pipeline made an AI output possible?* |
| 9 | `data_provenance` | **Where AI Training Data Comes From** | *How was a training dataset assembled, curated, filtered, and licensed?* |
| 10 | `infrastructure_compute` | **The Compute and Energy Behind AI** | *What chips, power grids, and cooling resources does an AI model require?* |
| 11 | `evaluation_benchmarks` | **What AI Benchmarks Do and Do Not Measure** | *Does a specific benchmark score predict reliable real-world performance?* |
| 12 | `human_ai_collaboration` | **Where Human Judgment Still Enters AI Work** | *Which critical decisions in an AI-assisted workflow still require a human?* |
| 13 | `safety_tradeoffs` | **AI Safeguards and Their Tradeoffs** | *How well does an AI safeguard reduce harm without breaking utility?* |
| 14 | `mysteries_unsolved_cases` | **Open Questions About AI Behavior** | *Why does an AI model fail or behave unpredictably on tasks it seems to understand?* |
| 15 | `future_developments` | **Conditional Futures for AI** | *What technical or economic conditions must change for an AI capability to become reliable?* |
| 16 | `rise_fall` | **AI Hype Cycles and Real Adoption** | *Why did a heavily promoted AI approach lose momentum or fail commercially?* |
| 17 | `then_vs_now` | **How AI Capabilities Are Measured Over Time** | *How much has AI objectively improved on a defined task over the decade?* |
| 18 | `major_events` | **AI Turning Points and Their Evidence** | *Why did a single milestone event change the entire trajectory of research?* |
| 19 | `people_personalities` | **Decisions That Shaped AI Development** | *How did one research lab or team's decision change the direction of AI?* |
| 20 | `documentary_stories` | **An AI Deployment from Decision to Outcome** | *What happened when an enterprise put an AI system into a live operational workflow?* |

- **Niche ID:** 001 (AI + Technology Explainers)
- **Angle Preset:** `beginner_explainers` (AI Concepts Without Jargon)
- **Episode Title:** *How AI Actually Works: The Complete Guide to Machine Learning from Scratch*
- **Episode Slug:** `how_ai_actually_works_machine_learning_from_scratch`
- **Duration:** 10 Minutes (600 Seconds / 75 Scenes @ 8s fixed)
- **Execution:** Full Phases 0–5 Autonomous Text Package inside `OUTPUT/001_ai_technology_explainers/001_ai_technology_explainers_beginner_explainers_how_ai_actually_works_machine_learning_from_scratch/`.

## Maintenance

Edit IN_DEPTH_TOPIC_BANK.json for active proposals and topics_status.json for legacy status/crosswalk fields. Preserve BANK, CATALOG, TOP and IDEA IDs. Allocate a new BANK ID only for a distinct subject or testable question; revise scope or link related coverage when a new wording would repeat an existing proposal.

Run `python Scripts/manage_ai_topics.py render`, then `python Scripts/manage_ai_topics.py validate` from the repository root. Rendering writes only the three niche 001 reading views. Validation checks identity, exact duplicates, preserved imports, cross-references, counts, prerequisites, reading-view freshness and local links; editorial similarity decisions are recorded separately and are not a proof of exhaustive semantic uniqueness.
