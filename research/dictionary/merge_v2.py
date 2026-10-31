"""辞書 v2 のまとめ（2026-11-01 Claude）。draft_v2.jsonl（frozen_d3＋区切りの直し＋K1001〜K1019）に、
ChatGPT の見直し（review_v2_chatgpt.tsv）の直しと、ChatGPT の項目（terms_v2_chatgpt.jsonl）を入れる。裁定は review_v2_adjudication.md。
  python research/dictionary/merge_v2.py → materials/dictionary/merged_v2.jsonl
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, "materials", "dictionary")

FIX = {  # id → 変える欄（GWR は Merkmalskatalog の許可値だけ）
    "K1001": {"pattern": "^(名称|名称_通称|施設名|施設_名称|施設_施設通称|site name|property name|bezeichnung|designationofficial)$",
              "add_address": [" recreation ground", " car park"]},
    "K1002": {"pattern": "^(gebaeudekategorie|gkat)(_?code)?$", "values": "10[1-46]0|1080"},
    "K1003": {"values": "801[1-9]|802[0-3]"},
    "K1004": {"values": "74[0-6][0-9]|7499"},
    "K1005": {"values": "75\\d\\d"},
    "K1006": {"values": "100[1-578]|300[1-578]"},
    "K1007": {"values": "90[1-9]"},
    "K1008": {"values": "990[1-4]"},
    "K1009": {"pattern": "(^|[_ -])(kategorie|typ|art|klasse|periode|herkunft|konfession|thema|vorlagenart|abstimmungsart|rechtsform)[_ -]?(code|id)$"},
    "K1011": {"values": "s1([1-5](\\d{1,3})?)?|s2"},
    "K1013": {"pattern": "^(sloid|didok|bpuic|servicepoint_?number|uic_?number)$"},
    "K1019": {"pattern": "^(?!.*(件数|人数|回数|数$)).*(費|料|料金|料等|代金|(?<![年世時交])代)$"},
}
CG_FIX = {"KC1004": {"values": "[a-z]{2}|[a-z]{3}"}}  # 数 3 桁は電話の国番号と取り違えるので外す（strong のため）


def main():
    rows = [json.loads(l) for l in open(os.path.join(D, "draft_v2.jsonl"), encoding="utf-8") if l.strip()]
    for r in rows:
        f = FIX.get(r["id"])
        if not f:
            if r["id"].startswith("K10"):
                r["reviewer"] = "chatgpt"
            continue
        for k, v in f.items():
            if k == "add_address":
                r["suffix_vote"]["address"] += v
            else:
                r[k] = v
        r["reviewer"] = "chatgpt（直しを入れた）"
    for l in open(os.path.join(D, "terms_v2_chatgpt.jsonl"), encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            r.update(CG_FIX.get(r["id"], {}))
            r["reviewer"] = "claude"
            rows.append(r)
    with open(os.path.join(D, "merged_v2.jsonl"), "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(len(rows))


if __name__ == "__main__":
    main()
