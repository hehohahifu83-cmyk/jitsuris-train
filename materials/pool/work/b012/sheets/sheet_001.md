# ラベル用シート 001 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：ID_DECLIV_TRECHO
- 例1 値：200 | 799 | 852 | 996 | 423
  - 同じ表の列：ID_TRECHO, COMPRIMENTO, LARGURA, DECLIVIDADE_MINIMA, DECLIVIDADE_MEDIA, DECLIVIDADE_MAXIMA, COTA_MINIMA, COTA_MEDIA

## g0002（1 列）
- 見出し：ID_TRECHO
- 例1 値：64 | 49219 | 240 | 49024 | 67
  - 同じ表の列：ID_DECLIV_TRECHO, COMPRIMENTO, LARGURA, DECLIVIDADE_MINIMA, DECLIVIDADE_MEDIA, DECLIVIDADE_MAXIMA, COTA_MINIMA, COTA_MEDIA

## g0003（1 列）
- 見出し：COMPRIMENTO
- 例1 値：62.78 | 83.3 | 108.15 | 90.19 | 71.45
  - 同じ表の列：ID_DECLIV_TRECHO, ID_TRECHO, LARGURA, DECLIVIDADE_MINIMA, DECLIVIDADE_MEDIA, DECLIVIDADE_MAXIMA, COTA_MINIMA, COTA_MEDIA

## g0004（1 列）
- 見出し：LARGURA
- 例1 値：3.5 | 2.97 | 88.5 | 2.03 | 3.16
  - 同じ表の列：ID_DECLIV_TRECHO, ID_TRECHO, COMPRIMENTO, DECLIVIDADE_MINIMA, DECLIVIDADE_MEDIA, DECLIVIDADE_MAXIMA, COTA_MINIMA, COTA_MEDIA

## g0005（1 列）
- 見出し：DECLIVIDADE_MINIMA
- 例1 値：0 | 6.38 | 0 | 11.98 | 0
  - 同じ表の列：ID_DECLIV_TRECHO, ID_TRECHO, COMPRIMENTO, LARGURA, DECLIVIDADE_MEDIA, DECLIVIDADE_MAXIMA, COTA_MINIMA, COTA_MEDIA

## g0006（1 列）
- 見出し：DECLIVIDADE_MEDIA
- 例1 値：4.92 | 28.34 | 12.06 | 16.33 | 8.01
  - 同じ表の列：ID_DECLIV_TRECHO, ID_TRECHO, COMPRIMENTO, LARGURA, DECLIVIDADE_MINIMA, DECLIVIDADE_MAXIMA, COTA_MINIMA, COTA_MEDIA

## g0007（1 列）
- 見出し：DECLIVIDADE_MAXIMA
- 例1 値：16.67 | 11.08 | 33.69 | 28.31 | 72
  - 同じ表の列：ID_DECLIV_TRECHO, ID_TRECHO, COMPRIMENTO, LARGURA, DECLIVIDADE_MINIMA, DECLIVIDADE_MEDIA, COTA_MINIMA, COTA_MEDIA

## g0008（1 列）
- 見出し：COTA_MINIMA
- 例1 値：1025.01 | 773.17 | 874 | 723.51 | 749.83
  - 同じ表の列：ID_DECLIV_TRECHO, ID_TRECHO, COMPRIMENTO, LARGURA, DECLIVIDADE_MINIMA, DECLIVIDADE_MEDIA, DECLIVIDADE_MAXIMA, COTA_MEDIA

## g0009（1 列）
- 見出し：COTA_MEDIA
- 例1 値：821.04 | 811.48 | 788.71 | 769.19 | 936.82
  - 同じ表の列：ID_DECLIV_TRECHO, ID_TRECHO, COMPRIMENTO, LARGURA, DECLIVIDADE_MINIMA, DECLIVIDADE_MEDIA, DECLIVIDADE_MAXIMA, COTA_MINIMA

## g0010（1 列）
- 見出し：COTA_MAXIMA
- 例1 値：779.03 | 1061.19 | 751.63 | 930.4 | 802.97
  - 同じ表の列：ID_DECLIV_TRECHO, ID_TRECHO, COMPRIMENTO, LARGURA, DECLIVIDADE_MINIMA, DECLIVIDADE_MEDIA, DECLIVIDADE_MAXIMA, COTA_MINIMA

## g0011（3 列）
- 見出し：ID_BASE_TRECHO
- 例1 値：62446 | 42665 | 3469 | 4219 | 42740
  - 同じ表の列：ID_BASE_RT, IND_RT, GEOMETRIA
