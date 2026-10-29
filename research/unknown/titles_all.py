"""原因の確かめ用：確定したすべての陣の表の題名の対応表を作る（2026-10-30 Claude）。
materials/pool/titles.json は b017 までで止まっていた（`materials/build_pool_extras.py` は陣を確定したあと手で動かす手順で、b018 以降動かしていない）。
ここでは titles.json を上書きせず、同じ作り方で research/unknown/titles_all.json に書く。題名が言語ごとの辞書（b063 の {'de':…, 'fr':…}）なら en → de → 最初の値の順で 1 つ選ぶ。
使い方：python research/unknown/titles_all.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "materials"))
from build_pool_extras import POOL, read_jsonl  # noqa: E402


def one(t):
    if isinstance(t, dict):
        return str(t.get("en") or t.get("de") or next((v for v in t.values() if v), ""))
    return str(t or "")


def main():
    batches = sorted(b["batch"] if isinstance(b, dict) else b for b in json.load(open(POOL / "manifest.json", encoding="utf-8")).get("batches", []))
    titles, per = {}, {}
    for b in batches:
        w = POOL / "work" / b
        if not (w / "adopted.json").exists() or not (w / "corpus.jsonl").exists():
            continue
        by_url = {a["resource_url"]: one(a.get("title")) for a in json.load(open(w / "adopted.json", encoding="utf-8"))["adopted"]}
        n = 0
        for c in read_jsonl(w / "corpus.jsonl"):
            t = by_url.get(c.get("resource_page")) or by_url.get(c["table"]) or ""
            if t and c["table"] not in titles:
                titles[c["table"]] = t
                n += 1
        per[b] = n
    (HERE / "titles_all.json").write_text(json.dumps(titles, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    old = json.load(open(POOL / "titles.json", encoding="utf-8"))
    same = sum(titles.get(k) == v for k, v in old.items())
    print(f"titles_all.json {len(titles)} 表（titles.json {len(old)} 表のうち同じ題名 {same}）")
    print(" ".join(f"{b}:{n}" for b, n in per.items()))


if __name__ == "__main__":
    main()
