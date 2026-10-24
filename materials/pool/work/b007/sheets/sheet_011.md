# ラベル用シート 011 / 019

- LABEL_GUIDE v1.8 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_011.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g1201（1 列）
- 見出し：ID_SETOR_CENSITARIO_2010
- 例1 値：3350 | 4142 | 3987 | 5708 | 3434
  - 同じ表の列：ID_IVS, POPULACAO_TOTAL, POPFEM, POPMASC, IVS_2012, COD_SETOR_CENSITARI…, GEOMETRIA

## g1202（1 列）
- 見出し：ID_ROTA_CICLOVIARIA
- 例1 値：14825 | 11292 | 13286 | 14365 | 11330
  - 同じ表の列：COD_ROTA_CICLOVIARIA, ID_TRECHO, ANO_MES_IMPLANTACAO, TIPO_ROTA_CICLOVIAR…, EXTENSAO_CICLOVIA, SITUACAO_ROTA, SENTIDO_CIRCULACAO, GEOMETRIA

## g1203（1 列）
- 見出し：COD_ROTA_CICLOVIARIA
- 例1 値：5.PA | 4.AV | 6.VI | 5.PR | 3.OM
  - 同じ表の列：ID_ROTA_CICLOVIARIA, ID_TRECHO, ANO_MES_IMPLANTACAO, TIPO_ROTA_CICLOVIAR…, EXTENSAO_CICLOVIA, SITUACAO_ROTA, SENTIDO_CIRCULACAO, GEOMETRIA

## g1204（1 列）
- 見出し：ID_TRECHO
- 例1 値：40270 | 4566 | 33651 | 34905 | 212
  - 同じ表の列：ID_ROTA_CICLOVIARIA, COD_ROTA_CICLOVIARIA, ANO_MES_IMPLANTACAO, TIPO_ROTA_CICLOVIAR…, EXTENSAO_CICLOVIA, SITUACAO_ROTA, SENTIDO_CIRCULACAO, GEOMETRIA

## g1205（1 列）
- 見出し：ANO_MES_IMPLANTACAO
- 例1 値：2012/01 | 2016/02 | 2013/04 | 2012/07 | 2009
  - 同じ表の列：ID_ROTA_CICLOVIARIA, COD_ROTA_CICLOVIARIA, ID_TRECHO, TIPO_ROTA_CICLOVIAR…, EXTENSAO_CICLOVIA, SITUACAO_ROTA, SENTIDO_CIRCULACAO, GEOMETRIA

## g1206（1 列）
- 見出し：TIPO_ROTA_CICLOVIARIA
- 例1 値：CICLOFAIXA | CICLOVIA | CICLOFAIXA | CICLOVIA | CICLOVIA
  - 同じ表の列：ID_ROTA_CICLOVIARIA, COD_ROTA_CICLOVIARIA, ID_TRECHO, ANO_MES_IMPLANTACAO, EXTENSAO_CICLOVIA, SITUACAO_ROTA, SENTIDO_CIRCULACAO, GEOMETRIA

## g1207（1 列）
- 見出し：EXTENSAO_CICLOVIA
- 例1 値：146.894254197138 | 42.1346561755727 | 63.9061537681968 | 20.1694537327104 | 14.0903986465086
  - 同じ表の列：ID_ROTA_CICLOVIARIA, COD_ROTA_CICLOVIARIA, ID_TRECHO, ANO_MES_IMPLANTACAO, TIPO_ROTA_CICLOVIAR…, SITUACAO_ROTA, SENTIDO_CIRCULACAO, GEOMETRIA

## g1208（1 列）
- 見出し：SITUACAO_ROTA
- 例1 値：IMPLANTADA | IMPLANTADA | IMPLANTADA | IMPLANTADA | IMPLANTADA
  - 同じ表の列：ID_ROTA_CICLOVIARIA, COD_ROTA_CICLOVIARIA, ID_TRECHO, ANO_MES_IMPLANTACAO, TIPO_ROTA_CICLOVIAR…, EXTENSAO_CICLOVIA, SENTIDO_CIRCULACAO, GEOMETRIA

## g1209（1 列）
- 見出し：SENTIDO_CIRCULACAO
- 例1 値：BIDIRECIONAL | BIDIRECIONAL | BIDIRECIONAL | BIDIRECIONAL | BIDIRECIONAL
  - 同じ表の列：ID_ROTA_CICLOVIARIA, COD_ROTA_CICLOVIARIA, ID_TRECHO, ANO_MES_IMPLANTACAO, TIPO_ROTA_CICLOVIAR…, EXTENSAO_CICLOVIA, SITUACAO_ROTA, GEOMETRIA

## g1210（1 列）
- 見出し：ID_PONTO_ONIBUS_LINHA
- 例1 値：34232 | 41900 | 34857 | 34820 | 34349
  - 同じ表の列：COD_LINHA, ORIGEM, IDENTIFICADOR_PONTO…, GEOMETRIA

## g1211（1 列）
- 見出し：COD_LINHA
- 例1 値：8205 | 8205 | 8205 | 8205 | 8205
  - 同じ表の列：ID_PONTO_ONIBUS_LIN…, ORIGEM, IDENTIFICADOR_PONTO…, GEOMETRIA

