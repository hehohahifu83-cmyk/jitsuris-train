# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：Anlage_projekt-bezeichnung
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, ［個人別の記録のため削除］hr, Anmeldedatum, Anlage_inbetriebnah…

## g0002（1 列）
- 見出し：Empfaengerwechsel
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Anlage_projekt-beze…, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, ［個人別の記録のため削除］hr, Anmeldedatum, Anlage_inbetriebnah…

## g0003（1 列）
- 見出し：Anlage_energietraeger
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Leistung_kw, Produktion_kwh, Verguetung_chf, ［個人別の記録のため削除］hr, Anmeldedatum, Anlage_inbetriebnah…

## g0004（1 列）
- 見出し：Leistung_kw
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | 3 | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Produktion_kwh, Verguetung_chf, ［個人別の記録のため削除］hr, Anmeldedatum, Anlage_inbetriebnah…

## g0005（1 列）
- 見出し：Produktion_kwh
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Verguetung_chf, ［個人別の記録のため削除］hr, Anmeldedatum, Anlage_inbetriebnah…

## g0006（1 列）
- 見出し：Verguetung_chf
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, ［個人別の記録のため削除］hr, Anmeldedatum, Anlage_inbetriebnah…

## g0007（1 列）
- 見出し：［個人別の記録のため削除］hr
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, Anmeldedatum, Anlage_inbetriebnah…

## g0008（1 列）
- 見出し：Anmeldedatum
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, ［個人別の記録のため削除］hr, Anlage_inbetriebnah…

## g0009（1 列）
- 見出し：Anlage_inbetriebnahme
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, ［個人別の記録のため削除］hr, Anmeldedatum

## g0010（1 列）
- 見出し：Anlage_vertragsende
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Anlage_projekt-beze…, Empfaengerwechsel, Anlage_energietraeg…, Leistung_kw, Produktion_kwh, Verguetung_chf, ［個人別の記録のため削除］hr, Anmeldedatum

## g0011（1 列）
- 見出し：Id
- 例1 値：5 | ［個人別の記録のため削除］ | 3 | 4 | ［個人別の記録のため削除］
  - 同じ表の列：Titel, Ausgabejahr, Auftraggeber, Kanton, Link

## g00［個人別の記録のため削除］（1 列）
- 見出し：Titel
- 例1 値：Wärme- und Kältenutzung aus Sempacher- … | ［個人別の記録のため削除］ | Potenzial des Walensees für Wärme- und … | Impacts of using lakes and rivers for e… | Factsheet Wärmenutzung aus Seen und Fli…
  - 同じ表の列：Id, Ausgabejahr, Auftraggeber, Kanton, Link

## g0013（1 列）
- 見出し：Ausgabejahr
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Id, Titel, Auftraggeber, Kanton, Link

## g0014（1 列）
- 見出し：Auftraggeber
- 例1 値：Schmit M., Wüst. A, Bryner A,. Penicka … | Gaudard A., Weber C., Alexander T.J., H… | AWEL, Amt für Abfall Wasser, Energie un… | Amt für Wasser und Energie des Kantons … | Amt für Wasser und Energie des Kantons …
  - 同じ表の列：Id, Titel, Ausgabejahr, Kanton, Link

## g0015（1 列）
- 見出し：Kanton
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：Id, Titel, Ausgabejahr, Auftraggeber, Link

## g0018（1 列）
- 見出し：Thorium_Kg
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Date, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Uranium_reprocessin…, Plutonium_Kg

## g0019（1 列）
- 見出し：Uranium_depleted_Kg
- 例1 値：［個人別の記録のため削除］ | 8 | 8 | 15 | 8
  - 同じ表の列：Date, Thorium_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Uranium_reprocessin…, Plutonium_Kg

## g0020（1 列）
- 見出し：Uranium_natural_Kg
- 例1 値：955833 | 1545182 | 1543682 | ［個人別の記録のため削除］42580 | 662399
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Uranium_reprocessin…, Plutonium_Kg

## g0021（1 列）
- 見出し：Uranium_enriched_low_Kg
- 例1 値：107565 | 89831 | 81903 | 134011 | 13［個人別の記録のため削除］52
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_hi…, Uranium_reprocessin…, Plutonium_Kg

## g0022（1 列）
- 見出し：Uranium_enriched_high_Kg
- 例1 値：0 | 0 | 0 | 0 | 0
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_reprocessin…, Plutonium_Kg

## g0023（1 列）
- 見出し：Uranium_reprocessing_Kg
- 例1 値：684［個人別の記録のため削除］ | 0 | ［個人別の記録のため削除］7623 | 684［個人別の記録のため削除］ | 183728
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Plutonium_Kg

