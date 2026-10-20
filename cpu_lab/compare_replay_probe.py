#!/usr/bin/env python3
"""Compare audited-replay and baseline jobs on the same held-out synthetic probe."""
from __future__ import annotations
import argparse, json
from pathlib import Path

THRESHOLD_PP = 1.5

def load(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("stage") != "after" or data.get("split") != "progress_probe":
        raise ValueError(f"{path}: expected after-training progress_probe result")
    if data.get("fixed_test_sets_used") is not False or data.get("training_overlap") != 0:
        raise ValueError(f"{path}: invalid probe isolation metadata")
    rows = {x["id"]: x for x in data["predictions"]}
    if len(rows) != data.get("probe_count") or not rows:
        raise ValueError(f"{path}: invalid probe rows/count")
    return data, rows

def compare(baseline_paths, replay_paths, out_path):
    if len(baseline_paths) != 2 or len(replay_paths) != 2:
        raise ValueError("exactly two matched seeds are required per condition")
    pairs = []
    for bp, rp in zip(baseline_paths, replay_paths):
        b, br = load(bp); r, rr = load(rp)
        if str(b.get("seed")) != str(r.get("seed")):
            raise ValueError("baseline and replay seeds do not match")
        if br.keys() != rr.keys() or any(br[i]["target"] != rr[i]["target"] for i in br):
            raise ValueError("probe IDs or gold labels changed")
        if b.get("model_name") != r.get("model_name"):
            raise ValueError("model names do not match")
        n = len(br)
        bc = sum(int(x["correct"]) for x in br.values())
        rc = sum(int(x["correct"]) for x in rr.values())
        pairs.append({"seed": str(b["seed"]), "count": n, "baseline_correct": bc,
                      "replay_correct": rc, "baseline_accuracy": bc/n,
                      "replay_accuracy": rc/n, "delta_pp": (rc-bc)*100/n,
                      "improved": [i for i in br if not br[i]["correct"] and rr[i]["correct"]],
                      "regressed": [i for i in br if br[i]["correct"] and not rr[i]["correct"]]})
    if pairs[0]["count"] != pairs[1]["count"]:
        raise ValueError("probe size differs between seeds")
    mean_delta = sum(p["delta_pp"] for p in pairs) / len(pairs)
    result = {"experiment": "audited_replay_vs_baseline", "probe_count": pairs[0]["count"],
              "seeds": pairs, "mean_delta_pp": mean_delta, "threshold_pp": THRESHOLD_PP,
              "result": "replay_benefit_signal" if mean_delta >= THRESHOLD_PP else
                        "replay_regression_signal" if mean_delta <= -THRESHOLD_PP else
                        "no_difference_under_threshold",
              "interpretation": "diagnostic synthetic probe only; not the fixed-test result"}
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--baseline", nargs=2, required=True); p.add_argument("--replay", nargs=2, required=True)
    p.add_argument("--out", required=True); a=p.parse_args()
    try: print(json.dumps(compare(a.baseline,a.replay,a.out), ensure_ascii=False))
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as e: p.error(str(e))

if __name__ == "__main__": main()
