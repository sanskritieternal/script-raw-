# Documented facts and original calculation

Research date: 2026-10-18. Use [Claim_Ledger.md](Claim_Ledger.md) for exact factual wording, sources and confidence. This file organizes that evidence without introducing additional historical or empirical claims.

## Evidence groups

| Research section | Claim IDs | Editorial use |
|---|---|---|
| Historical source identity | C001 | Orient to the dated source |
| Mechanism and architecture | C002–C008 | Explain the selected operation and its place in the system |
| Explanation limits | C009–C010 | Present attributed positions together |
| Original arithmetic | C011–C013 | Demonstrate transparent numbers with explicit limits |

## T1: invented one-query example

This is original educational data. A, B and C label abstract positions, not words, semantic classes or actual model tokens. The query is associated with position B for the masking example. We supply projected vectors directly; we do not claim they were learned. No trained model was run.

Define one query `q = (sqrt(2) * ln(2), 0)` and key dimension `d_k = 2`.

| Position | Key | Value |
|---|---|---|
| A | (1, 0) | (2, 0) |
| B | (0, 1) | (0, 4) |
| C | (0, 0) | (0, 0) |

For this example, apply `score_i = dot(q, key_i) / sqrt(2)`. The scores are `(ln(2), 0, 0)`. Their exponentials are `(2, 1, 1)` and their sum is 4. Normalization therefore gives `(1/2, 1/4, 1/4)`.

The weighted sum is `(1/2)*(2,0) + (1/4)*(0,4) + (1/4)*(0,0) = (1,1)`.

For a separate causal-mask illustration at B, exclude C before normalization. Treat its exponential contribution as zero; the allowed contributions sum to 3. The weights become `(2/3, 1/3, 0)` and the weighted sum becomes `(4/3, 4/3)`.

Simply erasing C's weight after the original normalization would leave a total of 3/4; that is not the masked calculation above. Do not animate this shortcut as equivalent.

## Checks and limits

Python standard-library `math` evaluated the dot products, scale, exponentials, normalization and sums. Results were compared with the fractions above at absolute tolerance 1e-12, with four component-wise comparisons passing. Floating-point thirds are stored as approximations in [Research_Calculations.json](Research_Calculations.json); use exact fractions in editorial labels where legible.

This calculation establishes only the arithmetic for supplied vectors. It does not establish that a model associates a word with a meaning, that a weight causes a full-network prediction, or that masking improves any task result. It omits training, multiple heads, other layers, dropout and a prediction head. These omissions must remain explicit in downstream instructions.

## Downstream acceptance criteria

- Preserve the label “synthetic example” wherever its numbers appear.
- Keep weights visually distinct from value vectors and the final combined vector.
- Keep the unmasked and masked examples distinct; do not imply they are an empirical before/after intervention.
- Use C009–C010 for the attributed methodological discussion, rather than using this toy example to settle it.
- Check all numerical overlays against the JSON and exact expressions before accepting a scene draft.
