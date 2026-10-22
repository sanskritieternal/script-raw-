# AI & Technology Explainers Channel Master Topic Roadmap (Scratch to Advanced)
**Niche:** 001 AI + Technology Explainers (Robotics_AI)  
**Channel Language:** English (YouTube)  
**Target Audience:** General Public, Tech Enthusiasts, Knowledge Seekers (Global)  
**Production Format:** 10-Minute Explainer / Documentary Episodes (600s, 75 Fixed 8s Scenes)  
**Execution & Sync Report:** [topics/001_ai_technology_explainers/TOPICS_COVERED_REPORT.md](../../topics/001_ai_technology_explainers/TOPICS_COVERED_REPORT.md)  

---

## 1. Channel Progression Strategy

This curriculum organizes artificial intelligence, machine learning history, neural architectures, data provenance, ethical boundaries, and real-world deployment into four sequential learning tiers:
- **Tier 1: Foundations (Scratch / Beginner)** — Demystifying AI buzzwords, what learning from examples actually means, neural networks simplified, and separating hype from mathematical reality.
- **Tier 2: Core Architectures & How AI Works (Intermediate)** — From raw inputs to probabilistic tokens: transformers, self-attention mechanisms, diffusion image generation, and training loss optimization.
- **Tier 3: Systems, Data Provenance & Infrastructure (Upper Intermediate)** — Where training datasets come from, synthetic data, GPU cluster supercomputing, model distillation, and quantitative evaluation benchmarks.
- **Tier 4: Advanced Concepts, Alignment & Societal Horizon (Advanced / Expert)** — Emergent reasoning, interpretability/mechanistic safety, RLHF alignment tradeoffs, hallucination mitigation, and autonomous agent frameworks.

---

## 2. Topic Styles & Narrative Angles (20 Curated Formats)

