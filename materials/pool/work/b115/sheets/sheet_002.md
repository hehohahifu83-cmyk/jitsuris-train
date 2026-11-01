# ラベル用シート 002 / 002

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Prog-core-resp-desc_Desc-prog-resp-essent_eng
- 例1 値：Internal Services are those groups of r… | Internal Services are those groups of r… | Internal Services are those groups of r… | Internal Services are those groups of r… | Internal Services are those groups of r…
  - 同じ表の列：Min-portfolio_Porte…, Min-portfolio_Porte…, Entity_Entite_eng, Entity_Entite_fra, Prog-core-resp-code…, Prog-core-resp-desc…, Prog-inv-code_Code-…, Notes_eng

## g0122（1 列）
- 見出し：Prog-core-resp-desc_Desc-prog-resp-essent_fra
- 例1 値：Les Services internes comprennent les g… | Les Services internes comprennent les g… | Les Services internes comprennent les g… | Les Services internes comprennent les g… | Les Services internes comprennent les g…
  - 同じ表の列：Min-portfolio_Porte…, Min-portfolio_Porte…, Entity_Entite_eng, Entity_Entite_fra, Prog-core-resp-code…, Prog-core-resp-desc…, Prog-inv-code_Code-…, Notes_eng

## g0123（1 列）
- 見出し：Prog-inv-code_Code-rep-prog
- 例1 値：BUN05 | BYP10 | BVH06 | BUJ07 | BWW08
  - 同じ表の列：Min-portfolio_Porte…, Min-portfolio_Porte…, Entity_Entite_eng, Entity_Entite_fra, Prog-core-resp-code…, Prog-core-resp-desc…, Prog-core-resp-desc…, Notes_eng

## g0124（1 列）
- 見出し：Notes_eng
- 例1 値：This department is not required to use … | This department is not required to use … | This department is not required to use … | This department is not required to use … | This department is not required to use …
  - 同じ表の列：Min-portfolio_Porte…, Min-portfolio_Porte…, Entity_Entite_eng, Entity_Entite_fra, Prog-core-resp-code…, Prog-core-resp-desc…, Prog-core-resp-desc…, Prog-inv-code_Code-…

## g0125（1 列）
- 見出し：Notes_fra
- 例1 値：Ce ministère n'a pas à ventiler les dép… | Ce ministère n'a pas à ventiler les dép… | Ce ministère n'a pas à ventiler les dép… | Ce ministère n'a pas à ventiler les dép… | Ce ministère n'a pas à ventiler les dép…
  - 同じ表の列：Min-portfolio_Porte…, Min-portfolio_Porte…, Entity_Entite_eng, Entity_Entite_fra, Prog-core-resp-code…, Prog-core-resp-desc…, Prog-core-resp-desc…, Prog-inv-code_Code-…

## g0126（1 列）
- 見出し：SubjectArea-eng
- 例1 値：Competence of testing laboratories | Security personnel | Competence of testing laboratories | Security personnel | Security personnel
  - 同じ表の列：SubjectArea-fra, StandardTitle-eng, StandardTitre-fra, Company-Compagnie, City-Ville, Province-code_Code-…, State_Province-eng, State_Province-fra

## g0127（1 列）
- 見出し：SubjectArea-fra
- 例1 値：La compétence des laboratoires d'essais | Personnel de sécurité | Fournitures de bureau | Fournitures de bureau | Personnel de sécurité
  - 同じ表の列：SubjectArea-eng, StandardTitle-eng, StandardTitre-fra, Company-Compagnie, City-Ville, Province-code_Code-…, State_Province-eng, State_Province-fra

## g0128（1 列）
- 見出し：StandardTitle-eng
- 例1 値：Security Officers and Security Officer … | Laboratory Acceptance | Security Officers and Security Officer … | Security Officers and Security Officer … | Remanufactured Toner Cartridges
  - 同じ表の列：SubjectArea-eng, SubjectArea-fra, StandardTitre-fra, Company-Compagnie, City-Ville, Province-code_Code-…, State_Province-eng, State_Province-fra

## g0129（1 列）
- 見出し：StandardTitre-fra
- 例1 値：D'acceptation des laboratoires | Cartouches de toner remises à neuf | Cartouches de toner remises à neuf | Agents de sécurité et superviseurs des … | Agents de sécurité et superviseurs des …
  - 同じ表の列：SubjectArea-eng, SubjectArea-fra, StandardTitle-eng, Company-Compagnie, City-Ville, Province-code_Code-…, State_Province-eng, State_Province-fra

