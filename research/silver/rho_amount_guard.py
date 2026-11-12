"""rho の金額の守り（2026-11-13 Claude。読むだけの形。bench/silver24_prereg_20261113.md）。
前回の銀の学習（C3b）で増えた重大は全部、rho（不明を言い切りに戻す段）が本体の amount に戻した列だった（research/silver_crit_why.md、Codex の再現 research/silver_review_codex/）。
守り：rho が amount に戻すのは、列名に金額の強い手がかり（recheck.cue_types に amount）があるときだけ。無ければ不明のまま。
"""
import recheck
import verifier as V

_orig = V.candidate


def guarded_candidate(label, why, guarded, top3, header, p_row, labels, rho):
    t = _orig(label, why, guarded, top3, header, p_row, labels, rho)
    if t == "amount" and "amount" not in recheck.cue_types(header, ""):
        return None
    return t


class use:
    """with use(): の中だけ V.candidate を守りつきにする。"""
    def __enter__(self):
        V.candidate = guarded_candidate

    def __exit__(self, *a):
        V.candidate = _orig
