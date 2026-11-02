"""Jitsuris experimental multi-view late fusion (research only).

This module combines already-produced probabilities. It does not load or alter
model weights and deliberately has no default weights or decision thresholds:
those must be selected from table-grouped out-of-fold calibration data.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Optional, Sequence, Tuple

import numpy as np


@dataclass(frozen=True)
class FusionPolicy:
    """Calibrated settings for one frozen candidate.

    source_weights:
        Nonnegative weights for probability-producing classifiers such as
        the multilingual encoder and the sparse feature model. The weights
        must be fixed before evaluating a held-out set.
    thresholds:
        Per-label acceptance thresholds, optionally with "*" as a fallback.
    value_veto_threshold:
        If set, a value-only verifier may abstain a numeric prediction when
        it strongly prefers a different numeric label. It never supplies a
        replacement prediction.
    numeric_rescue_threshold:
        If set, a numeric specialist may supply a review candidate when a
        strong deterministic cue agrees and the encoder places that label in
        its top three. It never changes the asserted prediction.
    """

    source_weights: Mapping[str, float]
    thresholds: Mapping[str, float]
    numeric_labels: Tuple[str, ...] = ("date", "amount", "quantity", "rate", "id")
    min_numeric_margin: float = 0.0
    value_veto_threshold: Optional[float] = None
    numeric_rescue_threshold: Optional[float] = None
    abstain_label: str = "unknown"
    catch_all_label: Optional[str] = "other"

    def __post_init__(self) -> None:
        if not self.source_weights:
            raise ValueError("source_weights must contain at least one source")
        if any(not np.isfinite(w) or w < 0 for w in self.source_weights.values()):
            raise ValueError("source weights must be finite and nonnegative")
        if sum(self.source_weights.values()) <= 0:
            raise ValueError("at least one source weight must be positive")
        if not self.thresholds:
            raise ValueError("thresholds must be calibrated explicitly")
        if any(not np.isfinite(t) or not 0 <= t <= 1 for t in self.thresholds.values()):
            raise ValueError("acceptance thresholds must be in [0, 1]")
        if not np.isfinite(self.min_numeric_margin) or not 0 <= self.min_numeric_margin <= 1:
            raise ValueError("min_numeric_margin must be in [0, 1]")
        for name, value in (
            ("value_veto_threshold", self.value_veto_threshold),
            ("numeric_rescue_threshold", self.numeric_rescue_threshold),
        ):
            if value is not None and (not np.isfinite(value) or not 0 <= value <= 1):
                raise ValueError(f"{name} must be in [0, 1]")


@dataclass(frozen=True)
class FusedDecision:
    prediction: str
    candidate: Optional[str]
    confidence: float
    reason: str
    top3: Tuple[Tuple[str, float], ...]
    source_top1: Mapping[str, str]


def _probabilities(value: np.ndarray, rows: int, labels: Sequence[str], name: str) -> np.ndarray:
    arr = np.asarray(value, dtype=np.float64)
    if arr.shape != (rows, len(labels)):
        raise ValueError(
            f"{name} must have shape {(rows, len(labels))}; received {arr.shape}"
        )
    if not np.isfinite(arr).all() or (arr < 0).any():
        raise ValueError(f"{name} must contain finite, nonnegative probabilities")
    totals = arr.sum(axis=1, keepdims=True)
    if (totals <= 0).any():
        raise ValueError(f"{name} contains a row with zero probability mass")
    return arr / totals


def _top_index(row: np.ndarray) -> int:
    # Stable ordering makes tied outputs reproducible.
    return int(np.argsort(-row, kind="stable")[0])


def _threshold(label: str, labels: Sequence[str], thresholds: Mapping[str, float]) -> float:
    if label in thresholds:
        return float(thresholds[label])
    if "*" in thresholds:
        return float(thresholds["*"])
    missing = sorted(set(labels) - set(thresholds))
    raise ValueError(f"thresholds must cover every model label or provide '*'; missing={missing}")


def fuse_columns(
    source_probabilities: Mapping[str, np.ndarray],
    labels: Sequence[str],
    policy: FusionPolicy,
    *,
    value_only_probabilities: Optional[np.ndarray] = None,
    numeric_specialist_probabilities: Optional[np.ndarray] = None,
    strong_numeric_cues: Optional[Sequence[Optional[str]]] = None,
) -> list[FusedDecision]:
    """Fuse model views and apply conservative abstention.

    Required base views are encoder and sparse. More probability sources may
    be added by placing their calibrated weights in the policy. All matrices
    use the same label order and contain one row per column.

    The value-only model is a veto, not a voting classifier. The numeric
    specialist can provide a review candidate only; it cannot override the
    fused assertion. Final unknown decisions can still carry that candidate.
    """
    labels = tuple(labels)
    if not labels or len(set(labels)) != len(labels):
        raise ValueError("labels must be nonempty and unique")
    if policy.abstain_label in labels:
        raise ValueError("abstain_label must be a sentinel outside the trained labels")
    if "encoder" not in source_probabilities or "sparse" not in source_probabilities:
        raise ValueError("source_probabilities must include both 'encoder' and 'sparse'")
    if set(source_probabilities) != set(policy.source_weights):
        raise ValueError(
            "source names must match policy.source_weights exactly "
            f"(sources={sorted(source_probabilities)}, weights={sorted(policy.source_weights)})"
        )
    if not set(policy.numeric_labels).issubset(labels):
        raise ValueError("numeric_labels must be contained in labels")
    if "*" not in policy.thresholds and not set(labels).issubset(policy.thresholds):
        missing = sorted(set(labels) - set(policy.thresholds))
        raise ValueError(f"thresholds must cover every model label or provide '*'; missing={missing}")

    first = np.asarray(source_probabilities["encoder"])
    if first.ndim != 2 or first.shape[1] != len(labels):
        raise ValueError("encoder probabilities must be a rows-by-labels matrix")
    n_rows = first.shape[0]
    sources = {
        name: _probabilities(value, n_rows, labels, name)
        for name, value in source_probabilities.items()
    }
    total_weight = float(sum(policy.source_weights.values()))
    fused = sum(
        (float(policy.source_weights[name]) / total_weight) * sources[name]
        for name in sources
    )
    fused /= fused.sum(axis=1, keepdims=True)

    verifier = None
    if value_only_probabilities is not None:
        if policy.value_veto_threshold is None:
            raise ValueError("value_veto_threshold is required when a verifier is supplied")
        verifier = _probabilities(value_only_probabilities, n_rows, labels, "value_only_probabilities")

    specialist = None
    if numeric_specialist_probabilities is not None:
        if policy.numeric_rescue_threshold is None:
            raise ValueError("numeric_rescue_threshold is required when a specialist is supplied")
        if strong_numeric_cues is None or len(strong_numeric_cues) != n_rows:
            raise ValueError("one strong_numeric_cues item is required per input row")
        raw_specialist = np.asarray(numeric_specialist_probabilities, dtype=np.float64)
        numeric_width = len(policy.numeric_labels)
        if raw_specialist.shape == (n_rows, numeric_width):
            if not np.isfinite(raw_specialist).all() or (raw_specialist < 0).any():
                raise ValueError("numeric specialist must contain finite, nonnegative probabilities")
            totals = raw_specialist.sum(axis=1, keepdims=True)
            if (totals <= 0).any():
                raise ValueError("numeric specialist contains a row with zero probability mass")
            specialist = raw_specialist / totals
        else:
            specialist = _probabilities(
                raw_specialist, n_rows, labels, "numeric_specialist_probabilities"
            )
    elif strong_numeric_cues is not None:
        raise ValueError("strong_numeric_cues requires numeric_specialist_probabilities")

    numeric_indices = [labels.index(label) for label in policy.numeric_labels]
    decisions: list[FusedDecision] = []
    for i in range(n_rows):
        row = fused[i]
        order = np.argsort(-row, kind="stable")
        winner_index = int(order[0])
        winner = labels[winner_index]
        confidence = float(row[winner_index])
        prediction = winner
        reason = "accepted"

        # The specialist only proposes a candidate supported by both an
        # explicit cue and the encoder's top-three set.
        candidate = None
        if specialist is not None:
            cue = strong_numeric_cues[i]
            if cue in policy.numeric_labels:
                cue_index = labels.index(cue)
                encoder_order = np.argsort(-sources["encoder"][i], kind="stable")[:3]
                if (
                    cue_index in encoder_order
                    and specialist[
                        i,
                        policy.numeric_labels.index(cue)
                        if specialist.shape[1] == len(policy.numeric_labels)
                        else cue_index,
                    ] >= float(policy.numeric_rescue_threshold)
                ):
                    candidate = cue

        # The value-only verifier can reject a numeric assertion, but never
        # writes its own label into the result.
        if prediction in policy.numeric_labels and verifier is not None:
            verifier_index = _top_index(verifier[i])
            verifier_label = labels[verifier_index]
            if (
                verifier_label in policy.numeric_labels
                and verifier_label != prediction
                and verifier[i, winner_index] < float(policy.value_veto_threshold)
            ):
                prediction = policy.abstain_label
                reason = "value_verifier_conflict"

        if prediction in policy.numeric_labels and policy.min_numeric_margin > 0:
            numeric_scores = sorted((float(row[j]) for j in numeric_indices), reverse=True)
            if len(numeric_scores) > 1 and numeric_scores[0] - numeric_scores[1] < policy.min_numeric_margin:
                prediction = policy.abstain_label
                reason = "numeric_margin_below_threshold"

        if prediction == winner and confidence < _threshold(winner, labels, policy.thresholds):
            prediction = policy.abstain_label
            reason = "confidence_below_threshold"

        if prediction == policy.catch_all_label:
            prediction = policy.abstain_label
            reason = "catch_all_abstained"

        if candidate == prediction:
            candidate = None

        top3 = tuple(
            (labels[int(j)], float(row[int(j)]))
            for j in order[: min(3, len(labels))]
        )
        source_top1 = {
            name: labels[_top_index(probabilities[i])]
            for name, probabilities in sources.items()
        }
        decisions.append(
            FusedDecision(
                prediction=prediction,
                candidate=candidate,
                confidence=confidence,
                reason=reason,
                top3=top3,
                source_top1=source_top1,
            )
        )
    return decisions
