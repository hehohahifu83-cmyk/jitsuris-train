# G1 の 1 回だけの測り（`research/g1/g1_eval.py`）

- 事前記録 `bench/g1_prereg_20261111.md`。採点 861 列（正解が unknown・S・other・person の列を除く）。
- 正解：先生 2 人（Claude・Codex）の独立のラベル（互いに SHA だけを連絡）の裁定。SHA-256 6b5679faff9d7a87ad2367bee637d4a26611853851889e106f367d245747b7a6。
- G1 は Alberta・Ontario・Berlin の 3 カタログだけ（英語・ドイツ語）。

| 形 | 正しい（平均） | 不明 | 重大（3 本の合計） | ほかの誤り | 種子ごとの正しい |
|---|---:|---:|---:|---:|---|
| L+G | 79.83% | 12.78% | 6 | 7.16% | 691・682・689 |
| L24+G | 80.29% | 12.47% | 6 | 7.01% | 697・689・688 |
| L24+G-V | 81.15% | 11.19% | 17 | 7.01% | 704・696・696 |

## 主：L24+G は L+G より悪くないか（公開元で引き直す）

- 正しいの差 +0.46、90% 区間 -0.13〜+1.04（下限が -1.0 より上か：○）
- 重大の差 +0（増えないか：○）
- ほかの誤りの差 -0.15（読むだけ）
- **判定：悪くない（L24 を土台のままにする）**

## 読むだけ：検査役を外した形（L24+G-V 対 L24+G）

- 正しいの差 +0.85、90% 区間 +0.25〜+1.63、重大の差 +11、ほかの誤りの差 +0.00

## 読むだけ：カタログごと

| 形 | Alberta | Ontario | Berlin | address→org | org→address |
|---|---:|---:|---:|---:|---:|
| L+G | 80.5%（311） | 81.9%（454） | 68.1%（96） | 1.7 | 1.3 |
| L24+G | 80.0%（311） | 82.8%（454） | 69.4%（96） | 0.7 | 1.7 |
| L24+G-V | 81.0%（311） | 83.0%（454） | 72.6%（96） | 0.7 | 1.7 |

### 公開元ごとの正しい（3 本の平均）

