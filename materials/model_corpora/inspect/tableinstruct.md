# tableinstruct の点検（ファイルの形だけ）

- 出典：TableInstruct, Zhang et al. (TableLlama), osunlp/TableInstruct on Hugging Face
- ライセンス表示：CC-BY-4.0
- URL：https://huggingface.co/api/datasets/osunlp/TableInstruct/tree/main?recursive=true

## ファイル一覧（34 件）
- data_v3（0 bytes）
- eval_data（0 bytes）
- eval_data/in_domain_test（0 bytes）
- eval_data/in_domain_test/row_pop_test（0 bytes）
- eval_data/out_of_domain_test（0 bytes）
- .gitattributes（2350 bytes）
- README.md（2591 bytes）
- data_v3/col_pop_train_287916.json（217460051 bytes）
- data_v3/col_type_train_628254.json（5492365857 bytes）
- data_v3/ent_link_train_1264217.json（30111065647 bytes）
- data_v3/fetaqa_train_7325.json（15963683 bytes）
- data_v3/hitab_train_7417.json（16965026 bytes）
- data_v3/rel_extraction_train_62954.json（638894054 bytes）
- data_v3/row_pop_train_286396.json（1056760920 bytes）
- data_v3/tabfact_train_92283.json（156156441 bytes）
- eval_data/in_domain_test/col_pop_test.json（6049373 bytes）
- eval_data/in_domain_test/col_type_test.json（30208430 bytes）
- eval_data/in_domain_test/ent_link_test.json（63224287 bytes）
- eval_data/in_domain_test/fetaqa_test.json（6870735 bytes）
- eval_data/in_domain_test/hitab_test.json（6679333 bytes）
- eval_data/in_domain_test/rel_extraction_test.json（32504380 bytes）
- eval_data/in_domain_test/row_pop_test/part_0.json（791375 bytes）
- eval_data/in_domain_test/row_pop_test/part_1.json（768964 bytes）
- eval_data/in_domain_test/row_pop_test/part_2.json（721508 bytes）
- eval_data/in_domain_test/row_pop_test/part_3.json（782829 bytes）
- eval_data/in_domain_test/row_pop_test/part_4.json（744308 bytes）
- eval_data/in_domain_test/row_pop_test/part_5.json（669960 bytes）
- eval_data/in_domain_test/tabfact_test.json（37664458 bytes）
- eval_data/out_of_domain_test/feverous_eval.json（10019115 bytes）
- eval_data/out_of_domain_test/hybridqa_eval.json（7026415 bytes）
- eval_data/out_of_domain_test/kvret_test.json（1328160 bytes）
- eval_data/out_of_domain_test/totto_eval.json（6921686 bytes）
- eval_data/out_of_domain_test/wikisql_test.json（24666348 bytes）
- eval_data/out_of_domain_test/wikitq_test.json（8064571 bytes）

### data_v3/col_type_train_628254.json（先頭 4KB）
```
[
  {
    "instruction": "This is a column type annotation task. The goal for this task is to choose correct types for one selected column of the table from the given candidates. The Wikipedia page, section and table caption (if any) provide important information for choosing the correct column types.",
    "input_seg": "[TLE] The Wikipedia page is about Slovak parliamentary election, 1990. The Wikipedia section is about Results. [TAB] col: | party | votes | % | seats | row 1: | Public Against Violence | 991,285 | 29.35 | 48 | [SEP] row 2: | Christian Democratic Movement | 648,782 | 19.21 | 31 | [SEP] row 3: | Slovak National Party | 470,984 | 13.94 | 22 | [SEP] row 4: | Communist Party of Slovakia | 450,855 | 13.35 | 22 | [SEP] row 5: | Coexistence \u2013 Hungarian Christian Democratic Movement | 292,636 | 8.66 | 14 | [SEP] row 6: | Democratic Party | 148,567 | 4.40 | 7 | [SEP] row 7: | Party of Greens | 117,871 | 3.49 | 6 | [SEP] row 8: | Alliance of Farmers and the Countryside | 85,060 | 2.52 | 0 | [SEP] row 9: | Social Democracy | 61,401 | 1.82 | 0 | [SEP] row 10: | Freedom Party | 60,041 | 1.78 | 0 | [SEP] row 11: | R\u00f3movia | 24,797 | 0.73 | 0 | [SEP] row 12: | Movement of Czechoslovakian Understanding | 13,417 | 0.40 | 0 | [SEP] row 13: | People's Democratic Party\u2013Rally for the Republic | 7,023 | 0.21 | 0 | [SEP] row 14: | Free Bloc | 3,326 | 0.10 | 0 | [SEP] row 15: | Czechoslovakian Socialist Party | 1,166 | 0.03 | 0 | [SEP] row 16: | Czechoslovakian Democratic Forum | 515 | 0.02 | 0 | [SEP] row 17: | Invalid/blank votes | 77,925 | \u2013 | \u2013 | [SEP] row 18: | Total | 3,455,651 | 100 | 150 | [SEP] row 19: | Registered voters/turnout | 3,622,650 | 95.39 | \u2013 | [SEP] row 20: | Source: Statistics.sk | Source: Statistics.sk | Source: Statistics.sk | Source: Statistics.sk |",
    "question": "The column 'party' contains following entities: <Public Against Violence>, <Christian Democratic Movement>, <Slovak National Party>, <Communist Party of Slovakia>, <Coexistence \u2013 Hungarian Christian Democratic Movement>, <Democratic Party>, <Party of Greens>, <Freedom Party>, <Czechoslovakian Socialist Party>, etc. The column type candidates are: american_football.football_conference, tv.tv_writer, education.school, location.capital_of_administrative_division, tv.tv_series_season, rail.locomotive_class, interests.collection_category, book.book, food.food, metropolitan_transit.transit_stop, language.human_language, sports.sports_championship_event, music.artist, royalty.monarch, tv.tv_director, film.writer, sports.tournament_event_competition, sports.sports_league_draft, book.periodical, tv.tv_program, royalty.chivalric_order_member, sports.sports_award_winner, award.competition, theater.theater_actor, architecture.venue, broadcast.tv_channel, business.product_category, music.performance_role, geography.mountain, religion.religion, location.country, cvg.cvg_publisher, royalty.kingdom, education.educational_degree, celebrities.celebrity, exhibitions.exhibition_sponsor, education.university, award.award_discipline, location.in_district, broadcast.genre, olympics.olympic_event_competition, business.business_operation, film.film, organization.membership_organization, ice_hockey.hockey_player, automotive.model, broadcast.tv_station, cricket.cricket_player, music.record_label, boats.ship_class, music.genre, computer.computer, boats.ship, visual_art.visual_artist, organization.organization, olympics.olympic_games, location.admini
```

