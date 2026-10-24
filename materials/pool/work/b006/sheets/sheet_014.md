# ラベル用シート 014 / 018

- LABEL_GUIDE v1.8 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_014.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1561（1 列）
- 見出し：ACAO
- 例1 値：2001 - Execução da Atividade Institucio… | 2001 - Execução da Atividade Institucio… | 2001 - Execução da Atividade Institucio… | 2001 - Execução da Atividade Institucio… | 2001 - Execução da Atividade Institucio…
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, SUBACAO

## g1562（1 列）
- 見出し：SUBACAO
- 例1 値：001 - EXECUÇÃO DA ATIVIDADE INSTITUCION… | 001 - EXECUÇÃO DA ATIVIDADE INSTITUCION… | 001 - EXECUÇÃO DA ATIVIDADE INSTITUCION… | 001 - EXECUÇÃO DA ATIVIDADE INSTITUCION… | 001 - EXECUÇÃO DA ATIVIDADE INSTITUCION…
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO

## g1563（1 列）
- 見出し：CATEGORIA_ECONOMICA
- 例1 値：3 - Despesas Correntes | 3 - Despesas Correntes | 3 - Despesas Correntes | 3 - Despesas Correntes | 3 - Despesas Correntes
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO

## g1564（2 列）
- 見出し：ANO
- 例1 値：2020 | 2020 | 2020 | 2020 | 2020
  - 同じ表の列：ORGAO_ENTIDADE, CONTRATADO, OBJETO, DATA_INICIO_VIGENCIA, DATA_FIM_VIGENCIA, VALOR, PROCESSO_COMPRA
- 例2 値：2021 | 2021 | 2021 | 2021 | 2021
  - 同じ表の列：num_not, racacor, dt_notific, dt_sin_pri, dt_nasc, forma_doenca, classificacao, evolucao

## g1565（1 列）
- 見出し：ORGAO_ENTIDADE
- 例1 値：Secretaria Municipal de Saude | Secretaria Municipal de Seguranca e Pre… | Secretaria Municipal de Assitência Soci… | Secretaria Municipal de Saude | Secretaria Municipal de Seguranca e Pre…
  - 同じ表の列：ANO, CONTRATADO, OBJETO, DATA_INICIO_VIGENCIA, DATA_FIM_VIGENCIA, VALOR, PROCESSO_COMPRA

## g1566（1 列）
- 見出し：CONTRATADO
- 例1 値：Provider Produtos Hospitalares e Senean… | HCE - Investimentos Importacao e Export… | Provest - Protecao e Vestuario Industri… | Abasantos | Saude e Tecnologia Ltda
  - 同じ表の列：ANO, ORGAO_ENTIDADE, OBJETO, DATA_INICIO_VIGENCIA, DATA_FIM_VIGENCIA, VALOR, PROCESSO_COMPRA

## g1567（1 列）
- 見出し：OBJETO
- 例1 値：Aquisicao de Respiradores categoria PFF… | Luvas para procedimentos e Gorros desca… | Respirador purificador de ar tipo pecas… | Mascaras, luvas, aventais e alcool | oculos de protecao
  - 同じ表の列：ANO, ORGAO_ENTIDADE, CONTRATADO, DATA_INICIO_VIGENCIA, DATA_FIM_VIGENCIA, VALOR, PROCESSO_COMPRA

## g1568（1 列）
- 見出し：DATA_INICIO_VIGENCIA
- 例1 値：Entrega imediata | 13/04/2020 | 27/03/2020 | 25/03/2020 | 23/03/2020
  - 同じ表の列：ANO, ORGAO_ENTIDADE, CONTRATADO, OBJETO, DATA_FIM_VIGENCIA, VALOR, PROCESSO_COMPRA

## g1569（1 列）
- 見出し：DATA_FIM_VIGENCIA
- 例1 値：29/07/2020 | 13/04/2020 | 13/06/2016 | 31/03/2020 | 22/09/2020
  - 同じ表の列：ANO, ORGAO_ENTIDADE, CONTRATADO, OBJETO, DATA_INICIO_VIGENCIA, VALOR, PROCESSO_COMPRA

## g1570（1 列）
- 見出し：VALOR
- 例1 値：39360,00 | 76600,00 | 30000,00 | 130000,00 | 120000,00
  - 同じ表の列：ANO, ORGAO_ENTIDADE, CONTRATADO, OBJETO, DATA_INICIO_VIGENCIA, DATA_FIM_VIGENCIA, PROCESSO_COMPRA

## g1571（1 列）
- 見出し：PROCESSO_COMPRA
- 例1 値：04.000.318.20.87 | 04.000.397.20.53 | 01.028.433.20.19 | 04.000.408.20.78 | 01.030.638.20.64
  - 同じ表の列：ANO, ORGAO_ENTIDADE, CONTRATADO, OBJETO, DATA_INICIO_VIGENCIA, DATA_FIM_VIGENCIA, VALOR

## g1572（1 列）
- 見出し：IdAssunto
- 例1 値：203653 | 203553 | 204274 | 203075 | 203846
  - 同じ表の列：IdMan, Serie, DataMan, DataLoc, Assunto, Status, DataStatus, dias tram

## g1573（1 列）
- 見出し：IdMan
- 例1 値：197617 | 198518 | 198226 | 197764 | 198754
  - 同じ表の列：IdAssunto, Serie, DataMan, DataLoc, Assunto, Status, DataStatus, dias tram

## g1574（1 列）
- 見出し：Serie
- 例1 値：A | A
  - 同じ表の列：IdAssunto, IdMan, DataMan, DataLoc, Assunto, Status, DataStatus, dias tram

## g1575（1 列）
- 見出し：DataMan
- 例1 値：03/01/2020 11:30 | 06/01/2020 16:56 | 06/01/2020 08:04 | 03/01/2020 18:27 | 07/01/2020 21:54
  - 同じ表の列：IdAssunto, IdMan, Serie, DataLoc, Assunto, Status, DataStatus, dias tram

