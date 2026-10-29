# 判断の説明 007 — ChatGPT

## r0001
- 前回の答えを変えるか：変えない。前回はidと判断（決め手：値の形、メモ：BAQUA_TI はモニタリング事業の識別コード。）。
- 種類：id
- 決め手：値の形
- ①列名・単位の語から読めること：「monitoring_program」BAQUA_TI は事業・調査プログラムの略号で、測定項目名ではない。列自体の単位はない。単位欄「unit: CFU/100ml」。
- ②表の題名から読めること：題名情報は提示されていないため、単位欄と観測時系列の構成を補助的に使う。
- ③同じ表の列名から読めること：兄弟列は「station_number, latidude, date_of_probing, parameter_type, value, lower_LOD, unit」。station_number・date_of_probing・parameter_type・value・lower_LOD・unit が並ぶため、monitoring_program は測定系列を特定する軸。CFU/100ml は別の value に付く単位。
- ④値の形から読めること：値の例「BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI | BAQUA_TI」。同じ BAQUA_TI が反復し、1回の測定値ではなく系列の識別コードとして使われている。
- 迷った種類と、それを退けた理由：quantityも考えたが CFU/100ml は値列の単位で、program自体は件数・濃度ではない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：コード表があれば BAQUA_TI の展開名を確認できる。id 判定は高い。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0002
- 前回の答えを変えるか：変えない。前回はunknownと判断（決め手：決められない、メモ：funk と数値だけでは指標・区分・識別子を特定できない。）。
- 種類：unknown
- 決め手：決められない
- ①列名・単位の語から読めること：「funk」funk はドイツ語で機能・無線等の複数の意味があり、この列名だけでは統計量の対象を特定できない。単位なし。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。表題がなく用途が分からない。
- ③同じ表の列名から読めること：兄弟列は「arten, d, f, i, e, model」。arten・d・f・i・e・model も略号や短い列名で、意味を照合できない。
- ④値の形から読めること：値の例「29 | 35 | 5 | 68 | 92」。29・35・5・68・92 は数値だが、件数・コード・スコアのどれとも読める。
- 迷った種類と、それを退けた理由：quantity、id、category が候補だが、見出し・隣列・値のどれにも区別の根拠がない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：データ辞書、表題、単位、funk の展開語のいずれかが必要。
- 規則にするなら（当てはまらない例も）：列名が汎用/略号で、表題・単位・兄弟列・値から対象の意味を一つに絞れないならunknown。単位・辞書・元表の説明が得られた場合にのみ決める。
- 確信：中

