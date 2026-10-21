# W2/W6 validation-only experiments

Run date: 2026-10-21. The analysis uses `eval_reports/runs/39496935773`, job2 (E5-base, seed 1, `FT_LR=3e-5`, `FT_VAL=1`) and its four learning-side validation splits. It excludes run 39506074807 and all fixed, independent, sealed, and blind evaluation sets. The script verified all 889 saved rows against the source validation split and restored their source-table group IDs; the 889 rows cover 148 tables. It used no cell values and writes aggregate metrics only.

## W2: same-table probability reranker

A logistic-regression reranker (`C=1`) used the first-pass top-3 probabilities, same-table peer mean and maximum probabilities, normalized column position, and table length. Five-fold `GroupKFold` kept every source table in one fold.

| Measure | Existing guarded result | Out-of-fold reranker |
|---|---:|---:|
| Unknown-header OK | 203/255 (79.6%) | 202/255 (79.2%) |
| Unknown-header critical numeric errors | 2 | 2 |
| All validation OK | 822/889 (92.5%) | 826/889 (92.9%) |

W2 does not meet its preregistered unknown-header gain of +1.0 percentage point. The overall gain is +0.45 points, but the unknown-header slice falls by 0.39 points, and critical errors do not decrease. Do not forward this reranker as a candidate.

## W6: top-1 calibration and selective threshold

The saved files contain top-3 probabilities rather than the full 16-class vector or logits. Therefore, the temperature experiment is a grouped cross-fit of binary top-1 correctness, not full multiclass temperature scaling. The median fitted temperature was 1.039 (range 0.946–1.093). Equal-count ECE improved from 4.13% to 3.75%, while Brier score changed from 0.04478 to 0.04505 and log loss from 0.15786 to 0.16156; the overall calibration evidence is mixed.

As an empirical threshold curve, `tau=0.90` reduced critical numeric confusions from 2 to 0 among 391 answered critical predictions (baseline: 2 among 403). The overall unknown rate rose from 11.02% to 13.61% (+2.59 points), and false numeric answers on `other` rows fell from 14 to 4. This meets the empirical +3-point abstention budget, but it is not a certified risk guarantee.

For a conservative table-grouped Learn-then-Test check, 103 tables fit the temperature and 45 disjoint tables calibrated the threshold. At a 5% target and 95% confidence, the Bonferroni Hoeffding upper bound was 23.75% for every tested threshold; no candidate was certified. This bound concerns mean table-level selective loss and does not certify pooled per-column risk. Do not forward W6 as a qualified candidate. A future attempt needs more independent table groups and full-class scores, or a preregistered risk target and guarantee matched to the actual deployment unit.

The machine-readable aggregate output is `bench/w2_w6_validation_20261021.json`; the reproducible validation-only analysis is `bench/w2_w6_validation.py`.