- 例2 値：55262 | 13506 | 32125 | 28436 | 6711
  - 同じ表の列：ID_BASE_RE, IND_RE, GEOMETRIA

## g0012（1 列）
- 見出し：ID_BASE_RT
- 例1 値：87554 | 76318 | 40622 | 40540 | 54754
  - 同じ表の列：ID_BASE_TRECHO, IND_RT, GEOMETRIA

## g0013（1 列）
- 見出し：IND_RT
- 例1 値：S | S | S | N | S
  - 同じ表の列：ID_BASE_TRECHO, ID_BASE_RT, GEOMETRIA

## g0014（4 列）
- 見出し：GEOMETRIA
- 例1 値：LINESTRING (603758.02067207 7802942.108… | LINESTRING (605394.227712451 7803034.52… | LINESTRING (610819.455452432 7793350.03… | LINESTRING (613048.209118506 7794647.76… | LINESTRING (607829.767931887 7809674.89…
  - 同じ表の列：ID_BASE_TRECHO, ID_BASE_RT, IND_RT
- 例2 値：LINESTRING (615445.5645218 7807674.6277… | LINESTRING (605889.253915008 7807480.86… | LINESTRING (606381.279805544 7811786.61… | LINESTRING (602876.121202829 7787854.94… | LINESTRING (606381.279805544 7811786.61…
  - 同じ表の列：ID_TCV, TIPO_TRECHO_CIRCULA…, ID_NO_CIRC_INICIAL, ID_NO_CIRC_FINAL

## g0015（1 列）
- 見出し：ID_EQUIP_SEG_ALIM_NUTRI_UPCC
- 例1 値：89 | 58 | 77 | 75 | 59
  - 同じ表の列：NUMERO_IMOVEL, BAIRRO, CATEGORIA, COMPOSTAGEM, COMERCIALIZACAO, ANO_CADASTRO, TIPO_PRODUCAO, EXTENSAO_AREA_UP

## g0016（1 列）
- 見出し：NUMERO_IMOVEL
- 例1 値：330 | 147 | 1200 | 353 | 491
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, BAIRRO, CATEGORIA, COMPOSTAGEM, COMERCIALIZACAO, ANO_CADASTRO, TIPO_PRODUCAO, EXTENSAO_AREA_UP

## g0017（1 列）
- 見出し：BAIRRO
- 例1 値：Esplanada | Diamante | Nossa Senhora de Fátima | Coqueiros | Novo Aarão Reis
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, NUMERO_IMOVEL, CATEGORIA, COMPOSTAGEM, COMERCIALIZACAO, ANO_CADASTRO, TIPO_PRODUCAO, EXTENSAO_AREA_UP

## g0018（1 列）
- 見出し：CATEGORIA
- 例1 値：Horta | Horta | Agrofloresta | Horta | Horta
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, NUMERO_IMOVEL, BAIRRO, COMPOSTAGEM, COMERCIALIZACAO, ANO_CADASTRO, TIPO_PRODUCAO, EXTENSAO_AREA_UP

## g0019（1 列）
- 見出し：COMPOSTAGEM
- 例1 値：Não | Sim | Não | Sim | Sim
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, NUMERO_IMOVEL, BAIRRO, CATEGORIA, COMERCIALIZACAO, ANO_CADASTRO, TIPO_PRODUCAO, EXTENSAO_AREA_UP

## g0020（1 列）
- 見出し：COMERCIALIZACAO
- 例1 値：Não | Não | Não | Não | Sim
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, NUMERO_IMOVEL, BAIRRO, CATEGORIA, COMPOSTAGEM, ANO_CADASTRO, TIPO_PRODUCAO, EXTENSAO_AREA_UP

## g0021（1 列）
- 見出し：ANO_CADASTRO
- 例1 値：2016 | 2020 | 2013 | 1996 | 2018
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, NUMERO_IMOVEL, BAIRRO, CATEGORIA, COMPOSTAGEM, COMERCIALIZACAO, TIPO_PRODUCAO, EXTENSAO_AREA_UP

## g0022（1 列）
- 見出し：TIPO_PRODUCAO
- 例1 値：Agroecológica | Agroecológica | Agroecológica | Agroecológica | Agroecológica
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, NUMERO_IMOVEL, BAIRRO, CATEGORIA, COMPOSTAGEM, COMERCIALIZACAO, ANO_CADASTRO, EXTENSAO_AREA_UP

## g0023（1 列）
- 見出し：EXTENSAO_AREA_UP
- 例1 値：389.59 | 705.41 | 42.35 | 9093.2 | 849.15
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, NUMERO_IMOVEL, BAIRRO, CATEGORIA, COMPOSTAGEM, COMERCIALIZACAO, ANO_CADASTRO, TIPO_PRODUCAO

## g0024（1 列）
- 見出し：GEOMETRIA
- 例1 値：POLYGON ((603075.090423166 7797967.0773… | POLYGON ((616217.861287807 7803485.9440… | POLYGON ((617126.116299475 7806542.6618… | POLYGON ((613988.399382128 7809096.8019… | POLYGON ((614467.919965472 7797740.5235…
  - 同じ表の列：ID_EQUIP_SEG_ALIM_N…, NUMERO_IMOVEL, BAIRRO, CATEGORIA, COMPOSTAGEM, COMERCIALIZACAO, ANO_CADASTRO, TIPO_PRODUCAO

## g0025（1 列）
- 見出し：INDICE_CADASTRAL
- 例1 値：354003 008 0763 | 398033 010 0063 | 380003 006 0012 | 824016 018 0011 | 799049 022 0020
  - 同じ表の列：NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0026（2 列）
- 見出し：NULOTCTM
- 例1 値：040077700265 | 170113200325 | 160830200555 | 040713000060 | 040186800515
  - 同じ表の列：INDICE_CADASTRAL, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：010111000415 | 010241500030 | 090049300265 | 010264500090 | 091058400455
  - 同じ表の列：INDICE_CADASTRAL, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0027（2 列）
- 見出し：ZONEAMENTO_PVIPTU
- 例1 値：ZA | ZAP | ZAR2 | ZA | ZAR2
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：ZAR1 | ZA | ZCBH | ZA | ZCBH
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0028（2 列）
- 見出し：FREQUENCIA_COLETA
- 例1 値：COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA DIARIA
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：COLETA DIARIA | COLETA DIARIA | COLETA DIARIA | COLETA DIARIA | COLETA DIARIA
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0029（2 列）
- 見出し：IND_MEIO_FIO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0030（2 列）
- 見出し：IND_PAVIMENTACAO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0031（1 列）
- 見出し：IND_ARBORIZACAO
- 例1 値：SIM | SIM | NÃO | NÃO | NÃO
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0032（1 列）
- 見出し：IND_GALERIA_PLUVIAL
- 例1 値：NÃO | SIM | SIM | SIM | NÃO
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_ILUMINACAO_PUBL…

## g0033（2 列）
- 見出し：IND_ILUMINACAO_PUBLICA
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL
- 例2 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL

## g0034（2 列）
- 見出し：IND_REDE_ESGOTO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL
- 例2 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL

## g0035（1 列）
- 見出し：Linha Origem ou Destino
- 例1 値：AC07 | 2001 | PR02 | 1002 | 4003
  - 同じ表の列：Estacao

## g0036（1 列）
- 見出し：Estacao
- 例1 値：Move Antônio Carlos | Estação Diamante | Estação Venda Nova | Estação Diamante | Move Antônio Carlos
  - 同じ表の列：Linha Origem ou Des…

## g0037（1 列）
- 見出し：Topic
- 例1 値：Population | Population | Income | Population | Housing
  - 同じ表の列：Variable, Definition, Universe

## g0038（1 列）
- 見出し：Variable
- 例1 値：Education_Attainment_share_LT_highschool | Income_ChildrenByPoverty_chi_above_pov | Population_Race_share_asian_pacific_isl… | Labor_LaborForce_in_labor_force_f | Labor_LaborForce_female_participation_r…
  - 同じ表の列：Topic, Definition, Universe

## g0039（1 列）
- 見出し：Definition
- 例1 値：Two or more races | Share of population with attainment of … | Other race | Population living in households | Share of population that is Black/Afric…
  - 同じ表の列：Topic, Variable, Universe

## g0040（1 列）
- 見出し：Universe
- 例1 値：Total Population | Total Workers aged 16 and over | Total population aged 25 or older | Total Workers aged 16 and over | Total Population
  - 同じ表の列：Topic, Variable, Definition

## g0041（1 列）
- 見出し：年次・月次コード
- 例1 値：主要指標4 ―全世帯,生計支出7分位階層別― | tuki | tuki | nen | tuki
  - 同じ表の列：年次・月次, 西暦(年), 月, 都平均, 第1階層, 第2階層, 第3階層, 第4階層

## g0042（1 列）
- 見出し：年次・月次
- 例1 値：令和 7年11月 | 令和 8年 4月 | 令和 5年平均 | 令和 2年平均 | 令和 7年 7月
  - 同じ表の列：年次・月次コード, 西暦(年), 月, 都平均, 第1階層, 第2階層, 第3階層, 第4階層

## g0043（2 列）
- 見出し：西暦(年)
- 例1 値：2025 | 2025 | 2025 | 2019 | 2026
  - 同じ表の列：年次・月次コード, 年次・月次, 月, 都平均, 第1階層, 第2階層, 第3階層, 第4階層
- 例2 値：2026 | 2023 | 2025 | 2024 | 2026
  - 同じ表の列：年月, 月, 総合, 生鮮食品を除く総合, 持家の帰属家賃を除く総合, 食料, 住居, 持家の帰属家賃を除く住居

## g0044（7 列）
- 見出し：月
- 例1 値：7 | 5 | 2 | 11 | 4
  - 同じ表の列：年次・月次コード, 年次・月次, 西暦(年), 都平均, 第1階層, 第2階層, 第3階層, 第4階層
- 例2 値：01 | 07 | 09 | 05 | 12
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 年, 戸籍謄抄本, 住民票の写し, 印鑑証明, 婚姻

## g0045（1 列）
- 見出し：都平均
- 例1 値：29.6 | 26.2 | 26.5 | 28.5 | 26.9
  - 同じ表の列：年次・月次コード, 年次・月次, 西暦(年), 月, 第1階層, 第2階層, 第3階層, 第4階層

## g0046（1 列）
- 見出し：第1階層
- 例1 値：53.7 | 58.3 | 56.2 | 51.9 | 57.3
  - 同じ表の列：年次・月次コード, 年次・月次, 西暦(年), 月, 都平均, 第2階層, 第3階層, 第4階層

## g0047（1 列）
- 見出し：第2階層
- 例1 値：41.6 | 43.0 | 45.1 | 49.6 | 44.8
  - 同じ表の列：年次・月次コード, 年次・月次, 西暦(年), 月, 都平均, 第1階層, 第3階層, 第4階層

## g0048（1 列）
- 見出し：第3階層
- 例1 値：44.4 | 37.4 | 37.9 | 39.0 | 38.7
  - 同じ表の列：年次・月次コード, 年次・月次, 西暦(年), 月, 都平均, 第1階層, 第2階層, 第4階層

## g0049（1 列）
- 見出し：第4階層
- 例1 値：37.9 | 35.5 | 33.2 | 37.0 | 35.5
  - 同じ表の列：年次・月次コード, 年次・月次, 西暦(年), 月, 都平均, 第1階層, 第2階層, 第3階層

## g0050（1 列）
- 見出し：第5階層
- 例1 値：31.3 | 35.9 | 34.0 | 32.4 | 31.4
  - 同じ表の列：年次・月次コード, 年次・月次, 西暦(年), 月, 都平均, 第1階層, 第2階層, 第3階層

## g0051（84 列）
- 見出し：全国地方公共団体コード
- 例1 値：131024 | 131024 | 131024 | 131024 | 131024
  - 同じ表の列：地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)
- 例2 値：131041 | 131041 | 131041 | 131041 | 131041
  - 同じ表の列：ID, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字

## g0052（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都中央区 | 東京都中央区 | 東京都中央区 | 東京都中央区 | 東京都中央区
  - 同じ表の列：全国地方公共団体コード, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0053（1 列）
- 見出し：施設名称
- 例1 値：久松町区民館 | 新場橋区民館 | 晴海地域交流センター「はるみらい」 | 中央区立産業会館 | 浜町集会施設「浜町メモリアル」
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0054（1 列）
- 見出し：施設名称_カナ
- 例1 値：ニホンバシコウカイドウ | ニホンバシコウカイドウ | チュウオウクリツサンギョウカイカン
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0055（1 列）
- 見出し：施設名称_英字
- 例1 値：nihonbashikokaido | nihonbashikokaido
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0056（1 列）
- 見出し：スペース名称
- 例1 値：ホール | 集会室 | 集会室 | 集会室 | 集会室
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0057（1 列）
- 見出し：スペース名称_カナ
- 例1 値：ホール | シュウカイシツ | チュウオウクリツサンギョウカイカン
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_英字, 建物名等(方書)

## g0058（1 列）
- 見出し：スペース名称_英字
- 例1 値：meeting room | hall
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 建物名等(方書)

## g0059（1 列）
- 見出し：建物名等(方書)
- 例1 値：日本橋区民センター内2階 | 日本橋区民センター内4階
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字

## g0060（1 列）
- 見出し：連絡先FormURL
- 例1 値：http://www.nihonbasikokaido.com/ | http://www.nihonbasikokaido.com/
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字

## g0061（1 列）
- 見出し：年月日[西暦]
- 例1 値：20251101 | 20231001 | 20140401 | 20120901 | 20250101
  - 同じ表の列：港区総数日本人世帯数[世帯], 港区総数日本人人口男[人], 港区総数日本人人口女[人], 港区総数日本人人口計[人], 港区総数外国人世帯数[世帯], 港区総数外国人人口男[人], 港区総数外国人人口女[人], 港区総数外国人人口計[人]

## g0062（1 列）
- 見出し：港区総数日本人世帯数[世帯]
- 例1 値：125880 | 120167 | 125751 | 115501 | 133365
  - 同じ表の列：年月日[西暦], 港区総数日本人人口男[人], 港区総数日本人人口女[人], 港区総数日本人人口計[人], 港区総数外国人世帯数[世帯], 港区総数外国人人口男[人], 港区総数外国人人口女[人], 港区総数外国人人口計[人]

## g0063（1 列）
- 見出し：港区総数日本人人口男[人]
- 例1 値：114476 | 91234 | 82312 | 97860 | 94037
  - 同じ表の列：年月日[西暦], 港区総数日本人世帯数[世帯], 港区総数日本人人口女[人], 港区総数日本人人口計[人], 港区総数外国人世帯数[世帯], 港区総数外国人人口男[人], 港区総数外国人人口女[人], 港区総数外国人人口計[人]

## g0064（1 列）
- 見出し：港区総数日本人人口女[人]
- 例1 値：105153 | 108564 | 118312 | 128139 | 130321
  - 同じ表の列：年月日[西暦], 港区総数日本人世帯数[世帯], 港区総数日本人人口男[人], 港区総数日本人人口計[人], 港区総数外国人世帯数[世帯], 港区総数外国人人口男[人], 港区総数外国人人口女[人], 港区総数外国人人口計[人]

## g0065（1 列）
- 見出し：港区総数日本人人口計[人]
- 例1 値：170181 | 223506 | 202505 | 189536 | 214741
  - 同じ表の列：年月日[西暦], 港区総数日本人世帯数[世帯], 港区総数日本人人口男[人], 港区総数日本人人口女[人], 港区総数外国人世帯数[世帯], 港区総数外国人人口男[人], 港区総数外国人人口女[人], 港区総数外国人人口計[人]

## g0066（1 列）
- 見出し：港区総数外国人世帯数[世帯]
- 例1 値：- | 10510 | 13292 | - | -
  - 同じ表の列：年月日[西暦], 港区総数日本人世帯数[世帯], 港区総数日本人人口男[人], 港区総数日本人人口女[人], 港区総数日本人人口計[人], 港区総数外国人人口男[人], 港区総数外国人人口女[人], 港区総数外国人人口計[人]

## g0067（1 列）
- 見出し：港区総数外国人人口男[人]
- 例1 値：9807 | 9768 | 10459 | 11025 | 9772
  - 同じ表の列：年月日[西暦], 港区総数日本人世帯数[世帯], 港区総数日本人人口男[人], 港区総数日本人人口女[人], 港区総数日本人人口計[人], 港区総数外国人世帯数[世帯], 港区総数外国人人口女[人], 港区総数外国人人口計[人]

## g0068（1 列）
- 見出し：港区総数外国人人口女[人]
- 例1 値：- | 8554 | 8312 | 11744 | -
  - 同じ表の列：年月日[西暦], 港区総数日本人世帯数[世帯], 港区総数日本人人口男[人], 港区総数日本人人口女[人], 港区総数日本人人口計[人], 港区総数外国人世帯数[世帯], 港区総数外国人人口男[人], 港区総数外国人人口計[人]

## g0069（1 列）
- 見出し：港区総数外国人人口計[人]
- 例1 値：19122 | - | 17224 | - | 24003
  - 同じ表の列：年月日[西暦], 港区総数日本人世帯数[世帯], 港区総数日本人人口男[人], 港区総数日本人人口女[人], 港区総数日本人人口計[人], 港区総数外国人世帯数[世帯], 港区総数外国人人口男[人], 港区総数外国人人口女[人]

## g0070（1 列）
- 見出し：港区総数複数国籍世帯数[世帯]
- 例1 値：- | - | - | - | 3282
  - 同じ表の列：年月日[西暦], 港区総数日本人世帯数[世帯], 港区総数日本人人口男[人], 港区総数日本人人口女[人], 港区総数日本人人口計[人], 港区総数外国人世帯数[世帯], 港区総数外国人人口男[人], 港区総数外国人人口女[人]

## g0071（36 列）
- 見出し：ID
- 例1 値：23 | 76 | 43 | 37 | 62
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字
- 例2 値：292 | 197 | 253 | 117 | 147
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称

## g0072（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区
  - 同じ表の列：全国地方公共団体コード, ID, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字
- 例2 値：東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 都道府県, 市区町村

## g0073（1 列）
- 見出し：施設名称
- 例1 値：落合第二地域センター | 四谷地域センター | 新宿区立新宿コズミックスポーツセンター | 四谷地域センター | 新宿区立戸山生涯学習館
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字

## g0074（1 列）
- 見出し：施設名称_カナ
- 例1 値：ワカマツチイキセンター | シンジュクタブンカキョウセイプラザ | ショウガイシャフクシセンター | ワカマツチイキセンター | ショウガイシャフクシセンター
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 施設名称, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字

## g0075（1 列）
- 見出し：施設名称_英字
- 例1 値：Kashiwagi Chiiki Center | Kumin Gallery | Enokicho Chiiki Center | Akagi Lifelong Learning Hall | Tsunohazu Chiiki Center
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 施設名称, 施設名称_カナ, スペース名称, スペース名称_カナ, スペース名称_英字

## g0076（1 列）
- 見出し：スペース名称
- 例1 値：教養室A | 集会室(和室)4(つつじ) | 和室 | 学習室B | 集会室(和室)5(水仙)
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称_カナ, スペース名称_英字

## g0077（1 列）
- 見出し：スペース名称_カナ
- 例1 値：チョウリコウサクシツ | カイギシツサン | クッキングルーム | シチョウカクシツ | シュウカイシツ2
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_英字

## g0078（1 列）
- 見出し：スペース名称_英字
- 例1 値：Lecture Room B | Study Room C | Multi-purpose room | Hall | Study Room A
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ

## g0079（1 列）
- 見出し：建物名等(方書)
- 例1 値：ハイジア11階
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ

## g0080（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都江東区 | 東京都江東区 | 東京都江東区 | 東京都江東区 | 東京都江東区
  - 同じ表の列：全国地方公共団体コード, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 利用可能曜日

## g0081（1 列）
- 見出し：施設名称
- 例1 値：富岡北地区集会所 | 東陽区民館 | 江東区産業会館 | スポーツ会館 | 亀戸文化センター
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 利用可能曜日

## g0082（1 列）
- 見出し：施設名称_カナ
- 例1 値：ヒラノチクシュウカイジョ | カメイドブンカセンター | コウトウクバショウキネンカン | コウトウクブンカセンター | コウトウコウカイドウ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 利用可能曜日

## g0083（1 列）
- 見出し：施設名称_英字
- 例1 値：Hukagawa sports center | Komatsubashi community center | Komatsubashi community center | Gender Equality Promotion Center | Ariake sports center
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, スペース名称, スペース名称_カナ, スペース名称_英字, 利用可能曜日

## g0084（1 列）
- 見出し：スペース名称
- 例1 値：第1研修室 | 和室 | 和室 | 和室 | 洋室
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称_カナ, スペース名称_英字, 利用可能曜日

## g0085（1 列）
- 見出し：スペース名称_カナ
- 例1 値：オンガクスタジオ | タウンホール | サブ・レクホール | タモクテキホール | ダイサンカイギシツ
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_英字, 利用可能曜日

## g0086（1 列）
- 見出し：スペース名称_英字
- 例1 値：room 2 | Japanese-style room 2 | music studio | Training Rooms 3 | Meeting Room 1
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 利用可能曜日

## g0087（2 列）
- 見出し：利用可能曜日
- 例1 値：月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字
- 例2 値：月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日 | 月火水木金土日
  - 同じ表の列：都道府県コード又は市区町村コード, 都道府県名, 名称, 名称_カナ, POIコード, 方書, 開始時間, 終了時間

## g0088（3 列）
- 見出し：開始時間
- 例1 値：09:00 | 09:00 | 09:00 | 09:00 | 09:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字
- 例2 値：09:00 | 09:00 | 09:00 | 09:00 | 09:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, POIコード, 終了時間, 利用可能時間特記事項, 説明

## g0089（3 列）
- 見出し：地方公共団体名
- 例1 値：東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区
  - 同じ表の列：全国地方公共団体コード, 許可番号, 営業形態, 名称, 許可年月日, 備考
- 例2 値：東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区
  - 同じ表の列：全国地方公共団体コード, 名称, 面積(m2)

## g0090（1 列）
- 見出し：許可番号
- 例1 値：6品保生環き第84号 | 4品保生環き第80号 | 6品保生環き第37号 | 7品保生環き第57号 | 6品保生環き第85号
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 営業形態, 名称, 許可年月日, 備考

## g0091（2 列）
- 見出し：営業形態
- 例1 値：旅館・ホテル営業 | 旅館・ホテル営業 | 旅館・ホテル営業 | 旅館・ホテル営業 | 簡易宿所営業
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 許可番号, 名称, 許可年月日, 備考
- 例2 値：旅館・ホテル営業 | 簡易宿所営業 | 旅館・ホテル営業 | 旅館・ホテル営業 | 旅館・ホテル営業
  - 同じ表の列：名称, 許可年月日

## g0092（1 列）
- 見出し：名称
- 例1 値：東京SUOMIホテル | TK Court Shinagawa | アーバンステイ品川 | リオス・スリー | SunStay立会川II
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 許可番号, 営業形態, 許可年月日, 備考

## g0093（1 列）
- 見出し：許可年月日
- 例1 値：2019-10-25T00:00:00 | 2025-07-02T00:00:00 | 2018-04-18T00:00:00 | 2025-08-27T00:00:00 | 2023-12-08T00:00:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 許可番号, 営業形態, 名称, 備考

## g0094（1 列）
- 見出し：備考
- 例1 値：休止中
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 許可番号, 営業形態, 名称, 許可年月日

## g0095（1 列）
- 見出し：年度
- 例1 値：2023年度 | 2023年度 | 2023年度 | 2023年度 | 2023年度
  - 同じ表の列：No, 請求の概要, 決定件数, 決定件数内訳)全部開示, 決定件数内訳)部分開示, 決定件数内訳)不存在, 決定件数内訳)存否応答拒否

## g0096（2 列）
- 見出し：No
- 例1 値：2 | 23 | 26 | 99 | 28
  - 同じ表の列：年度, 請求の概要, 決定件数, 決定件数内訳)全部開示, 決定件数内訳)部分開示, 決定件数内訳)不存在, 決定件数内訳)存否応答拒否
- 例2 値：1 | 0 | 3 | 4 | 0
  - 同じ表の列：Year end, Category, Amount

## g0097（1 列）
- 見出し：請求の概要
- 例1 値：道路に関する相談文書 | 土木関係文書 | 近隣説明報告書等 | 契約関係文書 | 購読紙関連文書
  - 同じ表の列：年度, No, 決定件数, 決定件数内訳)全部開示, 決定件数内訳)部分開示, 決定件数内訳)不存在, 決定件数内訳)存否応答拒否

## g0098（1 列）
- 見出し：決定件数
- 例1 値：1 | 2 | 1 | 1 | 3
  - 同じ表の列：年度, No, 請求の概要, 決定件数内訳)全部開示, 決定件数内訳)部分開示, 決定件数内訳)不存在, 決定件数内訳)存否応答拒否

## g0099（1 列）
- 見出し：決定件数内訳)全部開示
- 例1 値：44 | 5 | 1 | 1 | 1
  - 同じ表の列：年度, No, 請求の概要, 決定件数, 決定件数内訳)部分開示, 決定件数内訳)不存在, 決定件数内訳)存否応答拒否

