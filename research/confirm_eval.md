# 確かめる陣の 1 回だけの測り（`research/confirm_eval.py`）

- 事前記録 `bench/confirm_prereg_20261031.md`。採点 1247 列。正解は列名の同じ列の裁定を入れたもの。辞書 SHA-256 08a227016f1ad94ccf5e3408626c1e72358540761f70ef26343de9139a6f4a45。

| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |
|---|---:|---:|---:|---:|---|
| A | 85.03% | 8.45% | 14 | 6.15% | 1069・1056・1056 |
| L | 85.38% | 8.42% | 16 | 5.77% | 1069・1060・1065 |
| L+K | 85.67% | 8.02% | 19 | 5.80% | 1072・1065・1068 |

## 決まり 1〜4

| 比べ | 1. 正しい | 2. 重大 | 3. ほか < 正しい | 4. 90% 区間 | 判定 | 良く／悪く（固有の列） |
|---|---|---|---|---|---|---|
| L+K 対 A（主な問い：L＋K は A より良いか） | +0.64 ○ | +5 × | -0.35 ○ | +0.13〜+1.15 ○ | 確かめられなかった | 9／3 |
| L 対 A（D2 の付け直しの一般化） | +0.35 × | +2 × | -0.37 ○ | -0.10〜+0.81 × | 確かめられなかった | 6／3 |
| L+K 対 L（D3 の辞書の一般化） | +0.29 × | +3 × | +0.03 ○ | +0.05〜+0.54 ○ | 確かめられなかった | 4／0 |

## 辞書が変えた列（L と L＋K、3 本すべて）

| 本 | id | 列名 | 正解 | L | L＋K |
|---|---|---|---|---|---|
| 1 | b068-0007 | Less than $5,000, Number | quantity | unknown | amount |
| 1 | b069-0017 | STATISTIC CODE | id | unknown | id |
| 1 | b070-0005 | 幼稚園(円） | amount | unknown | amount |
| 1 | b074-0179 | geschosse_anzahl | quantity | unknown | quantity |
| 2 | b068-0007 | Less than $5,000, Number | quantity | unknown | amount |
| 2 | b069-0017 | STATISTIC CODE | id | unknown | id |
| 2 | b070-0005 | 幼稚園(円） | amount | unknown | amount |
| 2 | b072-0204 | geschosse_anzahl | quantity | unknown | quantity |
| 2 | b074-0109 | EDID | id | unknown | id |
| 2 | b074-0179 | geschosse_anzahl | quantity | unknown | quantity |
| 3 | b068-0007 | Less than $5,000, Number | quantity | unknown | amount |
| 3 | b069-0017 | STATISTIC CODE | id | unknown | id |
| 3 | b070-0005 | 幼稚園(円） | amount | unknown | amount |
| 3 | b074-0109 | EDID | id | unknown | id |
| 3 | b074-0179 | geschosse_anzahl | quantity | unknown | quantity |
| 3 | b081-0030 | Percentage paid within 30 working d | org | org | rate |
