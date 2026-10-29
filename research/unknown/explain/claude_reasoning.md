# 重大・不明になった列：Claude の推論（`research/unknown/claude_reasoning.py`）

ChatGPT の説明（`explain/answers_chatgpt/`）を読む前に書いた。Claude は正解・今の仕組みの段を見ている。規則は `rules_draft.py`（まだ製品に入れていない）。

## 規則の下書きを当てた結果（決める陣＝新しい陣 8 つ。参考値）

| 列の組 | 列 | 正しい | 重大 | 不明のまま | ほかの誤り |
|---|---:|---:|---:|---:|---:|
| 今の仕組みが誤った列（重大 1・数字の列を数字以外と言い切った 36） | 37 | 14 | 0 | 3 | 20 |
| 不明の列のうち A〜F で拾えない 199 列 | 199 | 16 | 0 | 183 | 0 |

- 今の仕組みが誤った 37 列：今は正しい 0。規則の下書きで正しくなる 14、不明に下がる 3（言い切りの誤りが不明になるのは安全側）

## 規則ごと

| 規則 | 種類 | 中身 | 当たった列 | 正しい | 重大 |
|---|---|---|---:|---:|---:|
| D5 | id | ドイツ語の番号：…_code・…_nr・laufnummer | 1 | 1 | 0 |
| G2 | date | 週・四半期・期間の列名（week・woche・semaine・kw・yearweek・quarter・quartal・time_period・temporal・fiscal_year）で、値が週の番号・年と週・年と四半期 | 8 | 8 | 0 |
| G3 | rate | 満足度・賛否の段階の列名で、値に小数があり 0〜100 | 6 | 6 | 0 |
| G5 | id | 列名が「Id …」「… Id」「… Nr」「nummer」「Signatur」「reference」で、値が数字・コード | 7 | 7 | 0 |
| G6 | quantity | 列名が「No. …」（No. ill・No. laboratory confirmed）で値が整数 | 1 | 1 | 0 |
| G7 | date | 時刻の幅（09.00-11.45）が値の 8 割以上で、列名に uhrzeit・zeit・time | 2 | 2 | 0 |
| G8 | id／不明 | 名前の種類なのに値が数字だけ → 列名に番号の語があれば id、なければ不明（言い切った答えに当てる） | 3 | 0 | 0 |
| G9 | quantity | 列名に decimals・nachkommastellen（小数の桁数）で値が整数 | 5 | 5 | 0 |

## 規則にしない・別の段が要るもの（推論から）

- **G1 欠けの記号**：[x]・[z]・[c]（英国統計）・「.」（CSO）・NA・nil は値の形を読む前に外す。外して値が残らない列は S（今の正解は quantity が付いているので正解を見直す）。ChatGPT は [x] を印と読んで category にした
- **G4 横持ちの表**：「Degree of severity 0〜3」「Arrest/Detention > …」「EW_…_SA」のように、同じ形の列名が並んで値が整数なら、それぞれ区分ごとの数（quantity）。列名の語だけでは決まらず、表をまるごと見る段が要る（C3 計画の「表をまるごと読む本体」・C3c）
- **G10 言い切った答えと列名の強い手がかりの食い違い**：「GOR CODE」を category と言い切った。今は見張りで言い切った列は recheck を通らない。言い切った答えにも code$・_nr・No. の手がかりとの食い違いを調べる段を足す
- **G11 同じ表の通貨の列**：同じ表の列名に waehrung・currency・devise があれば、その表の金額らしい列の通貨の手がかりにする
- **G12 汎用の値の列**：value・wert・VALUE・OBS_VALUE は、同じ表の einheit・unit・metrik・valueCategory の**値**が渡れば決まる。今はシートにも決め方にも単位の列の名前しか渡っていない。データの経路を直す（決め方の規則ではない）
- **正解を見直す**：u0017・u0103 など値がすべて欠けの列（LABEL_GUIDE では S）、u0171（崩れた白書の表）、並び順（kategorie_sortierung＝id）と順位（Rank＝category）の食い違い、u0239・u0306（組織名に account／org）。正解の側を直すと不明・誤りの数が変わる

## 列ごと