## g0100（1 列）
- 見出し：決定件数内訳)部分開示
- 例1 値：2 | 1 | 2 | 1 | 6
  - 同じ表の列：年度, No, 請求の概要, 決定件数, 決定件数内訳)全部開示, 決定件数内訳)不存在, 決定件数内訳)存否応答拒否

## g0101（1 列）
- 見出し：決定件数内訳)不存在
- 例1 値：4 | 1 | 2 | 1
  - 同じ表の列：年度, No, 請求の概要, 決定件数, 決定件数内訳)全部開示, 決定件数内訳)部分開示, 決定件数内訳)存否応答拒否

## g0102（1 列）
- 見出し：決定件数内訳)存否応答拒否
- 例1 値：1 | 2 | 1
  - 同じ表の列：年度, No, 請求の概要, 決定件数, 決定件数内訳)全部開示, 決定件数内訳)部分開示, 決定件数内訳)不存在

## g0103（3 列）
- 見出し：地方公共団体名
- 例1 値：東京都大田区 | 東京都大田区 | 東京都大田区 | 東京都大田区 | 東京都大田区
  - 同じ表の列：全国地方公共団体コード, ID, 名称
- 例2 値：東京都大田区 | 東京都大田区 | 東京都大田区 | 東京都大田区 | 東京都大田区
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 面積, 間取り, 建設年度, 管理戸数, 一般

