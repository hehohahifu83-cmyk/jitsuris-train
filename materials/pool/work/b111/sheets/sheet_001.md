# ラベル用シート 001 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：TRANSPORT_TYPE
- 例1 値：TOT | TOT | TOT | TOT | TOT
  - 同じ表の列：TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0002（1 列）
- 見出し：TRANSPORT_MEAN
- 例1 値：TOT | TOT | TOT | TOT | TOT
  - 同じ表の列：TRANSPORT_TYPE, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0003（1 列）
- 見出し：TRAVEL_REASON
- 例1 値：SCHOOL | OTH_REAS | SHOP | SERV_ACC | SERV_ACC
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0004（1 列）
- 見出し：SOCIO_DEMO_VARIABLE_TYPE
- 例1 値：URB_RUR | HH_INC | GEO | DAY | LANG_REG
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0005（1 列）
- 見出し：SOCIO_DEMO_VARIABLE
- 例1 値：CHF_GE12001 | CH07 | CH04 | CH03 | DK_NOANS
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, PERIOD_REF, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0006（1 列）
- 見出し：PERIOD_REF
- 例1 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, UNIT_MEAS, VALUE, OBS_CONFIDENCE

## g0007（1 列）
- 見出し：UNIT_MEAS
- 例1 値：NBSTAGE | KM | NBSTAGE | KM | MIN
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, VALUE, OBS_CONFIDENCE

## g0008（2 列）
- 見出し：VALUE
- 例1 値：0.0161 | 9.1736 | 32.8589 | 0.8814 | 1.2850
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, OBS_CONFIDENCE
- 例2 値：19.83176391 | 18.00290116 | 8.677926653 | 56.13801021 | 27.22128861
  - 同じ表の列：REF_YEAR, GEO_COMM, GEO_CANT

## g0009（1 列）
- 見出し：OBS_CONFIDENCE
- 例1 値：0.2424 | 0.7803 | 0.4471 | 0.1612 | 0.0173
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE

## g0010（1 列）
- 見出し：OBS_STATUS
- 例1 値：A | A | U | A | A
  - 同じ表の列：TRANSPORT_TYPE, TRANSPORT_MEAN, TRAVEL_REASON, SOCIO_DEMO_VARIABLE…, SOCIO_DEMO_VARIABLE, PERIOD_REF, UNIT_MEAS, VALUE

## g0011（2 列）
- 見出し：REF_YEAR
- 例1 値：2023 | 2023 | 2023 | 2023 | 2023
  - 同じ表の列：GEO_COMM, GEO_CANT, VALUE
- 例2 値：2014 | 2014 | 2014 | 2014 | 2014
  - 同じ表の列：PERSPECTIVE, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE

## g0012（1 列）
- 見出し：GEO_COMM
- 例1 値：1002 | 97 | 991 | 571 | 2309
  - 同じ表の列：REF_YEAR, GEO_CANT, VALUE

## g0013（1 列）
- 見出し：GEO_CANT
- 例1 値：BE | BE | BE | BL | BE
  - 同じ表の列：REF_YEAR, GEO_COMM, VALUE

## g0014（1 列）
- 見出し：PERSPECTIVE
- 例1 値：R | R | R | R | R
  - 同じ表の列：REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE

## g0015（1 列）
- 見出し：GEO_CANT_RESID
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE

## g0016（1 列）
- 見出し：GEO_COMM_RESID
- 例1 値：3 | 6 | 32 | 4 | 24
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_CANT_WORK, GEO_COMM_WORK, VALUE

## g0017（1 列）
- 見出し：GEO_CANT_WORK
- 例1 値：77 | 1 | 1 | 1 | 1
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_COMM_WORK, VALUE

## g0018（1 列）
- 見出し：GEO_COMM_WORK
- 例1 値：7777 | 66 | 7777 | 1701 | 1702
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, VALUE

## g0019（1 列）
- 見出し：VALUE
- 例1 値：6 | 16 | 11 | 11 | 16
  - 同じ表の列：PERSPECTIVE, REF_YEAR, GEO_CANT_RESID, GEO_COMM_RESID, GEO_CANT_WORK, GEO_COMM_WORK

## g0020（1 列）
- 見出し：Jahr_Monat
- 例1 値：2026-09 | 2026-09 | 2026-09 | 2026-09 | 2026-09
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Fahrzeugart, Treibstoff, Anzahl

## g0021（1 列）
- 見出し：BFS_Gemeindenummer
- 例1 値：2762 | 2771 | 2766 | 2773 | 2764
  - 同じ表の列：Jahr_Monat, Gemeinde, Fahrzeugart, Treibstoff, Anzahl