## g1576（1 列）
- 見出し：DataLoc
- 例1 値：06/01/2020 16:36 | 14/01/2020 16:11 | 13/01/2020 13:42 | 06/01/2020 15:43 | 14/01/2020 17:52
  - 同じ表の列：IdAssunto, IdMan, Serie, DataMan, Assunto, Status, DataStatus, dias tram

## g1577（1 列）
- 見出し：Assunto
- 例1 値：RECLAMAÇÃO - SERVIÇOS DE IPTU | SOLICITAÇÕES DOS SERVIÇOS DO MEIO AMBIE… | COMUNICAÇÃO DE IRREGULARIDADES | SUGESTÕES PARA OS SEVIÇOS MEIO AMBIENTE | ORIENTAÇÕES SOBRE SERVIÇOS DE PODA
  - 同じ表の列：IdAssunto, IdMan, Serie, DataMan, DataLoc, Status, DataStatus, dias tram

## g1578（1 列）
- 見出し：DataStatus
- 例1 値：16/01/2020 10:43 | 04/02/2020 11:52 | 27/01/2020 10:53 | 13/02/2020 13:43 | 10/02/2020 16:32
  - 同じ表の列：IdAssunto, IdMan, Serie, DataMan, DataLoc, Assunto, Status, dias tram

## g1579（1 列）
- 見出し：dias tram
- 例1 値：49 | 21 | 73 | 35 | 24
  - 同じ表の列：IdAssunto, IdMan, Serie, DataMan, DataLoc, Assunto, Status, DataStatus

## g1580（1 列）
- 見出し：LocalDestino
- 例1 値：PBH/SUOUVI | PBH/SUOUVI | PBH/SUOUVI | PBH/SUOUVI | PBH/SUOUVI
  - 同じ表の列：IdAssunto, IdMan, Serie, DataMan, DataLoc, Assunto, Status, DataStatus

## g1581（1 列）
- 見出し：No do ticket
- 例1 値：31.00455174/2021-63 | 31.00452457/2021-90 | 31.00448444/2021-92 | 31.00451492/2021-52 | 31.00445031/2021-93
  - 同じ表の列：Data de registro da…, Data de encaminhame…, Assunto, Etapa, Dias em tramitacao …, SLA, Canal de captacao, Origem da demanda

## g1582（1 列）
- 見出し：Data de registro da Manifestacao
- 例1 値：01/12/2021 | 02/12/2021 | 01/12/2021 | 09/12/2021 | 02/12/2021
  - 同じ表の列：No do ticket, Data de encaminhame…, Assunto, Etapa, Dias em tramitacao …, SLA, Canal de captacao, Origem da demanda

## g1583（1 列）
- 見出し：Data de encaminhamento apos triagem
- 例1 値：13/12/2021 | 13/12/2021 | 09/12/2021 | 13/12/2021 | 01/12/2021
  - 同じ表の列：No do ticket, Data de registro da…, Assunto, Etapa, Dias em tramitacao …, SLA, Canal de captacao, Origem da demanda

## g1584（1 列）
- 見出し：Assunto
- 例1 値：Descumprimento de Prazo | Dificuldade de Acesso | Irregularidade | Dificuldade de Acesso | Ato de Improbidade
  - 同じ表の列：No do ticket, Data de registro da…, Data de encaminhame…, Etapa, Dias em tramitacao …, SLA, Canal de captacao, Origem da demanda

## g1585（1 列）
- 見出し：Etapa
- 例1 値：Encerrado | Encerrado | Demandas encaminhadas aos órgãos, ainda… | Encerrado | Encerrado
  - 同じ表の列：No do ticket, Data de registro da…, Data de encaminhame…, Assunto, Dias em tramitacao …, SLA, Canal de captacao, Origem da demanda

## g1586（1 列）
- 見出し：Dias em tramitacao com a PBH
- 例1 値：7 | 88 | 3 | 28 | 4
  - 同じ表の列：No do ticket, Data de registro da…, Data de encaminhame…, Assunto, Etapa, SLA, Canal de captacao, Origem da demanda

## g1587（1 列）
- 見出し：SLA
- 例1 値：Atenção / attention | No prazo / onTime | No prazo / onTime | No prazo / onTime | Crítico / critical
  - 同じ表の列：No do ticket, Data de registro da…, Data de encaminhame…, Assunto, Etapa, Dias em tramitacao …, Canal de captacao, Origem da demanda

## g1588（1 列）
- 見出し：Canal de captacao
- 例1 値：Portal | Portal | Origem Interna | Telefônico | Portal
  - 同じ表の列：No do ticket, Data de registro da…, Data de encaminhame…, Assunto, Etapa, Dias em tramitacao …, SLA, Origem da demanda

## g1589（1 列）
- 見出し：Origem da demanda
- 例1 値：Ouvidor SUS | Ouvidor SUS | Ouvidor SUS | Ouvidor SUS | Ouvidor SUS
  - 同じ表の列：No do ticket, Data de registro da…, Data de encaminhame…, Assunto, Etapa, Dias em tramitacao …, SLA, Canal de captacao

## g1590（1 列）
- 見出し：Unidade de Destino
- 例1 値：PMBH > SMPOG / SUGESP PMBH > SMPOG / SU… | PMBH / SMASAC | PMBH / SMASAC | PMBH / SMFA | PMBH / SMFA
  - 同じ表の列：No do ticket, Data de registro da…, Data de encaminhame…, Assunto, Etapa, Dias em tramitacao …, SLA, Canal de captacao

## g1591（1 列）
- 見出し：ID_ESTACAO_HIDROMETEOROLOGICA
- 例1 値：61 | 36 | 4 | 3 | 7
  - 同じ表の列：CODIGO, ALTITUDE, TIPO_ESTACAO, GEOMETRIA

