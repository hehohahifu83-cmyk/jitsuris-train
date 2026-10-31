# D3 の判定：決める陣（`research/d3_eval.py`、探索の扱い）

- 事前記録 `bench/d3_prereg_20261031.md`。正解は列名の同じ列の裁定を入れたもの（`research/labels/consistency_20261031/decisions.jsonl`）。採点 1207 列。
- 辞書：`materials/dictionary/frozen_d3.jsonl`（SHA-256 08a227016f1ad94ccf5e3408626c1e72358540761f70ef26343de9139a6f4a45）。

| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |
|---|---:|---:|---:|---:|---|
| L | 88.21% | 7.29% | 4 | 4.39% | 1065・1068・1061 |
| L+K | 89.09% | 6.43% | 4 | 4.36% | 1081・1076・1069 |
| L+T | 88.01% | 7.07% | 8 | 4.69% | 1059・1064・1064 |
| L+K+T | 88.98% | 6.19% | 8 | 4.61% | 1077・1073・1072 |

## 採る決まり（相手は L）

| 形 | 1. 正しい | 2. 重大 | 3. ほか < 正しい | 4. 90% 区間 | 判定 | 変わった固有の列（良く／悪く、3 本中 2 本以上） |
|---|---|---|---|---|---|---|
| L+K | +0.88 ○ | +0 ○ | -0.03 ○ | +0.41〜+1.38 ○ | **採る** | 8／0 |
| L+T | -0.19 × | +4 × | +0.30 × | -0.70〜+0.28 × | 採らない | 5／8 |
| L+K+T | +0.77 ○ | +4 × | +0.22 ○ | +0.03〜+1.50 ○ | 採らない | 13／8 |

**この回の形：L+K**（K と T の両方を満たし、合わせた形も満たせば L＋K＋T。片方だけなら、その形）

## 辞書が変えた列（L＋K、種子 1）

| id | 列名 | 正解 | L | L＋K |
|---|---|---|---|---|
| b067-0215 | monat | date | unknown | date |
| b067-0229 | stimmbeteiligung | rate | unknown | rate |
| b067-0358 | bruttolastgang_kwh | quantity | unknown | quantity |
| b072-0103 | GEO_CANT | id | unknown | id |
| b072-0285 | quartier_bfs_nr | id | unknown | id |
| b072-0299 | monat | date | unknown | date |
| b072-0307 | quartier_bfs_nr | id | unknown | id |
| b074-0063 | GEO_CANT_RESID | id | unknown | id |
| b074-0065 | GEO_CANT_WORK | id | unknown | id |
| b074-0080 | GEO_CANT_RESID | id | unknown | id |
| b074-0082 | GEO_CANT_WORK | id | category | id |
| b074-0247 | quartier_bfs_nr | id | unknown | id |
| b074-0267 | quartier_bfs_nr | id | unknown | id |
| b078-0165 | stadtkreis_bfs_nr | id | unknown | id |
| b078-0167 | quartier_bfs_nr | id | unknown | id |
| b078-0177 | quartier_bfs_nr | id | unknown | id |
