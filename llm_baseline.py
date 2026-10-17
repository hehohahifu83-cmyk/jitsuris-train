"""公開用：採点（score_real）だけ。大型AIへの問い合わせ部分は入れていない。"""
from collections import defaultdict
CLASSES = ["date", "amount", "quantity", "rate", "id", "org", "person", "product", "account", "tax_class", "text", "category", "email", "phone", "address"]


def score_real(pred, truth):
    """15種類の列は従来どおり。その他の列は「不明／その他」と答えれば正しい見送り"""
    N = {"date", "amount", "quantity", "rate", "id"}
    c = w = u = k = oc = ow = 0
    for p, t in zip(pred, truth):
        if t == "other":
            oc, ow = (oc + 1, ow) if p in ("unknown", "other") else (oc, ow + 1)
            continue
        if p in ("unknown", "other"): u += 1
        elif p == t: c += 1
        else:
            w += 1; k += p in N and t in N
    n = c + w + u
    return {"correct": c, "n": n, "acc_all": c / max(n, 1), "wrong": w, "unknown": u, "critical": k, "other_ok": oc, "other_ng": ow}
