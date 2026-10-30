# ラベル用シート 002 / 003

- LABEL_GUIDE v2.3 だけで決める。予測は見ない。決められない列は unknown、表が崩れている・値が空の列は S
- 使えるラベル：account address amount category date email id org other person phone product quantity rate tax_class text unknown S
- 1 グループ＝見出しと値の形が同じ列のまとまり。グループの全部の列に同じラベルが付く。例が 2 つあるときは両方を見て決める
- 答え：末尾の「答えの雛形」を `answers/sheet_002.tsv` に写し、各行の TAB の後ろにラベルを 1 つ書く

## g0121（1 列）
- 見出し：Regime
- 例1 値：Fussgängerzone | Fussgängerzone | Fussgängerzone | Fussgängerzone | Fussgängerzone
  - 同じ表の列：Geo Point, Geo Shape, Fussgängerzonen-ID, Zum Objekt navigier…

## g0122（2 列）
- 見出し：Zum Objekt navigieren
- 例1 値：https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/…
  - 同じ表の列：Geo Point, Geo Shape, Fussgängerzonen-ID, Regime
- 例2 値：https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/… | https://opendatabs.github.io/map-links/…
  - 同じ表の列：Geo Point, Geo Shape, Objekt-ID, Infos, Zufahrt

## g0123（1 列）
- 見出し：Objekt-ID
- 例1 値：1 | 4 | 3 | 5 | 2
  - 同じ表の列：Geo Point, Geo Shape, Infos, Zufahrt, Zum Objekt navigier…

## g0124（1 列）
- 見出し：Infos
- 例1 値：https://www.bs.ch/themen/mobilitaet/fah… | https://www.bs.ch/themen/mobilitaet/fah… | https://www.bs.ch/themen/mobilitaet/fah… | https://www.bs.ch/themen/mobilitaet/fah… | https://www.bs.ch/themen/mobilitaet/fah…
  - 同じ表の列：Geo Point, Geo Shape, Objekt-ID, Zufahrt, Zum Objekt navigier…

## g0125（1 列）
- 見出し：Zufahrt
- 例1 値：https://www.bs.ch/themen/mobilitaet/fah… | https://www.bs.ch/themen/mobilitaet/fah… | https://www.bs.ch/themen/mobilitaet/fah… | https://www.bs.ch/themen/mobilitaet/fah… | https://www.bs.ch/themen/mobilitaet/fah…
  - 同じ表の列：Geo Point, Geo Shape, Objekt-ID, Infos, Zum Objekt navigier…

## g0126（1 列）
- 見出し：mitglied_sitznummer_vorhanden
- 例1 値：J | J | N | J | N
  - 同じ表の列：mitglied_partei_deu…, mitglied_partei_fra…, mitglied_wohnort, mitglied_beruf_deut…, mitglied_beruf_franz, mitglied_wahlkreis_…, mitglied_wahlkreis_…, mitglied_fraktion_d…

## g0127（1 列）
- 見出し：mitglied_partei_deutsch
- 例1 値：BDP | SVP | Die Mitte | GLP | FDP
  - 同じ表の列：mitglied_sitznummer…, mitglied_partei_fra…, mitglied_wohnort, mitglied_beruf_deut…, mitglied_beruf_franz, mitglied_wahlkreis_…, mitglied_wahlkreis_…, mitglied_fraktion_d…

## g0128（1 列）
- 見出し：mitglied_partei_franz
- 例1 値：Le Centre | PVL | PVL | PLR | PSA
  - 同じ表の列：mitglied_sitznummer…, mitglied_partei_deu…, mitglied_wohnort, mitglied_beruf_deut…, mitglied_beruf_franz, mitglied_wahlkreis_…, mitglied_wahlkreis_…, mitglied_fraktion_d…

## g0129（1 列）
- 見出し：mitglied_wohnort
- 例1 値：Gasel | Schönried | Rüschegg | Interlaken | Biel/Bienne
  - 同じ表の列：mitglied_sitznummer…, mitglied_partei_deu…, mitglied_partei_fra…, mitglied_beruf_deut…, mitglied_beruf_franz, mitglied_wahlkreis_…, mitglied_wahlkreis_…, mitglied_fraktion_d…

## g0130（1 列）
- 見出し：mitglied_beruf_deutsch
- 例1 値：Agronomingenieur HTL / Landwirt | Gemeinderat / Vorsteher Direktion Siche… | Unternehmer | Betriebswirtschafterin / Unternehmerin … | Geschäftsleiterin
  - 同じ表の列：mitglied_sitznummer…, mitglied_partei_deu…, mitglied_partei_fra…, mitglied_wohnort, mitglied_beruf_franz, mitglied_wahlkreis_…, mitglied_wahlkreis_…, mitglied_fraktion_d…

## g0131（1 列）
- 見出し：mitglied_beruf_franz
- 例1 値：secrétaire communale | agriculteur | agriculteur dipl. | chef de section | agriculteur dipl.
  - 同じ表の列：mitglied_sitznummer…, mitglied_partei_deu…, mitglied_partei_fra…, mitglied_wohnort, mitglied_beruf_deut…, mitglied_wahlkreis_…, mitglied_wahlkreis_…, mitglied_fraktion_d…

## g0132（1 列）
- 見出し：mitglied_wahlkreis_deutsch
- 例1 値：Mittelland-Nord | Thun | Emmental | Bern | Oberaargau
  - 同じ表の列：mitglied_sitznummer…, mitglied_partei_deu…, mitglied_partei_fra…, mitglied_wohnort, mitglied_beruf_deut…, mitglied_beruf_franz, mitglied_wahlkreis_…, mitglied_fraktion_d…

