"""「わからない」と答える基準（しきい値）を下げたとき、重大な取り違えを 0 にできるか、そのとき答える割合はいくつかを測る。

入力：Kaggle の学習が残した probs_<試験名>_<条件>.json（列名・正解・予測・上位3つの確率。列の値は入らない）。
      eval_reports/latest/ に置かれる。未見セット（blind_set*）は読まない。
方針：重大な取り違えは「数字の種類（date・amount・quantity・rate・id）どうしの取り違え」。
      数字の種類を答えようとしたとき、1位の確率が T_num 未満なら「不明」にする（数字の種類だけに厳しい基準）。
      T_num は一部の試験で決め、決めなかった試験で確かめる（試験ごとに 1 つ外して決める＝leave-one-test-out）。同じ試験で決めて同じ試験で測ると甘くなるため。
使い方：python abstain_eval.py eval_reports/latest [条件名（ft・sparse・blend50・blend60・blend70。既定 blend70）] [置き場（job1・job2・report。省略で全部）]
"""
import glob, json, os, sys
from evaluation_records import summarize_records

NUMERIC = {"date", "amount", "quantity", "rate", "id"}
THRESHOLDS = [round(0.5 + 0.01 * i, 2) for i in range(0, 50)]  # 0.50 〜 0.99


def runs(dir_, cond):
    """置き場の名前の一覧。Kaggle の回収は『<置き場>_probs_<試験>_<条件>.json』（置き場は job1・job2・report など）。
    置き場の付かない名前（probs_…）は空の名前 ""。"""
    found = set()
    for path in glob.glob(os.path.join(dir_, f"*probs_*_{cond}.json")):
        base = os.path.basename(path)
        i = base.find("probs_")
        found.add(base[:i].rstrip("_") if i > 0 else "")
    return sorted(found)


def load(dir_, cond, run=None):
    """run=None で置き場が 1 つだけならそれを読む。複数あるときは取り違えを防ぐため止まる（run を指定する）。"""
    found = runs(dir_, cond)
    if run is None:
        if len(found) > 1:
            raise ValueError(f"置き場が複数ある {found}。どれかを指定する")
        run = found[0] if found else ""
    pattern = f"{run}_probs_*_{cond}.json" if run else f"probs_*_{cond}.json"
    tests = {}
    for path in sorted(glob.glob(os.path.join(dir_, pattern))):
        if "blind" in os.path.basename(path).lower():
            raise RuntimeError("blind test sets must not be evaluated")
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        if d.get("schema_version") != 3:
            raise ValueError(f"unsupported evaluation schema in {os.path.basename(path)}; regenerate with schema_version=3")
        rows = d.get("rows")
        if not isinstance(rows, list):
            raise ValueError(f"missing rows array: {os.path.basename(path)}")
        for row in rows:
            if not isinstance(row, dict):
                raise ValueError(f"malformed evaluation row: {os.path.basename(path)}")
            if row.get("prediction") != row.get("guarded_prediction"):
                raise ValueError(f"legacy prediction alias differs from guarded prediction: {os.path.basename(path)}")
            reason = row.get("decision_reason")
            if reason is not None and not isinstance(reason, str):
                raise ValueError(f"malformed decision reason: {os.path.basename(path)}")
            if row.get("guarded_prediction") == "unknown" and not reason:
                raise ValueError(f"unknown prediction is missing a decision reason: {os.path.basename(path)}")
            if row.get("guarded_prediction") != "unknown" and reason is not None:
                raise ValueError(f"accepted prediction has a decision reason: {os.path.basename(path)}")
            top3 = row.get("top3") or []
            raw = top3[0].get("label") if top3 else None
            if row.get("raw_prediction") != raw:
                raise ValueError(f"raw prediction differs from top-1 probability label: {os.path.basename(path)}")
        summarize_records(rows)  # reject outcome/critical counts that disagree with truth and guarded prediction
        tests[d["test"]] = rows
    return tests


def apply(rows, t_num):
    """しきい値を当てた結果の数え方（score_real と同じ意味）。"""
    c = w = u = k = oc = ow = 0
    for r in rows:
        pred = r["guarded_prediction"]
        p1 = r["top3"][0]["probability"] if r["top3"] else 1.0
        if pred in NUMERIC and p1 < t_num:
            pred = "unknown"
        if r["truth"] == "other":
            if pred in ("unknown", "other"): oc += 1
            else: ow += 1
            continue
        if pred in ("unknown", "other"): u += 1
        elif pred == r["truth"]: c += 1
        else:
            w += 1
            if pred in NUMERIC and r["truth"] in NUMERIC: k += 1
    n = c + w + u
    return {"correct": c, "wrong": w, "unknown": u, "critical": k, "n": n, "acc_all": c / max(n, 1),
            "answered": (c + w) / max(n, 1), "precision": c / max(c + w, 1), "other_ng": ow}


def smallest_safe_threshold(tests, names):
    """names の試験すべてで重大が 0 になる最小の T_num。無ければ None。"""
    for t in THRESHOLDS:
        if all(apply(tests[n], t)["critical"] == 0 for n in names):
            return t
    return None


def report(dir_, cond="blend70", run=None):
    tests = load(dir_, cond, run)
    if not tests:
        return f"{dir_} に probs_*_{cond}.json がない"
    lines = [f"条件 {cond}／試験 {', '.join(tests)}", "", "| 試験 | 今のまま（重大・正解率・答えた割合） | T_num=0.9 | T_num=0.95 | 重大0になる最小の T_num（その試験だけで） |", "|---|---|---|---|---|"]
    def cell(m): return f"{m['acc_all']:.1%}・重大{m['critical']}・答えた{m['answered']:.0%}"
    for n, rows in tests.items():
        base = apply(rows, 0.0)
        lines.append(f"| {n} | {cell(base)} | {cell(apply(rows, 0.9))} | {cell(apply(rows, 0.95))} | {smallest_safe_threshold(tests, [n])} |")
    lines += ["", "試験を 1 つ外して T_num を決め、外した試験で確かめる（leave-one-test-out）：", "", "| 外した試験 | 他の試験で決めた T_num | 外した試験の結果（正解率・重大・答えた割合） |", "|---|---|---|"]
    names = list(tests)
    for held in names:
        others = [n for n in names if n != held]
        t = smallest_safe_threshold(tests, others) if others else None
        lines.append(f"| {held} | {t} | " + (cell(apply(tests[held], t)) if t is not None else "決められない（重大 0 にならない）") + " |")
    allt = smallest_safe_threshold(tests, names)
    lines += ["", f"全試験で重大 0 になる最小の T_num：{allt}（すべての試験で決めた値。未見の試験で同じになる保証はない）"]
    return "\n".join(lines)


if __name__ == "__main__":
    d_ = sys.argv[1] if len(sys.argv) > 1 else "eval_reports/latest"
    c_ = sys.argv[2] if len(sys.argv) > 2 else "blend70"
    r_ = sys.argv[3] if len(sys.argv) > 3 else None
    for run_ in ([r_] if r_ is not None else (runs(d_, c_) or [""])):
        print(f"## 置き場：{run_ or '（なし）'}\n")
        print(report(d_, c_, run_))
        print()
