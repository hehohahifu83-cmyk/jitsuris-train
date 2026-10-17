"""先生役のラベルつきの本物の列名（自治体標準オープンデータセット）を学習データにする。日本語名と英語名の両方を使う。"""
import json, random, re
from gen import column, vary_case, to_fullwidth
from materials.teacher_labels import LABELS

PLACEHOLDER = re.compile(r"[○〇]|xxx|ooo|XXXX", re.I)


def real_rows(seed=11, copies=6):
    fields = json.load(open(__file__.replace("real_data.py", "materials/jp_municipal_fields.json"), encoding="utf-8"))
    uniq, order = {}, []
    for f in fields:
        if f["name"] not in uniq:
            uniq[f["name"]] = f; order.append(f["name"])
    rng = random.Random(seed)
    rows = []
    for i, name in enumerate(order):
        lab = LABELS.get(i)
        if not lab:
            continue
        f = uniq[name]
        heads = [name] + ([f["name_en"]] if f["name_en"] else [])
        for h in heads:
            for _ in range(copies):
                hh = h
                r = rng.random()
                if r < 0.25:
                    hh = vary_case(rng, hh)
                elif r < 0.35:
                    hh = to_fullwidth(rng, hh)
                elif r < 0.45:
                    hh = hh.replace("_", rng.choice([" ", "", "・"]))
                vals = column(rng, lab)
                ex = f["example"]
                if ex and not PLACEHOLDER.search(ex) and rng.random() < 0.5:
                    vals = vals[:-1] + [ex]
                rows.append((hh, vals, lab))
    return rows


if __name__ == "__main__":
    rr = real_rows()
    print(len(rr), "行", len({h for h, _, _ in rr}), "種類の列名")
