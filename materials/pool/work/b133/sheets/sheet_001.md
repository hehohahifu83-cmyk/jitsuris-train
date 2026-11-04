# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（2 列）
- 見出し：nom_français
- 例1 値：nb_poisson | longueur_fourche_frais | maillage | no_poisson | taille
  - 同じ表の列：définition_français, english_definition, jeux_de_donnees_dat…
- 例2 値：nom_navire | type_longueur | longueur_totale_cong | poids_gonades_cong | age
  - 同じ表の列：définition_français, english_definition, jeux_de_donnees_dat…

## g0002（1 列）
- 見出し：définition_français
- 例1 値：Numéro du navire | Nombre de poissons mesurés | Type de longueur | Poids congelé du foie (g) | Résultat des opérations du trait
  - 同じ表の列：nom_français, english_definition, jeux_de_donnees_dat…

## g0003（1 列）
- 見出し：english_definition
- 例1 値：Age reading in years using otoliths | Longitude of the tow (DD) | A unique and stable taxon identifier gi… | Name of the ship | Ship number
  - 同じ表の列：nom_français, définition_français, jeux_de_donnees_dat…

## g0004（1 列）
- 見出し：jeux_de_donnees_data_set
- 例1 値：sentinel_fix_stations | sentinel_fix_stations | sentinel_fix_stations | sentinel_fix_stations | sentinel_fix_carbio
  - 同じ表の列：nom_français, définition_français, english_definition

## g0005（1 列）
- 見出し：définition_français
- 例1 値：Longueur à la fourche du spécimen frais… | Numéro de la strate | Distance chalutée (mille nautique) calc… | Numéro séquentiel du trait | Longueur à la fourche du spécimen conge…
  - 同じ表の列：nom_français, english_definition, jeux_de_donnees_dat…

## g0006（1 列）
- 見出し：english_definition
- 例1 値：Description of the stage of maturity | Identification of the source of informa… | Unique reference code for each species | Number of fish measured | Ship number
  - 同じ表の列：nom_français, définition_français, jeux_de_donnees_dat…

## g0007（1 列）
- 見出し：jeux_de_donnees_data_set
- 例1 値：mobile_freql | mobile_stations | mobile_stations | mobile_stations, mobile_captures_catche… | mobile_stations, mobile_captures_catche…
  - 同じ表の列：nom_français, définition_français, english_definition

## 答えの雛形

```
g0001	
g0002	
g0003	
g0004	
g0005	
g0006	
g0007	
```