## r0003
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：同じ表の列名、メモ：EW_Total_Company の非季節調整済み企業数。）。
- 種類：quantity
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「EW_Total_Company_NSA」NSA は非季節調整値を示し、Company は企業数を表す語。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Period, Year, Quarter, EW_Total_Company_SA, EW_Compulsory_SA, EW_CVL_SA, EW_Admin_SA, EW_CVA_SA, EW_Receiver_SA」。Period・Year・Quarter と、EW_Total_Company_SA / EW_Compulsory_SA 等の並列時系列があり、雇用企業数の系列と読める。
- ④値の形から読めること：値の先頭例「3597 | 3520 | 2553 | 2567 | 5067 | 5615 | 4700 | 5689」。後半の非欠損値は「4948 | 4630 | 3813 | 4409 | 3963 | 5305 | 5405 | 5404」。3597, 3520 等に加え後半も4948, 4630等の整数実績。単なる年度コードではなく系列の値。
- 迷った種類と、それを退けた理由：amountやidでなく、会社の数え上げ。季節調整済みでも量の意味は変わらない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：企業数の定義・単位があれば確認できるが、同じ表の系列構造で十分。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0004
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：見出しの語、メモ：Dwellings value の表における dwelling の戸数。）。
- 種類：quantity
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Dwellings value」Dwellings value は「住宅の価値」とも読めるので列名だけでは曖昧。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Valuation Band  Range, Intervening bands, Tenure Status」。Valuation Band Range・Intervening bands・Tenure Status が並ぶため、評価帯と居住形態ごとの住宅戸数を集計した列と読む。
- ④値の形から読めること：値の先頭例「nil | nil | 82 | nil | 579 | 99 | 354 | 292」。後半の非欠損値は「87 | 53 | 122 | 5 | 41 | 41 | 41 | 61」。nilのほか82, 579, 99等、後半も87, 53, 122等の整数件数。通貨額の小数・通貨記号ではない。
- 迷った種類と、それを退けた理由：amountも検討したが、金額なら評価帯そのものか通貨額が必要。兄弟列とカウント値からquantity。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：列名は曖昧だが、件数であることは表の定義があればさらに確実。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0005
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：見出しの語、メモ：Rank は踏切インベントリの順位。）。
- 種類：category
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Rank」Rank は順位を明示する語。単位欄の記載はなし。
- ②表の題名から読めること：表題「Grade Crossings Inventory」。Grade Crossings Inventory は踏切一覧で、順位付け対象のリスト。
- ③同じ表の列名から読めること：兄弟列は「TC Number, Railway Company, Region, Province, Access, Jurisdiction, Mile, Subdivision, Spur Mile Point」。TC Number・Railway Company・Region・Province・Mile など対象踏切の属性列があり、Rankはその項目群に付く相対順位。
- ④値の形から読めること：値の先頭例「109 | 143 | 168 | 291 | 315 | 338 | 352 | 372」。後半の非欠損値は「376 | 513 | 534 | 550 | 557 | 559 | 753 | 755」。109, 143, 168…から後半376, 513…まで順序尺度の整数。TC Numberのような固有IDとは別。
- 迷った種類と、それを退けた理由：idも候補だが、見出しがRankで対象の順序を表す。quantityの件数ではない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：順位の定義（何を基準に並べたか）が分かれば順位尺度を確認できる。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0006
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：見出しの語、メモ：AnzStand は施設・拠点数を示す。）。
- 種類：quantity
- 決め手：見出しの語
- ①列名・単位の語から読めること：「AnzStand」AnzStand はドイツ語の略で Anzahl Standorte（拠点数）と読む。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。表題はなし。
- ③同じ表の列名から読めること：兄弟列は「KT, Inst, Adr, Ort, KT_Standort, Ort_Standort, LA」。KT・Inst・Adr・Ort・KT_Standort・Ort_Standort・LA と行政地域・機関・所在地の列が並び、各組合せの拠点数の集計と整合する。
- ④値の形から読めること：値の先頭例「1 | 16 | 1 | 15 | 3 | 1 | 1 | 13」。後半の非欠損値は「2 | 2 | 12 | 2 | 22 | 22 | 6 | 5」。1, 16, 1, 15 等、後半にも2, 12, 22, 6などの整数カウント。
- 迷った種類と、それを退けた理由：idも考えたが Standort の参照番号ではなく、Anzahl（数）であり拠点数。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：見出しの展開と表の集計単位が分かれば確定できる。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0007
- 前回の答えを変えるか：変えない。前回はidと判断（決め手：表の題名、メモ：歴史的名称索引の Tree 欄に並ぶ参照番号。）。
- 種類：id
- 決め手：表の題名
- ①列名・単位の語から読めること：「Tree」Tree は単独だと樹木本数にも見える。単位欄の記載はなし。
- ②表の題名から読めること：表題「Ballarat Historical Naming Index」。Ballarat Historical Naming Index は歴史的名称の索引で、Tree は索引内の分類・参照欄。
- ③同じ表の列名から読めること：兄弟列は「Type, Site, Locality, Ward, Authority, See Entry, Not in use, Unknown / uncertain, Beyond Maps」。Type・Site・Locality・Ward・Authority・See Entry 等、名称と参照先の属性が並ぶ。
- ④値の形から読めること：値の例「2519, 3508 | 842 | 553 | 2664, 174」。2519, 3508、842、2664, 174 等の番号は名称索引の参照番号で、樹木の数ではない。
- 迷った種類と、それを退けた理由：quantityも候補だが、題名とSee Entryが示す索引参照を優先。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：個々の番号のリンク先があれば参照キーとさらに確認できる。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0008
- 前回の答えを変えるか：変えない。前回はaccountと判断（決め手：値の形、メモ：Supplier 欄の値は Funding Account という内部会計口座名。）。
- 種類：account
- 決め手：値の形
- ①列名・単位の語から読めること：「Supplier」Supplier は通常仕入先だが、値は TPS – Funding Account 1 という内部会計口座名。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Departmental Family, Entity, Date, Expense type, Expense area, Transaction Number, Amount」。Departmental Family・Entity・Date・Expense type・Expense area・Transaction Number・Amount が並ぶ支出明細。口座名が支払先の法人名とは異なる。
- ④値の形から読めること：値の例「TPS – Funding Account 1 | TPS – Funding Account 1 | TPS – Funding Account 1 | TPS – Funding Account 1 | TPS – Funding Account 2 | TPS – Funding Account 1 | TPS – Funding Account 2 | TPS – Funding Account 2」。TPS – Funding Account 1 が繰り返し、Supplier欄が資金口座を表す。
- 迷った種類と、それを退けた理由：orgも候補だが値は会社・取引先名ではなくFunding Accountという会計口座。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：Supplier欄でも値の実体が組織名ならorgにする。
- 規則にするなら（当てはまらない例も）：列名がsupplierでも値が内部口座・費目・部署を表すならaccount。ただし支払先法人名ならorg。
- 確信：中

