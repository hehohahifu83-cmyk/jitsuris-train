# e5-base frozen UNIT-context error audit (2026-10-18)

## Scope

Analyzed only `eval_reports/latest/job{1,2}_probs_{dev220,general,business,business2,japan_procurement}_ft.json`.
These are the five permitted fixed sets. No blind set, set 3, 5, or 7 was opened. The reports contain normalized column names, gold/predicted labels, and probabilities; no column values.

## Observed outcomes

| Set | Seed | Rows | Wrong | Critical wrong | Unknown |
|---|---:|---:|---:|---:|---:|
| dev220 | 1 | 220 | 6 | 1 | 0 |
| dev220 | 2 | 220 | 5 | 1 | 0 |
| general | 1 | 383 | 7 | 1 | 15 |
| general | 2 | 383 | 8 | 1 | 18 |
| business | 1 | 490 | 26 | 4 | 8 |
| business | 2 | 490 | 29 | 5 | 8 |
| business2 | 1 | 976 | 25 | 4 | 15 |
| business2 | 2 | 976 | 28 | 4 | 15 |
| japan_procurement | 1 | 92 | 0 | 0 | 1 |
| japan_procurement | 2 | 92 | 0 | 0 | 1 |

### Most frequent confusions by seed

- dev220, seed 1: quantity→category 2; org→person 1; org→account 1; category→text 1; id→quantity 1
- dev220, seed 2: quantity→category 2; category→text 1; category→tax_class 1; id→quantity 1
- general, seed 1: category→text 1; org→address 1; text→category 1; id→address 1; text→account 1; id→quantity 1
- general, seed 2: text→category 2; category→text 1; id→address 1; amount→id 1; text→account 1; id→category 1
- business, seed 1: category→quantity 10; org→account 4; category→id 2; amount→quantity 2; quantity→amount 1; org→address 1
- business, seed 2: category→quantity 12; org→account 4; amount→quantity 4; account→org 2; org→address 2; quantity→amount 1
- business2, seed 1: amount→quantity 3; quantity→category 3; account→category 2; id→category 2; category→id 2; quantity→address 2
- business2, seed 2: category→quantity 4; category→id 3; amount→quantity 3; id→category 2; org→address 2; quantity→address 2
- japan_procurement, seed 1: none
- japan_procurement, seed 2: none

### Critical errors recurring across both seeds

- dev220: `purchase order by customer`, id→quantity (seeds 1, 2)
- business: `total invoices paid`, quantity→amount (seeds 1, 2)
- business: `australian sourced goods`, amount→quantity (seeds 1, 2)
- business: `overseas sourced goods`, amount→quantity (seeds 1, 2)
- business2: `total invoices paid`, quantity→amount (seeds 1, 2)
- business2: `fine`, amount→quantity (seeds 1, 2)
- business2: `sales-goods-svcs_ventes-biens-srvs`, amount→quantity (seeds 1, 2)
- business2: `miscellaneous_divers`, amount→quantity (seeds 1, 2)

## Hypotheses, not conclusions

- The business/business2 sets repeatedly confuse `category` with `quantity`, and `amount` with `quantity`; the error pattern suggests that numeric-looking headers and label boundaries deserve focused audit. Because prediction JSON omits values and full table context, it cannot establish whether the model, taxonomy, or original label is responsible.
- The same critical error on a column in both seeds indicates a systematic case, not seed noise. It still does not prove that the label is wrong; do not relabel from model confidence alone.
- The general set has more `other`/`unknown` boundary cases, while the Japan procurement set has no wrong predictions in these two runs. Investigate guard/abstention and category/other ambiguity separately from classification accuracy.

## Next controlled test

Keep e5-base, UNIT context, frozen embeddings, batch/optimizer, epochs, and all other settings fixed; add only training-time text/value/context augmentation (`FT_AUG=1`) and compare seeds 1/2 with the matching frozen UNIT baseline. The transform creates different views of training rows; it does not copy evaluation errors into training.

Research basis: [Confident Learning](https://arxiv.org/abs/1911.00068) motivates checking label quality using prediction probabilities, but flagged cases require external review; [Robust Learning for Text Classification with Multi-source Noise Simulation and Hard Example Mining](https://arxiv.org/abs/2107.07113) supports testing robustness augmentation and hard-example methods, though its OCR task differs from Jitsuris and does not guarantee gains here.

Measure the five fixed sets separately: accuracy, wrong/critical errors, unknowns, training time, and peak GPU memory. Treat absolute differences under 1.5 percentage points as no difference. No label changes or automatic pseudo-labels will be accepted from this audit.

## Missing evidence

These reports do not contain raw values, same-table context, source-level duplicates, preprocessing traces, or a retained trained checkpoint. Root causes beyond observed confusion patterns remain unverified.


## Follow-up correction (2026-10-19)

The previous generic recommendation to test `FT_AUG=1` was stale: the paired e5-base, UNIT, frozen-embedding augmentation run had already completed before this audit was generated. Its two-seed results were compared with the matching no-augmentation baseline:

| Set | Baseline seed1/2 | FT_AUG seed1/2 | Mean delta |
|---|---:|---:|---:|
| dev220 | 95.9% / 97.3% | 95.9% / 96.8% | -0.25 pp |
| general | 92.5% / 91.5% | 90.8% / 93.6% | +0.20 pp |
| business | 92.4% / 91.8% | 91.4% / 92.4% | -0.20 pp |
| business2 | 95.3% / 95.5% | 95.1% / 95.5% | -0.10 pp |
| japan_procurement | 98.9% / 98.9% | 98.9% / 98.9% | 0.00 pp |

All average accuracy differences are under the predeclared 1.5-point threshold. Total wrong counts were 134 in both conditions; critical errors 20 vs 21; unknowns 89 vs 93. Do not repeat the same augmentation test or call it an accuracy gain.

A prior e5-base `FT_LR=2e-5` run covered seed 1 without frozen embeddings and was weaker on general/business. The next experiment tests whether the lower learning rate behaves differently with the selected frozen-embedding + UNIT setup: change only `FT_LR`, run seeds 1/2, and compare with the latest matched frozen baseline. This is an interaction check, not evidence that a gain is expected. Plan: [next-experiment-plan-2026-10-19.md](next-experiment-plan-2026-10-19.md).

The hard-coded `FT_AUG` suggestion in the report generator has been removed. New audits now direct reviewers to check the completed experiment ledger before naming another condition.
