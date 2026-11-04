# ラベル用シート 001 / 001

- LABEL_GUIDE v2.4 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：LIC_NUM
- 例1 値：172 | 204 | 183 | 153 | 181
  - 同じ表の列：NTS, QUARTER, EFF_DATE, STATUS, PROJ_AREA, AREA_AC, AREA_HA, SOURCE

## g0002（1 列）
- 見出し：NTS
- 例1 値：039H04 | 049E11 | 059H16 | 049G13 | 039H03
  - 同じ表の列：LIC_NUM, QUARTER, EFF_DATE, STATUS, PROJ_AREA, AREA_AC, AREA_HA, SOURCE

## g0003（1 列）
- 見出し：QUARTER
- 例1 値：SW | NW | NW | SW | NE
  - 同じ表の列：LIC_NUM, NTS, EFF_DATE, STATUS, PROJ_AREA, AREA_AC, AREA_HA, SOURCE

## g0004（1 列）
- 見出し：EFF_DATE
- 例1 値：2008-06-05 | 2009-03-16 | 2011-06-01 | 2008-06-05 | 2008-06-05
  - 同じ表の列：LIC_NUM, NTS, QUARTER, STATUS, PROJ_AREA, AREA_AC, AREA_HA, SOURCE

## g0005（1 列）
- 見出し：STATUS
- 例1 値：Active | Active | Pending | Active | Active
  - 同じ表の列：LIC_NUM, NTS, QUARTER, EFF_DATE, PROJ_AREA, AREA_AC, AREA_HA, SOURCE

## g0006（1 列）
- 見出し：PROJ_AREA
- 例1 値：UTM 15 NAD83 | UTM 16 NAD83 | UTM 17 NAD83 | UTM 16 NAD83 | UTM 17 NAD83
  - 同じ表の列：LIC_NUM, NTS, QUARTER, EFF_DATE, STATUS, AREA_AC, AREA_HA, SOURCE

## g0007（1 列）
- 見出し：AREA_AC
- 例1 値：18194.48366914 | 33456.87692298 | 33611.19158433 | 33610.41379887 | 25040.54553417
  - 同じ表の列：LIC_NUM, NTS, QUARTER, EFF_DATE, STATUS, PROJ_AREA, AREA_HA, SOURCE

## g0008（1 列）
- 見出し：AREA_HA
- 例1 値：12029.674 | 10985.946 | 24844.126 | 13673.171 | 13099.706
  - 同じ表の列：LIC_NUM, NTS, QUARTER, EFF_DATE, STATUS, PROJ_AREA, AREA_AC, SOURCE

## g0009（1 列）
- 見出し：SOURCE
- 例1 値：AANDC - NRO | AANDC - NRO | AANDC - NRO | AANDC - NRO | AANDC - NRO
  - 同じ表の列：LIC_NUM, NTS, QUARTER, EFF_DATE, STATUS, PROJ_AREA, AREA_AC, AREA_HA

## g0010（1 列）
- 見出し：MAX_X_E
- 例1 値：-91.73322275467389 | -83.24708069960047 | -74.79504950683295 | -89.4999999995 | -83.23927303624046
  - 同じ表の列：LIC_NUM, NTS, QUARTER, EFF_DATE, STATUS, PROJ_AREA, AREA_AC, AREA_HA

## g0011（1 列）
- 見出し：Layer
- 例1 値：Horse Mussel / Modioles | Deep Pelagic / Pélagique profond | Benthic habitats /Habitats benthiques | Shallow Pelagic / Pélagique de faible p… | Benthic habitats /Habitats benthiques
  - 同じ表の列：Field

## g0012（1 列）
- 見出し：Field
- 例1 値：UNIT_ID | HabitatCODE | OBJECTID | Shape_Length | Shape
  - 同じ表の列：Layer

## g0013（1 列）
- 見出し：Layer / Couche
- 例1 値：NS_NB_Civic_Address | NS_NB_Watersheds | NS_NB_LandUse | NS_NB_Parks_ProtectedAreas | NS_NB_LandUse
  - 同じ表の列：Field / Champ

## g0014（1 列）
- 見出し：Field / Champ
- 例1 値：Watershed_ID / ID_du_bassin_versant | Biogeographic_Region / Région_biogéogra… | Biogeographic_Region / Région_biogéogra… | Biogeographic_Region / Région_biogéogra… | Area_ha / superficie_hectares
  - 同じ表の列：Layer / Couche

## g0015（1 列）
- 見出し：Year:2021-2022
- 例1 値：Year: 2019-2020 | Targeted Engagements Grants Funded | Rapid Response Provided | Collaborative Networks Launched | Collaborative Networks Launched
  - 同じ表の列：Total

## g0016（1 列）
- 見出し：Total
- 例1 値：3 | Total | 3 | 14 | Total
  - 同じ表の列：Year:2021-2022

## g0017（1 列）
- 見出し：Year/Annee
- 例1 値：2023 | 2024 | 2022 | 2022 | 2023
  - 同じ表の列：Geography/Region ge…, Age group/Groupe d'…, Gender/Genre, Take-up rate/Taux d…

