"""いくつかの陣をつないだ set の予測を、陣ごとの pred_e5base_seed1.json に分ける（2026-10-27 Claude）。

予測の依頼は 1 回 1 つの set なので、待っている陣をまとめて 1 回で予測し、id の先頭（bNNN-）で分ける。
各陣の set.json の id がすべて予測にあることを確かめ、set_sha256 は各陣の set.json の値に直す。
  python materials/pool/split_preds.py materials/pool/work/pend1027 [pred_c2_seed1.json]
（2 つ目の引数で予測のファイル名を変える。既定 pred_e5base_seed1.json。2026-10-29）
"""
import hashlib
import json
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parent / "work"


def main(argv=None):
    args = argv or sys.argv[1:]
    combined = Path(args[0])
    name = args[1] if len(args) > 1 else "pred_e5base_seed1.json"
    pred = json.loads((combined / name).read_text(encoding="utf-8"))
    sources = json.loads((combined / "sources.json").read_text(encoding="utf-8"))["sources"]
    by_id = {r["id"]: r for r in pred["rows"]}
    for batch in sources:
        set_path = WORK / batch / "set.json"
        out = WORK / batch / name
        if out.exists():
            raise SystemExit(f"{out} がもうある")
        cols = json.loads(set_path.read_text(encoding="utf-8"))["columns"]
        missing = [c["id"] for c in cols if c["id"] not in by_id]
        if missing:
            raise SystemExit(f"{batch}: 予測に無い列 {missing[:5]}")
        rows = [by_id[c["id"]] for c in cols]
        doc = {**pred, "set_id": f"label-assist-{batch}",
               "set_sha256": hashlib.sha256(set_path.read_bytes()).hexdigest(),
               "split_from": {"set_id": pred["set_id"], "set_sha256": pred["set_sha256"]}, "rows": rows}
        out.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{batch}: {len(rows)} rows")


if __name__ == "__main__":
    main()
