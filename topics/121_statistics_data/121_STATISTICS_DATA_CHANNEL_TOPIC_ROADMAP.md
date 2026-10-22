# Statistics & Data Channel Master Topic Roadmap (Scratch to Advanced)
**Niche:** 121 Statistics & Data (Math_Scientific_Methods)  
**Channel Language:** English (YouTube)  
**Target Audience:** Data Scientists, Statisticians, Analysts, Machine Learning Engineers, Curious Decision-Makers (Global)  
**Production Format:** 10-Minute Documentary Explainer Episodes (600s, 75 Fixed 8s Scenes)  
**Execution & Sync Report:** [topics/121_statistics_data/TOPICS_COVERED_REPORT.md](./TOPICS_COVERED_REPORT.md)  

---

## 1. Channel Progression Strategy

This curriculum organizes the core disciplines of Statistics & Data across four progressive tiers:
- **Tier 1: Descriptive Statistics, Probability Foundations & Distributions (Beginner / Scratch)** — Mean vs median vs mode skewness, variance and standard deviation, normal Gaussian bell curves, the Central Limit Theorem, and basic combinatorics.
- **Tier 2: Inferential Statistics, Hypothesis Testing & Regression Modeling (Intermediate)** — Null hypothesis significance testing (NHST), p-values and alpha thresholds, Type I and Type II errors, confidence intervals, and ordinary least squares (OLS) linear regression.
- **Tier 3: Causal Inference, Bayesian Analytics & Big Data Architectures (Upper Intermediate)** — Simpson's paradox, difference-in-differences, instrumental variables, Bayesian prior updating, Monte Carlo Markov Chain (MCMC) simulations, and A/B test sample sizing.
- **Tier 4: Statistical Misdirection, AI Bias & Master Data Architecture (Advanced / Masterclass)** — Darrell Huff's deceptive chart axes, survivor bias (Abraham Wald's bomber armor), algorithmic feedback loops, differential privacy, and enterprise data governance.

---

## 2. Topic Styles & Narrative Angles (32 Curated Formats)

