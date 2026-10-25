# 見張り・recheck の規則の見直し（強化案 V1、2026-10-25 Claude。開発用：b013・b014、C1 種子 1）

- 目的：安全のための規則が、正しい答えをどれだけ壊し、重大をどれだけ防いでいるかを規則ごとに数える
- 採点は other 以外の 2,204 列。製品の形＝見張り → recheck v1 → 検査役 v2（b001〜b012 で学ぶ）→ rho 0.7
- **ここで決めることは C2 の線を b015 で決め直すときの案**。封印セット #3 の C1 の凍結構成は変えない。b013 は rho を決めた陣でもあるので、ここで良く見えた変更は b015 で確かめてから入れる
- 道具：`research/recheck_review.py`（recheck の規則を 1 つずつ外して製品の形を測る）、`research/merge/merge_eval.py score`

## 1. 見張り（予測ファイルの guarded_prediction）
| 理由 | 正しい raw を壊した | 重大を防いだ | ほかの誤りを防いだ |
|---|---:|---:|---:|
| date_value_evidence_low | 47 | 0 | 2 |
| probability_below_threshold | 14 | 3 | 3 |
| numeric_values_not_parseable | 10 | 0 | 3 |
| numeric_top2_too_close | 3 | 4 | 0 |
| other_class | 0 | 0 | 19 |

日付の規則・数が読めない規則を外すと、見張りだけの段は 88.4→91.0% になるが、**製品の形は 85.2→85.3% でほぼ変わらない**（壊した日付は recheck の date_header がもともと 26 列戻しているうえ、残りは後の段で再び不明になる）。→ 見張りより recheck の方が効く

## 2. recheck v1 の言い切りの検査
| 理由 | 正しい言い切りを不明に | 重大を防いだ | 誤りを不明に |
|---|---:|---:|---:|
| low_confidence_no_cue | 69 | 12 | 7 |
| period_header_no_unit | 51 | 5 | 0 |
| amount_without_cue | 36 | 17 | 0 |
| no_value_evidence | 4 | 1 | 0 |
| ほか（cue_conflict・amount_precision・money_band・rate_without_cue） | 9 | 0 | 0 |

## 3. 規則を 1 つずつ外した製品の形（合格の線：重大 ≤ 0.2%＝4 列、不明 ≤ 10%＝220 列）
| 外した規則 | 正解率 | 不明 | 重大 | 線 |
|---|---:|---:|---:|---|
| なし（今の形） | 85.2% | 228（10.3%） | 2 | 不明が線の外 |
| **low_confidence_no_cue** | **86.0%** | **205（9.3%）** | **3** | **内側** |
| period_header_no_unit | 87.5% | 172（7.8%） | 7 | 重大が外 |
| amount_without_cue | 86.0% | 207（9.4%） | 6 | 重大が外 |
| period_header_no_unit ＋ low_confidence_no_cue | 88.3% | 149（6.8%） | 8 | 重大が外 |

- period_header_no_unit が防いだ重大 5 は、どれも単位のない年度の列で数量と金額を取り違えたもの（値だけでは見分けられない）。狭める規則は見つからなかった → 残す
- **案：C2 の製品の形では low_confidence_no_cue を外す**（+0.8 ポイント、不明 −1.0 ポイント、重大 +1）。b015 で、外す前後の両方を測ってから決める
- 本当の伸びしろ：重大を出さずに period_header・amount_without_cue の列を言い切れる手段（表の題名・単位・同じ表の列の値＝強化案 B3、組ごとの 2 択の検査役＝V4）

## 4. ラベルの掃除（commit bc3ce81）のあとで測り直した（2026-10-25 23:59 Claude）
採点 2,196 列（掃除で unknown にした列が抜けた）。同じ道具 `research/recheck_review.py`
| 外した規則 | 正解率 | 不明 | 重大 |
|---|---:|---:|---:|
| なし（今の形） | 85.2% | 223（10.2%） | 3 |
| **period_header_no_unit** | **87.6%** | **172（7.8%）** | **3** |
| low_confidence_no_cue | 86.2% | 195（8.9%） | 4 |
| amount_without_cue | 86.0% | 204（9.3%） | 6 |
（2 つ同時に外す形は時間切れで測れなかった）

- **前回 period_header_no_unit が防いだ重大 5 は、掃除で unknown にした年度の列そのもの**（正解が決められない列）だった。掃除のあとは、この規則は重大を 1 つも防がず、正解 2.4 ポイント・不明 51 列を払っている
- **案を改める：C2 の製品の形では period_header_no_unit を外す**（重大 3 のまま、正解 +2.4、不明 10.2→7.8%）。low_confidence_no_cue は重大 +1 なので次点。b015 で両方の前後を測ってから決め、b016 で確かめる