## g0133（1 列）
- 見出し：mitglied_wahlkreis_franz
- 例1 値：Jura bernois | Berne | Berne | Bienne-Seeland | Jura bernois
  - 同じ表の列：mitglied_sitznummer…, mitglied_partei_deu…, mitglied_partei_fra…, mitglied_wohnort, mitglied_beruf_deut…, mitglied_beruf_franz, mitglied_wahlkreis_…, mitglied_fraktion_d…

## g0134（1 列）
- 見出し：mitglied_fraktion_deutsch
- 例1 値：EDU | SVP | GLP | EVP | SVP
  - 同じ表の列：mitglied_sitznummer…, mitglied_partei_deu…, mitglied_partei_fra…, mitglied_wohnort, mitglied_beruf_deut…, mitglied_beruf_franz, mitglied_wahlkreis_…, mitglied_wahlkreis_…

## g0135（1 列）
- 見出し：mitglied_fraktion_franz
- 例1 値：PVL | UDC | UDC | UDF | PEV
  - 同じ表の列：mitglied_sitznummer…, mitglied_partei_deu…, mitglied_partei_fra…, mitglied_wohnort, mitglied_beruf_deut…, mitglied_beruf_franz, mitglied_wahlkreis_…, mitglied_wahlkreis_…

## g0136（1 列）
- 見出し：interessenbindung_typ
- 例1 値：B | A | B | A | B
  - 同じ表の列：interessenbindung_f…, interessenbindung_f…, interessenbindung_g…, interessenbindung_g…, interessenbindung_b…, interessenbindung_e…, interessenbindung_a…, interessenbindung_a…

## g0137（1 列）
- 見出し：interessenbindung_funktion_deutsch
- 例1 値：Mitglied | Präsidium | Präsidium | Mitglied | Mitglied
  - 同じ表の列：interessenbindung_t…, interessenbindung_f…, interessenbindung_g…, interessenbindung_g…, interessenbindung_b…, interessenbindung_e…, interessenbindung_a…, interessenbindung_a…

## g0138（1 列）
- 見出し：interessenbindung_funktion_franz
- 例1 値：Membre | Membre | Membre | Membre | Membre
  - 同じ表の列：interessenbindung_t…, interessenbindung_f…, interessenbindung_g…, interessenbindung_g…, interessenbindung_b…, interessenbindung_e…, interessenbindung_a…, interessenbindung_a…

## g0139（1 列）
- 見出し：interessenbindung_gremium_deutsch
- 例1 値：Stiftungsrat | Ausschuss | Industrie | Vorstand | Gemeindeexekutive
  - 同じ表の列：interessenbindung_t…, interessenbindung_f…, interessenbindung_f…, interessenbindung_g…, interessenbindung_b…, interessenbindung_e…, interessenbindung_a…, interessenbindung_a…

## g0140（1 列）
- 見出し：interessenbindung_gremium_franz
- 例1 値：Conseil d`administration | Comité directeur | Comité directeur | Autre | Conseil d`administration
  - 同じ表の列：interessenbindung_t…, interessenbindung_f…, interessenbindung_f…, interessenbindung_g…, interessenbindung_b…, interessenbindung_e…, interessenbindung_a…, interessenbindung_a…

## g0141（1 列）
- 見出し：interessenbindung_beginn_datum
- 例1 値：2026-06-01 | 2020-03-11 | 2019-11-11 | 2024-05-19 | 2025-06-01
  - 同じ表の列：interessenbindung_t…, interessenbindung_f…, interessenbindung_f…, interessenbindung_g…, interessenbindung_g…, interessenbindung_e…, interessenbindung_a…, interessenbindung_a…

## g0142（1 列）
- 見出し：interessenbindung_ende_datum
- 例1 値：2026-12-01 | 2026-12-01 | 2026-12-01 | 2026-05-30
  - 同じ表の列：interessenbindung_t…, interessenbindung_f…, interessenbindung_f…, interessenbindung_g…, interessenbindung_g…, interessenbindung_b…, interessenbindung_a…, interessenbindung_a…

## g0143（1 列）
- 見出し：interessenbindung_amtsbezogen_deutsch
- 例1 値：Von Amtes wegen | Von Amtes wegen | Von Amtes wegen | Von Amtes wegen | Von Amtes wegen
  - 同じ表の列：interessenbindung_t…, interessenbindung_f…, interessenbindung_f…, interessenbindung_g…, interessenbindung_g…, interessenbindung_b…, interessenbindung_e…, interessenbindung_a…

## g0144（1 列）
- 見出し：interessenbindung_amtsbezogen_franz
- 例1 値：Exercée d’office | Exercée d’office | Exercée d’office | Exercée d’office | Exercée d’office
  - 同じ表の列：interessenbindung_t…, interessenbindung_f…, interessenbindung_f…, interessenbindung_g…, interessenbindung_g…, interessenbindung_b…, interessenbindung_e…, interessenbindung_a…

## g0145（1 列）
- 見出し：interessenbindung_entschaedigung_deutsch
- 例1 値：Bezahlt | Bezahlt | Ehrenamtlich | Bezahlt | Ehrenamtlich
  - 同じ表の列：interessenbindung_t…, interessenbindung_f…, interessenbindung_f…, interessenbindung_g…, interessenbindung_g…, interessenbindung_b…, interessenbindung_e…, interessenbindung_a…