Every episode is produced using one of the 32 niche angle presets defined in [`REGISTRY/Niches/121_statistics_data/ANGLE_PLAN.json`](file:///h:/script-raw-/REGISTRY/Niches/121_statistics_data/ANGLE_PLAN.json):

| # | Angle Slug / Style | Primary Angle Focus | Core Story Question Formulated |
|---|---|---|---|
| 1 | `history_origins` | **Why a Statistical Method Was Invented** | *Which research or administrative problem motivated one method?* |
| 2 | `famous_examples` | **A Famous Dataset Reanalyzed** | *Does a widely cited result survive alternative valid analyses?* |
| 3 | `hidden_stories` | **Who Was Not Counted?** | *Which population was missed by a survey or administrative dataset?* |
| 4 | `beginner_explainers` | **What Does the Average Hide?** | *How can identical averages describe different distributions?* |
| 5 | `advanced_concepts` | **Estimand Before Estimate** | *What quantity is a study trying to learn, and what was actually measured?* |
| 6 | `mysteries_unsolved_cases` | **Conflicting Statistics** | *Why do two credible estimates of the same topic disagree?* |
| 7 | `technology_innovation` | **A New Data Pipeline** | *Did automation improve timeliness at the cost of data quality?* |
| 8 | `people_personalities` | **The Statistician's Design Choice** | *Which sampling or modeling decision shaped one result?* |
| 9 | `major_events` | **A Revision Changes the Headline** | *Why did an official estimate change after release?* |
| 10 | `how_it_works` | **From Sample to Estimate** | *How is a sample used to estimate a population quantity?* |
| 11 | `rise_fall` | **A Metric Loses Trust** | *Which documented errors or incentives weakened one indicator?* |
| 12 | `then_vs_now` | **A Trend That May Not Be Comparable** | *Did a method change create an apparent rise or fall?* |
| 13 | `future_developments` | **Designing the Next Data Collection** | *What information would most reduce uncertainty on one question?* |
| 14 | `myths_vs_facts` | **Significant Means Important?** | *Does a reported statistical significance imply a meaningful effect?* |
| 15 | `documentary_stories` | **A Number's Production Trail** | *How did one public statistic move from raw records to headline?* |
| 16 | `observation_to_explanation` | **A Correlation Appears** | *Can one observed association support a causal story?* |
| 17 | `measurement_method` | **Measuring What Matters** | *Does a variable capture the concept named in a chart?* |
| 18 | `scale_and_timespan` | **Daily Noise and Long Trend** | *How does aggregation change an apparent pattern?* |
| 19 | `field_vs_lab` | **Controlled Sample Versus Population** | *Can a study result apply outside its recruited participants?* |
| 20 | `natural_variation` | **Separating Signal From Variation** | *Is a change larger than expected sampling or process variation?* |
| 21 | `mechanism_chain` | **From Treatment to Outcome** | *Which measured steps support a proposed causal pathway?* |
| 22 | `extreme_case` | **An Outlier in the Dataset** | *Is an extreme value an error, a real case, or a sign of model failure?* |
| 23 | `classification_debate` | **Changing a Category** | *How do alternative category boundaries change an estimate?* |
| 24 | `interacting_systems` | **Two Variables Are Not Enough** | *Which interacting factors change one statistical relationship?* |
| 25 | `data_gap` | **Missing Data Are Not Random** | *How could nonresponse distort one conclusion?* |
| 26 | `prediction_test` | **A Model Meets New Data** | *How well did a prediction perform beyond its training sample?* |
| 27 | `human_impact` | **A Metric Used to Allocate Resources** | *Who gains or loses when one indicator drives a decision?* |
| 28 | `field_proof_or_test` | **Checking a Statistical Claim** | *Can an independent analyst reproduce one published estimate?* |
| 29 | `field_definition_choice` | **Who Is in the Denominator?** | *How does denominator choice change a reported rate?* |
| 30 | `field_model_assumptions` | **What the Model Assumes** | *Which assumption most influences one estimate?* |
| 31 | `field_counterexample` | **Averages Mislead** | *Can two groups have the same average but very different outcomes?* |
| 32 | `field_teaching_difficulty` | **Reading Uncertainty Correctly** | *Which mistake do learners make about one confidence interval or p-value?* |

---

## 3. Topic Catalog (Scratch to Advanced Curriculum)

### Tier 1: Foundational Frameworks
1. **How to Lie with Statistics: Deceptive Charts and Simpson's Paradox**
   - *Question:* How can a medical treatment appear superior in every single patient sub-group yet fail completely when aggregated?
   - *Key Focus:* Simpson's paradox, truncated Y-axes, cherry-picked baselines, 3D chart distortion, and Darrell Huff's classic deception tactics.
2. **The Central Limit Theorem: The Miracle That Makes Statistics Work**
   - *Question:* Why do the averages of virtually any random distribution inevitably form a perfect Gaussian bell curve?
   - *Key Focus:* Sample means convergence, standard error of the mean, normal distribution properties, and the mathematical bedrock of polling.
3. **Mean, Median, and Mode: Why Averages Lie in Unequal Worlds**
   - *Question:* Why does a single billionaire walking into a bar make every patron an 'average millionaire'?
   - *Key Focus:* Right-skewed power law distributions, median household wealth vs mean, bimodal distributions, and outlier sensitivity.
4. **Abraham Wald and Survivorship Bias: Where Not to Put Armor on Airplanes**
   - *Question:* Why did a mathematician order military brass to reinforce the airplane parts with ZERO bullet holes?
   - *Key Focus:* Missing data bias, selection mechanisms, WWII Statistical Research Group, and why studying successful startup founders misleads entrepreneurs.
5. **P-Values and the 0.05 Threshold: The Arbitrary Gatekeeper of Science**
   - *Question:* Why did Ronald Fisher pick 0.05 as the boundary for 'statistical significance', and why is it breaking modern science?
   - *Key Focus:* Null hypothesis, alpha error rates, false positive probabilities, p-hacking, and the American Statistical Association statement.
### Tier 2: Practical Mechanics & Channels
6. **The Monte Hall Problem: Why Your Brain Hates Conditional Probability**
   - *Question:* Why did hundreds of PhD mathematicians send hate mail insisting you shouldn't switch doors on a game show?
   - *Key Focus:* Marilyn vos Savant controversy, sample space enumeration, updating conditional probabilities, and cognitive intuition failures.
7. **Linear Regression and the Ordinary Least Squares (OLS) Engine**
   - *Question:* How do algorithms find the exact best-fitting line through a scattered cloud of noisy data points?
   - *Key Focus:* Sum of squared errors (SSE), slope and intercept formulas, R-squared variance explained, and Gauss-Markov theorem assumptions.
8. **A/B Testing at Scale: How Tech Giants Run 10,000 Experiments a Year**
   - *Question:* How does Google determine if changing a button's blue shade by 2% increases ad revenue by $200 million?
   - *Key Focus:* Statistical power (1 - beta), minimum detectable effect (MDE), sample size calculation, peeking bias, and multi-armed bandits.
9. **Power Laws and Fat Tails: Why the Normal Curve Fails in Finance and Pandemics**
   - *Question:* Why do Gaussian models underestimate stock market crashes by factors of a billion?
   - *Key Focus:* Nassim Taleb's Mediocristan vs Extremistan, Pareto 80/20 distributions, kurtosis, fat-tailed risk, and Black Swan events.
10. **Florence Nightingale: The Data Visualization Pioneer Who Saved Armies with Charts**
   - *Question:* How did a Victorian nurse use innovative rose/polar area diagrams to prove dirty hospital sewage killed more soldiers than enemy bullets?
   - *Key Focus:* Polar area coxcomb charts, statistical visual persuasion, British Royal Commission sanitary reforms, and evidence-based public health.
### Tier 3: Strategic & Advanced Architectures
11. **Causal Inference: Judea Pearl's Ladder of Causation**
   - *Question:* Why can associative machine learning models never answer 'Why?' without causal diagrams?
   - *Key Focus:* Directed Acyclic Graphs (DAGs), counterfactuals, do-calculus, confounding backdoors, and difference-in-differences econometrics.
12. **Monte Carlo Simulations: Solving Impossible Math with Millions of Dice Rolls**
   - *Question:* How did Stanislaw Ulam invent a simulation method while playing solitaire that helped design the hydrogen bomb?
   - *Key Focus:* Pseudorandom number generators, probability integration, financial portfolio stress-testing, and Markov Chain Monte Carlo (MCMC).
13. **The Overfitting Trap: Why Beautiful Models Flop in the Real World**
   - *Question:* Why does a model that predicts past stock prices with 99.9% accuracy lose all your money tomorrow?
   - *Key Focus:* Bias-variance tradeoff, memorizing noise vs signal, train-validation-test splits, cross-validation, and regularization (L1 Lasso / L2 Ridge).
14. **Election Polling Decoded: How 1,000 People Represent 300 Million Citizens**
   - *Question:* How do pollsters adjust for non-response bias, cell phone usage, educational weighting, and shy voters?
   - *Key Focus:* Stratified random sampling, demographic post-stratification weighting, likely voter screens, and margin of error calculations.
15. **Algorithmic Bias: When Data Models Automate Historic Discrimination**
   - *Question:* How do recidivism risk scoring algorithms (COMPAS) and automated loan screeners institutionalize racial bias?
   - *Key Focus:* Proxy variables, historical training label bias, disparate impact vs disparate treatment, and fairness metrics mathematical trade-offs.
### Tier 4: Future Horizons & Masterclasses
16. **Differential Privacy: How Apple and the US Census Collect Data Without Revealing You**
   - *Question:* How can an algorithm mathematically guarantee that your personal medical record cannot be extracted from a public database?
   - *Key Focus:* Epsilon privacy budget, Laplace noise injection, randomized response technique, and the 2020 US Census privacy overhaul.
17. **Goodhart's Law: When a Statistical Metric Becomes a Target, It Ceases to Be a Good Metric**
   - *Question:* Why did British colonial bounties on cobra skins cause locals to breed thousands of cobras at home?
   - *Key Focus:* Campbell's law, metric gaming, standardized testing perverse incentives, corporate KPI distortion, and vanity metrics.
18. **Benford's Law: The Mathematical Anomaly Catching Tax Frauds and Election Cheats**
   - *Question:* Why does the number 1 appear as the first digit in naturally occurring numbers 30% of the time, while 9 appears only 4%?
   - *Key Focus:* Scale invariance, logarithmic distributions, forensic accounting detection (Enron), and detecting falsified balance sheets.
19. **Data Governance and Lakehouses: The Plumbing of Enterprise Intelligence**
   - *Question:* How do modern corporations manage petabytes of unstructured data across Snowflake, Databricks, and S3 without total chaos?
   - *Key Focus:* ETL vs ELT pipelines, data mesh architecture, schema evolution, data lineage, and regulatory compliance (GDPR/CCPA).
20. **The Master Data Architecture: The Quantitative Decision-Making Blueprint**
   - *Question:* What comprehensive framework unites descriptive discovery, rigorous causal testing, Bayesian updating, and ethical governance?
   - *Key Focus:* End-to-end data pipeline integrity, hypothesis-driven experimentation frameworks, executive metric hygiene, and automated validation.

---

## 4. Flagship Launch Episode
- **Niche ID:** 121 (Statistics & Data)
- **Angle Preset:** `root_cause_analysis`
- **Episode Title:** *How to Lie with Statistics: Deceptive Charts and Simpson's Paradox*
- **Episode Slug:** `121_statistics_data_root_cause_analysis_how_to_lie_with_statistics`
- **Duration:** 10 Minutes (600 Seconds / 75 Scenes @ 8s fixed)
- **Execution:** Full Phases 0–5 Autonomous Production Package inside `OUTPUT/121_statistics_data/`.