## g1212（1 列）
- 見出し：ORIGEM
- 例1 値：SANTO ANDRE | NOVA GRANADA | MARIA GORETTI | SANTO ANDRE | NOVA GRANADA
  - 同じ表の列：ID_PONTO_ONIBUS_LIN…, COD_LINHA, IDENTIFICADOR_PONTO…, GEOMETRIA

## g1213（1 列）
- 見出し：IDENTIFICADOR_PONTO_ONIBUS
- 例1 値：460701 | 374784 | 330894 | 374665 | 930365
  - 同じ表の列：ID_PONTO_ONIBUS_LIN…, COD_LINHA, ORIGEM, GEOMETRIA

## g1214（1 列）
- 見出し：ID_ESTPB
- 例1 値：7 | 9 | 45 | 82 | 6
  - 同じ表の列：TIPO, CORREDOR_MOVE, EIXO_MOVE, SISTEMA_TRONCAL, INTEGRACAO_FISICA_M…, SITUACAO, GESTOR, GEOMETRIA

## g1215（1 列）
- 見出し：TIPO
- 例1 値：TRANSFERENCIA MOVE | TRANSFERENCIA MOVE | TRANSFERENCIA MOVE | TRANSFERENCIA MOVE | TRANSFERENCIA MOVE
  - 同じ表の列：ID_ESTPB, CORREDOR_MOVE, EIXO_MOVE, SISTEMA_TRONCAL, INTEGRACAO_FISICA_M…, SITUACAO, GESTOR, GEOMETRIA

## g1216（1 列）
- 見出し：CORREDOR_MOVE
- 例1 値：SANTOS DUMONT | ANTONIO CARLOS | PARANA | DOM PEDRO I | ANTONIO CARLOS
  - 同じ表の列：ID_ESTPB, TIPO, EIXO_MOVE, SISTEMA_TRONCAL, INTEGRACAO_FISICA_M…, SITUACAO, GESTOR, GEOMETRIA

## g1217（1 列）
- 見出し：EIXO_MOVE
- 例1 値：ANTONIO CARLOS | CRISTIANO MACHADO | ANTONIO CARLOS | ANTONIO CARLOS | ROTOR CENTRAL
  - 同じ表の列：ID_ESTPB, TIPO, CORREDOR_MOVE, SISTEMA_TRONCAL, INTEGRACAO_FISICA_M…, SITUACAO, GESTOR, GEOMETRIA

## g1218（1 列）
- 見出し：SISTEMA_TRONCAL
- 例1 値：MOVE | MOVE | MOVE | MOVE | MOVE
  - 同じ表の列：ID_ESTPB, TIPO, CORREDOR_MOVE, EIXO_MOVE, INTEGRACAO_FISICA_M…, SITUACAO, GESTOR, GEOMETRIA

## g1219（1 列）
- 見出し：INTEGRACAO_FISICA_METRO
- 例1 値：NAO | SIM | NAO | NAO | NAO
  - 同じ表の列：ID_ESTPB, TIPO, CORREDOR_MOVE, EIXO_MOVE, SISTEMA_TRONCAL, SITUACAO, GESTOR, GEOMETRIA

## g1220（1 列）
- 見出し：SITUACAO
- 例1 値：EM OPERACAO | EM OPERACAO | EM OPERACAO | EM OPERACAO | EM OPERACAO
  - 同じ表の列：ID_ESTPB, TIPO, CORREDOR_MOVE, EIXO_MOVE, SISTEMA_TRONCAL, INTEGRACAO_FISICA_M…, GESTOR, GEOMETRIA

## g1221（1 列）
- 見出し：GESTOR
- 例1 値：BHBUS/MOVE: BHTRANS - SETOP/METROPOLITA… | SETOP | BHTRANS | BHBUS/MOVE: BHTRANS - SETOP/METROPOLITA… | BHBUS/MOVE: BHTRANS - SETOP/METROPOLITA…
  - 同じ表の列：ID_ESTPB, TIPO, CORREDOR_MOVE, EIXO_MOVE, SISTEMA_TRONCAL, INTEGRACAO_FISICA_M…, SITUACAO, GEOMETRIA

## g1222（1 列）
- 見出し：ID_AREAS_PRIORITARIAS_SBN_2022
- 例1 値：47 | 249 | 726 | 470 | 490
  - 同じ表の列：AREA_M2, EXP_ALAG, EXP_DESL, EXP_INUN, EXP_ONDA, VUL_ALAG, VUL_DESL, VUL_INUN

## g1223（1 列）
- 見出し：EXP_ALAG
- 例1 値：1.25 | 0.0 | 0.3 | 1.25 | 1.55
  - 同じ表の列：ID_AREAS_PRIORITARI…, AREA_M2, EXP_DESL, EXP_INUN, EXP_ONDA, VUL_ALAG, VUL_DESL, VUL_INUN

## g1224（1 列）
- 見出し：EXP_DESL
- 例1 値：0.0 | 0.0 | 0.67 | 0.0 | 0.0
  - 同じ表の列：ID_AREAS_PRIORITARI…, AREA_M2, EXP_ALAG, EXP_INUN, EXP_ONDA, VUL_ALAG, VUL_DESL, VUL_INUN

## g1225（1 列）
- 見出し：EXP_INUN
- 例1 値：0.0 | 0.0 | 0.0 | 0.0 | 0.55
  - 同じ表の列：ID_AREAS_PRIORITARI…, AREA_M2, EXP_ALAG, EXP_DESL, EXP_ONDA, VUL_ALAG, VUL_DESL, VUL_INUN

