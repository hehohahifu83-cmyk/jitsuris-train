"""教材庫の「おまけ」のファイルを作る（2026-10-25 Claude。学習の設定 FT_TITLE・FT_POOL_UNDECIDABLE 用。学習はしない）。

1. materials/pool/titles.json：表の名前 → 表の題名（work/<陣>/adopted.json の title。値は入れない）
2. materials/pool/undecidable.jsonl：Claude が裁定で unknown と決めた列（人が見ても種類を決められない列。batch_*.jsonl には入らない）。
   形は batch_*.jsonl と同じ（label は "unknown"）。学習で "other" として足すと、見張りが other を「不明」にするので、
   「決められない列には言い切らない」を学ぶ（research/root-cause-audit-2026-10-24.md 原因 6）
確定した陣（manifest.json にある陣）だけを使う。個人の記録を外したあとの corpus を読む。
使い方：python materials/build_pool_extras.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POOL = ROOT / "materials" / "pool"


def read_jsonl(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]


def main():
    batches = sorted(b["batch"] if isinstance(b, dict) else b for b in json.load(open(POOL / "manifest.json", encoding="utf-8")).get("batches", []))
    titles, undec = {}, []
    for b in batches:
        w = POOL / "work" / b
        if not (w / "adopted.json").exists() or not (w / "corpus.jsonl").exists():
            continue
        by_url = {a["resource_url"]: a.get("title", "") for a in json.load(open(w / "adopted.json", encoding="utf-8"))["adopted"]}
        corpus = read_jsonl(w / "corpus.jsonl")
        for c in corpus:
            t = by_url.get(c.get("resource_page")) or by_url.get(c["table"]) or ""
            if t:
                titles[c["table"]] = t
        if (w / "decisions.jsonl").exists():
            for d in read_jsonl(w / "decisions.jsonl"):
                if d["label"] == "unknown" and d["i"] < len(corpus):
                    undec.append({**corpus[d["i"]], "label": "unknown", "teacher": f"claude-{b}", "batch": b})
    (POOL / "titles.json").write_text(json.dumps(titles, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    with open(POOL / "undecidable.jsonl", "w", encoding="utf-8") as fh:
        for r in undec:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"titles {len(titles)} tables; undecidable {len(undec)} columns from {len(batches)} batches")


if __name__ == "__main__":
    main()
