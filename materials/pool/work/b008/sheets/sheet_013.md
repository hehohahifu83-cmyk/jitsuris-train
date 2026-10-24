# ラベル用シート 013 / 013

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_013.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1441（1 列）
- 見出し：INEP
- 例1 値：31357740 | 31250651 | 31362140 | 31357375 | 31361810
  - 同じ表の列：REGIONAL, ESCOLA, TURNO, EI_0_A_1_ANO, EI_1_A_2_ANOS, EI_2_A_3_ANOS, EI_3_A_4_ANOS, EI_4_A_5_ANOS

## g1442（1 列）
- 見出し：TURNO
- 例1 値：NOITE | TARDE | MANHÃ | MANHÃ | INTEGRAL
  - 同じ表の列：REGIONAL, ESCOLA, INEP, EI_0_A_1_ANO, EI_1_A_2_ANOS, EI_2_A_3_ANOS, EI_3_A_4_ANOS, EI_4_A_5_ANOS

## g1443（1 列）
- 見出し：EI_0_A_1_ANO
- 例1 値：0 | 0 | 0 | 14 | 0
  - 同じ表の列：REGIONAL, ESCOLA, INEP, TURNO, EI_1_A_2_ANOS, EI_2_A_3_ANOS, EI_3_A_4_ANOS, EI_4_A_5_ANOS

## g1444（1 列）
- 見出し：EI_1_A_2_ANOS
- 例1 値：0 | 0 | 0 | 27 | 0
  - 同じ表の列：REGIONAL, ESCOLA, INEP, TURNO, EI_0_A_1_ANO, EI_2_A_3_ANOS, EI_3_A_4_ANOS, EI_4_A_5_ANOS

## g1445（1 列）
- 見出し：EI_2_A_3_ANOS
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：REGIONAL, ESCOLA, INEP, TURNO, EI_0_A_1_ANO, EI_1_A_2_ANOS, EI_3_A_4_ANOS, EI_4_A_5_ANOS

## g1446（1 列）
- 見出し：EI_3_A_4_ANOS
- 例1 値：0 | 38 | 0 | 0 | 0
  - 同じ表の列：REGIONAL, ESCOLA, INEP, TURNO, EI_0_A_1_ANO, EI_1_A_2_ANOS, EI_2_A_3_ANOS, EI_4_A_5_ANOS

## g1447（1 列）
- 見出し：EI_4_A_5_ANOS
- 例1 値：0 | 0 | 0 | 52 | 58
  - 同じ表の列：REGIONAL, ESCOLA, INEP, TURNO, EI_0_A_1_ANO, EI_1_A_2_ANOS, EI_2_A_3_ANOS, EI_3_A_4_ANOS

## g1448（1 列）
- 見出し：EI_5_A_6_ANOS
- 例1 値：38 | 0 | 51 | 0 | 0
  - 同じ表の列：REGIONAL, ESCOLA, INEP, TURNO, EI_0_A_1_ANO, EI_1_A_2_ANOS, EI_2_A_3_ANOS, EI_3_A_4_ANOS

## g1449（1 列）
- 見出し：INDICE_CADASTRAL
- 例1 値：964102 010 0019 | 908091 035A2401 | 971011 008 0013 | 957038 301 254X | 890030 022 0412
  - 同じ表の列：NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g1450（1 列）
- 見出し：NULOTCTM
- 例1 値：210579000435 | 190748000150 | 190421101100 | 190761300350 | 210057900015
  - 同じ表の列：INDICE_CADASTRAL, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g1451（1 列）
- 見出し：ZONEAMENTO_PVIPTU
- 例1 値：ZAP | ZAP | ZAP | ZAR2 | ZAR2
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g1452（1 列）
- 見出し：FREQUENCIA_COLETA
- 例1 値：COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g1453（1 列）
- 見出し：IND_MEIO_FIO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g1454（1 列）
- 見出し：IND_PAVIMENTACAO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g1455（1 列）
- 見出し：IND_ARBORIZACAO
- 例1 値：NÃO | NÃO | NÃO | NÃO | NÃO
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g1456（1 列）
- 見出し：IND_GALERIA_PLUVIAL
- 例1 値：NÃO | NÃO | NÃO | SIM | NÃO
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_ILUMINACAO_PUBL…

## g1457（1 列）
- 見出し：IND_ILUMINACAO_PUBLICA
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL

## g1458（1 列）
- 見出し：IND_REDE_ESGOTO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL

