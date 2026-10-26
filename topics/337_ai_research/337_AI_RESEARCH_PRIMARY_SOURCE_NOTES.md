# AI research primary-source follow-up — 2026-10-24

## BANK-337-041 — 2012 ImageNet classification paper

- Primary conference proceedings: Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton, *ImageNet Classification with Deep Convolutional Neural Networks*, NeurIPS 2012: https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html .
- The abstract describes a deep convolutional model trained on the LSVRC-2010 ImageNet training set and reports top-1/top-5 test errors of 39.7%/18.9% for its specified setup.
- Limit: this is the authors' benchmark result under a dated dataset, metric and implementation. It does not prove general visual understanding, independently isolate every architectural contribution, or establish sole historical causality. The proceedings abstract was inspected; full methods and baseline comparisons need the linked paper before scripting fine detail.

## BANK-337-042 — WILDS

- Primary peer-reviewed conference paper: Koh et al., *WILDS: A Benchmark of in-the-Wild Distribution Shifts*, Proceedings of Machine Learning Research 139 (2021): https://proceedings.mlr.press/v139/koh21a.html .
- The authors curated 10 datasets spanning shifts across hospitals, camera traps, time and location, and report lower out-of-distribution than in-distribution performance for their standard training baselines.
- Limit: the selected tasks, partitions and baselines do not measure every population, deployment, current model or future update. A gap in this benchmark is not an individual medical or social outcome. Check the paper's exact split and metric before any numeric comparison.

## Scope and overlap

Archive pitches about generic ablation, data overlap, scaling, metric claims and replication route to existing 337 questions. AlexNet is framed as a dated research evaluation, leaving Transformer mechanism to 001; WILDS is a cross-domain research benchmark, leaving particular hospital-pathology transport to 336. Neither case is an assessment of coding assistants in 338.
