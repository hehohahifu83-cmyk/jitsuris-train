"""教材庫の英語の表で、CP1252 のファイルを CP932 で読んで化けた表の一覧を作る（2026-11-01 Claude。オーナー了承「そうしろ」）。
化けた表＝言語が ja でない表で、列名・値・兄弟の列・行の値のどこかに「｣」（0xA3 を CP932 で読んだ字）がある表。
直し方：文字列を CP932 に戻して元のバイトを得て、CP1252 で読み直す（encoder_context.cp932_to_cp1252）。
  python research/valuefix/make_list.py → materials/pool/valuefix_cp1252.jsonl
"""
import collections
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
from encoder_context import cp932_to_cp1252  # noqa: E402


def strings(d):
    rv = d.get("row_values") or []
    return [str(x) for x in [d.get("header", "")] + list(d.get("values") or []) + list(d.get("context") or []) + (list(rv) if isinstance(rv, list) else [])]


def main():
    tabs = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(ROOT, "materials", "pool", "batch_*.jsonl"))):
        for line in open(f, encoding="utf-8"):
            d = json.loads(line)
            tabs[d.get("table")].append((os.path.basename(f)[6:10], d))
    out = []
    for t, rs in sorted(tabs.items(), key=lambda x: str(x[0])):
        if rs[0][1].get("language") == "ja" or not any("｣" in s for _, d in rs for s in strings(d)):
            continue
        changed = sum(cp932_to_cp1252(s) != s for _, d in rs for s in strings(d))
        q = sum(any("｣" in v for v in d.get("values") or []) for _, d in rs)
        out.append({"table": t, "batch": rs[0][0], "publisher": rs[0][1].get("publisher"), "columns": len(rs), "columns_with_pound_in_values": q,
                    "strings_changed": changed, "from": "cp932", "to": "cp1252"})
    p = os.path.join(ROOT, "materials", "pool", "valuefix_cp1252.jsonl")
    with open(p, "w", encoding="utf-8") as fh:
        for o in out:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    print(f"表 {len(out)}・列 {sum(o['columns'] for o in out)}・値に £ がある列 {sum(o['columns_with_pound_in_values'] for o in out)}・直る文字列 {sum(o['strings_changed'] for o in out)}")


if __name__ == "__main__":
    main()
