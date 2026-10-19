# 保存済みモデルの推論評価（学習なし）

- source checkpoint: Actions run 39241962638, job1, seed 1
- training configuration: multilingual-e5-base, 2 epochs
- fixed development datasets only; ft and blend70; 10 row-level comparisons
- comparison includes row order, normalized header, truth, final decision, and top-1 label
- lower top-3 ranks may swap only when rank-aligned probabilities stay within tolerance
- top-3 probabilities must differ by at most 0.005
- schema version 3 records include decision reasons; column values are not saved.

| dataset | condition | accuracy | wrong | unknown | critical | n (truth other excluded) | max drift |
|---|---:|---:|---:|---:|---:|---:|---:|
| dev220 | ft | 96.8% | 7 | 0 | 1 | 220 | 0.000005 |
| dev220 | blend70 | 96.8% | 7 | 0 | 1 | 220 | 0.000906 |
| general | ft | 91.2% | 9 | 17 | 1 | 295 | 0.000004 |
| general | blend70 | 90.8% | 9 | 18 | 1 | 295 | 0.000926 |
| business | ft | 92.2% | 26 | 11 | 1 | 475 | 0.000008 |
| business | blend70 | 91.8% | 21 | 18 | 0 | 475 | 0.000952 |
| business2 | ft | 95.9% | 22 | 15 | 3 | 913 | 0.000005 |
| business2 | blend70 | 95.9% | 20 | 17 | 3 | 913 | 0.001293 |
| japan_procurement | ft | 98.9% | 0 | 1 | 0 | 92 | 0.000000 |
| japan_procurement | blend70 | 98.9% | 0 | 1 | 0 | 92 | 0.000320 |

n excludes rows whose truth is other; all row records were included in parity checks.

All ten comparisons passed.
