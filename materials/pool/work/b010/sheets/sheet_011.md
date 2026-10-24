# ラベル用シート 011 / 014

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_011.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1201（1 列）
- 見出し：Club_Venue_Suburb
- 例1 値：BOOLEROO CENTRE | LOXTON | CUMMINS | PORT ADELAIDE | BERRI
  - 同じ表の列：Club_Venue_State, Club_Venue_Sports

## g1202（1 列）
- 見出し：Club_Venue_State
- 例1 値：SA | SA | SA | SA | SA
  - 同じ表の列：Club_Venue_Suburb, Club_Venue_Sports

## g1203（1 列）
- 見出し：Club_Venue_Sports
- 例1 値：Athletics | Tennis | Australian Rules | Tennis | Table Tennis
  - 同じ表の列：Club_Venue_Suburb, Club_Venue_State

## g1204（1 列）
- 見出し：Collection_Date
- 例1 値：2017-06-03 | 2018-12-01 | 2018-06-12 | 2014-07-13 | 2018-06-05
  - 同じ表の列：Schedule_Code, Bin_Types, PickupDay, Actual_PickupDay, Comments

## g1205（1 列）
- 見出し：Schedule_Code
- 例1 値：1 | 2 | 2 | 1 | 1
  - 同じ表の列：Collection_Date, Bin_Types, PickupDay, Actual_PickupDay, Comments