## r0009
- 前回の答えを変えるか：変えない。前回はidと判断（決め手：見出しの語、メモ：Control Budget Code は予算区分コード。）。
- 種類：id
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Control Budget Code」Control Budget Code は予算管理コードと明示。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Organisation Code, Organisation, Sub Segment Code, Economic Category Code, Economic Budget Code, PESA Economic Group Code, Version, Year, Quarter」。Organisation Code・Organisation・Sub Segment Code・Economic Category Code 等、同じ表に複数のコード列とその名称列がある。
- ④値の形から読めること：値の例「DEL | DEL | AME | DEL | AME | DEL | DEL | DEL」。DEL・AMEが反復する固定コード。予算区分をコードで参照し、数値測定値ではない。
- 迷った種類と、それを退けた理由：categoryとも迷うが、Code列でコード値を持つため、記述名/説明列と分けてid。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：コードの説明列があればDEL/AMEの指す区分を確認できる。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0010
- 前回の答えを変えるか：変えない。前回はidと判断（決め手：値の形、メモ：Body の値は機関を指す統計 URI。）。
- 種類：id
- 決め手：値の形
- ①列名・単位の語から読めること：「Body」Body は支出記録の主体を指す列。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Date, Transaction Number, Amount, Supplier ID, Expense Area, Expense Type, Expense Code, Service Code, Service Label」。Date・Transaction Number・Amount・Supplier ID・Expense Area/Type/Code・Service Code が並び、Bodyは支出主体の参照属性。
- ④値の形から読めること：値の例「http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/… | http://statistics.data.gov.uk/…」。statistics.data.gov.uk のURIが値で、行の機関リソースを指す。単なるWebリンクではない。
- 迷った種類と、それを退けた理由：orgは機関名の列に使う。これは実名でなく機関リソースURIなのでid。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：URIの末尾と公開データ辞書で参照対象を確認できる。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0011
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Workforce Projections の就業人口推計値。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Emp_Wkf_POPD_15+yrs_2025」Emp_Wkf_POPD_15+yrs_2025 は15歳以上の就業人口推計系列を表す変数名。単位欄の記載はなし。
- ②表の題名から読めること：表題「Workforce Projections」。Workforce Projections とあり、労働人口の予測表。
- ③同じ表の列名から読めること：兄弟列は「Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029」。2021〜2029年の同系列列と Six_Cities22 が並び、年ごとの人口推計である。
- ④値の形から読めること：値の先頭例「1,227,114.17300 | 894,414.05980 | 609,571.58220 | 2,731,099.81500 | 167,351.77280 | 324,530.32080 | 205,582.51470 | 44,294.62793」。後半の非欠損値は「3,472,859.05123 | 829,849.02260 | 4,302,708.07383」。1,227,114.17300等の大きな小数は推計計算の精度を示す。人口人数の集計規模。
- 迷った種類と、それを退けた理由：amount/ rateではなく就業者数。小数表記でも値の意味は人数。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：人口の実測・推計値はquantity。率なら列名にemployment rateや%の手掛かりが要る。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0012
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Workforce Projections の就業人口推計値。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Emp_Wkf_POPD_15+yrs_2029」r0011と同じ系列名。違いは2029年の予測列。単位欄の記載はなし。
- ②表の題名から読めること：表題「Workforce Projections」。Workforce Projections の年次推計という文脈はr0011と同じ。
- ③同じ表の列名から読めること：兄弟列は「Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028」。同じ表の2021〜2028年列とSix_Cities22が並ぶ。r0011と同じ軸。
- ④値の形から読めること：値の先頭例「1,278,131.66100 | 963,977.38350 | 651,945.91510 | 2,894,054.95960 | 173,273.05480 | 341,466.13440 | 217,865.96360 | 45,579.74043」。後半の非欠損値は「3,672,239.85283 | 847,353.49270 | 4,519,593.34553」。1,278,131.66100等、後半3,672,239.85283など。r0011との差は対象年で、値は人口規模の推計。
- 迷った種類と、それを退けた理由：r0011と同じ（違い：2029年列の値）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：同じ表・同じ指標系列のためr0011と同じ確信。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0013
- 前回の答えを変えるか：変えない。前回はidと判断（決め手：見出しの語、メモ：bath 内の位置番号で、実験対象を区別する値。）。
- 種類：id
- 決め手：見出しの語
- ①列名・単位の語から読めること：「bathPosition」bathPosition は実験浴槽内の位置番号を指す。単位欄の記載はなし。
- ②表の題名から読めること：表題「Reducing pest risk in birch wood products - The effective heat treatme…」。白樺材の加熱処理による害虫リスク低減実験。
- ③同じ表の列名から読めること：兄弟列は「treeLocation, batch, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, vialPosition, replicate」。treeLocation・batch・treeSpecies・experimentNumber・treeNumber・boltNumber・corkNumber・vialPosition・replicate 等、実験対象と配置のキーが並ぶ。
- ④値の形から読めること：値の先頭例「4 | 9 | NA | 16 | 18 | NA | NA | NA」。後半の非欠損値は「17 | 12 | 22 | 21」。4, 9, 16, 18に加え17, 12, 22等。NAもあり、各試料の配置位置値。
- 迷った種類と、それを退けた理由：quantityの位置数ではなく各試料が置かれた場所番号。空間座標ではなく実験内の識別値。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：実験配置図があれば位置番号の役割を確かめられる。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0014
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：見出しの語、メモ：Service_FR はサービス種別の固定語彙。）。
- 種類：category
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Service_FR」Service_FR はフランス語のサービス名・サービス区分を表す。単位欄の記載はなし。
- ②表の題名から読めること：表題「Enterprise Service Model Consumption Actuals」。Enterprise Service Model Consumption Actuals はサービス利用実績の表。
- ③同じ表の列名から読めること：兄弟列は「Department_EN, Department_FR, Service_EN, Value, Date_Captured」。Department_EN/FR、Service_EN、Value、Date_Captured があり、Service_FR は英語列と対になるフランス語の分類値。
- ④値の形から読めること：値の先頭例「Téléphonie - Fixe et Mobile | Accès à distance protégé | Téléphonie - Fixe et Mobile | Téléphonie - Fixe et Mobile | Téléphonie - Fixe et Mobile | Gestion des justificatifs inte… | Téléphonie - Fixe et Mobile | Conférence」。後半の非欠損値は「Courriel」。Téléphonie - Fixe et Mobile、Accès à distance protégé、Courriel 等のサービス語が並ぶ。
- 迷った種類と、それを退けた理由：textも考えたが、対応するService_ENと固定サービス一覧の値であり、自由記述ではない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：他言語の対応列と一緒に固定語彙をcategoryとする。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0015
- 前回の答えを変えるか：変えない。前回はrateと判断（決め手：見出しの語、メモ：vj_rel_kumsum は前年比の相対累積変化率。）。
- 種類：rate
- 決め手：見出しの語
- ①列名・単位の語から読めること：「vj_rel_kumsum」vj_rel_kumsum はドイツ語略号の相対累積前年差と読む（vj=Vorjahr、rel=相対、kumsum=累積和）。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「jahr, quartal, branchen, n, kumsum, vj_abs_n, vj_rel_n, vj_abs_kumsum」。jahr・quartal・branchen・n・kumsum・vj_abs_n・vj_rel_n・vj_abs_kumsum が並び、nと累積値に対する前年差の率/実数を分けている。
- ④値の形から読めること：値の先頭例「NA | NA | NA | NA | 0.0369630369630369 | 0.0329865516366405 | 0.0265224219158959 | -0.0110789980732178」。後半の非欠損値は「0.158341658341658 | 0.00323415265200522 | 0.0384615384615385 | 0.0436277670320224 | 0.0459845984598459 | 0.021223470661673 | 0.0115321252059308 | 0.0200423429781227」。0.03696等の小数と後半0.15834等。相対変化率の値。
- 迷った種類と、それを退けた理由：quantityは絶対差の列（vj_abs_kumsum）に対応。relativeとあるためrate。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：rel/absを区別し、相対変化はrate、絶対件数差はquantityにする。
- 規則にするなら（当てはまらない例も）：値が相対比・割合・率を示すならrate。絶対数や金額を記録する列はquantity/amount。
- 確信：中

