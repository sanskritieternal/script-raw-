# Selected primary-source research: dated statistical cases

Checked 2026-10-24. These source checks bound four proposed questions; they do not verify the other archived hooks, complete a script, or approve production.

## Berkeley graduate admissions, fall 1973 — BANK-121-047

- Primary study: P. J. Bickel, E. A. Hammel and J. W. O’Connell, “Sex Bias in Graduate Admissions: Data from Berkeley,” *Science* 187 (1975), 398–404. [Original article scan](https://faculty.ucmerced.edu/jvevea/classes/Spark/readings/Bickel-Berkeley.pdf).
- The paper analyzes 12,763 sufficiently complete fall 1973 applications across 101 departments or interdepartmental majors. Its campus totals show about 44% of male applicants and 35% of female applicants admitted. The authors then compare department-level patterns, where program choice and differing admission rates change the interpretation.
- Limit: This is one application cycle at one university. The article explicitly separates aggregate association from an individual decision’s causes. Do not retell it as “women were favored in every department,” as proof that discrimination did or did not exist, or as a medical treatment result. The widely reused six-department example is a subset of the full analysis.

## 2020 Census privacy implementation — BANK-121-048

- Primary operator sources: U.S. Census Bureau, [Decennial Census Disclosure Avoidance](https://www.census.gov/programs-surveys/decennial-census/disclosure-avoidance.2020.html) and [2020 TopDown Algorithm working paper](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html).
- The bureau describes the 2020 Disclosure Avoidance System as using differential-privacy accounting for published census tables. It identifies apportionment state totals as an exception to statistical noise. The TopDown paper describes the particular algorithm, rather than every possible differential-privacy design.
- Limit: Product, geography, table, invariant and release version matter. A formal privacy guarantee is conditional on the stated mechanism and budget; avoid claiming zero disclosure risk or uniform accuracy of every small-area statistic. The original BANK-121-025 wording is retained as an unverified pitch.

## ASA p-value statement, 2016 — BANK-121-049

- Primary organization source: American Statistical Association, [2016 statement on statistical significance and p-values](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf).
- Its six principles warn that a p-value does not measure the probability the studied hypothesis is true or the size or importance of an effect, and that scientific or policy decisions should not hinge solely on a threshold.
- Limit: This is guidance about interpretation and reporting, not a finding that every use of 0.05 is invalid or a demonstration that a particular result is false. Separate the dated 2016 statement from later journal editorials and task-force positions.

## Wells Fargo sales targets — BANK-121-050

- Primary regulator source: Consumer Financial Protection Bureau, [September 8, 2016 consent order](https://files.consumerfinance.gov/f/documents/092016_cfpb_WFBconsentorder.pdf) and [enforcement announcement](https://www.consumerfinance.gov/archive/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/).
- The CFPB describes unauthorized accounts and other products opened or enrolled under sales targets and compensation incentives. This supports a bounded example of a performance count being gamed.
- Limit: The order establishes the regulator’s findings and legal disposition for the conduct it addresses. Do not infer that every account was unauthorized, that a mathematical law caused individual acts, or that a specific employee’s motive is known from the aggregate record. The broader banking scandal belongs to a finance or regulatory treatment; this BANK question stays on metric design and data quality.