## g1459（1 列）
- 見出し：ID_ISA_SUB_BACIA
- 例1 値：230 | 109 | 144 | 27 | 74
  - 同じ表の列：COD_SUB_BACIA, AREA_SUB_BACIA, POPULACAO_SUB_BACIA, DENSIDADE_SUB_BACIA, IAB_SUB_BACIA, POPULACAO_SEM_REDE_…, POPULACAO_COM_REDE_…, ICE_SUB_BACIA

## g1460（1 列）
- 見出し：COD_SUB_BACIA
- 例1 値：4130401 | 4112202 | 4131100 | 4130813 | 4140206
  - 同じ表の列：ID_ISA_SUB_BACIA, AREA_SUB_BACIA, POPULACAO_SUB_BACIA, DENSIDADE_SUB_BACIA, IAB_SUB_BACIA, POPULACAO_SEM_REDE_…, POPULACAO_COM_REDE_…, ICE_SUB_BACIA

## g1461（1 列）
- 見出し：AREA_SUB_BACIA
- 例1 値：74.9 | 128.92 | 82.9 | 99.84 | 531.48
  - 同じ表の列：ID_ISA_SUB_BACIA, COD_SUB_BACIA, POPULACAO_SUB_BACIA, DENSIDADE_SUB_BACIA, IAB_SUB_BACIA, POPULACAO_SEM_REDE_…, POPULACAO_COM_REDE_…, ICE_SUB_BACIA

## g1462（1 列）
- 見出し：POPULACAO_SUB_BACIA
- 例1 値：37994 | 21137 | 18829 | 14828 | 13834
  - 同じ表の列：ID_ISA_SUB_BACIA, COD_SUB_BACIA, AREA_SUB_BACIA, DENSIDADE_SUB_BACIA, IAB_SUB_BACIA, POPULACAO_SEM_REDE_…, POPULACAO_COM_REDE_…, ICE_SUB_BACIA

## g1463（1 列）
- 見出し：DENSIDADE_SUB_BACIA
- 例1 値：5.33 | 26.98 | 183.7 | 84.78 | 10.23
  - 同じ表の列：ID_ISA_SUB_BACIA, COD_SUB_BACIA, AREA_SUB_BACIA, POPULACAO_SUB_BACIA, IAB_SUB_BACIA, POPULACAO_SEM_REDE_…, POPULACAO_COM_REDE_…, ICE_SUB_BACIA

## g1464（1 列）
- 見出し：IAB_SUB_BACIA
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：ID_ISA_SUB_BACIA, COD_SUB_BACIA, AREA_SUB_BACIA, POPULACAO_SUB_BACIA, DENSIDADE_SUB_BACIA, POPULACAO_SEM_REDE_…, POPULACAO_COM_REDE_…, ICE_SUB_BACIA

## g1465（1 列）
- 見出し：POPULACAO_SEM_REDE_COLETORA
- 例1 値：2047 | 0 | 131 | 1 | 112
  - 同じ表の列：ID_ISA_SUB_BACIA, COD_SUB_BACIA, AREA_SUB_BACIA, POPULACAO_SUB_BACIA, DENSIDADE_SUB_BACIA, IAB_SUB_BACIA, POPULACAO_COM_REDE_…, ICE_SUB_BACIA

## g1466（1 列）
- 見出し：POPULACAO_COM_REDE_COLETORA
- 例1 値：1643 | 8596 | 23070 | 13195 | 23112
  - 同じ表の列：ID_ISA_SUB_BACIA, COD_SUB_BACIA, AREA_SUB_BACIA, POPULACAO_SUB_BACIA, DENSIDADE_SUB_BACIA, IAB_SUB_BACIA, POPULACAO_SEM_REDE_…, ICE_SUB_BACIA

## g1467（1 列）
- 見出し：ICE_SUB_BACIA
- 例1 値：0.98 | 1 | 1 | 0.448 | 0.978
  - 同じ表の列：ID_ISA_SUB_BACIA, COD_SUB_BACIA, AREA_SUB_BACIA, POPULACAO_SUB_BACIA, DENSIDADE_SUB_BACIA, IAB_SUB_BACIA, POPULACAO_SEM_REDE_…, POPULACAO_COM_REDE_…

## g1468（1 列）
- 見出し：POPULACAO_SEM_INTERCEPTACAO
- 例1 値：0 | 1350 | 67 | 0 | 137
  - 同じ表の列：ID_ISA_SUB_BACIA, COD_SUB_BACIA, AREA_SUB_BACIA, POPULACAO_SUB_BACIA, DENSIDADE_SUB_BACIA, IAB_SUB_BACIA, POPULACAO_SEM_REDE_…, POPULACAO_COM_REDE_…