## g0146（1 列）
- 見出し：geschaeft_nr
- 例1 値：2021.RRGR.177 | 2021.RRGR.65 | 2014.RRGR.622 | 2014.GEF.11848 | 2016.RRGR.375
  - 同じ表の列：geschaeft_typ_deuts…, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0147（1 列）
- 見出し：geschaeft_typ_deutsch
- 例1 値：Motion | Interpellation | Ernennung / Wahl | Motion | Kreditgeschäft GR
  - 同じ表の列：geschaeft_nr, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0148（1 列）
- 見出し：geschaeft_typ_franz
- 例1 値：Loi | Interpellation | Interpellation | Affaire de crédit GC | Rapport de tiers
  - 同じ表の列：geschaeft_nr, geschaeft_typ_deuts…, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0149（1 列）
- 見出し：geschaeft_federfuehrung_kuerzel_deutsch
- 例1 値：BKD | GSI | GSI | SID | GSI
  - 同じ表の列：geschaeft_nr, geschaeft_typ_deuts…, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0150（1 列）
- 見出し：geschaeft_federfuehrung_kuerzel_franz
- 例1 値：INC | DIJ | INC | DTT | GC
  - 同じ表の列：geschaeft_nr, geschaeft_typ_deuts…, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0151（1 列）
- 見出し：geschaeft_vorberatende_kommission_uid
- 例1 値：1ea6c3cf0fde4b5283eb9dab423b160b | f2cb74be68324391a0ab07a565d1ce98 | da02607aa637486b91e4e64a34b77f06 | da02607aa637486b91e4e64a34b77f06 | da02607aa637486b91e4e64a34b77f06
  - 同じ表の列：geschaeft_nr, geschaeft_typ_deuts…, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0152（1 列）
- 見出し：geschaeft_vorberatende_kommission_deutsch
- 例1 値：Bau-, Energie-, Verkehrs- und Raumplanu… | Bildungskommission | Bau-, Energie-, Verkehrs- und Raumplanu… | Finanzkommission | Geschäftsprüfungskommission
  - 同じ表の列：geschaeft_nr, geschaeft_typ_deuts…, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0153（1 列）
- 見出し：geschaeft_vorberatende_kommission_franz
- 例1 値：Commission des finances | Commission des finances | Commission de justice | Commission des finances | Commission des finances
  - 同じ表の列：geschaeft_nr, geschaeft_typ_deuts…, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorstoss_…

## g0154（1 列）
- 見出し：geschaeft_vorstoss_hauptvorstoesser_uid
- 例1 値：e4a20569997f4846b3d067db6602593c | 32801908e1f74a449bdfd2628e8026e9 | f481a05c29844e2b8fe953312bd25f26 | e4a20569997f4846b3d067db6602593c | 78f163e7297343cf82b13f6173a04f62
  - 同じ表の列：geschaeft_nr, geschaeft_typ_deuts…, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorberate…

## g0155（1 列）
- 見出し：geschaeft_vorstoss_weitere_mitunterzeichner_anzahl
- 例1 値：0 | 0 | 0 | 0 | 25
  - 同じ表の列：geschaeft_nr, geschaeft_typ_deuts…, geschaeft_typ_franz, geschaeft_federfueh…, geschaeft_federfueh…, geschaeft_vorberate…, geschaeft_vorberate…, geschaeft_vorberate…

## g0156（1 列）
- 見出し：bfs_nummer
- 例1 値：3951 | 3781 | 3713 | 3847 | 3953
  - 同じ表の列：jahr, typ, betrag, gemeindestand, kategorie

## g0157（1 列）
- 見出し：typ
- 例1 値：Nettoschuld/-vermögen(-) je Einwohner i… | Investitionsanteil in % | Bruttoverschuldungsanteil in % | Bruttoverschuldungsanteil in % | Nettoschuld/-vermögen(-) je Einwohner i…
  - 同じ表の列：jahr, bfs_nummer, betrag, gemeindestand, kategorie

## g0158（1 列）
- 見出し：betrag
- 例1 値：-3050430.38 | -24123.52 | -2810.3 | 99.13 | 18.75
  - 同じ表の列：jahr, bfs_nummer, typ, gemeindestand, kategorie

## g0159（1 列）
- 見出し：gemeindestand
- 例1 値：2021-01-01 | 2021-01-01 | 2021-01-01 | 2021-01-01 | 2021-01-01
  - 同じ表の列：jahr, bfs_nummer, typ, betrag, kategorie

## g0160（1 列）
- 見出し：kategorie
- 例1 値：1. ideal > 100% | 1. ideal > 100% | 4. sehr stark > 30% | 1. schwach < 10% | 4. ungenügend < 50%
  - 同じ表の列：jahr, bfs_nummer, typ, betrag, gemeindestand

## g0161（1 列）
- 見出し：projekttragerschaft
- 例1 値：Gemeinde Disentis/Mustér | Gemeinde Laax | Nova Fundaziun Origen | Pendicularas Scuol SA | Stadthalle Chur AG
  - 同じ表の列：infrastruktur, gemeinde, geo_point

## g0162（1 列）
- 見出し：infrastruktur
- 例1 値：Heididorf Maienfeld | Baumwipfelpfad Laax | Biathlon Arena Lenzerheide | Landwasserwelt Graubünden | Sporthalle Färbi Davos
  - 同じ表の列：projekttragerschaft, gemeinde, geo_point

## g0163（3 列）
- 見出し：gemeinde
- 例1 値：Pontresina | Tujetsch | Arosa | Surses | Scuol
  - 同じ表の列：projekttragerschaft, infrastruktur, geo_point