## g0024（1 列）
- 見出し：Plutonium_Kg
- 例1 値：1430 | 1 | 1 | 1 | 2414
  - 同じ表の列：Date, Thorium_Kg, Uranium_depleted_Kg, Uranium_natural_Kg, Uranium_enriched_lo…, Uranium_enriched_hi…, Uranium_reprocessin…

## g0025（2 列）
- 見出し：GEO_NR
- 例1 値：118 | 1322 | 138 | 723 | 243
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS
- 例2 値：52 | 62 | 62 | 52 | 62
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0026（1 列）
- 見出し：CLASS_HAB
- 例1 値：2 | 2 | 3 | 4 | 1
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0027（3 列）
- 見出し：GEOM_PERIOD
- 例1 値：2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS
- 例2 値：2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01 | 2022-05-01
  - 同じ表の列：GEO_NR, CLASS_HAB, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0028（1 列）
- 見出し：VARIABLE
- 例1 値：sec_t_20 | sec_t_20 | sec_tran_20 | schu_t_98 | sec_gen_20
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0029（2 列）
- 見出し：SOURCE
- 例1 値：SDL | SDL | SDL | SDL | SDL
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS
- 例2 値：ESTV | ESTV | EFV | ESTV | ESTV
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0030（1 列）
- 見出し：VA［個人別の記録のため削除］E_PERIOD
- 例1 値：1998/99 | 2020/21 | 2008/09 | ［個人別の記録のため削除］/20 | 2020/21
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0031（3 列）
- 見出し：UNIT_VA［個人別の記録のため削除］E
- 例1 値：Num | Num | Num | Num | Num
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, VA［個人別の記録のため削除］E, STATUS
- 例2 値：Num | Num | Per | Num | Num
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, VA［個人別の記録のため削除］E, STATUS

## g0032（1 列）
- 見出し：VA［個人別の記録のため削除］E
- 例1 値：56 | ［個人別の記録のため削除］33 | 3095 | 1［個人別の記録のため削除］0 | 0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, STATUS

## g0033（3 列）
- 見出し：STATUS
- 例1 値：A | A | A | A | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E
- 例2 値：A | A | A | A | A
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E

## g0034（1 列）
- 見出し：GEO_NR
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］1 | 131 | ［個人別の記録のため削除］1 | ［個人別の記録のため削除］
  - 同じ表の列：CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0035（2 列）
- 見出し：CLASS_HAB
- 例1 値：4 | 2 | 2 | Total | 3
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS
- 例2 値：Total | 3 | 4 | Total | 4
  - 同じ表の列：GEO_NR, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0036（1 列）
- 見出し：VARIABLE
- 例1 値：wh_en_gaz | umz_zu_t_p | bat_stor_2 | sur_5z | bat_tot
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0037（1 列）
- 見出し：SOURCE
- 例1 値：GWS | GWS | GWS, STATPOP | GWS | GWS
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0038（2 列）
- 見出し：VA［個人別の記録のため削除］E_PERIOD
- 例1 値：2021 | 2020 | 2021 | 2021 | 2021
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS
- 例2 値：2023 | 2021 | 2023 | 2023 | 2021
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0039（2 列）
- 見出し：VA［個人別の記録のため削除］E
- 例1 値：8428.0 | 886.0 | 208.0 | 275.0 | 44.0
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, STATUS
- 例2 値：26.05 | 0.0 | 223006.96 | 548.9 | ［個人別の記録のため削除］.46
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, VARIABLE, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, STATUS

## g0040（1 列）
- 見出し：VARIABLE
- 例1 値：rev_cel_20 | rev_mar_35 | rev_ren_70 | rev_cel_80 | dep_inv
  - 同じ表の列：GEO_NR, CLASS_HAB, GEOM_PERIOD, SOURCE, VA［個人別の記録のため削除］E_PERIOD, UNIT_VA［個人別の記録のため削除］E, VA［個人別の記録のため削除］E, STATUS

## g0042（1 列）
- 見出し：NOM_DU_LIEU
- 例1 値：Ideavox | Westhive | Le D5 | Cité universitaire de Genève | Hono Coworking Space
  - 同じ表の列：OBJECTID, STRUCTURE_PORTEUSE, ZONE_GEOGRAPHIQUE, VILLE_OU_COMMUNE, WEBSITE, EQUIPEMENTS, SERVICES, TYPES_ESPACE

