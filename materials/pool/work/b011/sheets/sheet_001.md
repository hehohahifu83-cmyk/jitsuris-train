# ラベル用シート 001 / 015

- LABEL_GUIDE v1.9 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：ID_TCV
- 例1 値：17820 | 16885 | 15436 | 16516 | 13543
  - 同じ表の列：TIPO_TRECHO_CIRCULA…, ID_NO_CIRC_INICIAL, ID_NO_CIRC_FINAL, GEOMETRIA

## g0002（1 列）
- 見出し：TIPO_TRECHO_CIRCULACAO
- 例1 値：Trecho de conversão | Trecho de via | Trecho de via | Trecho de via | Trecho de via
  - 同じ表の列：ID_TCV, ID_NO_CIRC_INICIAL, ID_NO_CIRC_FINAL, GEOMETRIA

## g0003（1 列）
- 見出し：ID_NO_CIRC_INICIAL
- 例1 値：96625 | 128565 | 32933 | 77002 | 101732
  - 同じ表の列：ID_TCV, TIPO_TRECHO_CIRCULA…, ID_NO_CIRC_FINAL, GEOMETRIA

## g0004（1 列）
- 見出し：ID_NO_CIRC_FINAL
- 例1 値：96624 | 192837 | 46356 | 101627 | 84380
  - 同じ表の列：ID_TCV, TIPO_TRECHO_CIRCULA…, ID_NO_CIRC_INICIAL, GEOMETRIA