## r0016
- 前回の答えを変えるか：変えない。前回はidと判断（決め手：見出しの語、メモ：replicate は実験反復を区別する番号。）。
- 種類：id
- 決め手：見出しの語
- ①列名・単位の語から読めること：「replicate」replicate は実験の反復番号を示す。単位欄の記載はなし。
- ②表の題名から読めること：表題「Reducing pest risk in birch wood products - The effective heat treatme…」。加熱処理実験の表。
- ③同じ表の列名から読めること：兄弟列は「treeLocation, batch, treeSpecies, experimentNumber, treeNumber, boltNumber, corkNumber, bathPosition, vialPosition」。experimentNumber・treeNumber・boltNumber・bathPosition・vialPosition と試料設計の識別軸が並ぶ。
- ④値の形から読めること：値の先頭例「13 | 20 | 5 | 16 | 23 | 1 | 13 | 16」。後半の非欠損値は「17 | 10 | 9 | 11 | 10 | 2 | 17 | 14」。13, 20, 5, 16, 23等、後半にも17, 10, 9などの個別反復番号。
- 迷った種類と、それを退けた理由：quantity（反復回数）ではなく各行の反復試料の番号。総反復回数ならquantity。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：列が各反復の識別値ならid、反復数を集計した列ならquantity。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0017
- 前回の答えを変えるか：変える（id）。前回はunknown。Versichererは保険者を示し、兄弟列のDurchschnittsbestandが平均保有数を別に持つ。先頭・後半の整数値は保険者コードと読むのが妥当と判断した。
- 種類：id
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「Versicherer」Versicherer は保険者（保険会社）を意味し、数量名ではない。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。表題なし。
- ③同じ表の列名から読めること：兄弟列は「Kanton, Geschaftsjahr, Durchschnittsbestand」。Kanton・Geschäftsjahr・Durchschnittsbestand（平均保有数）が並び、保険者別・州別・会計年度別の平均を集計している。Versichererは主体を指定する軸。
- ④値の形から読めること：値の先頭例「57 | 62 | 134 | 246 | 343 | 360 | 376 | 455」。後半の非欠損値は「774 | 829 | 881 | 994 | 1386 | 1479 | 1507 | 1509」。57, 62, 134…から774, 829, 1509等のコード風整数。測定値の範囲より insurer identifier と読むのが妥当。
- 迷った種類と、それを退けた理由：quantityの平均保有数は別列。ここは保険者を識別する数値コードなのでid。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：保険者コード表か別名列があれば照合できるため確信は中。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0018
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：National Sheep Census の羊・群れの頭数。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「TOTAL_SHEEP_MOUNTAIN」TOTAL_SHEEP_MOUNTAIN はMountain sheepの総数を示す変数名。単位欄の記載はなし。
- ②表の題名から読めること：表題「DAFM National Sheep Census 2020」。DAFM National Sheep Census 2020 は羊の国勢調査。
- ③同じ表の列名から読めること：兄弟列は「COUNTY, CENSUS_YEAR, NO_OF_HERD_NUMBERS, FLOCKS_WITH_SHEEP_IND, FLOCKS_WITH_TOTAL_SHEEP_CALC, BREEDING_EWES_TOTAL, BREEDING_RAMS_TOTAL, OTHER_SHEEP_TOTAL, TOTAL_SHEEP_CALC」。COUNTY・CENSUS_YEAR・NO_OF_HERD_NUMBERS・BREEDING_EWES_TOTAL等、地域・年・群れ・羊頭数が並ぶ。
- ④値の形から読めること：値の先頭例「13028 | 10984 | 1316 | 59191 | 196521 | 6312 | 105879 | 183200」。後半の非欠損値は「4496 | 36649 | 1985 | 12707 | 223575 | 2167 | 8363 | 47578」。13,028から196,521、後半223,575等の大きな整数。全頭数の集計。
- 迷った種類と、それを退けた理由：idではなく頭数。品種コードのような識別値でもない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：家畜の頭数・群れ数はquantity。品種名や識別番号は別ラベル。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0019
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：同じ表の列名、メモ：Age の 0-64 は年齢階級。）。
- 種類：category
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「Age」Age の値は年齢そのものではなく年齢帯。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Year, Week, Ending, NoDeaths_EP, Expected, LowerB, UpperB, Diff」。Year・Week・Ending・NoDeaths_EP・Expected・LowerB・UpperB・Diff の死亡統計に年齢階級が付く。
- ④値の形から読めること：値の例「0-64 | 0-64 | 0-64 | 0-64 | 0-64 | 0-64 | 0-64 | 0-64」。0-64が反復。連続した年齢の実数ではなく二つの年齢区分。
- 迷った種類と、それを退けた理由：quantity（年齢）ではなく複数年齢をまとめた区分なのでcategory。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：年齢階級はcategory、具体的な年齢値や人数はquantity。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0020
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：見出しの語、メモ：vj_abs_kumsum は件数 n の累積差。）。
- 種類：quantity
- 決め手：見出しの語
- ①列名・単位の語から読めること：「vj_abs_kumsum」vj_abs_kumsum は絶対値の累積前年差と読む。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「jahr, quartal, branchen, n, kumsum, vj_abs_n, vj_rel_n, vj_rel_kumsum」。jahr・quartal・branchen・n・kumsum・vj_abs_n・vj_rel_n・vj_abs_kumsum・vj_rel_kumsum と、絶対/相対や単年/累積を対比する。
- ④値の形から読めること：値の先頭例「NA | NA | NA | NA | 74 | 130 | 152 | -23」。後半の非欠損値は「634 | 15 | 89 | 203 | 418 | 51 | 56 | 142」。74, 130, 152, -23など整数。後半634,15,89等も絶対差の量。
- 迷った種類と、それを退けた理由：rateはvj_rel_kumsum側。絶対件数の累積差なのでquantity。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：絶対件数や件数差はquantity、相対差はrate。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0021
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Material Footprint の金属鉱石量。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Metal ores」Metal ores は鉱石という材料の構成量。単位欄の記載はなし。
- ②表の題名から読めること：表題「Material Footprint for Australia」。Material Footprint for Australia は材料フットプリントの年次集計。
- ③同じ表の列名から読めること：兄弟列は「Product, Biomass, Fossil fuels, Non-metallic minerals, Total (All categories)」。Product・Biomass・Fossil fuels・Non-metallic minerals・Total が同じ材料区分として並ぶ。
- ④値の形から読めること：値の先頭例「234140400 | 217336500 | 225465800 | 253387400 | 254395200 | 257881300 | 256568800 | 241431400」。後半の非欠損値は「254128800 | 254251100 | 273260400 | 261005500 | 264220400 | 238106600 | 264054300 | 256022700」。234,140,400等の大きな値と後半264,220,400等。鉱石の物質量で金額通貨ではない。
- 迷った種類と、それを退けた理由：otherも候補だが、この表の量の構成要素で、材料フローの絶対量。面積・温度などの属性値ではない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：物質フローの材料量はquantity。材料の評価額を通貨で示す場合はamount。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0022
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Individual Tax Statistics の全申告件数。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Total - All Returns /Total - Toutes les declarations」Total - All Returns は全申告数を示す語。単位欄の記載はなし。
- ②表の題名から読めること：表題「Individual Tax Statistics by Area (ITSA) (2022 Tax Year)」。Individual Tax Statistics by Area (ITSA) (2022 Tax Year) は税申告統計。
- ③同じ表の列名から読めること：兄弟列は「Prov/Terr, CMA-CA/RMR-AR, Classification, Total Income / Revenu total, Under $5,000 / Moins de 5 000 …, $5,000 to $9,999 / 5 000 $ a  …, $10,000 to $14,999 / 10 000 $ …, $15,000 to $19,999 / 15 000 $ …, $20,000 to $24,999 / 20 000 $ …」。Prov/Terr・CMA/CA・Classification・Total Income・所得帯ごとの申告数が並び、総件数列と所得額列を対比できる。
- ④値の形から読めること：値の先頭例「85540 | 132900 | 88150 | 135920 | 136280 | 25200 | 13210 | 29660」。後半の非欠損値は「27250 | 104040 | 331810 | 17630 | 65030 | 55250 | 13120 | 49280」。85,540や132,900など整数。後半27250,104040等も件数規模。
- 迷った種類と、それを退けた理由：amountはTotal Incomeの列。ここはreturns（申告）の件数でquantity。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：申告・応募・取引の件数を表すTotalはquantity。通貨額の合計はamount。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0023
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：見出しの語、メモ：vj_abs_n は件数 n の前年比差。）。
- 種類：quantity
- 決め手：見出しの語
- ①列名・単位の語から読めること：「vj_abs_n」vj_abs_n は前年比の絶対差（abs）を件数nに対して示すと読める。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「jahr, quartal, branchen, n, kumsum, vj_rel_n, vj_abs_kumsum, vj_rel_kumsum」。n・vj_rel_n・vj_abs_kumsum・vj_rel_kumsum が並び、nの絶対差と相対差を分ける。
- ④値の形から読めること：値の先頭例「NA | NA | NA | NA | 74 | 56 | 22 | -23」。後半の非欠損値は「317 | 71 | 89 | 114 | 194 | 51 | 5 | 86」。74,56,22,-23等の整数差で、後半317,71等。
- 迷った種類と、それを退けた理由：rateはvj_rel_n。実数の差なのでquantity。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：絶対差はquantity、相対変化率はrate。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0024
- 前回の答えを変えるか：変える（category）。前回のunknownからcategoryへ変更。兄弟列群の構造とr0038に出る1を合わせて、テーマフラグと判断。
- 種類：category
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「energy」energyは資源量や電力量にも見えるが、この列の値は実測単位を伴わない。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「issued, administration, agriculture, construction, crime, culture, education, finances, geography」。issued・administration・agriculture・construction・crime・culture・education・finances・geographyと同じ主題別列群。r0038 financesでは0/1の値が見える。
- ④値の形から読めること：値の例「0 | 0 | 0 | 0 | 0 | 0 | 0 | 0」。提示値はすべて0。単独なら不明だが、同じ主題群のfinance等と同型で、対象テーマの有無を示すフラグと読む。
- 迷った種類と、それを退けた理由：quantityのエネルギー量なら単位/数値規模が必要。ここはテーマ名を列ごとに分けた0/1指標なのでcategory。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：同じ表の主題列が0/1で有無を示すならcategory。ただしkWh等の測定単位があるenergyはquantity。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0025
- 前回の答えを変えるか：変えない。前回はidと判断（決め手：値の形、メモ：C01・D02 は援助種別の分類コード。）。
- 種類：id
- 決め手：値の形
- ①列名・単位の語から読めること：「Type of Aid」Type of Aid は援助種別、値はC01/D02/A01形式のコード。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Extending Agency, Donor Project Number, Project Title, Nature of Submission, Benefitting Country Code, Input Sector code, Channel of Delivery Code, Type of Flow, Type of Finance」。Extending Agency・Donor Project Number・Project Title・Benefitting Country Code・Input Sector 等、援助案件の種類と参照コードを並べる。
- ④値の形から読めること：値の先頭例「C01 | C01 | C01 | C01 | C01 | D02 | C01 | C01」。後半の非欠損値は「A01」。C01が反復しD02/A01もある。援助分類体系のコード値。
- 迷った種類と、それを退けた理由：categoryも候補だが、コード形式で分類体系を参照する値。説明語の列ならcategory。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：援助コード表があれば各コードの説明を確かめられる。
- 規則にするなら（当てはまらない例も）：列名が番号・code・referenceを示し、値が対象やコード体系を参照するならid。ただし住所を構成する郵便番号・国コードや、意味自体が区分のコードはガイドの例に従う。
- 確信：中