## g0018（1 列）
- 見出し：Geography/Region geographique
- 例1 値：YT | NU | PE | NS | NS
  - 同じ表の列：Year/Annee, Age group/Groupe d'…, Gender/Genre, Take-up rate/Taux d…

## g0019（1 列）
- 見出し：Age group/Groupe d'age
- 例1 値：19-34 | 0-18 | 19-34 | 0-18 | 35-49
  - 同じ表の列：Year/Annee, Geography/Region ge…, Gender/Genre, Take-up rate/Taux d…

## g0020（1 列）
- 見出し：Gender/Genre
- 例1 値：2 | 2 | 1 | 2 | 2
  - 同じ表の列：Year/Annee, Geography/Region ge…, Age group/Groupe d'…, Take-up rate/Taux d…

## g0021（1 列）
- 見出し：Take-up rate/Taux de participation (%)
- 例1 値：22 | 39 | 35 | 41 | 23
  - 同じ表の列：Year/Annee, Geography/Region ge…, Age group/Groupe d'…, Gender/Genre

## g0022（1 列）
- 見出し：Stat-auth_Aut-leg_eng
- 例1 値：Canada disability savings grants | Payments to the Newfoundland offshore p… | Government's contribution to the Supple… | Government's contribution to the Death … | Government's contribution to the Canada…
  - 同じ表の列：Stat-auth_Aut-leg_f…, Entity_Entite_eng, Entity_Entite_fra, 2024/2025, 2023/2024, Amt-units_Mnt-unite

## g0023（1 列）
- 見出し：Stat-auth_Aut-leg_fra
- 例1 値：Fonds de la taxe sur l’essence | Transfert canadien en matière de santé … | Cotisation patronale du gouvernement au… | Contribution du gouvernement au régime … | Cotisation patronale du gouvernement au…
  - 同じ表の列：Stat-auth_Aut-leg_e…, Entity_Entite_eng, Entity_Entite_fra, 2024/2025, 2023/2024, Amt-units_Mnt-unite

## g0024（1 列）
- 見出し：Entity_Entite_eng
- 例1 値：Shared Services Canada | Canadian Forces | Public Service | Royal Canadian Mounted Police | Canadian Forces
  - 同じ表の列：Stat-auth_Aut-leg_e…, Stat-auth_Aut-leg_f…, Entity_Entite_fra, 2024/2025, 2023/2024, Amt-units_Mnt-unite

## g0025（1 列）
- 見出し：Entity_Entite_fra
- 例1 値：Fonction publique | Forces canadiennes | Fonction publique | Gendarmerie royale du Canada | Forces canadiennes
  - 同じ表の列：Stat-auth_Aut-leg_e…, Stat-auth_Aut-leg_f…, Entity_Entite_eng, 2024/2025, 2023/2024, Amt-units_Mnt-unite

## g0026（1 列）
- 見出し：2024/2025
- 例1 値：25253 | 502 | 28 | 430 | 3
  - 同じ表の列：Stat-auth_Aut-leg_e…, Stat-auth_Aut-leg_f…, Entity_Entite_eng, Entity_Entite_fra, 2023/2024, Amt-units_Mnt-unite

## g0027（1 列）
- 見出し：2023/2024
- 例1 値：26 | 483 | 10307 | 57445 | 4834
  - 同じ表の列：Stat-auth_Aut-leg_e…, Stat-auth_Aut-leg_f…, Entity_Entite_eng, Entity_Entite_fra, 2024/2025, Amt-units_Mnt-unite

## g0028（1 列）
- 見出し：Amt-units_Mnt-unite
- 例1 値：x1000000 | x1000000 | x1000000 | x1000000 | x1000000
  - 同じ表の列：Stat-auth_Aut-leg_e…, Stat-auth_Aut-leg_f…, Entity_Entite_eng, Entity_Entite_fra, 2024/2025, 2023/2024

## g0029（1 列）
- 見出し：Fscl-yr_Ex-fin
- 例1 値：2014/2015 | 2014/2015 | 2015/2016 | 2014/2015 | 2015/2016
  - 同じ表の列：Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Pymt-desc_Desc-paim…, Pymt-desc_Desc-paim…, Avail-auth-prev-FY_…, Auth-requested_Dep-…

## g0030（1 列）
- 見出し：Min-code
- 例1 値：17 | 16 | 08 | 14 | 13
  - 同じ表の列：Fscl-yr_Ex-fin, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Pymt-desc_Desc-paim…, Pymt-desc_Desc-paim…, Avail-auth-prev-FY_…, Auth-requested_Dep-…

## g0031（1 列）
- 見出し：Min-portfolio_Portefeuille-min_eng
- 例1 値：Canadian Heritage | Privy Council Office | National Defence | Natural Resources | Parliament
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Dept-nbr_No-min, Pymt-desc_Desc-paim…, Pymt-desc_Desc-paim…, Avail-auth-prev-FY_…, Auth-requested_Dep-…

