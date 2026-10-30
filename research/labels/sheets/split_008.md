# 割れている組の見直し 008（LABEL_GUIDE v2.2）

同じ陣・同じ列名なのに種類が割れている組。判断するのは「少ないほうの列」（番号つき）。
`answers/split_NNN.tsv` に少ないほうの列 1 列ずつ 1 行：`gid`・`col`（番号）・`label`（付けるべき種類。今のままなら今の種類、決められなければ unknown）・`reason`。
今のラベルは参考。v2.2 の決まりと、その列の表・値・同じ表の列から決める。表が違って意味が違えば、割れたままでよい。

## G211　b064「designation」（2 列：category 1・address 1）

多いほうの category の例：

- Parking / Parking / Parkplätze / Parkplatz am Bahnhof / Parkhaus Badischer Bahnhof, Schwarzwaldstrasse 160 / Parking / Parking / Parking（同じ表：sloid・parentSloidServicePoint・parentNumberServicePoint・additionalInformation・placesAvailable・prmPlacesAvailable・validFrom・validTo）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | address | entrée sud / Quai 1 / Place de la Gare / Passerelle au dessus des voies / Haupteingang / Place de la Gare / Hauptzugang bei Bushaltestelle / Hauptzugang Bahnhofgebäude | sloid・parentSloidServicePoint・parentNumberServicePoint・mainReferencePoint・additionalInformation・referencePointType・validFrom・validTo | 0-b587-63184087753d/download/actual-date-reference-point.csv |

## G212　b064「Datierung_Bemerkung」（2 列：text 1・category 1）

多いほうの text の例：

-  /  / Poststempel /  / Entzifferung unsicher / Orig.: 8 Octobre nouveau style 1701 / 9. Juni (?) / Dat. Karte (Br. undat.)（同じ表：ID・Signatur・AutorIn・Titel・Ort・Datierung_von・Datierung_bis・Illustration）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category |  /  /  /  /  / geschätzt /  /  | ID・Signatur・FotografIn・Titel・Inhalt_Kurzbeschreibung・Datierung_von・Datierung_bis・Farbe | https://ead.nb.admin.ch/ogd/photoglob-wehrli_metadata.csv |

## G213　b065「CoordinateReferenceSystem」（3 列：id 2・category 1）

多いほうの id の例：

- OSGB036 / OSGB036 / OSGB036 / OSGB036 / OSGB036 / OSGB036 / OSGB036 / OSGB036（同じ表：OrganisationURI・OrganisationLabel・SiteReference・PreviouslyPartOf・SiteplanURL・GeoX・GeoY・Hectares）
- ETRS89 / ETRS89 / ETRS89 / ETRS89 / ETRS89 / ETRS89 / ETRS89 / ETRS89（同じ表：OrganisationURI・OrganisationLabel・SiteReference・SiteplanURL・GeoX・GeoY・Hectares・Deliverable）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | OSGB36 / OSGB36 / OSGB36 / OSGB36 / OSGB36 / OSGB36 / OSGB36 / OSGB36 | ExtractDate・OrganisationURI・OrganisationLabel・ServiceTypeURI・ServiceTypeLabel・GeoX・GeoY・GeoPointLicensingURL | .gov.uk/media/6110/public-toilet-schema-toilet-list-2014.csv |

## G214　b065「Region」（2 列：address 1・category 1）

多いほうの address の例：

- North East / North East / North East / North East / North East / North East / North East / North East（同じ表：Country・Country Code・Region Code・Second Tier Authority・Local Authority・Local Authority Code・Calendar Year・LA CO2 Sector）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | category | Africa / Africa / Americas / Americas / Asia/Pacific / Eastern Europe and Central Asia / Europe / Europe | UK Treaty Actions November 2015 - Februa | _data/file/539985/UK_treaty_actions_Nov_2015_to_Feb_2016.csv |

## G215　b065「ServiceTypeLabel」（3 列：category 2・account 1）

多いほうの category の例：

- Public toilets / Public toilets / Public toilets / Public toilets / Public toilets / Public toilets / Public toilets / Public toilets（同じ表：ExtractDate・OrganisationURI・OrganisationLabel・ServiceTypeURI・CoordinateReferenceSystem・GeoX・GeoY・GeoPointLicensingURL）
- Premises Licence / Premises Licence / Premises Licence / Premises Licence / Premises Licence / Premises Licence / Premises Licence / Premises Licence（同じ表：ExtractDate・OrganisationURI・OrganisationLabel・CaseReference・CaseDate・ServiceTypeURI・EntertainmentTypeURI・EntertainmentTypeLabel）

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | account | Staff- busines travel / Staff- busines travel / Staff - expenses / Members - allowances / Members - allowances / Members - allowances / Staff- busines travel / Staff - expenses | ExtractDate・OrganisationURI・OrganisationLabel・ServiceTypeURI・MonthOfClaim・MonthPaid・ExpenseType・Amount | eland.gov.uk/media/2622/sldc-expense-payments-sep-nov-14.csv |

## G216　jp3「区分」（9 列：category 6・account 2・date 1）

多いほうの category の例：

- 現 / 滞 / 現 / 滞 / 現 / 滞 / 現 / 滞（同じ表：税目・予算額（円）・調定件数・調定税額（円）・調定前年度比（％）・収入件数・収入税額（円）・収入前年度比（％））
- 債権 /  /  / 基金 /  /  /  / （同じ表：平成２８年度・平成２９年度・平成３０年度・令和元年度・令和２年度・令和３年度・令和４年度・令和５年度）
-  / 田 / 畑 / 宅地 / 山林 / 雑種地 /  / 1)本表中、田畑については一般田畑（勧告遊休田、介在田及び市街化区域農地を除く）、山林については 一般山林（介在山林（同じ表：地積・単位当たり最高価格・単位当たり平均価格（A）・提示平均価格 （B）・対比(A)/(B））

| 列 | 今の種類 | 値（先頭 8 個） | 同じ表の列 | 表 |
|---:|---|---|---|---|
| 2 | date | 2009 / 2010 / 2011 / 2012 / 2013 / 2014 / 2015 / 2016 | 総額・法定普通税小計・市民税個人・市民税法人・固定資産税・軽自動車税・市たばこ税・特別土地保有税 | /09f617d6-5a67-46d9-81f6-8e66721b8109/download/shizei001.csv |
| 3 | account | 市税 / 配当割交付金 / 株式等譲渡所得割交付金 / 地方交付税 / 分担金及び負担金 / 使用料及び手数料 / 国庫支出金 / 財産収入 | 決算額(千円）・構成比（％）・人口１人当たり（円） | rce/e0d2f74e-b3bc-498a-bdbe-6c9e2e7e14f6/download/5-14-.xlsx |
| 5 | account | 報酬 / 給料 / 共済費 / 報償費 / 旅費 / 使用料及び賃借料 / 備品購入費 / 負担金補助及び交付金 | 地方公共団体コード・都道府県・市町村・年月日・年度・項目・名目・節 | esource/02e5cf7d-0dff-44f4-97ef-7c40cf6d36a5/download/upload |