## g1226（1 列）
- 見出し：EXP_ONDA
- 例1 値：1.6 | 3.0 | 3.75 | 3.0 | 2.85
  - 同じ表の列：ID_AREAS_PRIORITARI…, AREA_M2, EXP_ALAG, EXP_DESL, EXP_INUN, VUL_ALAG, VUL_DESL, VUL_INUN

## g1227（1 列）
- 見出し：VUL_ALAG
- 例1 値：3.0 | 0.5 | 1.85 | 2.55 | 0.05
  - 同じ表の列：ID_AREAS_PRIORITARI…, AREA_M2, EXP_ALAG, EXP_DESL, EXP_INUN, EXP_ONDA, VUL_DESL, VUL_INUN

## g1228（1 列）
- 見出し：VUL_DESL
- 例1 値：0.0 | 1.4 | 3.75 | 1.95 | 3.35
  - 同じ表の列：ID_AREAS_PRIORITARI…, AREA_M2, EXP_ALAG, EXP_DESL, EXP_INUN, EXP_ONDA, VUL_ALAG, VUL_INUN

## g1229（1 列）
- 見出し：VUL_INUN
- 例1 値：0.8 | 3.03 | 2.59 | 1.59 | 2.27
  - 同じ表の列：ID_AREAS_PRIORITARI…, AREA_M2, EXP_ALAG, EXP_DESL, EXP_INUN, EXP_ONDA, VUL_ALAG, VUL_DESL

## g1230（1 列）
- 見出し：VUL_ONDA
- 例1 値：2.45 | 2.6 | 1.15 | 4.3 | 3.15
  - 同じ表の列：ID_AREAS_PRIORITARI…, AREA_M2, EXP_ALAG, EXP_DESL, EXP_INUN, EXP_ONDA, VUL_ALAG, VUL_DESL

## g1231（1 列）
- 見出し：ID_CONJUNTO
- 例1 値：257 | 344 | 43 | 83 | 201
  - 同じ表の列：AGRUPAMENTO, STATUS_DO_EMPREENDI…, STATUS_DA_REGULARIZ…, UNIDADES_A_INICIAR, UNIDADES_EM_ANDAMEN…, UNIDADES_CONCLUIDAS, PROGRAMA_E/OU_DEMAN…, PROGRAMA_EXTERNO_E/…

## g1232（1 列）
- 見出し：AGRUPAMENTO
- 例1 値：19 | 11 | 3 | 38 | 25
  - 同じ表の列：ID_CONJUNTO, STATUS_DO_EMPREENDI…, STATUS_DA_REGULARIZ…, UNIDADES_A_INICIAR, UNIDADES_EM_ANDAMEN…, UNIDADES_CONCLUIDAS, PROGRAMA_E/OU_DEMAN…, PROGRAMA_EXTERNO_E/…

## g1233（1 列）
- 見出し：STATUS_DO_EMPREENDIMENTO
- 例1 値：Em estudo | Obra concluída | Obra concluída | Obra concluída | Obra concluída
  - 同じ表の列：ID_CONJUNTO, AGRUPAMENTO, STATUS_DA_REGULARIZ…, UNIDADES_A_INICIAR, UNIDADES_EM_ANDAMEN…, UNIDADES_CONCLUIDAS, PROGRAMA_E/OU_DEMAN…, PROGRAMA_EXTERNO_E/…

## g1234（1 列）
- 見出し：STATUS_DA_REGULARIZACAO
- 例1 値：Obra em andamento | Obra em andamento | Obra em andamento | Obra em andamento | Obra em andamento
  - 同じ表の列：ID_CONJUNTO, AGRUPAMENTO, STATUS_DO_EMPREENDI…, UNIDADES_A_INICIAR, UNIDADES_EM_ANDAMEN…, UNIDADES_CONCLUIDAS, PROGRAMA_E/OU_DEMAN…, PROGRAMA_EXTERNO_E/…

## g1235（1 列）
- 見出し：UNIDADES_A_INICIAR
- 例1 値：16 | 20 | 208 | 8 | 24
  - 同じ表の列：ID_CONJUNTO, AGRUPAMENTO, STATUS_DO_EMPREENDI…, STATUS_DA_REGULARIZ…, UNIDADES_EM_ANDAMEN…, UNIDADES_CONCLUIDAS, PROGRAMA_E/OU_DEMAN…, PROGRAMA_EXTERNO_E/…

## g1236（1 列）
- 見出し：UNIDADES_EM_ANDAMENTO
- 例1 値：32 | 180 | 109 | 44 | 88
  - 同じ表の列：ID_CONJUNTO, AGRUPAMENTO, STATUS_DO_EMPREENDI…, STATUS_DA_REGULARIZ…, UNIDADES_A_INICIAR, UNIDADES_CONCLUIDAS, PROGRAMA_E/OU_DEMAN…, PROGRAMA_EXTERNO_E/…

## g1237（1 列）
- 見出し：UNIDADES_CONCLUIDAS
- 例1 値：18 | 56 | 24 | 16 | 32
  - 同じ表の列：ID_CONJUNTO, AGRUPAMENTO, STATUS_DO_EMPREENDI…, STATUS_DA_REGULARIZ…, UNIDADES_A_INICIAR, UNIDADES_EM_ANDAMEN…, PROGRAMA_E/OU_DEMAN…, PROGRAMA_EXTERNO_E/…