## g1206（1 列）
- 見出し：Bin_Types
- 例1 値：General Waste (Blue Lid) & Organics (Gr… | General Waste (Blue Lid) & Organics (Gr… | General Waste (Blue Lid) & Organics (Gr… | General Waste (Blue Lid) & Organics (Gr… | General Waste (Blue Lid) & Organics (Gr…
  - 同じ表の列：Collection_Date, Schedule_Code, PickupDay, Actual_PickupDay, Comments

## g1207（1 列）
- 見出し：PickupDay
- 例1 値：Thursday | Friday | Monday | Thursday | Thursday
  - 同じ表の列：Collection_Date, Schedule_Code, Bin_Types, Actual_PickupDay, Comments

## g1208（1 列）
- 見出し：Actual_PickupDay
- 例1 値：NULL | NULL | NULL | NULL | NULL
  - 同じ表の列：Collection_Date, Schedule_Code, Bin_Types, PickupDay, Comments

## g1209（1 列）
- 見出し：Comments
- 例1 値：NULL | NULL | NULL | NULL | NULL
  - 同じ表の列：Collection_Date, Schedule_Code, Bin_Types, PickupDay, Actual_PickupDay

## g1210（1 列）
- 見出し：cartodb_id
- 例1 値：664 | 598 | 671 | 679 | 172
  - 同じ表の列：suburb, responsible_authori…, rest_area_number, site_status, lga, region, distance_from, road_number

## g1211（1 列）
- 見出し：responsible_authority
- 例1 値：Private | Private | Transport for NSW | Transport for NSW | Transport for NSW
  - 同じ表の列：cartodb_id, suburb, rest_area_number, site_status, lga, region, distance_from, road_number

## g1212（1 列）
- 見出し：rest_area_number
- 例1 値：1439 | 234 | 4514 | 817 | 1710
  - 同じ表の列：cartodb_id, suburb, responsible_authori…, site_status, lga, region, distance_from, road_number

## g1213（1 列）
- 見出し：site_status
- 例1 値：Open | Open | Open | Open | Open
  - 同じ表の列：cartodb_id, suburb, responsible_authori…, rest_area_number, lga, region, distance_from, road_number

## g1214（1 列）
- 見出し：lga
- 例1 値：BLAYNEY | SINGLETON | GUNNEDAH | CESSNOCK | TEMORA
  - 同じ表の列：cartodb_id, suburb, responsible_authori…, rest_area_number, site_status, region, distance_from, road_number

## g1215（1 列）
- 見出し：distance_from
- 例1 値：39km from Orange | 26km South of Nowra | 40km from Deniliquin and 82km to Hay | 1km South Casino | 41.6km from Wellington
  - 同じ表の列：cartodb_id, suburb, responsible_authori…, rest_area_number, site_status, lga, region, road_number

## g1216（1 列）
- 見出し：road_number
- 例1 値：6 | 8 | 7 | 12 | 76
  - 同じ表の列：cartodb_id, suburb, responsible_authori…, rest_area_number, site_status, lga, region, distance_from

## g1217（1 列）
- 見出し：link_no
- 例1 値：25 | 3340 | 1245 | 440 | 1500
  - 同じ表の列：cartodb_id, suburb, responsible_authori…, rest_area_number, site_status, lga, region, distance_from

## g1218（1 列）
- 見出し：ID_ESTACION_PUBLICO_ESPECIFICO
- 例1 値：3411 | 3375 | 4768 | 3411 | 4356
  - 同じ表の列：DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, DESC_TIPO_DESTINACAO, GEOMETRIA

## g1219（1 列）
- 見出し：DESTINACAO_ESPECIFICA
- 例1 値：MOTOFRETE | MOTOFRETE | MOTOFRETE | MOTOFRETE | MOTOFRETE
  - 同じ表の列：ID_ESTACION_PUBLICO…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, DESC_TIPO_DESTINACAO, GEOMETRIA

## g1220（1 列）
- 見出し：PERIODO_VALIDO_REGRA_OPERACAO
- 例1 値：08:00 ÀS 13:00 H | 08:00 ÀS 13:00 H | 08:00 ÀS 13:00 H | 08:00 ÀS 18:00 H | 08:00 ÀS 18:00 H
  - 同じ表の列：ID_ESTACION_PUBLICO…, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, DESC_TIPO_DESTINACAO, GEOMETRIA

## g1221（1 列）
- 見出し：TEMPO_PERMANENCIA
- 例1 値：1 HORA(S) | 1 HORA(S) | 1 HORA(S) | 1 HORA(S) | 1 HORA(S)
  - 同じ表の列：ID_ESTACION_PUBLICO…, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, DESC_TIPO_DESTINACAO, GEOMETRIA

## g1222（1 列）
- 見出し：DESC_TIPO_DESTINACAO
- 例1 値：MOTOFRETE | MOTOFRETE | MOTOFRETE | MOTOFRETE | MOTOFRETE
  - 同じ表の列：ID_ESTACION_PUBLICO…, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, GEOMETRIA

## g1223（1 列）
- 見出し：GEOMETRIA
- 例1 値：POINT (611920 7797037) | POINT (612085.44 7796209) | POINT (607925.6 7800253) | POINT (612921.75 7796865) | POINT (611149.56 7796793.5)
  - 同じ表の列：ID_ESTACION_PUBLICO…, DESTINACAO_ESPECIFI…, DIA_REGRA_OPERACAO, PERIODO_VALIDO_REGR…, NUMERO_VAGAS_FISICAS, NUMERO_VAGAS_ROTATI…, TEMPO_PERMANENCIA, DESC_TIPO_DESTINACAO

## g1224（1 列）
- 見出し：REGIONAL
- 例1 値：NOROESTE | NORDESTE | NORTE | BARREIRO | NORTE
  - 同じ表の列：CRAS, QTDE_FAMILIAS, MES_ANO_REFERENCIA

## g1225（1 列）
- 見出し：CRAS
- 例1 値：CRAS VILA SENHOR DOS PASSOS | CRAS VILA BIQUINHAS | CRAS APOLONIA | CRAS LAGOA | Endereço Fora Área CRAS
  - 同じ表の列：REGIONAL, QTDE_FAMILIAS, MES_ANO_REFERENCIA

## g1226（1 列）
- 見出し：QTDE_FAMILIAS
- 例1 値：2124 | 1742 | 1263 | 1865 | 1155
  - 同じ表の列：REGIONAL, CRAS, MES_ANO_REFERENCIA

## g1227（1 列）
- 見出し：MES_ANO_REFERENCIA
- 例1 値：012019 | 012019 | 012019 | 012019 | 012019
  - 同じ表の列：REGIONAL, CRAS, QTDE_FAMILIAS

## g1228（1 列）
- 見出し：ESCOLA
- 例1 値：CRECHE SANTA SOFIA | CENTRO DE EDUCACAO INFANTIL MARIA FLORI… | CRECHE INFANTIL OS TRES PORQUINHOS | CRECHE VOVO DUDU | CRECHE DO FREI CLAUDIO VAN BALEN
  - 同じ表の列：REGIONAL, INEP, BAIRRO, OFERTA REFEICAO

## g1229（1 列）
- 見出し：BAIRRO
- 例1 値：SANTA EFIGENIA | SANTA RITA DE CASSIA | POMPEIA | ALTO VERA CRUZ | PINDORAMA
  - 同じ表の列：REGIONAL, INEP, ESCOLA, OFERTA REFEICAO

## g1230（1 列）
- 見出し：OFERTA REFEICAO
- 例1 値：S | S | S | S | S
  - 同じ表の列：REGIONAL, INEP, ESCOLA, BAIRRO

## g1231（1 列）
- 見出し：INDICE_CADASTRAL
- 例1 値：483016 010 0020 | 494011 020B0016 | 510023 018 0595 | 150135 017 0015 | 489149 032 006X
  - 同じ表の列：NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g1232（1 列）
- 見出し：IND_REDE_ESGOTO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL

## g1233（1 列）
- 見出し：ID_COEF_CN_CENARIO_LEI11181
- 例1 値：126 | 242 | 114 | 41 | 238
  - 同じ表の列：SUBBACIA, AREA_M2, CNPD_LEI11181, GEOMETRIA

## g1234（1 列）
- 見出し：SUBBACIA
- 例1 値：4131303 | 4111403 | 4110005 | 4131201 | 4111904
  - 同じ表の列：ID_COEF_CN_CENARIO_…, AREA_M2, CNPD_LEI11181, GEOMETRIA

## g1235（1 列）
- 見出し：AREA_M2
- 例1 値：1327034.95 | 417071.32 | 2688712.97 | 1691407.17 | 504326.21
  - 同じ表の列：ID_COEF_CN_CENARIO_…, SUBBACIA, CNPD_LEI11181, GEOMETRIA

## g1236（1 列）
- 見出し：CNPD_LEI11181
- 例1 値：91.91 | 93.8 | 91.53 | 88.2 | 93.08
  - 同じ表の列：ID_COEF_CN_CENARIO_…, SUBBACIA, AREA_M2, GEOMETRIA

## g1237（1 列）
- 見出し：GEOMETRIA
- 例1 値：POLYGON ((606947.44 7798484,606888.5 77… | POLYGON ((616541.75 7798322,616531.25 7… | POLYGON ((606421.4 7793615.5,606406.1 7… | POLYGON ((613990.8 7797290.5,613969.4 7… | POLYGON ((617646.7 7808784.5,617644.4 7…
  - 同じ表の列：ID_COEF_CN_CENARIO_…, SUBBACIA, AREA_M2, CNPD_LEI11181

## g1238（1 列）
- 見出し：VIAGEM
- 例1 値：2022-03-15T00:00:00 | 2022-12-03T00:00:00 | 2022-10-03T00:00:00 | 2022-10-03T00:00:00 | 2022-10-03T00:00:00
  - 同じ表の列：LINHA, SUBLINHA, PC, CONCESSIONARIA, SAIDA, VEICULO, CHEGADA, CATRACA SAIDA

## g1239（1 列）
- 見出し：LINHA
- 例1 値：SC01A | SC01A | SC01A | SC01B | SC01A
  - 同じ表の列：VIAGEM, SUBLINHA, PC, CONCESSIONARIA, SAIDA, VEICULO, CHEGADA, CATRACA SAIDA

## g1240（1 列）
- 見出し：SUBLINHA
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：VIAGEM, LINHA, PC, CONCESSIONARIA, SAIDA, VEICULO, CHEGADA, CATRACA SAIDA

## g1241（1 列）
- 見出し：PC
- 例1 値：0 | 1 | 0 | 1 | 1
  - 同じ表の列：VIAGEM, LINHA, SUBLINHA, CONCESSIONARIA, SAIDA, VEICULO, CHEGADA, CATRACA SAIDA

## g1242（1 列）
- 見出し：CONCESSIONARIA
- 例1 値：801 | 801 | 801 | 801 | 801
  - 同じ表の列：VIAGEM, LINHA, SUBLINHA, PC, SAIDA, VEICULO, CHEGADA, CATRACA SAIDA

## g1243（1 列）
- 見出し：SAIDA
- 例1 値：09:47 | 06:07 | 05:41 | 05:21 | 05:40
  - 同じ表の列：VIAGEM, LINHA, SUBLINHA, PC, CONCESSIONARIA, VEICULO, CHEGADA, CATRACA SAIDA

## g1244（1 列）
- 見出し：VEICULO
- 例1 値：10961 | 40704 | 40704 | 10961 | 10961
  - 同じ表の列：VIAGEM, LINHA, SUBLINHA, PC, CONCESSIONARIA, SAIDA, CHEGADA, CATRACA SAIDA

## g1245（1 列）
- 見出し：CHEGADA
- 例1 値：16:04 | 09:36 | 05:14 | 11:21 | 07:14
  - 同じ表の列：VIAGEM, LINHA, SUBLINHA, PC, CONCESSIONARIA, SAIDA, VEICULO, CATRACA SAIDA

## g1246（1 列）
- 見出し：CATRACA SAIDA
- 例1 値：21744 | 80962 | 16405 | 30632 | 78092
  - 同じ表の列：VIAGEM, LINHA, SUBLINHA, PC, CONCESSIONARIA, SAIDA, VEICULO, CHEGADA

## g1247（1 列）
- 見出し：CATRACA CHEGADA
- 例1 値：53798 | 34970 | 48992 | 25459 | 28611
  - 同じ表の列：VIAGEM, LINHA, SUBLINHA, PC, CONCESSIONARIA, SAIDA, VEICULO, CHEGADA

## g1248（1 列）
- 見出し：ID_COMUNIDADE_QUILOMBOLA
- 例1 値：2 | 42 | 21 | 44 | 3
  - 同じ表の列：AREA_INCRA, PERIMETRO_INCRA, NUM_PROCESSO_INCRA, NUM_PROCESSO_FCP, SITUACAO, GEOMETRIA

## g1249（1 列）
- 見出し：AREA_INCRA
- 例1 値：0.0 | 22928.0 | 155080.0
  - 同じ表の列：ID_COMUNIDADE_QUILO…, PERIMETRO_INCRA, NUM_PROCESSO_INCRA, NUM_PROCESSO_FCP, SITUACAO, GEOMETRIA

## g1250（1 列）
- 見出し：PERIMETRO_INCRA
- 例1 値：1025.87 | 1833.8 | 0.0
  - 同じ表の列：ID_COMUNIDADE_QUILO…, AREA_INCRA, NUM_PROCESSO_INCRA, NUM_PROCESSO_FCP, SITUACAO, GEOMETRIA

## g1251（1 列）
- 見出し：NUM_PROCESSO_INCRA
- 例1 値：Não tem processo no INCRA | 54170.001373-2006-79 | 54000.104072-2019-72 | 54170.003740-2005-98 | 54170.006166-2007-91
  - 同じ表の列：ID_COMUNIDADE_QUILO…, AREA_INCRA, PERIMETRO_INCRA, NUM_PROCESSO_FCP, SITUACAO, GEOMETRIA

## g1252（1 列）
- 見出し：NUM_PROCESSO_FCP
- 例1 値：01420.101442-2020-46 | 01420.001223-2004-48 | 01420.003004-2005-84 | 01420.101304-2019-23 | 01420.000457-2007-11
  - 同じ表の列：ID_COMUNIDADE_QUILO…, AREA_INCRA, PERIMETRO_INCRA, NUM_PROCESSO_INCRA, SITUACAO, GEOMETRIA

## g1253（1 列）
- 見出し：SITUACAO
- 例1 値：Possui Relatório Técnico de Identificaç… | Fase de aproximação e mobilização. | Instaurado o processo administrativo. E… | Titulação da área atual de ocupação; e … | Portaria No 17 de 11-01-2016 publicada …
  - 同じ表の列：ID_COMUNIDADE_QUILO…, AREA_INCRA, PERIMETRO_INCRA, NUM_PROCESSO_INCRA, NUM_PROCESSO_FCP, GEOMETRIA

## g1254（1 列）
- 見出し：GEOMETRIA
- 例1 値：POLYGON ((608045.70 7794849.50, 608077.… | POLYGON ((608718.71 7799937.20, 608719.… | POLYGON ((614075.84 7807283.28, 614079.… | POLYGON ((614276.44 7796069.93, 614283.… | POLYGON ((613370.22 7797745.53, 613370.…
  - 同じ表の列：ID_COMUNIDADE_QUILO…, AREA_INCRA, PERIMETRO_INCRA, NUM_PROCESSO_INCRA, NUM_PROCESSO_FCP, SITUACAO

## g1255（1 列）
- 見出し：logan_passengers
- 例1 値：2342969 | 2297530 | 2016205 | 3136875 | 2422024
  - 同じ表の列：Year, Month, logan_intl_flights, hotel_occup_rate, hotel_avg_daily_rate, total_jobs, unemp_rate, labor_force_part_ra…

## g1256（1 列）
- 見出し：logan_intl_flights
- 例1 値：2780 | 4257 | 4153 | 3705 | 4400
  - 同じ表の列：Year, Month, logan_passengers, hotel_occup_rate, hotel_avg_daily_rate, total_jobs, unemp_rate, labor_force_part_ra…

## g1257（1 列）
- 見出し：hotel_occup_rate
- 例1 値：0.926 | 0.783 | 0.806 | 0.886 | 0.877
  - 同じ表の列：Year, Month, logan_passengers, logan_intl_flights, hotel_avg_daily_rate, total_jobs, unemp_rate, labor_force_part_ra…

## g1258（1 列）
- 見出し：hotel_avg_daily_rate
- 例1 値：244.45 | 337.92 | 223 | 223.2 | 259.62
  - 同じ表の列：Year, Month, logan_passengers, logan_intl_flights, hotel_occup_rate, total_jobs, unemp_rate, labor_force_part_ra…

## g1259（1 列）
- 見出し：total_jobs
- 例1 値：351598 | 329581 | 348670 | 340804 | 351084
  - 同じ表の列：Year, Month, logan_passengers, logan_intl_flights, hotel_occup_rate, hotel_avg_daily_rate, unemp_rate, labor_force_part_ra…

## g1260（1 列）
- 見出し：unemp_rate
- 例1 値：0.033 | 0.053 | 0.059 | 0.038 | 0.038
  - 同じ表の列：Year, Month, logan_passengers, logan_intl_flights, hotel_occup_rate, hotel_avg_daily_rate, total_jobs, labor_force_part_ra…

## g1261（1 列）
- 見出し：labor_force_part_rate
- 例1 値：0.662 | 0.642 | 0.67 | 0.67 | 0.644
  - 同じ表の列：Year, Month, logan_passengers, logan_intl_flights, hotel_occup_rate, hotel_avg_daily_rate, total_jobs, unemp_rate

## g1262（1 列）
- 見出し：pipeline_unit
- 例1 値：112 | 1000 | 1803 | 60 | 482
  - 同じ表の列：Year, Month, logan_passengers, logan_intl_flights, hotel_occup_rate, hotel_avg_daily_rate, total_jobs, unemp_rate

## g1263（1 列）
- 見出し：項目名
- 例1 値：Q9.2満足度 h.Discord(東京は設問なし) | Q22Wifi満足度 c.Tその他i subway free wifi(都営地… | Q6 行政サービス情報の収集方法 | Q11.2満足度 f.都の公式SNS / 海外は「行政の〜」 | Q12.3満足度 c.就職・退職に関する行政手続
  - 同じ表の列：データ形態, カテゴリー数, 質問文, 属性, 値

## g1264（2 列）
- 見出し：データ形態
- 例1 値：SA | SA | MA | SA | MA
  - 同じ表の列：項目名, カテゴリー数, 質問文, 属性, 値
- 例2 値：SA | SA | SA | SA | SA
  - 同じ表の列：項目名, カテゴリー数, 質問文, 属性, 値

## g1265（2 列）
- 見出し：カテゴリー数
- 例1 値：5 | 6 | 3 | 10 | 4
  - 同じ表の列：項目名, データ形態, 質問文, 属性, 値
- 例2 値：7 | 6 | 5 | 7 | 8
  - 同じ表の列：項目名, データ形態, 質問文, 属性, 値

## g1266（1 列）
- 見出し：質問文
- 例1 値：Q5: 日頃、行政サービスに関する情報をどこで目にしますか。 | Q10: 今後、どのSNSの活用を行政に期待しますか。 | Q13: 利用したことがない理由について当てはまるものをすべて選択してください。 | Q23: 社会のデジタル化が進むことについて、どう感じますか。 | Q20: 公衆無線lan(WiFi)の満足度について、当てはまるものを選択して…
  - 同じ表の列：項目名, データ形態, カテゴリー数, 属性, 値

## g1267（2 列）
- 見出し：属性
- 例1 値：4 | 1 | 2 | 5 | 4
  - 同じ表の列：項目名, データ形態, カテゴリー数, 質問文, 値
- 例2 値：2 | 2 | 1 | 2 | 5
  - 同じ表の列：項目名, データ形態, カテゴリー数, 質問文, 値

## g1268（1 列）
- 見出し：値
- 例1 値：特に理由はない | どちらかといえば満足 | 家族や友人がキャッシュレス決済をしているから | どちらかといえば不満 | 分からない
  - 同じ表の列：項目名, データ形態, カテゴリー数, 質問文, 属性

## g1269（1 列）
- 見出し：規模
- 例1 値：30人以上 | 5人以上 | 30人以上 | 5人以上 | 5人以上
  - 同じ表の列：産業, 現金給与総額/計(円), 現金給与総額/男(円), 現金給与総額/女(円), きまって支給する給与/計(円), きまって支給する給与/男(円), きまって支給する給与/女(円), 所定内給与(円)

## g1270（1 列）
- 見出し：産業
- 例1 値：生活関連サービス業,娯楽業 | 金融業,保険業 | 教育,学習支援業 | 建設業 | 医療,福祉
  - 同じ表の列：規模, 現金給与総額/計(円), 現金給与総額/男(円), 現金給与総額/女(円), きまって支給する給与/計(円), きまって支給する給与/男(円), きまって支給する給与/女(円), 所定内給与(円)

## g1271（1 列）
- 見出し：現金給与総額/計(円)
- 例1 値：605110 | 871931 | 797324 | 771207 | 307661
  - 同じ表の列：規模, 産業, 現金給与総額/男(円), 現金給与総額/女(円), きまって支給する給与/計(円), きまって支給する給与/男(円), きまって支給する給与/女(円), 所定内給与(円)

## g1272（1 列）
- 見出し：現金給与総額/男(円)
- 例1 値：492959 | 565377 | 573906 | 712554 | 648904
  - 同じ表の列：規模, 産業, 現金給与総額/計(円), 現金給与総額/女(円), きまって支給する給与/計(円), きまって支給する給与/男(円), きまって支給する給与/女(円), 所定内給与(円)

## g1273（1 列）
- 見出し：現金給与総額/女(円)
- 例1 値：411415 | 158423 | 234384 | 472633 | 381745
  - 同じ表の列：規模, 産業, 現金給与総額/計(円), 現金給与総額/男(円), きまって支給する給与/計(円), きまって支給する給与/男(円), きまって支給する給与/女(円), 所定内給与(円)

## g1274（1 列）
- 見出し：きまって支給する給与/計(円)
- 例1 値：318470 | 415133 | 435733 | 383408 | 482948
  - 同じ表の列：規模, 産業, 現金給与総額/計(円), 現金給与総額/男(円), 現金給与総額/女(円), きまって支給する給与/男(円), きまって支給する給与/女(円), 所定内給与(円)

## g1275（1 列）
- 見出し：きまって支給する給与/男(円)
- 例1 値：796003 | 718814 | 453777 | 429859 | 222106
  - 同じ表の列：規模, 産業, 現金給与総額/計(円), 現金給与総額/男(円), 現金給与総額/女(円), きまって支給する給与/計(円), きまって支給する給与/女(円), 所定内給与(円)

## g1276（1 列）
- 見出し：きまって支給する給与/女(円)
- 例1 値：601540 | 327926 | 415416 | 260195 | 352065
  - 同じ表の列：規模, 産業, 現金給与総額/計(円), 現金給与総額/男(円), 現金給与総額/女(円), きまって支給する給与/計(円), きまって支給する給与/男(円), 所定内給与(円)

## g1277（1 列）
- 見出し：所定内給与(円)
- 例1 値：344741 | 495940 | 389391 | 356489 | 352145
  - 同じ表の列：規模, 産業, 現金給与総額/計(円), 現金給与総額/男(円), 現金給与総額/女(円), きまって支給する給与/計(円), きまって支給する給与/男(円), きまって支給する給与/女(円)

## g1278（1 列）
- 見出し：所定外給与(円)
- 例1 値：13941 | 21001 | 23224 | 40230 | 31119
  - 同じ表の列：規模, 産業, 現金給与総額/計(円), 現金給与総額/男(円), 現金給与総額/女(円), きまって支給する給与/計(円), きまって支給する給与/男(円), きまって支給する給与/女(円)

## g1279（1 列）
- 見出し：測定地点(局)
- 例1 値：般 | 一 | 部 | 沿 | 般
  - 同じ表の列：ベンゼン, トリクロロ エチレン, テトラクロロエチレン, ジクロロ メタン, アクリロ ニトリル, 塩化ビニル モノマー

## g1280（1 列）
- 見出し：ベンゼン
- 例1 値：0.79 | 0.71 | 0.3 | 0.18 | 0.9
  - 同じ表の列：測定地点(局), トリクロロ エチレン, テトラクロロエチレン, ジクロロ メタン, アクリロ ニトリル, 塩化ビニル モノマー

## g1281（1 列）
- 見出し：トリクロロ エチレン
- 例1 値：1 | 0.1 | 2.7 | 環境基準 | 0.06
  - 同じ表の列：測定地点(局), ベンゼン, テトラクロロエチレン, ジクロロ メタン, アクリロ ニトリル, 塩化ビニル モノマー

## g1282（1 列）
- 見出し：テトラクロロエチレン
- 例1 値：0.07 | 0.24 | 0.13 | 0.12 | 0.06
  - 同じ表の列：測定地点(局), ベンゼン, トリクロロ エチレン, ジクロロ メタン, アクリロ ニトリル, 塩化ビニル モノマー

## g1283（1 列）
- 見出し：ジクロロ メタン
- 例1 値：1.2 | 0.078 | 150 | 2 | 酸化 エチレン
  - 同じ表の列：測定地点(局), ベンゼン, トリクロロ エチレン, テトラクロロエチレン, アクリロ ニトリル, 塩化ビニル モノマー

## g1284（1 列）
- 見出し：アクリロ ニトリル
- 例1 値：塩化メチル | 1.5 | 1.4 | 1.4 | 0.13
  - 同じ表の列：測定地点(局), ベンゼン, トリクロロ エチレン, テトラクロロエチレン, ジクロロ メタン, 塩化ビニル モノマー

## g1285（1 列）
- 見出し：塩化ビニル モノマー
- 例1 値：0.1 | 4.7 | 6.7 | <0.03 | 4.5
  - 同じ表の列：測定地点(局), ベンゼン, トリクロロ エチレン, テトラクロロエチレン, ジクロロ メタン, アクリロ ニトリル

## g1286（1 列）
- 見出し：配置
- 例1 値：D | F | C | E | A
  - 同じ表の列：施設名, 設置場所, 営業時間・利用時間, サイズ・口数(コインロッカー), ホームページ, PASMO対応

## g1287（1 列）
- 見出し：施設名
- 例1 値：ATM(みずほ銀行) | コインロッカー | モバイルバッテリースタンド(ChargeSPOT) | ATM(セブン銀行) | コインロッカー
  - 同じ表の列：配置, 設置場所, 営業時間・利用時間, サイズ・口数(コインロッカー), ホームページ, PASMO対応

## g1288（1 列）
- 見出し：設置場所
- 例1 値：B2階改札外コンコース(東西線九段下駅中野方面乗換方 階段横) | B2階改札外コンコース(1出口階段付近) | B2階改札外コンコース(3・4出口階段横) | B2階改札外コンコース(3・4出口階段下) | B2階改札外コンコース(1出口階段付近)
  - 同じ表の列：配置, 施設名, 営業時間・利用時間, サイズ・口数(コインロッカー), ホームページ, PASMO対応

## g1289（1 列）
- 見出し：営業時間・利用時間
- 例1 値：【全日】7時から21時まで | 【全日】5時から24時まで | 【月曜】7時から24時まで【火曜〜金曜】5時から24時まで【土曜】5時から22…
  - 同じ表の列：配置, 施設名, 設置場所, サイズ・口数(コインロッカー), ホームページ, PASMO対応

## g1290（1 列）
- 見出し：サイズ・口数(コインロッカー)
- 例1 値：【大型】2口【中型】2口【標準】8口 | 【大型】2口【中型】2口【標準】23口
  - 同じ表の列：配置, 施設名, 設置場所, 営業時間・利用時間, ホームページ, PASMO対応

## g1291（1 列）
- 見出し：ホームページ
- 例1 値：https://www.kobeyarestaurant.co.jp/fres…
  - 同じ表の列：配置, 施設名, 設置場所, 営業時間・利用時間, サイズ・口数(コインロッカー), PASMO対応

## g1292（1 列）
- 見出し：PASMO対応
- 例1 値：○ | ○ | ○
  - 同じ表の列：配置, 施設名, 設置場所, 営業時間・利用時間, サイズ・口数(コインロッカー), ホームページ

## g1293（1 列）
- 見出し：名称
- 例1 値：神田まちかど図書館 | 昌平まちかど図書館 | 四番町図書館 | 千代田図書館 | 日比谷図書文化館
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称_カナ, 名称_英字, 名称_通称, POIコード, 建物名等(方書), 法人番号

## g1294（1 列）
- 見出し：名称_カナ
- 例1 値：チヨダトショカン | ヨンバンチョウトショカン | ショウヘイマチカドトショカン | ヒビヤトショブンカカン | カンダマチカドトショカン
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_英字, 名称_通称, POIコード, 建物名等(方書), 法人番号

## g1295（1 列）
- 見出し：名称_英字
- 例1 値：CHIYODA LIBRARY | Hibiya Library & Museum
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_通称, POIコード, 建物名等(方書), 法人番号

## g1296（1 列）
- 見出し：名称_通称
- 例1 値：チヨダトショカン
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英字, POIコード, 建物名等(方書), 法人番号

## g1297（1 列）
- 見出し：建物名等(方書)
- 例1 値：千代田区役所9・10階 | 昌平童夢館1階 | 神田さくら館1階
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 名称_通称, POIコード, 法人番号

## g1298（1 列）
- 見出し：名称
- 例1 値：ちゅうおう区議会だより令和2年第1回臨時会号 | ちゅうおう区議会だより平成26年第2回定例会号 | ちゅうおう区議会だより令和5年第2回定例会号 | ちゅうおう区議会だより平成23年第1回定例会号 | ちゅうおう区議会だより平成30年第3回定例会号
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 号数, 発行年月, 発行元

## g1299（1 列）
- 見出し：発行元
- 例1 値：中央区議会議会局 | 中央区議会議会局 | 中央区議会議会局 | 中央区議会議会局 | 中央区議会議会局
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 号数, 発行年月

## g1300（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 号数, 発行年月, 発行元

## g1301（1 列）
- 見出し：名称
- 例1 値：令和3年第4回臨時会・令和4年第1回定例会号 | 平成18年新年号 | 平成22年第3回定例会号 | 平成20年第1回定例会号 | 令和7年第2回臨時会号
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 号数, 発行年月, 発行元

## g1302（1 列）
- 見出し：発行元
- 例1 値：新宿区議会 | 新宿区議会 | 新宿区議会 | 新宿区議会 | 新宿区議会
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 号数, 発行年月

## g1303（1 列）
- 見出し：名称
- 例1 値：文京区営関口二丁目アパート | 文京区営白山四丁目アパート | シルバーピアはくさん台 | シルバーピア向丘 | シルバーピア根津
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 建物名等(方書), 面積, 間取り, 建設年度, 管理戸数, 一般

## g1304（1 列）
- 見出し：建物名等(方書)
- 例1 値：3号棟 | 1号棟 | 2号棟
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 面積, 間取り, 建設年度, 管理戸数, 一般

## g1305（2 列）
- 見出し：面積
- 例1 値：33-44 | 24-27 | 28-42 | 28-39 | 39-39
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 建物名等(方書), 間取り, 建設年度, 管理戸数, 一般
- 例2 値：54-70 | 56-66 | 44-44 | 56-70 | 65-65
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 建物名等(方書), 間取り, 建設年度, 管理戸数

## g1306（4 列）
- 見出し：間取り
- 例1 値：1DK-2DK | 1DK-2DK | 3DK-3DK | 1DK-1DK | 3DK-3DK
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 建物名等(方書), 面積, 建設年度, 管理戸数, 一般
- 例2 値：1DK-1DK | 1K-1K | 2DK-3DK | 2DK-2DK | 1DK-2DK
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 面積, 建設年度, 管理戸数, 備考1_種別1

## g1307（4 列）
- 見出し：建設年度
- 例1 値：1992 | 1972 | 1995 | 1988 | 2003
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 建物名等(方書), 面積, 間取り, 管理戸数, 一般
- 例2 値：2000 | 2000 | 1996 | 2012 | 2021
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 面積, 間取り, 管理戸数, 備考1_種別1

## g1308（5 列）
- 見出し：管理戸数
- 例1 値：14 | 18 | 6 | 19 | 28
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 建物名等(方書), 面積, 間取り, 建設年度, 一般
- 例2 値：18 | 10 | 24 | 27 | 20
  - 同じ表の列：全国地方公共団体コード, 名称, シルバーピア

## g1309（3 列）
- 見出し：一般
- 例1 値：18 | 8 | 21 | 18 | 15
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 建物名等(方書), 面積, 間取り, 建設年度, 管理戸数
- 例2 値：14 | 9 | 12 | 12 | 9
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称, 建物名等(方書), 面積, 間取り, 建設年度

## g1310（2 列）
- 見出し：シルバーピア
- 例1 値：26 | 20 | 12 | 32 | 12
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 建物名等(方書), 面積, 間取り, 建設年度, 管理戸数
- 例2 値：20 | 2 | 18 | 20 | 10
  - 同じ表の列：全国地方公共団体コード, 名称, 管理戸数

## g1311（1 列）
- 見出し：名称
- 例1 値：シルバーピア浅草 | シルバーピア寿 | シルバーピアかっぱ橋 | シルバーピア蔵前 | シルバーピア東泉
  - 同じ表の列：全国地方公共団体コード, 管理戸数, シルバーピア

## g1312（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都江東区 | 東京都江東区 | 東京都江東区 | 東京都江東区 | 東京都江東区
  - 同じ表の列：全国地方公共団体コード, 名称

## g1313（1 列）
- 見出し：名称
- 例1 値：1970 HOTEL | 東京スタイル301.303 | TOKYO HIBI KIYOSUMI | Wabisabi Kameido | Nexus Villa Morishita
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名

## g1314（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区
  - 同じ表の列：全国地方公共団体コード, 確認番号, 名称, 確認年月日

## g1315（1 列）
- 見出し：確認番号
- 例1 値：第22号 | 30品保生環き第3号 | 品保生環き第51号 | 品保衛環き第68号 | 31品保生環き第4号
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 確認年月日

## g1316（1 列）
- 見出し：名称
- 例1 値：イシス美容室 | Moanin’ | Coiffeur秀樹 | チャーム美容室 | パルサーアンドアリス
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 確認番号, 確認年月日

## g1317（1 列）
- 見出し：確認年月日
- 例1 値：2015-07-15T00:00:00 | 2020-04-15T00:00:00 | 2012-03-19T00:00:00 | 2011-10-21T00:00:00 | 2019-05-24T00:00:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 確認番号, 名称

## g1318（1 列）
- 見出し：名称
- 例1 値：ヘアーカット専門店 HUI | 野寺理容室 | 下鳥理容所 | 美悠 | ヘアーサロン ニューチェリー
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名

## g1319（1 列）
- 見出し：名称
- 例1 値：せたがや区議会だより令和7年第1回区議会臨時会・第1回定例会号 | せたがや区議会だより令和6年第4回区議会定例会号 | せたがや区議会だより令和6年第3回区議会定例会号 | せたがや区議会だより令和7年第2回区議会臨時会号 | せたがや区議会だより令和7年第2回区議会定例会号
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 号数, 発行年月, 発行元, 町字ID

## g1320（1 列）
- 見出し：発行元
- 例1 値：世田谷区議会事務局 | 世田谷区議会事務局 | 世田谷区議会事務局 | 世田谷区議会事務局 | 世田谷区議会事務局
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 号数, 発行年月, 町字ID

## 答えの雛形

```
g1201	
g1202	
g1203	
g1204	
g1205	
g1206	
g1207	
g1208	
g1209	
g1210	
g1211	
g1212	
g1213	
g1214	
g1215	
g1216	
g1217	
g1218	
g1219	
g1220	
g1221	
g1222	
g1223	
g1224	
g1225	
g1226	
g1227	
g1228	
g1229	
g1230	
g1231	
g1232	
g1233	
g1234	
g1235	
g1236	
g1237	
g1238	
g1239	
g1240	
g1241	
g1242	
g1243	
g1244	
g1245	
g1246	
g1247	
g1248	
g1249	
g1250	
g1251	
g1252	
g1253	
g1254	
g1255	
g1256	
g1257	
g1258	
g1259	
g1260	
g1261	
g1262	
g1263	
g1264	
g1265	
g1266	
g1267	
g1268	
g1269	
g1270	
g1271	
g1272	
g1273	
g1274	
g1275	
g1276	
g1277	
g1278	
g1279	
g1280	
g1281	
g1282	
g1283	
g1284	
g1285	
g1286	
g1287	
g1288	
g1289	
g1290	
g1291	
g1292	
g1293	
g1294	
g1295	
g1296	
g1297	
g1298	
g1299	
g1300	
g1301	
g1302	
g1303	
g1304	
g1305	
g1306	
g1307	
g1308	
g1309	
g1310	
g1311	
g1312	
g1313	
g1314	
g1315	
g1316	
g1317	
g1318	
g1319	
g1320	
```
