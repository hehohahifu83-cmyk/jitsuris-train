# 不明・重大の原因の切り分け（`research/unknown/root_cause.py`）

- 対象：新しい陣 8 つの不明 329 列。本体 C2 の学習の教材は b001〜b014。「同じ形」は `rules_draft.py` の規則が当たる列

## 原因の大分け

| 原因 | 列 |
|---|---:|
| 決め方の段が止めた（本体は正しい） | 170 |
| 本体が誤り・形の規則なし | 93 |
| 本体が誤り・同じ形が教材にない | 58 |
| 本体が誤り・同じ形は教材にあった | 8 |

## 仕組みごと（上から順に当てて 1 つ選ぶ）

| 仕組み | 列 | うち本体は正しい | 正解の種類 |
|---|---:|---:|---|
| M1 英語の手がかりが下線・大文字つなぎの列名で当たらない（recheck の語の境目） | 28 | 24 | rate 11, id 9, date 5, amount 3 |
| M10 本体は正しいが、決め方の段が止めた（ほかの理由） | 57 | 57 | quantity 18, amount 17, rate 9, category 6 |
| M11 本体が誤り（ほかの理由） | 73 | 0 | quantity 29, category 20, id 9, rate 6 |
| M12 表全体の単位の列（UNIT: %）を、値でない列（コード・年）にも当てて手がかりがぶつかる | 6 | 6 | id 4, date 2 |
| M13 金額の語（cost）が部署の番号の列名（Cost Centre）に当たって手がかりがぶつかる | 5 | 5 | id 5 |
| M14 検査役が列名の強い手がかりを見ずに下げる | 12 | 7 | quantity 5, amount 4, rate 2, id 1 |
| M15 本体の入力は先頭 5 個の値だけで、先頭が欠けの記号ばかり（後ろの行に数がある） | 6 | 1 | quantity 6 |
| M2 文字化けの £（｣）を recheck・通貨の手がかりが読めない | 27 | 23 | amount 27 |
| M3 見張りの日付の値の形・列名の語が足りない（1900 年より前の年・週・2024-M04・Excel の日付の数など） | 19 | 19 | date 19 |
| M4 教材にない形（識別子の URI。教材の URI はリンクだけ＝other） | 45 | 0 | id 45 |
| M5 教材の付け方の食い違い（電力量・エネルギー：b005・b014 は quantity、b006・b007・b011 は other） | 13 | 5 | quantity 13 |
| M6 手がかりの辞書にドイツ語がない | 26 | 19 | quantity 11, rate 9, amount 3, id 2 |
| M7 汎用の値の列で、単位・指標の列の値が決め方に渡っていない | 8 | 2 | quantity 5, amount 3 |
| M8 値がすべて欠けの記号（[x]・.・NA） | 1 | 1 | quantity 1 |
| M9 正解の見直しが要る | 3 | 1 | category 1, account 1, org 1 |

## 本体は正しいのに止めた列：段と理由

| 段 | 理由 | 列 | 正解の種類 |
|---|---|---:|---|
| recheck | amount_without_cue | 28 | amount 28 |
| 見張り（本体の段） | date_value_evidence_low | 23 | date 23 |
| recheck | rate_without_cue | 22 | rate 22 |
| recheck | low_confidence_no_cue | 19 | quantity 11, id 8 |
| recheck | no_value_evidence | 16 | quantity 13, amount 2, rate 1 |
| 見張り（本体の段） | probability_below_threshold | 13 | category 6, quantity 4, account 1, org 1, text 1 |
| 検査役 | verifier:quantity | 13 | amount 9, id 2, rate 2 |
| recheck | cue_conflict:amount | 9 | id 7, date 2 |
| 見張り（本体の段） | numeric_values_not_parseable | 7 | quantity 5, amount 1, rate 1 |
| recheck | cue_conflict:date | 6 | amount 6 |
| recheck | cue_conflict:rate | 4 | id 2, date 2 |
| 検査役 | verifier:id | 4 | amount 4 |
| 通貨の手がかり | amount_without_cue | 2 | amount 2 |
| 検査役 | verifier:amount | 1 | id 1 |
| recheck | cue_conflict:quantity | 1 | id 1 |
| 検査役 | recheck:cue_id | 1 | quantity 1 |
| 検査役 | verifier:date | 1 | id 1 |

## 本体が誤った列：本体の 1 位と正解

| 本体の 1 位 | 正解 | 列 |
|---|---|---:|
| other | id | 53 |
| amount | quantity | 27 |
| other | quantity | 21 |
| other | rate | 11 |
| other | category | 6 |
| id | category | 6 |
| rate | quantity | 5 |
| other | amount | 5 |
| quantity | category | 4 |
| quantity | id | 4 |
| account | category | 2 |
| text | category | 1 |
| other | address | 1 |
| text | product | 1 |
| account | org | 1 |

## 規則の形ごと：不明の列と、学習の教材（b001〜b014）での同じ形

| 規則 | 種類 | 不明の列 | うち本体は正しい | 教材の同じ形（付いていた種類） |
|---|---|---:|---:|---|
| A | amount | 7 | 3 | なし |
| A2 | amount | 18 | 18 | なし |
| B | id | 45 | 0 | other 1 |
| C | quantity | 12 | 5 | other 8, quantity 3 |
| D1 | quantity | 11 | 9 | address 2 |
| D2 | rate | 9 | 4 | address 2, quantity 2, category 1 |
| D3 | amount | 3 | 3 | なし |
| D4 | date | 7 | 7 | category 1 |
| D5 | id | 7 | 7 | id 209, address 13, category 3 |
| E | amount | 7 | 7 | amount 8 |
| F | rate | 4 | 4 | rate 14, other 1 |
| G2 | date | 7 | 7 | date 15 |
| G3 | rate | 6 | 4 | なし |
| G5 | id | 3 | 2 | id 925, S 2, text 1, date 1, category 1, address 1, other 1 |