## g0043（1 列）
- 見出し：STRUCTURE_PORTEUSE
- 例1 値：Association HiFLOW | SPACES | Business Centre | Atelier 9 | Mousse Space
  - 同じ表の列：OBJECTID, NOM_DU_LIEU, ZONE_GEOGRAPHIQUE, VILLE_OU_COMMUNE, WEBSITE, EQUIPEMENTS, SERVICES, TYPES_ESPACE

## g0044（1 列）
- 見出し：ZONE_GEOGRAPHIQUE
- 例1 値：Pôle Metropolitain du Genevois Français | Canton de Genève | Canton de Genève | Canton de Genève | Canton de Genève
  - 同じ表の列：OBJECTID, NOM_DU_LIEU, STRUCTURE_PORTEUSE, VILLE_OU_COMMUNE, WEBSITE, EQUIPEMENTS, SERVICES, TYPES_ESPACE

## g0045（1 列）
- 見出し：VILLE_OU_COMMUNE
- 例1 値：Thyez | La Roche-sur-Foron | Gaillard | Meyrin | Gland
  - 同じ表の列：OBJECTID, NOM_DU_LIEU, STRUCTURE_PORTEUSE, ZONE_GEOGRAPHIQUE, WEBSITE, EQUIPEMENTS, SERVICES, TYPES_ESPACE

## g0047（1 列）
- 見出し：EQUIPEMENTS
- 例1 値：Mobilier de bureau | Accès Wifi,Mobilier de bureau,Café - th… | Établis,Outils à main - tournevis - mar… | Vidéo projecteur,Mobilier de bureau,Caf… | Atelier bois,Imprimantes 3D,Scanner 3D,…
  - 同じ表の列：OBJECTID, NOM_DU_LIEU, STRUCTURE_PORTEUSE, ZONE_GEOGRAPHIQUE, VILLE_OU_COMMUNE, WEBSITE, SERVICES, TYPES_ESPACE

## g0048（1 列）
- 見出し：SERVICES
- 例1 値：Accès aux équipements,Accès aux espaces… | Domiciliation,Location de bureaux,Locat… | Accès aux équipements,Domiciliation,Loc… | Accès aux espaces,Accès aux équipements… | Accès aux espaces,Accès aux équipements…
  - 同じ表の列：OBJECTID, NOM_DU_LIEU, STRUCTURE_PORTEUSE, ZONE_GEOGRAPHIQUE, VILLE_OU_COMMUNE, WEBSITE, EQUIPEMENTS, TYPES_ESPACE

## g0049（1 列）
- 見出し：TYPES_ESPACE
- 例1 値：Bureaux privatifs,Espace de coworking,R… | Espace de coworking,Bureaux privatifs,O… | Espace fablab,Atelier | Espace de coworking,Salle de réunions,B… | Espace collaboratif dématérialisé,Espac…
  - 同じ表の列：OBJECTID, NOM_DU_LIEU, STRUCTURE_PORTEUSE, ZONE_GEOGRAPHIQUE, VILLE_OU_COMMUNE, WEBSITE, EQUIPEMENTS, SERVICES

## g0050（1 列）
- 見出し：MODALITE_ACCES
- 例1 値：Tarifs des visites,Tarif à l'heure,Tari… | Abonnement mensuel,Pack d'heures,Tarif … | Abonnement mensuel,Tarif à l'heure | Tarifs des types espaces,Tarif à l'heur… | Tarifs des types espaces,Abonnement men…
  - 同じ表の列：OBJECTID, NOM_DU_LIEU, STRUCTURE_PORTEUSE, ZONE_GEOGRAPHIQUE, VILLE_OU_COMMUNE, WEBSITE, EQUIPEMENTS, SERVICES

## g0051（1 列）
- 見出し：LIEU_DIT
- 例1 値：Malval | Champ Coquet | Sous la Côte | Les Baillets | La Meure
  - 同じ表の列：OBJECTID, SHAPE_AREA, SHAPE_LEN

## g0052（2 列）
- 見出し：SHAPE_AREA
- 例1 値：3331.89690848 | 1186.31878776 | 4143.97593582 | 5265.544757325 | 6796.302675835
  - 同じ表の列：OBJECTID, LIEU_DIT, SHAPE_LEN
- 例2 値：594564.13077637 | 737051.358648255 | 281837.89335279 | 35［個人別の記録のため削除］4［個人別の記録のため削除］72792715 | 457554.0503896
  - 同じ表の列：OBJECTID, AM_L_OBJ, AM_L_BEREI

## g0053（1 列）
- 見出し：SHAPE_LEN
- 例1 値：568.43113475［個人別の記録のため削除］32 | 371.83［個人別の記録のため削除］456079 | 376.966283063243 | 181.953703678［個人別の記録のため削除］2 | 331.857542509064
  - 同じ表の列：OBJECTID, LIEU_DIT, SHAPE_AREA