## g1238（1 列）
- 見出し：PROGRAMA_E/OU_DEMANDA
- 例1 値：Vila Viva | Acampados; OP; PEAR -> Desabrigados | Vila Viva | Vila Viva | OPH
  - 同じ表の列：ID_CONJUNTO, AGRUPAMENTO, STATUS_DO_EMPREENDI…, STATUS_DA_REGULARIZ…, UNIDADES_A_INICIAR, UNIDADES_EM_ANDAMEN…, UNIDADES_CONCLUIDAS, PROGRAMA_EXTERNO_E/…

## g1239（1 列）
- 見出し：PROGRAMA_EXTERNO_E/OU_FONTE_RECURSO
- 例1 値：PAC 1; PPI | BNDES; PAC 1 | PAC 1; Pró-moradia | BNDES; PAC 1; Saneamento Para Todos | Pró-moradia
  - 同じ表の列：ID_CONJUNTO, AGRUPAMENTO, STATUS_DO_EMPREENDI…, STATUS_DA_REGULARIZ…, UNIDADES_A_INICIAR, UNIDADES_EM_ANDAMEN…, UNIDADES_CONCLUIDAS, PROGRAMA_E/OU_DEMAN…

## g1240（1 列）
- 見出し：PREVISAO_ANO_CONCLUSAO
- 例1 値：2018 | 2018 | 2017 | 2018 | 2021
  - 同じ表の列：ID_CONJUNTO, AGRUPAMENTO, STATUS_DO_EMPREENDI…, STATUS_DA_REGULARIZ…, UNIDADES_A_INICIAR, UNIDADES_EM_ANDAMEN…, UNIDADES_CONCLUIDAS, PROGRAMA_E/OU_DEMAN…

## g1241（1 列）
- 見出し：ID_VILA_FAVELA
- 例1 値：532 | 124 | 105 | 230 | 201
  - 同じ表の列：APELIDO, AGLOMERADO, DOMICILIOS, DATA_DOM, FONTE_DOM, ESTABELECIMENTOS, DATA_EST, FONTE_EST

## g1242（1 列）
- 見出し：APELIDO
- 例1 値：Quiabinho/Gavião/União | Concórdia | Parque Jardim Leblon | Vila da Paz / Pé de Vento | Bananal
  - 同じ表の列：ID_VILA_FAVELA, AGLOMERADO, DOMICILIOS, DATA_DOM, FONTE_DOM, ESTABELECIMENTOS, DATA_EST, FONTE_EST

## g1243（1 列）
- 見出し：AGLOMERADO
- 例1 値：Morro das Pedras | Morro das Pedras | Morro das Pedras | Jardim Montanhês | Santa Lúcia
  - 同じ表の列：ID_VILA_FAVELA, APELIDO, DOMICILIOS, DATA_DOM, FONTE_DOM, ESTABELECIMENTOS, DATA_EST, FONTE_EST

## g1244（1 列）
- 見出し：DOMICILIOS
- 例1 値：315 | 590 | 902 | 24 | 728
  - 同じ表の列：ID_VILA_FAVELA, APELIDO, AGLOMERADO, DATA_DOM, FONTE_DOM, ESTABELECIMENTOS, DATA_EST, FONTE_EST

## g1245（1 列）
- 見出し：DATA_DOM
- 例1 値：12/2014 | 12/2014 | 12/2014 | 12/2014 | 12/2014
  - 同じ表の列：ID_VILA_FAVELA, APELIDO, AGLOMERADO, DOMICILIOS, FONTE_DOM, ESTABELECIMENTOS, DATA_EST, FONTE_EST

## g1246（1 列）
- 見出し：FONTE_DOM
- 例1 値：IBGE - Censo 2010 | URBEL - Estudo Proporcional sobre Censo… | IBGE - Censo 2010 | URBEL - Estudo Proporcional sobre Censo… | URBEL - Estudo Proporcional sobre Censo…
  - 同じ表の列：ID_VILA_FAVELA, APELIDO, AGLOMERADO, DOMICILIOS, DATA_DOM, ESTABELECIMENTOS, DATA_EST, FONTE_EST

## g1247（1 列）
- 見出し：ESTABELECIMENTOS
- 例1 値：0 | 7 | 177 | 43 | 114
  - 同じ表の列：ID_VILA_FAVELA, APELIDO, AGLOMERADO, DOMICILIOS, DATA_DOM, FONTE_DOM, DATA_EST, FONTE_EST

## g1248（1 列）
- 見出し：DATA_EST
- 例1 値：12/2014 | 12/2014 | 12/2014 | 12/2014 | 12/2014
  - 同じ表の列：ID_VILA_FAVELA, APELIDO, AGLOMERADO, DOMICILIOS, DATA_DOM, FONTE_DOM, ESTABELECIMENTOS, FONTE_EST

## g1249（1 列）
- 見出し：FONTE_EST
- 例1 値：URBEL - Estudo Proporcional sobre Censo… | URBEL - Estudo Proporcional sobre Censo… | IBGE - Censo 2010 | URBEL - Estudo Proporcional sobre Censo… | IBGE - Censo 2010
  - 同じ表の列：ID_VILA_FAVELA, APELIDO, AGLOMERADO, DOMICILIOS, DATA_DOM, FONTE_DOM, ESTABELECIMENTOS, DATA_EST