## r0026
- 前回の答えを変えるか：変える（amount）。前回unknownからamountへ変更。Beschluss・ID・status・日付との並びでNachgefragtを申請額と判断。
- 種類：amount
- 決め手：同じ表の列名
- ①列名・単位の語から読めること：「Nachgefragt」Nachgefragt はドイツ語で申請・要求された額という意味に読める。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「Kategorie, Sparte, Beschluss, Status, Eingangsdatum, Beschlussdatum, ID」。Kategorie・Sparte・Beschluss・Status・Eingangsdatum・Beschlussdatumに加えて独立IDがある。申請額と決定額の対。
- ④値の形から読めること：値の先頭例「16100 | 8100 | 902600 | 22500 | 2500 | 20900 | 20000 | 12400」。後半の非欠損値は「4500 | 13900 | 1879500 | 1400 | 18500 | 415300 | 15600 | 19600」。16,100・902,600等、後半に1,879,500など金額らしい値。IDは別列。
- 迷った種類と、それを退けた理由：quantityの件数ではなく、要求額と決定額の組。通貨単位は未表示なので確信は中。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：申請額と決定額が別列に並ぶ金銭表ならamount。単位がなければ通貨・辞書で照合する。
- 規則にするなら（当てはまらない例も）：列名・対になる項目・表の文脈が申請額/決定額等の通貨価値を示すならamount。ただし件数はquantity、参照番号はid。
- 確信：中