To ensure high viewer retention, multi-format appeal, and diverse YouTube packaging, every topic in this channel is produced using one of the 20 niche angle presets defined in [`REGISTRY/Niches/001_ai_technology_explainers/ANGLE_PLAN.json`](file:///h:/script-raw-/REGISTRY/Niches/001_ai_technology_explainers/ANGLE_PLAN.json):

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

---

## 3. Topic Catalog (Scratch to Advanced)

### Tier 1: Foundations (Scratch / Beginner)
1. **AI Without Jargon: How Machine Learning Actually Works from Scratch**
   - *Question:* What does it really mean when we say an algorithm "learns" from data?
   - *Key Focus:* Pattern recognition, weight adjustments, statistical probability vs human reasoning, gradient descent simplified.
2. **Artificial Intelligence vs Machine Learning vs Deep Learning: The Definitive Map**
   - *Question:* How do symbolic AI, rule-based systems, neural networks, and modern LLMs differ structurally?
   - *Key Focus:* The taxonomy of AI, historical milestones (Turing, Dartmouth 1956, Expert Systems, Deep Learning era).
3. **The Anatomy of a Neural Network: Nodes, Layers, and Activation Functions**
   - *Question:* How does a mathematical perceptron turn raw numeric inputs into classifications and decisions?
   - *Key Focus:* Input, hidden, and output layers, activation thresholds (ReLU, Sigmoid), forward propagation.
4. **How AI Claims Compare to Reality: 7 Common Myths Debunked**
   - *Question:* Where does public AI hype diverge from verified technical benchmark evidence?
   - *Key Focus:* "Sentience" delusions, deterministic vs probabilistic outputs, stochastic parrots debate, true failure modes.

### Tier 2: Core Architectures & How AI Works (Intermediate)
5. **Attention Is All You Need: The Breakthrough That Changed AI Forever**
   - *Question:* How does the Transformer architecture process token relationships simultaneously instead of sequentially?
   - *Key Focus:* Self-attention mechanism, Query-Key-Value vectors, parallelized training, overcoming RNN/LSTM memory bottlenecks.
6. **From Prompt to Prediction: How Large Language Models Generate Sentences**
   - *Question:* What happens inside an LLM in the fractions of a second between pressing enter and receiving text?
   - *Key Focus:* Tokenization, embedding spaces, next-token probability distribution, temperature and top-p sampling.
7. **How AI Creates Images: The Physics of Latent Diffusion Models**
   - *Question:* Why do modern image generators add random noise to images just to learn how to remove it?
   - *Key Focus:* Forward diffusion (noise addition), reverse diffusion (denoising U-Net), text-conditioning via CLIP embeddings.
8. **Computer Vision Demystified: How Machines Recognize Objects in Pixels**
   - *Question:* How do Convolutional Neural Networks (CNNs) detect edges, textures, and composite faces?
   - *Key Focus:* Kernels, convolutions, feature extraction hierarchies, pooling layers, modern Vision Transformers (ViT).
9. **Speech Synthesis & Voice Cloning: Neural Audio Generation Explained**
   - *Question:* How do modern neural codecs and acoustic models replicate human vocal timbre and cadence?
   - *Key Focus:* Spectrograms, WaveNet, diffusion audio, zero-shot voice synthesis, acoustic feature extraction.

### Tier 3: Systems, Data Provenance & Infrastructure (Upper Intermediate)
10. **The Secret Labor Behind AI: Data Labeling, RLHF, and Content Moderation**
    - *Question:* What human workforce and annotation protocols make foundational models polite and functional?
    - *Key Focus:* Data annotation sweatshops, Reinforcement Learning from Human Feedback (RLHF), safety red-teaming.
11. **Where Training Data Comes From: Scraping the Web and Copyright Dilemmas**
    - *Question:* How are multi-terabyte datasets like Common Crawl curated, filtered, and contested under fair use?
    - *Key Focus:* Web scrapers, deduplication, synthetic dataset generation, copyright lawsuits, open vs proprietary datasets.
12. **The Compute Engine of AI: Inside the GPUs and Massive Data Centers**
    - *Question:* Why does AI require specialized tensor core chips and gigawatt power grids to train modern models?
    - *Key Focus:* Floating-point precision (FP16, FP8), H100 GPU clusters, inter-node networking (NVLink), cooling and energy demands.
13. **Model Cards & Evaluation: What Benchmarks Do and Do Not Prove**
    - *Question:* How do MMLU, GSM8K, and HumanEval measure capability, and why does benchmark contamination occur?
    - *Key Focus:* Evaluation metrics, model card documentation standards, data contamination, real-world generalization limits.
14. **Small Models & Quantization: Running Powerful AI Locally on Consumer Hardware**
    - *Question:* How can models originally requiring server farms be compressed to run on laptops and phones?
    - *Key Focus:* Model pruning, parameter quantization (4-bit, GGUF), distillation, edge AI deployment.

### Tier 4: Advanced Concepts, Alignment & Societal Horizon (Advanced / Expert)
15. **The Black Box Problem: Inside the Science of Mechanistic Interpretability**
    - *Question:* Can we trace and decode individual feature circuits inside deep neural networks?
    - *Key Focus:* Polysemantic neurons, sparse autoencoders, reverse-engineering neural circuits, Anthropic interpretability research.
16. **Why AI Hallucinates: Confabulation, Factuality, and Grounding Limits**
    - *Question:* Is hallucination an incurable mathematical property of probabilistic generative models?
    - *Key Focus:* Objective loss vs ground truth, retrieval-augmented generation (RAG), calibration, citation verification.
17. **AI Alignment and the Control Problem: Steering Superintelligent Systems**
    - *Question:* How do researchers ensure autonomous systems remain aligned with human values and safety bounds?
    - *Key Focus:* Specification gaming, instrumental convergence, reward hacking, constitutional AI principles.
18. **Autonomous AI Agents: From Chatbots to Goal-Driven Digital Workers**
    - *Question:* How do LLM agents decompose goals, utilize external APIs, maintain memory, and self-correct?
    - *Key Focus:* Tool use, ReAct prompting loops, vector databases for memory, multi-agent orchestration frameworks.
19. **The Economics of AI: The Hype Cycle vs Real Enterprise Value**
    - *Question:* Are enterprise companies achieving positive ROI from generative AI or facing an adoption plateau?
    - *Key Focus:* Total cost of ownership (TCO), unit economics of inference, productivity studies, historical tech bubble parallels.
20. **The Road to AGI: What Fundamental Breakthroughs Are Still Missing?**
    - *Question:* Why do scaling laws alone face limits, and what new paradigms (reasoning models, world models) are required?
    - *Key Focus:* Scaling laws vs compute walls, system 2 deliberative reasoning, embodied AI, world simulation models.

---

## 4. Flagship Launch Episode (Selected Route for P02 Workflow)
- **Niche ID:** 001 (AI + Technology Explainers)
- **Angle Preset:** `beginner_explainers` (AI Concepts Without Jargon)
- **Episode Title:** *How AI Actually Works: The Complete Guide to Machine Learning from Scratch*
- **Episode Slug:** `how_ai_actually_works_machine_learning_from_scratch`
- **Duration:** 10 Minutes (600 Seconds / 75 Scenes @ 8s fixed)
- **Execution:** Full Phases 0–5 Autonomous Text Package inside `OUTPUT/001_ai_technology_explainers/001_ai_technology_explainers_beginner_explainers_how_ai_actually_works_machine_learning_from_scratch/`.
