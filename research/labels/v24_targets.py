"""LABEL_GUIDE B3（番号か区分か）の食い違いの候補を教材庫から探す（2026-10-31 Claude。D1 が伸びなかった原因 C3、research/d1_why/findings.md）。

列名が「種類・区分」の語（typ・art・group・class・status・kategorie・stufe・種別・区分・分類 など）と「番号・コード」の語（nr・code・cd・id・コード・番号）の
両方を含む列、または列名が「〜_nr」「〜_code」で値が短いコードの列のうち、今のラベルが id の列。Claude が 1 列ずつ B3 で決めて v24_decisions.jsonl に書く。
  python research/labels/v24_targets.py → research/labels/v24_targets.jsonl
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KIND = re.compile(r"(typ|type|art\b|_art|group|grp|gruppe|kategorie|categ|status|klasse|class|stufe|level|種別|区分|分類|種類|poi)", re.I)
CODE = re.compile(r"(nr|code|_cd|cd$|id|コード|番号)\s*$", re.I)


def main():
    out = []
    for f in sorted((ROOT / "materials" / "pool").glob("batch_b*.jsonl")):
        for k, line in enumerate(open(f, encoding="utf-8")):
            r = json.loads(line)
            h = str(r["header"]).strip()
            if r["label"] != "id" or not CODE.search(h) or not KIND.search(h):
                continue
            out.append({"file": f.name, "line": k, "header": h, "table": r["table"], "values": r["values"], "context": r.get("context", [])[:10],
                        "from": "id"})
    p = ROOT / "research" / "labels" / "v24_targets.jsonl"
    p.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in out), encoding="utf-8")
    print(len(out), "targets")


if __name__ == "__main__":
    main()
