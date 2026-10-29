# 不明になった列の調査：まとめ（2026-10-29 Claude）

集計：`compare.md`（`compare.py`）・`candidates.md`（`candidates.py`）。列ごとの突き合わせは `compare.jsonl`。

## 先生の答え
- **ChatGPT**：329 列中 306 列を答え、正しい 286（93.5%）・**重大 0**・ほかの誤り 20（2026-10-29 23:30 訂正：初めの版は「正解が数字の種類で別の種類と答えた」7 列を重大と数えていた。score_real の重大は答えも数字の種類のときだけ）。「値の形」だけで決めた 42 列は正しい 29 で、値の形だけでは誤りやすい（[x] を印と読むなど）
- **Grok は使わない**：答えた 162 列の正しい割合 35.2%・重大 77（訂正後の数え方）。同じラベルが最大 16 行続き（u0031〜u0039 がすべて id、u0041〜u0047 がすべて amount）、メモも「番号・コード」「金額」の決まり文句で、列を見ずに付けた形。行のずれではない（1〜3 行ずらすと一致は減る）。そのため「2 人一致」（54 列）は手がかりにしない
- 本体の 1 位をそのまま答えにすると 329 列で正しい 170・重大 130。見張り・recheck が止めているのは正しい

## 人なら決められるのに不明になっている形（ChatGPT が正しく決めた列から）
1. **文字化けした £（`｣`、NFKC で `」`）**：`guard.py` は通貨として読むが、`recheck.py` の金額の手がかり・`verifier.py` の値の読み方は `£` しか見ていない。英国の paybill・契約額の列が amount_without_cue・cue_conflict:date で不明になる（27 列・18 表）
2. **列名が URI・URL で、値が `http://…/id/…` の識別子**：OrganisationURI・ServiceTypeURI など 45 列・38 表。見張りが other_class で止めている
3. **ドイツ語・スイスの語**：手がかりの辞書は日本語・英語・ポルトガル語だけ。anzahl・Prozent・quote・Ueberbauungsgrad・CHF・beitrag・jahr・monat・_code・_nr など 37 列
4. **エネルギーの単位**：`_kwh` で終わる列名・filesize（Megabytes）が数量と読めていない（12 列）
5. **英語の金額・率の語の抜け**：Value of New Contract・Contract_value・Paybill・SurplusAmount・IncomeAmount・Paid_fare・…Percent（語の中）・per 1000（13 列）

上の 11 候補を合わせると、不明 329 列のうち 130 列（91 表）が答えになり、正しい 130・重大 0。不明は 11.5% → 7.0% の見込み。**ただしこれは候補を作った列そのものでの数**で、ほかの陣での当てはまりと、今答えている列への悪い影響（新しい手がかりが別の手がかりとぶつかって正しい答えを下げる・誤らせる）はまだ見ていない。

## 候補で拾えない残り
- 率の調査表（「Satisfied」「Got everything I wanted」など、同じ表の列名で率と分かる）15 列、年や週だけの日付（「Week」37、「YearWeekIso」）15 列、表の題名で数量と分かる列（Emp_Wkf_POPD_15+yrs_20xx）12 列など。いずれも列名の語だけでは決まらず、同じ表の列名・表の題名を使う段が要る
- 「verifier:quantity」で下げた「Mandatory Relief %」など：手がかりはあるのに検査役が下げている。検査役の下げ方の見直しは別の話

## 続き（2026-10-29 23:30）
- オーナー指示で、重大・不明の列を ChatGPT に聞き返し、なぜそう判断したかを説明してもらう（`explain/sheets/`、6 枚・236 列）。Claude の推論は先に `explain/claude_reasoning.md` に書いた。規則の下書きは `rules_draft.py`、突き合わせは `explain_compare.py` → `explain/compare.md`

## 原因の切り分け（2026-10-30 0:00。オーナー方針「新しいことをする前に徹底的に原因を突き止める」）
`root_cause.py` → `root_cause.md`、`label_consistency.py` → `label_consistency.md`。上の候補 A〜F・G は**症状を塞ぐ規則**で、原因を直したものではない。原因は次のとおり（不明 329 列、上から順に当てて 1 つ選ぶ）。