## g0104（1 列）
- 見出し：名称
- 例1 値：宮ノ下児童公園 | 大森山谷公園 | 山王公園 | 東蒲田公園 | 田コロ児童公園
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名

## g0105（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区
  - 同じ表の列：全国地方公共団体コード, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)
- 例2 値：東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区
  - 同じ表の列：全国地方公共団体コード, 名称

## g0106（1 列）
- 見出し：施設名称
- 例1 値：北沢区民会館 | 砧区民会館 | 玉川区民会館 | 北沢区民会館 | 砧区民会館
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0107（1 列）
- 見出し：施設名称_カナ
- 例1 値：キヌタクミンカイカン | セタガヤクミンカイカン | キタザワクミンカイカン | セタガヤクミンカイカン | タマガワクミンカイカン
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0108（1 列）
- 見出し：施設名称_英字
- 例1 値：Tamagawa Civic Hall | Kitazawa Civic Hall | Kitazawa Civic Hall | Kinuta Civic Hall | Tamagawa Civic Hall
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, スペース名称, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0109（1 列）
- 見出し：スペース名称
- 例1 値：集会室A | 第5集会室 | 第1集会室 | 集会案E | 集会案A
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称_カナ, スペース名称_英字, 建物名等(方書)

## g0110（1 列）
- 見出し：スペース名称_カナ
- 例1 値：シュウカイシツシー | シュウカイシツ | レンシュウシツA | シュウカイシツB | シュウカイシツA
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_英字, 建物名等(方書)

