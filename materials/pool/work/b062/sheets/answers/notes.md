# b062 ラベル付けメモ（LABEL_GUIDE v2.0）

## 個人・ケース単位の記録：該当するシート列をすべて S

- `Data_from_PDG_Survey_Dec_14_to_Feb_15.csv`（g0045–g0054）：回答者ごとのアンケート記録。
- `DCMS_Spads_hospitality_Jan-Mar2011.csv`（g0102–g0103）：担当者ごとの接待・歓待記録。
- `Ministerial_Returns_-_April_to_June_2017_-_Hospitality.csv`（g0103、g0128–g0129）：大臣ごとの歓待記録。
- `et-hospitality-jan-mar-2011.csv`（g0103、g0154–g0155）：役職者ごとの歓待記録。
- `desnz-permanent-secretarys-meetings-july-september-2023.csv`（g0117–g0118）：個人名と会議目的を記録した面会記録。
- `sos-return-oct-dec10.csv`（g0133–g0137）：大臣ごとの出張記録。
- `dsit-ministerial-gifts-april-june-2023.csv`（g0138–g0144）：大臣ごとの贈答記録。
- `dft-meetings-return-q1-2018.csv`（g0138、g0145）：大臣ごとの面会記録。
- `FCDO_MINISTERS_TRANSPARENCY_RETURN_Q3_OCT-DEC_2020-_GIFTS.csv`（g0138–g0139、g0184–g0188）：大臣ごとの贈答記録。
- `Gifts-Jan-March-21.csv`（g0139–g0142、g0144、g0189–g0190）：特別顧問ごとの贈答記録。
- `HMRC_senior_officials_hospitality_October_to_December_2017.csv`（g0139、g0215–g0216）：上級職員ごとの歓待記録。
- `dwp-ministerial-meetings-13-may-to-31-july-2010.csv`（g0156–g0158）：大臣ごとの面会記録。
- `dh_132528.csv`（g0159–g0162）：出張ごとの目的・行先・費用記録。
- `4-Qtr_1_Senior_Officials_Travel_Data.csv`（g0159、g0383–g0391）：上級職員ごとの出張記録。
- `FCDO_SENIOR_OFFICIALS_TRANSPARENCY_RETURN_Q3_OCT-DEC_2020_-_TRAVEL.csv`（g0191–g0200）：上級職員ごとの出張記録。
- `HMRC_senior_officials_business_expenses_January_to_March_2024.csv`（g0205–g0214）：上級職員の個別業務出費記録。
- `5-Qtr_2_Senior_Officials_Hospitality.csv`（g0215、g0392）：上級職員ごとの歓待記録。
- `Ministerial_travel_data.csv`（g0247–g0255）：大臣ごとの出張記録。

## 表の形・空値による S

- `car_parking_account_2013_14_published_09_10_2015.csv`（g0017–g0018）：見出しが「Staff」「131,953」で、値のカテゴリと金額が見出し位置に入った崩れた2列表。
- `Crown-Prosecution-Service-Facility-Time-Report-17-18.csv`（g0024–g0025）：指標名・割合・数値が混在し、見出しが列の種類を表していない。
- `final-greenhouse-gas-emissions-2020-by-source-dataset.csv`（g0123）：値がすべて空の列。
- `compendium-re-offending-stats-2013-csv.csv`（g0256–g0258）：コホート見出しの下に複数種類の指標・カテゴリが混在し、安定した列種類を判定できない崩れた表。
- `RushmoorContractsList.csv`（g0325–g0334）：見出し位置に番号・組織名・日付・金額などのデータ値が入っている。

S以外は、シートの見出し・例・同じ表の列をLABEL_GUIDE v2.0に照らして独立に判定しました。予測や他の先生の回答は見ていません。