## g1592（1 列）
- 見出し：CODIGO
- 例1 値：27C | 43F | 1FP | 7FP | 22P
  - 同じ表の列：ID_ESTACAO_HIDROMET…, ALTITUDE, TIPO_ESTACAO, GEOMETRIA

## g1593（1 列）
- 見出し：ALTITUDE
- 例1 値：780.162 | 811.814 | 820.211 | 1165.19 | 884.493
  - 同じ表の列：ID_ESTACAO_HIDROMET…, CODIGO, TIPO_ESTACAO, GEOMETRIA

## g1594（1 列）
- 見出し：TIPO_ESTACAO
- 例1 値：Pluviométrica | Fluviométrica, Pluviométrica | Pluviométrica | Pluviométrica | Fluviométrica, Pluviométrica
  - 同じ表の列：ID_ESTACAO_HIDROMET…, CODIGO, ALTITUDE, GEOMETRIA

## g1595（1 列）
- 見出し：ID_UNIDADE_FPMZB
- 例1 値：344 | 366 | 365 | 385 | 331
  - 同じ表の列：IND_ABERTO_PUBLICO, LEGISLACAO, NUMERO, BAIRRO, GEOMETRIA

## g1596（1 列）
- 見出し：IND_ABERTO_PUBLICO
- 例1 値：SIM | SIM | SIM | SIM | SIM
  - 同じ表の列：ID_UNIDADE_FPMZB, LEGISLACAO, NUMERO, BAIRRO, GEOMETRIA

## g1597（1 列）
- 見出し：LEGISLACAO
- 例1 値：Lei Municipal n°. 8.511/2003 | Lei Municipal n°. 8.668/2003 | Lei Municipal n°. 9.328/2007 | Decreto Municipal no. 11.616/2004 e Lei… | Lei Municipal n°. 8.419/2002
  - 同じ表の列：ID_UNIDADE_FPMZB, IND_ABERTO_PUBLICO, NUMERO, BAIRRO, GEOMETRIA

## g1598（2 列）
- 見出し：NUMERO
- 例1 値：25 | 22 | 190 | 8001 | 1951
  - 同じ表の列：ID_UNIDADE_FPMZB, IND_ABERTO_PUBLICO, LEGISLACAO, BAIRRO, GEOMETRIA
- 例2 値：285 | 750 | 2280 | 225 | 6799
  - 同じ表の列：ID_EQ_ESP, TIPO, GEOMETRIA

## g1599（1 列）
- 見出し：BAIRRO
- 例1 値：Pousada Santo Antônio | Jardim Vitória | Estoril | Vila Clóris | Fernão Dias
  - 同じ表の列：ID_UNIDADE_FPMZB, IND_ABERTO_PUBLICO, LEGISLACAO, NUMERO, GEOMETRIA