## g0054（1 列）
- 見出し：AM_L_OBJ
- 例1 値：GE5 | GE44 | GE50 | GE11 | GE10
  - 同じ表の列：OBJECTID, AM_L_BEREI, SHAPE_AREA

## g0055（1 列）
- 見出し：AM_L_BEREI
- 例1 値：A | B | A | B | A
  - 同じ表の列：OBJECTID, AM_L_OBJ, SHAPE_AREA

## g0056（2 列）
- 見出し：BFS_Gemeindenummer
- 例1 値：2764 | 2829 | 2861 | 2766 | 2828
  - 同じ表の列：Gemeinde, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Alter, Anzahl_Plätze_Tages…
- 例2 値：2769 | 2769 | 2769 | 2788 | 2829
  - 同じ表の列：Gemeinde, Kategorie, PLZ, Ort, Website, Datenquelle, e_eingangskoordinate, n_eingangskoordinate

## g0058（1 列）
- 見出し：Institution
- 例1 値：Tagesheim Kakadu | Kita Laufen | Kinderkrippe Häslischloss Gartenstadt 5 | Tagesstruktur Bottmingen Burggartenstra… | Kindertagesstätte Taavi
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, PLZ, Ort, Trägerschaft, Rechtsform, Alter, Anzahl_Plätze_Tages…

## g0061（1 列）
- 見出し：Trägerschaft
- 例1 値：Einwohnergemeinde Bottmingen | Chindernäst GmbH | familea – Für Frauen, Kinder und Famili… | familea – Für Frauen, Kinder und Famili… | Kinderkrippe Häslischloss GmbH
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Rechtsform, Alter, Anzahl_Plätze_Tages…

## g0062（1 列）
- 見出し：Rechtsform
- 例1 値：privat | privat | öffentlich-rechtlich | privat | privat
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Trägerschaft, Alter, Anzahl_Plätze_Tages…

## g0063（1 列）
- 見出し：Alter
- 例1 値：4 bis 13 ［個人別の記録のため削除］hre | 4 bis ［個人別の記録のため削除］ ［個人別の記録のため削除］hre | 4 Monate bis Kindergarteneeintritt | 3 Monate bis 13 ［個人別の記録のため削除］hre | 6 bis 13 ［個人別の記録のため削除］hre
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Anzahl_Plätze_Tages…

## g0064（1 列）
- 見出し：Anzahl_Plätze_Tagesbetreuung
- 例1 値：22 | 17 | 33 | 30 | 20
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Alter

## g0065（1 列）
- 見出し：Anzahl_Plätze_Mittagstisch
- 例1 値：140 | ［個人別の記録のため削除］ | 60 | 47 | 30
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Institution, PLZ, Ort, Trägerschaft, Rechtsform, Alter

## g0066（1 列）
- 見出し：Gemeinde
- 例1 値：Frenkendorf | Muttenz | Liesberg | Oberdorf (BL) | Zunzgen
  - 同じ表の列：BFS_Gemeindenummer, Kategorie, PLZ, Ort, Website, Datenquelle, e_eingangskoordinate, n_eingangskoordinate

## g0070（1 列）
- 見出し：Datenquelle
- 例1 値：Sicherheitsdirektion BL - Fachbereich F… | Sicherheitsdirektion BL - Fachbereich F… | Sicherheitsdirektion BL - Fachbereich F… | Sicherheitsdirektion BL - Fachbereich F… | Sicherheitsdirektion BL - Fachbereich F…
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Ort, Website, e_eingangskoordinate, n_eingangskoordinate

## g0071（1 列）
- 見出し：e_eingangskoordinate
- 例1 値：26［個人別の記録のため削除］552.315 | 2633387.897 | 260434［個人別の記録のため削除］86 | 2613082.039 | 2622673.998
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Ort, Website, Datenquelle, n_eingangskoordinate

## g0072（1 列）
- 見出し：n_eingangskoordinate
- 例1 値：［個人別の記録のため削除］60423.022 | ［個人別の記録のため削除］57689.259 | ［個人別の記録のため削除］65441.86 | ［個人別の記録のため削除］57419.895 | ［個人別の記録のため削除］63654.607
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Ort, Website, Datenquelle, e_eingangskoordinate

## g0073（2 列）
- 見出し：koordinaten
- 例1 値：47.［個人別の記録のため削除］71526089605, 7.6319822337704455 | 47.50954343697323, 7.599860505798547 | 47.540［個人別の記録のため削除］386996969, 7.574738266367988 | 47.5095434279977, 7.599860492497234 | 47.51301154383288, 7.5985013645［個人別の記録のため削除］049
  - 同じ表の列：BFS_Gemeindenummer, Gemeinde, Kategorie, PLZ, Ort, Website, Datenquelle, e_eingangskoordinate