## g0032（1 列）
- 見出し：Min-portfolio_Portefeuille-min_fra
- 例1 値：Affaires étrangères, Commerce et Dévelo… | Environnement | Bureau de l'infrastructure du Canada | Citoyenneté et Immigration | Anciens Combattants
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Dept-nbr_No-min, Pymt-desc_Desc-paim…, Pymt-desc_Desc-paim…, Avail-auth-prev-FY_…, Auth-requested_Dep-…

## g0033（1 列）
- 見出し：Dept-nbr_No-min
- 例1 値：061 | 018 | 074 | 005 | 042
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Pymt-desc_Desc-paim…, Pymt-desc_Desc-paim…, Avail-auth-prev-FY_…, Auth-requested_Dep-…

## g0034（1 列）
- 見出し：Pymt-desc_Desc-paimt_eng
- 例1 値：Contribution | Grant | Contribution | Grant | Contribution
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Pymt-desc_Desc-paim…, Avail-auth-prev-FY_…, Auth-requested_Dep-…

## g0035（1 列）
- 見出し：Pymt-desc_Desc-paimt_fra
- 例1 値：Contribution | Subvention | Contribution | Contribution | Subvention
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Pymt-desc_Desc-paim…, Avail-auth-prev-FY_…, Auth-requested_Dep-…

## g0036（1 列）
- 見出し：Avail-auth-prev-FY_Aut-disp-EF-prec
- 例1 値：0 | 0 | 0 | 0 | 600000
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Pymt-desc_Desc-paim…, Pymt-desc_Desc-paim…, Auth-requested_Dep-…

## g0037（1 列）
- 見出し：Auth-requested_Dep-demandees
- 例1 値：0 | 35167026 | 626146 | 40249710 | 8350000
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Pymt-desc_Desc-paim…, Pymt-desc_Desc-paim…, Avail-auth-prev-FY_…

## g0038（1 列）
- 見出し：Supl-amt-reqstd_Mnt-supl-demandee
- 例1 値：3000000 | 0 | 0 | 0 | 0
  - 同じ表の列：Fscl-yr_Ex-fin, Min-code, Min-portfolio_Porte…, Min-portfolio_Porte…, Dept-nbr_No-min, Pymt-desc_Desc-paim…, Pymt-desc_Desc-paim…, Avail-auth-prev-FY_…

## g0039（1 列）
- 見出し：Assigned National Safety Mark Code/ Code marque nationale de
- 例1 値：Z05 | X11 | X35 | Z71 | Z71
  - 同じ表の列：Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…

## g0040（1 列）
- 見出し：Class Type English/ Catégorie de classe Anglais
- 例1 値：Truck Body | Trailer | Truck Body | Truck Body | Truck Body
  - 同じ表の列：Assigned National S…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…

## g0041（1 列）
- 見出し：Class Type French/ Catégorie de classe Français
- 例1 値：Carrosserie de camion | Véhicule incomplet | Remorque | Véhicule incomplet | Carrosserie de camion
  - 同じ表の列：Assigned National S…, Class Type English/…, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…

## g0042（1 列）
- 見出し：Notes English/ Notes Anglais
- 例1 値：Fire truck | Importer for Britax, BOB products | All RIG equipped trailers are CMVSs 223… | Importer for Britax, BOB products | Importer for Britax, BOB products
  - 同じ表の列：Assigned National S…, Class Type English/…, Class Type French/ …, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…

## g0043（1 列）
- 見出し：Notes French/ Notes Français
- 例1 値：Toutes les remorques munies d'un dispos… | Importateur pour les products Britax, B… | Importateur pour les produits Apramo, K… | Toutes les remorques munies d'un dispos… | Fabrique des remorques servant à la déc…
  - 同じ表の列：Assigned National S…, Class Type English/…, Class Type French/ …, Notes English/ Note…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…

## g0044（1 列）
- 見出し：Location City/ Emplacement ville
- 例1 値：St. Catharines | Maidstone | Etobicoke | Mayerthorpe | Aylmer
  - 同じ表の列：Assigned National S…, Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location Province E…, Location Province F…, Location Country En…

## g0045（1 列）
- 見出し：Location Province English/ Emplacement province Anglais
- 例1 値：Quebec | Quebec | Quebec | Quebec | Manitoba
  - 同じ表の列：Assigned National S…, Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province F…, Location Country En…

## g0046（1 列）
- 見出し：Location Province French/ Emplacement province Français
- 例1 値：Ontario | Ontario | Ontario | Québec | Ontario
  - 同じ表の列：Assigned National S…, Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Country En…

## g0047（1 列）
- 見出し：Location Country English/ Emplacement pays Anglais
- 例1 値：CANADA | CANADA | CANADA | CANADA | CANADA
  - 同じ表の列：Assigned National S…, Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…

## g0048（1 列）
- 見出し：Location Country French/ Emplacement pays Français
- 例1 値：ÉTATS-UNIS | CANADA | CANADA | CANADA | CANADA
  - 同じ表の列：Assigned National S…, Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…

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
```
