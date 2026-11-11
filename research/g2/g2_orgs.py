"""G2（2 つ目の海外の陣、直し M を測る）の公開元を決める（2026-11-12 Claude。research/g2/g2_orgs.py を写した、収集の前。メタデータの組織名だけを見る。データセットの中身は見ない）。

  python research/g2/g2_orgs.py            → research/g2/g2_orgs.json（組織ごとの今の割り当て・G1 に入れるか）
  python research/g2/g2_orgs.py --write    → 入れる組織を allocation.json に hold で登録する

決まり（bench/fixm_prereg_20261112.md）：
  カタログごとに割り当てる。G2＝GovData.de（ckan.govdata.de、ドイツの国・州・市の集約カタログ）。
  berlin-open-data は G1 の Berlin と重なるので外す（Berlin 統計局のファイルも採用で外す）。データセットのある組織だけ。
  名前は G1 の道具に合わせて行の印を "g1" のままにする（G2 に入れるかの印）。
"""
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "independent_eval"))
import allocation as A  # noqa: E402

PROBE = ROOT / "materials/pool/probe/orgs_f1_20261104c.json"
ALLOC = ROOT / "independent_eval/allocation.json"
OUT = ROOT / "research/g2/g2_orgs.json"
PARENT = {"govdata_de": "govdata_cat"}
EXCLUDE = {"berlin-open-data": "G1 の Berlin と重なる"}


def main(argv=None):
    write = "--write" in (argv if argv is not None else sys.argv[1:])
    probe = json.load(open(PROBE, encoding="utf-8"))
    alloc = A.load_allocation(ALLOC)
    rows = []
    for h in [x for x in probe["hosts"] if x["site"] in PARENT]:
        for o in h.get("orgs") or []:
            if not o.get("package_count"):
                continue
            pid = f"{PARENT[h['site']]}:{o['name']}"
            canon = A.resolve_publisher_id(pid, alloc.get("aliases", {}))
            now = next((p["pool"] for p in alloc["publishers"] if A.normalize_publisher_id(p["publisher_id"]) == canon), None)
            rows.append({"site": h["site"], "base": h["base"], "org": o["name"], "title": o.get("title", ""), "datasets": o["package_count"],
                         "publisher_id": pid, "pool_now": now, "g1": now in (None, "hold") and o["name"] not in EXCLUDE,
                         "reason": EXCLUDE.get(o["name"], "" if now in (None, "hold") else f"もう {now} に登録")})
    if write:
        today = date.today().isoformat()
        have = {A.normalize_publisher_id(p["publisher_id"]) for p in alloc["publishers"]}
        for r in rows:
            if r["g1"] and A.normalize_publisher_id(r["publisher_id"]) not in have:
                alloc["publishers"].append({"publisher_id": r["publisher_id"], "pool": "hold", "date": today})
                have.add(A.normalize_publisher_id(r["publisher_id"]))
        ALLOC.write_text(json.dumps(alloc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    doc = {"schema_version": 1, "probe": str(PROBE.relative_to(ROOT)), "rows": rows,
           "summary": {s: {"orgs": sum(r["site"] == s for r in rows), "g1": sum(r["site"] == s and r["g1"] for r in rows)} for s in PARENT}}
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(doc["summary"], ensure_ascii=False))


if __name__ == "__main__":
    main()