- 例2 値：Winterthur | Winterthur | Winterthur | Winterthur | Winterthur
  - 同じ表の列：jahr, stichtag, gemeinde_bfs_nr, altersklasse, heimat, anzahl, anzahl_ist_kleingru…

## g0164（1 列）
- 見出し：geo_point
- 例1 値：46.6998577038841, 8.84528576935237 | 46.6923784361034, 9.55654847554976 | 46.8549502078628, 9.50525183143168 | 46.7837414170555, 9.81397212233962 | 46.7986066454662, 9.82642563332892
  - 同じ表の列：projekttragerschaft, infrastruktur, gemeinde

## g0165（1 列）
- 見出し：anlagenbezeichnung
- 例1 値：Roland Arena Lenzerheide | Leichtathletikanlage St. Moritz | Schwinghalle Rüfeli, Untervaz | Bob-Bahn St. Moritz-Celerina | Sporthalle Färbi Davos
  - 同じ表の列：traegerschaft, sportart, sportverband, anlagetyp, datum_aufnahme_in_d…, gemeinde, bfs_gemeindenummer, nasak_anlage_nation…

## g0166（1 列）
- 見出し：traegerschaft
- 例1 値：Kletterhalle AP’N DAUN GmbH und AXA Leb… | Corvatsch AG | Stadt Chur | Gemeinde St. Moritz | Gemeinde Davos
  - 同じ表の列：anlagenbezeichnung, sportart, sportverband, anlagetyp, datum_aufnahme_in_d…, gemeinde, bfs_gemeindenummer, nasak_anlage_nation…

## g0167（1 列）
- 見出し：sportart
- 例1 値：Curling | Ski alpin | Fussball | Schwingen | Klettern
  - 同じ表の列：anlagenbezeichnung, traegerschaft, sportverband, anlagetyp, datum_aufnahme_in_d…, gemeinde, bfs_gemeindenummer, nasak_anlage_nation…

