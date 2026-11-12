"""G3（金額・単位の列が多い海外の陣、直し M を測り直す）の公開元（2026-11-12 Claude。データセットの中身は見ない）。

  python research/g3/g3_orgs.py   → research/g3/g3_orgs.json

決まり（bench/fixm_prereg_20261112.md の G3 の追記）：G1 と同じ 3 カタログ（Alberta・Ontario・Berlin、hold で登録済み）の組織のうち、
**G1 で表を採用した 92 公開元を除いた**組織だけ（公開元が G1 と重ならない）。新しい登録はしない。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "independent_eval"))
import allocation as A  # noqa: E402


def main():
    used = set()
    for w in ("g1", "g1x"):
        used |= {A.normalize_publisher_id(x["publisher_id"]) for x in json.load(open(ROOT / f"materials/pool/work/{w}/adopted.json", encoding="utf-8"))["adopted"]}
    rows = json.load(open(ROOT / "research/g1/g1_orgs.json", encoding="utf-8"))["rows"]
    out = [dict(r, g3=r["g1"] and A.normalize_publisher_id(r["publisher_id"]) not in used) for r in rows]
    doc = {"schema_version": 1, "excluded_g1_publishers": len(used), "rows": out,
           "summary": {s: sum(r["site"] == s and r["g3"] for r in out) for s in ("alberta", "ontario", "berlin")}}
    (ROOT / "research/g3/g3_orgs.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(doc["summary"])


if __name__ == "__main__":
    main()
