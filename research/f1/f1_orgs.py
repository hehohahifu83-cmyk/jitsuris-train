"""F1 の公開元を決める（2026-11-09 Claude、F1 の収集の前。メタデータの組織名だけを見る。データセットの中身は見ない）。

  python research/f1/f1_orgs.py            → research/f1/f1_orgs.json（組織ごとの自治体コード・今の割り当て・F1 に入れるか）
  python research/f1/f1_orgs.py --write    → 入れる組織の未登録の自治体を allocation.json に hold で登録し、組織 ID を別名でつなぐ

決まり（bench/g24fix_prereg_20261104.md「F1・SCRC の割り当ての決定」と「F1 の公開元の守り」に足す）：
  F1 に入れるのは、自治体コードの割り当てが hold か未登録の組織だけ。train（教材に使った、または使える）・eval2・eval3・main は外す。
  国の機関（総務省統計局・総務省公共クラウド）と事業者（jig.jp）は外す。新宿区・文京区は東京都のカタログ経由で教材庫にあるので外す。
  別の名前（tokyo:t131059 など）で教材庫・割り当てにいないかも、自治体コードで確かめた（2026-11-09）。
  金沢のカタログの「石川中央都市圏」は複数の市町の組なので、自治体コードを持たない hold の公開元として入れる。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "independent_eval"))
import allocation as A  # noqa: E402

PROBE = ROOT / "materials/pool/probe/orgs_f1_20261104d.json"
ALLOC = ROOT / "independent_eval/allocation.json"
OUT = ROOT / "research/f1/f1_orgs.json"
MUNI = json.load(open(ROOT / "materials/dict/jp_municipalities.json", encoding="utf-8"))
PARENT = {"jig_jp": "odp_jig", "kanazawa": "kanazawa_cat", "sendai": "sendai_city"}
EXCLUDE = {"jp-jig": "事業者（jig.jp）", "jp-go-soumu-kcloud": "国の機関", "jp-go-soumu-stat": "国の機関", "jp-tokyo-shinjuku": "教材庫にある（決定済み）",
           "jp-tokyo-bunkyo": "東京都のカタログ経由で教材庫にある（tokyo:t131059、train、80 列）"}
KANAZAWA = {"kanazawa": "金沢市", "hakusan": "白山市", "kahoku": "かほく市", "nonoichi": "野々市市", "tsubata": "津幡町", "uchinada": "内灘町"}


def code_of(pref, city):
    for r in MUNI:
        if r["pref"] == pref and (r["city"] or "") == (city or ""):
            return r["code"]
    return None


def split_title(title):
    m = re.match(r"^(北海道|東京都|京都府|大阪府|.{2,3}県)(.*)$", title)
    return (m.group(1), m.group(2)) if m else (None, None)


def main(argv=None):
    write = "--write" in (argv or sys.argv[1:])
    probe = json.load(open(PROBE, encoding="utf-8"))
    alloc = A.load_allocation(ALLOC)
    rows = []
    for h in [x for x in probe["hosts"] if x["site"] in PARENT]:   # F1 は日本の 3 カタログだけ（海外は割り当てない、決定済み）
        for o in h.get("orgs") or []:
            if not o.get("package_count"):
                continue
            name, title = o["name"], o["title"]
            row = {"site": h["site"], "base": h["base"], "org": name, "title": title, "datasets": o["package_count"],
                   "publisher_id": f"{PARENT[h['site']]}:{name}"}
            if name in EXCLUDE:
                row.update(code=None, pool_now=None, f1=False, reason=EXCLUDE[name])
            elif h["site"] == "sendai":
                row.update(code="041009")
            elif h["site"] == "kanazawa":
                row.update(code=code_of("石川県", KANAZAWA[name]) if name in KANAZAWA else None)
            else:
                pref, city = split_title(title)
                row.update(code=code_of(pref, city) if pref else None)
            if "f1" not in row:
                if row["code"]:
                    pool = A.assignment_for(row["code"], alloc)
                    registered = any(A.normalize_publisher_id(p["publisher_id"]) == row["code"] for p in alloc["publishers"])
                    row["pool_now"] = pool["pool"] if registered else "未登録"
                    ok = row["pool_now"] in ("hold", "未登録")
                    row.update(f1=ok, reason="hold か未登録" if ok else f"割り当てが {row['pool_now']}（F1 に使わない）")
                else:
                    row.update(pool_now="未登録", f1=True, reason="自治体コードの無い組（石川中央都市圏）。hold の公開元として入れる")
            rows.append(row)
    summary = {"orgs": len(rows), "f1": sum(r["f1"] for r in rows), "f1_datasets": sum(r["datasets"] for r in rows if r["f1"]),
               "excluded": {r["publisher_id"]: r["reason"] for r in rows if not r["f1"]}}
    OUT.write_text(json.dumps({"source": str(PROBE.relative_to(ROOT)), "summary": summary, "rows": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    if write:
        today = "2026-11-09"
        for r in rows:
            if not r["f1"]:
                continue
            if r["code"]:
                if r["pool_now"] == "未登録":
                    alloc = A.add_assignment(alloc, r["code"], today, ambiguous=True)   # ambiguous=True で hold
                alias = A.normalize_publisher_id(r["publisher_id"])
                if alias != r["code"]:
                    alloc["aliases"][alias] = r["code"]
            else:
                alloc = A.add_assignment(alloc, r["publisher_id"], today, ambiguous=True)
        A.validate_allocation(alloc)
        ALLOC.write_text(json.dumps(alloc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("allocation に登録した")


if __name__ == "__main__":
    main()
