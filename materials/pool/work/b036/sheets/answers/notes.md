# b036 S判定メモ

LABEL_GUIDE v2.0に従い、人物単位の記録は表全体を学習対象外（S）にした。

- **Tasmanian Immigration Records (1910-1940)**（g0134–g0136）：移民記録の個人・家族単位の項目。
- **Tasmanian Court Records (1824-1890)**（g0135、g0137–g0141）：個別の裁判記録。罪状、裁判日、PP_ID、判決などが一人・一件単位で並ぶ。
- **Obituaries indexed by State Library of WA**（g0188–g0195）：死亡者ごとの訃報記録。
- **In Memoriam Cards**（g0196–g0202）：故人・軍人ごとの追悼カード記録。

g0135（YEAR）は移民記録・裁判記録と集計表「Trade union membership and density by main job」に共通のグループID。シートのグループ分け上、同じIDには一つのラベルしか付けられないため、g0135全体をSにした。

ほかのS判定：
- **Public Trustee Financial Performance**（g0001–g0010）：項目名がデータ列に入り、残りの見出しが数値になっているため、表の構造が崩れている。
- **Change of Ownership Details for New and Second Hand Vehicles**（g0086–g0090）：区切り線・小計・見出しがデータ行に混在するクロス集計で、列として一貫していない。
- **Annual Food Act Report 2024-25**（g0164–g0165）：複数の小表の見出しが値に入り、「58」が列見出しになっているため、表の構造が崩れている。