## g0111（1 列）
- 見出し：スペース名称_英字
- 例1 値：Studio A | Conference room 4 | Conference roomA | Studio B | Assenmbly Room A
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, 建物名等(方書)

## g0112（1 列）
- 見出し：建物名等(方書)
- 例1 値：成城ホール | 成城ホール | 上用賀アートホール | 玉川せせらぎホール | 梅丘パークホール
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字

## g0113（4 列）
- 見出し：高度の種別
- 例1 値：階数 | 階数 | 階数 | 階数 | 階数
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 施設名称, 施設名称_カナ, 施設名称_英字, スペース名称, スペース名称_カナ, スペース名称_英字
- 例2 値：階数 | 階数 | 階数 | 階数 | 階数
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 名称_カナ, 名称_英字, 名称_通称, POIコード, 建物名等(方書)

## g0114（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都豊島区 | 東京都豊島区 | 東京都豊島区 | 東京都豊島区 | 東京都豊島区
  - 同じ表の列：全国地方公共団体コード, 名称, 号数, 発行年月, 発行元

## g0115（1 列）
- 見出し：名称
- 例1 値：としま区議会だより令和6年第4回定例会号 | としま区議会だより令和7年第3回定例会号 | としま区議会だより令和7年新年号 | としま区議会だより令和7年第1回定例会号 | としま区議会だより令和6年第3回臨時会号
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 号数, 発行年月, 発行元