- 例2 値：47.49374270802317, 7.591097830566832 | 47.463［個人別の記録のため削除］461919887, 7.836230540920188 | 47.461132638449556, 7.914650025186573 | 47.4［個人別の記録のため削除］0［個人別の記録のため削除］5741037, 7.844308260868218 | 47.49913102298276, 7.558253240913667
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODE

## g0074（1 列）
- 見出し：BFS_Nummer
- 例1 値：2882 | 2854 | 2862 | 2890 | 2768
  - 同じ表の列：Zusatz, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODE, GKODN

## g0075（1 列）
- 見出し：Zusatz
- 例1 値：Gemeindeverwaltung Ettingen | c/o Gemeindeverwaltung Zeglingen | Gemeindeverwaltung Maisprach | Gemeindeverwaltung Buus | Gemeindeverwaltung Giebenach
  - 同じ表の列：BFS_Nummer, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODE, GKODN

## g0076（1 列）
- 見出し：Ort
- 例1 値：Hemmiken | Röschenz | Schönenbuch | Muttenz | Gelterkinden
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Website, UID_Nummer, UID_Link, GKODE, GKODN

## g0077（1 列）
- 見出し：Website
- 例1 値：https://www.hemmiken.ch/ | https://www.roggenburg.ch/ | https://www.baselland.ch/politik-und-be… | https://www.muttenz.ch/ | https://www.schoenenbuch.ch/
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, UID_Nummer, UID_Link, GKODE, GKODN

## g0078（1 列）
- 見出し：UID_Nummer
- 例1 値：［個人別の記録のため削除］E115091561 | ［個人別の記録のため削除］E115091070 | ［個人別の記録のため削除］E115093063 | ［個人別の記録のため削除］E115090946 | ［個人別の記録のため削除］E115091897
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Link, GKODE, GKODN

## g0079（1 列）
- 見出し：UID_Link
- 例1 値：https://www.uid.admin.ch/Detail.aspx?ui… | https://www.uid.admin.ch/Detail.aspx?ui… | https://www.uid.admin.ch/Detail.aspx?ui… | https://www.uid.admin.ch/Detail.aspx?ui… | https://www.uid.admin.ch/Detail.aspx?ui…
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Nummer, GKODE, GKODN

## g0080（1 列）
- 見出し：GKODE
- 例1 値：2630957.514 | 2627789.583 | 2628702.59 | 2624［個人別の記録のため削除］9.498 | 263589［個人別の記録のため削除］87
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODN

## g0081（1 列）
- 見出し：GKODN
- 例1 値：［個人別の記録のため削除］5［個人別の記録のため削除］.321 | ［個人別の記録のため削除］65693.976 | ［個人別の記録のため削除］49827.567 | ［個人別の記録のため削除］62063.929 | ［個人別の記録のため削除］55642.584
  - 同じ表の列：BFS_Nummer, Zusatz, PLZ, Ort, Website, UID_Nummer, UID_Link, GKODE

## g0083（2 列）
- 見出し：Vorlage-ID
- 例1 値：2 | 3 | 6 | 2 | 2
  - 同じ表の列：Datum, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID, Wahllokal
- 例2 値：5 | 2 | 2 | 2 | 3
  - 同じ表の列：Datum, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, ID, Resultattyp

## g0084（1 列）
- 見出し：Titel
- 例1 値：«Stempelabgaben» | «Wirtschaftsabkommen Indonesien» | «Stimm- und Wahlrecht» | «Filmgesetz» | Änderung Zivildienstgesetz
  - 同じ表の列：Datum, Vorlage-ID, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID, Wahllokal

## g0085（1 列）
- 見出し：ID und Titel der Vorlage
- 例1 値：2: «Berufliche Vorsorge» | 1: «Liegenschaftssteuern» | 1: «Prämien-Entlastungs-Initiative» | 2: «Kriegsmaterial-Exporte» | 2: «Justiz-Initiative»
  - 同じ表の列：Datum, Vorlage-ID, Titel, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID, Wahllokal

## g0086（2 列）
- 見出し：Art der Vorlage
- 例1 値：national | kantonal | national | national | national
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Gemeinde-ID, Gemeinde, Wahllokal-ID, Wahllokal
- 例2 値：national | national | kantonal | national | national
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Gemeinde-ID, Gemeinde, ID, Resultattyp