## g1469（1 列）
- 見出し：TIPO_CARTAO
- 例1 値：DEFICIENTE | DEFICIENTE | DEFICIENTE | DEFICIENTE | DEFICIENTE
  - 同じ表の列：DATA, FAIXA_HORARIA_ORIGEM, H3_ORIGEM, H3_DESTINO

## g1470（1 列）
- 見出し：DATA
- 例1 値：2024-11-10 | 2024-11-10 | 2024-11-10 | 2024-11-10 | 2024-11-10
  - 同じ表の列：TIPO_CARTAO, FAIXA_HORARIA_ORIGEM, H3_ORIGEM, H3_DESTINO

## g1471（1 列）
- 見出し：FAIXA_HORARIA_ORIGEM
- 例1 値：16 | 18 | 5 | 15 | 11
  - 同じ表の列：TIPO_CARTAO, DATA, H3_ORIGEM, H3_DESTINO

## g1472（1 列）
- 見出し：H3_ORIGEM
- 例1 値：89a88cd994bffff | 89a88ccb4b7ffff | 89a881a4a07ffff | 89a88cda0bbffff | 89a881acdb7ffff
  - 同じ表の列：TIPO_CARTAO, DATA, FAIXA_HORARIA_ORIGEM, H3_DESTINO

## g1473（1 列）
- 見出し：H3_DESTINO
- 例1 値：89a88cd954fffff | 89a88cdb3c7ffff | 89a88cd9333ffff | 89a88cd954fffff | 89a881a4aa3ffff
  - 同じ表の列：TIPO_CARTAO, DATA, FAIXA_HORARIA_ORIGEM, H3_ORIGEM

## g1474（1 列）
- 見出し：VILAS CONJUNTOS ZEIS
- 例1 値：CONFISCO | SAO JORGE II | SAO JORGE I | ZILAH SPOSITO | JATOBA IV
  - 同じ表の列：REG, BAIRRO, LOTES REGULARIZADOS, DOMICILIOS BENEFICI…, DECRETOS DE APROVAC…, PLANTAS DE APROVACAO, ANO DA REGULARIZACAO, CARTORIO DE REGISTRO

## g1475（1 列）
- 見出し：REG
- 例1 値：N | B | B | O | N
  - 同じ表の列：VILAS CONJUNTOS ZEIS, BAIRRO, LOTES REGULARIZADOS, DOMICILIOS BENEFICI…, DECRETOS DE APROVAC…, PLANTAS DE APROVACAO, ANO DA REGULARIZACAO, CARTORIO DE REGISTRO

## g1476（1 列）
- 見出し：BAIRRO
- 例1 値：CIDADE JARDIM | BAIRRO DA GLORIA | CONFISCO | JARDIM FELICIDADE JARDIM GUANABARA TUPI… | VILA VISTA ALEGRE
  - 同じ表の列：VILAS CONJUNTOS ZEIS, REG, LOTES REGULARIZADOS, DOMICILIOS BENEFICI…, DECRETOS DE APROVAC…, PLANTAS DE APROVACAO, ANO DA REGULARIZACAO, CARTORIO DE REGISTRO

## g1477（1 列）
- 見出し：LOTES REGULARIZADOS
- 例1 値：611 | 412 | 88 | 449 | 1324
  - 同じ表の列：VILAS CONJUNTOS ZEIS, REG, BAIRRO, DOMICILIOS BENEFICI…, DECRETOS DE APROVAC…, PLANTAS DE APROVACAO, ANO DA REGULARIZACAO, CARTORIO DE REGISTRO

## g1478（1 列）
- 見出し：DOMICILIOS BENEFICIADOS
- 例1 値：17 | 463 | 578 | 97 | 376
  - 同じ表の列：VILAS CONJUNTOS ZEIS, REG, BAIRRO, LOTES REGULARIZADOS, DECRETOS DE APROVAC…, PLANTAS DE APROVACAO, ANO DA REGULARIZACAO, CARTORIO DE REGISTRO

## g1479（1 列）
- 見出し：DECRETOS DE APROVACAO
- 例1 値：N 6 818 DE 25 04 1991 | N 8 926 DE 26 09 1996, N 9 452 DE 17 12… | N 7 221 DE 19 05 1992 | N 10 483 DE 09 02 2001 | N 5 978 DE 24 06 1988
  - 同じ表の列：VILAS CONJUNTOS ZEIS, REG, BAIRRO, LOTES REGULARIZADOS, DOMICILIOS BENEFICI…, PLANTAS DE APROVACAO, ANO DA REGULARIZACAO, CARTORIO DE REGISTRO

