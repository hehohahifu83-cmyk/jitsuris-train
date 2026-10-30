# 本体の中で近い教材の列（`research/unknown/embed_read.py`。もとは `embed_nn.json`）

- 本体 C2 種子 1 の分類の最後の層への入力で近い教材の列（余弦）。teacher＝教材の種類、model＝本体がその教材の列に付ける答え。教材 48215 列、7440.6 秒

| 分け | 列 |
|---|---:|
| A 近い教材の多く（5 列以上）に本体の答えと同じ種類が付いている＝その教材から覚えた | 66 |
| B 近い教材の多くは正解の種類なのに、本体は別の種類と答えた | 5 |
| C 近い教材は割れていて、本体の答えの種類も混ざる | 2 |

## A の列で、本体の答えと同じ種類が付いていた近い教材の出どころ

| 出どころ | 列（延べ） |
|---|---:|
| g | 100 |
| b2 | 90 |
| b | 50 |
| syn | 42 |
| b013 | 38 |
| b014 | 37 |
| b012 | 36 |
| b006 | 35 |
| b011 | 34 |
| b009 | 25 |
| b008 | 24 |
| b010 | 16 |
| b005 | 15 |
| b007 | 9 |
| b003 | 6 |
| b004 | 4 |
| j | 4 |
| b002 | 1 |
| b001 | 1 |