## g0168（1 列）
- 見出し：sportverband
- 例1 値：Bündner Schwimmverband (vertreten durch… | Swiss-Ski | Bündner Unihockey Verband BUV | Swiss-Ski | Bündner Fussballverband BFV
  - 同じ表の列：anlagenbezeichnung, traegerschaft, sportart, anlagetyp, datum_aufnahme_in_d…, gemeinde, bfs_gemeindenummer, nasak_anlage_nation…

## g0169（1 列）
- 見出し：anlagetyp
- 例1 値：NASAK/KASAK (kantonale Bedeutung) | KASAK (kantonale Bedeutung) | KASAK (kantonale Bedeutung) | KASAK (regionale Bedeutung) | NASAK/KASAK (kantonale Bedeutung)
  - 同じ表の列：anlagenbezeichnung, traegerschaft, sportart, sportverband, datum_aufnahme_in_d…, gemeinde, bfs_gemeindenummer, nasak_anlage_nation…

## g0170（1 列）
- 見出し：datum_aufnahme_in_den_kasak_katalog
- 例1 値：2006-09-01 | 2024-08-20 | 2014-03-04 | 2012-08-21 | 2006-09-01
  - 同じ表の列：anlagenbezeichnung, traegerschaft, sportart, sportverband, anlagetyp, gemeinde, bfs_gemeindenummer, nasak_anlage_nation…

## g0171（1 列）
- 見出し：gemeinde
- 例1 値：Domat/Ems | Chur | Chur | St. Moritz | St. Moritz
  - 同じ表の列：anlagenbezeichnung, traegerschaft, sportart, sportverband, anlagetyp, datum_aufnahme_in_d…, bfs_gemeindenummer, nasak_anlage_nation…

## g0172（1 列）
- 見出し：bfs_gemeindenummer
- 例1 値：3901 | 3851 | 3575 | 3901 | 3582
  - 同じ表の列：anlagenbezeichnung, traegerschaft, sportart, sportverband, anlagetyp, datum_aufnahme_in_d…, gemeinde, nasak_anlage_nation…

## g0173（1 列）
- 見出し：nasak_anlage_nationale_bedeutung
- 例1 値：0 | 0 | 0 | 1 | 0
  - 同じ表の列：anlagenbezeichnung, traegerschaft, sportart, sportverband, anlagetyp, datum_aufnahme_in_d…, gemeinde, bfs_gemeindenummer

## g0174（1 列）
- 見出し：kasak_anlage_kantonale_bedeutung
- 例1 値：1 | 1 | 1 | 1 | 1
  - 同じ表の列：anlagenbezeichnung, traegerschaft, sportart, sportverband, anlagetyp, datum_aufnahme_in_d…, gemeinde, bfs_gemeindenummer

## g0175（1 列）
- 見出し：monat_jahr
- 例1 値：2026-09 | 2026-08 | 2026-08 | 2026-09 | 2026-06
  - 同じ表の列：jahr, monat, altersklasse, staat_d, kreis, quartiergruppe, anzahl

## g0176（1 列）
- 見出し：monat
- 例1 値：7 | 9 | 9 | 9 | 7
  - 同じ表の列：monat_jahr, jahr, altersklasse, staat_d, kreis, quartiergruppe, anzahl

## g0177（3 列）
- 見出し：altersklasse
- 例1 値：40-59 | 60-79 | 18-39 | 18-39 | 60-79
  - 同じ表の列：monat_jahr, jahr, monat, staat_d, kreis, quartiergruppe, anzahl
- 例2 値：20-24 | 90-94 | 30-34 | 60-64 | 25-29
  - 同じ表の列：jahr, stichtag, gemeinde_bfs_nr, gemeinde, heimat, anzahl, anzahl_ist_kleingru…

## g0178（1 列）
- 見出し：staat_d
- 例1 値：Ausland | Schweiz | Ausland | Ausland | Schweiz
  - 同じ表の列：monat_jahr, jahr, monat, altersklasse, kreis, quartiergruppe, anzahl

## g0179（1 列）
- 見出し：kreis
- 例1 値：Kreis Ost | Kreis Ost | Kreis Centrum | Kreis Centrum | Kreis Ost
  - 同じ表の列：monat_jahr, jahr, monat, altersklasse, staat_d, quartiergruppe, anzahl

## g0180（1 列）
- 見出し：quartiergruppe
- 例1 値：St.Fiden | Riethüsli | Rosenberg | St.Georgen | Riethüsli
  - 同じ表の列：monat_jahr, jahr, monat, altersklasse, staat_d, kreis, anzahl

## g0181（1 列）
- 見出し：bfsnr
- 例1 値：3203 | 3203 | 3203 | 3203 | 3203
  - 同じ表の列：datum, gemeinde, politischerkreis, quartiergruppen, altersklassen, teilgenommen, nicht_teilgenommen, stimmbeteiligung

## g0182（1 列）
- 見出し：gemeinde
- 例1 値：St.Gallen | St.Gallen | St.Gallen | St.Gallen | St.Gallen
  - 同じ表の列：datum, bfsnr, politischerkreis, quartiergruppen, altersklassen, teilgenommen, nicht_teilgenommen, stimmbeteiligung

## g0183（1 列）
- 見出し：politischerkreis
- 例1 値：unbekannt | Ost | Centrum | Centrum | West
  - 同じ表の列：datum, bfsnr, gemeinde, quartiergruppen, altersklassen, teilgenommen, nicht_teilgenommen, stimmbeteiligung

## g0184（1 列）
- 見出し：quartiergruppen
- 例1 値：25 | 13 | 31 | 23 | 13
  - 同じ表の列：datum, bfsnr, gemeinde, politischerkreis, altersklassen, teilgenommen, nicht_teilgenommen, stimmbeteiligung

## g0185（1 列）
- 見出し：altersklassen
- 例1 値：75+ | 25-34 | 18-24 | unbekannt | 18-24
  - 同じ表の列：datum, bfsnr, gemeinde, politischerkreis, quartiergruppen, teilgenommen, nicht_teilgenommen, stimmbeteiligung

## g0186（1 列）
- 見出し：teilgenommen
- 例1 値：181 | 50 | 165 | 120 | 84
  - 同じ表の列：datum, bfsnr, gemeinde, politischerkreis, quartiergruppen, altersklassen, nicht_teilgenommen, stimmbeteiligung

## g0187（1 列）
- 見出し：nicht_teilgenommen
- 例1 値：72 | 210 | 379 | 33 | 118
  - 同じ表の列：datum, bfsnr, gemeinde, politischerkreis, quartiergruppen, altersklassen, teilgenommen, stimmbeteiligung

## g0188（1 列）
- 見出し：stimmbeteiligung
- 例1 値：34.8 | 71.7 | 68.8 | 23.2 | 53.7
  - 同じ表の列：datum, bfsnr, gemeinde, politischerkreis, quartiergruppen, altersklassen, teilgenommen, nicht_teilgenommen

## g0189（1 列）
- 見出し：Geschäfts ID
- 例1 値：1490 | 6583 | 4050 | 5402 | 56
  - 同じ表の列：Komitee ID, Geschäftsnummer, Geschäftsart ID, Federführung ID, process_state_id, Eröffnung, Abschluss, letzte Änderung

## g0190（1 列）
- 見出し：Komitee ID
- 例1 値：468 | 468 | 468 | 468 | 468
  - 同じ表の列：Geschäfts ID, Geschäftsnummer, Geschäftsart ID, Federführung ID, process_state_id, Eröffnung, Abschluss, letzte Änderung

## g0191（1 列）
- 見出し：Geschäftsnummer
- 例1 値：61.13.37 | 22.07.06 | 32.15.01B | 12.11.02 | 51.19.107
  - 同じ表の列：Geschäfts ID, Komitee ID, Geschäftsart ID, Federführung ID, process_state_id, Eröffnung, Abschluss, letzte Änderung

## g0192（1 列）
- 見出し：Geschäftsart ID
- 例1 値：8 | 5 | 6 | 2 | 5
  - 同じ表の列：Geschäfts ID, Komitee ID, Geschäftsnummer, Federführung ID, process_state_id, Eröffnung, Abschluss, letzte Änderung

## g0193（1 列）
- 見出し：Federführung ID
- 例1 値：500 | 505 | 500 | 506 | 503
  - 同じ表の列：Geschäfts ID, Komitee ID, Geschäftsnummer, Geschäftsart ID, process_state_id, Eröffnung, Abschluss, letzte Änderung

## g0194（1 列）
- 見出し：process_state_id
- 例1 値：46 | 46 | 46 | 42 | 42
  - 同じ表の列：Geschäfts ID, Komitee ID, Geschäftsnummer, Geschäftsart ID, Federführung ID, Eröffnung, Abschluss, letzte Änderung

## g0195（1 列）
- 見出し：Eröffnung
- 例1 値：2016-06-13 | 2016-11-29 | 2013-03-04 | 2008-10-14 | 2016-04-25
  - 同じ表の列：Geschäfts ID, Komitee ID, Geschäftsnummer, Geschäftsart ID, Federführung ID, process_state_id, Abschluss, letzte Änderung

## g0196（1 列）
- 見出し：Abschluss
- 例1 値：2012-04-24 | 2016-02-29 | 2012-04-24 | 2019-01-15 | 2016-04-26
  - 同じ表の列：Geschäfts ID, Komitee ID, Geschäftsnummer, Geschäftsart ID, Federführung ID, process_state_id, Eröffnung, letzte Änderung

## g0197（1 列）
- 見出し：letzte Änderung
- 例1 値：2025-02-25T23:06:01+00:00 | 2025-02-24T17:18:14+00:00 | 2025-02-24T17:06:24+00:00 | 2025-02-24T16:54:30+00:00 | 2025-02-26T07:14:55+00:00
  - 同じ表の列：Geschäfts ID, Komitee ID, Geschäftsnummer, Geschäftsart ID, Federführung ID, process_state_id, Eröffnung, Abschluss

## g0198（1 列）
- 見出し：Geschäftsart
- 例1 値：KR Interpellation | KR Einfache Anfrage | KR Motion | KR Verwaltungsgeschäft | KR Verwaltungsgeschäft
  - 同じ表の列：Geschäfts ID, Komitee ID, Geschäftsnummer, Geschäftsart ID, Federführung ID, process_state_id, Eröffnung, Abschluss

## g0199（1 列）
- 見出し：datum_geschaeft_eingang
- 例1 値：2009-03-11 | 1997-04-23 | 2023-03-22 | 2026-04-29 | 2005-03-23
  - 同じ表の列：datum_geschaeft_abs…, geschaeftsnummer, grg_nummer, geschaftstitel, geschaftsart, kennung, sachbegriff_grgeko_1, status

## g0200（1 列）
- 見出し：datum_geschaeft_abschluss
- 例1 値：2005-06-08 | 1995-04-26 | 2009-06-03 | 2020-01-22 | 2011-06-29
  - 同じ表の列：datum_geschaeft_ein…, geschaeftsnummer, grg_nummer, geschaftstitel, geschaftsart, kennung, sachbegriff_grgeko_1, status

## g0201（1 列）
- 見出し：geschaeftsnummer
- 例1 値：04/WA 18/175 | 20/EA 211/515 | 04/BS 8/115 | 00/IN 66/324 | 16/EA 25/82
  - 同じ表の列：datum_geschaeft_ein…, datum_geschaeft_abs…, grg_nummer, geschaftstitel, geschaftsart, kennung, sachbegriff_grgeko_1, status

## g0202（1 列）
- 見出し：grg_nummer
- 例1 値：328 | 21 | 62 | 127 | 240
  - 同じ表の列：datum_geschaeft_ein…, datum_geschaeft_abs…, geschaeftsnummer, geschaftstitel, geschaftsart, kennung, sachbegriff_grgeko_1, status

## g0203（1 列）
- 見出し：geschaftstitel
- 例1 値：Kantonsbürgerrechtsgesuche per 23. Mai … | Ersatzwahl von zwei Mitgliedern der Jus… | Interpellation von Carmen Haag vom 12. … | Beschluss betreffend Genehmigung der "Ä… | Motion Ruth Mettler und Ernst Ritzi gem…
  - 同じ表の列：datum_geschaeft_ein…, datum_geschaeft_abs…, geschaeftsnummer, grg_nummer, geschaftsart, kennung, sachbegriff_grgeko_1, status

## g0204（1 列）
- 見出し：geschaftsart
- 例1 値：Antrag nach § 52 bzw. § 46 der Geschäft… | Beschluss | Motion | Gesetz | Einfache Anfrage
  - 同じ表の列：datum_geschaeft_ein…, datum_geschaeft_abs…, geschaeftsnummer, grg_nummer, geschaftstitel, kennung, sachbegriff_grgeko_1, status

## g0205（1 列）
- 見出し：kennung
- 例1 値：IN | BS | EA | IN | IN
  - 同じ表の列：datum_geschaeft_ein…, datum_geschaeft_abs…, geschaeftsnummer, grg_nummer, geschaftstitel, geschaftsart, sachbegriff_grgeko_1, status

## g0206（1 列）
- 見出し：sachbegriff_grgeko_1
- 例1 値：PTT, Radio, Fernsehen etc. | Niederlassung, Aufenthalt, Asyl | 85.0 Fürsorge, Massnahmen, Kinderheime,… | 64.1 Staats- und Gemeindesteuern, allge… | 41.2 Oberstufen: Real- und Sekundarschu…
  - 同じ表の列：datum_geschaeft_ein…, datum_geschaeft_abs…, geschaeftsnummer, grg_nummer, geschaftstitel, geschaftsart, kennung, status

## g0207（1 列）
- 見出し：zustaendigkeit
- 例1 値：Departement für Justiz und Sicherheit | Departement für Finanzen und Soziales | Departement für Finanzen und Soziales | Departement für Inneres und Volkswirtsc… | Departement für Finanzen und Soziales
  - 同じ表の列：datum_geschaeft_ein…, datum_geschaeft_abs…, geschaeftsnummer, grg_nummer, geschaftstitel, geschaftsart, kennung, sachbegriff_grgeko_1

## g0208（1 列）
- 見出し：startzeit
- 例1 値：2026-06-30T11:00:00+00:00 | 2026-06-29T08:00:00+00:00 | 2026-06-29T07:00:00+00:00 | 2026-07-05T00:00:00+00:00 | 2026-06-30T03:00:00+00:00
  - 同じ表の列：endzeit, messstelle, messwert, messstationId, indikator

## g0209（1 列）
- 見出し：endzeit
- 例1 値：2026-07-01T20:00:00+00:00 | 2026-07-04T12:00:00+00:00 | 2026-06-29T16:00:00+00:00 | 2026-07-02T02:00:00+00:00 | 2026-06-30T12:00:00+00:00
  - 同じ表の列：startzeit, messstelle, messwert, messstationId, indikator

## g0210（1 列）
- 見出し：messstelle
- 例1 値：Konstanz, Wallgutstrasse | Weinfelden, Berufsbildungszentrum | Weinfelden, Berufsbildungszentrum | Weinfelden, Berufsbildungszentrum | Konstanz, Wallgutstrasse
  - 同じ表の列：startzeit, endzeit, messwert, messstationId, indikator

## g0211（1 列）
- 見出し：messwert
- 例1 値：2.7 | 0.53 | 18.89 | 0.23 | 6.61
  - 同じ表の列：startzeit, endzeit, messstelle, messstationId, indikator

## g0212（1 列）
- 見出し：messstationId
- 例1 値：8afbe850-6268-4c59-aa29-8405e7b6da6b | 8afbe850-6268-4c59-aa29-8405e7b6da6b | 9fc10577-4551-49aa-9ebc-2a882720c0ac | 9fc10577-4551-49aa-9ebc-2a882720c0ac | 9fc10577-4551-49aa-9ebc-2a882720c0ac
  - 同じ表の列：startzeit, endzeit, messstelle, messwert, indikator

## g0213（1 列）
- 見出し：indikator
- 例1 値：Stickstoffdioxid | Lufttemperatur | Stickstoffmonoxid | Ozon | Ozon
  - 同じ表の列：startzeit, endzeit, messstelle, messwert, messstationId

## g0214（1 列）
- 見出し：zeit_von
- 例1 値：2026-02-11T21:00:00+00:00 | 2025-12-08T05:00:00+00:00 | 2026-02-03T07:00:00+00:00 | 2026-02-04T08:00:00+00:00 | 2026-02-11T01:00:00+00:00
  - 同じ表の列：zeit_bis, belegung, inflow, outflow, median_standzeit, koordinaten

## g0215（1 列）
- 見出し：zeit_bis
- 例1 値：2026-02-12T23:00:00+00:00 | 2026-02-09T19:00:00+00:00 | 2025-12-25T11:00:00+00:00 | 2026-02-06T20:00:00+00:00 | 2026-02-05T03:00:00+00:00
  - 同じ表の列：zeit_von, belegung, inflow, outflow, median_standzeit, koordinaten

## g0216（1 列）
- 見出し：belegung
- 例1 値：22.38 | 75.08 | 92.03 | 40.27 | 19.24
  - 同じ表の列：zeit_von, zeit_bis, inflow, outflow, median_standzeit, koordinaten

## g0217（1 列）
- 見出し：inflow
- 例1 値：3 | 0 | 36 | 0 | 4
  - 同じ表の列：zeit_von, zeit_bis, belegung, outflow, median_standzeit, koordinaten

## g0218（1 列）
- 見出し：outflow
- 例1 値：0 | 23 | 9 | 4 | 29
  - 同じ表の列：zeit_von, zeit_bis, belegung, inflow, median_standzeit, koordinaten

## g0219（1 列）
- 見出し：median_standzeit
- 例1 値：8161.0 | 39364.0 | 3331.0 | 4471.0 | 6421.0
  - 同じ表の列：zeit_von, zeit_bis, belegung, inflow, outflow, koordinaten

## g0220（2 列）
- 見出し：sloid
- 例1 値：ch:1:sloid:1075:696003 | ch:1:sloid:9255:91025 | ch:1:sloid:2103:618778 | ch:1:sloid:1300:26384 | ch:1:sloid:4550:867514
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validFrom, validTo
- 例2 値：ch:1:sloid:5541:286372 | ch:1:sloid:3227:822663 | ch:1:sloid:195:919334 | ch:1:sloid:24:271318 | ch:1:sloid:4302:906555
  - 同じ表の列：parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0221（2 列）
- 見出し：parentSloidServicePoint
- 例1 値：ch:1:sloid:7166 | ch:1:sloid:1215 | ch:1:sloid:1210 | ch:1:sloid:1157 | ch:1:sloid:1164
  - 同じ表の列：sloid, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validFrom, validTo
- 例2 値：ch:1:sloid:30635 | ch:1:sloid:8051 | ch:1:sloid:4301 | ch:1:sloid:6138 | ch:1:sloid:7100
  - 同じ表の列：sloid, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0222（2 列）
- 見出し：parentNumberServicePoint
- 例1 値：8504300 | 8506123 | 8500218 | 8503424 | 8501075
  - 同じ表の列：sloid, parentSloidServiceP…, type, designation, inductionLoop, wheelchairAccess, validFrom, validTo
- 例2 値：8500181 | 8500027 | 8501398 | 8503315 | 8508053
  - 同じ表の列：sloid, parentSloidServiceP…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0223（1 列）
- 見出し：type
- 例1 値：TICKET_COUNTER | TICKET_COUNTER | TICKET_COUNTER | TICKET_COUNTER | TICKET_COUNTER
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, inductionLoop, wheelchairAccess, validFrom, validTo

## g0224（1 列）
- 見出し：designation
- 例1 値：Stationsgebäude | Billettschalter | Billettschalter | Wirtshaus Zur Schifflände | Billettschalter
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, inductionLoop, wheelchairAccess, validFrom, validTo

## g0225（1 列）
- 見出し：inductionLoop
- 例1 値：PARTIALLY | NO | YES | NO | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, wheelchairAccess, validFrom, validTo

## g0226（1 列）
- 見出し：wheelchairAccess
- 例1 値：YES | YES | NOT_APPLICABLE | YES | NOT_APPLICABLE
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, validFrom, validTo

## g0227（3 列）
- 見出し：validFrom
- 例1 値：2021-10-06T00:00:00 | 2023-09-07T00:00:00 | 2024-06-17T00:00:00 | 2021-07-21T00:00:00 | 2021-07-21T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validTo
- 例2 値：2005-07-01T00:00:00 | 2017-01-01T00:00:00 | 2012-08-17T00:00:00 | 2015-12-13T00:00:00 | 2025-09-01T00:00:00
  - 同じ表の列：slnid, linienId, validTo, status, lineType, concessionType, swissLineNumber, number

## g0228（3 列）
- 見出し：validTo
- 例1 値：9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00 | 9999-12-31T00:00:00
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validFrom
- 例2 値：2033-05-31T00:00:00 | 2049-06-30T00:00:00 | 2035-07-31T00:00:00 | 2027-12-10T00:00:00 | 2029-12-08T00:00:00
  - 同じ表の列：slnid, linienId, validFrom, status, lineType, concessionType, swissLineNumber, number

## g0229（2 列）
- 見出し：creationDate
- 例1 値：2022-07-28T21:47:38 | 2023-10-31T15:05:27 | 2022-04-07T06:44:42 | 2022-07-25T08:26:16 | 2021-02-13T14:12:55
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, type, designation, inductionLoop, wheelchairAccess, validFrom
- 例2 値：2022-04-13T19:11:53 | 2023-03-09T13:10:10 | 2023-02-09T14:06:02 | 2021-12-06T08:16:39 | 2022-12-22T07:20:29
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom

## g0230（1 列）
- 見出し：slnid
- 例1 値：ch:1:slnid:1025013 | ch:1:slnid:1025361 | ch:1:slnid:1024416 | ch:1:slnid:1024328 | ch:1:slnid:1024534
  - 同じ表の列：linienId, validFrom, validTo, status, lineType, concessionType, swissLineNumber, number

## g0231（1 列）
- 見出し：linienId
- 例1 値：ch:1:Line:876:208 | ch:1:Line:100122:48 | ch:1:Line:876:210 | ch:1:Line:100122:64 | ch:1:Line:876:202
  - 同じ表の列：slnid, validFrom, validTo, status, lineType, concessionType, swissLineNumber, number

## g0232（1 列）
- 見出し：lineType
- 例1 値：ORDERLY | ORDERLY | ORDERLY | ORDERLY | ORDERLY
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, concessionType, swissLineNumber, number

## g0233（1 列）
- 見出し：concessionType
- 例1 値：FEDERALLY_LICENSED_OR_APPROVED_LINE | FEDERALLY_LICENSED_OR_APPROVED_LINE | FEDERALLY_LICENSED_OR_APPROVED_LINE | FEDERALLY_LICENSED_OR_APPROVED_LINE | FEDERALLY_LICENSED_OR_APPROVED_LINE
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, lineType, swissLineNumber, number

## g0234（1 列）
- 見出し：swissLineNumber
- 例1 値：b9.RE4 | n.3154 | n.3210 | f.22818 | f.21062
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, lineType, concessionType, number

## g0235（1 列）
- 見出し：number
- 例1 値：2300 | 25983 | 3900 | 2272 | 27801
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, lineType, concessionType, swissLineNumber

## g0236（1 列）
- 見出し：shortNumber
- 例1 値：6 | 3 | 13 | 70 | 13
  - 同じ表の列：slnid, linienId, validFrom, validTo, status, lineType, concessionType, swissLineNumber

## g0237（1 列）
- 見出し：designation
- 例1 値：Parking | Parkplätze | Parking | Parkplatz | Parking
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, additionalInformati…, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0238（1 列）
- 見出し：additionalInformation
- 例1 値：6 places | 72 / 2 Parkplätze | 68 / 2 Parkplätze | 8 / 1 Parkplätze | 16 / 1 Parkplätze
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, placesAvailable, prmPlacesAvailable, validFrom, validTo

## g0239（1 列）
- 見出し：placesAvailable
- 例1 値：YES | YES | YES | YES | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, prmPlacesAvailable, validFrom, validTo

## g0240（1 列）
- 見出し：prmPlacesAvailable
- 例1 値：NO | NO | YES | NO | YES
  - 同じ表の列：sloid, parentSloidServiceP…, parentNumberService…, designation, additionalInformati…, placesAvailable, validFrom, validTo

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
g0155	
g0156	
g0157	
g0158	
g0159	
g0160	
g0161	
g0162	
g0163	
g0164	
g0165	
g0166	
g0167	
g0168	
g0169	
g0170	
g0171	
g0172	
g0173	
g0174	
g0175	
g0176	
g0177	
g0178	
g0179	
g0180	
g0181	
g0182	
g0183	
g0184	
g0185	
g0186	
g0187	
g0188	
g0189	
g0190	
g0191	
g0192	
g0193	
g0194	
g0195	
g0196	
g0197	
g0198	
g0199	
g0200	
g0201	
g0202	
g0203	
g0204	
g0205	
g0206	
g0207	
g0208	
g0209	
g0210	
g0211	
g0212	
g0213	
g0214	
g0215	
g0216	
g0217	
g0218	
g0219	
g0220	
g0221	
g0222	
g0223	
g0224	
g0225	
g0226	
g0227	
g0228	
g0229	
g0230	
g0231	
g0232	
g0233	
g0234	
g0235	
g0236	
g0237	
g0238	
g0239	
g0240	
```
