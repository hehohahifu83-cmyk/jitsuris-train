# G3：金額の手がかりが無いと止まった 106 の調べ（2026-11-15 Claude。読むだけ。直しは作らない・測らない）

元：`research/g3/amount_unknown.json`（L24+G・3 本、最初に止めた段・rho・最後の段つき）。106＝最後まで再確認の amount_without_cue 32＋末尾の通貨確認 74。
2 つの手がかりの辞書は別のもの：再確認の `recheck.cue_types`（列名・単位）と、末尾の `verifier.has_amount_cue`（列名・単位・値 5 つ、`AMOUNT_CUES`）。

## 表ごとの分け方

| 表 | 出力 | 列 | 金額の情報のありか | 分け方 |
|---|---:|---:|---|---|
| t098 年金の給付額 | 30 | 10 | 列名：Income（4 列）、GAINS/RRAG・OAS/SV・GIS/SRG（給付の略語） | (a) 語彙。Income は末尾の辞書には入っているが再確認の辞書に無い（2 つの辞書が食い違う） |
| t022 Farm Cash Receipts | 24 | 8 | 列名は州。同じ表の FarmCashReceiptType の値（Total farm cash receipts…、行ごとに違う）・題名 | (a)＋(b)。「receipts」はどちらの辞書にも無い |
| t062 Investments | 21 | 7 | 列名は州。同じ表の Type の値（標本の 20 行すべて Capital expenditures） | (b)。値の expend は末尾の辞書の語 |
| t012 GDP | 20 | 7 | 列名は州。同じ表の ValueType の値（標本の 20 行すべて Chained (2007) dollars） | (b)。dollar は末尾の辞書の語 |
| t045 Calc_EntitledAmt | 3 | 1 | 列名の「Amt」が語の切れ目なしで付く | (a) 語の切り方 |
| t103 Allocation | 3 | 1 | 列名 | (a) 語彙 |
| t118 Reimbursement | 3 | 1 | 列名（再確認は通り、末尾で止まる） | (a) 語彙 |
| t069 Fuel tax rates | 2 | 2 | 題名の tax rates（セント/L の税率） | 題名だけ。金額か率かが決まらない |

(a) 語彙 41（t098 30・t045 3・t103 3・t118 3・t069 2）＋t022 の 24、(b) ほかの列の値 41（t012 20・t062 21）＋t022 の 24。

## (a) 語彙の反例（使い済みの陣、`research/g3/amount_cue_vocab_scan.py`）

候補の語を列名に含む列の正解（古い 23 陣・決める陣・確かめる陣・E1・E2・F1・G1・G2）：
- **income**：20 列のうち amount は 5。quantity 8（人数・世帯数など）、rate 1、category 1、account 1、other 1、S 2。
- **allocation**：14 列のうち amount は 1。rate 8、category 2、date 1、quantity 1、S 1。
- receipt：3 列、amount 0（quantity・date・unknown）。
- gains/gis/oas：7 列、amount 5、S 2。appropriation：1 列、category。

→ **語を足すだけでは、income・allocation は金額でない列のほうが多い**。辞書に足すと、手がかりのある数として言い切る段が通りやすくなり、重大の誤り（数の種類の取り違え）が増える向きに働く。語彙の直しは、語と値の形（通貨の記号・小数 2 桁）を組み合わせるなどの条件が要る。今は作らない。

## (b) ほかの列の値

- t012・t062 は、指標の列（ValueType・Type）の値が、corpus の標本 20 行で 1 種類だけ（dollars・expenditures）。ただし全体の行数は 378・528 で、標本の外では違う値が混ざりうる（StatCan の形の表では、同じ列に dollars と percent が混ざることがある）。行の対応（row_index）を確かめられない限り、列の種類を決める根拠にはならない。
- t022 は指標の値が行ごとに違う（総額・家畜・作物・直接払い）。どれも金額だが、金額の語は receipts だけ。
- 製品は今、ほかの列の値を手がかりに使っていない。使うなら「その指標の列が表のすべての行で 1 種類で、明示的な通貨の語を含む」などの決まりと、時点・区域・コードの列に漏らさない決まりを、新しい陣で事前に固定して測ることになる。

## 読み

- 金額の不明の大きな塊は 4 表（95 出力）に集まっている。G3 は金額の語で選んだ表なので、こうした「州が列の表」が多く入った。ほかの陣での重みは分からない。
- (a) は使い済みの陣で反例が多く、単純な語の追加は勧めない。(b) は情報が確かにある表もあるが、全行での確認が要り、製品の作りの変更（ほかの列の値を読む）になる。
- どちらも今すぐ直しにする根拠は弱い。Claude の案：直し N と同じく研究の候補として記録し、次の未使用の陣を作るときに、こうした表の割合と、(b) の決まりの事前の形を Codex と決める。