| 分け | id | 見出し | 正解 | 本体 | 近い 10 列の種類 | いちばん近い 3 列（出どころ・列名・種類・近さ） |
|---|---|---|---|---|---|---|
| A | b015-0007 | Tree | id | other | other 9, quantity 1 | g oldalSzam=other 0.913; g volume=other 0.903; b011 dbh=other 0.9 |
| A | b015-0063 | Sexual violence ('000) | quantity | rate | rate 5, quantity 4, other 1 | b009 抽出件数(%)=rate 0.933; b003 女=quantity 0.92; b010 VALUE=rate 0.918 |
| A | b015-0066 | Biomass | quantity | other | other 9, category 1 | b006 awater20=other 0.895; b2 total_floor_area_known=category 0.878; g 総観場3=other 0.877 |
| A | b015-0067 | Fossil fuels | quantity | amount | amount 8, quantity 2 | b Australian Sourced Goo=amount 0.894; b Overseas Sourced Goods=amount 0.856; b value_fte=quantity 0.855 |
| A | b015-0068 | Metal ores | quantity | other | other 9, quantity 1 | b006 awater20=other 0.92; b2 Volume (MCF)=quantity 0.907; g oldalSzam=other 0.901 |
| A | b015-0069 | Non-metallic minerals | quantity | other | other 9, quantity 1 | b006 awater20=other 0.921; g oldalSzam=other 0.919; b2 Volume (MCF)=quantity 0.915 |
| A | b015-0070 | Total (All categories) | quantity | amount | amount 10 | syn =amount 0.95; syn =amount 0.944; b006 非分割=amount 0.933 |
| A | b015-0082 | Emp_Wkf_POPD_15+yrs_2021 | quantity | amount | amount 10 | b2 Refunds-prev-yrs-exp_R=amount 0.982; b012 DESC_CARG_NAO_REALIZ=amount 0.982; b2 2022/23=amount 0.981 |
| A | b015-0083 | Emp_Wkf_POPD_15+yrs_2022 | quantity | amount | amount 10 | b012 DESC_CARG_NAO_REALIZ=amount 0.984; b014 Retirement Pension=amount 0.984; b2 Annual Sales 2013=amount 0.984 |
| A | b015-0084 | Emp_Wkf_POPD_15+yrs_2023 | quantity | amount | amount 9, quantity 1 | b012 DESC_CARG_NAO_REALIZ=amount 0.978; b012 Value of exports=amount 0.976; b006 REALIZADO=amount 0.976 |
| A | b015-0085 | Emp_Wkf_POPD_15+yrs_2024 | quantity | amount | amount 10 | b014 Retirement Pension=amount 0.985; b2 Annual Sales 2013=amount 0.985; b2 Annual Sales 2014=amount 0.985 |
| A | b015-0086 | Emp_Wkf_POPD_15+yrs_2025 | quantity | amount | amount 10 | b012 DESC_CARG_NAO_REALIZ=amount 0.985; b2 Annual Sales 2014=amount 0.983; b014 Retirement Pension=amount 0.983 |
| A | b015-0087 | Emp_Wkf_POPD_15+yrs_2026 | quantity | amount | amount 10 | b012 DESC_CARG_NAO_REALIZ=amount 0.982; b2 Annual Sales 2014=amount 0.982; b2 Refunds-prev-yrs-exp_R=amount 0.981 |
| A | b015-0088 | Emp_Wkf_POPD_15+yrs_2027 | quantity | amount | amount 10 | b2 2022/23=amount 0.979; b009 平成27年度(千円)=amount 0.976; b2 Refunds-prev-yrs-exp_R=amount 0.974 |
| A | b015-0089 | Emp_Wkf_POPD_15+yrs_2028 | quantity | amount | amount 10 | b006 REALIZADO=amount 0.985; b012 DESC_CARG_NAO_REALIZ=amount 0.981; b014 Children of Disabled o=amount 0.979 |
| A | b015-0090 | Emp_Wkf_POPD_15+yrs_2029 | quantity | amount | amount 10 | b012 DESC_CARG_NAO_REALIZ=amount 0.984; b006 REALIZADO=amount 0.982; b014 Retirement Pension=amount 0.979 |
| A | b016-0032 | 前5日間平均気温の品質情報 | category | other | other 10 | g 臭気=other 0.96; g 臭気=other 0.959; g CitesPerAuthor=other 0.955 |
| A | b016-0054 | 5 | category | other | other 6, category 4 | g ブロモホルム=other 0.89; b013 species=category 0.887; b014 Species/user types=other 0.882 |
| A | b016-0058 | 9 | category | quantity | quantity 6, category 4 | b d1=category 0.942; b d6=category 0.926; syn =quantity 0.923 |
| A | b017-0019 | TOTAL_SHEEP_MOUNTAIN | quantity | other | other 10 | b006 池沼=other 0.972; b009 LENGTH_OF_GILLNET=other 0.971; b011 Length=other 0.969 |
| A | b017-0136 | Structure | category | text | text 5, address 5 | b008 DESC=text 0.843; b014 COUNTERPART_AREA=address 0.83; b003 提供エリア=text 0.814 |
| A | b017-0168 | Prov/Terr | address | other | other 6, id 2, quantity 2 | g 発生県=id 0.848; b014 Page=id 0.828; b011 Station_Chainage=other 0.823 |
| A | b017-0178 | Tax gap component | category | account | account 8, category 2 | b ProcurementClassificat=account 0.883; b2 Government Funded=category 0.867; b2 scheme_description=category 0.862 |
| A | b017-0255 | Family_Famille | category | other | other 7, category 3 | g 科名=category 0.909; b2 目名=other 0.909; b2 科名=other 0.908 |
| A | b017-0269 | bathPosition | id | other | other 8, category 1, quantity 1 | g dag-stage=other 0.911; g digits=other 0.9; b013 val_cal=category 0.882 |
| A | b017-0271 | replicate | id | quantity | quantity 10 | b008 1=quantity 0.966; b013 p_certified=quantity 0.963; b003 NO UNITS=quantity 0.962 |
| A | b017-0296 | Service_FR | category | account | account 5, text 4, category 1 | b Description of Goods (=text 0.894; b2 Type/Narrative of Supp=text 0.889; b Type/Narrative of Supp=account 0.868 |
| A | b017-0346 | Amount per Container | quantity | amount | amount 5, quantity 5 | syn 商品小計=amount 0.88; b value_fte=quantity 0.851; b011 粗大ごみ回収料金=amount 0.849 |
| A | b017-0347 | Rank | category | other | other 5, category 5 | g Abstract Rank=other 0.959; g dag-stage=other 0.906; b013 val_cal=category 0.902 |
| A | b060-0177 | service | product | text | text 9, product 1 | b Product-English-Name-N=text 0.767; b009 Nom du service=text 0.75; syn Opportunity Name1=text 0.719 |
| A | b060-0393 | Body | id | other | other 10 | b2 Body=other 1.0; b2 Body=other 1.0; b Body=other 1.0 |
| A | b060-0737 | SiteReference | id | other | other 9, id 1 | b007 リソース名=other 0.932; b011 Station_Chainage=other 0.924; b014 Page=id 0.911 |
| A | b060-0860 | organisati | id | other | other 10 | b OrganisationURI=other 0.994; b008 dataURL=other 0.994; b OrganisationURI=other 0.993 |
| A | b062-0109 | Supplier | org | account | account 8, org 2 | b Entitiy=org 0.868; syn お届け先会社・部門=org 0.85; b006 LocalDestino=account 0.828 |
| A | b062-0256 | Control Budget Code | category | id | id 9, account 1 | b011 Economic Object Code=id 0.894; b2 economic_object_code=account 0.869; b2 Cost Centre=id 0.848 |
| A | b062-0358 | plan | text | category | category 7, text 3 | b class-title_en=category 0.824; b2 Item=category 0.82; b family-title_fr=category 0.809 |
| A | b063-0117 | Versicherer | id | quantity | quantity 10 | b011 State Government=quantity 0.955; b005 病院=quantity 0.95; g 西第５（北崎支所）=quantity 0.949 |
| A | b063-0125 | SMR 2019-2023 | rate | other | other 10 | b2 Health Deprivation and=other 0.968; b005 測定値=other 0.966; g dbpedia_score=other 0.966 |
| A | b063-0129 | SMR 2024 | rate | other | other 10 | g 硝酸態窒素及び亜硝酸態窒素=other 0.977; b005 測定値=other 0.977; g 硝酸態窒素及び亜硝酸態窒素=other 0.974 |
| A | b063-0135 | AnzStand | quantity | other | other 10 | b010 tj_ncv=other 0.953; b008 ElevationfromSeaLevel(=other 0.943; b014 Lon=other 0.941 |
| A | b063-0199 | Age | category | quantity | quantity 9, category 1 | b011 abstudy__living_allowa=quantity 0.955; g EmployeeCount=quantity 0.938; b2 Term-Deposit-Day-Count=quantity 0.936 |
| A | b063-0202 | LowerB | quantity | other | other 7, quantity 3 | b012 A=other 0.961; g 五島=other 0.942; g count_altmetric=quantity 0.94 |
| A | b063-0207 | AGE | category | id | id 7, category 1, other 1 | b Tournée=id 0.817; b012 中分類=id 0.804; g mechanism=category 0.803 |
| A | b063-0217 | monitoring_program | category | id | id 10 | b009 Column=id 0.804; b009 TECHTYPE=id 0.786; b013 FIELDSTUDY=id 0.771 |
| A | b063-0275 | Nachgefragt | amount | quantity | quantity 10 | b013 Family income between =quantity 0.927; b013 Carer Allowance=quantity 0.925; b006 ParentLabFor=quantity 0.914 |
| A | b063-0322 | kumsum | quantity | amount | amount 6, id 2, quantity 2 | syn =amount 0.939; b008 ICN=id 0.866; syn =amount 0.866 |
| A | b063-0323 | vj_abs_n | quantity | other | other 6, quantity 4 | b011 total_units_supplied_M=other 0.919; b2 Volume (MCF)=quantity 0.918; b2 Volume (10^3 m3)=quantity 0.912 |
| A | b063-0324 | vj_rel_n | rate | other | other 10 | g lnVR_upper=other 0.992; g not_danceable=other 0.985; b009 Kyeema=other 0.982 |
| A | b063-0325 | vj_abs_kumsum | quantity | other | other 9, amount 1 | b011 units_supplied_househo=other 0.859; b011 total_units_supplied_M=other 0.837; b011 units_supplied_househo=other 0.834 |
| A | b063-0326 | vj_rel_kumsum | rate | other | other 10 | b009 Jefferson=other 0.964; b005 測定値=other 0.962; g not_danceable=other 0.96 |
| A | b063-0495 | designation | category | address | address 8, category 2 | b014 Park=address 0.864; b013 property_type=address 0.863; b010 circuit=address 0.839 |
| A | b063-0714 | digital_platform | category | other | other 10 | b2 ServicesFunctionCode=other 0.863; g spotify_url=other 0.862; g spotify_url=other 0.858 |
| A | b064-0139 | Age | category | quantity | quantity 9, category 1 | b011 abstudy__living_allowa=quantity 0.955; b2 Want to live in this p=quantity 0.933; syn =quantity 0.933 |
| A | b064-0142 | Lim_min | quantity | other | other 10 | g 被害域長さ(100m)最小=other 0.97; b2 A2 Floorspace Gains sq=other 0.969; b006 Volume (Cb ft)=other 0.969 |
| A | b064-0155 | NO_COMPLEMENTAIRE | id | quantity | quantity 9, category 1 | b006 NUM_UNID_ANDAMENTO=quantity 0.97; b2 number_habitable_rooms=category 0.961; b003 NO UNITS=quantity 0.959 |
| A | b064-0160 | funk | id | quantity | quantity 7, other 3 | g control=quantity 0.946; b014 Pika.sum=quantity 0.943; g 五島=other 0.934 |
| A | b064-0174 | crime | category | quantity | quantity 10 | b013 BBQ=quantity 0.946; g Comments=quantity 0.945; g 背景_休日フラグ の個別のカウント=quantity 0.94 |
| A | b064-0177 | energy | category | other | other 10 | g 一般細菌=other 0.873; g 大腸菌※=other 0.866; g 臭気=other 0.861 |
| A | b064-0178 | finances | category | amount | amount 10 | syn Unit Cost（必須）=amount 0.917; b Bonus Details=amount 0.875; syn =amount 0.858 |
| A | b064-0184 | plz | address | id | id 10 | b Uadm Requerant=id 0.941; b006 receita=id 0.911; b010 AHRI=id 0.911 |
| A | b064-0370 | Datierung_Bemerkung | text | date | date 9, text 1 | b005 開催日時（表示用）=date 0.955; b004 終了時間=date 0.951; b013 Opening_Hours_Tue_Open=date 0.948 |
| A | b064-0372 | Widmung | text | other | other 6, category 4 | g mood=other 0.874; g Method=other 0.868; b007 POLLUTANT=category 0.861 |
| A | b065-0049 | Got some of what I wanted | rate | other | other 10 | b008 Value=other 0.962; b010 VALUE=other 0.942; b008 Total ROI supplies=other 0.94 |
| A | b065-0050 | Got none of what I wanted | rate | other | other 9, rate 1 | b008 Value=other 0.949; b010 VALUE=other 0.939; b005 Average Violations Per=other 0.935 |
| A | b065-0074 | Dwellings value | quantity | other | other 7, quantity 2, category 1 | b001 １世帯当たり人口
（人）=other 0.897; b012 A=other 0.897; b012 Douglas WTP (ML)=quantity 0.889 |
| A | b065-0202 | Type of Aid | category | id | id 8, category 2 | b2 SMOKE_CONT=id 0.977; b013 Heading=id 0.974; b012 Heading=id 0.974 |
| B | b017-0171 | Total - All Returns /Total - | quantity | amount | quantity 8, amount 2 | b2 VALUE=quantity 0.965; b2 VALUE=quantity 0.962; b Total Invoices Paid=quantity 0.959 |
| B | b060-0260 | 01:30 | quantity | rate | quantity 8, rate 2 | b010 VALUE=rate 0.845; b2 VALUE=quantity 0.844; b004 RETAIL SALES=quantity 0.837 |
| B | b060-0263 | 03:00 | quantity | rate | quantity 8, rate 1, amount 1 | b2 VALUE=quantity 0.871; b004 RETAIL SALES=quantity 0.868; b2 VALUE=quantity 0.864 |
| B | b062-0035 | EW_Total_Company_NSA | quantity | amount | quantity 9, amount 1 | b2 VALUE=quantity 0.928; b2 VALUE=quantity 0.923; b2 VALUE=quantity 0.923 |
| B | b063-0276 | Beschluss | amount | id | amount 7, id 3 | b Projet Investi=id 0.915; b011 Funding=amount 0.901; syn 貸方PRICE=amount 0.85 |
| C | b060-0265 | 04:00 | quantity | rate | rate 4, amount 3, quantity 3 | b007 Cumulative Reduction i=rate 0.9; b2 VALUE=amount 0.888; b VALUE=quantity 0.881 |
| C | b063-0213 | AGE | category | id | id 4, category 3, other 1 | g episode=other 0.802; g 現在時刻(月)=date 0.786; b006 地区割=id 0.777 |