| 公開元 | 列 | L+G | L24+G |
|---|---:|---:|---:|
| ontario_cat:economic-development-job-creation-and-trade | 40 | 63.3% | 63.3% |
| ontario_cat:health | 34 | 97.1% | 97.1% |
| ontario_cat:education | 33 | 80.8% | 81.8% |
| ontario_cat:environment-conservation-and-parks | 33 | 78.8% | 83.8% |
| ontario_cat:treasury-board-secretariat | 30 | 88.9% | 90.0% |
| ontario_cat:colleges-universities-research-excellence-and-security | 30 | 72.2% | 71.1% |
| ontario_cat:transportation | 29 | 80.5% | 83.9% |
| ontario_cat:finance | 27 | 74.1% | 74.1% |
| ontario_cat:solicitor-general | 25 | 78.7% | 80.0% |
| alberta_cat:servicealberta | 23 | 100.0% | 97.1% |
| alberta_cat:education | 23 | 50.7% | 49.3% |
| berlin_cat:bezirksamt-lichtenberg | 22 | 66.7% | 68.2% |
| ontario_cat:energy-and-mines | 22 | 93.9% | 93.9% |
| ontario_cat:municipal-affairs-and-housing | 21 | 95.2% | 95.2% |
| ontario_cat:labour-immigration-training-and-skills-development | 20 | 95.0% | 95.0% |
| ontario_cat:infrastructure | 20 | 46.7% | 48.3% |
| berlin_cat:bezirksamt-tempelhof-schoneberg | 19 | 77.2% | 78.9% |
| berlin_cat:bezirksamt-marzahn-hellersdorf | 18 | 40.7% | 40.7% |
| alberta_cat:education-and-childcare | 18 | 83.3% | 81.5% |
| alberta_cat:jobsskillstrainingandlabour2013-2016 | 18 | 88.9% | 88.9% |
| alberta_cat:forestry-and-parks | 17 | 100.0% | 100.0% |
| ontario_cat:seniors-and-accessibility | 16 | 93.8% | 93.8% |
| ontario_cat:public-and-business-service-delivery-and-procurement | 16 | 93.8% | 91.7% |
| alberta_cat:assisted-living-and-social-services | 14 | 71.4% | 71.4% |
| ontario_cat:children-community-and-social-services | 12 | 83.3% | 86.1% |
| alberta_cat:humanservices | 12 | 86.1% | 91.7% |
| ontario_cat:agriculture-food-and-rural-affairs | 11 | 90.9% | 97.0% |
| alberta_cat:aboriginalrelations2008-2011-2013-2016 | 11 | 100.0% | 97.0% |
| alberta_cat:community-and-social-services | 10 | 100.0% | 100.0% |
| alberta_cat:municipalaffairs | 10 | 43.3% | 43.3% |
| berlin_cat:der-polizeiprasident-in-berlin | 10 | 60.0% | 63.3% |
| alberta_cat:treasuryboardandfinance | 10 | 60.0% | 60.0% |
| alberta_cat:tourism-and-sport | 9 | 44.4% | 48.1% |
| alberta_cat:technology-and-innovation | 9 | 92.6% | 88.9% |
| alberta_cat:mental-health-and-addictions | 9 | 100.0% | 100.0% |
| alberta_cat:public-safety-and-emergency-services | 9 | 92.6% | 88.9% |
| alberta_cat:labour-and-immigration | 9 | 44.4% | 44.4% |
| berlin_cat:senatsverwaltung-fur-wirtschaft-technologie-und-forschung | 8 | 75.0% | 75.0% |
| alberta_cat:children-and-family-services | 8 | 100.0% | 100.0% |
| alberta_cat:environment1971-1992--1999-2011 | 8 | 100.0% | 91.7% |
| alberta_cat:transportation | 8 | 100.0% | 100.0% |
| ontario_cat:natural-resources | 8 | 66.7% | 75.0% |
| ontario_cat:long-term-care | 8 | 100.0% | 100.0% |
| alberta_cat:agriculture-and-irrigation | 7 | 61.9% | 61.9% |
| alberta_cat:energy | 7 | 66.7% | 81.0% |
| alberta_cat:environmentalprotection1992-1999 | 7 | 42.9% | 42.9% |
| alberta_cat:jobs-economy-and-northern-development | 7 | 85.7% | 85.7% |
| berlin_cat:bezirksamt-reinickendorf | 7 | 95.2% | 100.0% |
| alberta_cat:economicdevelopmentandtrade | 6 | 100.0% | 100.0% |
| berlin_cat:senatsverwaltung-fur-mobilitat-verkehr-klimaschutz-und-umwelt | 6 | 83.3% | 83.3% |
| berlin_cat:bezirksamt-pankow | 6 | 83.3% | 83.3% |
| ontario_cat:sport | 5 | 80.0% | 80.0% |
| alberta_cat:labour | 5 | 100.0% | 100.0% |
| ontario_cat:cabinet-office | 5 | 100.0% | 100.0% |
| alberta_cat:infrastructure | 4 | 75.0% | 75.0% |
| alberta_cat:health | 4 | 83.3% | 75.0% |
| alberta_cat:jobs-economy-trade-and-immigration | 4 | 50.0% | 50.0% |
| alberta_cat:agricultureandruraldevelopment | 4 | 75.0% | 75.0% |
| alberta_cat:agricultureandforestry | 4 | 100.0% | 100.0% |
| alberta_cat:economic-development-trade-and-tourism | 4 | 100.0% | 91.7% |
| alberta_cat:cultureandtourism | 3 | 0.0% | 0.0% |
| alberta_cat:seniors2001-2004-2011-2012-2014-2016 | 3 | 100.0% | 100.0% |
| ontario_cat:attorney-general | 3 | 100.0% | 100.0% |
| alberta_cat:culture-multiculturalism-and-status-of-women | 3 | 100.0% | 100.0% |
| alberta_cat:transportation-and-economic-corridors | 2 | 100.0% | 100.0% |
| alberta_cat:children-s-services | 2 | 100.0% | 100.0% |
| ontario_cat:tourism-culture-and-gaming | 2 | 100.0% | 100.0% |
| ontario_cat:francophone-affairs | 2 | 100.0% | 100.0% |
| ontario_cat:citizenship-and-multiculturalism | 2 | 50.0% | 16.7% |

