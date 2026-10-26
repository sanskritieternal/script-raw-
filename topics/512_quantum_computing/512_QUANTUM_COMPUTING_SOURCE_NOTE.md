# Quantum computing source follow-up - 2026-10-24

## BANK-512-044 - 2023 Google surface-code scaling experiment

- Primary paper: Google Quantum AI, *Suppressing quantum errors by scaling a surface code logical qubit*, Nature 614, 676-681 (published February 22, 2023), DOI 10.1038/s41586-022-05434-1, https://pmc.ncbi.nlm.nih.gov/articles/PMC9946823/ (open full-text copy inspected 2026-10-24; publisher https://www.nature.com/articles/s41586-022-05434-1). The team reports a 72-physical-qubit superconducting device, comparing a 49-qubit distance-5 surface-code logical qubit against an ensemble of 17-qubit distance-3 logical qubits. Reported average logical error per cycle over 25 cycles was 2.914 +/- 0.016% versus 3.028 +/- 0.023% (distance-5 versus distance-3), a modest comparison under the tested conditions.
- Primary team explanation: Google Quantum AI, *Suppressing quantum errors by scaling a surface code logical qubit*, https://research.google/blog/suppressing-quantum-errors-by-scaling-a-surface-code-logical-qubit/ (inspected 2026-10-24). Use as authors' interpretation, not independent replication.
- Claim limits: This is a controlled comparison of particular code sizes, hardware, errors and cycle count, not a useful fault-tolerant machine, arbitrary computation, cryptographic threat timeline or demonstrated algorithmic speedup. Average ensemble comparison is not every distance-3 subset; check the paper's methods and correlated-error discussion before scripting. Later hardware and results may differ.

## Scope and overlap

BANK-512-044 is a dated physical experiment. BANK-512-043 states the general scaling principle; BANK-512-034 covers classical benchmark fairness and BANK-512-040 algorithmic resource estimates.