## g1250（1 列）
- 見出し：POPULACAO
- 例1 値：342 | 311 | 645 | 139 | 916
  - 同じ表の列：ID_VILA_FAVELA, APELIDO, AGLOMERADO, DOMICILIOS, DATA_DOM, FONTE_DOM, ESTABELECIMENTOS, DATA_EST

## g1251（1 列）
- 見出し：Page
- 例1 値：/uncategorized/digitalFile_ad773b66-6e3… | /uncategorized/digitalFile_86ad07f3-33e… | /uncategorized/digitalFile_32542df0-e6e… | /uncategorized/digitalFile_136ca281-e3f… | /uncategorized/collection_5deba744-820a…
  - 同じ表の列：Pageviews, Unique Pageviews, Avg. Time on Page, Entrances, Bounce Rate, % Exit

## g1252（1 列）
- 見出し：Pageviews
- 例1 値：16 | 23 | 24 | 53 | 28
  - 同じ表の列：Page, Unique Pageviews, Avg. Time on Page, Entrances, Bounce Rate, % Exit

## g1253（1 列）
- 見出し：Unique Pageviews
- 例1 値：3 | 2 | 31 | 15 | 54
  - 同じ表の列：Page, Pageviews, Avg. Time on Page, Entrances, Bounce Rate, % Exit

## g1254（1 列）
- 見出し：Avg. Time on Page
- 例1 値：0:00:17 | 0:00:35 | 0:02:37 | 0:00:14 | 0:00:11
  - 同じ表の列：Page, Pageviews, Unique Pageviews, Entrances, Bounce Rate, % Exit

## g1255（1 列）
- 見出し：Entrances
- 例1 値：0 | 34 | 43 | 45 | 0
  - 同じ表の列：Page, Pageviews, Unique Pageviews, Avg. Time on Page, Bounce Rate, % Exit

## g1256（1 列）
- 見出し：Bounce Rate
- 例1 値：100.00% | 0.00% | 27.90% | 0.00% | 0.00%
  - 同じ表の列：Page, Pageviews, Unique Pageviews, Avg. Time on Page, Entrances, % Exit

## g1257（1 列）
- 見出し：% Exit
- 例1 値：6.67% | 50.00% | 64.71% | 4.88% | 28.51%
  - 同じ表の列：Page, Pageviews, Unique Pageviews, Avg. Time on Page, Entrances, Bounce Rate

## g1258（2 列）
- 見出し：arealand_sqmi
- 例1 値：0.110478500000000 | 1.768763720000000 | 0.189964190000000 | 7.277603290000000 | 3.464856830000000
  - 同じ表の列：year, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…, education_b15003_02…, education_b15003_02…
- 例2 値：0.095433810000000 | 0.052857440000000 | 1.135830290000000 | 0.494057240000000 | 0.191210800000000
  - 同じ表の列：tract, geoid20, year, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…

## g1259（2 列）
- 見出し：education_b15003_001e
- 例1 値：7537.000000000000000 | 10245.000000000000000 | 28206.000000000000000 | 83140.000000000000000 | 560.000000000000000
  - 同じ表の列：year, arealand_sqmi, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…, education_b15003_02…, education_b15003_02…
- 例2 値：647.000000000000000 | 2605.000000000000000 | 2748.000000000000000 | 2450.000000000000000 | 1596.000000000000000
  - 同じ表の列：tract, geoid20, year, arealand_sqmi, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…

## g1260（2 列）
- 見出し：education_b15003_lt9th
- 例1 値：11.495454570000000 | 8250.956696299999749 | 1447.219066910000038 | 481.803377730000022 | 1531.292051189999938
  - 同じ表の列：year, arealand_sqmi, education_b15003_00…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…, education_b15003_02…, education_b15003_02…
- 例2 値：70.863738229999996 | 258.767287780000004 | 49.330275340000000 | 356.232125129999986 | 48.439226079999997
  - 同じ表の列：tract, geoid20, year, arealand_sqmi, education_b15003_00…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…

## g1261（2 列）
- 見出し：education_b15003_9th_to_12thnodiploma
- 例1 値：565.762779049999949 | 858.396558619999951 | 3041.600028800000018 | 190.167302729999989 | 1571.491146820000040
  - 同じ表の列：year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_hs…, education_b15003_so…, education_b15003_02…, education_b15003_02…
- 例2 値：37.602584190000002 | 26.399999999999999 | 0.000000000000000 | 27.757353030000001 | 23.753231480000000
  - 同じ表の列：tract, geoid20, year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_hs…, education_b15003_so…

## g1262（2 列）
- 見出し：education_b15003_hsgrad_and_ged
- 例1 値：3198.947848549999890 | 1238.015051840000069 | 2594.833213519999845 | 699.481730559999960 | 718.195275349999974
  - 同じ表の列：year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_so…, education_b15003_02…, education_b15003_02…
- 例2 値：521.189380099999994 | 134.790402519999986 | 81.025013319999999 | 508.583413230000019 | 922.936322949999976
  - 同じ表の列：tract, geoid20, year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_so…

