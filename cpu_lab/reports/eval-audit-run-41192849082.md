# D2 固定5集合の全件監査

- 対象: GitHub Actions run `41192849082`、artifact `13040484799` (`jitsuris-evaluation-reports`)。ZIP SHA-256: `40fabdc5262399ad36f7b0a089165fc2c201eb18b781f3b705f2e6112e313d2c`。
- 確認日時: 2026-10-31 21:37 JST。許可された固定5集合のみを対象にし、封印・blind set は開いていない。
- artifact: 205ファイル（4 manifest、確率JSON 100、error JSON 100、`ERROR_ANALYSIS.md` 1）。4 job × 5集合 × 5条件、43,220行。各ファイルは2,161行。

## 4 job と重み

| Job | 条件 | Seed | FT_LABELFIX | 重み SHA-256 |
|---:|---|---:|---|---|
| 1 | A3 | 3 | なし | `7a649600bf9e03a6d3513991a54280cbb68d348527f4d0bb4657e9514267a19e` |
| 2 | L | 1 | materials/pool/labelfix_v24.jsonl | `df4958d40c50bc7696d070faccfacb21741d3ec99143aa3b310b9415ad59ba1c` |
| 3 | L | 2 | materials/pool/labelfix_v24.jsonl | `55d3a5a346afa41325ab4c0e78586700985e26bfda523b35f9960af2a8f78c92` |
| 4 | L | 3 | materials/pool/labelfix_v24.jsonl | `d12dd6d658c5e4d5c28ced997536a9470b97c63253667c56579df42718f155a1` |

4つのmanifestはすべて `completed`。seed・FT_LABELFIX・重みSHAは D2 の重み台帳と一致し、200個すべてのJSONのSHA-256も各job manifestと一致。ファイル名・seed・dataset・conditionのmetadata、行数、0から始まる連続indexを確認した。どのjob/conditionでも各indexの列名と正解ラベルは一致。error JSONは、対応する確率JSONの `wrong`・`unknown`・`other_ng` 行と完全一致（差分 **0**）。監査上の不一致 **0件**。

## job・条件別の集計

`正解率`は `correct` と、正解がotherで安全にunknownへ退避した `other_ok` を合わせて算出。`other誤り`は `other_ng`。`重大`は、誤り・unknown・other誤りのうちcriticalが付いた出力。各条件は5集合を合算している。

| Job | Seed | 条件 | 行 | 正解率 | 誤り | other誤り | 重大 | unknown |
|---:|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | ft | 2,161 | 96.30% | 37 | 9 | 5 | 34 |
| 1 | 3 | blend50 | 2,161 | 95.42% | 30 | 7 | 2 | 62 |
| 1 | 3 | blend60 | 2,161 | 96.34% | 26 | 6 | 2 | 47 |
| 1 | 3 | blend70 | 2,161 | 96.48% | 31 | 6 | 3 | 39 |
| 1 | 3 | sparse | 2,161 | 91.21% | 97 | 32 | 24 | 61 |
| 2 | 1 | ft | 2,161 | 96.25% | 40 | 10 | 3 | 31 |
| 2 | 1 | blend50 | 2,161 | 95.14% | 29 | 7 | 3 | 69 |
| 2 | 1 | blend60 | 2,161 | 96.16% | 28 | 6 | 3 | 49 |
| 2 | 1 | blend70 | 2,161 | 96.30% | 32 | 7 | 4 | 41 |
| 2 | 1 | sparse | 2,161 | 91.30% | 100 | 29 | 26 | 59 |
| 3 | 2 | ft | 2,161 | 96.44% | 36 | 8 | 5 | 33 |
| 3 | 2 | blend50 | 2,161 | 95.19% | 29 | 8 | 3 | 67 |
| 3 | 2 | blend60 | 2,161 | 96.16% | 26 | 7 | 3 | 50 |
| 3 | 2 | blend70 | 2,161 | 96.21% | 32 | 8 | 5 | 42 |
| 3 | 2 | sparse | 2,161 | 91.30% | 100 | 29 | 26 | 59 |
| 4 | 3 | ft | 2,161 | 96.44% | 43 | 7 | 6 | 27 |
| 4 | 3 | blend50 | 2,161 | 95.33% | 30 | 5 | 3 | 66 |
| 4 | 3 | blend60 | 2,161 | 96.21% | 29 | 4 | 3 | 49 |
| 4 | 3 | blend70 | 2,161 | 96.48% | 32 | 5 | 3 | 39 |
| 4 | 3 | sparse | 2,161 | 91.30% | 100 | 29 | 26 | 59 |

## 集合別