## g1480（1 列）
- 見出し：PLANTAS DE APROVACAO
- 例1 値：CP 276 001 M | CP 045 451 M a CP 045 454 M | CP 050 008 M a CP 050 012 M | CP 279 009 M a CP 279 026 M | CP 297 027 M a CP 297 047 M
  - 同じ表の列：VILAS CONJUNTOS ZEIS, REG, BAIRRO, LOTES REGULARIZADOS, DOMICILIOS BENEFICI…, DECRETOS DE APROVAC…, ANO DA REGULARIZACAO, CARTORIO DE REGISTRO

## g1481（1 列）
- 見出し：ANO DA REGULARIZACAO
- 例1 値：1989 | 2016 | 1988 | 1992 | 1990
  - 同じ表の列：VILAS CONJUNTOS ZEIS, REG, BAIRRO, LOTES REGULARIZADOS, DOMICILIOS BENEFICI…, DECRETOS DE APROVAC…, PLANTAS DE APROVACAO, CARTORIO DE REGISTRO

## g1482（1 列）
- 見出し：CARTORIO DE REGISTRO
- 例1 値：5 OFICIO | 5 OFICIO | 7 OFICIO | 3 OFICIO | 5 OFICIO
  - 同じ表の列：VILAS CONJUNTOS ZEIS, REG, BAIRRO, LOTES REGULARIZADOS, DOMICILIOS BENEFICI…, DECRETOS DE APROVAC…, PLANTAS DE APROVACAO, ANO DA REGULARIZACAO

## g1483（1 列）
- 見出し：Ward and Precinct (Updated 2022)
- 例1 値：2008 | 0313 | 0902 | 1104 | 0513
  - 同じ表の列：Total Population, White alone, Hispanic or Latino …, Asian, American Indian and…, Native Hawaiian and…, Two or More Non-Whi…, Total Population, A…

