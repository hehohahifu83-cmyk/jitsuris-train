# G3：数の列が不明になる段（L24+G、3 本の合計。`research/g3/amount_unknown.py`、読むだけ）

## 正解 amount（90 列 × 3 本）

| 段 | 数 | 割合 |
|---|---:|---:|
| 答えた | 117 | 43.3% |
| 再確認が止めた（amount_without_cue） | 100 | 37.0% |
| 再確認が止めた（amount_precision） | 18 | 6.7% |
| 本体・見張りで不明（理由なし） | 12 | 4.4% |
| 再確認が止めた（rate_without_cue） | 9 | 3.3% |
| 検査役が止めた | 6 | 2.2% |
| 再確認が止めた（low_confidence_no_cue） | 5 | 1.9% |
| 再確認が止めた（理由なし） | 3 | 1.1% |

## 正解 quantity（94 列 × 3 本）

| 段 | 数 | 割合 |
|---|---:|---:|
| 答えた | 224 | 79.4% |
| 再確認が止めた（low_confidence_no_cue） | 38 | 13.5% |
| 本体・見張りで不明（理由なし） | 16 | 5.7% |
| 検査役が止めた | 3 | 1.1% |
| 再確認が止めた（rate_without_cue） | 1 | 0.4% |

## 正解 rate（12 列 × 3 本）

| 段 | 数 | 割合 |
|---|---:|---:|
| 本体・見張りで不明（理由なし） | 18 | 50.0% |
| 答えた | 14 | 38.9% |
| 再確認が止めた（low_confidence_no_cue） | 4 | 11.1% |

## 正解 amount で不明になった列（本 1）