| Job | 集合 | 条件 | 行 | 正解率 | 誤り | other誤り | 重大 | unknown |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | dev220 | ft | 220 | 96.82% | 5 | 0 | 1 | 2 |
| 1 | dev220 | blend50 | 220 | 94.55% | 7 | 0 | 1 | 5 |
| 1 | dev220 | blend60 | 220 | 97.27% | 6 | 0 | 1 | 0 |
| 1 | dev220 | blend70 | 220 | 97.27% | 6 | 0 | 1 | 0 |
| 1 | dev220 | sparse | 220 | 86.36% | 21 | 0 | 1 | 9 |
| 1 | general | ft | 383 | 92.95% | 9 | 7 | 1 | 11 |
| 1 | general | blend50 | 383 | 92.95% | 8 | 6 | 0 | 13 |
| 1 | general | blend60 | 383 | 93.99% | 5 | 5 | 0 | 13 |
| 1 | general | blend70 | 383 | 93.21% | 6 | 6 | 0 | 14 |
| 1 | general | sparse | 383 | 86.42% | 22 | 16 | 1 | 14 |
| 1 | business | ft | 490 | 96.94% | 7 | 1 | 0 | 7 |
| 1 | business | blend50 | 490 | 96.33% | 5 | 0 | 0 | 13 |
| 1 | business | blend60 | 490 | 96.73% | 4 | 0 | 0 | 12 |
| 1 | business | blend70 | 490 | 97.35% | 5 | 0 | 0 | 8 |
| 1 | business | sparse | 490 | 92.45% | 24 | 1 | 11 | 12 |
| 1 | business2 | ft | 976 | 96.82% | 16 | 1 | 3 | 14 |
| 1 | business2 | blend50 | 976 | 95.70% | 10 | 1 | 1 | 31 |
| 1 | business2 | blend60 | 976 | 96.52% | 11 | 1 | 1 | 22 |
| 1 | business2 | blend70 | 976 | 96.82% | 14 | 0 | 2 | 17 |
| 1 | business2 | sparse | 976 | 92.73% | 30 | 15 | 11 | 26 |
| 1 | japan_procurement | ft | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 1 | japan_procurement | blend50 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 1 | japan_procurement | blend60 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 1 | japan_procurement | blend70 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 1 | japan_procurement | sparse | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 2 | dev220 | ft | 220 | 97.27% | 6 | 0 | 1 | 0 |
| 2 | dev220 | blend50 | 220 | 94.09% | 6 | 0 | 1 | 7 |
| 2 | dev220 | blend60 | 220 | 97.27% | 5 | 0 | 1 | 1 |
| 2 | dev220 | blend70 | 220 | 97.73% | 4 | 0 | 1 | 1 |
| 2 | dev220 | sparse | 220 | 87.27% | 21 | 0 | 2 | 7 |
| 2 | general | ft | 383 | 92.69% | 9 | 9 | 0 | 10 |
| 2 | general | blend50 | 383 | 93.21% | 7 | 5 | 0 | 14 |
| 2 | general | blend60 | 383 | 92.95% | 5 | 6 | 0 | 16 |
| 2 | general | blend70 | 383 | 92.95% | 8 | 7 | 0 | 12 |
| 2 | general | sparse | 383 | 85.64% | 22 | 16 | 1 | 17 |
| 2 | business | ft | 490 | 96.94% | 10 | 1 | 0 | 4 |
| 2 | business | blend50 | 490 | 95.10% | 4 | 0 | 0 | 20 |
| 2 | business | blend60 | 490 | 96.53% | 5 | 0 | 0 | 12 |
| 2 | business | blend70 | 490 | 97.14% | 6 | 0 | 0 | 8 |
| 2 | business | sparse | 490 | 91.63% | 28 | 1 | 12 | 12 |
| 2 | business2 | ft | 976 | 96.72% | 15 | 0 | 2 | 17 |
| 2 | business2 | blend50 | 976 | 95.70% | 12 | 2 | 2 | 28 |
| 2 | business2 | blend60 | 976 | 96.62% | 13 | 0 | 2 | 20 |
| 2 | business2 | blend70 | 976 | 96.52% | 14 | 0 | 3 | 20 |
| 2 | business2 | sparse | 976 | 93.44% | 29 | 12 | 11 | 23 |
| 2 | japan_procurement | ft | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 2 | japan_procurement | blend50 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 2 | japan_procurement | blend60 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 2 | japan_procurement | blend70 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 2 | japan_procurement | sparse | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 3 | dev220 | ft | 220 | 96.82% | 6 | 0 | 1 | 1 |
| 3 | dev220 | blend50 | 220 | 94.55% | 4 | 0 | 1 | 8 |
| 3 | dev220 | blend60 | 220 | 97.73% | 4 | 0 | 1 | 1 |
| 3 | dev220 | blend70 | 220 | 97.73% | 5 | 0 | 1 | 0 |
| 3 | dev220 | sparse | 220 | 87.27% | 21 | 0 | 2 | 7 |
| 3 | general | ft | 383 | 93.21% | 9 | 7 | 1 | 10 |
| 3 | general | blend50 | 383 | 92.17% | 8 | 6 | 0 | 16 |
| 3 | general | blend60 | 383 | 92.69% | 8 | 6 | 0 | 14 |
| 3 | general | blend70 | 383 | 92.69% | 10 | 7 | 1 | 11 |
| 3 | general | sparse | 383 | 85.64% | 22 | 16 | 1 | 17 |
| 3 | business | ft | 490 | 97.76% | 7 | 0 | 0 | 4 |
| 3 | business | blend50 | 490 | 95.92% | 3 | 0 | 0 | 17 |
| 3 | business | blend60 | 490 | 97.14% | 3 | 0 | 0 | 11 |
| 3 | business | blend70 | 490 | 97.14% | 4 | 0 | 0 | 10 |
| 3 | business | sparse | 490 | 91.63% | 28 | 1 | 12 | 12 |
| 3 | business2 | ft | 976 | 96.62% | 14 | 1 | 3 | 18 |
| 3 | business2 | blend50 | 976 | 95.70% | 14 | 2 | 2 | 26 |
| 3 | business2 | blend60 | 976 | 96.31% | 11 | 1 | 2 | 24 |
| 3 | business2 | blend70 | 976 | 96.41% | 13 | 1 | 3 | 21 |
| 3 | business2 | sparse | 976 | 93.44% | 29 | 12 | 11 | 23 |
| 3 | japan_procurement | ft | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 3 | japan_procurement | blend50 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 3 | japan_procurement | blend60 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 3 | japan_procurement | blend70 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 3 | japan_procurement | sparse | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 4 | dev220 | ft | 220 | 97.27% | 6 | 0 | 1 | 0 |
| 4 | dev220 | blend50 | 220 | 94.55% | 5 | 0 | 1 | 7 |
| 4 | dev220 | blend60 | 220 | 97.27% | 6 | 0 | 1 | 0 |
| 4 | dev220 | blend70 | 220 | 97.27% | 6 | 0 | 1 | 0 |
| 4 | dev220 | sparse | 220 | 87.27% | 21 | 0 | 2 | 7 |
| 4 | general | ft | 383 | 92.43% | 12 | 5 | 1 | 12 |
| 4 | general | blend50 | 383 | 92.43% | 8 | 4 | 0 | 17 |
| 4 | general | blend60 | 383 | 93.73% | 7 | 3 | 0 | 14 |
| 4 | general | blend70 | 383 | 93.21% | 8 | 5 | 1 | 13 |
| 4 | general | sparse | 383 | 85.64% | 22 | 16 | 1 | 17 |
| 4 | business | ft | 490 | 97.14% | 9 | 1 | 1 | 4 |
| 4 | business | blend50 | 490 | 95.51% | 5 | 0 | 0 | 17 |
| 4 | business | blend60 | 490 | 95.71% | 4 | 0 | 0 | 17 |
| 4 | business | blend70 | 490 | 96.73% | 6 | 0 | 0 | 10 |
| 4 | business | sparse | 490 | 91.63% | 28 | 1 | 12 | 12 |
| 4 | business2 | ft | 976 | 97.13% | 16 | 1 | 3 | 11 |
| 4 | business2 | blend50 | 976 | 96.11% | 12 | 1 | 2 | 25 |
| 4 | business2 | blend60 | 976 | 96.82% | 12 | 1 | 2 | 18 |
| 4 | business2 | blend70 | 976 | 97.13% | 12 | 0 | 1 | 16 |
| 4 | business2 | sparse | 976 | 93.44% | 29 | 12 | 11 | 23 |
| 4 | japan_procurement | ft | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 4 | japan_procurement | blend50 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 4 | japan_procurement | blend60 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 4 | japan_procurement | blend70 | 92 | 100.00% | 0 | 0 | 0 | 0 |
| 4 | japan_procurement | sparse | 92 | 100.00% | 0 | 0 | 0 | 0 |

## 反復する問題出力

- `wrong`・`unknown`・`other_ng` は **2119出力、235ケース**。うち223ケースは2条件以上で再発し、132ケースは5つ以上のjob×条件で再発。
- critical付きの問題出力は **{critical_outputs}件、31ケース**。

## 解釈上の注意

- 同梱の `ERROR_ANALYSIS.md` は「40ファイル / 17,288行」と明記されているため、全件監査の代わりにはせず、ここではprobability/errorの200ファイル全てを再集計した。
- 固定5集合は反復利用された診断用データ。ここでの成績は記述結果で、D2の事前判定を独立に再現するものでも、未見データでの確認でもない。sealed confirmation set は未使用。
- ラベル、モデル、評価データは変更していない。