## g1484（1 列）
- 見出し：Total Population
- 例1 値：0.2097457627118644 | 0.09573542210617929 | 0.03144354454502144 | -0.017719826145101973 | 0.033397559409120106
  - 同じ表の列：Ward and Precinct (…, White alone, Hispanic or Latino …, Asian, American Indian and…, Native Hawaiian and…, Two or More Non-Whi…, Total Population, A…

## g1485（1 列）
- 見出し：White alone
- 例1 値：0.56 | -0.0304182509506 | 0.120879120879 | -0.165446559297 | 0.0998685939553
  - 同じ表の列：Ward and Precinct (…, Total Population, Hispanic or Latino …, Asian, American Indian and…, Native Hawaiian and…, Two or More Non-Whi…, Total Population, A…

## g1486（1 列）
- 見出し：Hispanic or Latino (of any Race)
- 例1 値：-0.01020408163265306 | 0.15217391304347827 | -0.12687312687312688 | 0.17049180327868851 | 0.3983739837398374
  - 同じ表の列：Ward and Precinct (…, Total Population, White alone, Asian, American Indian and…, Native Hawaiian and…, Two or More Non-Whi…, Total Population, A…

## g1487（1 列）
- 見出し：Asian
- 例1 値：0.76 | 0.909090909091 | 0.373333333333 | 0.107476635514 | 0.219298245614
  - 同じ表の列：Ward and Precinct (…, Total Population, White alone, Hispanic or Latino …, American Indian and…, Native Hawaiian and…, Two or More Non-Whi…, Total Population, A…

## g1488（1 列）
- 見出し：American Indian and Alaska Native
- 例1 値：*** | *** | *** | *** | ***
  - 同じ表の列：Ward and Precinct (…, Total Population, White alone, Hispanic or Latino …, Asian, Native Hawaiian and…, Two or More Non-Whi…, Total Population, A…

## g1489（1 列）
- 見出し：Native Hawaiian and Other Pacific Islander
- 例1 値：*** | *** | *** | *** | ***
  - 同じ表の列：Ward and Precinct (…, Total Population, White alone, Hispanic or Latino …, Asian, American Indian and…, Two or More Non-Whi…, Total Population, A…

## g1490（1 列）
- 見出し：Two or More Non-White Races
- 例1 値：-0.204545454545 | *** | 1.0 | 0.109090909091 | ***
  - 同じ表の列：Ward and Precinct (…, Total Population, White alone, Hispanic or Latino …, Asian, American Indian and…, Native Hawaiian and…, Total Population, A…

## g1491（1 列）
- 見出し：Total Population, Age 18 and over
- 例1 値：0.20777160983346551 | 0.04335424985738734 | 0.02685284640171858 | 0.09621451104100946 | 0.24060693641618497
  - 同じ表の列：Ward and Precinct (…, Total Population, White alone, Hispanic or Latino …, Asian, American Indian and…, Native Hawaiian and…, Two or More Non-Whi…

## g1492（1 列）
- 見出し：White alone, Age 18 and over
- 例1 値：-0.0543248945148 | -0.229302832244 | -0.232927970065 | 0.0652173913043 | 1.0
  - 同じ表の列：Ward and Precinct (…, Total Population, White alone, Hispanic or Latino …, Asian, American Indian and…, Native Hawaiian and…, Two or More Non-Whi…

## g1493（1 列）
- 見出し：LocationAbbr
- 例1 値：NYK | NH | MS | IL | MP
  - 同じ表の列：YEAR, LocationDesc, DataSource, Topic, Subtopic, ShortQuestionText, Greater_Risk_Questi…, Data_Value_Symbol

## g1494（1 列）
- 見出し：LocationDesc
- 例1 値：San Diego, CA | Delaware | Guam | San Diego, CA | Alabama
  - 同じ表の列：YEAR, LocationAbbr, DataSource, Topic, Subtopic, ShortQuestionText, Greater_Risk_Questi…, Data_Value_Symbol

## g1495（1 列）
- 見出し：DataSource
- 例1 値：YRBSS | YRBSS | YRBSS | YRBSS | YRBSS
  - 同じ表の列：YEAR, LocationAbbr, LocationDesc, Topic, Subtopic, ShortQuestionText, Greater_Risk_Questi…, Data_Value_Symbol

## g1496（1 列）
- 見出し：Topic
- 例1 値：Alcohol and Other Drug Use | Dietary Behaviors | Dietary Behaviors | Unintentional Injuries and Violence | Unintentional Injuries and Violence
  - 同じ表の列：YEAR, LocationAbbr, LocationDesc, DataSource, Subtopic, ShortQuestionText, Greater_Risk_Questi…, Data_Value_Symbol

## g1497（1 列）
- 見出し：Subtopic
- 例1 値：Vegetables | Milk | Behaviors that Contribute to Violence | Soda or pop | Obesity and Overweight
  - 同じ表の列：YEAR, LocationAbbr, LocationDesc, DataSource, Topic, ShortQuestionText, Greater_Risk_Questi…, Data_Value_Symbol

## g1498（1 列）
- 見出し：ShortQuestionText
- 例1 値：Suicide plan | Illegal drugs at school | Ever cocaine use | Seat belt use | Ever ecstasy use
  - 同じ表の列：YEAR, LocationAbbr, LocationDesc, DataSource, Topic, Subtopic, Greater_Risk_Questi…, Data_Value_Symbol

## g1499（1 列）
- 見出し：Greater_Risk_Question
- 例1 値：N/A | Currently frequently smoked cigars | Drank soda or pop | Did not use birth control pills before … | Ever used marijuana
  - 同じ表の列：YEAR, LocationAbbr, LocationDesc, DataSource, Topic, Subtopic, ShortQuestionText, Data_Value_Symbol

## g1500（1 列）
- 見出し：Data_Value_Symbol
- 例1 値：% | % | % | % | %
  - 同じ表の列：YEAR, LocationAbbr, LocationDesc, DataSource, Topic, Subtopic, ShortQuestionText, Greater_Risk_Questi…

## g1501（1 列）
- 見出し：Data_Value_Type
- 例1 値：Percentage | Percentage | Percentage | Percentage | Percentage
  - 同じ表の列：YEAR, LocationAbbr, LocationDesc, DataSource, Topic, Subtopic, ShortQuestionText, Greater_Risk_Questi…

## 答えの雛形

```
g1441	
g1442	
g1443	
g1444	
g1445	
g1446	
g1447	
g1448	
g1449	
g1450	
g1451	
g1452	
g1453	
g1454	
g1455	
g1456	
g1457	
g1458	
g1459	
g1460	
g1461	
g1462	
g1463	
g1464	
g1465	
g1466	
g1467	
g1468	
g1469	
g1470	
g1471	
g1472	
g1473	
g1474	
g1475	
g1476	
g1477	
g1478	
g1479	
g1480	
g1481	
g1482	
g1483	
g1484	
g1485	
g1486	
g1487	
g1488	
g1489	
g1490	
g1491	
g1492	
g1493	
g1494	
g1495	
g1496	
g1497	
g1498	
g1499	
g1500	
g1501	
```
