# 単位の列の見出しを広げる：事前記録（2026-10-29 Claude）

- オーナー：「続けて」（2026-10-29。rho の決め直しのあと）。
- きっかけ：新しい公開元の陣（b015〜b017・b060〜b065）で、件数（quantity）↔金額（amount）の取り違えを 28 列集めた。b063 の「Wert」の表には単位の列（Einheit：Tonnen (t)・Personen）があるのに、本体に渡す「同じ表の単位列の値」が空だった。
- 原因：単位の列を見つける見出しの決まり（`encoder_context._UNIT_HEADER`）が英語・日本語（unit・units・uom・unit of measure・measurement unit・単位・単位名・amount units）だけ。ドイツ語の einheit、フランス語の unité、統計局の UNIT_MEAS・parameter_unit・data_value_unit などを見落とす。教材庫にも einheit 17 列・data_value_unit 7 列・parameter_unit 5 列などがあり、学習でも単位が届いていなかった。
- **この記録は、試しの予測の結果を見る前に固定する**。封印セット・blind_set*・セット 3・5・7・b018 は使わない。

## 広げた決まり（試しの中だけで使う。採るまで本番のコードは変えない）
`unit|units|uom|unit of measure|unit_of_measure|measurement unit（後ろに何か付いてもよい）|unit_meas(ure)|data_value_unit|parameter_unit|obs_unit|obsunit_uniteobs|einheit(_kurz|_lang)|masseinheit|maßeinheit|unité|unite|unité de mesure|unidad (de medida)|unidade de medida|単位|単位名|amount units`（全体一致、大文字小文字を区別しない）。予算の単位（unidade_orcamentaria）のような「組織の単位」は入れない。

## 試し（学習なし・CPU）
- 単位の例が変わる表の列だけ（b017 9 列・b063 98 列・b064 76 列＝183 列）を、広げた決まりで作った単位の例に替えた set にし、C2 種子 1 で 1 回予測する（`materials/pool/work/unitfix1029/`）。
- 比べる：同じ 183 列（とその 3 陣の全体）で、今の予測（単位なし）と新しい予測（単位あり）を、製品の形（recheck v1 → 検査役 v2 → ρ=0.8）で採点する。

## 採否（変えない）
- 183 列のうち採点できる列で、**重大が増えず、かつ正解率が下がらない（−0.5 ポイント以内）**なら採る。単位を本体に渡すのは今の仕組みのもともとのねらいなので、悪くならなければ直す側を採る。
- 採ったら：`encoder_context._UNIT_HEADER` を広げる（予測の set づくり `materials/corpus_to_set.py` と学習 `encoder_exp.py` の両方に効く）。学習し直し（C3 の次の候補）は別の事前記録とオーナー許可で。
- 記録だけ：3 陣全体の数字、変わった列の数と向き（正→誤・誤→正・不明→言い切り・言い切り→不明）。

## 結果
（ここに書く。上の規則は変えない）

### 結果（`research/unit_eval.py`、C2 種子 1・製品の形 ρ=0.8）

| 範囲 | 単位 | 結果 | 不明 | 重大 |
|---|---|---|---|---:|
| 替えた列（183） | 今（単位なし） | 正 84.6%・誤 13・不明 11・**重大 0**（採点 156） | 7.1% | 0.00% |
| 替えた列（183） | 広げた決まり（単位あり） | 正 84.6%・誤 11・不明 13・**重大 0**（採点 156） | 8.3% | 0.00% |
| 3 陣全体 | 今（単位なし） | 正 82.6%・誤 83・不明 147・**重大 1**（採点 1324） | 11.1% | 0.08% |
| 3 陣全体 | 広げた決まり（単位あり） | 正 82.6%・誤 81・不明 149・**重大 1**（採点 1324） | 11.3% | 0.08% |

- 変わった列の向き：{'言い切り→不明': 3}
- 判定（替えた列）：重大 0 → 0、正解率 84.6% → 84.6% → **採る**

### 採ったあと（2026-10-29 Claude）
- `encoder_context._UNIT_HEADER` を上の広げた決まりにした。試験 `tests/test_encoder_context.py`（UnitHeaderLanguagesTests：新しい見出しは見つかる・unidade_orcamentaria・unit count・Business Unit などは見つけない）。
- 効くところ：これからの予測の set づくり（`materials/corpus_to_set.py`）と学習（`encoder_exp.py` の教材庫の単位の例。einheit 17 列など）。今までの陣の set.json・予測は作り直していない。
- 効きは小さい（替えた 156 列で誤り 2 → 不明）。本体は英語の単位の例でしか学んでいないので、学習し直すとドイツ語の単位も手がかりにできる見込み（未確認。次の学習の候補）。
