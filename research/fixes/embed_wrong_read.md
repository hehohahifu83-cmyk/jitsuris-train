# 本体の中で近い教材の列（`research/unknown/embed_read.py`。もとは `embed_nn.json`）

- 本体 C2 種子 1 の分類の最後の層への入力で近い教材の列（余弦）。teacher＝教材の種類、model＝本体がその教材の列に付ける答え。教材 48215 列、4355.8 秒

| 分け | 列 |
|---|---:|
| A 近い教材の多く（5 列以上）に本体の答えと同じ種類が付いている＝その教材から覚えた | 168 |
| B 近い教材の多くは正解の種類なのに、本体は別の種類と答えた | 5 |
| C 近い教材は割れていて、本体の答えの種類も混ざる | 2 |

## A の列で、本体の答えと同じ種類が付いていた近い教材の出どころ

| 出どころ | 列（延べ） |
|---|---:|
| b2 | 162 |
| syn | 144 |
| b | 140 |
| b010 | 114 |
| b006 | 106 |
| b011 | 96 |
| b009 | 89 |
| g | 88 |
| b007 | 86 |
| b008 | 85 |
| b003 | 79 |
| b013 | 75 |
| b014 | 68 |
| b012 | 64 |
| b004 | 49 |
| b005 | 38 |
| j | 13 |
| b002 | 12 |
| b001 | 2 |