## g1600（3 列）
- 見出し：GEOMETRIA
- 例1 値：MULTIPOLYGON (((615297.803688803 779873… | POLYGON ((606957.712176678 7808855.4311… | POLYGON ((604524.09965792 7800128.98734… | POLYGON ((603217.514187964 7803699.7020… | POLYGON ((613421.55530769 7803957.26811…
  - 同じ表の列：ID_UNIDADE_FPMZB, IND_ABERTO_PUBLICO, LEGISLACAO, NUMERO, BAIRRO
- 例2 値：POLYGON ((606914.249044918 7798217.5872… | MULTIPOLYGON (((612837.340746257 779956… | POLYGON ((616918.59136481 7808547.77031… | POLYGON ((615702.633993693 7800637.6813… | POLYGON ((606278.913233607 7807663.8422…
  - 同じ表の列：ID_SUBBAC, SUBBACIA, COD_BACIA, AREA_M2, PERIMETRO_M

## g1601（1 列）
- 見出し：GRUPO
- 例1 値：DESPESA | RECEITA | DESPESA | RECEITA | DESPESA
  - 同じ表の列：PREVISTO, REALIZADO

## g1602（1 列）
- 見出し：PREVISTO
- 例1 値：3.331.303,54 | 3.514.091,08 | 4.600.518,79 | 3.271,00 | 265.392,60
  - 同じ表の列：GRUPO, REALIZADO

## g1603（1 列）
- 見出し：REALIZADO
- 例1 値：5.608,48 | 7.039.325,84 | 1.156.821,19 | 0 | 2.744.715,11
  - 同じ表の列：GRUPO, PREVISTO

## g1604（3 列）
- 見出し：ID_BASE_TRECHO
- 例1 値：49334 | 65264 | 66126 | 44711 | 66165
  - 同じ表の列：ID_RDESG, LADO_RDESG, IND_RDESG, DATA, GEOMETRIA
- 例2 値：43211 | 65038 | 50051 | 30659 | 29956
  - 同じ表の列：ID_RDAGU, LADO_RDAGU, IND_RDAGU, DATA, GEOMETRIA

## g1605（1 列）
- 見出し：ID_RDESG
- 例1 値：150485 | 151239 | 159227 | 150463 | 146318
  - 同じ表の列：ID_BASE_TRECHO, LADO_RDESG, IND_RDESG, DATA, GEOMETRIA

## g1606（1 列）
- 見出し：LADO_RDESG
- 例1 値：A | A | A | A | A
  - 同じ表の列：ID_BASE_TRECHO, ID_RDESG, IND_RDESG, DATA, GEOMETRIA

## g1607（1 列）
- 見出し：IND_RDESG
- 例1 値：S | S | S | N | N
  - 同じ表の列：ID_BASE_TRECHO, ID_RDESG, LADO_RDESG, DATA, GEOMETRIA

## g1608（3 列）
- 見出し：DATA
- 例1 値：2019-12-19 00:00:00 | 2023-05-29 00:00:00 | 2018-11-23 00:00:00 | 2019-11-18 00:00:00 | 2019-11-19 00:00:00
  - 同じ表の列：ID_BASE_TRECHO, ID_RDESG, LADO_RDESG, IND_RDESG, GEOMETRIA
- 例2 値：2022-08-01 00:00:00 | 2018-11-22 00:00:00 | 2022-07-26 00:00:00 | 2026-08-04 08:32:47 | 2019-11-28 00:00:00
  - 同じ表の列：ID_BASE_TRECHO, ID_RDAGU, LADO_RDAGU, IND_RDAGU, GEOMETRIA

## g1609（1 列）
- 見出し：ID_RDAGU
- 例1 値：149395 | 146590 | 146592 | 149364 | 149367
  - 同じ表の列：ID_BASE_TRECHO, LADO_RDAGU, IND_RDAGU, DATA, GEOMETRIA

## g1610（1 列）
- 見出し：LADO_RDAGU
- 例1 値：A | A | A | A | A
  - 同じ表の列：ID_BASE_TRECHO, ID_RDAGU, IND_RDAGU, DATA, GEOMETRIA

## g1611（1 列）
- 見出し：IND_RDAGU
- 例1 値：S | S | S | S | N
  - 同じ表の列：ID_BASE_TRECHO, ID_RDAGU, LADO_RDAGU, DATA, GEOMETRIA

## g1612（1 列）
- 見出し：ID_PAV
- 例1 値：97864 | 62711 | 113682 | 113758 | 119276
  - 同じ表の列：ID_BASE_TRECHO, IND_PAV, LADO_PAV, TP_PAV, DATA, GEOMETRIA

## g1613（1 列）
- 見出し：IND_PAV
- 例1 値：Sim | Sim | Sim | Sim | Sim
  - 同じ表の列：ID_PAV, ID_BASE_TRECHO, LADO_PAV, TP_PAV, DATA, GEOMETRIA

## g1614（1 列）
- 見出し：LADO_PAV
- 例1 値：Ambos | Ambos | Ambos | Ambos | Ambos
  - 同じ表の列：ID_PAV, ID_BASE_TRECHO, IND_PAV, TP_PAV, DATA, GEOMETRIA

## g1615（1 列）
- 見出し：TP_PAV
- 例1 値：Cimento | Asfalto | Asfalto | Asfalto | Asfalto
  - 同じ表の列：ID_PAV, ID_BASE_TRECHO, IND_PAV, LADO_PAV, DATA, GEOMETRIA

## g1616（1 列）
- 見出し：Modalidade Licitatoria
- 例1 値：Pregão Eletrônico | Pregão Eletrônico | Pregão Eletrônico | Pregão Eletrônico | Pregão Eletrônico
  - 同じ表の列：Numero do Processo, Sigla do Orgao Dema…, Objeto, Data de abertura

## g1617（1 列）
- 見出し：Numero do Processo
- 例1 値：01.059068.21.10 | 01.064771.21.96 | 04.001131.21.72 | 04.001167.21.10. | 04.000928.21.99
  - 同じ表の列：Modalidade Licitato…, Sigla do Orgao Dema…, Objeto, Data de abertura

## g1618（1 列）
- 見出し：Sigla do Orgao Demandante
- 例1 値：SMASAC | SMPOG | SMED | SMFA | SMASAC
  - 同じ表の列：Modalidade Licitato…, Numero do Processo, Objeto, Data de abertura

## g1619（1 列）
- 見出し：Objeto
- 例1 値：Prestação de serviço de acompanhamento … | Registro de preços para aquisições e en… | Registro de Preços para aquisição de fo… | Alienação de imóveis do Município de Be… | Aquisição de produtos hortifrutigranjei…
  - 同じ表の列：Modalidade Licitato…, Numero do Processo, Sigla do Orgao Dema…, Data de abertura

## g1620（1 列）
- 見出し：Data de abertura
- 例1 値：11.11.2021 | 17.11.2021 | 19.11.2021 | 12.11.2021 | 18.11.2021
  - 同じ表の列：Modalidade Licitato…, Numero do Processo, Sigla do Orgao Dema…, Objeto

## g1621（1 列）
- 見出し：Funcao_ou_Atividade_Exercida
- 例1 値：PORTEIRO_VIGIA | AUXILIAR_DE_COZINHA | AUXILIAR_ADMINISTRATIVO | PORTEIRO_VIGIA | TEC_EM_EDIFICACAO
  - 同じ表の列：Orgao

## g1622（1 列）
- 見出し：Orgao
- 例1 値：FMAS | FMAS | SMFA | EGM_SMFA | SMPOG
  - 同じ表の列：Funcao_ou_Atividade…

## g1623（1 列）
- 見出し：Setor_Tipo_de_Veiculo
- 例1 値：SMSA_GEURE | GP | SMSA_DRES_O | FPMZB | SMMA
  - 同じ表の列：FURGAO_DE_CARGA, MICRO_ONIBUS, MOTOCICLETA_TIPO_02, PA_CARREGADEIRA, PESADO, PICAPE_TIPO_01, PICAPE_TIPO_02, SERVICO_TIPO_01

## g1624（1 列）
- 見出し：FURGAO_DE_CARGA
- 例1 値：4 | 1 | 3 | 1 | 3
  - 同じ表の列：Setor_Tipo_de_Veicu…, MICRO_ONIBUS, MOTOCICLETA_TIPO_02, PA_CARREGADEIRA, PESADO, PICAPE_TIPO_01, PICAPE_TIPO_02, SERVICO_TIPO_01

## g1625（1 列）
- 見出し：MICRO_ONIBUS
- 例1 値：1 | 1
  - 同じ表の列：Setor_Tipo_de_Veicu…, FURGAO_DE_CARGA, MOTOCICLETA_TIPO_02, PA_CARREGADEIRA, PESADO, PICAPE_TIPO_01, PICAPE_TIPO_02, SERVICO_TIPO_01

## g1626（1 列）
- 見出し：MOTOCICLETA_TIPO_02
- 例1 値：3 | 1 | 1 | 18 | 2
  - 同じ表の列：Setor_Tipo_de_Veicu…, FURGAO_DE_CARGA, MICRO_ONIBUS, PA_CARREGADEIRA, PESADO, PICAPE_TIPO_01, PICAPE_TIPO_02, SERVICO_TIPO_01

## g1627（1 列）
- 見出し：PA_CARREGADEIRA
- 例1 値：3
  - 同じ表の列：Setor_Tipo_de_Veicu…, FURGAO_DE_CARGA, MICRO_ONIBUS, MOTOCICLETA_TIPO_02, PESADO, PICAPE_TIPO_01, PICAPE_TIPO_02, SERVICO_TIPO_01

## g1628（1 列）
- 見出し：PESADO
- 例1 値：3 | 12 | 2 | 10 | 2
  - 同じ表の列：Setor_Tipo_de_Veicu…, FURGAO_DE_CARGA, MICRO_ONIBUS, MOTOCICLETA_TIPO_02, PA_CARREGADEIRA, PICAPE_TIPO_01, PICAPE_TIPO_02, SERVICO_TIPO_01

## g1629（1 列）
- 見出し：PICAPE_TIPO_01
- 例1 値：1 | 1 | 1 | 39 | 1
  - 同じ表の列：Setor_Tipo_de_Veicu…, FURGAO_DE_CARGA, MICRO_ONIBUS, MOTOCICLETA_TIPO_02, PA_CARREGADEIRA, PESADO, PICAPE_TIPO_02, SERVICO_TIPO_01

## g1630（1 列）
- 見出し：PICAPE_TIPO_02
- 例1 値：3 | 2 | 6 | 1 | 1
  - 同じ表の列：Setor_Tipo_de_Veicu…, FURGAO_DE_CARGA, MICRO_ONIBUS, MOTOCICLETA_TIPO_02, PA_CARREGADEIRA, PESADO, PICAPE_TIPO_01, SERVICO_TIPO_01

## g1631（1 列）
- 見出し：SERVICO_TIPO_01
- 例1 値：5 | 5 | 1 | 3 | 1
  - 同じ表の列：Setor_Tipo_de_Veicu…, FURGAO_DE_CARGA, MICRO_ONIBUS, MOTOCICLETA_TIPO_02, PA_CARREGADEIRA, PESADO, PICAPE_TIPO_01, PICAPE_TIPO_02

## g1632（1 列）
- 見出し：SERVICO_TIPO_02_A
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：Setor_Tipo_de_Veicu…, FURGAO_DE_CARGA, MICRO_ONIBUS, MOTOCICLETA_TIPO_02, PA_CARREGADEIRA, PESADO, PICAPE_TIPO_01, PICAPE_TIPO_02

## g1633（2 列）
- 見出し：ID_TERRITORIO_PROTECAO
- 例1 値：80 | 92 | 155 | 144 | 122
  - 同じ表の列：TIPO_TERRITORIO, GEOMETRIA
- 例2 値：129 | 53 | 95 | 50 | 119
  - 同じ表の列：TIPO_TERRITORIO, GEOMETRIA

## g1634（2 列）
- 見出し：TIPO_TERRITORIO
- 例1 値：SPSBR | SPSBR | SPSBR | SPSBR | SPSBR
  - 同じ表の列：ID_TERRITORIO_PROTE…, GEOMETRIA
- 例2 値：CRAS | CRAS | CRAS | CRAS | CRAS
  - 同じ表の列：ID_TERRITORIO_PROTE…, GEOMETRIA

## g1635（9 列）
- 見出し：GEOMETRIA
- 例1 値：POLYGON ((606466.11 7796691.72, 606462.… | POLYGON ((610301.34 7792489.55, 610299.… | POLYGON ((605941.16 7802139.60, 605930.… | POLYGON ((605332.18 7797738.78, 605331.… | POLYGON ((614432.51 7796304.14, 614427.…
  - 同じ表の列：ID_TERRITORIO_PROTE…, TIPO_TERRITORIO
- 例2 値：POLYGON ((606568.203229669 7799326.7506… | POLYGON ((605980.431202408 7788611.9216… | POLYGON ((610840.193750837 7802801.0134… | POLYGON ((614981.330968872 7794930.1255… | POLYGON ((605703.436800818 7809784.3720…
  - 同じ表の列：ID_TERRITORIO_PROTE…, TIPO_TERRITORIO

## g1636（1 列）
- 見出し：ID_EQUIPAMENTO_CIDADANIA
- 例1 値：13 | 8 | 12 | 2 | 11
  - 同じ表の列：NUMERO_IMOVEL, DIAS_FUNCIONAMENTO, HORARIO_FUNCIONAMEN…, GEOMETRIA

## g1637（2 列）
- 見出し：NUMERO_IMOVEL
- 例1 値：481 | 50 | 382 | 189 | 142
  - 同じ表の列：ID_EQUIPAMENTO_CIDA…, DIAS_FUNCIONAMENTO, HORARIO_FUNCIONAMEN…, GEOMETRIA
- 例2 値：481 | 58 | 580 | 50 | 255
  - 同じ表の列：ID_EQ_SAUDE, CATEGORIA, SIGLA_CATEGORIA, GEOMETRIA

## g1638（1 列）
- 見出し：DIAS_FUNCIONAMENTO
- 例1 値：Segunda à sexta | Segunda à sexta | Sexta-feira | Segunda à sexta | Segunda à sexta
  - 同じ表の列：ID_EQUIPAMENTO_CIDA…, NUMERO_IMOVEL, HORARIO_FUNCIONAMEN…, GEOMETRIA

## g1639（1 列）
- 見出し：HORARIO_FUNCIONAMENTO
- 例1 値：09h às 17h | 09h às 17h | 09h às 17h | 09h às 17h | 08h às 18h
  - 同じ表の列：ID_EQUIPAMENTO_CIDA…, NUMERO_IMOVEL, DIAS_FUNCIONAMENTO, GEOMETRIA

## g1640（1 列）
- 見出し：DATA
- 例1 値：18/09/2026 | 16/09/2026 | 17/08/2026 | 28/08/2026 | 13/08/2026
  - 同じ表の列：IDENTIFICACAO, OCUPACAO, LOCAL DE TRABALHO, NUMERO DE VAGAS, EXPERIENCIA, ESCOLARIDADE, REMUNERACAO

## g1641（1 列）
- 見出し：IDENTIFICACAO
- 例1 値：9264592 | 9124555 | 9237630 | 9175701 | 9256630
  - 同じ表の列：DATA, OCUPACAO, LOCAL DE TRABALHO, NUMERO DE VAGAS, EXPERIENCIA, ESCOLARIDADE, REMUNERACAO

## g1642（1 列）
- 見出し：OCUPACAO
- 例1 値：Auxiliar de limpeza* (Unidade Belvedere) | Auxiliar de manutenção predial* (Artífi… | Montador de máquinas (Ajudante de monta… | Auxiliar de limpeza* | Operador de vendas (lojas)
  - 同じ表の列：DATA, IDENTIFICACAO, LOCAL DE TRABALHO, NUMERO DE VAGAS, EXPERIENCIA, ESCOLARIDADE, REMUNERACAO

## g1643（1 列）
- 見出し：LOCAL DE TRABALHO
- 例1 値：Diversas localidades | Sion/BH | Cinquentenário/BH | Não fixo | Brumadinho/MG
  - 同じ表の列：DATA, IDENTIFICACAO, OCUPACAO, NUMERO DE VAGAS, EXPERIENCIA, ESCOLARIDADE, REMUNERACAO

## g1644（2 列）
- 見出し：NUMERO DE VAGAS
- 例1 値：4 | 5 | 1 | 30 | 4
  - 同じ表の列：DATA, IDENTIFICACAO, OCUPACAO, LOCAL DE TRABALHO, EXPERIENCIA, ESCOLARIDADE, REMUNERACAO
- 例2 値：21 | 17 | 17 | 30 | 30
  - 同じ表の列：Data, Local realizacao, Turno, Carga horaria, A Requisitos

## g1645（1 列）
- 見出し：EXPERIENCIA
- 例1 値：6 meses | 6 meses | - | - | 6 meses
  - 同じ表の列：DATA, IDENTIFICACAO, OCUPACAO, LOCAL DE TRABALHO, NUMERO DE VAGAS, ESCOLARIDADE, REMUNERACAO

## g1646（1 列）
- 見出し：ESCOLARIDADE
- 例1 値：Ensino Médio completo | Não exigida | Ensino Fundamental incompleto | Ensino Médio completo | Ensino Fundamental completo
  - 同じ表の列：DATA, IDENTIFICACAO, OCUPACAO, LOCAL DE TRABALHO, NUMERO DE VAGAS, EXPERIENCIA, REMUNERACAO

## g1647（1 列）
- 見出し：REMUNERACAO
- 例1 値：R$ 1.910,22 + benefícios | R$ 1.697,00 + benefícios | A combinar | R$ 1.836,79 + benefícios | R$ 1.772,80
  - 同じ表の列：DATA, IDENTIFICACAO, OCUPACAO, LOCAL DE TRABALHO, NUMERO DE VAGAS, EXPERIENCIA, ESCOLARIDADE

## g1648（1 列）
- 見出し：Data
- 例1 値：03/05/2021 a 23/06/2021 | 03/02/2020 a 16/03/2020 | 03/05/2021 a 23/06/2021 | 27/01/2020 a 16/03/2020 | 27/01/2020 a 19/02/2020
  - 同じ表の列：Local realizacao, Numero de vagas, Turno, Carga horaria, A Requisitos

## g1649（1 列）
- 見出し：Local realizacao
- 例1 値：Escola Profissionalizante Raimunda da S… | Plataforma EAD PBH PRODABEL | Escola Profissionalizante Raimunda da S… | Escola Profissionalizante Raimunda da S… | Plataforma EAD PBH PRODABEL
  - 同じ表の列：Data, Numero de vagas, Turno, Carga horaria, A Requisitos

## g1650（1 列）
- 見出し：Turno
- 例1 値：Noite | Tarde | Manha | Tarde | Tarde
  - 同じ表の列：Data, Local realizacao, Numero de vagas, Carga horaria, A Requisitos

## g1651（1 列）
- 見出し：Carga horaria
- 例1 値：64 horas | 60 horas | 64 horas | 100 horas | 64 horas
  - 同じ表の列：Data, Local realizacao, Numero de vagas, Turno, A Requisitos

## g1652（1 列）
- 見出し：A Requisitos
- 例1 値：ENSINO FUNDAMENTAL INCOMPLETO, IDADE MI… | ENSINO FUNDAMENTAL INCOMPLETO, IDADE MI… | ENSINO FUNDAMENTAL II COMPLETO. IDADE M… | ENSINO FUNDAMENTAL II COMPLETO. IDADE M… | ENSINO FUNDAMENTAL INCOMPLETO,IDADE MIN…
  - 同じ表の列：Data, Local realizacao, Numero de vagas, Turno, Carga horaria

## g1653（1 列）
- 見出し：ID_EQUIP_EDUCACAO
- 例1 値：1981844.0 | 1981864.0 | 1982043.0 | 1981816.0 | 1982518.0
  - 同じ表の列：DEPENDENCIA_ADM, CODIGO_INEP, NUMERO, BAIRRO, REGIONAL, GEOMETRIA

## g1654（1 列）
- 見出し：DEPENDENCIA_ADM
- 例1 値：Creches Conveniadas | Creches Conveniadas | EMEIS | Municipal | EMEIS
  - 同じ表の列：ID_EQUIP_EDUCACAO, CODIGO_INEP, NUMERO, BAIRRO, REGIONAL, GEOMETRIA

## g1655（1 列）
- 見出し：CODIGO_INEP
- 例1 値：31373486 | 31219231 | 31358614 | 31003328 | 31362107
  - 同じ表の列：ID_EQUIP_EDUCACAO, DEPENDENCIA_ADM, NUMERO, BAIRRO, REGIONAL, GEOMETRIA

## g1656（2 列）
- 見出し：NUMERO
- 例1 値：1200.0 | 56.0 | 170.0 | 65.0 | 128.0
  - 同じ表の列：ID_EQUIP_EDUCACAO, DEPENDENCIA_ADM, CODIGO_INEP, BAIRRO, REGIONAL, GEOMETRIA
- 例2 値：550.0 | 1569.0 | 665.0 | 50.0 | 130.0
  - 同じ表の列：ID_EQ_ESP, TIPO, GEOMETRIA, STATUS

## g1657（1 列）
- 見出し：BAIRRO
- 例1 値：Flávio de Oliveira | Vitória | Novo Aarão Reis | Vista Alegre | Inconfidência
  - 同じ表の列：ID_EQUIP_EDUCACAO, DEPENDENCIA_ADM, CODIGO_INEP, NUMERO, REGIONAL, GEOMETRIA

## g1658（3 列）
- 見出し：REGIONAL
- 例1 値：BARREIRO | PAMPULHA | BARREIRO | CENTRO-SUL | PAMPULHA
  - 同じ表の列：ID_EQUIP_EDUCACAO, DEPENDENCIA_ADM, CODIGO_INEP, NUMERO, BAIRRO, GEOMETRIA
- 例2 値：PAMPULHA | OESTE | LESTE | CENTRO-SUL | NORTE
  - 同じ表の列：ID_UNIDADE_ILUMINAC…, NUMERO_IDENTIFICACAO, ILUMINACAO_DESTAQUE, OBJETO_ILUMINADO, PONTO_MODERNIZADO_L…, TELEGESTAO, BAIRRO, GEOMETRIA

## g1659（1 列）
- 見出し：ID_JUREF
- 例1 値：2209 | 2088 | 2158 | 2096 | 2224
  - 同じ表の列：COD_JURISDICAO, REGIONAL, GEOMETRIA

## g1660（2 列）
- 見出し：COD_JURISDICAO
- 例1 値：518 | 562 | 585 | 622 | 586
  - 同じ表の列：ID_JUREF, REGIONAL, GEOMETRIA
- 例2 値：313 | 615 | 403 | 802 | 210
  - 同じ表の列：ID_JURCR, REGIONAL, GEOMETRIA

## g1661（2 列）
- 見出し：REGIONAL
- 例1 値：BARREIRO | OESTE | PAMPULHA | OESTE | NORDESTE
  - 同じ表の列：ID_JUREF, COD_JURISDICAO, GEOMETRIA
- 例2 値：Norte | Diversos | Barreiro | Leste | Nordeste
  - 同じ表の列：ID_AREA_EMPREENDIME…, NUMERO_PO, TEMATICA, STATUS, GEOMETRIA

## g1662（1 列）
- 見出し：ID_JURCR
- 例1 値：2976 | 2961 | 2876 | 2805 | 2910
  - 同じ表の列：COD_JURISDICAO, REGIONAL, GEOMETRIA

## g1663（2 列）
- 見出し：REGIONAL
- 例1 値：NORDESTE | CENTRO-SUL | BARREIRO | VENDA NOVA | VENDA NOVA
  - 同じ表の列：ID_JURCR, COD_JURISDICAO, GEOMETRIA
- 例2 値：Leste | Venda Nova | Centro-Sul | Venda Nova | Centro-Sul
  - 同じ表の列：COD_VISTORIA, DATA_EXECUCAO_VISTO…, NIVEL_RISCO

## g1664（2 列）
- 見出し：ID_EQ_ESP
- 例1 値：1486 | 1892 | 1318 | 1279 | 1483
  - 同じ表の列：TIPO, NUMERO, GEOMETRIA, STATUS
- 例2 値：1379 | 1456 | 1685 | 1501 | 1964
  - 同じ表の列：TIPO, NUMERO, GEOMETRIA

## g1665（1 列）
- 見出し：TIPO
- 例1 値：QUADRA POLIESPORTIVA | QUADRA DE PETECA | QUADRA DE FUTSAL | ACADEMIA A CÉU ABERTO | QUADRA POLIESPORTIVA
  - 同じ表の列：ID_EQ_ESP, NUMERO, GEOMETRIA, STATUS

## g1666（1 列）
- 見出し：TIPO
- 例1 値：CAMPO DE FUTEBOL | ACADEMIA A CÉU ABERTO | ACADEMIA A CÉU ABERTO | ACADEMIA A CÉU ABERTO | CAMPO DE FUTEBOL
  - 同じ表の列：ID_EQ_ESP, NUMERO, GEOMETRIA

## g1667（1 列）
- 見出し：GEOMETRIA
- 例1 値：POINT (605854.613820906 7807993.8050613… | POINT (613446.48 7803943.82) | POINT (613795 7795949) | POINT (605668.956617142 7789754.6149687… | POINT (608780.80928515 7806779.15580819)
  - 同じ表の列：ID_EQ_ESP, TIPO, NUMERO

## g1668（1 列）
- 見出し：DT_MOVIMENTO
- 例1 値：2026-01-06T00:00:00 | 2026-01-05T00:00:00 | 2026-01-06T00:00:00 | 2026-01-06T00:00:00 | 2026-01-05T00:00:00
  - 同じ表の列：UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO

## g1669（1 列）
- 見出し：UNIDADE_ORCAMENTARIA
- 例1 値：2302 - FUNDO MUNICIPAL DE SAÚDE | 2302 - FUNDO MUNICIPAL DE SAÚDE | 2302 - FUNDO MUNICIPAL DE SAÚDE | 2700 - SECRETARIA MUNICIPAL DE OBRAS E … | 2302 - FUNDO MUNICIPAL DE SAÚDE
  - 同じ表の列：DT_MOVIMENTO, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO

## g1670（1 列）
- 見出し：FUNCAO
- 例1 値：08 - ASSISTÊNCIA SOCIAL | 26 - TRANSPORTE | 10 - SAÚDE | 10 - SAÚDE | 10 - SAÚDE
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, SUBFUNCAO, PROGRAMA, ACAO, SUBACAO

## g1671（1 列）
- 見出し：SUBFUNCAO
- 例1 値：302 - ASSISTÊNCIA HOSPITALAR E AMBULATO… | 451 - INFRA-ESTRUTURA URBANA | 302 - ASSISTÊNCIA HOSPITALAR E AMBULATO… | 244 - ASSISTÊNCIA COMUNITÁRIA | 302 - ASSISTÊNCIA HOSPITALAR E AMBULATO…
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, PROGRAMA, ACAO, SUBACAO

## g1672（1 列）
- 見出し：PROGRAMA
- 例1 値：030 - ATENDIMENTO AMBULATORIAL, EMERGEN… | 117 - GESTÃO DO SUS | 308 - BH CIDADE SUSTENTÁVEL: MOBILIZAR,… | 225 - INTERVENÇÃO EM ASSENTAMENTOS DE I… | 114 - ATENÇÃO SECUNDÁRIA E TERCIÁRIA À …
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, ACAO, SUBACAO

## g1673（1 列）
- 見出し：ACAO
- 例1 値：2405 - Benefícios, Transferência de Ren… | 2875 - Gestão da Assistência à Saúde | 2936 - REDE ESPECIALIZADA, REDE DE URGÊ… | 2829 - Vigilância em Saúde | 2620 - Gestão de Apoio à Assistência
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, SUBACAO

## g1674（1 列）
- 見出し：SUBACAO
- 例1 値：001 - Gestão da Política de Transporte … | 001 - Melhoria dos Processos de Suporte… | 002 - Benefícios Eventuais | 002 - Campanha de Divulgação Institucio… | 004 - ATENDIMENTO DA POPULAÇÃO NA REDE …
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO

## g1675（1 列）
- 見出し：CATEGORIA_ECONOMICA
- 例1 値：3 - Despesas Correntes | 3 - Despesas Correntes | 3 - Despesas Correntes | 3 - Despesas Correntes | 4 - Despesas de Capital
  - 同じ表の列：DT_MOVIMENTO, UNIDADE_ORCAMENTARIA, NUMERO_EMPENHO, CLASSIFICACAO_ORCAM…, FUNCAO, SUBFUNCAO, PROGRAMA, ACAO

## g1676（1 列）
- 見出し：entidade
- 例1 値：201 | 201 | 201 | 201 | 216
  - 同じ表の列：data_lancamento, receita, receita_classificac…, receita_detalhe, numero_documento, nro_docto_classific…, vl_documento

## g1677（1 列）
- 見出し：data_lancamento
- 例1 値：02/01/2026 00:00 | 02/01/2026 00:00 | 02/01/2026 00:00 | 05/01/2026 00:00 | 02/01/2026 00:00
  - 同じ表の列：entidade, receita, receita_classificac…, receita_detalhe, numero_documento, nro_docto_classific…, vl_documento

## g1678（1 列）
- 見出し：receita
- 例1 値：11125007 | 11130341 | 16110103 | 11220105 | 11210103
  - 同じ表の列：entidade, data_lancamento, receita_classificac…, receita_detalhe, numero_documento, nro_docto_classific…, vl_documento

## g1679（1 列）
- 見出し：receita_classificacao
- 例1 値：100006 | 100006 | 374028 | 370033 | 100016
  - 同じ表の列：entidade, data_lancamento, receita, receita_detalhe, numero_documento, nro_docto_classific…, vl_documento

## g1680（1 列）
- 見出し：receita_detalhe
- 例1 値：505 | 3 | 1 | 15 | 507
  - 同じ表の列：entidade, data_lancamento, receita, receita_classificac…, numero_documento, nro_docto_classific…, vl_documento

## 答えの雛形

```
g1561	
g1562	
g1563	
g1564	
g1565	
g1566	
g1567	
g1568	
g1569	
g1570	
g1571	
g1572	
g1573	
g1574	
g1575	
g1576	
g1577	
g1578	
g1579	
g1580	
g1581	
g1582	
g1583	
g1584	
g1585	
g1586	
g1587	
g1588	
g1589	
g1590	
g1591	
g1592	
g1593	
g1594	
g1595	
g1596	
g1597	
g1598	
g1599	
g1600	
g1601	
g1602	
g1603	
g1604	
g1605	
g1606	
g1607	
g1608	
g1609	
g1610	
g1611	
g1612	
g1613	
g1614	
g1615	
g1616	
g1617	
g1618	
g1619	
g1620	
g1621	
g1622	
g1623	
g1624	
g1625	
g1626	
g1627	
g1628	
g1629	
g1630	
g1631	
g1632	
g1633	
g1634	
g1635	
g1636	
g1637	
g1638	
g1639	
g1640	
g1641	
g1642	
g1643	
g1644	
g1645	
g1646	
g1647	
g1648	
g1649	
g1650	
g1651	
g1652	
g1653	
g1654	
g1655	
g1656	
g1657	
g1658	
g1659	
g1660	
g1661	
g1662	
g1663	
g1664	
g1665	
g1666	
g1667	
g1668	
g1669	
g1670	
g1671	
g1672	
g1673	
g1674	
g1675	
g1676	
g1677	
g1678	
g1679	
g1680	
```
