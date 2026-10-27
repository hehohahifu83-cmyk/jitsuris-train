# ラベル用シート 001 / 001

- LABEL_GUIDE v2.0 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_001.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0001（1 列）
- 見出し：text
- 例1 値：i d like to have this track onto my cla… | add the album to my flow español playli… | add digging now to my young at heart pl… | add this song by too poetic to my piano… | add this album to old school death metal
  - 同じ表の列：intent

## g0002（1 列）
- 見出し：intent
- 例1 値：AddToPlaylist | AddToPlaylist | AddToPlaylist | AddToPlaylist | AddToPlaylist
  - 同じ表の列：text

## g0003（1 列）
- 見出し：junior
- 例1 値：senior | junior | sophomore | senior | freshman
  - 同じ表の列：5, amazing school\curr…

## g0004（1 列）
- 見出し：5
- 例1 値：5 | 5 | 5 | 5 | 5
  - 同じ表の列：junior, amazing school\curr…

## g0005（1 列）
- 見出し：amazing school\current problem\very flexible\heavy\such notice\such short notic…
- 例1 値：amazing community\beautiful time\hard w… | great community | amazing community | liberal art education\amazing opportuni… | excellent sport program\beautiful campu…
  - 同じ表の列：junior, 5

## g0006（1 列）
- 見出し：act_tag
- 例1 値：sd | sd | sd | sd | sd
  - 同じ表の列：speaker, pos, text

## g0007（1 列）
- 見出し：speaker
- 例1 値：A | A | A | A | A
  - 同じ表の列：act_tag, pos, text

## g0008（1 列）
- 見出し：pos
- 例1 値：Well/UH ,/, the/DT weather/NN has/VBZ b… | and/CC it/PRP 's/HVS been/VBN humid/JJ … | I/PRP do/VBP n't/RB remember/VB a/DT ye… | well/UH ,/, it/PRP 's/BES not/RB really… | but/CC the/DT ,/, the/DT humidity/NN ha…
  - 同じ表の列：act_tag, speaker, text

## g0009（1 列）
- 見出し：text
- 例1 値：{D Well, } the weather [ has been, + ce… | {C and } it's been humid. / | I don't remember a year in a long time … | {D well, } it's not really late into th… | {C but } [ the, + the ] humidity has hu…
  - 同じ表の列：act_tag, speaker, pos

## g0010（1 列）
- 見出し：﻿is_rainy_day
- 例1 値：YES | YES | YES | YES | YES
  - 同じ表の列：Count, Day of Week, Time, total_votes, reviews_from_users, reviews_from_critics, num_of_movies_relea…, Year

## g0011（1 列）
- 見出し：Count
- 例1 値：20 | 143 | 150 | 177 | 52
  - 同じ表の列：﻿is_rainy_day, Day of Week, Time, total_votes, reviews_from_users, reviews_from_critics, num_of_movies_relea…, Year

## g0012（1 列）
- 見出し：Day of Week
- 例1 値：Saturday | Saturday | Saturday | Saturday | Saturday
  - 同じ表の列：﻿is_rainy_day, Count, Time, total_votes, reviews_from_users, reviews_from_critics, num_of_movies_relea…, Year

## g0013（1 列）
- 見出し：Time
- 例1 値：8:15pm | 8:00pm | 7:30pm | 7:00pm | 6:30pm
  - 同じ表の列：﻿is_rainy_day, Count, Day of Week, total_votes, reviews_from_users, reviews_from_critics, num_of_movies_relea…, Year

## g0014（1 列）
- 見出し：total_votes
- 例1 値：2707818 | 2707818 | 2707818 | 2707818 | 2707818
  - 同じ表の列：﻿is_rainy_day, Count, Day of Week, Time, reviews_from_users, reviews_from_critics, num_of_movies_relea…, Year

## g0015（1 列）
- 見出し：reviews_from_users
- 例1 値：14331 | 14331 | 14331 | 14331 | 14331
  - 同じ表の列：﻿is_rainy_day, Count, Day of Week, Time, total_votes, reviews_from_critics, num_of_movies_relea…, Year

## g0016（1 列）
- 見出し：reviews_from_critics
- 例1 値：12933 | 12933 | 12933 | 12933 | 12933
  - 同じ表の列：﻿is_rainy_day, Count, Day of Week, Time, total_votes, reviews_from_users, num_of_movies_relea…, Year

## g0017（1 列）
- 見出し：num_of_movies_released
- 例1 値：302 | 302 | 302 | 302 | 302
  - 同じ表の列：﻿is_rainy_day, Count, Day of Week, Time, total_votes, reviews_from_users, reviews_from_critics, Year

## g0018（1 列）
- 見出し：Year
- 例1 値：2009 | 2009 | 2009 | 2009 | 2009
  - 同じ表の列：﻿is_rainy_day, Count, Day of Week, Time, total_votes, reviews_from_users, reviews_from_critics, num_of_movies_relea…

## g0019（1 列）
- 見出し：avg_temp/F
- 例1 値：51 | 51 | 51 | 51 | 51
  - 同じ表の列：﻿is_rainy_day, Count, Day of Week, Time, total_votes, reviews_from_users, reviews_from_critics, num_of_movies_relea…

## g0020（1 列）
- 見出し：avg_spd_wind
- 例1 値：8.1 | 8.1 | 8.1 | 8.1 | 8.1
  - 同じ表の列：﻿is_rainy_day, Count, Day of Week, Time, total_votes, reviews_from_users, reviews_from_critics, num_of_movies_relea…

## g0021（1 列）
- 見出し：dir_wind
- 例1 値：280 | 280 | 280 | 280 | 280
  - 同じ表の列：﻿is_rainy_day, Count, Day of Week, Time, total_votes, reviews_from_users, reviews_from_critics, num_of_movies_relea…

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
```
