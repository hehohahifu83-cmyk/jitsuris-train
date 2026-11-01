"""古い 23 陣（辞書の確かめと同じ）で、製品＋K2 と ＋直し（F7 抜き）を比べる（2026-11-01 Claude。害の確かめ、採否には使わない）。"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
for p in (os.path.join(ROOT, "research"), os.path.join(ROOT, "research", "fixes")):
    sys.path.insert(0, p)
import d1_eval as D, eval_fixes as EF  # noqa: E402
G = ("F1b", "F3", "F6", "G1", "G2", "G3", "G4")
labels = list(D.V.LABELS)
train = [c for b in D.A.TRAIN for c in D.E.load_batch(b)]
okm = np.array([bool(c["truth"]) and c["truth"] in labels for c in train])
mv, _, _ = D.E.fit(np.hstack([D.V.matrix([c["values"] for c in train]), D.E.table_matrix(train)])[okm], np.array([c["truth"] for c in train])[okm])
os.environ["JITSURIS_DICT"] = os.path.join(ROOT, "materials", "dictionary", "frozen_v2.jsonl")
data = EF.load(EF.DECIDE + EF.CONFIRM)
pa, pb = {}, {}
a = EF.run(data, mv, labels, D.PRODUCT + ("K",), per=pa); EF._PCACHE.clear()
b = EF.run(data, mv, labels, D.PRODUCT + ("K",) + G, per=pb)
print("製品＋K2", a); print("＋直し", b)
for k in pa:
    if pa[k][0] != pb[k][0] and pb[k][0] not in ("unknown", pb[k][1]):
        print("  悪く", k, str(pa[k][2])[:30], pa[k][1], pa[k][0], "→", pb[k][0])
