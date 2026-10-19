# Numerical and diagram specifications
## Authoritative inputs
[Research_Calculations.json](../02_Phase1_RESEARCH_BIBLE/Research_Calculations.json) and [its derivation](../02_Phase1_RESEARCH_BIBLE/Facts_Documented.md) define all toy data.

| Stage | Exact display |
|---|---|
| Query | q = (√2 × ln 2, 0); dₖ = 2 |
| Keys A/B/C | (1,0); (0,1); (0,0) |
| Values A/B/C | (2,0); (0,4); (0,0) |
| Scaled scores | (ln 2, 0, 0) |
| Exponential contributions | (2,1,1) |
| Unmasked normalization total | 4 |
| Unmasked weights | (1/2,1/4,1/4) |
| Combined output | (1,1) |
| Allowed contributions after excluding C | (2,1,0); total 3 |
| Masked weights and output | (2/3,1/3,0); (4/3,4/3) |

Use fractions, not rounded decimals, for thirds. If bars accompany weights, use a fixed 0-to-1 scale, baseline zero and constant widths. Label weights as coefficients in the synthetic operation, never measured word importance. No percentages, benchmark charts or reported performance panels are planned.

## Animation acceptance
Reveal scores, exponentials, total, normalized weights and combined values in that order. C's exclusion changes normalization before weights update. Do not drop its original quarter and preserve the other old weights. Animate each coordinate separately for the weighted sum.

A source/year reference and synthetic label stay readable. Visual generation supplies no exact math. Reconcile rendered text and all diagram quantities against the calculation before accepting any real asset.