## r0027
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：表の題名、メモ：レッドリストの分類群（鳥の目）の区分値。）。
- 種類：category
- 決め手：表の題名
- ①列名・単位の語から読めること：「5」見出し「5」は単独では意味がない。単位欄の記載はなし。
- ②表の題名から読めること：表題「レッドリスト/レッドデータブック_第５次レッドリスト」。レッドリスト/レッドデータブック第5次の分類表。
- ③同じ表の列名から読めること：兄弟列は「1, 2, 3, 4, 6, 7, 8, 9, 10」。列名1,2,3,4,6,7,8,9,10が同じ分類レベルの列で、鳥の分類群を順に収める。
- ④値の形から読めること：値の先頭例「ツル目 | チドリ目 | ペリカン目 | スズメ目 | チドリ目 | チドリ目 | スズメ目 | スズメ目」。後半の非欠損値は「ネッタイチョウ目 | ミズナギドリ目 | ハト目 | カイツブリ目 | キツツキ目」。ツル目・チドリ目・ペリカン目など分類群の名前。後半も鳥類の目の名称。
- 迷った種類と、それを退けた理由：idではなく鳥類の分類名で、順位や件数でもない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：番号だけの列は表題・隣の分類列と値の意味で判断する。分類名ならcategory。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0028
- 前回の答えを変えるか：変えない。前回はotherと判断（決め手：値の形、メモ：値はデジタルプラットフォームのドメイン名・URL。）。
- 種類：other
- 決め手：値の形
- ①列名・単位の語から読めること：「digital_platform」digital_platform の値はプラットフォームのドメイン/URL。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「library_call_number, digital_reproduction, title, place_of_publication_or_produc…, date_of_publication_or_product…, date_of_publication_or_product…, series, digital_reproduction_copyright, digital_object_identifier」。library_call_number・digital_reproduction・title・place_of_publication_or_production・date...と資料メタデータが並び、値は資料そのものの組織名でなくアクセス先ドメイン。
- ④値の形から読めること：値の例「e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch | e-manuscripta.ch」。e-manuscripta.ch等のドメインが反復。Webリンクの形。
- 迷った種類と、それを退けた理由：orgも候補だがこれは会社名でなくURL/ドメイン。idは個別リソースURIではなくサイトの入口。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：一般Web URLはother。/id/ の組織リソースURIならid。
- 規則にするなら（当てはまらない例も）：値がURL・科学名・温度・濃度などguideでotherと定義された属性ならother。ただし/id/の組織URIはid。
- 確信：中

## r0029
- 前回の答えを変えるか：変えない。前回はcategoryと判断（決め手：見出しの語、メモ：AGE の Y75T79 などは年齢階級コード。）。
- 種類：category
- 決め手：見出しの語
- ①列名・単位の語から読めること：「AGE」AGE は年齢の軸だが、Y75T79やY5T9は年齢階級コード。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「TIME_PERIOD, GEO, SEX, OBS_STATUS, OBS_VALUE」。TIME_PERIOD・GEO・SEX・OBS_STATUS・OBS_VALUEと並ぶ統計分類軸。
- ④値の形から読めること：値の先頭例「Y75T79 | _T | Y85T89 | Y5T9 | Y45T49 | Y20T24 | Y45T49 | _T」。後半の非欠損値は「Y40T44 | Y55T59 | Y10T14 | Y55T59 | Y50T54 | Y30T34 | Y80T84 | Y0T4」。Y75T79・Y5T9・_T等、年齢帯を表す標準コード。
- 迷った種類と、それを退けた理由：quantityの実年齢でなく、年齢層のカテゴリ値。コードは層を符号化している。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：年齢階級コードはcategory、単独の年齢や人口数はquantity。
- 規則にするなら（当てはまらない例も）：値が固定された種別・状態・年齢帯・テーマの有無・順位区分ならcategory。ただし項目を一意に参照するコードはid、自由記述はtext。
- 確信：中