| 分け | id | 見出し | 正解 | 本体 | 近い 10 列の種類 | いちばん近い 3 列（出どころ・列名・種類・近さ） |
|---|---|---|---|---|---|---|
| A | b015-0047 | No. | id | category | category 10 | b010 NUM_MODE_TRANSPORT=category 0.977; b011 DEMO8=category 0.977; b011 asgc_ra=category 0.975 |
| A | b015-0052 | No. laboratory confirmed | quantity | category | category 9, quantity 1 | b009 MMM2019=category 0.954; b011 PT=category 0.953; b010 RESULT=category 0.942 |
| A | b016-0004 | @Caption | category | text | text 8, category 2 | b010 内容=text 0.962; b009 Comments=text 0.957; b006 subject=text 0.956 |
| A | b017-0057 | QUALCOU | address | category | category 10 | b008 UNIT=category 0.96; b006 veteran_cert=category 0.958; b006 forma_doenca=category 0.957 |
| A | b017-0065 | MEASURE | category | id | id 10 | b014 MEASURE=id 0.994; b010 FISHERY_ID=id 0.988; b004 reason_id=id 0.986 |
| A | b017-0144 | Product | category | product | product 10 | b011 Product=product 0.979; b013 Product=product 0.965; j 品目=product 0.956 |
| A | b017-0163 | Product | category | product | product 9, category 1 | b013 Product=product 0.983; b013 Produit=product 0.976; b011 Product=product 0.975 |
| A | b017-0230 | FSA | address | org | org 9, address 1 | b013 FSA=address 0.943; b005 名称_カナ=org 0.935; b010 CRAS=org 0.925 |
| A | b017-0258 | TraitValueDescription_Descri | category | text | text 9, category 1 | b2 HabitatDescription=text 0.9; g Setting=text 0.883; b014 type_or_title=text 0.87 |
| A | b017-0263 | batch | id | category | category 10 | b013 Bin=category 0.968; b010 FOREST=category 0.958; b009 INES Level=category 0.955 |
| A | b017-0286 | Site | address | category | category 8, address 2 | b013 dev_site=category 0.914; b009 dev_site=address 0.912; b003 ST_TYPE=category 0.912 |
| A | b017-0304 | Data Source | org | category | category 10 | b013 Source=category 0.952; b008 DataSource=category 0.95; b006 DataSource=category 0.95 |
| A | b017-0312 | Service | category | account | account 8, category 2 | b2 Expenditure=category 0.935; b2 SERVICE_RESPONSABLE=account 0.917; b Purpose=account 0.914 |
| A | b017-0331 | originating_sector_en | account | category | category 10 | b009 Cluster=category 0.966; b ANZSIC Division Name=category 0.961; b2 Service Category Label=category 0.958 |
| A | b060-0137 | Measure | text | category | category 10 | b011 区分３=category 0.949; b2 Statistic Label=category 0.949; b010 Indicator=category 0.941 |
| A | b060-0186 | policy_area | category | account | account 7, category 3 | b012 項目２=account 0.945; b010 Asset Workgroup=account 0.943; b008 用途分類=category 0.937 |
| A | b060-0187 | territorial_application_of_r | category | text | text 7, address 3 | b003 提供エリア=text 0.918; b014 COUNTERPART_AREA=address 0.905; b014 Location=address 0.893 |
| A | b060-0205 | GOR CODE | id | category | category 10 | b013 treatment_code=category 0.981; b2 LABEL=category 0.976; b2 Class_4=category 0.974 |
| A | b060-0287 | Department Family | org | category | category 9, org 1 | b012 借入先=category 0.846; b009 Portfolio Dept?=category 0.832; syn ブランド=category 0.819 |
| A | b060-0345 | Department | org | account | account 6, org 4 | b Department=org 0.985; b006 Department=org 0.979; b007 Division/Sitegroup=account 0.972 |
| A | b060-0515 | Department Family | org | category | category 10 | b014 Maintain=category 0.874; b003 診療科=category 0.863; b012 dept_f=category 0.855 |
| A | b060-0543 | Details | account | text | text 9, category 1 | b002 Transfer Purpose=text 0.938; b006 Objeto=text 0.936; b006 Assunto=category 0.932 |
| A | b060-0658 | Type | account | category | category 9, account 1 | b2 Type=account 0.991; b type=category 0.98; b DETAILS=category 0.974 |
| A | b060-0706 | Neither satisfied or dissati | quantity | category | category 8, other 1, quantity 1 | g MT2=other 0.899; syn Pay Frequency=category 0.895; b2 potential_epc_score_kn=category 0.883 |
| A | b060-0757 | Inspection or regulatory rem | category | account | account 8, category 2 | b2 SERVICE_RESPONSABLE=account 0.963; b2 Expenditure=category 0.937; b012 項目２=account 0.931 |
| A | b060-0800 | Department family | org | account | account 8, org 2 | b Department=org 0.97; b006 ORGAO_ENTIDADE=account 0.963; b009 Dept_Level_1=account 0.961 |
| A | b060-0831 | listed_building | id | address | address 10 | syn cityBlock=address 0.956; syn =address 0.954; syn =address 0.952 |
| A | b060-0900 | Question | id | category | category 10 | b010 Datum/ EPSG=category 0.904; b009 MEPSComp=category 0.894; b006 ballot_title_2=category 0.876 |
| A | b060-0980 | Parent Department | org | account | account 5, category 4, org 1 | b Entitiy=org 0.95; b006 LocalDestino=account 0.948; j 貸方部門=account 0.93 |
| A | b060-0981 | Organisation | org | category | category 5, org 4, account 1 | syn お届け先会社・部門=org 0.889; b008 Government=category 0.868; b Entitiy=org 0.854 |
| A | b060-1052 | IncomeType | account | category | category 10 | b IncomeType=category 1.0; b2 Merchant Category=category 0.982; b DETAILS=category 0.98 |
| A | b062-0070 | trading_bloc | org | category | category 9, address 1 | b013 sub_category=category 0.866; b008 Zone=category 0.865; b2 Beneficiary Location:G=category 0.86 |
| A | b062-0073 | Department Family | org | account | account 9, org 1 | b006 ORGAO_ENTIDADE=account 0.974; b Department=org 0.972; b009 Dept_Level_1=account 0.97 |
| A | b062-0186 | Extending Agency | id | org | org 10 | b013 Agencies=org 0.929; b008 Airline=org 0.925; syn Brand2=org 0.923 |
| A | b062-0260 | PESA Economic Group Code | account | category | category 10 | b007 区分=category 0.962; b006 SUBACAO=category 0.95; b007 区分=category 0.936 |
| A | b062-0319 | Proclass Category | account | category | category 5, account 5 | b2 ProcurementClassificat=category 0.982; b006 Revenue Category=category 0.981; b2 Service Category Label=category 0.977 |
| A | b062-0362 | plan | text | category | category 9, text 1 | b class-title_en=category 0.83; b2 Item=category 0.815; b family-title_fr=category 0.811 |
| A | b062-0431 | ServiceCategoryLabel | category | account | account 8, category 2 | b ProcurementClassificat=account 0.976; b012 区分=account 0.97; b005 会計名称=account 0.965 |
| A | b062-0437 | MandatoryReliefDescription | category | text | text 10 | b007 valores_possiveis=text 0.94; b012 PERIODO_VALIDO_REGRA_O=text 0.923; b013 PERIODO_VALIDO_REGRA_O=text 0.923 |
| A | b062-0438 | DiscretionaryReliefDescripti | category | text | text 10 | b013 Outcome=text 0.817; b007 Specific Outcomes of t=text 0.801; b010 Outcome=text 0.797 |
| A | b063-0071 | Gemeinde_Nr | id | address | address 6, id 4 | b010 HOUSE_NO=address 0.965; b013 house_no=address 0.96; b006 NUMERO_PO=id 0.947 |
| A | b063-0108 | Departement | org | account | account 9, org 1 | g Facility=account 0.956; b006 DEPARTMENT=account 0.953; syn Department（任意）=account 0.952 |
| A | b063-0109 | Verwaltungseinheit (Auftragg | org | account | account 10 | syn 管理部門=account 0.919; b007 Department=account 0.911; b006 LocalDestino=account 0.904 |
| A | b063-0141 | Id Of Animal Category | id | category | category 10 | b013 Type=category 0.99; b012 dev_type=category 0.989; b003 学校種=category 0.989 |
| A | b063-0143 | Degree of severity 0 | quantity | category | category 7, other 3 | b2 potential_epc_score_kn=category 0.915; b2 epc_rating_known=category 0.915; g 大腸菌※=other 0.909 |
| A | b063-0144 | Degree of severity 1 | quantity | category | category 9, other 1 | b2 epc_rating_known=category 0.923; b011 Trunk Circumference=category 0.917; b014 LUMquintile=category 0.913 |
| A | b063-0145 | Degree of severity 2 | quantity | category | category 6, other 4 | b2 epc_rating_known=category 0.914; b2 potential_epc_score_kn=category 0.914; g dag-stage=other 0.906 |
| A | b063-0146 | Degree of severity 3 | quantity | category | category 8, other 2 | b2 epc_rating_known=category 0.926; b011 Trunk Circumference=category 0.911; b2 potential_epc_score_kn=category 0.911 |
| A | b063-0147 | Id Experiment Category | id | category | category 10 | b014 CLASS=category 0.984; b Decision Category=category 0.983; b007 NIVEL_PROTECAO=category 0.983 |
| A | b063-0148 | Id Of Disease Category | id | category | category 10 | b Decision Type=category 0.98; b008 Class=category 0.977; b003 Class=category 0.976 |
| A | b063-0162 | parameter_group_it | category | org | org 10 | syn ブランド=org 0.855; syn ブランド=org 0.853; syn Brand2=org 0.85 |
| A | b063-0165 | parameter_decimals | quantity | category | category 8, other 2 | g _status_=other 0.923; g Hydrozoa_indet=category 0.923; b008 Decimals=category 0.889 |
| A | b063-0173 | parameter_decimals | quantity | category | category 8, other 2 | g _status_=other 0.923; g Hydrozoa_indet=category 0.923; b008 Decimals=category 0.889 |
| A | b063-0181 | parameter_decimals | quantity | category | category 9, other 1 | g Hydrozoa_indet=category 0.926; g _status_=other 0.912; b008 Decimals=category 0.909 |
| A | b063-0185 | Kostenbereich | category | account | account 10 | b002 Category=account 0.982; syn 部門=account 0.981; b2 MerchantCategory=account 0.98 |
| A | b063-0186 | Unterkostenbereich | category | account | account 10 | b007 項目=account 0.977; b011 Subcategory - EN=account 0.971; b009 Level_5=account 0.97 |
| A | b063-0187 | Kostenart | category | account | account 6, category 4 | b010 Expense_type=category 0.985; b013 Expense type=account 0.975; b2 Pro Class Description=category 0.973 |
| A | b063-0206 | GEO | address | id | id 10 | b006 mtfcc20=id 0.984; b2 STATISTIC=id 0.984; b010 LOG_TYPE=id 0.983 |
| A | b063-0242 | source | category | text | text 9, category 1 | b011 Source=text 0.94; g Source=category 0.934; b007 状況=text 0.905 |
| A | b063-0263 | label | text | category | category 10 | b010 feature=category 0.93; b010 Instrument=category 0.929; b010 type=category 0.924 |
| A | b063-0300 | kategorie_sortierung | id | category | category 10 | b009 CD_CLASS_VEH=category 0.985; b014 教育機関_本分校=category 0.98; b009 Level B=category 0.98 |
| A | b063-0330 | plz | address | id | id 10 | g Medcode=id 0.951; b006 SUBBACIA=id 0.95; syn ロット番号=id 0.95 |
| A | b063-0331 | haus_nr | address | id | id 10 | b008 Station No.=id 0.989; b005 NO=id 0.988; b005 町字ID=id 0.987 |
| A | b063-0355 | eingangsnummer_gebaeude | address | id | id 10 | b005 行政区番号=id 0.992; b010 基準地番号（連番）=id 0.991; b004 NO=id 0.991 |
| A | b063-0372 | id2 | id | category | category 9, other 1 | b2 TREETYPE=category 0.868; b008 Parameter=category 0.863; b2 Projection=category 0.83 |
| A | b063-0396 | traktandum_beschlussdetail_d | text | category | category 10 | b013 indicateur de resultat=category 0.913; b014 PAL*の低減率=category 0.911; b2 Grant Expenditure Rate=category 0.904 |
| A | b063-0397 | traktandum_beschlussdetail_f | text | category | category 9, text 1 | b008 Statistic=category 0.928; b010 データセット_キーワード=text 0.913; b2 CONTRAVENTION=category 0.913 |
| A | b063-0449 | richtung | text | address | address 8, category 2 | b012 路線名=address 0.878; b013 str_type=address 0.878; b013 Route=category 0.842 |
| A | b063-0462 | plz | address | id | id 10 | b013 sa2_5digitcode_2016=id 0.978; b009 4-digit ANZSCO code=id 0.978; b007 ID_ROTA_CICLOVIARIA=id 0.977 |
| A | b063-0579 | Aufgabengebiet (de) | category | account | account 6, category 4 | b2 Pro Class Description=category 0.967; b010 Expense_type=category 0.962; b Pro Class Description=account 0.961 |
| A | b063-0595 | TECHNIK | text | category | category 10 | syn Shipping Method Title=category 0.935; b011 material=category 0.922; b013 PrimTech=category 0.922 |
| A | b063-0601 | organisationseinheit | org | account | account 10 | b010 Business Unit=account 0.976; b006 管理=account 0.976; syn 部門=account 0.974 |
| A | b063-0711 | series | text | category | category 9, text 1 | b006 ballot_title_2=category 0.905; b2 Funding_Line=category 0.899; b006 CASE_TITLE=category 0.896 |
| A | b063-0722 | creator | org | person | person 10 | g Author=person 0.971; g creator=person 0.959; syn Owner=person 0.953 |
| A | b064-0004 | georegion | address | category | category 8, address 2 | b Jurisdiction=category 0.942; b010 ROAD_EDGE_TYPE=category 0.919; b011 Region@=category 0.917 |
| A | b064-0014 | georegion | address | category | category 8, address 2 | b Jurisdiction=category 0.947; b011 Region@=category 0.922; b2 Region=address 0.918 |
| A | b064-0046 | nfr | id | category | category 7, id 3 | b Base Layer 1=category 0.968; b Base Layer 1=category 0.967; b Base Layer 1=id 0.967 |
| A | b064-0109 | parameter_decimals | quantity | category | category 8, other 2 | g _status_=other 0.923; g Hydrozoa_indet=category 0.923; b008 Decimals=category 0.889 |
| A | b064-0117 | parameter_decimals | quantity | category | category 9, other 1 | g Hydrozoa_indet=category 0.925; b008 Decimals=category 0.922; b011 Chlorophyll [quality]=category 0.92 |
| A | b064-0137 | Semaine | date | quantity | quantity 10 | b008 tavg__mean_wave_period=quantity 0.949; b008 tsig__significant_peri=quantity 0.948; b011 FISHING_TIME=quantity 0.945 |
| A | b064-0147 | GEO_CANT | id | category | category 10 | syn =category 0.942; syn =category 0.941; b009 MMM2019=category 0.938 |
| A | b064-0164 | e | account | text | text 9, account 1 | b Description=account 0.918; b Description of Goods (=text 0.906; b013 Purpose=text 0.895 |
| A | b064-0168 | abkuerzung | id | category | category 9, id 1 | b2 conservation_area_site=category 0.896; b013 TraitCode=category 0.877; g source_vocabulary_id=category 0.873 |
| A | b064-0194 | verteilzone | id | category | category 7, id 3 | b Base Layer 2=id 0.979; b Base Layer 1=category 0.979; b Base Layer 3=category 0.979 |
| A | b064-0197 | kategorie_sortierung | id | category | category 10 | b003 本分校=category 0.99; b003 本分校=category 0.988; b2 Class_4=category 0.988 |
| A | b064-0210 | sitzung_titel | id | text | text 10 | b014 名称=text 0.742; b2 SCHEDULE_LINE_17=text 0.736; b013 根拠=text 0.736 |
| A | b064-0221 | eingangsnummer_gebaeude | address | id | id 10 | b010 OBJECTID=id 0.993; b009 OBJECTID=id 0.993; b011 OBJECTID=id 0.993 |
| A | b064-0222 | administrative_wohnungsnumme | address | id | id 10 | syn officeNumber=id 0.989; syn officeNumber=id 0.988; b005 町字ID=id 0.984 |
| A | b064-0224 | stockwerk_bezeichnung | address | category | category 10 | b010 Club_Venue_Sports=category 0.925; b014 Intended_Destination=category 0.9; b006 提供エリア=category 0.898 |
| A | b064-0225 | lage_auf_dem_stockwerk | address | category | category 10 | b008 Water Condition=category 0.986; b006 height_field_unit=category 0.985; b Shell_hardness_Duret饑d=category 0.985 |
| A | b064-0230 | Themen | category | text | text 8, category 2 | b006 subject=text 0.976; b003 データセット_キーワード=category 0.975; b2 データセット_キーワード=text 0.975 |
| A | b064-0251 | PLZ | address | id | id 10 | b004 KEY_CODE=id 0.983; b007 KEY_CODE=id 0.983; b007 KEY_CODE=id 0.982 |
| A | b064-0253 | Öffnungszeiten | text | category | category 8, text 2 | b008 用途=category 0.963; b005 支援内容=category 0.961; b2 [No.21]自由記述=text 0.961 |
| A | b064-0274 | betrieb_plz | address | id | id 10 | b004 SUBDIVISION ID=id 0.983; b007 ID_ROTA_CICLOVIARIA=id 0.983; b003 SUBDIVISION ID=id 0.983 |
| A | b064-0291 | Abstimmungsgegenstand | text | category | category 9, text 1 | b006 CASE_TITLE=category 0.956; b010 Claim=category 0.952; b005 支援内容=category 0.947 |
| A | b064-0318 | qualitaet | text | category | category 10 | b002 Measure=category 0.938; b008 Metric=category 0.923; b006 Measure=category 0.916 |
| A | b064-0320 | verantwortlichkeit_abkuerzun | id | org | org 10 | b007 GESTOR=org 0.86; b013 Agencies=org 0.857; b007 Orgao=org 0.849 |
| A | b064-0325 | richtung | address | category | category 8, address 2 | b013 Route=category 0.929; b008 Topography=category 0.88; b008 Route=address 0.874 |
| A | b064-0356 | designation | address | category | category 10 | b Designation-fr=category 0.966; b Designation-fr=category 0.952; b011 Function/Category=category 0.952 |
| A | b064-0366 | Titel | text | person | person 10 | g Authors=person 0.804; g trackback_author_nick=person 0.793; g creator=person 0.79 |
| A | b064-0380 | Datierung_Bemerkung | category | text | text 10 | b009 Terme operationnel=text 0.921; syn startDateTimeRemarks=text 0.917; b Notes=text 0.913 |
| A | b064-0384 | Signatur | id | org | org 10 | b007 施設名称_英字=org 0.936; b005 名称_カナ=org 0.934; b004 投票所_名称（英字）=org 0.932 |
| A | b064-0429 | title_de_CH | text | category | category 10 | b013 title_en=category 0.931; b014 Title=category 0.928; b006 ballot_title_1=category 0.927 |
| A | b064-0432 | title_rm_CH | text | category | category 10 | b006 CASE_TITLE=category 0.953; b010 Claim=category 0.953; b007 利用可能曜日=category 0.952 |
| A | b064-0433 | short_title_de_CH | text | category | category 10 | b004 実施サービス=category 0.936; b008 用途=category 0.934; b014 Title=category 0.931 |
| A | b064-0436 | short_title_rm_CH | text | category | category 8, text 2 | b006 CASE_TITLE=category 0.955; b004 実施サービス=category 0.954; b010 holiday=category 0.951 |
| A | b065-0123 | Second Tier Authority | address | org | org 7, address 3 | b2 Health Service Executi=org 0.97; b2 Health Service Executi=address 0.97; b007 運営主体=org 0.969 |
| A | b065-0191 | Region | category | address | address 10 | b011 Region=address 0.991; b008 Region=address 0.99; b010 Region=address 0.99 |
| A | b065-0193 | Extending Agency | id | org | org 10 | b013 Agencies=org 0.929; b008 Airline=org 0.925; syn Brand2=org 0.923 |
| A | b065-0203 | Department | org | account | account 9, org 1 | b Department=org 0.995; b007 Division/Sitegroup=account 0.985; b009 Dept_Level_1=account 0.981 |
| A | b065-0212 | Arrest/Detention > Assault w | quantity | category | category 8, quantity 2 | b2 Want to live in this p=quantity 0.981; g 背景_休日フラグ の個別のカウント=quantity 0.98; b2 Foreign Vehicle=category 0.973 |
| A | b065-0214 | Arrest/Detention > Child Sex | quantity | category | category 7, quantity 3 | b2 Want to live in this p=quantity 0.964; g 背景_休日フラグ の個別のカウント=quantity 0.964; b014 Teacher Size of School=category 0.954 |
| A | b065-0221 | Local Authority | address | org | org 9, address 1 | b011 Local Authority=org 0.985; b006 団体名=org 0.985; b006 団体名=org 0.985 |
| A | b065-0223 | Is the site Brownfield, Gree | category | address | address 10 | b014 Location=address 0.94; b003 市区町村名=address 0.922; b012 Where do you live?=address 0.922 |
| A | b065-0244 | Main, parent or sponsoring d | org | account | account 9, org 1 | b007 Department=account 0.949; syn お届け先会社・部門=org 0.917; syn 管理部門=account 0.915 |
| A | b019-0010 | 大分類 | id | category | category 10 | syn カテゴリー=category 0.988; b2 TPTREECAT=category 0.987; b008 AADT_Intervention_Cate=category 0.987 |
| A | b020-0039 | 管理職 | quantity | category | category 10 | syn 役職=category 0.99; b 身体介護=category 0.971; b2 tenure_known=category 0.971 |
| A | b022-0014 | Floor ID | address | category | category 10 | b013 ID=category 0.972; b012 SITC 3 digit=category 0.967; b011 Zone=category 0.966 |
| A | b022-0038 | indicator_descriptor | text | category | text 5, category 5 | g Indicator=text 0.964; b006 Indicator=category 0.917; b002 Measure=category 0.893 |
| A | b022-0048 | indicator | text | category | category 9, text 1 | g Indicator=text 0.96; b006 Indicator=category 0.96; b002 Measure=category 0.932 |
| A | b022-0064 | Count of Vehicle ROIDs | quantity | category | category 9, id 1 | b006 PUBLIC_FLG=category 0.963; b010 TESSELLATE=category 0.941; b010 NUM_MODE_TRANSPORT=category 0.938 |
| A | b023-0029 | education_and_training | quantity | category | category 8, quantity 2 | g Education=category 0.947; b2 Want to live in this p=quantity 0.946; b 無料送迎＿提供サービス＿通院=category 0.945 |
| A | b023-0040 | education_and_training | quantity | category | category 8, quantity 2 | g 背景_休日フラグ の個別のカウント=quantity 0.956; g Education=category 0.952; g Education=category 0.951 |
| A | b023-0047 | vehicle_class_1 | quantity | category | category 10 | b010 品目階層Item_Class=category 0.898; b014 Class=category 0.879; b Type de matériel=category 0.878 |
| A | b023-0048 | vehicle_class_2 | quantity | category | category 10 | syn 在庫タイプ=category 0.98; b2 Class_1=category 0.978; syn Order type=category 0.976 |
| A | b023-0049 | vehicle_class_3 | quantity | category | category 10 | b010 品目階層Item_Class=category 0.955; syn 在庫タイプ=category 0.945; b007 group=category 0.941 |
| A | b023-0050 | vehicle_class_4 | quantity | category | category 10 | b2 Class_1=category 0.98; syn 在庫タイプ=category 0.978; b2 Class_2=category 0.978 |
| A | b023-0051 | vehicle_class_5 | quantity | category | category 10 | b2 Class_1=category 0.98; b2 Class_2=category 0.977; syn 在庫タイプ=category 0.976 |
| A | b023-0072 | Tariff | category | tax_class | tax_class 10 | syn 貸方インボイス区分=tax_class 0.735; syn 貸方インボイス区分=tax_class 0.735; syn 適格請求書=tax_class 0.732 |
| A | b023-0084 | Main destination | category | text | text 10 | b004 利用対象者=text 0.917; b006 提供エリア=text 0.915; b 無料送迎＿送迎先（自宅・自宅以外）=text 0.91 |
| A | b023-0108 | Life Guard Service | text | category | category 7, text 3 | b006 駐車場情報=category 0.961; b2 CONTRAVENTION=category 0.944; b010 holiday=category 0.943 |
| A | b023-0120 | traffic_direction_seq | id | category | category 8, id 2 | b012 Watershed_BassinVersan=id 0.968; b010 MEDIUM_TYPE=category 0.946; b014 Category=category 0.934 |
| A | b026-0003 | Core Responsibility | category | account | account 9, text 1 | b2 Purpose=account 0.95; b Purpose=account 0.947; syn プロジェクト=account 0.946 |
| A | b026-0004 | Program | category | account | account 9, category 1 | b Pro Class Description=account 0.954; b2 Type of Expenditure=category 0.952; b2 desc_=account 0.952 |
| A | b026-0009 | Core Responsibility | category | account | account 9, text 1 | b PurposeOfExpenditure=text 0.97; b Payment Description=account 0.965; b2 Purpose=account 0.962 |
| A | b026-0033 | developed_by_en | category | org | org 10 | b2 Operator=org 0.957; b010 届出先=org 0.947; b008 Airline=org 0.941 |
| A | b026-0034 | developed_by_fr | category | org | org 10 | b006 Contractor=org 0.983; b006 developer=org 0.977; b009 publisher=org 0.977 |
| A | b035-0010 | profile | address | text | text 8, address 2 | b007 都　市　概　要=text 0.917; b004 アクセス方法=text 0.905; b Location=text 0.901 |
| A | b035-0038 | Reason for enforcement activ | category | text | category 5, text 5 | b005 開催パターン=category 0.957; b Dispute-Status_Statut-=category 0.956; b2 [No.21]自由記述=text 0.955 |
| A | b035-0039 | Written warnings | quantity | category | category 10 | syn 車椅子可=category 0.96; g 貸切可能=category 0.956; b2 Foreign Vehicle=category 0.955 |
| A | b036-0055 | Centre | org | address | address 10 | b014 Station=address 0.972; b008 Test Centre=address 0.971; b004 投票所_投票区名=address 0.968 |
| A | b036-0069 | operator | org | category | category 10 | g PulseSequenceType=category 0.945; g journal_pcode=category 0.94; b010 GIS_ACQUISITION_METHOD=category 0.938 |
| A | b036-0139 | CulturalSignificance | text | category | category 6, text 4 | b010 SITUACAO=category 0.944; b012 Universe=category 0.94; b003 データセット_キーワード=category 0.94 |
| A | b036-0141 | Location | address | category | category 10 | b003 提供エリア=category 0.964; b003 提供エリア=category 0.962; b006 提供エリア=category 0.961 |
| A | b036-0166 | Department | org | account | account 10 | b2 Department=account 0.99; b2 Department=account 0.99; b Department=account 0.99 |
| A | b036-0233 | Demographics | category | text | text 10 | b008 unsafe_=text 0.967; b008 Greater_Risk_Question=text 0.952; b005 Topic=text 0.951 |
| A | b036-0274 | PURPOSE | category | text | text 7, category 3 | g ReadcodeDescr=text 0.916; b002 Transfer Purpose=text 0.907; b006 Objeto=text 0.907 |
| A | b050-0009 | MAKE_DESC | org | category | category 10 | syn Seller Brand=category 0.837; syn Card Brand=category 0.837; syn vendor_brand=category 0.825 |
| A | b050-0039 | Evaluation criteria and weig | text | category | category 8, text 2 | b010 SITUACAO=category 0.907; g LDA=text 0.903; b008 Title complement=category 0.901 |
| A | b050-0040 | Title | org | text | text 10 | b008 Title=text 0.98; b Title=text 0.98; b DTF Publication Title=text 0.974 |
| A | b054-0001 | STATISTIC | id | category | category 10 | b010 Statistic=category 0.959; b006 vote=category 0.957; b004 FILING FREQUENCY=category 0.957 |
| A | b055-0002 | 区分レベル１ | account | category | category 10 | b006 SUBACAO=category 0.976; b006 CATEGORIA_ECONOMICA=category 0.969; b Classification=category 0.969 |
| A | b055-0003 | 区分レベル２ | account | category | category 10 | b006 CATEGORIA_ECONOMICA=category 0.987; b007 DESC_CATEGORIA=category 0.983; b011 Category - FR=category 0.981 |
| A | b055-0004 | 区分レベル３ | account | category | category 10 | b006 CATEGORIA_ECONOMICA=category 0.985; b006 CATEGORIA_ECONOMICA=category 0.979; syn class=category 0.978 |
| A | b055-0005 | 区分レベル４ | account | category | category 10 | b006 CATEGORIA_ECONOMICA=category 0.982; b006 CATEGORIA_ECONOMICA=category 0.982; syn class=category 0.977 |
| A | b055-0006 | 区分レベル５ | account | category | category 8, account 2 | b008 区分３=account 0.975; b2 ProcurementClassificat=category 0.971; b006 Revenue Category=category 0.97 |
| A | b055-0014 | 都分類地区１ | category | address | address 10 | b014 Electoral Division=address 0.925; b2 DIVISION=address 0.91; b009 Precinct=address 0.886 |
| A | b055-0015 | 都分類地区２ | category | address | address 10 | b009 地域名=address 0.983; b013 Region=address 0.975; b009 Region=address 0.973 |
| A | b055-0040 | 地域 | category | address | address 10 | b014 Location=address 0.94; b003 市区町村名=address 0.938; b012 Where do you live?=address 0.937 |
| A | b055-0074 | 市場名 | org | address | address 8, org 2 | b008 名称=address 0.974; b008 名称=address 0.97; b008 名称=address 0.97 |
| A | b055-0110 | 警察署名 | org | address | address 10 | b004 団体名=address 0.987; b003 団体名=address 0.987; b003 団体名=address 0.986 |
| A | b055-0139 | 対象 | text | category | category 8, text 2 | b008 Title complement=category 0.945; b004 利用可能曜日=category 0.939; b009 事項=category 0.934 |
| A | b055-0144 | 指標「ひまわり」の糖尿病関連項目より | text | category | category 8, text 2 | b003 データセット_キーワード=category 0.961; b2 [No.21]自由記述=text 0.956; b データセット_キーワード=category 0.956 |
| A | b055-0202 | 回収可能品目 | category | product | product 10 | b012 回収品目=product 0.992; b011 ゴミの品目_英字=product 0.985; j 品目=product 0.979 |
| A | b055-0293 | 名称 | address | org | org 7, address 3 | b008 名称_通称=org 0.991; b012 名称=org 0.991; b008 名称=address 0.99 |
| A | b055-0507 | 利用可能日時特記事項 | category | text | text 10 | b004 備考=text 0.985; j 備考=text 0.977; b011 備考=text 0.976 |
| A | b056-0012 | Program title | text | account | category 5, account 5 | b title=category 0.928; b014 Sub-program title=account 0.905; b2 Expenditure=category 0.897 |
| A | b056-0023 | Sub-program title | text | account | account 9, text 1 | b010 Program=account 0.934; b Description of Goods (=account 0.932; b2 Description of Goods (=account 0.928 |
| B | b063-0392 | traktandum_start_behandlung_ | date | text | date 7, text 3 | b008 Mon am=date 0.927; b009 Mon pm=date 0.924; b008 Tues am=date 0.916 |
| B | b063-0400 | sessionssitzung_uhrzeit | date | text | date 6, text 4 | b008 Tues am=date 0.951; b008 Mon am=date 0.947; b009 Mon pm=date 0.942 |
| B | b063-0560 | Titelvariante | text | category | text 6, category 4 | b010 holiday=category 0.895; b2 [No.21]自由記述=text 0.893; b003 定休日=category 0.891 |
| B | b056-0063 | Target | text | category | text 6, category 4 | b010 データセット_キーワード=text 0.927; b003 データセット_キーワード=category 0.927; b2 [No.21]自由記述=text 0.925 |
| B | b056-0066 | Target | text | category | text 6, category 4 | b010 データセット_キーワード=text 0.927; b003 データセット_キーワード=category 0.927; b2 [No.21]自由記述=text 0.925 |
| C | b062-0268 | Department Family | org | category | account 4, category 4, org 2 | b Entitiy=org 0.884; syn お届け先会社・部門=org 0.869; b006 LocalDestino=account 0.867 |
| C | b056-0043 | Sub-program title | text | account | text 4, account 4, category 2 | b title=category 0.924; b012 Sub-program title=text 0.903; b Description of Goods (=text 0.902 |