## g0116（2 列）
- 見出し：号数
- 例1 値：297 | 302 | 293 | 305 | 306
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 発行年月, 発行元
- 例2 値：233 | 234 | 231 | 228 | 230
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 発行年月, 発行元

## g0117（2 列）
- 見出し：発行年月
- 例1 値：2024-02 | 2023-08 | 2025-06 | 2025-01 | 2023-12
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 号数, 発行元
- 例2 値：2023-04 | 2023-10 | 2024-01 | 2024-10 | 2024-07
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 号数, 発行元

## g0118（1 列）
- 見出し：発行元
- 例1 値：豊島区議会事務局 | 豊島区議会事務局 | 豊島区議会事務局 | 豊島区議会事務局 | 豊島区議会事務局
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 号数, 発行年月

## g0119（1 列）
- 見出し：地方公共団体名
- 例1 値：練馬区 | 練馬区 | 練馬区 | 練馬区 | 練馬区
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 名称_カナ, 文化財分類, 種類, 場所名称, 法人番号

## g0120（1 列）
- 見出し：名称
- 例1 値：石神井城跡 | 中村囃子 | 草摺引図絵馬〈非公開〉 | 八の釜の湧き水 | 石神井西尋常小学校のリードオルガン
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称_カナ, 文化財分類, 種類, 場所名称, 法人番号

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
