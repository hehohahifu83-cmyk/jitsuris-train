"""モデルの種類ごとの読み込みの違いを 1 か所にまとめる（2026-10-20）。finetune_exp.py と tests/mmbert_smoke.py が使う。

ModernBERT 系（mmBERT-small など）：
- transformers 4.48〜4.5x では config に reference_compile があり、False にして torch.compile を使わない（長さが毎回違う入力で作り直しが起きる・triton に頼らない）。
  transformers 5.x ではその項目が無く、from_pretrained に渡すと『知らない引数』で落ちる（試運転 2 回目 run 39431299396 で確認）。→ 持っているときだけ設定する。
- 設定の上書きは config オブジェクトに行い、from_pretrained(config=…) で渡す（引数で渡すと版によって落ちる）。
E5（XLM-R 系）など：今までどおり（呼び出し側が num_labels と dropout の引数をそのまま渡す）。ここでは何も変えない。
"""
from __future__ import annotations

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