## g0022（1 列）
- 見出し：Gemeinde
- 例1 値：Brislach | Bottmingen | Muttenz | Burg im Leimental | Biel-Benken BL
  - 同じ表の列：Jahr_Monat, BFS_Gemeindenummer, Fahrzeugart, Treibstoff, Anzahl

## g0023（1 列）
- 見出し：Fahrzeugart
- 例1 値：Gelenkbus | Traktor | Sportgeräteanhänger | Personenwagen | Schwerer Motorwagen
  - 同じ表の列：Jahr_Monat, BFS_Gemeindenummer, Gemeinde, Treibstoff, Anzahl

## g0024（1 列）
- 見出し：Treibstoff
- 例1 値：Diesel | Elektrisch | Benzin | Diesel | Diesel
  - 同じ表の列：Jahr_Monat, BFS_Gemeindenummer, Gemeinde, Fahrzeugart, Anzahl

## g0025（1 列）
- 見出し：Anzahl
- 例1 値：10 | 100 | 3 | 6 | 5
  - 同じ表の列：Jahr_Monat, BFS_Gemeindenummer, Gemeinde, Fahrzeugart, Treibstoff

## g0026（2 列）
- 見出し：Anfangszeit
- 例1 値：2017-03-30T21:00:00+00:00 | 2017-03-30T18:30:00+00:00 | 2017-03-23T16:00:00+00:00 | 2017-03-24T00:30:00+00:00 | 2017-03-18T23:00:00+00:00
  - 同じ表の列：PM10, NO2, O3
- 例2 値：2016-11-17T07:30:00+00:00 | 2016-11-21T19:00:00+00:00 | 2016-11-29T07:00:00+00:00 | 2016-11-21T21:30:00+00:00 | 2016-11-10T15:00:00+00:00
  - 同じ表の列：NO2

## g0027（1 列）
- 見出し：PM10
- 例1 値：17.38275484 | 23.66198428 | 14.04253281 | 15.81939277 | 24.59756389
  - 同じ表の列：Anfangszeit, NO2, O3

## g0028（2 列）
- 見出し：NO2
- 例1 値：64.89740104 | 21.73700556 | 20.56477151 | 20.75408827 | 14.95315518
  - 同じ表の列：Anfangszeit, PM10, O3
- 例2 値：24.2918256 | 13.00682596 | 15.79819633 | 13.39655076 | 24.27843957
  - 同じ表の列：Anfangszeit

## g0029（1 列）
- 見出し：O3
- 例1 値：82.21195053 | 81.80896055 | 20.12356391 | 61.71133164 | 46.23212749
  - 同じ表の列：Anfangszeit, PM10, NO2