## g0130（1 列）
- 見出し：Company-Compagnie
- 例1 値：Clover Technologies Canada, ULC | Unitex N.B. Company Ltd. | Element Materials Technology Canada Inc. | Ressource Laser Inc. | Garda Security Group Inc.
  - 同じ表の列：SubjectArea-eng, SubjectArea-fra, StandardTitle-eng, StandardTitre-fra, City-Ville, Province-code_Code-…, State_Province-eng, State_Province-fra

## g0131（1 列）
- 見出し：City-Ville
- 例1 値：Ilderton | Regina | Markham | Ottawa | Saskatoon
  - 同じ表の列：SubjectArea-eng, SubjectArea-fra, StandardTitle-eng, StandardTitre-fra, Company-Compagnie, Province-code_Code-…, State_Province-eng, State_Province-fra

## g0132（1 列）
- 見出し：Province-code_Code-de-province
- 例1 値：BC | ON | MB | ON | SK
  - 同じ表の列：SubjectArea-eng, SubjectArea-fra, StandardTitle-eng, StandardTitre-fra, Company-Compagnie, City-Ville, State_Province-eng, State_Province-fra

## g0133（1 列）
- 見出し：State_Province-eng
- 例1 値：Saskatchewan | Alberta | Nova Scotia | Ontario | Saskatchewan
  - 同じ表の列：SubjectArea-eng, SubjectArea-fra, StandardTitle-eng, StandardTitre-fra, Company-Compagnie, City-Ville, Province-code_Code-…, State_Province-fra

## g0134（1 列）
- 見出し：State_Province-fra
- 例1 値：Québec | Québec | Ontario | Ontario | Alberta
  - 同じ表の列：SubjectArea-eng, SubjectArea-fra, StandardTitle-eng, StandardTitre-fra, Company-Compagnie, City-Ville, Province-code_Code-…, State_Province-eng

## g0135（1 列）
- 見出し：Country-code_Code-de-pays
- 例1 値：MY | CA | CA | CA | CA
  - 同じ表の列：SubjectArea-eng, SubjectArea-fra, StandardTitle-eng, StandardTitre-fra, Company-Compagnie, City-Ville, Province-code_Code-…, State_Province-eng

## g0136（1 列）
- 見出し：StandardTitle-eng
- 例1 値：Designation of Yarns | Textile Test Methods - resistance to mi… | Textile Test Methods - Unidirectional E… | Heating Fuel Oil | Design, manufacture and use of large pa…
  - 同じ表の列：StandardTitre-fra, International-Base_…, Action, Edition_Édition, Stage_Stade, Stage-date_Date-du-…, Public-review-start…, Public-review-end_E…

## g0137（1 列）
- 見出し：StandardTitre-fra
- 例1 値：Formation et accréditation des observat… | Vitrage de Sécurité | Méthodes pour épreuves textiles – Résis… | Méthodes pour épreuves textiles – Laine… | Méthodes pour épreuves textiles – Mode …
  - 同じ表の列：StandardTitle-eng, International-Base_…, Action, Edition_Édition, Stage_Stade, Stage-date_Date-du-…, Public-review-start…, Public-review-end_E…

## g0138（1 列）
- 見出し：International-Base_Référence-inter-nationale
- 例1 値：ISO-3073 | ISO-2061 | ISO-105-B02 | ISO-2551 | ISO-14184-1
  - 同じ表の列：StandardTitle-eng, StandardTitre-fra, Action, Edition_Édition, Stage_Stade, Stage-date_Date-du-…, Public-review-start…, Public-review-end_E…

## g0139（1 列）
- 見出し：Action
- 例1 値：N* | w | ne | ne | ne
  - 同じ表の列：StandardTitle-eng, StandardTitre-fra, International-Base_…, Edition_Édition, Stage_Stade, Stage-date_Date-du-…, Public-review-start…, Public-review-end_E…

## g0140（1 列）
- 見出し：Edition_Édition
- 例1 値：2 | 4 | 13 | 4 | 4
  - 同じ表の列：StandardTitle-eng, StandardTitre-fra, International-Base_…, Action, Stage_Stade, Stage-date_Date-du-…, Public-review-start…, Public-review-end_E…

## g0141（1 列）
- 見出し：Stage_Stade
- 例1 値：60.6 | 20.98 | 60.6 | 95 | 60.6
  - 同じ表の列：StandardTitle-eng, StandardTitre-fra, International-Base_…, Action, Edition_Édition, Stage-date_Date-du-…, Public-review-start…, Public-review-end_E…