## r0030
- 前回の答えを変えるか：変えない。前回はunknownと判断（決め手：決められない、メモ：時間帯ごとの数値だが、測定対象も単位も示されない。）。
- 種類：unknown
- 決め手：決められない
- ①列名・単位の語から読めること：「01:30」01:30 は時刻ラベルで、列の値そのものは測定された数値。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。表題なし。
- ③同じ表の列名から読めること：兄弟列は「DATE, 00:00, 00:30, 01:00, 02:00, 02:30, 03:00, 03:30, 04:00」。DATEと00:00・00:30・01:00・02:00など30分刻みの列が並び、時刻別観測値の一列。対象指標名がない。
- ④値の形から読めること：値の先頭例「97 | 96 | 52 | 92 | 93 | 95 | 96 | 97」。後半の非欠損値は「99 | 98 | 106 | 104 | 106 | 100 | 94 | 123」。97, 96, 52, 92等の数値、後半99〜123。単位・何を計っているかは不明。
- 迷った種類と、それを退けた理由：dateではない（暦の時点でなく、その時間の測定値）。quantity/otherの別を決める対象・単位がない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：行名・表題・単位のどれか、例えば水位・人数・温度の説明が必要。
- 規則にするなら（当てはまらない例も）：列名が汎用/略号で、表題・単位・兄弟列・値から対象の意味を一つに絞れないならunknown。単位・辞書・元表の説明が得られた場合にのみ決める。
- 確信：中

## r0031
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：見出しの語、メモ：kumsum は件数 n の累積合計。）。
- 種類：quantity
- 決め手：見出しの語
- ①列名・単位の語から読めること：「kumsum」kumsum はドイツ語圏統計でkumulative Summe（累積合計）の略。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「jahr, quartal, branchen, n, vj_abs_n, vj_rel_n, vj_abs_kumsum, vj_rel_kumsum」。jahr・quartal・branchen・n・vj_abs_n等、件数nとその累積・前年差の系列が並ぶ。
- ④値の形から読めること：値の先頭例「2002 | 3941 | 3941 | 5731 | 2076 | 4071 | 5883 | 2053」。後半の非欠損値は「4638 | 4653 | 2403 | 4856 | 9508 | 2454 | 4912 | 7227」。2002, 3941, 5731等の非負整数で、後半4638〜9508。累積件数の規模。
- 迷った種類と、それを退けた理由：idではなく集計された累積量。率ならvj_rel_*の列。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：件数nの累積和はquantity。比率の累積変化はrate。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0032
- 前回の答えを変えるか：変えない。前回はaddressと判断（決め手：表の題名、メモ：保護構造物一覧の建物・場所の名称。）。
- 種類：address
- 決め手：表の題名
- ①列名・単位の語から読めること：「Structure」Structure は構造物・建物を表す。単位欄の記載はなし。
- ②表の題名から読めること：表題「Protected Structures Wicklow Rathnew (CDP 2022 - 2028)」。Protected Structures Wicklow Rathnew は保護対象の建造物一覧。
- ③同じ表の列名から読めること：兄弟列は「X, Y, ID, RPS_Number, Location, OBJECTID」。X・Y・ID・RPS_Number・Location・OBJECTIDがあり、Structureは座標や登録番号が別に付く対象物の名称。
- ④値の形から読めること：値の先頭例「Church - Parochial Hall | Lifeboat House -The Comhaltas … | Anchor | The Handball Alley | Grimshaw’s Lodge, | Ruin of The Cholera House, | Signal room and waiting room o… | Saint Nathi’s / Round Mount」。後半の非欠損値は「Graveyard | Doorcase | Church | Abbey ruin | The Bridge Tavern, Public Hous… | Gaol | Chapel | Letter box」。Church - Parochial Hall、Lifeboat House、The Handball Alley、後半Graveyard・Abbey ruin等、場所/構造物の名称。
- 迷った種類と、それを退けた理由：textも考えたが、自由な説明文でなく保護対象の場所・建造物を命名する欄。種類名と固有名が混ざるため確信は中。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：建物・土地・史跡の名称はaddress。ただし美術品等の異種文化財が混ざり場所を指さないならunknown。
- 規則にするなら（当てはまらない例も）：値が住所・場所・建物・停留所等の場所名称を指すならaddress。ただし組織名はorg、住所とは別の参照コードはid。
- 確信：中

## r0033
- 前回の答えを変えるか：変えない。前回はrateと判断（決め手：見出しの語、メモ：vj_rel_n は n の前年比相対変化率。）。
- 種類：rate
- 決め手：見出しの語
- ①列名・単位の語から読めること：「vj_rel_n」vj_rel_n は前年比の相対変化率（rel）をnに対して示す。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「jahr, quartal, branchen, n, kumsum, vj_abs_n, vj_abs_kumsum, vj_rel_kumsum」。jahr・quartal・branchen・n・vj_abs_n・vj_abs_kumsum・vj_rel_kumsumの対照から、relは絶対件数でない。
- ④値の形から読めること：値の先頭例「NA | NA | NA | NA | 0.0369630369630369 | 0.0288808664259927 | 0.012290502793296 | -0.0110789980732178」。後半の非欠損値は「0.162480779087647 | 0.031305114638448 | 0.0384615384615385 | 0.0487387772552372 | 0.0870345446388514 | 0.021223470661673 | 0.00203832042397067 | 0.0385823239120682」。0.0369・0.0288・0.01229等の小数、後半0.16248等。割合の尺度。
- 迷った種類と、それを退けた理由：quantityの件数差はvj_abs_n。相対的な変化なのでrate。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：相対変化・割合はrate、絶対差や件数はquantity。
- 規則にするなら（当てはまらない例も）：値が相対比・割合・率を示すならrate。絶対数や金額を記録する列はquantity/amount。
- 確信：中