## g0005（2 列）
- 見出し：GEOMETRIA
- 例1 値：LINESTRING (612100.63 7792752.03, 61211… | LINESTRING (605391.31 7810125.00, 60538… | LINESTRING (610097.76 7792525.60, 61020… | LINESTRING (606576.03 7809035.02, 60657… | LINESTRING (612762.18 7801344.05, 61277…
  - 同じ表の列：ID_TCV, TIPO_TRECHO_CIRCULA…, ID_NO_CIRC_INICIAL, ID_NO_CIRC_FINAL
- 例2 値：LINESTRING (612028.62 7804664.78, 61202… | LINESTRING (616680.59 7806673.03, 61668… | LINESTRING (616088.78 7797876.77, 61610… | LINESTRING (599589.62 7789456.28, 59957… | LINESTRING (616087.61 7803589.41, 61609…
  - 同じ表の列：ID_DECLIV_TRECHO_UF…, ID_TRECHO, LARGURA, COTA_MINIMA, COTA_MEDIA, COTA_MAXIMA

## g0006（1 列）
- 見出し：ID_CCTRL
- 例1 値：10545 | 8743 | 8788 | 9389 | 8776
  - 同じ表の列：GEOMETRIA

## g0007（4 列）
- 見出し：GEOMETRIA
- 例1 値：POLYGON ((599260.6535571 7791108.943403… | POLYGON ((613097.312219381 7805812.9004… | POLYGON ((603716.130605585 7791172.0805… | POLYGON ((608293.456495232 7789437.6635… | POLYGON ((605704.863332906 7803242.0337…
  - 同じ表の列：ID_CCTRL
- 例2 値：POLYGON ((611695.749571609 7806133.3451… | POLYGON ((600968.63177685 7790085.62164… | POLYGON ((610400.063565695 7798764.5650… | POLYGON ((607034.406774475 7791845.7633… | POLYGON ((609153.605250228 7798575.0836…
  - 同じ表の列：ID_JURCR, COD_JURISDICAO, REGIONAL

## g0008（1 列）
- 見出し：ID_JURCR
- 例1 値：2091 | 2142 | 2261 | 2215 | 2204
  - 同じ表の列：COD_JURISDICAO, REGIONAL, GEOMETRIA

## g0009（2 列）
- 見出し：COD_JURISDICAO
- 例1 値：594 | 525 | 077 | 649 | 529
  - 同じ表の列：ID_JURCR, REGIONAL, GEOMETRIA
- 例2 値：222 | 191 | 603 | 653 | 562
  - 同じ表の列：ID_JUREF, REGIONAL, GEOMETRIA

## g0010（1 列）
- 見出し：REGIONAL
- 例1 値：OESTE | BARREIRO | NOROESTE | LESTE | LESTE
  - 同じ表の列：ID_JURCR, COD_JURISDICAO, GEOMETRIA

## g0011（1 列）
- 見出し：INDICE_CADASTRAL
- 例1 値：807035 016 0011 | 732022 007B0018 | 253090 009 0058 | 244005C001 0582 | 252003 013 0018
  - 同じ表の列：NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0012（2 列）
- 見出し：NULOTCTM
- 例1 値：030386000325 | 020382700345 | 020381400420 | 030027000030 | 030266600010
  - 同じ表の列：INDICE_CADASTRAL, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：181035200185 | 150721900290 | 180338600075 | 180390000430 | 180496900330
  - 同じ表の列：INDICE_CADASTRAL, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0013（2 列）
- 見出し：ZONEAMENTO_PVIPTU
- 例1 値：ZA | ZAR2 | ZE | ZAR2 | ZAR2
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：ZAP | ZAP | ZAP | ZAR2 | ZAR2
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0014（2 列）
- 見出し：FREQUENCIA_COLETA
- 例1 値：COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA | COLETA ALTERNADA
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0015（1 列）
- 見出し：IND_MEIO_FIO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0016（2 列）
- 見出し：IND_PAVIMENTACAO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0017（2 列）
- 見出し：IND_ARBORIZACAO
- 例1 値：NÃO | NÃO | NÃO | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…
- 例2 値：SIM | NÃO | NÃO | NÃO | NÃO
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_GALERIA_PLUVIAL, IND_ILUMINACAO_PUBL…

## g0018（2 列）
- 見出し：IND_GALERIA_PLUVIAL
- 例1 値：SIM | NÃO | SIM | SIM | NÃO
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_ILUMINACAO_PUBL…
- 例2 値：SIM | SIM | NÃO | NÃO | NÃO
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_ILUMINACAO_PUBL…

## g0019（2 列）
- 見出し：IND_ILUMINACAO_PUBLICA
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL
- 例2 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL

## g0020（2 列）
- 見出し：IND_REDE_ESGOTO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL
- 例2 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：INDICE_CADASTRAL, NULOTCTM, ZONEAMENTO_PVIPTU, FREQUENCIA_COLETA, IND_MEIO_FIO, IND_PAVIMENTACAO, IND_ARBORIZACAO, IND_GALERIA_PLUVIAL

## g0021（1 列）
- 見出し：ID_BHIDEL
- 例1 値：80 | 47 | 149 | 64 | 61
  - 同じ表の列：CODIGO_BHIDEL, AREA_M2, GEOMETRIA

## g0022（1 列）
- 見出し：CODIGO_BHIDEL
- 例1 値：4112900 | 4131400 | 4113100 | 4113700 | 4111800
  - 同じ表の列：ID_BHIDEL, AREA_M2, GEOMETRIA

## g0023（1 列）
- 見出し：AREA_M2
- 例1 値：788 | 268 | 19 | 66 | 1666
  - 同じ表の列：ID_BHIDEL, CODIGO_BHIDEL, GEOMETRIA

## g0024（1 列）
- 見出し：Linha/SubLinha
- 例1 値：815/01 | 815/01 | 815/01 | 815/01 | 815/01
  - 同じ表の列：Servico, Consorcio, Data Pesquisa, Dia Semana, Rota, Hora Viagem, Sequencia do PED, Embarque

## g0025（1 列）
- 見出し：Servico
- 例1 値：ALIMENTADORA | ALIMENTADORA | ALIMENTADORA | ALIMENTADORA | ALIMENTADORA
  - 同じ表の列：Linha/SubLinha, Consorcio, Data Pesquisa, Dia Semana, Rota, Hora Viagem, Sequencia do PED, Embarque

## g0026（1 列）
- 見出し：Consorcio
- 例1 値：CONSORCIO BHLESTE | CONSORCIO BHLESTE | CONSORCIO BHLESTE | CONSORCIO BHLESTE | CONSORCIO BHLESTE
  - 同じ表の列：Linha/SubLinha, Servico, Data Pesquisa, Dia Semana, Rota, Hora Viagem, Sequencia do PED, Embarque

## g0027（1 列）
- 見出し：Data Pesquisa
- 例1 値：10/11/2014 | 05/12/2015 | 05/12/2015 | 05/12/2015 | 05/12/2015
  - 同じ表の列：Linha/SubLinha, Servico, Consorcio, Dia Semana, Rota, Hora Viagem, Sequencia do PED, Embarque

## g0028（1 列）
- 見出し：Dia Semana
- 例1 値：Sabado | Sabado | Segunda | Sabado | Sabado
  - 同じ表の列：Linha/SubLinha, Servico, Consorcio, Data Pesquisa, Rota, Hora Viagem, Sequencia do PED, Embarque

## g0029（1 列）
- 見出し：Rota
- 例1 値：Pc1->Pc2 | Pc1->Pc2 | Pc1->Pc2 | Pc1->Pc2 | Pc1->Pc2
  - 同じ表の列：Linha/SubLinha, Servico, Consorcio, Data Pesquisa, Dia Semana, Hora Viagem, Sequencia do PED, Embarque

## g0030（1 列）
- 見出し：Hora Viagem
- 例1 値：09:24 | 06:00 | 06:42 | 16:26 | 10:20
  - 同じ表の列：Linha/SubLinha, Servico, Consorcio, Data Pesquisa, Dia Semana, Rota, Sequencia do PED, Embarque

## g0031（1 列）
- 見出し：Sequencia do PED
- 例1 値：13 | 36 | 6 | 43 | 19
  - 同じ表の列：Linha/SubLinha, Servico, Consorcio, Data Pesquisa, Dia Semana, Rota, Hora Viagem, Embarque

## g0032（1 列）
- 見出し：Embarque
- 例1 値：0 | 0 | 0 | 0 | 3
  - 同じ表の列：Linha/SubLinha, Servico, Consorcio, Data Pesquisa, Dia Semana, Rota, Hora Viagem, Sequencia do PED

## g0033（1 列）
- 見出し：Desembarque
- 例1 値：0 | 1 | 1 | 0 | 0
  - 同じ表の列：Linha/SubLinha, Servico, Consorcio, Data Pesquisa, Dia Semana, Rota, Hora Viagem, Sequencia do PED

## g0034（1 列）
- 見出し：ID_VILA_FAVELA
- 例1 値：1432 | 1446 | 1458 | 1403 | 1338
  - 同じ表の列：APELIDO_LOCALIDADE, DESC_LOCALIDADE, QTDE_DOMICILIO, FONTE_DOMICILIO, DATA_QTDE_DOMICILIO, QTDE_ESTABELECIMENTO, FONTE_ESTABELECIMEN…, DATA_QTDE_ESTABELEC…

## g0035（1 列）
- 見出し：APELIDO_LOCALIDADE
- 例1 値：Buraco de Cobra | Nova Cintra | Vila Dona Geralda | Buraco Quente | Vila Santo Antônio
  - 同じ表の列：ID_VILA_FAVELA, DESC_LOCALIDADE, QTDE_DOMICILIO, FONTE_DOMICILIO, DATA_QTDE_DOMICILIO, QTDE_ESTABELECIMENTO, FONTE_ESTABELECIMEN…, DATA_QTDE_ESTABELEC…

## g0036（1 列）
- 見出し：DESC_LOCALIDADE
- 例1 値：Vila / Favela | Vila / Favela | Vila / Favela | Vila / Favela | Vila / Favela
  - 同じ表の列：ID_VILA_FAVELA, APELIDO_LOCALIDADE, QTDE_DOMICILIO, FONTE_DOMICILIO, DATA_QTDE_DOMICILIO, QTDE_ESTABELECIMENTO, FONTE_ESTABELECIMEN…, DATA_QTDE_ESTABELEC…

## g0037（1 列）
- 見出し：QTDE_DOMICILIO
- 例1 値：210 | 89 | 1367 | 728 | 104
  - 同じ表の列：ID_VILA_FAVELA, APELIDO_LOCALIDADE, DESC_LOCALIDADE, FONTE_DOMICILIO, DATA_QTDE_DOMICILIO, QTDE_ESTABELECIMENTO, FONTE_ESTABELECIMEN…, DATA_QTDE_ESTABELEC…

## g0038（1 列）
- 見出し：FONTE_DOMICILIO
- 例1 値：URBEL - Informações Cadastrais | IBGE - Censo 2010 | IBGE - Censo 2010 | URBEL - Estudo Proporcional sobre Censo… | URBEL - Contagem através de fotointerpr…
  - 同じ表の列：ID_VILA_FAVELA, APELIDO_LOCALIDADE, DESC_LOCALIDADE, QTDE_DOMICILIO, DATA_QTDE_DOMICILIO, QTDE_ESTABELECIMENTO, FONTE_ESTABELECIMEN…, DATA_QTDE_ESTABELEC…

## g0039（1 列）
- 見出し：DATA_QTDE_DOMICILIO
- 例1 値：01/12/2014 | 01/12/2014 | 01/12/2014 | 01/12/2014 | 01/12/2014
  - 同じ表の列：ID_VILA_FAVELA, APELIDO_LOCALIDADE, DESC_LOCALIDADE, QTDE_DOMICILIO, FONTE_DOMICILIO, QTDE_ESTABELECIMENTO, FONTE_ESTABELECIMEN…, DATA_QTDE_ESTABELEC…

## g0040（1 列）
- 見出し：QTDE_ESTABELECIMENTO
- 例1 値：35 | 169 | 5 | 8 | 10
  - 同じ表の列：ID_VILA_FAVELA, APELIDO_LOCALIDADE, DESC_LOCALIDADE, QTDE_DOMICILIO, FONTE_DOMICILIO, DATA_QTDE_DOMICILIO, FONTE_ESTABELECIMEN…, DATA_QTDE_ESTABELEC…

## g0041（1 列）
- 見出し：FONTE_ESTABELECIMENTO
- 例1 値：URBEL - Estudo Proporcional sobre Censo… | URBEL - Estudo Proporcional sobre Censo… | URBEL - Estudo Proporcional sobre Censo… | IBGE - Censo 2010 | IBGE - Censo 2010
  - 同じ表の列：ID_VILA_FAVELA, APELIDO_LOCALIDADE, DESC_LOCALIDADE, QTDE_DOMICILIO, FONTE_DOMICILIO, DATA_QTDE_DOMICILIO, QTDE_ESTABELECIMENTO, DATA_QTDE_ESTABELEC…

## g0042（1 列）
- 見出し：DATA_QTDE_ESTABELECIMENTO
- 例1 値：01/12/2014 | 01/12/2014 | 01/12/2014 | 01/12/2014 | 01/12/2014
  - 同じ表の列：ID_VILA_FAVELA, APELIDO_LOCALIDADE, DESC_LOCALIDADE, QTDE_DOMICILIO, FONTE_DOMICILIO, DATA_QTDE_DOMICILIO, QTDE_ESTABELECIMENTO, FONTE_ESTABELECIMEN…

## g0043（1 列）
- 見出し：QTDE_POPULACAO_EXISTENTE
- 例1 値：391 | 1173 | 1661 | 15003 | 95
  - 同じ表の列：ID_VILA_FAVELA, APELIDO_LOCALIDADE, DESC_LOCALIDADE, QTDE_DOMICILIO, FONTE_DOMICILIO, DATA_QTDE_DOMICILIO, QTDE_ESTABELECIMENTO, FONTE_ESTABELECIMEN…

## g0044（2 列）
- 見出し：Topic
- 例1 値：Population | Population | Population | Education | Population
  - 同じ表の列：Variable, Definition, Universe
- 例2 値：Labor | Population | Population | Population | Population
  - 同じ表の列：Variable, Definition, Universe

## g0045（1 列）
- 見出し：Variable
- 例1 値：Labor_Commute_total_commuters | Population_Nativity_native_born | Population_Age_share_20_to_34 | Population_Age_65_plus | Housing_Vehicles_share_no_vehicles
  - 同じ表の列：Topic, Definition, Universe

## g0046（1 列）
- 見出し：Definition
- 例1 値：Total Workers aged 16 and over | Female population not in labor force | Share of population with attainment of … | Population living in group quarters | White alone
  - 同じ表の列：Topic, Variable, Universe

## g0047（1 列）
- 見出し：Universe
- 例1 値：Households | Total Population | Total Workers aged 16 and over | Total Population | Total Population
  - 同じ表の列：Topic, Variable, Definition

## g0048（1 列）
- 見出し：1
- 例1 値：172 | 424 | 55 | 451 | 313
  - 同じ表の列：総合, 101.5, 99.4, 2, 2.1, -0.6

## g0049（1 列）
- 見出し：総合
- 例1 値：他の諸雑費 | 交通 | 被服及び履物 | 履物類 | 生鮮食品及びエネルギーを除く総合
  - 同じ表の列：1, 101.5, 99.4, 2, 2.1, -0.6

## g0050（1 列）
- 見出し：101.5
- 例1 値：99.7 | 100.3 | 103.3 | 111.1 | 101.1
  - 同じ表の列：1, 総合, 99.4, 2, 2.1, -0.6

## g0051（1 列）
- 見出し：99.4
- 例1 値：99.9 | 101.4 | 98.8 | 94.8 | 102.1
  - 同じ表の列：1, 総合, 101.5, 2, 2.1, -0.6

## g0052（1 列）
- 見出し：2
- 例1 値：-12.4 | 6 | -1.7 | 3.7 | 0.4
  - 同じ表の列：1, 総合, 101.5, 99.4, 2.1, -0.6

## g0053（1 列）
- 見出し：2.1
- 例1 値：0 | 0.1 | 0 | 0 | 0
  - 同じ表の列：1, 総合, 101.5, 99.4, 2, -0.6

## g0054（1 列）
- 見出し：-0.6
- 例1 値：1.7 | 1.1 | -0.5 | 0 | -0.8
  - 同じ表の列：1, 総合, 101.5, 99.4, 2, 2.1

## g0055（1 列）
- 見出し：URI
- 例1 値：https://covid19.supportnavi.metro.tokyo… | https://covid19.supportnavi.metro.tokyo… | https://covid19.supportnavi.metro.tokyo… | https://covid19.supportnavi.metro.tokyo… | https://covid19.supportnavi.metro.tokyo…
  - 同じ表の列：psid, provider, provider.prefecture…, content.target, content.application…, content.application…, content.information…, tags

## g0056（1 列）
- 見出し：psid
- 例1 値：psid1.0+JA8000020130001+UM002553 | psid1.0+JA8000020130001+UM002264 | psid1.0+JA8000020130001+UM002256 | psid1.0+JA8000020130001+UM002482 | psid1.0+JA8000020130001+UM002586
  - 同じ表の列：URI, provider, provider.prefecture…, content.target, content.application…, content.application…, content.information…, tags

## g0057（1 列）
- 見出し：provider
- 例1 値：東京都 | 東京都 | 東京都 | 東京都 | 東京都
  - 同じ表の列：URI, psid, provider.prefecture…, content.target, content.application…, content.application…, content.information…, tags

## g0058（1 列）
- 見出し：provider.prefecture_id
- 例1 値：13 | 13 | 13 | 13 | 13
  - 同じ表の列：URI, psid, provider, content.target, content.application…, content.application…, content.information…, tags

## g0059（1 列）
- 見出し：content.target
- 例1 値：新型コロナウイルスの感染拡大に伴い、一時的に道路占用料を納付期限内に納めること… | 全学年の学生が対象です。 ※ただし、本科の第1学年から第3学年まで(入学後在籍… | 島しょの港湾、漁港などに係る占用者等 | 新型コロナウイルス感染症の影響により、移転資金貸付金の納付期限内の返済が困難と… | ◯タクシー事業者向け補助金 東京都内の法人・個人タクシー(ハイヤー含む)事業者…
  - 同じ表の列：URI, psid, provider, provider.prefecture…, content.application…, content.application…, content.information…, tags

## g0060（1 列）
- 見出し：content.application_start_date
- 例1 値：2021年4月30日 | 2022年3月22日 | 2022年6月24日 | 2021年5月6日 | 2020年9月10日
  - 同じ表の列：URI, psid, provider, provider.prefecture…, content.target, content.application…, content.information…, tags

## g0061（1 列）
- 見出し：content.application_close_date
- 例1 値：2022年10月31日 | 2022年8月31日 | 2022年9月30日 | 2023年3月31日 | 2023年3月31日
  - 同じ表の列：URI, psid, provider, provider.prefecture…, content.target, content.application…, content.information…, tags

## g0062（1 列）
- 見出し：content.information_release_date
- 例1 値：2022-03-02T06:10:24 | 2022-05-18T02:29:29 | 2022-03-30T08:05:55 | 2021-03-10T13:26:31 | 2022-04-27T02:01:46
  - 同じ表の列：URI, psid, provider, provider.prefecture…, content.target, content.application…, content.application…, tags

## g0063（1 列）
- 見出し：tags
- 例1 値：個人向け 行政からのお知らせ 東京都 行政からのお知らせ | 補助金 東京都 医療の確保・整備に関すること | 事業者向け 事業相談 休校 臨時休業 中小企業向け その他・個人事業主向け 東… | 事業者向け 中小企業向け その他・個人事業主向け 給付・助成 東京都 雇用・従… | 支払いの減免・猶予 事業者向け 新型コロナ 東京都 公的施設の使用
  - 同じ表の列：URI, psid, provider, provider.prefecture…, content.target, content.application…, content.application…, content.information…

## g0064（1 列）
- 見出し：theme
- 例1 値：資金繰り(もらう) | 行政からのお知らせ | 雇用・従業員に関すること | 相談 | 相談
  - 同じ表の列：URI, psid, provider, provider.prefecture…, content.target, content.application…, content.application…, content.information…

## g0065（1 列）
- 見出し：性別
- 例1 値：男子(%) | 女子(%) | 合計(%) | 合計(人) | 女子(人)
  - 同じ表の列：小学生1年生, 小学生2年生, 小学生3年生, 小学生4年生, 小学生5年生, 小学生6年生, 中学生1年生, 中学生2年生

## g0066（1 列）
- 見出し：小学生1年生
- 例1 値：84 | 167 | 8.3 | 8.4 | 83
  - 同じ表の列：性別, 小学生2年生, 小学生3年生, 小学生4年生, 小学生5年生, 小学生6年生, 中学生1年生, 中学生2年生

## g0067（1 列）
- 見出し：小学生2年生
- 例1 値：8.3 | 8.4 | 83 | 8.4 | 167
  - 同じ表の列：性別, 小学生1年生, 小学生3年生, 小学生4年生, 小学生5年生, 小学生6年生, 中学生1年生, 中学生2年生

## g0068（1 列）
- 見出し：小学生3年生
- 例1 値：166 | 8.3 | 8.3 | 83 | 8.3
  - 同じ表の列：性別, 小学生1年生, 小学生2年生, 小学生4年生, 小学生5年生, 小学生6年生, 中学生1年生, 中学生2年生

## g0069（1 列）
- 見出し：小学生4年生
- 例1 値：8.4 | 83 | 8.3 | 84 | 167
  - 同じ表の列：性別, 小学生1年生, 小学生2年生, 小学生3年生, 小学生5年生, 小学生6年生, 中学生1年生, 中学生2年生

## g0070（1 列）
- 見出し：小学生5年生
- 例1 値：83 | 8.4 | 8.3 | 8.4 | 167
  - 同じ表の列：性別, 小学生1年生, 小学生2年生, 小学生3年生, 小学生4年生, 小学生6年生, 中学生1年生, 中学生2年生

## g0071（1 列）
- 見出し：小学生6年生
- 例1 値：8.3 | 8.3 | 83 | 83 | 166
  - 同じ表の列：性別, 小学生1年生, 小学生2年生, 小学生3年生, 小学生4年生, 小学生5年生, 中学生1年生, 中学生2年生

## g0072（1 列）
- 見出し：中学生1年生
- 例1 値：83 | 84 | 167 | 8.4 | 8.4
  - 同じ表の列：性別, 小学生1年生, 小学生2年生, 小学生3年生, 小学生4年生, 小学生5年生, 小学生6年生, 中学生2年生

## g0073（1 列）
- 見出し：中学生2年生
- 例1 値：8.4 | 167 | 83 | 8.3 | 84
  - 同じ表の列：性別, 小学生1年生, 小学生2年生, 小学生3年生, 小学生4年生, 小学生5年生, 小学生6年生, 中学生1年生

## g0074（1 列）
- 見出し：中学生3年生
- 例1 値：8.3 | 83 | 8.3 | 83 | 8.3
  - 同じ表の列：性別, 小学生1年生, 小学生2年生, 小学生3年生, 小学生4年生, 小学生5年生, 小学生6年生, 中学生1年生

## g0075（1 列）
- 見出し：学校種別
- 例1 値：専修学校 | 小学校 | 注2)「高等学校(通信制)」の学校数のうち7校(公立校3校、私立校4校)は、「… | 専修学校 | 義務教育学校
  - 同じ表の列：設置者等, 学校数(校、園), 学校数/本校(校、園), 学校数/分校(校、園), 学級数(学級), 在学者数(人), 在学者数/男(人), 在学者数/女(人)

## g0076（1 列）
- 見出し：設置者等
- 例1 値：私立 | 公立 | 総数(国・公・私立) | 国立 | 公立
  - 同じ表の列：学校種別, 学校数(校、園), 学校数/本校(校、園), 学校数/分校(校、園), 学級数(学級), 在学者数(人), 在学者数/男(人), 在学者数/女(人)

## g0077（1 列）
- 見出し：学校数(校、園)
- 例1 値：6 | 148 | 3 | 373 | -
  - 同じ表の列：学校種別, 設置者等, 学校数/本校(校、園), 学校数/分校(校、園), 学級数(学級), 在学者数(人), 在学者数/男(人), 在学者数/女(人)

## g0078（1 列）
- 見出し：学校数/本校(校、園)
- 例1 値：187 | 11 | 913 | 188 | 8
  - 同じ表の列：学校種別, 設置者等, 学校数(校、園), 学校数/分校(校、園), 学級数(学級), 在学者数(人), 在学者数/男(人), 在学者数/女(人)

## g0079（2 列）
- 見出し：学校数/分校(校、園)
- 例1 値：- | - | - | - | -
  - 同じ表の列：学校種別, 設置者等, 学校数(校、園), 学校数/本校(校、園), 学級数(学級), 在学者数(人), 在学者数/男(人), 在学者数/女(人)
- 例2 値：- | - | - | - | -
  - 同じ表の列：学校種別, 設置者等, 学校数(校、園), 学校数/本校(校、園), 学校数/小中一貫教育(再掲)(校、園), 学校数/中高一貫教育(再掲)(校、園), 学級数(学級), 在学者数(人)

## g0080（1 列）
- 見出し：学級数(学級)
- 例1 値：3404 | ... | ... | 358 | 3723
  - 同じ表の列：学校種別, 設置者等, 学校数(校、園), 学校数/本校(校、園), 学校数/分校(校、園), 在学者数(人), 在学者数/男(人), 在学者数/女(人)

## g0081（1 列）
- 見出し：在学者数(人)
- 例1 値：10403 | 25150 | 207 | 11637 | 227462
  - 同じ表の列：学校種別, 設置者等, 学校数(校、園), 学校数/本校(校、園), 学校数/分校(校、園), 学級数(学級), 在学者数/男(人), 在学者数/女(人)

## g0082（2 列）
- 見出し：在学者数/男(人)
- 例1 値：88868 | 38906 | 5140 | 10509 | 13534
  - 同じ表の列：学校種別, 設置者等, 学校数(校、園), 学校数/本校(校、園), 学校数/分校(校、園), 学級数(学級), 在学者数(人), 在学者数/女(人)
- 例2 値：127 | 10534 | 58741 | 10182 | 584
  - 同じ表の列：学校種別, 設置者等, 学校数(校、園), 学校数/本校(校、園), 学校数/分校(校、園), 学校数/小中一貫教育(再掲)(校、園), 学校数/中高一貫教育(再掲)(校、園), 学級数(学級)

## g0083（1 列）
- 見出し：在学者数/女(人)
- 例1 値：4634 | 297950 | 4834 | 1789 | -
  - 同じ表の列：学校種別, 設置者等, 学校数(校、園), 学校数/本校(校、園), 学校数/分校(校、園), 学級数(学級), 在学者数(人), 在学者数/男(人)

## g0084（1 列）
- 見出し：教員数(本務者)(人)
- 例1 値：2180 | 10056 | 1541 | 21442 | 6935
  - 同じ表の列：学校種別, 設置者等, 学校数(校、園), 学校数/本校(校、園), 学校数/分校(校、園), 学級数(学級), 在学者数(人), 在学者数/男(人)

## g0085（1 列）
- 見出し：駅名
- 例1 値：舎人 | 足立小台 | 熊野前 | 西日暮里 | 江北
  - 同じ表の列：一日平均乗車人員, 一日平均降車人員

## g0086（1 列）
- 見出し：一日平均乗車人員
- 例1 値：26123 | 6348 | 90024 | 2431 | 4439
  - 同じ表の列：駅名, 一日平均降車人員

## g0087（1 列）
- 見出し：一日平均降車人員
- 例1 値：2389 | 4562 | 90024 | 2582 | 6570
  - 同じ表の列：駅名, 一日平均乗車人員

## g0088（53 列）
- 見出し：全国地方公共団体コード
- 例1 値：131024 | 131024 | 131024 | 131024 | 131024
  - 同じ表の列：地方公共団体名, 名称, 湊1, 面積(m2)
- 例2 値：131041 | 131041 | 131041 | 131041 | 131041
  - 同じ表の列：地方公共団体名, 名称, 面積(m2)

## g0089（1 列）
- 見出し：地方公共団体名
- 例1 値：東京都中央区 | 東京都中央区 | 東京都中央区 | 東京都中央区 | 東京都中央区
  - 同じ表の列：全国地方公共団体コード, 名称, 湊1, 面積(m2)

## g0090（1 列）
- 見出し：名称
- 例1 値：水谷橋公園 | 晴海第三公園 | 千代田公園 | 地蔵橋公園 | 築地川亀井橋公園
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 湊1, 面積(m2)

## g0091（1 列）
- 見出し：湊1
- 例1 値：勝どき5 | 銀座1 | 日本橋中洲 | 日本橋箱崎町 | 明石町
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 面積(m2)

## g0092（3 列）
- 見出し：面積(m2)
- 例1 値：7103.16 | 1133.19 | 816.95 | 2182.9 | 47452.83
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 湊1
- 例2 値：484.35 | 1900.84 | 538.09 | 53.97 | 79.68
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称

## g0093（2 列）
- 見出し：年月日[西暦]
- 例1 値：20260901 | 20260301 | 20260801 | 20260601 | 20260701
  - 同じ表の列：0歳男[人], 0歳女[人], 1歳男[人], 1歳女[人], 2歳男[人], 2歳女[人], 3歳男[人], 3歳女[人]
- 例2 値：20260701 | 20260801 | 20260601 | 20260101 | 20260301
  - 同じ表の列：地区, 世帯数, 人口男[人], 人口女[人], 人口合計[人]

## g0094（1 列）
- 見出し：0歳男[人]
- 例1 値：1184 | 1193 | 1172 | 1175 | 1179
  - 同じ表の列：年月日[西暦], 0歳女[人], 1歳男[人], 1歳女[人], 2歳男[人], 2歳女[人], 3歳男[人], 3歳女[人]

## g0095（1 列）
- 見出し：0歳女[人]
- 例1 値：1166 | 1182 | 1189 | 1158 | 1129
  - 同じ表の列：年月日[西暦], 0歳男[人], 1歳男[人], 1歳女[人], 2歳男[人], 2歳女[人], 3歳男[人], 3歳女[人]

## g0096（1 列）
- 見出し：1歳男[人]
- 例1 値：1143 | 1187 | 1144 | 1195 | 1147
  - 同じ表の列：年月日[西暦], 0歳男[人], 0歳女[人], 1歳女[人], 2歳男[人], 2歳女[人], 3歳男[人], 3歳女[人]

## g0097（1 列）
- 見出し：1歳女[人]
- 例1 値：1118 | 1111 | 1129 | 1111 | 1104
  - 同じ表の列：年月日[西暦], 0歳男[人], 0歳女[人], 1歳男[人], 2歳男[人], 2歳女[人], 3歳男[人], 3歳女[人]

## g0098（1 列）
- 見出し：2歳男[人]
- 例1 値：1190 | 1206 | 1207 | 1171 | 1190
  - 同じ表の列：年月日[西暦], 0歳男[人], 0歳女[人], 1歳男[人], 1歳女[人], 2歳女[人], 3歳男[人], 3歳女[人]

## g0099（1 列）
- 見出し：2歳女[人]
- 例1 値：1095 | 1115 | 1130 | 1075 | 1080
  - 同じ表の列：年月日[西暦], 0歳男[人], 0歳女[人], 1歳男[人], 1歳女[人], 2歳男[人], 3歳男[人], 3歳女[人]

## g0100（1 列）
- 見出し：3歳男[人]
- 例1 値：1153 | 1145 | 1158 | 1160 | 1147
  - 同じ表の列：年月日[西暦], 0歳男[人], 0歳女[人], 1歳男[人], 1歳女[人], 2歳男[人], 2歳女[人], 3歳女[人]

## g0101（1 列）
- 見出し：3歳女[人]
- 例1 値：1127 | 1072 | 1134 | 1134 | 1117
  - 同じ表の列：年月日[西暦], 0歳男[人], 0歳女[人], 1歳男[人], 1歳女[人], 2歳男[人], 2歳女[人], 3歳男[人]

## g0102（1 列）
- 見出し：4歳男[人]
- 例1 値：1166 | 1195 | 1211 | 1187 | 1185
  - 同じ表の列：年月日[西暦], 0歳男[人], 0歳女[人], 1歳男[人], 1歳女[人], 2歳男[人], 2歳女[人], 3歳男[人]

## g0103（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区
  - 同じ表の列：全国地方公共団体コード, 名称, 面積(m2)
- 例2 値：東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区 | 東京都新宿区
  - 同じ表の列：全国地方公共団体コード, ID, 名称, 建物名等(方書)

## g0104（1 列）
- 見出し：名称
- 例1 値：須賀公園 | 荒井山公園 | 甘泉園公園 | 藤兵衛公園 | 新小川公園
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 面積(m2)

## g0105（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都江東区 | 東京都江東区 | 東京都江東区 | 東京都江東区 | 東京都江東区
  - 同じ表の列：全国地方公共団体コード, 名称, 面積(m2)
- 例2 値：東京都江東区 | 東京都江東区 | 東京都江東区 | 東京都江東区 | 東京都江東区
  - 同じ表の列：全国地方公共団体コード, 名称

## g0106（1 列）
- 見出し：名称
- 例1 値：江東区立亀戸運動公園 | 江東区立油堀川公園 | 江東区立豊洲ぐるり公園 | 江東区立八名川公園 | 江東区立日曹橋公園
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 面積(m2)

## g0107（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区
  - 同じ表の列：全国地方公共団体コード, 確認番号, 名称, 確認年月日
- 例2 値：東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区 | 東京都品川区
  - 同じ表の列：全国地方公共団体コード, 確認番号, 営業形態, 名称, 確認年月日

## g0108（1 列）
- 見出し：確認番号
- 例1 値：品保セ衛環き第133号 | 品保生環き第79号 | 品保生環き第67号 | 6品保生環き第16号 | 品保生環き第80号
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 名称, 確認年月日

## g0109（1 列）
- 見出し：名称
- 例1 値：ヘアーサロンアサコ | バーバーホンダ | トウキョウズバーバー | ヘアーサロンイバヤシ | クイン理容
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 確認番号, 確認年月日

## g0110（2 列）
- 見出し：確認年月日
- 例1 値：1984-02-17T00:00:00 | 2008-06-19T00:00:00 | 2010-09-22T00:00:00 | 2001-03-15T00:00:00 | 2018-03-07T00:00:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 確認番号, 名称
- 例2 値：2009-07-09T00:00:00 | 2019-03-27T00:00:00 | 2014-04-17T00:00:00 | 1989-01-10T00:00:00 | 1983-10-05T00:00:00
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 確認番号, 営業形態, 名称

## g0111（24 列）
- 見出し：ID
- 例1 値：269 | 73 | 229 | 219 | 244
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 営業形態, 名称
- 例2 値：19 | 36 | 106 | 147 | 32
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 指定番号, 樹種名称, 樹種名称_カナ, 指定状態, 指定年, 指定月

## g0112（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都大田区 | 東京都大田区 | 東京都大田区 | 東京都大田区 | 東京都大田区
  - 同じ表の列：全国地方公共団体コード, ID, 営業形態, 名称
- 例2 値：東京都大田区 | 東京都大田区 | 東京都大田区 | 東京都大田区 | 東京都大田区
  - 同じ表の列：全国地方公共団体コード, ID, 営業形態, 名称

## g0113（1 列）
- 見出し：営業形態
- 例1 値：クリーニング所(取次所) | クリーニング所(取次所) | クリーニング所(一般) | クリーニング所(一般) | クリーニング所(取次所)
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 名称

## g0114（1 列）
- 見出し：名称
- 例1 値：不入流伝習館 | ザ・リバープレイス フロント | ロイヤルクリーニング北千束駅前店 | ポニークリーニング糀谷駅前店 | 株式会社 JALエービーシー
  - 同じ表の列：全国地方公共団体コード, ID, 地方公共団体名, 営業形態

## g0115（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区
  - 同じ表の列：全国地方公共団体コード, 名称
- 例2 値：東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区 | 東京都世田谷区
  - 同じ表の列：全国地方公共団体コード, 名称, 間取り, 建設年度, 管理戸数

## g0116（1 列）
- 見出し：名称
- 例1 値：弦巻三丁目ゆずりは公園 | 弁天公園 | ねこじゃらし公園 | 桜丘こぶし公園 | 宇奈根東部記念公園
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名

## g0117（2 列）
- 見出し：地方公共団体名
- 例1 値：東京都渋谷区 | 東京都渋谷区 | 東京都渋谷区 | 東京都渋谷区 | 東京都渋谷区
  - 同じ表の列：全国地方公共団体コード, 年, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚
- 例2 値：東京都渋谷区 | 東京都渋谷区 | 東京都渋谷区 | 東京都渋谷区 | 東京都渋谷区
  - 同じ表の列：全国地方公共団体コード, 名称, 名称_カナ, 建物名等(方書), 車椅子可, 車椅子貸出, ツエ貸出, バリアフリートイレ

## g0118（1 列）
- 見出し：年
- 例1 値：2022 | 2018 | 2020 | 2023 | 2019
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 月, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚

## g0119（1 列）
- 見出し：月
- 例1 値：4 | 4 | 4 | 4 | 4
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 年, 戸籍謄抄本等, 住民票の写し, 印鑑証明, 婚姻, 離婚

## g0120（1 列）
- 見出し：戸籍謄抄本等
- 例1 値：79,981 | 65,504 | 80,456 | 79,824 | 85,236
  - 同じ表の列：全国地方公共団体コード, 地方公共団体名, 年, 月, 住民票の写し, 印鑑証明, 婚姻, 離婚

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