| 仕組み | 列 | 確かめ方 | 直す場所 |
|---|---:|---|---|
| M1 recheck の英語の手がかりが `\b` で探すため、下線・大文字つなぎの列名（`__floating_rate__`・`SumOfAmount`・`spur_code`）で当たらない | 28 | 下線と大文字の境目を空白にすると 28 列で正解の手がかりが出る | `recheck.cue_types`（列名を分けてから探す。JS の対も） |
| M2 文字化けの £（｣、NFKC で 」）を guard は読むが、recheck・`verifier.AMOUNT_CUES` は £ だけ | 27 | 値・列名に 」 がある列 | recheck・verifier の通貨の一覧を guard とそろえる（通貨の一覧が 3 か所に分かれている） |
| M3 見張りの日付の判定：年は 19xx・20xx だけ（1680・1812 は年と読まない）、2026-W01・2024-M04・2012_2013・202441・Excel の日付の数がない、列名の語に week・monat・temporal・「日」だけ がない | 19 | `guard.date_shares` が 0（23 列中 22） | `guard._H1_HEADER`・`_H1_VALUE`・日付の値の形 |
| M4 識別子の URI（OrganisationURI）が学習の教材にない。教材の URI はすべてリンク（other で正しい） | 45 | b001〜b014 の URI の列 13 列はすべてリンク | 教材（b060 以降を学習に入れる）か規則 B |
| M5 電力量・エネルギーの付け方が教材で割れている：Claude の裁定が b005・b014 で「kWh は量＝quantity」、b006・b011 で「エネルギー・電力は測定値＝other」。LABEL_GUIDE に電力・エネルギーの語がない | 13 | `adjudication`・`decisions.jsonl` の理由 | LABEL_GUIDE に決まりを書き、教材を付け直す |
| M6 手がかりの辞書が日本語・英語・ポルトガル語だけ（ドイツ語がない） | 26 | 規則 D が当たる列 | recheck の辞書 |
| M7 value・wert の列：同じ表の単位・指標の列の**値**が決め方に渡らない | 8 | | データの経路 |
| M8 値がすべて欠けの記号（[x]・.・NA）。LABEL_GUIDE では S なのに正解は quantity | 7 | | 正解の見直し |
| M9 正解の見直しが要る（u0012・u0171・u0239・u0306・u0192） | 3 | | 正解の見直し |
| M12 縦持ちの表の単位の列（UNIT: %）を、値でない列（STATISTIC・TLIST・jahr）にも当てて手がかりがぶつかる | 6 | `recheck.cue_types(header, unit)` で unit からだけ手がかりが出る | 単位の列は値の列にだけ当てる |
| M13 金額の語 `\bcost` が「Cost Centre」（部署の番号）に当たる | 5 | | recheck の辞書（cost centre を除く） |
| M14 検査役が列名の強い手がかり（%・Amount・Price）を見ずに下げる | 12 | 検査役の段で止まり、列名に別の手がかりがある | 検査役 v2 の下げ方 |
| M10 本体は正しいが、決め方の段が止めた（**まだ原因が分からない**） | 57 | | 調べる |
| M11 本体が誤り（**まだ原因が分からない**） | 73 | | ChatGPT の説明（explain）と教材の突き合わせで調べる |

- 重大の 1 列（b064-0137「Semaine」→ quantity、正解 date）：学習の教材に週の列は 1 列（b014・date）しかなく、フランス語の semaine はない。同じ表に Nombre_Deces（件数）が並ぶ。原因は M3 と同じ「週の列が教材・規則にない」
- 2026-10-29 の候補 A〜F・G は、M1・M2・M6 の症状を列名の語ごとに塞いでいた（例：D5 `_code` は M1、A・A2 は M2）。**原因（M1・M2・M3・M12・M13）を直せば規則を足さずに済む部分がある**ので、規則を足す前に原因の直しを先に試す

## 次（未実施）
1. M10・M11（130 列）の原因を調べる（ChatGPT の説明が届いたら突き合わせる）
2. 原因ごとの直し方を事前記録に書く：M1・M2・M3・M12・M13 はコードの直し、M5・M8・M9 は LABEL_GUIDE と正解の直し、M4・M6 は教材か辞書
3. 決める陣（新しい陣 8 つ）と確かめる陣を分けて、1 つずつ試す
