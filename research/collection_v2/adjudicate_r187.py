"""教材 b187（静岡、取り直しの 29 表・217 列）の裁定（2026-11-07 Claude）。先生＝Codex（LABEL_GUIDE v2.4）、2 人目の票＝L 種子 1（r187）。

  python research/collection_v2/adjudicate_r187.py   → work/b187/decisions.jsonl

決め方は adjudicate_r124.py の K1〜K5（rule）と同じ。手で 1 行。抜き取り 10 行は全部見て誤り 0、先例の抜き取り 5 グループは食い違い 0。
崩れた 1 表（沼津市統計書 農林水産業、Codex の notes）は exclude_tables.json で表ごと外す。学習曲線 W2 の学習が終わった後に確定した（W2 のデータには入っていない）。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from adjudicate_r124 import rule  # noqa: E402

BATCHES = ["b187"]
MANUAL = {
    "b187#143": ("address", "Wi-Fi の使える場所（店・会社・施設）の名前の英語表記（いろいろな施設の一覧、B10-3。R4：元の名前の列に合わせる）"),
}
EXTRA = {}


def main():
    tot = {}
    for b in (sys.argv[1:] or BATCHES):
        w = ROOT / "materials" / "pool" / "work" / b
        out = []
        for line in open(w / "review.jsonl", encoding="utf-8"):
            r = json.loads(line)
            key = f"{b}#{r['i']}"
            if r["kind"] == "audit":
                lab, why = r["teacher"], "抜き取り：先生とモデルの一致を確かめた"
            elif key in MANUAL:
                lab, why = MANUAL[key]
            else:
                got = rule(r)
                if not got:
                    raise SystemExit(f"未裁定 {key} {r['teacher']} {r['model']} {r['header']!r}")
                lab, why = got
            out.append({"i": r["i"], "label": lab, "reason": why, "by": "claude-20261107"})
        seen = {d["i"] for d in out}
        for key, (lab, why) in EXTRA.items():
            bb, i = key.split("#")
            if bb == b and int(i) not in seen:
                out.append({"i": int(i), "label": lab, "reason": why, "by": "claude-20261107"})
        with open(w / "decisions.jsonl", "w", encoding="utf-8") as fh:
            for d in out:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        tot[b] = len(out)
    print(tot, sum(tot.values()))


if __name__ == "__main__":
    main()