## g1263（2 列）
- 見出し：education_b15003_somecollegenodegree
- 例1 値：250.721252329999999 | 390.371568910000008 | 982.779486570000017 | 586.067360440000016 | 4191.143836010000086
  - 同じ表の列：year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_02…, education_b15003_02…
- 例2 値：44.828236230000002 | 204.364964839999999 | 382.035625579999987 | 368.712757319999980 | 114.376860330000000
  - 同じ表の列：tract, geoid20, year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…

## g1264（2 列）
- 見出し：education_b15003_021e
- 例1 値：288.276340829999981 | 4868.979706950000036 | 1359.007105590000037 | 2188.661361689999922 | 1899.665021300000035
  - 同じ表の列：year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…, education_b15003_02…
- 例2 値：43.316380000000002 | 0.426332290000000 | 0.000000000000000 | 42.580512589999998 | 141.023255930000005
  - 同じ表の列：tract, geoid20, year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…

## g1265（1 列）
- 見出し：education_b15003_022e
- 例1 値：9006.490133119999882 | 6329.228040910000345 | 7997.233833070000401 | 5876.562967169999865 | 8211.334453379999104
  - 同じ表の列：year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…, education_b15003_02…

## g1266（1 列）
- 見出し：education_b15003_gradprofdegree
- 例1 値：10518.051769190000414 | 3305.595682600000146 | 5341.306207450000329 | 1744.336496829999987 | 3862.265486509999846
  - 同じ表の列：year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…, education_b15003_02…

## g1267（1 列）
- 見出し：tract
- 例1 値：070104 | 020200 | 140202 | 981300 | 061000
  - 同じ表の列：geoid20, year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…

## g1268（1 列）
- 見出し：geoid20
- 例1 値：25025081301 | 25025130101 | 25025101102 | 25025090901 | 25025120700
  - 同じ表の列：tract, year, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…

## g1269（1 列）
- 見出し：year
- 例1 値：2025.000000000000000 | 2025.000000000000000 | 2025.000000000000000 | 2025.000000000000000 | 2025.000000000000000
  - 同じ表の列：tract, geoid20, arealand_sqmi, education_b15003_00…, education_b15003_lt…, education_b15003_9t…, education_b15003_hs…, education_b15003_so…

## g1270（1 列）
- 見出し：Date
- 例1 値：06/29/2013 | 12/07/2010 | 02/06/2011 | 07/17/2011 | 07/09/2013
  - 同じ表の列：Year, Month, DayOfYear, Total, BPD, BFD, EMS

## g1271（1 列）
- 見出し：DayOfYear
- 例1 値：333 | 178 | 66 | 37 | 182
  - 同じ表の列：Date, Year, Month, Total, BPD, BFD, EMS

## g1272（1 列）
- 見出し：Total
- 例1 値：2110 | 2335 | 3101 | 3028 | 2511
  - 同じ表の列：Date, Year, Month, DayOfYear, BPD, BFD, EMS

## g1273（1 列）
- 見出し：BPD
- 例1 値：2374 | 1923 | 2668 | 2108 | 2385
  - 同じ表の列：Date, Year, Month, DayOfYear, Total, BFD, EMS

## g1274（1 列）
- 見出し：BFD
- 例1 値：258 | 642 | 229 | 191 | 225
  - 同じ表の列：Date, Year, Month, DayOfYear, Total, BPD, EMS

## g1275（1 列）
- 見出し：EMS
- 例1 値：389 | 411 | 374 | 347 | 404
  - 同じ表の列：Date, Year, Month, DayOfYear, Total, BPD, BFD

## g1276（1 列）
- 見出し：Neighborhood
- 例1 値：Parks | Parks | Roslindale | City Hall Truck | City Hall Truck
  - 同じ表の列：Date, Connections

## g1277（1 列）
- 見出し：Date
- 例1 値：05/07/2014 12:00:00 AM | 07/17/2014 12:00:00 AM | 04/19/2015 12:00:00 AM | 07/14/2014 12:00:00 AM | 08/18/2014 12:00:00 AM
  - 同じ表の列：Neighborhood, Connections

## g1278（1 列）
- 見出し：Connections
- 例1 値：57 | 408 | 0 | 0 | 160
  - 同じ表の列：Neighborhood, Date