| id | 表 | 列名 | 単位 | 値（5 つまで） | 本体 | 理由 |
|---|---|---|---|---|---|---|
| g3-0063 | t010 | 22-23 Fiscal Funding |  | $50,000 / $70,000 / $70,000 / $74,374 / $70,000 | amount | amount_precision |
| g3-0073 | t012 | Alberta |  | 12002000000 / 64839000000 / 11865000000 / 11429000000 / 24371000000 | amount | amount_without_cue |
| g3-0074 | t012 | BritishColumbia |  | 12330000000 / 6682000000 / 3787000000 / 11383000000 / 4421000000 | amount | amount_without_cue |
| g3-0075 | t012 | Manitoba |  | 645000000 / 2457000000 / 1154000000 / 748000000 / 346000000 | amount | amount_without_cue |
| g3-0076 | t012 | NewBrunswick |  | 1384000000 / 1675000000 / 840000000 / 589000000 / 861000000 | amount | amount_without_cue |
| g3-0077 | t012 | NewfoundlandAndLabrador |  | 103000000 / 399000000 / 395000000 / 2678000000 / 1411000000 | amount | amount_without_cue |
| g3-0078 | t012 | NovaScotia |  | 745000000 / 526000000 / 654000000 / 1414000000 / 517000000 | amount | amount_without_cue |
| g3-0079 | t012 | Ontario |  | 38216000000 / 74697000000 / 8675000000 / 32142000000 / 38200000000 | amount | amount_without_cue |
| g3-0146 | t022 | Alberta |  | 2858359000 / 822429000 / 1633196000 / 463252000 / 1104378000 | amount | amount_without_cue |
| g3-0147 | t022 | BritishColumbia |  | 337127000 / 141835000 / 248352000 / 123271000 / 161259000 | amount | amount_without_cue |
| g3-0148 | t022 | Canada |  | 11001979000 / 869559000 / 4922669000 / 507425000 / 2740017000 | amount | amount_without_cue |
| g3-0149 | t022 | Manitoba |  | 194840000 / 55076000 / 183010000 / 4136000 / 51587000 | amount | amount_without_cue |
| g3-0150 | t022 | NewBrunswick |  | 223000 / 115802000 / 11524000 / 1948000 / 2091000 | amount | amount_without_cue |
| g3-0151 | t022 | NewfoundlandAndLabrador |  | 755000 / 0 / 15271000 / 1000 / 25787000 | amount | amount_without_cue |
| g3-0152 | t022 | NovaScotia |  | 15564000 / 58799000 / 82961000 / 548000 / 1425000 | amount | amount_without_cue |
| g3-0153 | t022 | Ontario |  | 404589000 / 2628071000 / 1149243000 / 1167745000 / 391933000 | amount | amount_without_cue |
| g3-0261 | t041 | Approved Funding |  | $25,428 / $184,180 / $233,256 / $297,155 / $168,286 | amount | amount_precision |
| g3-0298 | t045 | Calc_EntitledAmt |  | 940000 / 6000 / 426000 / 157000 / 334000 | amount | amount_without_cue |
| g3-0319 | t049 | Amount |  | 28431.21 / 60048 / 350224.65 / 39704.18 / 654554211.55 | amount | verifier:id |
| g3-0332 | t051 | Pump Price/Prix à la pompe |  | 69.2 / 111.5 / 50 / 78.9 / 54.5 | amount | verifier:rate |
| g3-0334 | t051 | Federal Excise Tax/Taxe d'acci |  | 10 / 6.6 / 10 / 10 / 10 | unknown | None |
| g3-0335 | t051 | Federal Carbon Tax/Taxe carbon |  | 4.4 / 4.4 / 4.4 / 4.4 / 4.4 | rate | rate_without_cue |
| g3-0336 | t051 | Ontario Tax/Taxe de l'Ontario |  | 14.7 / 14.7 / 14.7 / 14.7 / 14.7 | unknown | None |
| g3-0337 | t051 | GST/HST / TPS/TVH |  | 14.6 / 15.5 / 12.8 / 3.8 / 3.6 | unknown | None |
| g3-0338 | t051 | Wholesale Margin/Marge de gros |  | 7.1 / 10.2 / 6.5 / 15 / 14.3 | unknown | None |
| g3-0400 | t062 | Alberta |  | 134200000 / 1560900000 / 334600000 / 1376300000 / 280400000 | amount | amount_without_cue |
| g3-0401 | t062 | BritishColumbia |  | 70400000 / 14400000 / 1329500000 / 391900000 / 348600000 | amount | amount_without_cue |
| g3-0402 | t062 | Canada |  | 31783600000 / 12308300000 / 1180000000 / 703300000 / 4181800000 | amount | amount_without_cue |
| g3-0403 | t062 | Manitoba |  | 180000000 / 581000000 / 96500000 / 241400000 / 6698900000 | amount | amount_without_cue |
| g3-0404 | t062 | NewBrunswick |  | 632200000 / 1463400000 / 525100000 / 6191800000 / 59100000 | amount | amount_without_cue |
| g3-0405 | t062 | NewfoundlandAndLabrador |  | 7300000 / 31800000 / 138800000 / 1038300000 / 25300000 | amount | amount_without_cue |
| g3-0406 | t062 | NovaScotia |  | 329800000 / 47700000 / 204200000 / 29000000 / 31300000 | amount | amount_without_cue |
| g3-0440 | t069 | Clear Fuel Regular (Carburant  |  | 9.9 / 10.9 / 7.8 / 12.6 / 9 | amount | amount_without_cue |
| g3-0441 | t069 | Clear Fuel Railway (Carburant  |  | 2.6 / 2.9 / 2.5 / 4.5 / 2.4 | amount | amount_without_cue |
| g3-0480 | t076 | Local Appropriation |  | 41100 / 147233988.24 / 663216.16324 / 2600 / 250222 | amount | amount_precision |
| g3-0481 | t076 | Total Local Appropriation |  | 159417.82999 / 13764 / 609.28 / 313998.83 / 168739 | amount | amount_precision |
| g3-0482 | t076 | Provincial Library Operating G |  | 41658 / 47824 / 21606 / 16650 / 25225 | amount | low_confidence_no_cue |
| g3-0485 | t076 | Total cash receipts |  | 41636.120000 / 513344.64 / 54658.590000 / 34467.040000 / 23848.04 | amount | amount_precision |
| g3-0605 | t098 | Annual Income Private (min.) / |  | 9,120.00 / 16,200.00 / 7,680.00 / 456 / 3,888.00 | amount | amount_without_cue |
| g3-0606 | t098 | Annual Income Private (max.) / |  | 16,079.99 / 8,287.99 / 8,663.99 / 9,343.99 / 3,719.99 | amount | amount_without_cue |
| g3-0607 | t098 | GAINS / RRAG |  | 0 / 0 / 0 / 0 / 0 | amount | amount_without_cue |
| g3-0608 | t098 | Total OAS/GIS /SV/SRG total |  | 1,387.81 / 1,432.81 / 1,738.81 / 1,079.77 / 1,718.81 | amount | amount_without_cue |
| g3-0609 | t098 | OAS / SV |  | 713.34 / 713.34 / 713.34 / 713.34 / 713.34 | amount | amount_without_cue |
| g3-0610 | t098 | GIS / SRG |  | 133.43 / 361.43 / 745.47 / 299.43 / 422.43 | amount | amount_without_cue |
| g3-0611 | t098 | Total Monthly Income (min.) /R |  | 2,243.77 / 1,861.81 / 2,082.77 / 2,244.77 / 1,866.81 | amount | amount_without_cue |
| g3-0612 | t098 | Total Monthly Income (max.) /R |  | 2,242.76 / 1,863.80 / 1,964.80 / 1,909.80 / 1,894.80 | amount | amount_without_cue |
| g3-0613 | t098 | Monthly Income Private (min.)  |  | 222 / 32 / 480 / 976 / 1,650.00 | amount | amount_without_cue |
| g3-0614 | t098 | Monthly Income Private (max.)  |  | 411.99 / 329.99 / 766.66 / 1,203.99 / 230.66 | amount | amount_without_cue |
| g3-0640 | t103 | Allocation |  | 30,000 / 3,720,000 / 150,000 / 30,000 / 90,000 | amount | amount_without_cue |
| g3-0728 | t118 | Reimbursement |  | 87770946.68 / 16891452.79 / 98188505.99 / 84160791.9 / 100239705.9 | amount | None |
| g3-0743 | t120 | Coordination of Benefits(4) |  | 1566409.25 / 21098195 / 4302.78 / 464108.79999 / 598108.30000 | amount | amount_precision |

## 読み（2026-11-14 Claude。原因の調べ。直しはまだ作らない・測らない）
- 正解 amount の不明 153（3 本）のうち **再確認の amount_without_cue が 100**。そのうち **92 が 4 表**（t098 年金の給付額・t022 Farm Cash Receipts・t062 Investments・t012 GDP）。どれも**列名が州の名前**（Alberta・Ontario…）で、金額の手がかりが列名・単位・同じ表の列名のどこにも無い。本体は amount と答えているが、再確認が「手がかり無しの金額」として止めた。題名も「Investments」「Gross Domestic Product」などで、金額の語は弱い。
  - これは**決めたとおりの動き**（手がかり無しで数を金額と言い切らない安全の決まり、`bench/recheck_v1.md`）。止めずに通すと、手がかりの無い数の列を金額と言い切る重大の誤りが増えうる。表 4 つに集まっているので、直しの効き目も表 4 つ次第になる。
- **amount_precision 18（6 列×3 本）は誤りの道筋**：
  1. `$74,374`・`$25,428` のような **3 桁区切り（,）を小数として数えている**（2 列。値に $ があっても、この止めは通貨の記号を見ない）。
  2. `159417.82999999999`・`41636.120000000003` のような **表計算の小数の誤差**（実際は 2 桁）を、お金の桁を超える小数としている（3 列。`663216.16324774758` のような本当に細かい値は残る）。
- そのほか：t051（ガソリン価格の内訳、セント・リットル当たり）は本体の不明・率との迷い、検査役の止め 6（Amount を id など）。
- 数量 quantity は 79% 答えている（不明はほとんど low_confidence_no_cue）。率 rate は 12 列中、本体の不明が半分。
