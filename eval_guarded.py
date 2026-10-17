import sys, exp2
from exp import score
from guard import guard
def evaluate(m, use_guard=True, thr=0.5):
    out = {}
    for tag, mode, pert in (("both","both",False),("崩し","both",True),("header","header",False),("values","values",False)):
        t=[0,0,0,0]
        for seed in range(5):
            ev=exp2.eval_rows(100+seed,mode,pert);P=m.predict_proba(exp2.mat(ev,True));pred=[]
            for (h,v,_),p in zip(ev,P):
                order=sorted(zip(m.classes_,p),key=lambda x:-x[1]);lab=order[0][0] if order[0][1]>=thr else "unknown"
                if use_guard and lab!="unknown": lab=guard(lab,order,v)
                pred.append(lab)
            s=score(pred,[c for *_,c in ev]);t[0]+=s["correct"];t[1]+=s["wrong"];t[2]+=s["unknown"];t[3]+=s["critical"]
        out[tag]=[x/5 for x in t]
    return out
if __name__=="__main__":
    for v2 in (False, True):
        o,m=exp2.run(1500,8,True,v2=v2,share=0.4,return_model=True)
        r=evaluate(m)
        print(f"v2={v2}:", "  ".join(f"{k} 正{a:.1f} 誤{b:.1f} 不明{c:.1f} 重大{d:.1f}" for k,(a,b,c,d) in r.items()))
