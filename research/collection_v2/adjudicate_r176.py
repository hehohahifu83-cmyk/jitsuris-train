"""教材 第 5 回 b176〜b180（Shirasagi 5 サイト）の裁定（2026-11-06 Claude）。先生＝Codex（LABEL_GUIDE v2.4）、2 人目の票＝L 種子 1（r176 でまとめて予測）。

  python research/collection_v2/adjudicate_r176.py   → 各陣の work/<陣>/decisions.jsonl

決め方は adjudicate_r124.py の K1〜K5（rule）と同じ。残りと、規則が合わない行は MANUAL で決めた。抜き取り 44 行は全部見て誤り 0。
b176 g0003 の先例の抜き取りは、Codex が回答の前に先例のラベルを見てしまったので、盲検の抜き取りに数えない（残り 15 グループで食い違い 0）。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from adjudicate_r124 import rule  # noqa: E402

BATCHES = ["b176", "b177", "b178", "b179", "b180"]
EN = "施設の名前の英字表記（AED・公共施設の一覧、B10-3。R4：元の名前の列に合わせる）"
MANUAL = {
    "b176#8": ("text", "「施設の利用可能時間に従う」という説明だけで曜日ではない（K5 の曜日の規則は当てない）"),
    "b177#24": ("address", EN), "b177#198": ("address", EN), "b178#11": ("address", EN), "b178#50": ("address", EN),
    "b179#45": ("address", EN),
    "b177#121": ("address", "AED の設置施設の名前（図書館・宿舎などいろいろな施設、B10-3）"),
    "b177#215": ("address", "公共施設の名前（B10-3）"), "b177#216": ("address", "公共施設の名前の読み（R4）"),
    "b178#4": ("address", "公共施設の名前の読み（R4）"),
    "b178#5": ("text", "備考（設備の記述。b145#335 と同じ）"),
    "b179#32": ("text", "駐車場の説明（台数・共有の書き添え）"),
    "b179#64": ("text", "ごみの出し方の注意の文（見出しは料金種別だが値は文）"),
    "b179#123": ("address", "投票所の施設の通称（B10-3）"),
    "b180#7": ("category", "疾病の分類のコード（ICD-10 の範囲、B3 の種類のコード）"),
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
            out.append({"i": r["i"], "label": lab, "reason": why, "by": "claude-20261105"})
        seen = {d["i"] for d in out}
        for key, (lab, why) in EXTRA.items():
            bb, i = key.split("#")
            if bb == b and int(i) not in seen:
                out.append({"i": int(i), "label": lab, "reason": why, "by": "claude-20261105"})
        with open(w / "decisions.jsonl", "w", encoding="utf-8") as fh:
            for d in out:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        tot[b] = len(out)
    print(tot, sum(tot.values()))


if __name__ == "__main__":
    main()