## g0030（2 列）
- 見出し：Datum/Zeit
- 例1 値：2026-10-23T07:00:00+00:00 | 2026-10-25T02:00:00+00:00 | 2026-10-18T08:00:00+00:00 | 2026-10-20T21:00:00+00:00 | 2026-10-28T10:00:00+00:00
  - 同じ表の列：timestamp_text, PM10 (Stundenmittel…, PM2.5 (Stundenmitte…, O3 (Stundenmittelwe…, NO2 (Stundenmittelw…, geo_point_2d
- 例2 値：2026-10-27T09:00:00+00:00 | 2026-10-21T11:00:00+00:00 | 2026-09-23T16:00:00+00:00 | 2026-10-26T00:00:00+00:00 | 2026-09-21T06:00:00+00:00
  - 同じ表の列：timestamp_text, pm10_stundenmittelw…, pm2_5_stundenmittel…, no2_stundenmittelwe…, o3_stundenmittelwer…, geo_point_2d

## g0031（2 列）
- 見出し：timestamp_text
- 例1 値：2026-09-22 14:00:00 | 2026-10-13 09:00:00 | 2026-10-08 12:00:00 | 2026-10-30 02:00:00 | 2026-10-07 00:00:00
  - 同じ表の列：Datum/Zeit, PM10 (Stundenmittel…, PM2.5 (Stundenmitte…, O3 (Stundenmittelwe…, NO2 (Stundenmittelw…, geo_point_2d
- 例2 値：2026-10-11 17:00:00 | 2026-09-27 11:00:00 | 2026-09-27 23:00:00 | 2026-10-01 16:00:00 | 2026-10-21 04:00:00
  - 同じ表の列：Datum/Zeit, pm10_stundenmittelw…, pm2_5_stundenmittel…, no2_stundenmittelwe…, o3_stundenmittelwer…, geo_point_2d

## g0032（1 列）
- 見出し：PM10 (Stundenmittelwerte)
- 例1 値：6.125 | 12.903 | 11.924 | 14.814 | 15.642
  - 同じ表の列：Datum/Zeit, timestamp_text, PM2.5 (Stundenmitte…, O3 (Stundenmittelwe…, NO2 (Stundenmittelw…, geo_point_2d

## g0033（1 列）
- 見出し：PM2.5 (Stundenmittelwerte)
- 例1 値：7.493 | 8.21 | 8.645 | 1.903 | 11.045
  - 同じ表の列：Datum/Zeit, timestamp_text, PM10 (Stundenmittel…, O3 (Stundenmittelwe…, NO2 (Stundenmittelw…, geo_point_2d

## g0034（1 列）
- 見出し：O3 (Stundenmittelwerte)
- 例1 値：37.591 | 58.688 | 67.849 | 72.269 | 62.282
  - 同じ表の列：Datum/Zeit, timestamp_text, PM10 (Stundenmittel…, PM2.5 (Stundenmitte…, NO2 (Stundenmittelw…, geo_point_2d

## g0035（1 列）
- 見出し：NO2 (Stundenmittelwerte)
- 例1 値：33.512 | 18.714 | 14.987 | 32.541 | 11.069
  - 同じ表の列：Datum/Zeit, timestamp_text, PM10 (Stundenmittel…, PM2.5 (Stundenmitte…, O3 (Stundenmittelwe…, geo_point_2d

## g0036（2 列）
- 見出し：geo_point_2d
- 例1 値：47.5659354, 7.58192 | 47.5659354, 7.58192 | 47.5659354, 7.58192 | 47.5659354, 7.58192 | 47.5659354, 7.58192
  - 同じ表の列：Datum/Zeit, timestamp_text, PM10 (Stundenmittel…, PM2.5 (Stundenmitte…, O3 (Stundenmittelwe…, NO2 (Stundenmittelw…
- 例2 値：47.5670167, 7.5925446 | 47.5670167, 7.5925446 | 47.5670167, 7.5925446 | 47.5670167, 7.5925446 | 47.5670167, 7.5925446
  - 同じ表の列：Datum/Zeit, timestamp_text, pm10_stundenmittelw…, pm2_5_stundenmittel…, no2_stundenmittelwe…, o3_stundenmittelwer…

## g0037（1 列）
- 見出し：ZST_NR (Text)
- 例1 値：659 | 350 | 409 | 409 | 405
  - 同じ表の列：ZST_NR (numerisch), SiteCode, DateTimeFrom, DateTimeTo, LaneCode, ValuesApproved, ValuesEdited, TrafficType

## g0038（1 列）
- 見出し：ZST_NR (numerisch)
- 例1 値：406 | 408 | 405 | 402 | 415
  - 同じ表の列：ZST_NR (Text), SiteCode, DateTimeFrom, DateTimeTo, LaneCode, ValuesApproved, ValuesEdited, TrafficType

## g0039（1 列）
- 見出し：SiteCode
- 例1 値：00000405 | 00000405 | 00000417 | 00000405 | 00000350
  - 同じ表の列：ZST_NR (Text), ZST_NR (numerisch), DateTimeFrom, DateTimeTo, LaneCode, ValuesApproved, ValuesEdited, TrafficType

## g0040（1 列）
- 見出し：DateTimeFrom
- 例1 値：2026-10-29T14:00:00+00:00 | 2026-10-29T17:00:00+00:00 | 2026-10-29T07:00:00+00:00 | 2026-10-29T14:00:00+00:00 | 2026-10-29T16:00:00+00:00
  - 同じ表の列：ZST_NR (Text), ZST_NR (numerisch), SiteCode, DateTimeTo, LaneCode, ValuesApproved, ValuesEdited, TrafficType

## g0041（1 列）
- 見出し：DateTimeTo
- 例1 値：2026-10-29T19:00:00+00:00 | 2026-10-29T18:00:00+00:00 | 2026-10-29T07:00:00+00:00 | 2026-10-29T07:00:00+00:00 | 2026-10-29T04:00:00+00:00
  - 同じ表の列：ZST_NR (Text), ZST_NR (numerisch), SiteCode, DateTimeFrom, LaneCode, ValuesApproved, ValuesEdited, TrafficType

## g0042（1 列）
- 見出し：LaneCode
- 例1 値：1 | 2 | 6 | 1 | 2
  - 同じ表の列：ZST_NR (Text), ZST_NR (numerisch), SiteCode, DateTimeFrom, DateTimeTo, ValuesApproved, ValuesEdited, TrafficType

## g0043（1 列）
- 見出し：ValuesApproved
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：ZST_NR (Text), ZST_NR (numerisch), SiteCode, DateTimeFrom, DateTimeTo, LaneCode, ValuesEdited, TrafficType

## g0044（1 列）
- 見出し：ValuesEdited
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：ZST_NR (Text), ZST_NR (numerisch), SiteCode, DateTimeFrom, DateTimeTo, LaneCode, ValuesApproved, TrafficType

## g0045（1 列）
- 見出し：TrafficType
- 例1 値：MIV | MIV | MIV | MIV | MIV
  - 同じ表の列：ZST_NR (Text), ZST_NR (numerisch), SiteCode, DateTimeFrom, DateTimeTo, LaneCode, ValuesApproved, ValuesEdited

## g0046（1 列）
- 見出し：Total
- 例1 値：36 | 323 | 291 | 723 | 494
  - 同じ表の列：ZST_NR (Text), ZST_NR (numerisch), SiteCode, DateTimeFrom, DateTimeTo, LaneCode, ValuesApproved, ValuesEdited

## g0047（1 列）
- 見出し：pm10_stundenmittelwerte_ug_m3
- 例1 値：11.357 | 15.976 | 9.654 | 20.427 | 15.927
  - 同じ表の列：Datum/Zeit, timestamp_text, pm2_5_stundenmittel…, no2_stundenmittelwe…, o3_stundenmittelwer…, geo_point_2d

## g0048（1 列）
- 見出し：pm2_5_stundenmittelwerte_ug_m3
- 例1 値：1.926 | 11.684 | 5.045 | 16.64 | 4.202
  - 同じ表の列：Datum/Zeit, timestamp_text, pm10_stundenmittelw…, no2_stundenmittelwe…, o3_stundenmittelwer…, geo_point_2d

## g0049（1 列）
- 見出し：no2_stundenmittelwerte_ug_m3
- 例1 値：35.761 | 23.619 | 7.871 | 33.161 | 19.689
  - 同じ表の列：Datum/Zeit, timestamp_text, pm10_stundenmittelw…, pm2_5_stundenmittel…, o3_stundenmittelwer…, geo_point_2d

## g0050（1 列）
- 見出し：o3_stundenmittelwerte_ug_m3
- 例1 値：38.369 | 70.042 | 37.918 | 57.946 | 54.559
  - 同じ表の列：Datum/Zeit, timestamp_text, pm10_stundenmittelw…, pm2_5_stundenmittel…, no2_stundenmittelwe…, geo_point_2d

## g0051（1 列）
- 見出し：kategorie
- 例1 値：Finanzielles | Geschwindigkeitskontrollen | Geschwindigkeitskontrollen | Statistische Zahlen Ordnungsbussen | Geschwindigkeitskontrollen
  - 同じ表の列：kennzahl, jahr, wert

## g0052（1 列）
- 見出し：kennzahl
- 例1 値：Übertretungsquote in % | Ordnungsbussenertrag (in Schweizer Fran… | Strafanzeigen aus semi-stationären und … | Übertretungen Gesetz über die Abfallbew… | Ordnungsbussen aus semi-stationärne und…
  - 同じ表の列：kategorie, jahr, wert

## g0053（3 列）
- 見出し：jahr
- 例1 値：2023 | 2023 | 2024 | 2024 | 2024
  - 同じ表の列：kategorie, kennzahl, wert
- 例2 値：2025 | 2023 | 2024 | 2023 | 2024
  - 同じ表の列：bussentyp_code, bussentyp, anzahl_bussen

## g0054（1 列）
- 見出し：wert
- 例1 値：3125.0 | 17206.0 | 18892.0 | 790842.85 | 2348.0
  - 同じ表の列：kategorie, kennzahl, jahr

## g0055（1 列）
- 見出し：bussentyp_code
- 例1 値：21 | 7 | 4 | 4 | 6
  - 同じ表の列：jahr, bussentyp, anzahl_bussen

## g0056（1 列）
- 見出し：bussentyp
- 例1 値：OB-Zettel | Gemeindeabtretungen | Film GK | Gemeindeabtretungen | Combiniert RL/GK
  - 同じ表の列：jahr, bussentyp_code, anzahl_bussen

## g0057（1 列）
- 見出し：anzahl_bussen
- 例1 値：4875 | 14073 | 124031 | 6012 | 438
  - 同じ表の列：jahr, bussentyp_code, bussentyp

## g0058（1 列）
- 見出し：fahrzeugart_code
- 例1 値：001 | 001 | 001 | 001 | 001
  - 同じ表の列：fahrzeugart, marken_code, marke, typengenehmigungs_nr, karosserieform_code, karosserieform, farbe, sitzplaetze

## g0059（1 列）
- 見出し：fahrzeugart
- 例1 値：Personenwagen | Personenwagen | Personenwagen | Personenwagen | Personenwagen
  - 同じ表の列：fahrzeugart_code, marken_code, marke, typengenehmigungs_nr, karosserieform_code, karosserieform, farbe, sitzplaetze

## g0060（1 列）
- 見出し：marken_code
- 例1 値：7102 | 7907 | 7907 | 4050 | 7116
  - 同じ表の列：fahrzeugart_code, fahrzeugart, marke, typengenehmigungs_nr, karosserieform_code, karosserieform, farbe, sitzplaetze

## g0061（1 列）
- 見出し：marke
- 例1 値：OPEL | OPEL | OPEL | KIA | OPEL
  - 同じ表の列：fahrzeugart_code, fahrzeugart, marken_code, typengenehmigungs_nr, karosserieform_code, karosserieform, farbe, sitzplaetze

## g0062（1 列）
- 見出し：typengenehmigungs_nr
- 例1 値：1OA693 | 1SC704 | 1OA680 | 1OA607 | 1DB154
  - 同じ表の列：fahrzeugart_code, fahrzeugart, marken_code, marke, karosserieform_code, karosserieform, farbe, sitzplaetze

## g0063（1 列）
- 見出し：karosserieform_code
- 例1 値：161 | 161 | 161 | 161 | 163
  - 同じ表の列：fahrzeugart_code, fahrzeugart, marken_code, marke, typengenehmigungs_nr, karosserieform, farbe, sitzplaetze

## g0064（1 列）
- 見出し：karosserieform
- 例1 値：Limousine | Stationswagen | Limousine | Limousine | Limousine
  - 同じ表の列：fahrzeugart_code, fahrzeugart, marken_code, marke, typengenehmigungs_nr, karosserieform_code, farbe, sitzplaetze

## g0065（1 列）
- 見出し：farbe
- 例1 値：Rot | Schwarz | Grün | Blau | Grün
  - 同じ表の列：fahrzeugart_code, fahrzeugart, marken_code, marke, typengenehmigungs_nr, karosserieform_code, karosserieform, sitzplaetze

## g0066（1 列）
- 見出し：sitzplaetze
- 例1 値：5 | 5 | 4 | 7 | 5
  - 同じ表の列：fahrzeugart_code, fahrzeugart, marken_code, marke, typengenehmigungs_nr, karosserieform_code, karosserieform, farbe

## g0067（1 列）
- 見出し：stehplaetze
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：fahrzeugart_code, fahrzeugart, marken_code, marke, typengenehmigungs_nr, karosserieform_code, karosserieform, farbe

## g0068（2 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:1088:313603 | ch:1:sloid:8100:382713 | ch:1:sloid:3307:490370 | ch:1:sloid:3305:961518 | ch:1:sloid:6025:302462
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo
- 例2 値：ch:1:sloid:8064:182048 | ch:1:sloid:79238:130998 | ch:1:sloid:18400:784985 | ch:1:sloid:1021:325599 | ch:1:sloid:8314:348029
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom, validTo

## g0069（3 列）
- 見出し：parentSloidServicePoint
- 例1 値：ch:1:sloid:5205 | ch:1:sloid:1280 | ch:1:sloid:2033 | ch:1:sloid:9400 | ch:1:sloid:6005
  - 同じ表の列：sloid, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo
- 例2 値：ch:1:sloid:9673 | ch:1:sloid:4286 | ch:1:sloid:71484 | ch:1:sloid:87848 | ch:1:sloid:6602
  - 同じ表の列：sloid, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0070（3 列）
- 見出し：parentNumberServicePoint
- 例1 値：8506294 | 8506003 | 8504100 | 8503103 | 8502199
  - 同じ表の列：sloid, parentSloidServiceP…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo
- 例2 値：8591269 | 8579394 | 8572119 | 8572797 | 8506602
  - 同じ表の列：sloid, parentSloidServiceP…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0071（1 列）
- 見出し：designation
- 例1 値：Parking | Bahnhof | Parking | Parking | Parking
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0072（1 列）
- 見出し：additionalInformation
- 例1 値：44 / 1 Parkplätze | 203 / 5 Parkplätze Bahnhof ist aktuell … | 32 / 1 Parkplätze | 16 / 1 Parkplätze | 6 Parkplätze
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0073（1 列）
- 見出し：placesAvailable
- 例1 値：YES | YES | YES | YES | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, prmPlacesAvailable, validFrom, validTo

## g0074（1 列）
- 見出し：prmPlacesAvailable
- 例1 値：YES | YES | NO | YES | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, validFrom, validTo

## g0075（2 列）
- 見出し：validFrom
- 例1 値：2021-07-21T00:00:00 | 2023-04-21T00:00:00 | 2023-07-06T00:00:00 | 2023-08-08T00:00:00 | 2021-10-06T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validTo
- 例2 値：2023-09-12T00:00:00 | 2022-08-30T00:00:00 | 2023-07-04T00:00:00 | 2023-11-28T00:00:00 | 2021-07-21T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validTo

## g0076（2 列）
- 見出し：validTo
- 例1 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom
- 例2 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom

## g0077（2 列）
- 見出し：creationDate
- 例1 値：2022-02-15T11:50:12 | 2023-10-30T15:44:57 | 2022-02-15T08:49:19 | 2023-11-06T08:45:05 | 2022-04-12T07:03:23
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom
- 例2 値：2023-06-29T07:02:37 | 2022-07-15T13:20:31 | 2022-07-28T08:26:41 | 2022-07-11T05:25:23 | 2022-03-30T08:16:37
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, referencePointType, validFrom

## g0078（1 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:4029:2:2 | ch:1:sloid:75464:0:684372 | ch:1:sloid:4305:0:1 | ch:1:sloid:78259:1:50 | ch:1:sloid:91445::11
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0079（1 列）
- 見出し：boardingDevice
- 例1 値：LIFTS | NO | NO | LIFTS | NOT_APPLICABLE
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, shuttle, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0080（1 列）
- 見出し：shuttle
- 例1 値：NO | YES | NO | NO | NO
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, contrastingAreas, dynamicAudio, dynamicVisual, height

## g0081（1 列）
- 見出し：contrastingAreas
- 例1 値：YES | YES | YES | NO | NO
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, dynamicAudio, dynamicVisual, height

## g0082（1 列）
- 見出し：dynamicAudio
- 例1 値：YES | NO | YES | YES | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicVisual, height

## g0083（1 列）
- 見出し：dynamicVisual
- 例1 値：NO | YES | YES | NO | NO
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, height

## g0084（1 列）
- 見出し：height
- 例1 値：16.0 | 30.0 | 14.0 | 6.0 | 16.0
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual

## g0085（1 列）
- 見出し：inclination
- 例1 値：1.0 | -2.0 | 2.0 | 2.0 | 2.0
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, boardingDevice, shuttle, contrastingAreas, dynamicAudio, dynamicVisual

## g0086（1 列）
- 見出し：designation
- 例1 値：Hauptzugang | Infosäule | Kundencenterbereich Bahnhofplatz | Perron | Bahnhofplatz
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, mainReferencePoint, additionalInformati…, referencePointType, validFrom, validTo

## g0087（1 列）
- 見出し：mainReferencePoint
- 例1 値：true | true | true | true | true
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, referencePointType, validFrom, validTo

## g0088（1 列）
- 見出し：additionalInformation
- 例1 値：Der Referenzpunkt befindet sich beim Üb… | Haupteingang nordseitig bei der Treppe … | Überdachung Hausperron | Kundencenter Bahnhofplatz | Il faut marcher depuis le début de la p…
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, referencePointType, validFrom, validTo

## g0089（1 列）
- 見出し：referencePointType
- 例1 値：MAIN_STATION_ENTRANCE | PLATFORM | PLATFORM | MAIN_STATION_ENTRANCE | PLATFORM
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, mainReferencePoint, additionalInformati…, validFrom, validTo

## g0090（1 列）
- 見出し：Datum
- 例1 値：2020-06-12 | 2020-06-18 | 2020-06-17 | 2020-06-14 | 2020-06-17
  - 同じ表の列：Bad_ID, Besucherstand, Max. Kapazitat wahr…, Bemerkung Max. Kapa…

## g0091（1 列）
- 見出し：Bad_ID
- 例1 値：c5ed7622ecbf1f | c5ed761e9a9100 | c5ed761e9a9100 | c5ed761e9a9100 | c5ed76249da809
  - 同じ表の列：Datum, Besucherstand, Max. Kapazitat wahr…, Bemerkung Max. Kapa…

## g0092（1 列）
- 見出し：Besucherstand
- 例1 値：28 | 5 | 18 | 45 | 22
  - 同じ表の列：Datum, Bad_ID, Max. Kapazitat wahr…, Bemerkung Max. Kapa…

## g0093（1 列）
- 見出し：Max. Kapazitat wahrend Corona
- 例1 値：1780 | 30 | 1480 | 1480 | 1200
  - 同じ表の列：Datum, Bad_ID, Besucherstand, Bemerkung Max. Kapa…

## g0094（1 列）
- 見出し：Bemerkung Max. Kapazitaten
- 例1 値：Eislaufen im Winter für max. 180 Person… | Vom 13.05.20 bis 30.5.20 normal geöffne… | Eislaufen im Winter für max. 180 Person… | Eislaufen im Winter für max. 180 Person… | Vom 13.05.20 bis 30.5.20 normal geöffne…
  - 同じ表の列：Datum, Bad_ID, Besucherstand, Max. Kapazitat wahr…

## g0095（1 列）
- 見出し：Kanton
- 例1 値：St. Gallen | St. Gallen | St. Gallen | St. Gallen | St. Gallen
  - 同じ表の列：Gemeinde, PLZ, Location, is_disabled, is_reserved, Provider_ID, vehicle_type_id

## g0096（1 列）
- 見出し：Gemeinde
- 例1 値：St. Gallen | St. Gallen | St. Gallen | St. Gallen | St. Gallen
  - 同じ表の列：Kanton, PLZ, Location, is_disabled, is_reserved, Provider_ID, vehicle_type_id

## g0097（1 列）
- 見出し：PLZ
- 例1 値：9008 | 9000 | 9000 | 9011 | 9014
  - 同じ表の列：Kanton, Gemeinde, Location, is_disabled, is_reserved, Provider_ID, vehicle_type_id

## g0098（1 列）
- 見出し：Location
- 例1 値：47.430504, 9.373842 | 47.430984, 9.373722 | 47.40429, 9.341804 | 47.41216, 9.348002 | 47.426632, 9.378333
  - 同じ表の列：Kanton, Gemeinde, PLZ, is_disabled, is_reserved, Provider_ID, vehicle_type_id

## g0099（1 列）
- 見出し：is_disabled
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Kanton, Gemeinde, PLZ, Location, is_reserved, Provider_ID, vehicle_type_id

## g0100（1 列）
- 見出し：is_reserved
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Kanton, Gemeinde, PLZ, Location, is_disabled, Provider_ID, vehicle_type_id

## g0101（1 列）
- 見出し：Provider_ID
- 例1 値：dott_st-gallen | dott_st-gallen | dott_st-gallen | dott_st-gallen | dott_st-gallen
  - 同じ表の列：Kanton, Gemeinde, PLZ, Location, is_disabled, is_reserved, vehicle_type_id

## g0102（1 列）
- 見出し：vehicle_type_id
- 例1 値：dott_st-gallen:dott_scooter | dott_st-gallen:dott_scooter | dott_st-gallen:dott_scooter | dott_st-gallen:dott_scooter | dott_st-gallen:dott_scooter
  - 同じ表の列：Kanton, Gemeinde, PLZ, Location, is_disabled, is_reserved, Provider_ID

## g0103（1 列）
- 見出し：stichtag
- 例1 値：2014-12-31 | 2024-12-31 | 2020-12-31 | 2016-12-31 | 2012-12-31
  - 同じ表の列：jahr, noga082_id, noga082, betriebe, betriebe_ist_kleing…, beschaeftigte, vzae

## g0104（1 列）
- 見出し：noga082_id
- 例1 値：13 | 56 | 41 | 93 | 52
  - 同じ表の列：jahr, stichtag, noga082, betriebe, betriebe_ist_kleing…, beschaeftigte, vzae

## g0105（1 列）
- 見出し：noga082
- 例1 値：Maschinenbau | Metallerzeugung und -bearbeitung | Mit Finanz- und Versicherungsdienstleis… | Lagerei sowie Erbringung von sonstigen … | Vorbereitende Baustellenarbeiten, Bauin…
  - 同じ表の列：jahr, stichtag, noga082_id, betriebe, betriebe_ist_kleing…, beschaeftigte, vzae

## g0106（1 列）
- 見出し：betriebe
- 例1 値：53 | 28 | 81 | 25 | 6
  - 同じ表の列：jahr, stichtag, noga082_id, noga082, betriebe_ist_kleing…, beschaeftigte, vzae

## g0107（1 列）
- 見出し：betriebe_ist_kleingruppe
- 例1 値：False | False | False | False | False
  - 同じ表の列：jahr, stichtag, noga082_id, noga082, betriebe, beschaeftigte, vzae

## g0108（1 列）
- 見出し：beschaeftigte
- 例1 値：6 | 162 | 6802 | 1696 | 128
  - 同じ表の列：jahr, stichtag, noga082_id, noga082, betriebe, betriebe_ist_kleing…, vzae

## g0109（1 列）
- 見出し：vzae
- 例1 値：15.66 | 86.5 | 456.6 | 173.64 | 92.79
  - 同じ表の列：jahr, stichtag, noga082_id, noga082, betriebe, betriebe_ist_kleing…, beschaeftigte

## g0110（1 列）
- 見出し：id
- 例1 値：bundesbeschluss-uber-die-finanzierung-u… | bundesbeschluss-uber-die-finanzierung-u… | bundesbeschluss-uber-die-finanzierung-u… | bundesbeschluss-uber-die-finanzierung-u… | bundesbeschluss-uber-die-finanzierung-u…
  - 同じ表の列：title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0111（1 列）
- 見出し：title_de_CH
- 例1 値：Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u…
  - 同じ表の列：id, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0112（1 列）
- 見出し：title_fr_CH
- 例1 値：Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u…
  - 同じ表の列：id, title_de_CH, title_it_CH, title_rm_CH, date, shortcode, domain, status

## g0113（1 列）
- 見出し：title_it_CH
- 例1 値：Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_rm_CH, date, shortcode, domain, status

## g0114（1 列）
- 見出し：title_rm_CH
- 例1 値：Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u… | Bundesbeschluss über die Finanzierung u…
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, date, shortcode, domain, status

## g0115（1 列）
- 見出し：date
- 例1 値：2014-02-09 | 2014-02-09 | 2014-02-09 | 2014-02-09 | 2014-02-09
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, shortcode, domain, status

## g0116（1 列）
- 見出し：shortcode
- 例1 値：E1 | E1 | E1 | E1 | E1
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, domain, status

## g0117（1 列）
- 見出し：domain
- 例1 値：federation | federation | federation | federation | federation
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, status

## g0118（1 列）
- 見出し：status
- 例1 値：unknown | unknown | unknown | unknown | unknown
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain

## g0119（1 列）
- 見出し：answer
- 例1 値：accepted | accepted | accepted | accepted | accepted
  - 同じ表の列：id, title_de_CH, title_fr_CH, title_it_CH, title_rm_CH, date, shortcode, domain

## g0120（3 列）
- 見出し：BFS_NR
- 例1 値：34 | 13 | 37 | 42 | 2
  - 同じ表の列：INDIKATOR_ID, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_KURZ, EINHEIT_LANG
- 例2 値：6 | 42 | 23 | 54 | 8
  - 同じ表の列：INDIKATOR_ID, INDIKATOR_JAHR, INDIKATOR_VALUE, EINHEIT_KURZ, EINHEIT_LANG

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
g0008	
g0009	
g0010	
g0011	
g0012	
g0013	
g0014	
g0015	
g0016	
g0017	
g0018	
g0019	
g0020	
g0021	
g0022	
g0023	
g0024	
g0025	
g0026	
g0027	
g0028	
g0029	
g0030	
g0031	
g0032	
g0033	
g0034	
g0035	
g0036	
g0037	
g0038	
g0039	
g0040	
g0041	
g0042	
g0043	
g0044	
g0045	
g0046	
g0047	
g0048	
g0049	
g0050	
g0051	
g0052	
g0053	
g0054	
g0055	
g0056	
g0057	
g0058	
g0059	
g0060	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
g0067	
g0068	
g0069	
g0070	
g0071	
g0072	
g0073	
g0074	
g0075	
g0076	
g0077	
g0078	
g0079	
g0080	
g0081	
g0082	
g0083	
g0084	
g0085	
g0086	
g0087	
g0088	
g0089	
g0090	
g0091	
g0092	
g0093	
g0094	
g0095	
g0096	
g0097	
g0098	
g0099	
g0100	
g0101	
g0102	
g0103	
g0104	
g0105	
g0106	
g0107	
g0108	
g0109	
g0110	
g0111	
g0112	
g0113	
g0114	
g0115	
g0116	
g0117	
g0118	
g0119	
g0120	
```