## g1279（1 列）
- 見出し：Protocol
- 例1 値：ICLEI: Local Government Operations Prot… | ICLEI: Local Government Operations Prot… | ICLEI: Local Government Operations Prot… | ICLEI: Local Government Operations Prot… | ICLEI: Local Government Operations Prot…
  - 同じ表の列：Department, Sector, Fuel Type, Year (Fiscal Year), GHG Emissions (t CO…

## g1280（1 列）
- 見出し：Department
- 例1 値：PWD | BPS | PWD | Fire | Police
  - 同じ表の列：Protocol, Sector, Fuel Type, Year (Fiscal Year), GHG Emissions (t CO…

## g1281（1 列）
- 見出し：Sector
- 例1 値：Vehicles | Unknown | Vehicles | Buildings | Vehicles
  - 同じ表の列：Protocol, Department, Fuel Type, Year (Fiscal Year), GHG Emissions (t CO…

## g1282（1 列）
- 見出し：Fuel Type
- 例1 値：Diesel | Natural Gas | Gasoline | Diesel | Electricity
  - 同じ表の列：Protocol, Department, Sector, Year (Fiscal Year), GHG Emissions (t CO…

## g1283（1 列）
- 見出し：Year (Fiscal Year)
- 例1 値：2010 | 2020 | 2016 | 2015 | 2008
  - 同じ表の列：Protocol, Department, Sector, Fuel Type, GHG Emissions (t CO…

## g1284（1 列）
- 見出し：GHG Emissions (t CO2e)
- 例1 値：172 | - | - | 923.06 | 2,959
  - 同じ表の列：Protocol, Department, Sector, Fuel Type, Year (Fiscal Year)

## g1285（1 列）
- 見出し：DateTime_Measured
- 例1 値：2020-03-18 06:15:00 | 2020-03-20 08:30:00 | 2020-03-17 13:30:00 | 2020-03-23 01:15:00 | 2020-03-18 17:30:00
  - 同じ表の列：Total_Demand_KW

## g1286（1 列）
- 見出し：Total_Demand_KW
- 例1 値：0 | 975 | 0 | 0 | 0
  - 同じ表の列：DateTime_Measured

## g1287（1 列）
- 見出し：pid_long
- 例1 値：604325000 | 604048000 | 1202138000 | 401037600 | 303840000
  - 同じ表の列：id, cm_id, building_typology, building_subtypology, use_class, sqft_class, year_built_class, st_num

## g1288（1 列）
- 見出し：cm_id
- 例1 値：500105010 | 303547000 | 502598000 | 303061020 | 300475000
  - 同じ表の列：id, pid_long, building_typology, building_subtypology, use_class, sqft_class, year_built_class, st_num

## g1289（1 列）
- 見出し：building_typology
- 例1 値：Residential (Mixed-Use) | Multi-Family (3 units) | Multi-Family (3 units) | Multi-Family (3 units) | Multi-Family (2 units)
  - 同じ表の列：id, pid_long, cm_id, building_subtypology, use_class, sqft_class, year_built_class, st_num

## g1290（1 列）
- 見出し：building_subtypology
- 例1 値：Multi-Family (3 units), Pre-1915 | Multi-Family (3 units), Pre-1915 | Residential (Mixed-Use), 1980-present | Hotel, 1980-present | Vacant
  - 同じ表の列：id, pid_long, cm_id, building_typology, use_class, sqft_class, year_built_class, st_num

## g1291（1 列）
- 見出し：use_class
- 例1 値：Residential | Commercial | Vacant | Commercial | Residential
  - 同じ表の列：id, pid_long, cm_id, building_typology, building_subtypology, sqft_class, year_built_class, st_num

## g1292（1 列）
- 見出し：sqft_class
- 例1 値：< 25,000 sqft | < 25,000 sqft | < 25,000 sqft | >= 100,000 sqft | < 25,000 sqft
  - 同じ表の列：id, pid_long, cm_id, building_typology, building_subtypology, use_class, year_built_class, st_num

## g1293（1 列）
- 見出し：year_built_class
- 例1 値：1950-1979 | Pre-1915 | Pre-1915 | Pre-1915 | Pre-1915
  - 同じ表の列：id, pid_long, cm_id, building_typology, building_subtypology, use_class, sqft_class, st_num

## g1294（1 列）
- 見出し：st_num
- 例1 値：33 | 193 | 1575 | 400 | 209 211
  - 同じ表の列：id, pid_long, cm_id, building_typology, building_subtypology, use_class, sqft_class, year_built_class

## g1295（1 列）
- 見出し：zipcode
- 例1 値：2110 | 2127 | 2128 | 2127 | 2109
  - 同じ表の列：id, pid_long, cm_id, building_typology, building_subtypology, use_class, sqft_class, year_built_class

## g1296（1 列）
- 見出し：case_no
- 例1 値：V874508 | V908861 | V873588 | V929824 | V857360
  - 同じ表の列：ap_case_defn_key, status_dttm, status, code, value, violation_stno, violation_sthigh, violation_suffix

## g1297（1 列）
- 見出し：ap_case_defn_key
- 例1 値：1013 | 1013 | 1013 | 1013 | 1013
  - 同じ表の列：case_no, status_dttm, status, code, value, violation_stno, violation_sthigh, violation_suffix

## g1298（1 列）
- 見出し：status_dttm
- 例1 値：2025-09-04 15:39:57 | 2025-04-30 09:05:45 | 2025-03-20 08:14:08 | 2025-12-12 09:25:43 | 2025-11-20 15:16:14
  - 同じ表の列：case_no, ap_case_defn_key, status, code, value, violation_stno, violation_sthigh, violation_suffix

## g1299（1 列）
- 見出し：status
- 例1 値：Closed | Closed | Closed | Open | Open
  - 同じ表の列：case_no, ap_case_defn_key, status_dttm, code, value, violation_stno, violation_sthigh, violation_suffix

## g1300（1 列）
- 見出し：code
- 例1 値：105.1 | 104.6 | 105.1 | 105 | 102.8
  - 同じ表の列：case_no, ap_case_defn_key, status_dttm, status, value, violation_stno, violation_sthigh, violation_suffix

## g1301（1 列）
- 見出し：value
- 例1 値：N/A | N/A | N/A | N/A | N/A
  - 同じ表の列：case_no, ap_case_defn_key, status_dttm, status, code, violation_stno, violation_sthigh, violation_suffix

## g1302（1 列）
- 見出し：violation_stno
- 例1 値：22 | 95 | 61 | 270 | 18
  - 同じ表の列：case_no, ap_case_defn_key, status_dttm, status, code, value, violation_sthigh, violation_suffix

## g1303（1 列）
- 見出し：violation_sthigh
- 例1 値：31 | 790 | 37A | 1667 | 773
  - 同じ表の列：case_no, ap_case_defn_key, status_dttm, status, code, value, violation_stno, violation_suffix

## g1304（1 列）
- 見出し：violation_suffix
- 例1 値：AV | ST | ST | ST | PL
  - 同じ表の列：case_no, ap_case_defn_key, status_dttm, status, code, value, violation_stno, violation_sthigh

## g1305（1 列）
- 見出し：violation_city
- 例1 値：Mattapan | Roslindale | Dorchester | Dorchester | West Roxbury
  - 同じ表の列：case_no, ap_case_defn_key, status_dttm, status, code, value, violation_stno, violation_sthigh

## g1306（1 列）
- 見出し：mailing_neighborhood
- 例1 値：Jamaica Plain | Jamaica Plain | Dorchester | Dorchester | Hyde Park
  - 同じ表の列：state, x_coord, y_coord, recollect, trashday, pwd_district

## g1307（2 列）
- 見出し：state
- 例1 値：MA | MA | MA | MA | MA
  - 同じ表の列：mailing_neighborhood, x_coord, y_coord, recollect, trashday, pwd_district
- 例2 値：MA | MA | MA | MA | MA
  - 同じ表の列：Division/Sitegroup, Site, City, Country, Type, Category, UOM, Feb 14

## g1308（1 列）
- 見出し：x_coord
- 例1 値：-71.061340001416 | -71.05429000164445 | -71.03014000123652 | -71.06118000112106 | -71.05574000098919
  - 同じ表の列：mailing_neighborhood, state, y_coord, recollect, trashday, pwd_district

## g1309（1 列）
- 見出し：y_coord
- 例1 値：42.251850000190714 | 42.34856999925462 | 42.29092999974307 | 42.30716999954422 | 42.29594000003194
  - 同じ表の列：mailing_neighborhood, state, x_coord, recollect, trashday, pwd_district

## g1310（1 列）
- 見出し：recollect
- 例1 値：TH | T | W | TH | TH
  - 同じ表の列：mailing_neighborhood, state, x_coord, y_coord, trashday, pwd_district

## g1311（1 列）
- 見出し：trashday
- 例1 値：TH | W | T | F | F
  - 同じ表の列：mailing_neighborhood, state, x_coord, y_coord, recollect, pwd_district

## g1312（1 列）
- 見出し：pwd_district
- 例1 値：7 | 5 | 2 | 7 | 7
  - 同じ表の列：mailing_neighborhood, state, x_coord, y_coord, recollect, trashday

## g1313（1 列）
- 見出し：District
- 例1 値：Brighton | Dorchester | Roxbury | Dorchester | Dorchester
  - 同じ表の列：CityLampNumber, NStarAcct, ExistingSizeLumens, ExistingWattage, Type, KWH/YR, Cost / Yr, NewSize

## g1314（1 列）
- 見出し：CityLampNumber
- 例1 値：14604 | 3902 | 22396 | 4024 | 24403
  - 同じ表の列：District, NStarAcct, ExistingSizeLumens, ExistingWattage, Type, KWH/YR, Cost / Yr, NewSize

## g1315（1 列）
- 見出し：NStarAcct
- 例1 値：25710891000 | NULL | 25955831000 | 25710981009 | 25711101003
  - 同じ表の列：District, CityLampNumber, ExistingSizeLumens, ExistingWattage, Type, KWH/YR, Cost / Yr, NewSize

## g1316（1 列）
- 見出し：ExistingSizeLumens
- 例1 値：16000 | 16000 | 11000 | 25000 | 25000
  - 同じ表の列：District, CityLampNumber, NStarAcct, ExistingWattage, Type, KWH/YR, Cost / Yr, NewSize

## g1317（1 列）
- 見出し：ExistingWattage
- 例1 値：0.295 | 0.295 | 0.295 | 0.295 | 0.192
  - 同じ表の列：District, CityLampNumber, NStarAcct, ExistingSizeLumens, Type, KWH/YR, Cost / Yr, NewSize

## g1318（2 列）
- 見出し：Type
- 例1 値：Sodium | Sodium | Sodium | Sodium | Sodium
  - 同じ表の列：District, CityLampNumber, NStarAcct, ExistingSizeLumens, ExistingWattage, KWH/YR, Cost / Yr, NewSize
- 例2 値：Volume | Volume | Cost | Volume | Cost
  - 同じ表の列：Division/Sitegroup, Site, City, State, Country, Category, UOM, Feb 14

## g1319（1 列）
- 見出し：KWH/YR
- 例1 値：806 | 806 | 806 | 1239 | 806
  - 同じ表の列：District, CityLampNumber, NStarAcct, ExistingSizeLumens, ExistingWattage, Type, Cost / Yr, NewSize

## g1320（1 列）
- 見出し：Cost / Yr
- 例1 値：69.123800000000003 | 44.966700000000003 | 44.966700000000003 | 69.123800000000003 | 69.123800000000003
  - 同じ表の列：District, CityLampNumber, NStarAcct, ExistingSizeLumens, ExistingWattage, Type, KWH/YR, NewSize

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
