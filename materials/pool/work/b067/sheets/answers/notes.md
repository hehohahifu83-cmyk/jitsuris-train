# b067 除外メモ

- `https://ogd.parl.apps.be.ch/data/mitglied.csv`：州議会の議員1人ごとの名簿。人物単位の記録として表全体の列（corpus row 162–171、groups g0126–g0135）を `S` にした。
- `https://ogd.parl.apps.be.ch/data/interessenbindung.csv`：議員の個別の利害関係・任期・報酬等を記録する表。人物に結びつく個別記録として表全体の列（corpus row 172–181、groups g0136–g0145）を `S` にした。
- `Nr, Ort, Beschreibung, LV95 E, LV95 N, Standort, Bild` の表では `Standort` の値がすべて日付形式で列名と合わず、見出しと値の対応が壊れているため、その列だけ `S`（group g0296）にした。

ラベルは LABEL_GUIDE v2.3 と各シートの見出し・例・同表列を使い、モデル予測は参照していない。