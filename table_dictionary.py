"""表の列の知識の辞書（2026-10-31 Claude。オーナー指示「表に特化した知識を集めた辞書を…迷ったら辞書を参照」）。

辞書は materials/dictionary/terms.jsonl（1 行 1 項目）。動くときは辞書のファイルを読むだけで、AI は呼ばない。
項目の形：
  {"id": "K0001", "pattern": 列名に当てる正規表現（NFKC・小文字にした列名に search）, "type": 種類（LABELS のどれか）,
   "values": 値の正規表現（任意。空でない値の 8 割以上が fullmatch したときだけ当てる）,
   "meaning": 何を表す語か, "source": 出典（URL か文書名）, "origin": "past:<陣や集合>" か "new", "author": 書いた AI, "reviewer": 見た AI}
使い方（apply）：迷ったときだけ見る。迷った＝最後の答えが不明、または本体の 1 位の確率が doubt 未満。
当たった項目の種類が 1 つに決まり、それが本体の上位 3 つに入っていれば、その種類にする。当たらない・割れる・上位 3 つに無いときは変えない。

2026-10-31 追加（値の知識、research/confirm_why/findings.md の方向）：
  "suffix_vote": {"address": [語尾...], "org": [語尾...]}：値の語尾で多数決。片方が空でない値の min_share（既定 0.6）以上で、
                 もう片方が 0.2 未満のときだけ、その種類（type は書かない）。LABEL_GUIDE 73・75・82・98・99 の語。
  "strong": true：本体が自信を持っていても（迷っていなくても）当てる。上位 3 つに入っている条件は同じ。
                 列名と値の形の両方で決まる、公的な一覧の項目だけに使う。
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

DEFAULT = Path(__file__).resolve().parent / "materials" / "dictionary" / "terms.jsonl"
LABELS = ("account", "address", "amount", "category", "date", "email", "id", "org", "other", "phone", "product", "quantity",
          "rate", "tax_class", "text")
_EMPTY = {"", "nan", "none", "null", "na", "n/a", "-", "－", "―", "*", "＊", "…", "."}


def norm(s) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(s))).strip().lower()


class Dictionary:
    def __init__(self, entries):
        self.entries = []
        for e in entries:
            if "suffix_vote" in e:
                if set(e["suffix_vote"]) - set(LABELS):
                    raise ValueError(f"{e.get('id')}: 種類が違う {set(e['suffix_vote'])}")
            elif e["type"] not in LABELS:
                raise ValueError(f"{e.get('id')}: 種類が違う {e['type']}")
            self.entries.append((e, re.compile(e["pattern"], re.I), re.compile(e["values"], re.I) if e.get("values") else None))

    @classmethod
    def load(cls, path=None):
        p = Path(path) if path else DEFAULT
        rows = [json.loads(line) for line in open(p, encoding="utf-8") if line.strip()] if p.exists() else []
        ids = [r["id"] for r in rows]
        if len(ids) != len(set(ids)):
            raise ValueError("辞書の id が重なっている")
        return cls(rows)

    @staticmethod
    def _vote(e, vals):
        if not vals:
            return None
        share = {t: sum(any(v.endswith(norm(x)) for x in sfx) for v in vals) / len(vals) for t, sfx in e["suffix_vote"].items()}
        best = max(share, key=share.get)
        others = [x for t, x in share.items() if t != best]
        if e.get("vote_only") and best not in e["vote_only"]:   # 片方の語尾は「止める」だけに使う（避難所の一覧の学校は address になるため）
            return None
        return best if share[best] >= e.get("min_share", 0.6) and all(x < 0.2 for x in others) else None

    def lookup(self, header, values=(), strong_only=False):
        """当たった項目の [(種類, id)]。strong_only は強い項目だけ。"""
        h = norm(header)
        vals = [norm(v) for v in values if norm(v) not in _EMPTY]
        hits = []
        for e, pat, vpat in self.entries:
            if strong_only and not e.get("strong"):
                continue
            if not pat.search(h):
                continue
            if vpat is not None and (not vals or sum(bool(vpat.fullmatch(v)) for v in vals) < 0.8 * len(vals)):
                continue
            t = self._vote(e, vals) if "suffix_vote" in e else e["type"]
            if t:
                hits.append((t, e["id"]))
        return hits

    def apply(self, final, top3, header, values=(), doubt=0.95):
        """(答え, 使った項目の id か None)。"""
        if not top3:
            return final, None
        sure = final != "unknown" and top3[0]["probability"] >= doubt
        hits = self.lookup(header, values, strong_only=sure)
        types = {t for t, _ in hits}
        if len(types) != 1:
            return final, None
        t = next(iter(types))
        if t == final or t not in [x["label"] for x in top3[:3]]:
            return final, None
        return t, ",".join(i for _, i in hits)
