"""Trainable table-aware ensemble for Jitsuris (research only).

The base classifiers remain separate. A small nonlinear meta-classifier learns
which expert signals and same-table peer predictions are useful for each row.
A second, selective gate is calibrated on disjoint table groups; it can abstain
but cannot invent a label.

Training requires table-grouped out-of-fold base probabilities. Do not pass
in-sample predictions or evaluation-set labels.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Optional, Sequence, Tuple

import numpy as np


@dataclass(frozen=True)
class MetaDecision:
    prediction: str
    candidate: Optional[str]
    raw_prediction: str
    confidence: float
    critical_risk: float
    reason: str
    top3: Tuple[Tuple[str, float], ...]


class TableGraphRiskFusion:
    """Learn a nonlinear stacker, same-table message passing, and abstention.

    The default calibration goals follow Jitsuris' stated product constraints:
    zero observed critical errors, no more than 5% observed total errors among
    asserted outputs, and no more than 10% unknown outputs. These are empirical
    calibration targets, not statistical guarantees.
    """

    def __init__(
        self,
        labels: Sequence[str],
        *,
        critical_labels: Sequence[str] = ("date", "amount", "quantity", "rate", "id"),
        catch_all_label: Optional[str] = "other",
        unknown_label: str = "unknown",
        max_critical_error_rate: float = 0.0,
        max_overall_error_rate: float = 0.05,
        max_unknown_rate: float = 0.10,
        min_calibration_groups: int = 20,
        min_calibration_rows: int = 100,
        min_risk_positives: int = 8,
        n_splits: int = 5,
        random_state: int = 0,
    ) -> None:
        self.labels = tuple(labels)
        self.critical_labels = tuple(critical_labels)
        self.catch_all_label = catch_all_label
        self.unknown_label = unknown_label
        self.max_critical_error_rate = float(max_critical_error_rate)
        self.max_overall_error_rate = float(max_overall_error_rate)
        self.max_unknown_rate = float(max_unknown_rate)
        self.min_calibration_groups = int(min_calibration_groups)
        self.min_calibration_rows = int(min_calibration_rows)
        self.min_risk_positives = int(min_risk_positives)
        self.n_splits = int(n_splits)
        self.random_state = int(random_state)
        if not self.labels or len(set(self.labels)) != len(self.labels):
            raise ValueError("labels must be nonempty and unique")
        if self.unknown_label in self.labels:
            raise ValueError("unknown_label must be outside the trained label set")
        if not set(self.critical_labels).issubset(self.labels):
            raise ValueError("critical_labels must be contained in labels")
        if self.catch_all_label is not None and self.catch_all_label not in self.labels:
            raise ValueError("catch_all_label must be a trained label or None")
        for name, value in (
            ("max_critical_error_rate", self.max_critical_error_rate),
            ("max_overall_error_rate", self.max_overall_error_rate),
            ("max_unknown_rate", self.max_unknown_rate),
        ):
            if not 0 <= value <= 1:
                raise ValueError(f"{name} must be in [0, 1]")
        if self.n_splits < 2:
            raise ValueError("n_splits must be at least 2")

        self.source_names_: Optional[Tuple[str, ...]] = None
        self.classifier_ = None
        self.risk_model_ = None
        self.risk_mode_: Optional[str] = None
        self.risk_threshold_: Optional[float] = None
        self.confidence_threshold_: Optional[float] = None
        self.fit_info_: dict = {}

    def fit(
        self,
        train_probabilities: Mapping[str, np.ndarray],
        train_labels: Sequence[str],
        train_table_ids: Sequence[object],
        calibration_probabilities: Mapping[str, np.ndarray],
        calibration_labels: Sequence[str],
        calibration_table_ids: Sequence[object],
        *,
        base_predictions_are_oof: bool,
        calibration_is_held_out: bool,
    ) -> "TableGraphRiskFusion":
        """Fit only from base OOF predictions plus a separate calibration split.

        The two Boolean arguments are explicit attestations by the caller.
        The table-ID overlap check below catches accidental group reuse, but
        cannot verify how the base model artifacts themselves were produced.
        """
        if base_predictions_are_oof is not True:
            raise ValueError("training probabilities must be out-of-fold by whole table")
        if calibration_is_held_out is not True:
            raise ValueError("calibration rows must be held out by whole table")
        source_names = tuple(sorted(train_probabilities))
        if "encoder" not in source_names or "sparse" not in source_names:
            raise ValueError("include at least the encoder and sparse classifiers")
        if tuple(sorted(calibration_probabilities)) != source_names:
            raise ValueError("train and calibration source names must match exactly")

        train_y = self._labels_array(train_labels, "train_labels")
        cal_y = self._labels_array(calibration_labels, "calibration_labels")
        train_groups = self._group_array(train_table_ids, len(train_y), "train_table_ids")
        cal_groups = self._group_array(calibration_table_ids, len(cal_y), "calibration_table_ids")
        train_group_set, cal_group_set = set(train_groups), set(cal_groups)
        overlap = train_group_set.intersection(cal_group_set)
        if overlap:
            raise ValueError(f"table groups occur in both train and calibration: {len(overlap)}")
        if len(train_group_set) < self.n_splits:
            raise ValueError(f"need at least {self.n_splits} training table groups for cross-fitting")
        if len(cal_group_set) < self.min_calibration_groups:
            raise ValueError(
                f"need at least {self.min_calibration_groups} independent calibration tables"
            )
        if len(cal_y) < self.min_calibration_rows:
            raise ValueError(f"need at least {self.min_calibration_rows} calibration rows")
        if set(train_y) != set(self.labels):
            missing = sorted(set(self.labels) - set(train_y))
            raise ValueError(f"training labels must include every configured class; missing={missing}")

        train_sources = self._validate_sources(train_probabilities, len(train_y), source_names)
        cal_sources = self._validate_sources(calibration_probabilities, len(cal_y), source_names)
        x_train = self._build_features(train_sources, train_groups)
        x_cal = self._build_features(cal_sources, cal_groups)

        # Cross-fit the stacker itself to create honest examples for the risk model.
        from sklearn.model_selection import GroupKFold

        splitter = GroupKFold(n_splits=self.n_splits)
        oof_meta = np.zeros((len(train_y), len(self.labels)), dtype=np.float64)
        fold_count = 0
        for tr, va in splitter.split(x_train, train_y, groups=train_groups):
            model = self._new_classifier()
            if len(set(train_y[tr])) == 1:
                prior = np.zeros(len(self.labels), dtype=np.float64)
                prior[self.labels.index(train_y[tr][0])] = 1.0
                oof_meta[va] = prior
            else:
                model.fit(x_train[tr], train_y[tr])
                oof_meta[va] = self._aligned_probabilities(model, x_train[va])
            fold_count += 1

        oof_pred = np.asarray(self.labels, dtype=object)[np.argmax(oof_meta, axis=1)]
        critical_targets = np.asarray(
            [
                int(pred != truth and (pred in self.critical_labels or truth in self.critical_labels))
                for pred, truth in zip(oof_pred, train_y)
            ],
            dtype=np.int8,
        )
        positives = int(critical_targets.sum())
        self.risk_model_ = None
        self.risk_mode_ = "confidence_disagreement_fallback"
        if positives >= self.min_risk_positives and positives < len(critical_targets):
            from sklearn.linear_model import LogisticRegression

            self.risk_model_ = LogisticRegression(
                C=0.5,
                class_weight="balanced",
                max_iter=1000,
                random_state=self.random_state,
            )
            self.risk_model_.fit(x_train, critical_targets)
            self.risk_mode_ = "learned_critical_error_risk"

        self.classifier_ = self._new_classifier()
        self.classifier_.fit(x_train, train_y)
        cal_probs = self._aligned_probabilities(self.classifier_, x_cal)
        cal_risk = self._risk_scores(x_cal, cal_sources, cal_probs)
        self.risk_threshold_, self.confidence_threshold_ = self._calibrate(
            cal_probs, cal_risk, cal_y
        )
        self.source_names_ = source_names
        self.fit_info_ = {
            "train_rows": int(len(train_y)),
            "train_tables": int(len(train_group_set)),
            "calibration_rows": int(len(cal_y)),
            "calibration_tables": int(len(cal_group_set)),
            "meta_crossfit_folds": fold_count,
            "critical_oof_errors": positives,
            "risk_mode": self.risk_mode_,
            "risk_threshold": self.risk_threshold_,
            "confidence_threshold": self.confidence_threshold_,
            "calibration_targets": {
                "critical_error_rate": self.max_critical_error_rate,
                "overall_error_rate": self.max_overall_error_rate,
                "unknown_rate": self.max_unknown_rate,
            },
        }
        return self

    def predict(
        self,
        probabilities: Mapping[str, np.ndarray],
        table_ids: Sequence[object],
    ) -> list[MetaDecision]:
        """Predict with the learned gate and calibrated selective boundary."""
        if self.classifier_ is None or self.source_names_ is None:
            raise RuntimeError("fit must complete before predict")
        if tuple(sorted(probabilities)) != self.source_names_:
            raise ValueError("prediction source names differ from the fitted source names")
        first = np.asarray(probabilities[self.source_names_[0]])
        if first.ndim != 2 or first.shape[1] != len(self.labels):
            raise ValueError("each source must provide rows-by-labels probabilities")
        groups = self._group_array(table_ids, first.shape[0], "table_ids")
        sources = self._validate_sources(probabilities, first.shape[0], self.source_names_)
        x = self._build_features(sources, groups)
        probs = self._aligned_probabilities(self.classifier_, x)
        risk = self._risk_scores(x, sources, probs)

        decisions: list[MetaDecision] = []
        for i, row in enumerate(probs):
            order = np.argsort(-row, kind="stable")
            best = int(order[0])
            raw = self.labels[best]
            confidence = float(row[best])
            rejected = False
            reason = "accepted"
            if raw == self.catch_all_label:
                rejected, reason = True, "catch_all_abstained"
            elif risk[i] > float(self.risk_threshold_):
                rejected, reason = True, "critical_risk_above_threshold"
            elif confidence < float(self.confidence_threshold_):
                rejected, reason = True, "confidence_below_threshold"

            prediction = self.unknown_label if rejected else raw
            candidate = raw if rejected and raw != self.catch_all_label else None
            top3 = tuple(
                (self.labels[int(j)], float(row[int(j)]))
                for j in order[: min(3, len(self.labels))]
            )
            decisions.append(
                MetaDecision(
                    prediction=prediction,
                    candidate=candidate,
                    raw_prediction=raw,
                    confidence=confidence,
                    critical_risk=float(risk[i]),
                    reason=reason,
                    top3=top3,
                )
            )
        return decisions

    def predict_proba(
        self,
        probabilities: Mapping[str, np.ndarray],
        table_ids: Sequence[object],
    ) -> tuple[np.ndarray, np.ndarray]:
        """Return calibrated-stack probabilities and critical-risk scores."""
        if self.classifier_ is None or self.source_names_ is None:
            raise RuntimeError("fit must complete before predict_proba")
        if tuple(sorted(probabilities)) != self.source_names_:
            raise ValueError("prediction source names differ from the fitted source names")
        first = np.asarray(probabilities[self.source_names_[0]])
        if first.ndim != 2 or first.shape[1] != len(self.labels):
            raise ValueError("each source must provide rows-by-labels probabilities")
        groups = self._group_array(table_ids, first.shape[0], "table_ids")
        sources = self._validate_sources(probabilities, first.shape[0], self.source_names_)
        x = self._build_features(sources, groups)
        probs = self._aligned_probabilities(self.classifier_, x)
        return probs, self._risk_scores(x, sources, probs)

    def _labels_array(self, values: Sequence[str], name: str) -> np.ndarray:
        arr = np.asarray(values, dtype=object)
        if arr.ndim != 1 or not len(arr):
            raise ValueError(f"{name} must be a nonempty one-dimensional sequence")
        invalid = sorted(set(arr) - set(self.labels))
        if invalid:
            raise ValueError(f"{name} contains labels outside the configured set: {invalid}")
        return arr

    @staticmethod
    def _group_array(values: Sequence[object], rows: int, name: str) -> np.ndarray:
        arr = np.asarray(values, dtype=object)
        if arr.shape != (rows,):
            raise ValueError(f"{name} must have one table ID per row")
        if any(value is None or value == "" for value in arr):
            raise ValueError(f"{name} cannot contain missing table IDs")
        try:
            for value in arr:
                hash(value)
        except TypeError as exc:
            raise ValueError(f"{name} values must be hashable") from exc
        return arr

    def _validate_sources(
        self,
        raw: Mapping[str, np.ndarray],
        rows: int,
        names: Sequence[str],
    ) -> dict[str, np.ndarray]:
        if tuple(sorted(raw)) != tuple(names):
            raise ValueError("source names must match exactly")
        out = {}
        for name in names:
            arr = np.asarray(raw[name], dtype=np.float64)
            if arr.shape != (rows, len(self.labels)):
                raise ValueError(
                    f"{name} must have shape {(rows, len(self.labels))}; received {arr.shape}"
                )
            if not np.isfinite(arr).all() or (arr < 0).any():
                raise ValueError(f"{name} must contain finite, nonnegative probabilities")
            mass = arr.sum(axis=1, keepdims=True)
            if (mass <= 0).any():
                raise ValueError(f"{name} contains a row with zero probability mass")
            out[name] = arr / mass
        return out

    def _build_features(
        self,
        sources: Mapping[str, np.ndarray],
        table_ids: np.ndarray,
    ) -> np.ndarray:
        """Build expert-score, uncertainty, agreement, and leave-one-out table features."""
        base = []
        top = []
        for name in self.source_names_ or tuple(sorted(sources)):
            p = sources[name]
            order = np.argsort(-p, axis=1, kind="stable")
            top.append(order[:, 0])
            base.append(p)
            sorted_p = np.take_along_axis(p, order, axis=1)
            margin = sorted_p[:, 0] - sorted_p[:, 1]
            entropy = -(p * np.log(np.clip(p, 1e-12, 1.0))).sum(axis=1)
            entropy /= max(np.log(len(self.labels)), 1e-12)
            base.extend((sorted_p[:, :1], margin[:, None], entropy[:, None]))

        pair_agreement = []
        for i in range(len(top)):
            for j in range(i + 1, len(top)):
                pair_agreement.append((top[i] == top[j]).astype(np.float64)[:, None])
        if pair_agreement:
            base.append(np.hstack(pair_agreement))

        # Leave-one-column-out message passing on the table graph. Only peer
        # predictions are shared; no labels or target-column values are copied.
        table_to_rows: dict[object, list[int]] = {}
        for i, table_id in enumerate(table_ids):
            table_to_rows.setdefault(table_id, []).append(i)
        peer_count = np.zeros((len(table_ids), 1), dtype=np.float64)
        for name in self.source_names_ or tuple(sorted(sources)):
            p = sources[name]
            peer_mean = np.zeros_like(p)
            peer_top = np.zeros_like(p)
            one_hot = np.eye(len(self.labels), dtype=np.float64)[np.argmax(p, axis=1)]
            for row_ids in table_to_rows.values():
                if len(row_ids) < 2:
                    continue
                idx = np.asarray(row_ids, dtype=np.int64)
                sum_p = p[idx].sum(axis=0)
                sum_top = one_hot[idx].sum(axis=0)
                for row_id in row_ids:
                    peer_mean[row_id] = (sum_p - p[row_id]) / (len(row_ids) - 1)
                    peer_top[row_id] = (sum_top - one_hot[row_id]) / (len(row_ids) - 1)
                    peer_count[row_id, 0] = len(row_ids) - 1
            base.extend((peer_mean, peer_top))
        base.append(np.log1p(peer_count))
        return np.hstack(base)

    def _new_classifier(self):
        from sklearn.ensemble import HistGradientBoostingClassifier

        return HistGradientBoostingClassifier(
            learning_rate=0.08,
            max_iter=180,
            max_leaf_nodes=15,
            min_samples_leaf=20,
            l2_regularization=1.0,
            early_stopping=False,
            random_state=self.random_state,
        )

    def _aligned_probabilities(self, model, x: np.ndarray) -> np.ndarray:
        raw = model.predict_proba(x)
        out = np.zeros((len(x), len(self.labels)), dtype=np.float64)
        for j, label in enumerate(model.classes_):
            out[:, self.labels.index(label)] = raw[:, j]
        mass = out.sum(axis=1, keepdims=True)
        mass[mass <= 0] = 1.0
        return out / mass

    def _risk_scores(
        self,
        x: np.ndarray,
        sources: Mapping[str, np.ndarray],
        stacked_probabilities: np.ndarray,
    ) -> np.ndarray:
        if self.risk_model_ is not None:
            raw = self.risk_model_.predict_proba(x)
            positive_col = list(self.risk_model_.classes_).index(1)
            return raw[:, positive_col]
        confidence = stacked_probabilities.max(axis=1)
        tops = [
            np.argmax(sources[name], axis=1)
            for name in (self.source_names_ or tuple(sorted(sources)))
        ]
        agreement = np.zeros(len(confidence), dtype=np.float64)
        if tops:
            top_matrix = np.vstack(tops)
            for i in range(len(confidence)):
                counts = np.bincount(top_matrix[:, i], minlength=len(self.labels))
                agreement[i] = counts.max() / len(tops)
        return np.clip(0.60 * (1.0 - confidence) + 0.40 * (1.0 - agreement), 0.0, 1.0)

    def _calibrate(
        self,
        probabilities: np.ndarray,
        risk: np.ndarray,
        truth: np.ndarray,
    ) -> tuple[float, float]:
        confidence = probabilities.max(axis=1)
        raw = np.asarray(self.labels, dtype=object)[np.argmax(probabilities, axis=1)]
        mismatch = raw != truth
        critical_error = np.asarray(
            [
                int(wrong and (pred in self.critical_labels or actual in self.critical_labels))
                for wrong, pred, actual in zip(mismatch, raw, truth)
            ],
            dtype=np.int8,
        )
        assertable = np.ones(len(truth), dtype=bool)
        if self.catch_all_label is not None:
            assertable &= raw != self.catch_all_label

        risk_grid = np.unique(np.quantile(risk, np.linspace(0.0, 1.0, 41)))
        conf_grid = np.unique(np.quantile(confidence, np.linspace(0.0, 1.0, 41)))
        best = None
        for risk_threshold in risk_grid:
            for confidence_threshold in conf_grid:
                accepted = (
                    assertable
                    & (risk <= risk_threshold)
                    & (confidence >= confidence_threshold)
                )
                n_accepted = int(accepted.sum())
                if not n_accepted:
                    continue
                unknown_rate = 1.0 - n_accepted / len(truth)
                if unknown_rate > self.max_unknown_rate:
                    continue
                critical_rate = float(critical_error[accepted].mean())
                overall_error_rate = float(mismatch[accepted].mean())
                if critical_rate > self.max_critical_error_rate:
                    continue
                if overall_error_rate > self.max_overall_error_rate:
                    continue
                score = (
                    n_accepted,
                    -int(critical_error[accepted].sum()),
                    -int(mismatch[accepted].sum()),
                    float(risk_threshold),
                    -float(confidence_threshold),
                )
                if best is None or score > best[0]:
                    best = (score, float(risk_threshold), float(confidence_threshold))
        if best is None:
            raise ValueError(
                "no calibration thresholds meet all configured targets; "
                "do not relax them using a fixed evaluation or sealed set"
            )
        return best[1], best[2]
