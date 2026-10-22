"""教材の corpus（1 行＝1 列）を、evaluate_independent.py predict が読む set の形にする（ラベルの手伝いの予測用、2026-10-22 Claude）。

ラベルは読まない。id は corpus の並び順（<prefix>-0001 …）。単位列の例は encoder_context.unit_context_map で同じ表から作る。
使い方：python materials/corpus_to_set.py <corpus.jsonl> <set.json> <prefix>
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from encoder_context import unit_context_map  # noqa: E402


def convert(corpus_path, prefix):
    rows = [json.loads(line) for line in open(corpus_path, encoding="utf-8") if line.strip()]
    units = unit_context_map([(r["header"], r["values"], "", r.get("context") or [], r["table"]) for r in rows])
    cols = []
    for i, r in enumerate(rows, 1):
        cols.append({"id": f"{prefix}-{i:04d}", "table": r["table"], "source": r.get("source", ""), "language": "ja",
                     "header": r["header"], "values": r["values"][:5] or [""], "siblings": r.get("context") or [],
                     "unit": units.get(r["table"], "")})
    return {"schema_version": 1, "set_id": f"label-assist-{prefix}", "columns": cols}


if __name__ == "__main__":
    data = convert(sys.argv[1], sys.argv[3])
    Path(sys.argv[2]).write_text(json.dumps(data, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print(len(data["columns"]))