## r0034
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Workforce Projections の就業人口推計値。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Emp_Wkf_POPD_15+yrs_2027」r0011と同じEmp_Wkf_POPD_15+yrs系列。違いは2027年。単位欄の記載はなし。
- ②表の題名から読めること：表題「Workforce Projections」。Workforce Projections。
- ③同じ表の列名から読めること：兄弟列は「Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2023, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029」。同じSix_Cities22と2021〜2029年列。
- ④値の形から読めること：値の先頭例「1,249,173.48000 | 927,782.30500 | 629,413.12760 | 2,806,368.91260 | 169,894.80070 | 332,610.99360 | 210,939.51460 | 44,870.87752」。後半の非欠損値は「3,564,685.09902 | 836,008.01070 | 4,400,693.10972」。1,249,173.48000等、後半3,564,685.09902など。年次人口推計。
- 迷った種類と、それを退けた理由：r0011と同じ（違い：2027年列の推計値）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0011と同じ根拠。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

## r0035
- 前回の答えを変えるか：変えない。前回はtextと判断（決め手：見出しの語、メモ：Widmung は書物に記された自由形式の献辞。）。
- 種類：text
- 決め手：見出しの語
- ①列名・単位の語から読めること：「Widmung」Widmung はドイツ語で献辞・贈呈文。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「ID, Signatur, AutorIn, Titel, Ort, Datierung_von, Datierung_bis, Datierung_Bemerkung, Illustration」。ID・Signatur・AutorIn・Titel・Ort・Datierung_von/bis・Datierung_Bemerkung等の蔵書・書誌記録の一部。
- ④値の形から読めること：値の例「'In segno di alta stima, e Con…」。'In segno di alta stima…' のような自由な献辞文。
- 迷った種類と、それを退けた理由：dateやidではなく、資料に記された文章そのもの。固定選択肢でもない。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：自由記述の献辞・注記はtext。決まった種別語の列ならcategory。
- 規則にするなら（当てはまらない例も）：値が自由な題名・注記・文書名ならtext。ただし固定された型/選択肢はcategory、日時はdate。
- 確信：中

## r0036
- 前回の答えを変えるか：変えない。前回はunknownと判断（決め手：決められない、メモ：時刻別の数値だが測定対象・単位が示されない。）。
- 種類：unknown
- 決め手：決められない
- ①列名・単位の語から読めること：「03:00」03:00は列見出しの観測時刻。単位欄の記載はなし。
- ②表の題名から読めること：題名は示されていない。題名なし。
- ③同じ表の列名から読めること：兄弟列は「DATE, 00:00, 00:30, 01:00, 01:30, 02:00, 02:30, 03:30, 04:00」。DATEと00:00、00:30、01:00、01:30、02:00、02:30、03:30、04:00があり、r0030と同じ時間帯系列。
- ④値の形から読めること：値の先頭例「97 | 108 | 58 | 94 | 98 | 94 | 95 | 117」。後半の非欠損値は「99 | 106 | 96 | 111 | 96 | 93 | 92 | 96」。97,108,58,94等、後半99,106,96…の測定値。対象・単位はない。
- 迷った種類と、それを退けた理由：r0030と同じ（違い：03:00の列で、値は97〜117等）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0030と同じ。
- 規則にするなら（当てはまらない例も）：列名が汎用/略号で、表題・単位・兄弟列・値から対象の意味を一つに絞れないならunknown。単位・辞書・元表の説明が得られた場合にのみ決める。
- 確信：中

## r0037
- 前回の答えを変えるか：変えない。前回はquantityと判断（決め手：表の題名、メモ：Workforce Projections の就業人口推計値。）。
- 種類：quantity
- 決め手：表の題名
- ①列名・単位の語から読めること：「Emp_Wkf_POPD_15+yrs_2023」r0011と同じ15歳以上の就業人口推計列。違いは2023年。単位欄の記載はなし。
- ②表の題名から読めること：表題「Workforce Projections」。Workforce Projections。
- ③同じ表の列名から読めること：兄弟列は「Six_Cities22, Emp_Wkf_POPD_15+yrs_2021, Emp_Wkf_POPD_15+yrs_2022, Emp_Wkf_POPD_15+yrs_2024, Emp_Wkf_POPD_15+yrs_2025, Emp_Wkf_POPD_15+yrs_2026, Emp_Wkf_POPD_15+yrs_2027, Emp_Wkf_POPD_15+yrs_2028, Emp_Wkf_POPD_15+yrs_2029」。Six_Cities22と2021、2022、2024〜2029年の兄弟列が並び、2023年列が欠けている。
- ④値の形から読めること：値の先頭例「1,242,188.46500 | 850,937.51060 | 583,815.02590 | 2,676,941.00150 | 156,672.76460 | 318,318.66920 | 212,785.51820 | 44,370.78162」。後半の非欠損値は「3,409,088.73512 | 807,299.11440 | 4,216,387.84952」。1,242,188.46500等、後半3,409,088.73512など。
- 迷った種類と、それを退けた理由：r0011と同じ（違い：2023年の推計値）。
- 自信が低い・決められないなら、その理由と、何があれば決められたか：r0011と同じ。
- 規則にするなら（当てはまらない例も）：列名と表の文脈が個数・人数・件数・時間長・物質量等の数えられる量を示すならquantity。ただし通貨額はamount、割合はrate、温度/濃度等はother。
- 確信：中