## g0087（2 列）
- 見出し：Gemeinde-ID
- 例1 値：1 | 3 | 1 | 3 | 2
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde, Wahllokal-ID, Wahllokal
- 例2 値：9 | 9 | 1 | 2 | 3
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde, ID, Resultattyp

## g0089（1 列）
- 見出し：Wahllokal-ID
- 例1 値：15 | 15 | 21 | 20 | 30
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal

## g0090（1 列）
- 見出し：Wahllokal
- 例1 値：Basel brieflich Stimmende | Elektronisch Stimmende AS | Riehen briefl. & elektr. Stimmende (Tot… | Basel brieflich Stimmende | Basel brieflich Stimmende
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID

## g0091（2 列）
- 見出し：ID
- 例1 値：2021-09-26_01_11 | 2022-11-27_01_30 | 2025-09-28_02_23 | 2021-09-26_04_10 | 2021-09-26_03_21
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Wahllokal-ID
- 例2 値：2021-11-28_02_09 | 2022-02-13_01_09 | 2026-06-14_04_03 | 2022-09-25_03_01 | 2021-03-07_01_01
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, Resultattyp

## g0092（1 列）
- 見出し：Titel
- 例1 値：Klimafonds-Initiative | «Prämien-Entlastungs-Initiative» | «Transplantationsgesetz» | «Berufliche Vorsorge» | «13. AHV-Rente»
  - 同じ表の列：Datum, Vorlage-ID, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, ID, Resultattyp

## g0093（1 列）
- 見出し：ID und Titel der Vorlage
- 例1 値：3: «Zämme in Europa» | 1: «Klimagerechtigkeitsinitiative» und … | 1: «Gute-Luft-Initiative» | 2: Ernährungsinitiative | 4: «Parkgebühren»
  - 同じ表の列：Datum, Vorlage-ID, Titel, Art der Vorlage, Gemeinde-ID, Gemeinde, ID, Resultattyp

## g0095（1 列）
- 見出し：Resultattyp
- 例1 値：Schlussresultat | Schlussresultat | Schlussresultat | Schlussresultat | Schlussresultat
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, ID

## g0096（1 列）
- 見出し：Stimmberechtigte
- 例1 値：709 | 9066 | 786 | 755 | 90221
  - 同じ表の列：Datum, Vorlage-ID, Titel, ID und Titel der Vo…, Art der Vorlage, Gemeinde-ID, Gemeinde, ID

## g0097（1 列）
- 見出し：Verkehrsmittel
- 例1 値：Barrierefrei | Auto | Auto | Bus | Velo
  - 同じ表の列：Sperrung, ZusatzPP, Alt-Texte, Bildquellen

## g0098（1 列）
- 見出し：Sperrung
- 例1 値：False | False | False | True | True
  - 同じ表の列：Verkehrsmittel, ZusatzPP, Alt-Texte, Bildquellen

## g0099（1 列）
- 見出し：ZusatzPP
- 例1 値：False | True | False | False | False
  - 同じ表の列：Verkehrsmittel, Sperrung, Alt-Texte, Bildquellen

## g0100（1 列）
- 見出し：Alt-Texte
- 例1 値：Anreiseempfehlung für Autofahrer ohne S… | Anreiseempfehlung für Busreisende ohne … | Anreiseempfehlung für Autofahrer mit Sp… | Anreiseempfehlung für Autofahrer mit Sp… | Anreiseempfehlung für Tramreisende
  - 同じ表の列：Verkehrsmittel, Sperrung, ZusatzPP, Bildquellen

## g0101（1 列）
- 見出し：Bildquellen
- 例1 値：https://data-bs.ch/stata/kapo/eventverk… | https://data-bs.ch/stata/kapo/eventverk… | https://data-bs.ch/stata/kapo/eventverk… | https://data-bs.ch/stata/kapo/eventverk… | https://data-bs.ch/stata/kapo/eventverk…
  - 同じ表の列：Verkehrsmittel, Sperrung, ZusatzPP, Alt-Texte

## g0102（1 列）
- 見出し：abstimmung_uid
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：traktandum_uid, abstimmungsliste_st…, Übersicht vom

## g0103（1 列）
- 見出し：traktandum_uid
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：abstimmung_uid, abstimmungsliste_st…, Übersicht vom

## g0104（1 列）
- 見出し：abstimmungsliste_stimme
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：abstimmung_uid, traktandum_uid, Übersicht vom

## g0105（1 列）
- 見出し：Übersicht vom
- 例1 値：［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］ | ［個人別の記録のため削除］
  - 同じ表の列：abstimmung_uid, traktandum_uid, abstimmungsliste_st…

## g0106（1 列）
- 見出し：datum_vorstoss_eingang
- 例1 値：［個人別の記録のため削除］-01-23 | 2022-03-30 | ［個人別の記録のため削除］-08-30 | ［個人別の記録のため削除］-05-08 | 2023-03-01
  - 同じ表の列：registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0107（1 列）
- 見出し：registraturnummer
- 例1 値：2020/EA 46/111 | 2020/EA 13/47 | 20［個人別の記録のため削除］/EA 62/182 | 2020/MO 18/195 | 20［個人別の記録のため削除］/LM 2/190
  - 同じ表の列：datum_vorstoss_eing…, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0108（1 列）
- 見出し：nr_legislatur
- 例1 値：0421/20［個人別の記録のため削除］-2020/GR | 0288/20［個人別の記録のため削除］-20［個人別の記録のため削除］/GR | 0043/2020-2024/GR | 0329/20［個人別の記録のため削除］-20［個人別の記録のため削除］/GR | 0470/20［個人別の記録のため削除］-2020/GR
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0109（1 列）
- 見出し：grg_nr
- 例1 値：58 | 490 | 55 | 110 | 217
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0110（1 列）
- 見出し：vorstoss_bezeichnung
- 例1 値：Spassfahrten mit hochmotorisierten und … | Kriminalitätszunahme: Was tut der Kanto… | Stimmrechtsalter ［個人別の記録のため削除］ im Kanton Thurgau | Beteiligung der Politischen Gemeinden a… | Vollzugskonzept Qualitativer Bodenschut…
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0111（1 列）
- 見出し：vorstossart_bezeichnung
- 例1 値：Einfache Anfrage | Einfache Anfrage | Antrag nach § 52 bzw. § 46 der Geschäft… | Interpellation | Interpellation
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_code, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g01［個人別の記録のため削除］（1 列）
- 見出し：vorstossart_code
- 例1 値：5 | 2 | 5 | 5 | 4
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, sachbegriffe_grgeko…, sachbegriffe_grgeko…

## g0113（1 列）
- 見出し：sachbegriffe_grgeko_1
- 例1 値：17.7 Staatspersonal: einzelne Personale… | 85.0 Fürsorge, Massnahmen, Kinderheime,… | 14.2 Niederlassung, Aufenthalt, Asyl | 64.1 Staats- und Gemeindesteuern, allge… | 1［個人別の記録のため削除］ Gebiet, Organisation, Reglemente, …
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…

## g0114（1 列）
- 見出し：sachbegriffe_grgeko_2
- 例1 値：90.0 Wirtschaftliche Entwicklung | 73.2 Elektrizität inkl. Versorgung, Was… | ［個人別の記録のため削除］.2 Abstimmungen | 70.2 Baugesetz; Planungen Hoch- und Tie… | 74.1 Strassenverkehr, öffentlicher Verk…
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…

## g0115（1 列）
- 見出し：sachbegriffe_grgeko_3
- 例1 値：7［個人別の記録のため削除］ Allgemeines, Energiegesetz, Kernen… | 90.0 Wirtschaftliche Entwicklung | 70.1 Raumplanung, Richtpläne | 1［個人別の記録のため削除］ Gebiet, Organisation, Reglemente, …
  - 同じ表の列：datum_vorstoss_eing…, registraturnummer, nr_legislatur, grg_nr, vorstoss_bezeichnung, vorstossart_bezeich…, vorstossart_code, sachbegriffe_grgeko…

## g01［個人別の記録のため削除］（1 列）
- 見出し：VM-Nummer
- 例1 値：27 | 6［個人別の記録のため削除］ | 769 | 704 | 146
  - 同じ表の列：TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0117（1 列）
- 見出し：TU-Code
- 例1 値：11 | 11 | 11 | 11 | 11
  - 同じ表の列：VM-Nummer, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0118（1 列）
- 見出し：Variante
- 例1 値：101 | 102 | 111 | 109 | 101
  - 同じ表の列：VM-Nummer, TU-Code, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0119（1 列）
- 見出し：SJYID
- 例1 値：ch:1:sjyid:100001:66-005 | ch:1:sjyid:100001:13-002 | ch:1:sjyid:100001:717-001 | ch:1:sjyid:100001:74-002 | ch:1:sjyid:100001:40-001
  - 同じ表の列：VM-Nummer, TU-Code, Variante, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0［個人別の記録のため削除］0（1 列）
- 見出し：Abfahrt-BP-Nummer
- 例1 値：8507000 | 8507492 | 8500010 | 8507000 | 8509000
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0［個人別の記録のため削除］1（1 列）
- 見出し：Abfahrtsort
- 例1 値：Basel SBB | St. Gallen | Domodossola (I) | Basel SBB | Bregenz
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtszeit, Ankunft-BP-Nummer, Ankunftsort

## g0［個人別の記録のため削除］2（1 列）
- 見出し：Abfahrtszeit
- 例1 値：07:18 | 31:14 | 14:30 | 20:38 | 19:41
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Ankunft-BP-Nummer, Ankunftsort

## g0［個人別の記録のため削除］3（1 列）
- 見出し：Ankunft-BP-Nummer
- 例1 値：8503000 | 8301003 | 850［個人別の記録のため削除］09 | 8500010 | 8500090
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunftsort

## g0［個人別の記録のため削除］4（1 列）
- 見出し：Ankunftsort
- 例1 値：Basel Bad Bf | Basel SBB | Zürich HB | Feldkirch | Domodossola (I)
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer

## g0［個人別の記録のため削除］5（1 列）
- 見出し：Ankunftszeit
- 例1 値：18:13 | 09:53 | 20:23 | 11:52 | 11:29
  - 同じ表の列：VM-Nummer, TU-Code, Variante, SJYID, Abfahrt-BP-Nummer, Abfahrtsort, Abfahrtszeit, Ankunft-BP-Nummer

## g0［個人別の記録のため削除］6（1 列）
- 見出し：ID
- 例1 値：FK | SPB | KOM | SBF | OMB
  - 同じ表の列：Organisation_Kurzbe…, Direktion_Kurzbezei…, Dienststelle_Kurzbe…

## g0［個人別の記録のため削除］7（1 列）
- 見出し：Organisation_Kurzbezeichnung
- 例1 値：Stadt | Stadt | Stadt | Stadt | Stadt
  - 同じ表の列：ID, Direktion_Kurzbezei…, Dienststelle_Kurzbe…

## g0［個人別の記録のため削除］8（1 列）
- 見出し：Direktion_Kurzbezeichnung
- 例1 値：DPB | DIF | DSSI | DPB | BB
  - 同じ表の列：ID, Organisation_Kurzbe…, Dienststelle_Kurzbe…

## g0［個人別の記録のため削除］9（1 列）
- 見出し：Dienststelle_Kurzbezeichnung
- 例1 値：SF | ［個人別の記録のため削除］R | ［個人別の記録のため削除］SW | PD | ABB
  - 同じ表の列：ID, Organisation_Kurzbe…, Direktion_Kurzbezei…

## g0130（1 列）
- 見出し：PUBLISHER
- 例1 値：Oberjugendanwaltschaft des Kantons Züri… | Statistisches Amt des Kantons Zürich | Volksschulamt des Kantons Zürich | Stadt Uster | Gesundheitsdirektion des Kantons Zürich
  - 同じ表の列：ABTEI［個人別の記録のため削除］NG, PUBLISHER_SUFFIX

## g0131（1 列）
- 見出し：ABTEI［個人別の記録のため削除］NG
- 例1 値：Kantonale Denkmalpflege | Analysen & Studien | Kantonales Rechnungswesen | Geschäftsfeld Medizin, Abteilung Gesund… | Kantonales Labor
  - 同じ表の列：PUBLISHER, PUBLISHER_SUFFIX

## g0132（1 列）
- 見出し：PUBLISHER_SUFFIX
- 例1 値：stadt-uster | statistisches-amt-kanton-zuerich | stadt-winterthur | direktion-der-justiz-und-des-innern-kan… | aln-kanton-zuerich
  - 同じ表の列：PUBLISHER, ABTEI［個人別の記録のため削除］NG

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
g00［個人別の記録のため削除］	
g0013	
g0014	
g0015	
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
g0042	
g0043	
g0044	
g0045	
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
g0058	
g0061	
g0062	
g0063	
g0064	
g0065	
g0066	
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
g0083	
g0084	
g0085	
g0086	
g0087	
g0089	
g0090	
g0091	
g0092	
g0093	
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
g01［個人別の記録のため削除］	
g0113	
g0114	
g0115	
g01［個人別の記録のため削除］	
g0117	
g0118	
g0119	
g0［個人別の記録のため削除］0	
g0［個人別の記録のため削除］1	
g0［個人別の記録のため削除］2	
g0［個人別の記録のため削除］3	
g0［個人別の記録のため削除］4	
g0［個人別の記録のため削除］5	
g0［個人別の記録のため削除］6	
g0［個人別の記録のため削除］7	
g0［個人別の記録のため削除］8	
g0［個人別の記録のため削除］9	
g0130	
g0131	
g0132	
```