| 番号 | 見出し | 正解 | 今の仕組み（理由） | ChatGPT 前回 | Claude | 規則 | 推論 |
|---|---|---|---|---|---|---|---|
| x0001 | GEO_CANT | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「GEO_CANT」で 1,1,2＝州の番号。GEO_ の列名で値が整数→id だが、GEO_ は地名の列にもなる。規則にしない |
| x0002 | kategorie_sortierung | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | b063-0300 と同じ（正解を見直す） |
| x0003 | Id Of Disease Category | id | 今の仕組みは category と言い切った（本体 category） | — | id | G5 | 「Id Of Disease Category」。G5 で id |
| x0004 | parameter_decimals | quantity | 今の仕組みは category と言い切った（本体 category） | — | quantity | G9 | G9 |
| x0005 | sitzung_titel | id | 今の仕組みは text と言い切った（本体 text） | — | text |  | 「sitzung_titel」で「61. Sitzung」＝会の回の名前。正解は id だが、題名（titel）の列で文字の値なので text とも読める（正解を見直す） |
| x0006 | abkuerzung | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「abkuerzung」（略号）で UPI・ZEMIS＝システムの略号。id か category かは境目。規則にしない |
| x0007 | parameter_decimals | quantity | 今の仕組みは category と言い切った（本体 category） | — | quantity | G9 | G9 |
| x0008 | parameter_decimals | quantity | 今の仕組みは category と言い切った（本体 category） | — | quantity | G9 | G9 |
| x0009 | Degree of severity 2 | quantity | 今の仕組みは category と言い切った（本体 category） | — | category |  | b063-0143 と同じ（G4） |
| x0010 | Extending Agency | id | 今の仕組みは org と言い切った（本体 org） | — | unknown | G8 | 「Extending Agency」で 3,3,3＝機関のコード。本体は org。名前の種類なのに値が数字だけ→G8 で不明 |
| x0011 | kategorie_sortierung | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「kategorie_sortierung」で 1,1,2＝並べる順の番号。正解は id だが、順位（Rank）の列は category と付いている（u Rank）。並び順・順位の正解をそろえる必要がある（正解を見直す） |
| x0012 | No. laboratory confirmed | quantity | 今の仕組みは category と言い切った（本体 category） | — | quantity | G6 | 「No. laboratory confirmed」＝確認された件数。英語の「No. X」は number of X。recheck の \bno\.? of\b は of が要るので当たらない。G6 で quantity |
| x0013 | nfr | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「nfr」で 5A＝排出の分類コード（NFR）。略語は辞書でしか決まらない。規則にしない |
| x0014 | Question | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「Question」で Q1・Q10＝設問の番号。id か category かは境目（正解は id）。規則にしない |
| x0015 | verteilzone | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「verteilzone」で 261_LZ＝区域のコード。列名からは区分（category）とも読める。規則にしない |
| x0016 | Arrest/Detention > Assault with Weapon | quantity | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「Arrest/Detention > Assault with Weapon」で 0 だけ。「区分 > 区分」の列名が並ぶ横持ちの表で、値は件数。G4 |
| x0017 | Degree of severity 1 | quantity | 今の仕組みは category と言い切った（本体 category） | — | category |  | b063-0143 と同じ（G4） |
| x0018 | sessionssitzung_uhrzeit | date | 今の仕組みは text と言い切った（本体 text） | — | date | G7 | 「sessionssitzung_uhrzeit」。G7 で date |
| x0019 | Signatur | id | 今の仕組みは org と言い切った（本体 org） | — | id | G5 | 「Signatur」で GS-GUGE-BIEDERMANN-A-9＝所蔵の請求記号。本体は org（人名を含むため）。G5（^signatur$）で id |
| x0020 | No. | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「No.」だけで 1,2,3… と続く整数＝行の番号。本体は category。G6b で id |
| x0021 | verantwortlichkeit_abkuerzung | id | 今の仕組みは org と言い切った（本体 org） | — | org |  | 「verantwortlichkeit_abkuerzung」で KTTGWH・BAFU＝担当の役所の略号。本体は org。略号は org とも id とも読める。正解は id（正解を見直す） |
| x0022 | listed_building | id | 今の仕組みは address と言い切った（本体 address） | — | unknown | G8 | 「listed_building」で 1072858 など 7 桁の整数＝登録番号。本体は address。名前の種類なのに値が数字だけ→G8 で不明（列名に番号の語がないので id にはしない） |
| x0023 | parameter_decimals | quantity | 今の仕組みは category と言い切った（本体 category） | — | quantity | G9 | G9 |
| x0024 | Arrest/Detention > Child Sex | quantity | 今の仕組みは category と言い切った（本体 category） | — | category |  | b065-0212 と同じ（G4） |
| x0025 | Neither satisfied or dissatisfied | quantity | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「Neither satisfied or dissatisfied」で 7,4,5,3 の整数＝回答の人数。同じ段階の列名でも、小数なら率（u0005 Satisfied 35.3）・整数なら人数。G3 は小数のときだけ rate にし、整数は決めない |
| x0026 | Degree of severity 3 | quantity | 今の仕組みは category と言い切った（本体 category） | — | category |  | b063-0143 と同じ（G4）。値が 0 だけ |
| x0027 | Id Of Animal Category | id | 今の仕組みは category と言い切った（本体 category） | — | id | G5 | 「Id Of Animal Category」で animal_1。列名が Id で始まる。G5 で id |
| x0028 | Degree of severity 0 | quantity | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「Degree of severity 0」で 0,12,200＝その重さの段階の動物の数。列名は区分の名前に見えるが、値は数。同じ表に Degree of severity 1〜3 が並ぶ（区分ごとの数の横持ちの表）。列名の語では決まらず、表をまるごと読む段が要る（G4：同じ形の兄弟列が並び、値が整数なら quantity） |
| x0029 | GOR CODE | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「GOR CODE」で H・H。列名が CODE で終わるのに category。recheck の \bcode$ は大文字小文字を問わないので当たるはず→見張りの段で category と言い切ったため recheck を通らない。言い切った答えにも列名の強い手がかり（code$）との食い違いを調べる段が要る（G10） |
| x0030 | Gemeinde_Nr | id | 今の仕組みは address と言い切った（本体 address） | — | id | D5 | 「Gemeinde_Nr」で 5,7,12＝自治体の番号。本体は address。G8（_nr）で id。D5 の _nr$ でも id |
| x0031 | id2 | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「id2」で city・europe＝駐車場の短い名前のコード。列名の id2 は ^id\b に当たらない（id の後に 2）。id\d*$ にすれば当たる。G5 を広げるかは確かめる陣で |
| x0032 | parameter_decimals | quantity | 今の仕組みは category と言い切った（本体 category） | — | quantity | G9 | 「parameter_decimals」で 0＝小数の桁数。数（quantity）。G9 |
| x0033 | batch | id | 今の仕組みは category と言い切った（本体 category） | — | category |  | 「batch」で 1,1,2,2。実験の回の番号。列名の語だけでは category と id の境目で、規則にしにくい（batch は区分とも読める）。決めないのが安全 |
| x0034 | Semaine | date | 今の仕組みは quantity と言い切った（本体 quantity） | — | date | G2 | 【重大】「Semaine」（週）で値 2〜53 の整数。本体は quantity と言い切った。週・月の番号は日付の部分（LABEL_GUIDE の date）で、列名の語だけで決まる。G2 で date。同じ表に Nombre_Deces（件数）があるので、値の形（小さい整数）だけで読むと数量に寄る |
| x0035 | traktandum_start_behandlung_uhrzeit | date | 今の仕組みは text と言い切った（本体 text） | — | date | G7 | 「traktandum_start_behandlung_uhrzeit」で 13.30-16.30＝時刻の幅。本体は text。G7 で date |
| x0036 | Id Experiment Category | id | 今の仕組みは category と言い切った（本体 category） | — | id | G5 | 「Id Experiment Category」。G5 で id |
| x0037 | Extending Agency | id | 今の仕組みは org と言い切った（本体 org） | — | unknown | G8 | b062-0186 と同じ表の形（別の年）。G8 で不明 |
| e0001 | Tree | id | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.679） | id | unknown |  |  |
| e0002 | TIME_PERIOD | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.965） | date | date | G2 |  |
| e0003 | Rateable Value 2010 | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.987） | amount | unknown |  |  |
| e0004 | monitoring_program | category | recheck：確信が低く、手がかりもない（本体 1 位 id 0.617） | id | unknown |  | 「monitoring_program」で BAQUA_TI。正解 category、ChatGPT id。値が 1 種類のコード。境目 |
| e0005 | EW_Total_Company_SA | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.765） | category | unknown |  | u0103 と同じ（G1） |
| e0006 | Beschluss | amount | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 id 0.494） | unknown | unknown |  | 「Beschluss」（決定）で 11300。同じ表に Nachgefragt（申請）・Kategorie。決定した額。CHF の手がかりが同じ表のどこにもなければ決めない |
| e0007 | Body | id | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.985） | id | unknown |  |  |
| e0008 | OrganisationCode | id | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.977） | id | unknown |  |  |
| e0009 | Arrest/Detention > Assault | quantity | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.896） | quantity | unknown |  |  |
| e0010 | SiteReference | id | recheck：確信が低く、手がかりもない（本体 1 位 id 0.838） | id | id | G5 |  |
| e0011 | value | quantity | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 rate 0.437） | unknown | unknown |  | 「value」で 92,109。同じ表に valueCategory・agegroup・sex。value だけでは決めない（LABEL_GUIDE）。valueCategory の値（例：人数）が分かれば決まる→同じ表の単位・区分の列の値を決め方に渡す必要（G12） |
| e0012 | Type of Aid | category | recheck：確信が低く、手がかりもない（本体 1 位 id 0.724） | id | unknown |  | 「Type of Aid」で C01。正解 category、ChatGPT id。列名が Type of…（種類）なら値がコードでも category。規則にできる：列名が type・kind・art・typ・category で始まるなら id にしない |
| e0013 | EW_CVL_SA | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.939） | category | unknown |  | u0103 と同じ（G1） |
| e0014 | Grand Total 
(workforce numbers) | quantity | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.981） | quantity | unknown |  |  |
| e0015 | Lim_min | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.881） | quantity | unknown |  |  |
| e0016 | SMR 2024 | rate | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.879） | rate | unknown |  |  |
| e0017 | PaymentDate | date | cue_conflict:amount（本体 1 位 date 0.985） | date | unknown |  |  |
| e0018 | Cost Centre | id | cue_conflict:amount（本体 1 位 id 0.982） | id | unknown |  |  |
| e0019 | UK Treaty Actions November 2015 - Februa | text | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 text 0.49） | text | unknown |  |  |
| e0020 | max_time_generation | quantity | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.967） | quantity | unknown |  |  |
| e0021 | $15,000 to $19,999 / 15 000 $ a 19 999 $ | quantity | verifier:quantity（本体 1 位 amount 0.981） | quantity | unknown |  |  |
| e0022 | Procurement Start Date | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.985） | date | unknown |  |  |
| e0023 | Rank | category | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.523） | category | unknown |  |  |
| e0024 | Quarter | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.912） | date | date | G2 |  |
| e0025 | $5,000 to $9,999 / 5 000 $ a  9 999 $ | quantity | verifier:quantity（本体 1 位 amount 0.975） | quantity | unknown |  |  |
| e0026 | service | product | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 text 0.454） | category | unknown |  | 「service」でサービスの名前。正解 product、ChatGPT category。境目 |
| e0027 | RANK OF IMD SCORE (where 1 is most depri | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 category 0.354） | category | unknown |  |  |
| e0028 | date_of_publication_or_production_standa | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.986） | date | unknown |  |  |
| e0029 | value | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.985） | amount | unknown |  |  |
| e0030 | TIME_PERIOD | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.958） | date | date | G2 |  |
| e0031 | Class ID | id | verifier:amount（本体 1 位 id 0.993） | id | id | G5 |  |
| e0032 | TOTAL_SHEEP_MOUNTAIN | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.955） | quantity | unknown |  |  |
| e0033 | $10,000 to $14,999 / 10 000 $ a 14 999 $ | quantity | verifier:quantity（本体 1 位 amount 0.984） | quantity | unknown |  |  |
| e0034 | $20,000 to $24,999 / 20 000 $ a 24 999 $ | quantity | verifier:quantity（本体 1 位 amount 0.984） | quantity | unknown |  |  |
| e0035 | Version | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 category 0.494） | category | unknown |  |  |
| e0036 | Got everything I wanted | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.679） | rate | unknown |  |  |
| e0037 | EW_Receiver_SA | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.83） | category | unknown |  | u0103 と同じ（G1） |
| e0038 | Fossil fuels | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.743） | quantity | unknown |  |  |
| e0039 | temporal | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.981） | date | date | G2 |  |
| e0040 | Emp_Wkf_POPD_15+yrs_2026 | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.981） | quantity | unknown |  |  |
| e0041 | Number | quantity | recheck:cue_id（本体 1 位 quantity 0.96） | quantity | unknown |  |  |
| e0042 | Under $5,000 / Moins de 5 000 $ | quantity | verifier:quantity（本体 1 位 amount 0.96） | quantity | unknown |  |  |
| e0043 | 5 | category | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.575） | category | unknown |  |  |
| e0044 | designation | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 address 0.409） | address | unknown |  | 「designation」で停留所・窓口の名前。正解 category、ChatGPT address。地点の名前は address か category か境目 |
| e0045 | 6 | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 category 0.436） | category | unknown |  |  |
| e0046 | STATISTIC | id | cue_conflict:rate（本体 1 位 id 0.991） | id | unknown |  |  |
| e0047 | Price (K) | amount | verifier:quantity（本体 1 位 amount 0.981） | amount | unknown |  |  |
| e0048 | Q2 (July - September 2014) | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.984） | amount | unknown |  |  |
| e0049 | buy_to_let_properties__fixed_rate__over_ | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.959） | rate | unknown |  |  |
| e0050 | crime | category | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.685） | unknown | unknown |  | 「crime」で 0 だけ。同じ表に administration・agriculture…（分野の名前が並ぶ）＝その分野に当たるかの印（0/1）。正解は category。値が 0 だけでは数とも印とも読めない。決めないのが正しい |
| e0051 | Emp_Wkf_POPD_15+yrs_2022 | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.985） | quantity | unknown |  |  |
| e0052 | perPikaHabitat | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.952） | rate | unknown |  |  |
| e0053 | temporal | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.977） | date | date | G2 |  |
| e0054 | FISCAL_YEAR | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.976） | date | unknown |  |  |
| e0055 | Structure | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 text 0.403） | address | unknown |  | 「Structure」で建物の名前。正解 category、ChatGPT address。境目 |
| e0056 | List Number_ numero de liste | id | cue_conflict:quantity（本体 1 位 id 0.958） | id | unknown |  |  |
| e0057 | id2 | id | recheck：確信が低く、手がかりもない（本体 1 位 id 0.675） | id | unknown |  |  |
| e0058 | referenztarif | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.848） | unknown | unknown |  | 「referenztarif」で 683。同じ表に waehrung（通貨）。通貨の列があるので金額。同じ表の列名に通貨の語（waehrung・currency・devise）があれば通貨の手がかりにする（G11） |
| e0059 | Surplus Spend | amount | verifier:id（本体 1 位 amount 0.982） | amount | unknown |  |  |
| e0060 | Wert | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.919） | unknown | unknown |  | 「Wert」。同じ表に Einheit。G12 |
| e0061 | Emp_Wkf_POPD_15+yrs_2021 | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.98） | quantity | unknown |  |  |
| e0062 | principal_dwelling_houses__fixed_rate__f | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.955） | rate | unknown |  |  |
| e0063 | Service_FR | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 account 0.468） | category | unknown |  |  |
| e0064 | Very Satisfied | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.711） | rate | rate | G3 |  |
| e0065 | Type of Post | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 category 0.493） | category | unknown |  |  |
| e0066 | Irrecoverable VAT | amount | recheck：値に根拠がない（0 だけなど）（本体 1 位 amount 0.981） | amount | unknown |  |  |
| e0067 | Metal ores | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.81） | quantity | unknown |  |  |
| e0068 | Non-metallic minerals | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.864） | quantity | unknown |  |  |
| e0069 | modell_lauf | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.978） | date | unknown |  |  |
| e0070 | UpperB | quantity | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.64） | quantity | unknown |  |  |
| e0071 | wert | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.972） | unknown | unknown |  | 「wert」。G12 |
| e0072 | pop | quantity | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.692） | quantity | unknown |  |  |
| e0073 | Emp_Wkf_POPD_15+yrs_2028 | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.979） | quantity | unknown |  |  |
| e0074 | OrganisationCode | id | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.978） | id | unknown |  |  |
| e0075 | pop | quantity | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.812） | quantity | unknown |  |  |
| e0076 | @Caption | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.983） | S | unknown |  | 「@Caption」で @Creator…＝白書の表が崩れている。正解 date だが、LABEL_GUIDE では S（正解を見直す） |
| e0077 | Total - All Returns /Total - Toutes les  | quantity | 見張り：数字の種類の 1 位と 2 位が近い（本体 1 位 amount 0.524） | quantity | unknown |  |  |
| e0078 | Q4 (January - March 2015) | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.903） | amount | unknown |  |  |
| e0079 | Emp_Wkf_POPD_15+yrs_2027 | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.972） | quantity | unknown |  |  |
| e0080 | 前5日間平均気温の品質情報 | category | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.945） | category | unknown |  |  |
| e0081 | Emp_Wkf_POPD_15+yrs_2024 | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.987） | quantity | unknown |  |  |
| e0082 | reporting_period | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.682） | category | unknown |  | 「reporting_period」で P01・P02＝会計の期間。正解 date、ChatGPT category。会計の期の番号は date か category か LABEL_GUIDE で決まっていない（正解を見直す） |
| e0083 | Widmung | text | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 other 0.475） | text | unknown |  |  |
| e0084 | Non-Payroll staff (contingent labour/con | amount | verifier:quantity（本体 1 位 amount 0.887） | amount | unknown |  |  |
| e0085 | buy_to_let_properties__floating_rate__st | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.944） | rate | unknown |  |  |
| e0086 | Arrest/Detention > Fraud | quantity | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.735） | quantity | unknown |  |  |
| e0087 | Total | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.989） | unknown | unknown |  | 「Total」で 1,062.00（小数 2 桁）。同じ表に Transaction Date。金額らしいが通貨の手がかりがない。通貨の手がかりの規則（amount_cue_veto）で不明にしたのは決まりどおり |
| e0088 | principal_dwelling_houses__floating_rate | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.954） | rate | unknown |  |  |
| e0089 | principal_dwelling_houses__floating_rate | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.633） | rate | unknown |  |  |
| e0090 | Mandatory Relief % | rate | verifier:quantity（本体 1 位 rate 0.977） | rate | unknown |  |  |
| e0091 | Dwellings value | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.595） | quantity | unknown |  |  |
| e0092 | EW_Total_Company_NSA | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.607） | quantity | unknown |  |  |
| e0093 | Titel | org | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 org 0.495） | address | unknown |  | 「Titel」で Parkhaus Storchen。正解 org、ChatGPT address。境目 |
| e0094 | wert | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.943） | unknown | unknown |  | 「wert」で 12931,44。同じ表に metrik・einheit。einheit（単位）の値が渡れば決まる（G12） |
| e0095 | vj_rel_kumsum | rate | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.698） | rate | unknown |  |  |
| e0096 | Gcons2006 | quantity | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.934） | unknown | unknown |  | 「Gcons2006」で 14300＝ガスの使用量（kWh）。略語で単位がない。決めない（同じ表に Gcons2005Valid） |
| e0097 | Cost Centre | id | cue_conflict:amount（本体 1 位 id 0.988） | id | unknown |  |  |
| e0098 | Neither satisfied nor dissatisfied | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.564） | rate | rate | G3 |  |
| e0099 | Family_Famille | category | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.825） | other | unknown |  | 「Family_Famille」で植物の科。正解 category、ChatGPT other。分類群は区分 |
| e0100 | Arrest/Detention > Drugs | quantity | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.896） | quantity | unknown |  |  |
| e0101 | MaleLowerQuartile | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.95） | rate | unknown |  |  |
| e0102 | Time period | quantity | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 quantity 0.478） | quantity | unknown |  |  |
| e0103 | Control Budget Code | category | cue_conflict:amount（本体 1 位 id 0.616） | id | unknown |  | 「Control Budget Code」で DEL・AME＝予算の区分。正解 category、ChatGPT id。列名が Code でも値が少ない種類の略号なら区分。境目 |
| e0104 | Tax gap component | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 account 0.468） | category | unknown |  |  |
| e0105 | Legislatur | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.913） | date | unknown |  |  |
| e0106 | Cost Centre | id | cue_conflict:amount（本体 1 位 id 0.978） | id | unknown |  |  |
| e0107 | plan | text | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 category 0.459） | text | unknown |  |  |
| e0108 | principal_dwelling_houses__floating_rate | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.96） | rate | unknown |  |  |
| e0109 | SMR 2019-2023 | rate | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.859） | rate | unknown |  |  |
| e0110 | Value | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.99） | amount | unknown |  |  |
| e0111 | YearWeekIso | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.987） | date | unknown |  |  |
| e0112 | Wert | amount | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 other 0.419） | unknown | unknown |  | 「Wert」で 4.4e10。同じ表に Kennzahl。G12 |
| e0113 | NO_COMPLEMENTAIRE | id | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.863） | S | unknown |  | 「NO_COMPLEMENTAIRE」で 1。同じ表の列名に ZIP のかけらが混ざる。ChatGPT は S。列名の NO_ は番号（id）。表が崩れていても列は読める |
| e0114 | SiteReference | id | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.794） | id | id | G5 |  |
| e0115 | Arrest/Detention > Child Pornography | quantity | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.585） | quantity | unknown |  |  |
| e0116 | Contract Commencement Date | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.984） | date | unknown |  |  |
| e0117 | Q3 (October - December 2014) | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.987） | amount | unknown |  |  |
| e0118 | Datierung_Bemerkung | text | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.669） | text | unknown |  |  |
| e0119 | AnzStand | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.964） | quantity | unknown |  |  |
| e0120 | Age | category | 見張り：数字の種類なのに値が数として読めない（本体 1 位 quantity 0.862） | category | unknown |  |  |
| e0121 | digital_platform | category | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.891） | other | unknown |  | 「digital_platform」で e-manuscripta.ch。正解 category、ChatGPT other。サイトの名前の区分。境目 |
| e0122 | Quarter | date | cue_conflict:amount（本体 1 位 date 0.974） | date | date | G2 |  |
| e0123 | Arrest/Detention > Murder / Manslaughter | quantity | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.707） | quantity | unknown |  |  |
| e0124 | TLIST(A1) | date | cue_conflict:rate（本体 1 位 date 0.986） | date | unknown |  |  |
| e0125 | energy | category | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.637） | unknown | unknown |  | u0006 と同じ |
| e0126 | aktiver_energieverbrauch | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.836） | quantity | unknown |  |  |
| e0127 | Ratio | rate | 見張り：数字の種類なのに値が数として読めない（本体 1 位 rate 0.98） | rate | unknown |  |  |
| e0128 | Property | org | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 text 0.488） | account | unknown |  | 「Property」で Home Office - IPS。正解 org、ChatGPT account。組織名なので org |
| e0129 | Arrest/Detention > Immigration | quantity | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.949） | quantity | unknown |  |  |
| e0130 | 03:00 | quantity | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 rate 0.395） | unknown | unknown |  | u0068 と同じ |
| e0131 | Biomass | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.776） | quantity | unknown |  |  |
| e0132 | wert | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.609） | unknown | unknown |  | 「wert」。G12 |
| e0133 | EW_Admin_SA | quantity | 見張り：数字の種類なのに値が数として読めない（本体 1 位 quantity 0.584） | category | unknown |  | u0103 と同じ（G1） |
| e0134 | principal_dwelling_houses__fixed_rate__o | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.941） | rate | unknown |  |  |
| e0135 | Arrest/Detention > Modern Slavery / Huma | quantity | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.68） | quantity | unknown |  |  |
| e0136 | finances | category | recheck：値に根拠がない（0 だけなど）（本体 1 位 amount 0.76） | unknown | unknown |  | u0006 と同じ |
| e0137 | buy_to_let_properties__floating_rate__tr | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.949） | rate | unknown |  |  |
| e0138 | Emp_Wkf_POPD_15+yrs_2025 | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.984） | quantity | unknown |  |  |
| e0139 | Grand Total 
(workforce numbers) | quantity | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.981） | quantity | unknown |  |  |
| e0140 | Total | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.989） | amount | unknown |  |  |
| e0141 | AGE | category | recheck：確信が低く、手がかりもない（本体 1 位 id 0.516） | category | unknown |  |  |
| e0142 | Got none of what I wanted | rate | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.579） | rate | rate | G3 |  |
| e0143 | VALUE | quantity | 見張り：数字の種類なのに値が数として読めない（本体 1 位 quantity 0.92） | S | unknown |  | 「VALUE」で値がすべて「.」（欠け）。正解は quantity だが、LABEL_GUIDE では値が空ばかりの列は S（正解を見直す） |
| e0144 | LowerB | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.687） | quantity | unknown |  |  |
| e0145 | C02199V02655 | id | cue_conflict:rate（本体 1 位 id 0.993） | id | unknown |  |  |
| e0146 | C02350V02827 | id | cue_conflict:amount（本体 1 位 id 0.993） | id | unknown |  |  |
| e0147 | Gcons2005 | quantity | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.944） | unknown | unknown |  | u0008 と同じ |
| e0148 | organisati | id | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.986） | id | unknown |  |  |
| e0149 | Nachgefragt | amount | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.88） | unknown | unknown |  | 「Nachgefragt」で 16100。u0016 と同じ表。申請額。通貨の手がかりがないので決めない |
| e0150 | Supplier | org | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 account 0.422） | account | unknown |  | 「Supplier」で TPS – Funding Account 1。正解 org、ChatGPT account。値は口座名なので境目 |
| e0151 | Prov/Terr | address | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 other 0.468） | address | unknown |  |  |
| e0152 | vj_abs_kumsum | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.554） | quantity | unknown |  |  |
| e0153 | Amount per Container | quantity | 見張り：数字の種類の 1 位と 2 位が近い（本体 1 位 amount 0.549） | quantity | unknown |  |  |
| e0154 | Got some of what I wanted | rate | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.679） | rate | rate | G3 |  |
| e0155 | Total | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.988） | amount | unknown |  |  |
| e0156 | Cost Centre | id | cue_conflict:amount（本体 1 位 id 0.967） | id | unknown |  |  |
| e0157 | Versicherer | id | verifier:id（本体 1 位 quantity 0.971） | unknown | unknown |  | 「Versicherer」（保険者）で 57,62＝保険者の番号。名前の語なのに値が整数。G8 と同じ考えで、名前としては言い切らないが、id とも決めない |
| e0158 | Emp_Wkf_POPD_15+yrs_2023 | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.975） | quantity | unknown |  |  |
| e0159 | OrganisationCode | id | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.978） | id | unknown |  |  |
| e0160 | Payroll staff costs | amount | verifier:quantity（本体 1 位 amount 0.984） | amount | unknown |  |  |
| e0161 | Q1 (April - June 2014) | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.986） | amount | unknown |  |  |
| e0162 | STATISTIC | category | recheck：確信が低く、手がかりもない（本体 1 位 id 0.874） | id | unknown |  | 「STATISTIC」で STOCKNURSE。正解 category、ChatGPT id。統計の系列のコード（正解を見直す） |
| e0163 | Value (L) | amount | verifier:quantity（本体 1 位 amount 0.981） | amount | unknown |  |  |
| e0164 | funk | id | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.657） | unknown | unknown |  | 「funk」で 29,35。意味が分からない略語。決めない |
| e0165 | EAP amount ($) | amount | verifier:quantity（本体 1 位 amount 0.989） | amount | unknown |  |  |
| e0166 | 終了日（日） | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.981） | date | unknown |  |  |
| e0167 | date_of_publication_or_production | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.982） | date | unknown |  |  |
| e0168 | vj_rel_n | rate | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.947） | rate | unknown |  |  |
| e0169 | sensor | id | recheck：確信が低く、手がかりもない（本体 1 位 id 0.834） | id | unknown |  |  |
| e0170 | 9 | category | 見張り：数字の種類なのに値が数として読めない（本体 1 位 quantity 0.648） | category | unknown |  |  |
| e0171 | EW_CVA_SA | quantity | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.977） | category | unknown |  | u0103 と同じ（G1） |
| e0172 | bathPosition | id | 見張り：本体の 1 位が other（種類を付けない）（本体 1 位 other 0.632） | id | unknown |  |  |
| e0173 | Got most of what I wanted | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.557） | rate | rate | G3 |  |
| e0174 | Beschaffungsgegenstand | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 category 0.498） | category | unknown |  |  |
| e0175 | MCC | id | verifier:quantity（本体 1 位 id 0.984） | id | unknown |  |  |
| e0176 | Emp_Wkf_POPD_15+yrs_2029 | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.981） | quantity | unknown |  |  |
| e0177 | min_time_generation | quantity | recheck：値に根拠がない（0 だけなど）（本体 1 位 quantity 0.951） | quantity | unknown |  |  |
| e0178 | EW_Compulsory_SA | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.852） | category | unknown |  | 「EW_Compulsory_SA」で値がすべて [x]（伏せた値）。G1 で欠けとして外すと値が残らない。正解は quantity だが、値が空ばかりなら S（正解を見直す）。ChatGPT は [x] を印と読んで category にした→[x]・[z] は英国統計の欠けの記号だと規則に書く（G1） |
| e0179 | Sexual violence ('000) | quantity | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.72） | quantity | unknown |  |  |
| e0180 | replicate | id | recheck：確信が低く、手がかりもない（本体 1 位 quantity 0.928） | id | unknown |  |  |
| e0181 | Discretionary relief % | rate | verifier:quantity（本体 1 位 rate 0.973） | rate | unknown |  |  |
| e0182 | Week | date | 見張り：date なのに値に日付の形が少ない（本体 1 位 date 0.887） | date | date | G2 |  |
| e0183 | RemunerationValue | amount | 見張り：数字の種類なのに値が数として読めない（本体 1 位 amount 0.88） | amount | unknown |  |  |
| e0184 | Variable | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 category 0.438） | category | unknown |  |  |
| e0185 | Cost Centre | id | cue_conflict:amount（本体 1 位 id 0.982） | id | unknown |  |  |
| e0186 | STATISTIC | id | cue_conflict:amount（本体 1 位 id 0.993） | id | unknown |  |  |
| e0187 | Age | category | 見張り：数字の種類なのに値が数として読めない（本体 1 位 quantity 0.889） | category | unknown |  |  |
| e0188 | kumsum | quantity | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 amount 0.425） | quantity | unknown |  |  |
| e0189 | IrrecoverableVAT | amount | recheck：値に根拠がない（0 だけなど）（本体 1 位 amount 0.983） | amount | unknown |  |  |
| e0190 | Total (All categories) | quantity | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.93） | quantity | unknown |  |  |
| e0191 | plz | address | recheck：確信が低く、手がかりもない（本体 1 位 id 0.864） | address | unknown |  |  |
| e0192 | 04:00 | quantity | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.746） | unknown | unknown |  | u0068 と同じ |
| e0193 | Satisfied | rate | recheck：rate なのに率の手がかりがない（本体 1 位 rate 0.803） | rate | rate | G3 |  |
| e0194 | AGE | category | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 id 0.369） | category | unknown |  |  |
| e0195 | vj_abs_n | quantity | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 other 0.48） | quantity | unknown |  |  |
| e0196 | 01:30 | quantity | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 rate 0.395） | unknown | unknown |  | 「01:30」で 97,96。同じ表に DATE・00:00…＝30 分ごとの計測。量か率かは表の題名がないと分からない。決めない |
| e0197 | library_call_number | id | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 org 0.434） | id | unknown |  |  |
| e0198 | bruttoinlandprodukt | amount | recheck：amount なのに列名・単位に金額の手がかりがない（本体 1 位 amount 0.982） | amount | unknown |  |  |
| e0199 | originating_sector_fr | account | 見張り：本体の 1 位の確率がしきい値より低い（本体 1 位 account 0.451） | org | unknown |  | 「originating_sector_fr」で役所の名前。正解 account、ChatGPT org。値は組織名なので org が自然（正解を見直す） |
