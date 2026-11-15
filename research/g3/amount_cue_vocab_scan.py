"""G3 の金額の手がかりの調べ（a）語彙：使い済みの陣で、候補の語を列名に含む列の正解の内訳を数える（2026-11-15 Claude、読むだけ）。
  python research/g3/amount_cue_vocab_scan.py（ai-bridge の labels を /home/user/ai-bridge に置く）
"""
import sys,os,re,json
sys.path[:0]=[os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'fix_n')]
import fix_n_dev as FD
D,R,F1E,G1E,G2E=FD.D,FD.R,FD.F1E,FD.G1E,FD.G2E
B='/home/user/ai-bridge/labels'
fx=D.label_fixes(os.path.join(FD.ROOT,"research","labels","consistency_20261031","decisions.jsonl"))
sets={"古い23":D.EF.load(D.EF.DECIDE+D.EF.CONFIRM),"決める":D.load_side("decide",fx),"確かめる":D.load_side("confirm",fx),"E1":R.load("E1"),"E2":R.load("E2"),
"F1":F1E.load_f1(B+'/f1/final.jsonl'),"G1":G1E.load_g1(B+'/g1/final.jsonl'),"G2":G2E.load_g2(B+'/g2/final.jsonl')}
words={"income":r"income","allocation":r"allocat","reimburse":r"reimburs","entitled":r"entitle","receipt":r"receipt","gains/gis/oas":r"\b(gains|gis|oas)\b","appropriation":r"appropriat"}
from collections import Counter,defaultdict
out=defaultdict(Counter)
for sn,data in sets.items():
    for b,cols in data.items():
        for c in cols:
            h=str(c['header']).lower()
            for w,p in words.items():
                if re.search(p,h): out[w][(sn,c['truth'])]+=1
for w,c in out.items(): print(w,dict(c))
