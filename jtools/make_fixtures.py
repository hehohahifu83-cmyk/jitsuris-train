"""Python と JS で道具の結果が同じかを確かめる正解のデータを作る（2026-11-01 Claude）。

  python jtools/make_fixtures.py   → jtools/fixtures.json
  node --test jtools/              → JS 版が同じ結果を出すか（jtools/parity.test.mjs）

中身：
  values：手で選んだ変わった値（全角・和暦・漢数字・通貨・番号）の read_value と check の結果
  tables：教材庫の本物の表（b001〜b111、b018 を除く。各陣の先頭 3 つの表、行のそろった値があるもの）の run_table の結果。入力は corpus.jsonl から読む（ここには結果だけ）。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from jtools import check_digits as CD  # noqa: E402
from jtools import read_value as RV  # noqa: E402
from jtools import run_tools as RT  # noqa: E402
from jtools import table_arith as TA  # noqa: E402
from jtools import std_fields as SF
from jtools import facility_kind as FK
from jtools import column_links as CL

FACILITIES = [
    ['名称', ['中央商店', '北商店'], ['営業許可番号']],
    ['施設名称', ['中央保育所', '北保育所'], ['定員', '所在地']],
    ['施設名', ['中央保育所', '北保育所'], ['避難', '所在地']],
    ['名称', ['中央公園', '体育館', '図書館'], ['住所']],
    ['名称', ['株式会社A', '株式会社B', '株式会社C', '不明', '不明'], []],
    ['名称', ['株式会社A', '株式会社B', '不明', '不明', '不明'], []],
    ['場所名称', [], []], ['事業所名称', [], []],
    ['名称', [], []], ['名称', [None, '', '-', 'nan'], []],
    ['施設名', ['中央公園', '不明'], []],
    ['名称_カナ', ['チュウオウコウエン'], ['営業許可番号']],
    ['数量', ['中央公園'], ['所在地']],
    ['名称', ['A', 'B'], ['所在地']],
    ['NAME', ['North Park'], []],
]
LINK_TABLES = [
    [{'header': h, 'values': vs} for h, vs in [('施設名', ['中央公園']), ('施設名カナ', ['チュウオウコウエン']), ('運営者', ['市役所'])]],
    [{'header': h, 'values': vs} for h, vs in [('UNIT', ['人']), ('人口', ['100', '200']), ('団体コード', ['011002', '011003'])]],
    [{'header': h, 'values': vs} for h, vs in [('単位', ['円']), ('EINHEIT', ['kg']), ('値', ['100', '200'])]],
    [{'header': h, 'values': []} for h in ['名称', '名称', '名称_英字', '名称_かな', '名称_通称', '名称_en']],
    [{'header': h, 'values': []} for h in ['name', 'nameKana', 'nameEn', 'name_EN', 'name_kana', 'name_english']],
    [{'header': h, 'values': ['A']} for h in ['施設名', '場所名称', '運営団体名']],
    [], [{'header': '単位', 'values': []}, {'header': '値', 'values': []}],
    [{'header': '施設名', 'values': ['中央公園']}, {'header': '施設名_カナ', 'values': ['チュウオウコウエン']}],
]

VALUES = [
    "１，２３４円", "△1,200", "▲500", "(3,000)", "1,234-", "千二百三十四", "3万5千", "二千二十四", "壱万", "〇", "〇〇", "5千", "1.5万",
    "¥1,234", "$-12.50", "US$1,000", "1.234,56 €", "1'234.50", "12,5", "45%", "3‰", "1,234千円", "1361.0百万円", "R$ 1.910,22", "€ 120,863.00",
    "£42,580.00", "100ドル", "3.5kg", "10人", "４０ｔ", "28.3m", "1.0ha", "２回", "+7", ".5", "007", "0.000",
    "令和7年4月1日", "令和元年", "平成30年度", "昭和 58年 3月", "R7.4.1", "H18. 1.26", "h 9.12. 2", "2024-04-01", "2024-04-01T12:30:05Z",
    "2024/4/1", "2024-04", "2024年4月", "2024年度", "1.4.2024", "1/28/2008 12:00 AM", "13/02/2020", "12:30", "24:00", "12:30:05", "25:00",
    "20240401", "42735", "1723010401.69", "Q1", "FY2024", "abc", "-", "n/a", "", " ", "x", "1 234", "1,23", "1,2345", "12.3.4",
    "7000012050002", "7000012050003", "T7000012050002", "T 7000012050002", "4901234567894", "4901234567895", "96385074", "0000000000000",
    "9784003101018", "4-00-310101-4", "ISBN 978-4-00-310101-8", "GB82 WEST 1234 5698 7654 32", "GB82WEST12345698765433",
    "4111 1111 1111 1111", "4111111111111112", "131016", "131017", "011002", "〒100-0001", "100-0001", "SW1A 1AA", "Tw11 0lw", "K1A 0B1",
    "12345", "12345-6789", "ＡＢＣ１２３", "零幅​スペース", "1 000",
]


def tables():
    out = []
    for p in sorted((ROOT / "materials" / "pool" / "work").glob("b[0-9][0-9][0-9]/corpus.jsonl")):
        n = int(p.parent.name[1:])
        if n == 18 or n > 111:   # b018 は使わない決まり。b112 から先は E3（ラベルの前に値を読まない）
            continue
        by = {}
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                if r.get("row_values"):
                    by.setdefault(r["table"], []).append(r)
        for url in list(by)[:3]:
            cols = by[url]
            res = RT.run_table([{"header": c["header"], "values": c.get("values"), "rows": c.get("row_values")} for c in cols])
            rels = TA.relations([{"header": c["header"], "rows": c["row_values"]} for c in cols]) \
                if len({len(c["row_values"]) for c in cols}) == 1 and len(cols) >= 2 else []
            out.append({"corpus": str(p.relative_to(ROOT)), "table": url, "result": res, "relations": rels})
    return out


def main():
    doc = {"values": [{"in": v, "read": RV.read_value(v), "check": CD.check(v)} for v in VALUES],
           "summaries": [{"in": vs, "read": RV.column_summary(vs), "ids": CD.column_summary(vs)}
                         for vs in (VALUES[:20], VALUES[37:60], VALUES[73:], ["〇", "〇", "", "有"], [])],
           "tables": tables(),
           "standard": [{"header": h, "result": SF.lookup(h)} for h in sorted({str(r[i]) for r in SF.DATA['fields'] for i in (1, 2)} | {'', 'not-a-standard-field', ' ＩＤ ', '\ufeff名称\n'})],
           "facility": [{"in": row, "result": FK.decide(*row)} for row in FACILITIES],
           "column_links": [{"in": cols, "links": CL.find_links(cols), "result": RT.run_table(cols)} for cols in LINK_TABLES],
           "base_headers": [{"in": h, "result": CL.base_header(h)} for h in ['名称_カナ', '名称（英字）', '施設名かな表記', 'name_en', 'nameKana', 'nameEn', 'name_EN', '名称', 'カナ', '']]}
    path = ROOT / "jtools" / "fixtures.json"
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print(f"{path.relative_to(ROOT)}: values {len(doc['values'])}, tables {len(doc['tables'])}, "
          f"relations {sum(len(t['relations']) for t in doc['tables'])}, size {path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
