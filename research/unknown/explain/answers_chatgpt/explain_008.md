# 判断の説明 008 — ChatGPT

## r0038
- 前回の答えを変えるか：変える（category）。前回unknownからcategoryへ変更。後ろの行の1と同じ主題列群を確認。
- 種類：category
- 決め手：値の形
- ①列名・単位の語から読めること：「finances」finances は金融量にも見えるが、ここでは主題フラグ列。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「issued, administration, agriculture, construction, crime, culture, education, energy, geography」。issued・administration・agriculture・construction・crime・culture・education・energy・geographyと同じ分野名の列群。
- ④値の形から読めること：値の先頭例「0 | 0 | 0 | 0 | 0 | 0 | 0 | 0」。後半の非欠損値は「1 | 1 | 1」。0が続く一方、後ろの行では1も出る。値は0/1で、財務額の単位や桁ではない。
- 迷った種類と、それを退けた理由：quantityの金融金額ではなく、行がfinanceテーマに属するかの有無。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：0/1の主題・該当フラグはcategory。単位付き金融金額はamount。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0039
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：見出しの語、メモ：Sexual violence ('000) は被害経験者数を千人単位で示す。）。
- 種類：quantity
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Sexual violence ('000)」Sexual violence ('000) は暴力経験者の人数を千人単位で表す語。単位欄の記載はなし。
- ②表の題名から読めること：表題「Women aged 18+ years who experienced sexual violence in past 12 months」。Women aged 18+ years who experienced sexual violence in past 12 months と明記。
- ③同じ表の列名から読めること：兄弟列は「All perpetrators, Total women ('000)」。All perpetrators と Total women ('000) が並び、女性総数の内訳人数の列。
- ④値の形から読めること：値の例「45.2 | 44.2 | 30.2 | 75.8 | 171.6」。45.2, 44.2, 30.2, 75.8, 171.6 (thousands) の数値。パーセント記号はない。
- 迷った種類と、それを退けた理由：rateも考えられるが、題名は人数を数え、'000は千人単位。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：人数の千人単位表記はquantity、割合なら%またはrateの語が要る。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0040
- 前回の答えを変えるか：変えない。前回はidと判断（決め手：見出しの語、メモ：SiteReference は地点を参照する識別番号。）。
- 種類：id
- 決め手：見出しの語
- ①列名・単位の語から読めること：「SiteReference」SiteReference は敷地・計画地点の参照番号。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「OrganisationURI, SiteplanURL, GeoX, GeoY, Hectares, PlanningStatus, PermissionType, PermissionDate, PlanningHistory」。OrganisationURI・SiteplanURL・GeoX・GeoY・Hectares・PlanningStatus・PermissionType/Date・PlanningHistoryがあり、計画地属性とは別の参照キー。
- ④値の形から読めること：値の先頭例「292 | 351 | 1411 | 2024 | 2343 | 3053 | 4608a | 8069」。後半の非欠損値は「8071 | 9020 | 9041 | 9056 | 9057 | 9061 | 9120 | 9542」。292,351,1411…と4608a、後半8071〜9542など。数値/英数字の識別子。
- 迷った種類と、それを退けた理由：quantity/areaではなくsite key。住所や座標は別列。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：Reference/IDで対象地を参照する値はid。面積や座標を記録する列はother。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0041
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：表の題名、メモ：Tax gap component は税ギャップ内訳の定義済み区分。）。
- 種類：category
- 決め手：表の題名
- ①列名・単位の語から読めること：「Tax gap component」Tax gap component は税ギャップを構成する要素名。単位欄の記載はなし。
- ②表の題名から読めること：表題「Overall federal tax gap report: Estimates and key findings for non-com…」。Overall federal tax gap report の推計・調査資料。
- ③同じ表の列名から読めること：兄弟列は「2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022」。2014〜2022年が列に並び、各行の component が時系列で追われる次元。
- ④値の形から読めること：値の先頭例「PIT: reporting gap (hidden off… | PIT: gross tax gap (lower-boun… | PIT: net tax gap (upper-bound) | CIT: reporting gap (SMEs, lowe… | CIT: reporting gap (SMEs, uppe… | CIT: reporting gap (SMEs, % of… | CIT: reporting gap (large corp… | CIT: reporting gap (large corp…」。後半の非欠損値は「PIT: reporting gap (hidden off… | CIT: gross tax gap (% of CIT r… | CIT: net tax gap (lower-bound) | CIT: Impact of CRA compliance … | GST/HST: reporting gap | Excise: reporting gap (illegal… | Excise: payment gap | Excise: gross tax gap」。PIT reporting gap、gross/net tax gap、CIT等の定義済み要素名が並ぶ。
- 迷った種類と、それを退けた理由：textも候補だが長文の自由記述でなく、税ギャップの固定項目ラベル。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：固定された指標・構成要素名はcategory。説明文ならtext。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0042
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Workforce Projections の就業人口推計値。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Emp_Wkf_POPD_15+yrs_2021」r0011と同じ就業人口推計。違いは2021年列。単位欄の記載はなし。
- ②表の題名から読めること：表題「Workforce Projections」。Workforce Projections。
- ③同じ表の列名から読めること：兄弟列は「Six_Cities22, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029」。2022〜2029年の兄弟推計列とSix_Cities22が並ぶ。
- ④値の形から読めること：値の先頭例「1,196,330.31600 | 778,407.35730 | 535,028.74800 | 2,509,766.42130 | 157,777.72240 | 291,003.62210 | 191,479.51860 | 41,550.21832」。後半の非欠損値は「3,191,577.50272 | 770,642.03630 | 3,962,219.53902」。1,196,330.31600等、後半3,191,577.50272。
- 迷った種類と、それを退けた理由：r0011と同じ（違い：2021年列）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0011と同じ。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0043
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：見出しの語、メモ：Age の 0-64・65+ は年齢階級。）。
- 種類：category
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Age」Ageの0-64・65+は年齢階級で、人数ではない。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「AC, Semaine, Fin, Nombre_Deces, Attendu, Lim_min, Lim_sup, Exces」。AC・Semaine・Fin・Nombre_Deces・Attendu・Lim_min/Lim_sup・Excesの死亡統計に年齢区分が付く。
- ④値の形から読めること：値の例「0-64 | 65+ | 65+ | 65+ | 65+ | 0-64 | 65+ | 65+」。0-64と65+が並び、区切られた階級値。
- 迷った種類と、それを退けた理由：quantityの年齢/死亡件数ではなく、観測を分ける属性区分。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：年齢帯はcategory、個人の年齢や死亡数はquantity。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0044
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Material Footprint の化石燃料量。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Fossil fuels」Fossil fuels は材料フットプリント内の燃料物質量。単位欄の記載はなし。
- ②表の題名から読めること：表題「Material Footprint for Australia」。Material Footprint for Australia。
- ③同じ表の列名から読めること：兄弟列は「Product, Biomass, Metal ores, Non-metallic minerals, Total (All categories)」。Product・Biomass・Metal ores・Non-metallic minerals・Totalの材料区分と並ぶ。
- ④値の形から読めること：値の先頭例「155975600 | 153398500 | 150781700 | 152557700 | 161329100 | 175027300 | 166924500 | 163439700」。後半の非欠損値は「186349700 | 197940300 | 205485400 | 209350000 | 218237500 | 202894000 | 257562200 | 271479400」。155,975,600等、後半186,349,700〜218,237,500。物質フロー値。
- 迷った種類と、それを退けた理由：amountではない（通貨単位なし）。otherの気温等の測定属性とも異なり、材料量の集計。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：物質フローの材料量はquantity。燃料の金額ならamount。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0045
- 前回の答えを変えるか：変えない。前回はtextと判断（決め手：値の形、メモ：plan に入る個別の計画書名・文書名。）。
- 種類：text
- 決め手：値の形
- ①列名・単位の語から読めること：「plan」plan欄には個別の計画文書・計画名称が入る。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「FID, id, code, location」。FID・id・code・locationが別列にあり、planはキーでも場所でもなく対象計画の表題。
- ④値の形から読めること：値の例「Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado… | Runnymede 2030 Local Plan, Ado…」。Runnymede 2030 Local Plan, Adoption…が反復する長い名称。
- 迷った種類と、それを退けた理由：productではなく商品名でない計画書名。addressは別のlocation列。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：資料・計画書の題名はtext。商品名はproduct、場所はaddress。
- 規則にするなら（当てはまらない例も）：値が自由な題名・注記・文書名ならtext。ただし固定された型/選択肢はcategory、日時はdate。
- 確信：中

## r0046
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：同じ表の列名、メモ：死亡数の予測に対する下限値で、死亡件数の尺度。）。
- 種類：quantity
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「LowerB」LowerB は下限(bound)を示すが対象は死亡件数。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Year, Week, Ending, Age, NoDeaths_EP, Expected, UpperB, Diff」。Year・Week・Ending・Age・NoDeaths_EP・Expected・UpperB・Diffが並ぶので、死亡数予測の下限。
- ④値の形から読めること：値の先頭例「147 | 147 | 145 | 139 | 140 | 139 | 143 | 133」。後半の非欠損値は「130 | 141 | 130 | 132 | 129 | 126 | 127 | 137」。147, 147, 145…と後半130等の整数で、同じ行の期待死亡件数を挟む境界値。
- 迷った種類と、それを退けた理由：dateではなく値の境界。統計値otherではなく件数の下限quantity。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：件数の上/下限はquantity。日付・時刻の限界ならdate。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0047
- 前回の答えを変えるか：変えない。前回はrateと判断（決め手：同じ表の列名、メモ：SMR は観測死亡数と期待死亡数の比率。）。
- 種類：rate
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「SMR 2024」SMRはstandardized mortality ratio、標準化死亡比。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「institution, indicator, taux observe 2019-2023, taux attendu 2019-2023, SMR 2019-2023, nombre de cas 2019-2023, taux observe 2024, taux attendu 2024, nombre de cas 2024」。institution・indicator・観測率・期待率・SMR 2019-2023・nombre de cas・SMR 2024・症例数が並び、比率指標と件数を分ける。
- ④値の形から読めること：値の先頭例「1.0 | 0.0 | 1.0 | * | * | 0.0 | 2.3 | 2.2」。後半の非欠損値は「1.4 | 1.5」。1.0, 0.0, 2.3, 2.2等、*は欠測/秘匿表示。比率尺度。
- 迷った種類と、それを退けた理由：quantityは症例数の兄弟列。SMR自体は観測/期待の比なのでrate。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：観測値と期待値の比率はrate。生の症例数はquantity。
- 規則にするなら（当てはまらない例も）：値が相対比・割合・率を示すならrate。絶対数や金額を記録する列はquantity/amount。
- 確信：中

## r0048
- 前回の答えを変えるか：変えない。前回はunknownと判断（決め手：決められない、メモ：時刻別の数値だが、測定対象も単位も示されない。）。
- 種類：unknown
- 決め手：決められない
- ①列名・単位の語から読めること：「04:00」04:00は時刻ラベルであって値の単位ではない。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「DATE, 00:00, 00:30, 01:00, 01:30, 02:00, 02:30, 03:00, 03:30」。DATEと00:00から03:30までの時刻列が同じ並び。r0030と同じ観測表。
- ④値の形から読めること：値の先頭例「113 | 207 | 52 | 137 | 194 | 112 | 103 | 165」。後半の非欠損値は「101 | 116 | 106 | 114 | 108 | 104 | 93 | 92」。113,207,52,137等、後半101,116,106…の数値。対象も単位も示されない。
- 迷った種類と、それを退けた理由：r0030と同じ（違い：04:00列の値113〜207等）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0030と同じ。
- 規則にするなら（当てはまらない例も）：列名が汎用/略号で、表題・単位・兄弟列・値から対象の意味を一つに絞れないならunknown。単位・辞書・元表の説明が得られた場合にのみ決める。
- 確信：中

## r0049
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Workforce Projections の就業人口推計値。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Emp_Wkf_POPD_15+yrs_2024」r0011と同じEmp_Wkf_POPD_15+yrs系列。違いは2024年。単位欄の記載はなし。
- ②表の題名から読めること：表題「Workforce Projections」。Workforce Projections。
- ③同じ表の列名から読めること：兄弟列は「Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029」。Six_Cities22と2021〜2023、2025〜2029年の兄弟列。
- ④値の形から読めること：値の先頭例「1,230,867.76500 | 884,670.85480 | 600,290.44310 | 2,715,829.06290 | 165,808.21300 | 328,091.61860 | 205,357.00860 | 44,707.77680」。後半の非欠損値は「3,459,793.67990 | 820,224.66740 | 4,280,018.34730」。1,230,867.76500等、後半3,459,793.67990。
- 迷った種類と、それを退けた理由：r0011と同じ（違い：2024年列）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0011と同じ。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0050
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Material Footprint の非金属鉱物量。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Non-metallic minerals」Non-metallic minerals は材料フットプリント内の非金属鉱物量。単位欄の記載はなし。
- ②表の題名から読めること：表題「Material Footprint for Australia」。Material Footprint for Australia。
- ③同じ表の列名から読めること：兄弟列は「Product, Biomass, Fossil fuels, Metal ores, Total (All categories)」。Product・Biomass・Fossil fuels・Metal ores・Totalと同じ分類列群。
- ④値の形から読めること：値の先頭例「166919700 | 154698500 | 173701100 | 158463100 | 163166300 | 173209100 | 181089500 | 180795700」。後半の非欠損値は「167227500 | 184414300 | 192722900 | 204783600 | 214025300 | 212367900 | 241991400 | 256627800」。166,919,700等、後半184,414,300〜214,025,300。物質量の系列。
- 迷った種類と、それを退けた理由：r0021と同じ材料フローの量（違い：非金属鉱物）。通貨amountではない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：材料構成要素のフロー値はquantity、価格列ならamount。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0051
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：見出しの語、メモ：容器ごとの内容量で、lbs・mL・L などの単位がある。）。
- 種類：quantity
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Amount per Container」Amount per Container は容器1つ当たりの内容量を表す。単位欄の記載はなし。
- ②表の題名から読めること：表題「Hazardous Waste Inventory Audit」。Hazardous Waste Inventory Audit は有害廃棄物容器の監査。
- ③同じ表の列名から読めること：兄弟列は「Date, New/Used, Hazard Class, Quantity」。Date・New/Used・Hazard Class・Quantityと並び、amountは容器の容量/重量を示す属性。
- ④値の形から読めること：値の先頭例「0.50 lbs | 104 mL | 17 mL | 18.9 L | 104 mL | 946 mL | 6 Oz | 91 mL」。後半の非欠損値は「3.785 L | 0.035 Kg | 473 mL | 4 L | 0.30 lb | 95 mL | 160 mL | 57 mL」。0.50 lbs、104 mL、18.9 L、6 Oz等、後半に3.785 L・0.035 Kg・160 mL。明示単位付き内容量。
- 迷った種類と、それを退けた理由：amountは通貨額の型。ここは重量/体積のquantity。濃度ならother。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：容器内容の重量・体積はquantity。単価や処分費はamount。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0052
- 前回の答えを変えるか：変える（id）。前回addressからidへ変更。見出しは地理単位だが値は地域コード。
- 種類：id
- 決め手：値の形
- ①列名・単位の語から読めること：「Prov/Terr」Prov/Terr はprovince/territoryの略だが、値は地名でなく12・13・24などの統計地域コード。単位欄の記載はなし。
- ②表の題名から読めること：表題「Individual Tax Statistics by Area (ITSA) (2022 Tax Year)」。Individual Tax Statistics by Area (ITSA) の地域別申告集計。
- ③同じ表の列名から読めること：兄弟列は「CMA-CA/RMR-AR, Classification, Total - All Returns /Total - T…, Total Income / Revenu total, Under $5,000 / Moins de 5 000 …, $5,000 to $9,999 / 5 000 $ a  …, $10,000 to $14,999 / 10 000 $ …, $15,000 to $19,999 / 15 000 $ …, $20,000 to $24,999 / 20 000 $ …」。CMA-CA/RMR-AR・Classification・Total Returns・Total Income等、地理コードを統計分類軸として使う。
- ④値の形から読めること：値の先頭例「12 | 13 | 13 | 24 | 24 | 24 | 24 | 24」。後半の非欠損値は「35 | 35 | 35 | 35 | 35 | 48 | 48 | 48」。12,13,24,35,48等の数値コードが反復。名称文字列ではない。
- 迷った種類と、それを退けた理由：addressと迷うが、ここでは省略語だけでなく数値コードとして地域を参照する。州名そのものならaddress。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：地域の参照コードはid、読める州名・住所・郵便番号はaddress。コード対応表があれば確証。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0053
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Workforce Projections の就業人口推計値。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Emp_Wkf_POPD_15+yrs_2028」r0011と同じ15歳以上就業人口推計。違いは2028年。単位欄の記載はなし。
- ②表の題名から読めること：表題「Workforce Projections」。Workforce Projections。
- ③同じ表の列名から読めること：兄弟列は「Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2029」。2021〜2027・2029年の同系列とSix_Cities22。
- ④値の形から読めること：値の先頭例「1,264,090.28500 | 946,889.18120 | 641,598.97340 | 2,852,578.43960 | 171,698.56400 | 337,276.71730 | 214,454.49020 | 45,219.51648」。後半の非欠損値は「3,621,227.72758 | 842,015.36620 | 4,463,243.09378」。1,264,090.28500等、後半3,621,227.72758。
- 迷った種類と、それを退けた理由：r0011と同じ（違い：2028年列）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0011と同じ。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0054
- 前回の答えを変えるか：変えない。前回はotherと判断（決め手：見出しの語、メモ：Family は植物の科学的な分類群名。）。
- 種類：other
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Family_Famille」Family_Famille は生物分類の科（family/famille）。単位欄の記載はなし。
- ②表の題名から読めること：表題「TOPIC Open - Literature Review Module」。TOPIC Open - Literature Review Module は種・形質等の研究文献データ。
- ③同じ表の列名から読めること：兄弟列は「ID, SpeciesCode_CodeEspece, Synonym_Synonyme, TraitCode, TraitValue_ValeurTrait, TraitValueDescription_Descript…, TraitValueComments_Commentaire…, ReferenceID, ReferenceType」。ID・SpeciesCode・Synonym・TraitCode・TraitValue等に分類学的属性が並ぶ。
- ④値の形から読めること：値の先頭例「Sapindaceae | betulaceae | Rosaceae | Asteraceae | Asteraceae | asteraceae | Asteraceae | cyperaceae」。後半の非欠損値は「Juglandaceae | Cornaceae | aspleniaceae | poaceae | Poaceae | rosaceae | juncaceae | Cupressaceae」。Sapindaceae・Rosaceae・Asteraceae等の植物学上の科名。値の形式は固有の科学分類名。
- 迷った種類と、それを退けた理由：categoryも候補だが、LABEL_GUIDEは学名・科学名をotherに置く。組織名や自由文ではない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：学名・生物分類の科学名はother。一般的な選択区分ならcategory。
- 規則にするなら（当てはまらない例も）：値がURL・科学名・温度・濃度などguideでotherと定義された属性ならother。ただし/id/の組織URIはid。
- 確信：中

## r0055
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：同じ表の列名、メモ：死亡数の予測に対する下限値で、死亡件数の尺度。）。
- 種類：quantity
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「Lim_min」Lim_min は死亡数の下限値（minimum bound）。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「AC, Semaine, Fin, Age, Nombre_Deces, Attendu, Lim_sup, Exces」。AC・Semaine・Fin・Age・Nombre_Deces・Attendu・Lim_sup・Exces。上限Lim_supや期待数と対。
- ④値の形から読めること：値の先頭例「151 | 1023 | 879 | 1038 | 885 | 129 | 1101 | 1119」。後半の非欠損値は「1122 | 1088 | 902 | 131 | 1138 | 1138 | 141 | 1160」。151,1023,879等、後半1122,1088…の整数。死亡数の予測境界。
- 迷った種類と、それを退けた理由：r0046と同じ（違い：下限の列で、死亡数推計の別系列）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0046と同じ。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0056
- 前回の答えを変えるか：変えない。前回はidと判断（決め手：同じ表の列名、メモ：組織名・組織ID列と対になる組織 URI。）。
- 種類：id
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「organisati」organisati は見出しが途中で切れた表記だが、値のURIと列配置からorganisation URIと読める。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「FID, id_0, id, organisa_1, siterefere, site_id_2, siteplanur, geox, geoy」。FID・id_0・id・organisa_1・sitereference・site_id_2・siteplanurl・geox・geoyが同居し、organisatiは組織リソースのURI。
- ④値の形から読めること：値の例「http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org… | http://opendatacommunities.org…」。http://opendatacommunities.org/id/... の形。一般サイトURLでなく/id/リソース参照。
- 迷った種類と、それを退けた理由：otherも候補だが、v2.1は組織・サービスの種類を指す/id URIをidと明記。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：/id/の対象URIはid、地図や文書リンクはother。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0057
- 前回の答えを変えるか：変えない。前回はrateと判断（決め手：同じ表の列名、メモ：満足度の回答段階ごとの割合。）。
- 種類：rate
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「Got some of what I wanted」Got some of what I wanted は満足度回答段階ごとの割合列。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Data status, Department, Organisation, Got everything I wanted, Got most of what I wanted, Got none of what I wanted, Very Satisfied, Satisfied, Neither satisfied nor dissatis…」。Got everything/most/none、Very Satisfied、Satisfied等同じ設問の選択肢列と並び、構成比を表す。
- ④値の形から読めること：値の先頭例「14.1 | 26.7 | 37.7 | 45 | 26 | 25.9 | 24.85 | 18」。後半の非欠損値は「27 | 25 | 28.2 | 12.2 | 27.6 | 17.2 | 23.3 | 20」。14.1, 26.7, 37.7, 45等、後半27, 25, 28.2等。割合として他段階と合計される尺度。
- 迷った種類と、それを退けた理由：categoryは回答段階のラベル列に使う。ここは選択肢別の数値割合なのでrate。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：アンケートの回答選択肢の割合はrate。個々の回答を分類するラベルならcategory。
- 規則にするなら（当てはまらない例も）：値が相対比・割合・率を示すならrate。絶対数や金額を記録する列はquantity/amount。
- 確信：中

## r0058
- 前回の答えを変えるか：変えない。前回はrateと判断（決め手：同じ表の列名、メモ：SMR は観測死亡数と期待死亡数の比率。）。
- 種類：rate
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「SMR 2019-2023」SMR 2019-2023 は観測死亡指標と期待死亡指標の比。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「institution, indicator, taux observe 2019-2023, taux attendu 2019-2023, nombre de cas 2019-2023, taux observe 2024, taux attendu 2024, SMR 2024, nombre de cas 2024」。institution・indicator・taux observé/attendu・SMR・nombre de casが並び、件数と比率を明確に分ける。
- ④値の形から読めること：値の先頭例「1.1 | 0.7 | 1.0 | * | * | 0.6 | 1.6 | 5.2」。後半の非欠損値は「0.0 | 2.8 | 1.3 | 0.9 | 0.9」。1.1,0.7,1.0,*…と後半0.0,2.8,1.3等。比率値。
- 迷った種類と、それを退けた理由：quantityはnombre de cas（症例数）。SMRは率/比。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：SMRなど観測対期待の比はrate。症例数はquantity。
- 規則にするなら（当てはまらない例も）：値が相対比・割合・率を示すならrate。絶対数や金額を記録する列はquantity/amount。
- 確信：中

## r0059
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：見出しの語、メモ：品質情報の 8 は気象データの品質コード。）。
- 種類：category
- 決め手：見出しの語
- ①列名・単位の語から読めること：「前5日間平均気温の品質情報」前5日間平均気温の品質情報は気象値ではなく観測品質コード。単位欄の記載はなし。
- ②表の題名から読めること：表題「気象観測_最新の気象データ」。気象観測_最新の気象データ。
- ③同じ表の列名から読めること：兄弟列は「観測所番号, 都道府県, 地点, 国際地点番号, 終了日（年）, 終了日（月）, 終了日（日）, 前5日間平均気温（℃）, 前5日間平均気温平年差（℃）」。観測所・都道府県・地点・日付各欄・平均気温（℃）・気温平年差・他の品質情報が並び、品質欄は測定単位と別。
- ④値の形から読めること：値の例「8 | 8 | 8 | 8 | 8 | 8 | 8 | 8」。8が反復する定数コード。温度なら℃付き小数や実測値の範囲になる。
- 迷った種類と、それを退けた理由：otherの気温測定値ではなく、観測値の品質状態を表すcategory。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：品質フラグの固定コードはcategory。実測気温はother。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0060
- 前回の答えを変えるか：変える（amount）。前回unknownからamountへ変更。後半の値とNachgefragt・独立ID・日付列を合わせて再判断。
- 種類：amount
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「Beschluss」Beschluss は決定・採択。単語だけなら決議番号にも読める。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Kategorie, Sparte, Nachgefragt, Status, Eingangsdatum, Beschlussdatum, ID」。Kategorie・Sparte・Nachgefragt・Status・Eingangsdatum・Beschlussdatumと独立IDがあり、申請額と決定日を持つ助成/予算表。
- ④値の形から読めること：値の先頭例「11300 | 2200 | 66200 | NA | 600 | 6800 | 10400 | 6500」。後半の非欠損値は「0 | 14000 | 200900 | 1900 | 8000 | 8800 | 181100 | 160800」。11,300・66,200・6,800等、後半200,900や181,100。IDは別列で、0やNAも金額列として自然。
- 迷った種類と、それを退けた理由：idも候補だが識別子は別のID列。Nachgefragtと対になる決定額と読むのが整合。通貨記号がなく確信は中。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：申請額・決定額が対で並ぶ表のBeschluss値はamount。決議番号なら明示コード/IDの手掛かりが必要。
- 規則にするなら（当てはまらない例も）：列名・対になる項目・表の文脈が申請額/決定額等の通貨価値を示すならamount。ただし件数はquantity、参照番号はid。
- 確信：中

## r0061
- 前回の答えを変えるか：変えない。前回はaddressと判断（決め手：見出しの語、メモ：plz は郵便番号。）。
- 種類：address
- 決め手：見出しの語
- ①列名・単位の語から読めること：「plz」plz はドイツ語 Postleitzahl（郵便番号）。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「jahr, bezirk_nr, bezirk, id, ort, leistungsauftrag, leistungsauftrag_gmde, indikator, wert」。jahr・bezirk_nr・bezirk・id・ort・leistungsauftrag等、地域名・地域番号と併せて住所軸を記録。
- ④値の形から読めること：値の先頭例「8910 | 8910 | 8910 | 8451 | 8460 | 8192 | 8152 | 8152」。後半の非欠損値は「8305 | 8303 | 8303 | 8302 | 8305 | 8305 | 8172 | 8172」。8910, 8451, 8192等4桁の郵便番号。後半8305, 8172等も同形式。
- 迷った種類と、それを退けた理由：idではなく郵便番号。LABEL_GUIDEは郵便番号をaddressに明記。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：郵便番号はaddress。郵便番号以外の統計区域コードはidとなることがある。
- 規則にするなら（当てはまらない例も）：値が住所・場所・建物・停留所等の場所名称を指すならaddress。ただし組織名はorg、住所とは別の参照コードはid。
- 確信：中

## r0062
- 前回の答えを変えるか：変えない。前回はtextと判断（決め手：見出しの語、メモ：Datierung_Bemerkung は日付に関する自由記述の注記。）。
- 種類：text
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Datierung_Bemerkung」Datierung_Bemerkung は日付の注記/転記上の備考。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Illustration, Widmung」。ID・Signatur・AutorIn・Titel・Ort・Datierung_von/bis・Illustration・Widmungが並び、日付欄とは別の補足欄。
- ④値の形から読めること：値の先頭例「Poststempel | Entzifferung unsicher | Orig.: 8 Octobre nouveau style… | 9. Juni (?) | Dat. Karte (Br. undat.) | Entzifferung unsicher | Entzifferung unsicher | Orig.: 29. Brumaire an IV」。後半の非欠損値は「Orig.: 7. Brumaire an XIII | Datum Zeugnis Emil Gottfried v…」。Poststempel、Entzifferung unsicher、Orig.: 日付、9. Juni (?)等、様式の異なる自由注記。
- 迷った種類と、それを退けた理由：dateは正規化された時点。ここは不確かな転記も含む自由文text。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：日付に関する自由注記はtext、標準化された日付列はdate。
- 規則にするなら（当てはまらない例も）：値が自由な題名・注記・文書名ならtext。ただし固定された型/選択肢はcategory、日時はdate。
- 確信：中

## r0063
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Material Footprint のバイオマス量。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Biomass」Biomass は材料フットプリントにおける生物資源の物質量。単位欄の記載はなし。
- ②表の題名から読めること：表題「Material Footprint for Australia」。Material Footprint for Australia。
- ③同じ表の列名から読めること：兄弟列は「Product, Fossil fuels, Metal ores, Non-metallic minerals, Total (All categories)」。Product・Fossil fuels・Metal ores・Non-metallic minerals・Totalと同じ材料区分列。
- ④値の形から読めること：値の先頭例「131582800 | 123151500 | 143881300 | 154014800 | 160529000 | 179414000 | 183334800 | 173978700」。後半の非欠損値は「164841600 | 147294700 | 175690600 | 170827200 | 175287500 | 144189600 | 159225000 | 166390000」。131,582,800等、後半164,841,600〜175,690,600。量の系列で通貨記号はない。
- 迷った種類と、それを退けた理由：r0021と同じ（違い：鉱石でなくbiomassの材料量）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：物質フロー量はquantity、通貨評価額ならamount。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0064
- 前回の答えを変えるか：変える（S）。前回はunknown。今回は列名の先頭にZIP由来の文字列が混入し、列と値の対応が壊れているため、通常の分類ではなく除外に変更した。
- 種類：S
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「NO_COMPLEMENTAIRE」NO_COMPLEMENTAIRE はフランス語の追加番号に見えるが、列の値の解釈以前に表ヘッダーが壊れている。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「PK     L"]]­„³²MóMó   …, ID_DOSSIER, TYPE_DOSSIER, TYPE_OPERATION, NOM_DOSSIER, NO_DOSSIER, STATUT, OPERATION, ORIGINE」。同じ表の列名の先頭にPK ZIPバイナリ由来の文字列が混ざり、ID_DOSSIER等と並んでいる。構造破損。
- ④値の形から読めること：値の例「1 | 1 | 1 | 1 | 1 | 1 | 1 | 1」。値1が反復しても、列位置や定義が信頼できない。
- 迷った種類と、それを退けた理由：id/quantity/categoryの選択より先に表が崩れているためS。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：破損ヘッダーや列ずれはS。正常な列名と値が復元できたら再判定。
- 規則にするなら（当てはまらない例も）：列構造が破損して列名と値の対応を信用できない場合はS。意味が読める正常列には使わない。
- 確信：中

## r0065
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Workforce Projections の就業人口推計値。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Emp_Wkf_POPD_15+yrs_2022」r0011と同じ15歳以上就業人口の予測。違いは2022年。単位欄の記載はなし。
- ②表の題名から読めること：表題「Workforce Projections」。Workforce Projections。
- ③同じ表の列名から読めること：兄弟列は「Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029」。Six_Cities22と2021・2023〜2029年の同系列列。
- ④値の形から読めること：値の先頭例「1,181,105.90700 | 776,608.72070 | 542,331.13300 | 2,500,045.76070 | 154,303.68380 | 300,092.53510 | 197,583.65530 | 42,883.56708」。後半の非欠損値は「3,194,909.20198 | 778,362.84380 | 3,973,272.04578」。1,181,105.90700等、後半3,194,909.20198。
- 迷った種類と、それを退けた理由：r0011と同じ（違い：2022年列）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0011と同じ。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0066
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：見出しの語、メモ：service は定義済みサービス名の区分。）。
- 種類：category
- 決め手：見出しの語
- ①列名・単位の語から読めること：「service」service はここではWebサービス名の分析軸。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「reporting_month, portfolio, users, sessions, cumulative_users」。reporting_month・portfolio・users・sessions・cumulative_usersが並び、アクセス指標をサービス別に集計する。
- ④値の形から読めること：値の先頭例「Find Business Regulation (FBR) | Report a Trade Barrier (RaTB) | Regulated Professions Register… | Business.gov.uk | Trade Remedies Service (TRS) | Business.gov.uk | Digital Market Access Service … | Report a Breach (RaB)」。後半の非欠損値は「Strategic Companies Insight To… | Make an Export Plan | AI Summariser | Check How to Export Goods (CHE… | Find a Buyer | DBT Assist | Data Workspace | Shared Parental Leave Tools (S…」。Find Business Regulation、Report a Trade Barrier、Regulated Professions Register、Make an Export Plan等、サービス名がカテゴリとして反復。
- 迷った種類と、それを退けた理由：productも考えたが、購入する品目でなく行政Webサービスの分析区分。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：Web解析で対象サービスごとに集計する列はcategory。サービス提供者名ならorg。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0067
- 前回の答えを変えるか：変えない。前回はrateと判断（決め手：同じ表の列名、メモ：満足度の回答段階ごとの割合。）。
- 種類：rate
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「Got none of what I wanted」Got none of what I wanted は満足度調査の回答段階。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Data status, Department, Organisation, Got everything I wanted, Got most of what I wanted, Got some of what I wanted, Very Satisfied, Satisfied, Neither satisfied nor dissatis…」。Got everything/most/someなど同一設問の各回答段階が並ぶ。
- ④値の形から読めること：値の先頭例「16.5 | 16.6 | 24.6 | 5 | 14 | 33.3 | 19 | 63」。後半の非欠損値は「9 | 10 | 12.3 | 31.7 | 29 | 43 | 15.2 | 7.1」。16.5,16.6,24.6等、後半9,10,12.3等。段階別の割合値。
- 迷った種類と、それを退けた理由：r0057と同じ（違い：『どれも得られなかった』の回答割合）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0057と同じ。
- 規則にするなら（当てはまらない例も）：値が相対比・割合・率を示すならrate。絶対数や金額を記録する列はquantity/amount。
- 確信：中

## r0068
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：表の題名、メモ：レッドリスト内の生態区分コード。）。
- 種類：category
- 決め手：表の題名
- ①列名・単位の語から読めること：「9」見出し9は単独では型が分からない。単位欄の記載はなし。
- ②表の題名から読めること：表題「レッドリスト/レッドデータブック_第５次レッドリスト」。レッドリスト/レッドデータブック第5次の生態区分。
- ③同じ表の列名から読めること：兄弟列は「1, 2, 3, 4, 5, 6, 7, 8, 10」。列1〜8,10が並び、9は同じ分類軸の一欄。
- ④値の形から読めること：値の先頭例「③ | D | D | B2ab | A2 | C2b | B2ab | B2ab」。後半の非欠損値は「3 | D1 | D2 | D2 | 2 | 2 | 12 | 23」。③・D・B2ab・A2・C2b・2・12・23等、保全状況/生態分類コード。順位の連番ではない。
- 迷った種類と、それを退けた理由：idも候補だが、コードは分類状態そのものを示し個体参照キーではない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：保全区分や生態状態のコード値はcategory。個体IDならid。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0069
- 前回の答えを変えるか：変えない。前回はaddressと判断（決め手：同じ表の列名、メモ：公共交通の停留所・窓口などサービス地点の名称。）。
- 種類：address
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「designation」designation は停留所・サービス地点に付ける名称。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「sloid, parentSloidServicePoint, parentNumberServicePoint, type, inductionLoop, wheelchairAccess, validFrom, validTo, creationDate」。sloid・parentSloidServicePoint・parentNumberServicePoint・type・accessibility・validFrom等と並び、実際の地点名フィールド。
- ④値の形から読めること：値の先頭例「Bissone (lago) | Informationsschalter | Stazione Lugano FLP | Guichet d'information | Capolago SNL | Billettschalter | Guichet des billets | Billettschalter」。後半の非欠損値は「Point de vente du Sentier | Bilettschalter | Bergstation Luftseilbahn Weglo… | Brusino Arsizio (lago) | Haupteingang | Guichet de billets | Reisezentrum Köniz」。Bissone (lago)、Stazione Lugano FLP、Guichet d'information、後半Point de vente du Sentier等の地点/窓口名。
- 迷った種類と、それを退けた理由：orgは運営機関名、categoryはtype。ここは地点そのものの名称なのでaddress。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：停留所・窓口・観測地点の名称はaddress。運営組織はorg。
- 規則にするなら（当てはまらない例も）：値が住所・場所・建物・停留所等の場所名称を指すならaddress。ただし組織名はorg、住所とは別の参照コードはid。
- 確信：中

## r0070
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Material Footprint の全材料量。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Total (All categories)」Total (All categories) は材料全区分の合計量。単位欄の記載はなし。
- ②表の題名から読めること：表題「Material Footprint for Australia」。Material Footprint for Australia。
- ③同じ表の列名から読めること：兄弟列は「Product, Biomass, Fossil fuels, Metal ores, Non-metallic minerals」。Product・Biomass・Fossil fuels・Metal ores・Non-metallic mineralsの各成分と並び、総和列。
- ④値の形から読めること：値の先頭例「688618500 | 648585000 | 693829900 | 718423000 | 739419600 | 785531700 | 787917600 | 759645500」。後半の非欠損値は「772547600 | 783900400 | 847159300 | 845966300 | 871770700 | 797558100 | 922832900 | 950519900」。688,618,500等、後半772,547,600〜871,770,700。集計された物質量。
- 迷った種類と、それを退けた理由：amountは通貨合計。ここは資源物量の総計。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：材料フロー成分およびその合計はquantity。価格の合計はamount。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0071
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：見出しの語、メモ：AGE の Y40T44 などは年齢階級コード。）。
- 種類：category
- 決め手：見出しの語
- ①列名・単位の語から読めること：「AGE」AGEのY40T44などは5歳刻みの年齢帯コード。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「TIME_PERIOD, GEO, SEX, OBS_STATUS, OBS_VALUE」。TIME_PERIOD・GEO・SEX・OBS_STATUS・OBS_VALUEの人口統計の軸列と並ぶ。
- ④値の形から読めること：値の先頭例「Y40T44 | Y15T19 | Y30T34 | Y10T14 | Y30T34 | Y30T34 | Y55T59 | Y75T79」。後半の非欠損値は「_T | Y0T4 | Y60T64 | Y80T84 | Y60T64 | Y70T74 | _T」。Y40T44, Y15T19, Y75T79, _T等。年齢階級ラベル。
- 迷った種類と、それを退けた理由：quantityの実年齢ではなく年齢群の分類値。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：年齢帯はcategory、年齢人数はquantity。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0072
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Workforce Projections の就業人口推計値。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Emp_Wkf_POPD_15+yrs_2026」r0011と同じ就業人口推計系列。違いは2026年。単位欄の記載はなし。
- ②表の題名から読めること：表題「Workforce Projections」。Workforce Projections。
- ③同じ表の列名から読めること：兄弟列は「Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029」。Six_Cities22と2021〜2025、2027〜2029年列の間の2026年系列。
- ④値の形から読めること：値の先頭例「1,235,608.02200 | 908,883.28090 | 617,945.99980 | 2,762,437.30270 | 168,306.25900 | 328,030.50980 | 207,870.90790 | 44,528.80621」。後半の非欠損値は「3,511,173.78561 | 831,581.83090 | 4,342,755.61651」。1,235,608.02200等、後半3,511,173.78561。
- 迷った種類と、それを退けた理由：r0011と同じ（違い：2026年列）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0011と同じ。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0073
- 前回の答えを変えるか：変える（category）。前回unknownからcategoryへ変更。r0038と同じ表構造で、値の違いはcrimeの提示行が全て0。
- 種類：category
- 決め手：値の形
- ①列名・単位の語から読めること：「crime」crime は犯罪件数にも見えるが、兄弟列のtopic flagとして読む。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「issued, administration, agriculture, construction, culture, education, energy, finances, geography」。issued・administration・agriculture・construction・culture・education・energy・finances・geographyとr0038と同じ主題列群。
- ④値の形から読めること：値の例「0 | 0 | 0 | 0 | 0 | 0 | 0 | 0」。提示値は全て0。r0038の同表型financesでは後半に1が出ており、0/1の有無指標と整合。
- 迷った種類と、それを退けた理由：quantityの犯罪件数なら単位・イベント数の文脈が要る。ここは主題タグの有無category。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：主題の0/1フラグはcategory。逮捕件数のような数え上げ犯罪統計はquantity。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

