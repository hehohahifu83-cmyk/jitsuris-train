"""まとめた set（materials/pool/work/r*）への予測を、陣ごとの pred_l_seed1.json に分ける（2026-11-04 Claude、教材集め v2）。

  python materials/split_preds.py materials/pool/work/r124/pred_lp_job2.json
    → materials/pool/work/<陣>/pred_l_seed1.json（行の id の先頭が陣の名前。set.json の id の集合と合うことを確かめる）
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main(path):
    doc = json.load(open(path, encoding="utf-8"))
    by = {}
    for r in doc["rows"]:
        by.setdefault(r["id"].split("-")[0], []).append(r)
    meta = {k: v for k, v in doc.items() if k != "rows"}
    for b, rows in sorted(by.items()):
        w = ROOT / "materials" / "pool" / "work" / b
        ids = {c["id"] for c in json.load(open(w / "set.json", encoding="utf-8"))["columns"]}
        if ids != {r["id"] for r in rows}:
            raise SystemExit(f"{b}: set.json と予測の id が合わない")
        (w / "pred_l_seed1.json").write_text(json.dumps({**meta, "split_from": str(Path(path)), "rows": rows}, ensure_ascii=False) + "\n", encoding="utf-8")
        print(b, len(rows))


if __name__ == "__main__":
    main(sys.argv[1])
