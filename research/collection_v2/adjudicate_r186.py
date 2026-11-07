"""教材 第 7 回 b186〜b196（Shirasagi：静岡 b186・b188・b189、徳島 b190、香川 b192・b193、鳥取 b194〜b196）の裁定（2026-11-07 Claude）。
先生＝Codex（LABEL_GUIDE v2.4）、2 人目の票＝L 種子 1（r186 でまとめて予測）。

  python research/collection_v2/adjudicate_r186.py   → 各陣の work/<陣>/decisions.jsonl

決め方は adjudicate_r124.py の K1〜K5（rule）と同じ。残り 23 行は MANUAL で決めた。抜き取り 90 行は全部見て誤り 0。先例の抜き取り 41 グループは食い違い 0。
崩れた 6 表（b188 1・b189 4・b190 1、Codex の notes）は exclude_tables.json で表ごと外す（食い違いのうち 39 行。裁定の記録は残すが教材に入らない）。
文化財の所有者の列（b186・b192）は、個人の所有が元の表で「個人」と伏せてあり、個人の名前は無いことを Claude が値で確かめた（unknown のまま教材に入れない）。
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from adjudicate_r124 import rule  # noqa: E402

BATCHES = ["b186", "b188", "b189", "b190", "b192", "b193", "b194", "b195", "b196"]
EN = "施設の名前の英字表記（公共施設・避難所・観光施設の一覧、B10-3。R4：元の名前の列に合わせる）"
FAC = "いろいろな種類の施設が並ぶ一覧の施設の名前（B10-3）"
CRS = "座標参照系のコード（EPSG 6668）。方式の種類を表すコード（B3）。b195・b196 の測地系の列と同じ"
PARK = "駐車場の説明（有無に台数・注意の書き添え。b179#32 と同じ）"
MANUAL = {
    "b186#209": ("address", EN), "b188#112": ("address", EN), "b192#5": ("address", EN), "b195#5": ("address", EN),
    "b196#4": ("address", EN), "b196#14": ("address", EN),
    "b188#14": ("address", "公共施設の名前の読み（R4）"),
    "b188#117": ("address", "国籍・地域のコード（ガイドの国・国コードの決まりで address。Codex の答えどおり）"),
    "b188#48": ("text", PARK), "b190#17": ("text", PARK),
    "b188#96": ("text", "備考（値は 1 つだけ。b178#5 と同じく備考は text）"),
    "b189#4": ("address", "体育施設の愛称（B10-3）"), "b189#6": ("text", "備考（設備の記述）"),
    "b189#8": ("category", "調査項目の一覧（決まった項目の名前。Codex の答えどおり）"),
    "b189#107": ("address", "中学校区の区域の名前（Codex の答えどおり）"),
    "b190#24": ("address", "公共施設の名前の読み（R4）"), "b190#28": ("address", "津波避難ビルなどの避難先の名前（B10-3）"),
    "b190#29": ("address", "避難先の名前の読み（R4）"),
    "b190#41": ("category", "ユニバーサルメニューの決まった語を ; でつないだもの（b183#14 のゴミ種類と同じ）"),
    "b195#48": ("category", CRS), "b196#24": ("category", CRS), "b196#38": ("category", CRS),
    "b196#5": ("address", "観光施設・直売所の通称（B10-3）"),
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