## g0142（1 列）
- 見出し：Stage-date_Date-du-stade
- 例1 値：2018-05-08 | 2018-05-08 | 2018-12-12 | 2019-01-15 | 2020-01-31
  - 同じ表の列：StandardTitle-eng, StandardTitre-fra, International-Base_…, Action, Edition_Édition, Stage_Stade, Public-review-start…, Public-review-end_E…

## g0143（1 列）
- 見出し：Public-review-start_Examen-publique-ouverture
- 例1 値：2019-01-16 | 2019-01-16 | 2018-12-12 | 2019-08-16 | 2018-08-02
  - 同じ表の列：StandardTitle-eng, StandardTitre-fra, International-Base_…, Action, Edition_Édition, Stage_Stade, Stage-date_Date-du-…, Public-review-end_E…

## g0144（1 列）
- 見出し：Public-review-end_Examen-publique-clôture
- 例1 値：2019-01-31 | 2019-01-31 | 2019-01-31 | 2019-01-31 | 2019-01-31
  - 同じ表の列：StandardTitle-eng, StandardTitre-fra, International-Base_…, Action, Edition_Édition, Stage_Stade, Stage-date_Date-du-…, Public-review-start…

## g0145（1 列）
- 見出し：Pub-target-date_Cible-de-publication
- 例1 値：2019-02-15 | 2019-02-15 | 2019-01-31 | 2019-02-15 | 2021-07-31
  - 同じ表の列：StandardTitle-eng, StandardTitre-fra, International-Base_…, Action, Edition_Édition, Stage_Stade, Stage-date_Date-du-…, Public-review-start…

## g0146（1 列）
- 見出し：Class Type English/ Catégorie de classe Anglais
- 例1 値：Trailer | Trailer | Truck Body | Trailer | Trailer
  - 同じ表の列：Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…, Location Country Fr…

## g0147（1 列）
- 見出し：Class Type French/ Catégorie de classe Français
- 例1 値：Voiture particulière | Remorque | Remorque | Remorque | Remorque
  - 同じ表の列：Class Type English/…, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…, Location Country Fr…

## g0148（1 列）
- 見出し：Notes English/ Notes Anglais
- 例1 値：All RIG equipped trailers are CMVSS 223… | Also have plants in Dallas, Oregon and … | Formerly Therm Dynamics | All RIG equipped trailers are CMVSS 223… | Also have a manufacturing plant in Gosh…
  - 同じ表の列：Class Type English/…, Class Type French/ …, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…, Location Country Fr…

## g0149（1 列）
- 見出し：Notes French/ Notes Français
- 例1 値：Il y a aussi une usine à Dallas, Oregon… | Il y a aussi une usine à Dallas, Oregon… | Toutes les remorques munies d'un dispos… | Cette compagnie fabrique des remorques … | Toutes les remorques équipées d'un disp…
  - 同じ表の列：Class Type English/…, Class Type French/ …, Notes English/ Note…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…, Location Country Fr…

## g0150（1 列）
- 見出し：Location City/ Emplacement ville
- 例1 値：Shipshewana | Fort Worth | Lafayette | Middlebury | St-Martin
  - 同じ表の列：Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location Province E…, Location Province F…, Location Country En…, Location Country Fr…

## g0151（1 列）
- 見出し：Location Province English/ Emplacement province Anglais
- 例1 値：Idaho | Texas | Texas | Indiana | Alabama
  - 同じ表の列：Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province F…, Location Country En…, Location Country Fr…

## g0152（1 列）
- 見出し：Location Province French/ Emplacement province Français
- 例1 値：Minnesota | Michigan | Indiana | Washington | Michigan
  - 同じ表の列：Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Country En…, Location Country Fr…

## g0153（1 列）
- 見出し：Location Country English/ Emplacement pays Anglais
- 例1 値：Ukraine | United States | China | United States | United States
  - 同じ表の列：Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country Fr…

## g0154（1 列）
- 見出し：Location Country French/ Emplacement pays Français
- 例1 値：États-Unis | États-Unis | États-Unis | États-Unis | États-Unis
  - 同じ表の列：Class Type English/…, Class Type French/ …, Notes English/ Note…, Notes French/ Notes…, Location City/ Empl…, Location Province E…, Location Province F…, Location Country En…

## 答えの雛形

```
g0121	
g0122	
g0123	
g0124	
g0125	
g0126	
g0127	
g0128	
g0129	
g0130	
g0131	
g0132	
g0133	
g0134	
g0135	
g0136	
g0137	
g0138	
g0139	
g0140	
g0141	
g0142	
g0143	
g0144	
g0145	
g0146	
g0147	
g0148	
g0149	
g0150	
g0151	
g0152	
g0153	
g0154	
```
