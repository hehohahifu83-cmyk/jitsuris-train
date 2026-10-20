"""モデルの種類ごとの読み込みの違いを 1 か所にまとめる（2026-10-20）。finetune_exp.py と tests/mmbert_smoke.py が使う。

ModernBERT 系（mmBERT-small など）：
- transformers 4.48〜4.5x では config に reference_compile があり、False にして torch.compile を使わない（長さが毎回違う入力で作り直しが起きる・triton に頼らない）。
  transformers 5.x ではその項目が無く、from_pretrained に渡すと『知らない引数』で落ちる（試運転 2 回目 run 39431299396 で確認）。→ 持っているときだけ設定する。
- 設定の上書きは config オブジェクトに行い、from_pretrained(config=…) で渡す（引数で渡すと版によって落ちる）。
E5（XLM-R 系）など：今までどおり（呼び出し側が num_labels と dropout の引数をそのまま渡す）。ここでは何も変えない。
"""
from __future__ import annotations

import math
import os
import re

MODERNBERT_DROPOUTS = ("attention_dropout", "mlp_dropout", "embedding_dropout", "classifier_dropout")
XLMR_DROPOUTS = {"hidden_dropout_prob": 0.0, "attention_probs_dropout_prob": 0.0}


def apply_modernbert_overrides(cfg, num_labels=None, pooling="", no_dropout=False):
    """config に上書きを行い、実際に変えた項目の辞書を返す（学習の記録に残す）。"""
    changes = {}
    if hasattr(cfg, "reference_compile"):
        cfg.reference_compile = False
        changes["reference_compile"] = False
    pooling = (pooling or "").strip()
    if pooling:
        if pooling not in ("cls", "mean"):
            raise ValueError(f"FT_POOLING must be cls or mean: {pooling}")
        cfg.classifier_pooling = pooling
        changes["classifier_pooling"] = pooling
    if no_dropout:
        for key in MODERNBERT_DROPOUTS:
            if hasattr(cfg, key):
                setattr(cfg, key, 0.0)
                changes[key] = 0.0
    if num_labels is not None:
        cfg.num_labels = int(num_labels)
        changes["num_labels"] = int(num_labels)
    return changes


def no_dropout_args(model_type):
    """E5 などの FT_NO_DROPOUT=1 のときの from_pretrained の引数（今までどおり）。"""
    return {} if model_type == "modernbert" else dict(XLMR_DROPOUTS)


# ---- 重みが pytorch_model.bin だけの repo（mmBERT-small）の読み込み ----
# transformers は、torch が 2.6 未満だと .bin の読み込みを断る（torch.load の脆弱性への対応）。Kaggle の torch が古い場合の逃げ道として、
# safetensors に置き直す。置き直しは torch.load(weights_only=True)（任意のコードを動かさない読み方）で行う。
# 並べて流す仕事が同じ置き場を使うので、仕事を流す前に親（kaggle/run.py）が 1 回だけ行う。
def torch_version_tuple(version_text):
    nums = re.findall(r"\d+", version_text or "")
    return tuple(int(x) for x in nums[:2]) if len(nums) >= 2 else (0, 0)


def needs_bin_conversion(model_dir, torch_version, force=False):
    """safetensors が無く pytorch_model.bin だけがあり、torch が 2.6 未満（または force）なら True。"""
    if not model_dir or not os.path.isdir(model_dir):
        return False
    names = os.listdir(model_dir)
    if any(n.endswith(".safetensors") for n in names) or "pytorch_model.bin" not in names:
        return False
    return bool(force) or torch_version_tuple(torch_version) < (2, 6)


def convert_bin_to_safetensors(model_dir):
    """pytorch_model.bin を model.safetensors に置き直す（元の .bin は残す）。返すのは (出力のパス, テンソルの数)。"""
    import torch
    from safetensors.torch import save_file
    state = torch.load(os.path.join(model_dir, "pytorch_model.bin"), map_location="cpu", weights_only=True)
    state = {k: v.detach().contiguous().clone() for k, v in state.items()}   # 重みを共有しているテンソルは safetensors が嫌うので複製する
    out = os.path.join(model_dir, "model.safetensors")
    save_file(state, out, metadata={"format": "pt"})
    return out, len(state)


# ---- 損失が有限でない状態が続いたときの扱い（fp16 の桁あふれ対策）----
class NonFiniteGuard:
    """100 step ごとに見る損失が、有限でない状態を limit 回続けて見たとき：
    fp16 を使っていて fallback が許されていれば 'fallback'（fp32 に切り替える。重みは GradScaler が更新を飛ばしているので壊れていない）、
    そうでなければ例外（何も学ばないまま結果だけ出るのを防ぐ）。それ以外は 'ok'。"""

    def __init__(self, amp_on, fallback, limit=3):
        self.amp_on, self.fallback, self.limit = bool(amp_on), bool(fallback), int(limit)
        self.count, self.fallback_step = 0, None

    def observe(self, loss_value, step):
        if math.isfinite(loss_value):
            self.count = 0
            return "ok"
        self.count += 1
        if self.count < self.limit:
            return "ok"
        if self.amp_on and self.fallback:
            self.amp_on, self.fallback_step, self.count = False, step, 0
            return "fallback"
        raise RuntimeError(f"損失が {self.limit} 回続けて有限でない（学習が壊れている）")