### eval_data/in_domain_test/col_type_test.json（先頭 4KB）
```
[
  {
    "table_id": "15221362-5",
    "instruction": "This is a column type annotation task. The goal for this task is to choose correct types for one selected column of the table from the given candidates. The Wikipedia page, section and table caption (if any) provide important information for choosing the correct column types.",
    "input": "[TLE] The Wikipedia page is about List of public sector undertakings in India. The Wikipedia section is about A5. [TAB] col: | s.no | company | incorporated | ministry | city | state | sector | group | ratna status | status | row 1: | 81 | Gail Gas Ltd. | 2008 | Ministry Of Petroleum & Natural Gas | New Delhi |  | Enterprises Under Construction |  |  |  | [SEP] row 2: | 82 | Garden Reach Shipbuilders & Engineers Ltd. | 1960 | Ministry Of Defence D/o Defence Production | Kolkata | West Bengal | Manufacturing | Transportation Equipment | Miniratna Category - I |  | [SEP] row 3: | 83 | Ghogarpalli Integrated Power Company Limited | 2009 | Ministry Of Power | New Delhi |  | Enterprises Under Construction |  |  |  | [SEP] row 4: | 84 | Goa Shipyard Ltd. | 1967 | Ministry Of Defence D/o Defence Production | Vasco Da Gama | Goa | Manufacturing | Transportation Equipment | Miniratna Category - I |  | [SEP] row 5: | 85 | Handicrafts & Handloom Exports Corp. Of India Ltd. | 1962 | Ministry Of Textiles |  |  | Services | Trading & Marketing |  |  | [SEP] row 6: | 86 | Heavy Engineering Corporation | 1958 | Ministry Of Heavy Industries & Public Enterprises D/o Heavy Industries |  | Jharkhand | Manufacturing | Heavy Engineering |  |  | [SEP] row 7: | 87 | Hindustan Aeronautics Ltd. | 1964 | Ministry Of Defence D/o Defence Production | Bangalore | Karnataka | Manufacturing | Transportation Equipment | Navratna |  | [SEP] row 8: | 88 | Hindustan Antibiotics Ltd. | 1954 | Ministry Of Chemicals & Fertilizers D/o Pharmaceuticals | Pune | Maharashtra | Manufacturing | Chemicals & Pharmaceuticals |  |  | [SEP] row 9: | 89 | Hindustan Cables Limited | 1972 | Ministry Of Heavy Industries & Public Enterprises D/o Heavy Industries | Kolkata | West Bengal | Manufacturing | Medium & Light Engineering |  |  | [SEP] row 10: | 90 | Hindustan Copper Limited | 1967 | Ministry Of Mines | Kolkata | West Bengal | Mining | Other Minerals & Metals | Miniratna Category - I |  | [SEP] row 11: | 91 | Hindustan Fertilizer Corporation Limited | 1978 | Ministry Of Chemicals & Fertilizers D/o Fertilizer |  |  | Manufacturing | Fertilizers |  |  | [SEP] row 12: | 92 | Hindustan Fluorocarbons Limited | 1983 | Ministry Of Chemicals & Fertilizers D/o Chemicals & Petrochemicals |  | Andhra Pradesh | Manufacturing | Chemicals & Pharmaceuticals |  |  | [SEP] row 13: | 93 | Hindustan Insecticides Ltd. | 1954 | Ministry Of Chemicals & Fertilizers D/o Chemicals & Petrochemicals |  |  | Manufacturing | Chemicals & Pharmaceuticals |  |  | [SEP] row 14: | 94 | Hindustan Newsprint Ltd. | 1982 | Ministry Of Heavy Industries & Public Enterprises D/o Heavy Industries |  | Kerala | Manufacturing | Consumer Goods | Miniratna Category - I |  | [SEP] row 15: | 95 | Hindustan Organic Chemicals Limited | 1960 | Ministry Of Chemicals & Fertilizers D/o Chemicals & Petrochemicals | Mumbai | Maharashtra | Manufacturing | Chemicals & Pharmaceuticals |  |  | [SEP] row 16: | 96 | Hindustan Paper Corporation | 1970 | Ministry Of Heavy Industries & Public Enterprises D/o Heavy Industries |  |  | Manufacturing | Consumer Goods | Miniratna Category - I |  | [SEP] row 17
```
