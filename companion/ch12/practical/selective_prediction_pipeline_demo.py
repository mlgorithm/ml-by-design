"""Demonstrate selective prediction with a finite human-review budget."""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_dataset(seed: int = 42) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    n_examples = 1800

    attendance_drop = np.clip(rng.normal(0.35, 0.18, n_examples), 0.0, 1.0)
    assignment_gap = np.clip(rng.normal(0.30, 0.20, n_examples), 0.0, 1.0)
    grade_drop = np.clip(rng.normal(0.25, 0.16, n_examples), 0.0, 1.0)
    lms_inactivity = np.clip(rng.normal(0.32, 0.18, n_examples), 0.0, 1.0)

    features = np.column_stack(
        [attendance_drop, assignment_gap, grade_drop, lms_inactivity]
    )
    latent_risk = (
        2.2 * attendance_drop
        + 1.7 * assignment_gap
        + 1.4 * grade_drop
        + 1.2 * lms_inactivity
        + rng.normal(0.0, 0.45, n_examples)
    )
    labels = (latent_risk > 1.85).astype(int)
    return features, labels


def simulate_reviewer_predictions(
    true_labels: np.ndarray, accuracy: float, seed: int = 7
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    correct_mask = rng.random(len(true_labels)) < accuracy
    predictions = true_labels.copy()
    predictions[~correct_mask] = 1 - predictions[~correct_mask]
    return predictions


def report_metrics(name: str, predictions: np.ndarray, labels: np.ndarray) -> None:
    print(f"{name}_accuracy={accuracy_score(labels, predictions):.3f}")
    print(f"{name}_positive_recall={recall_score(labels, predictions):.3f}")


def main() -> None:
    features, labels = build_dataset()
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        labels,
        test_size=0.30,
        random_state=42,
        stratify=labels,
    )

    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(max_iter=2000)),
        ]
    )
    model.fit(x_train, y_train)

    probabilities = model.predict_proba(x_test)[:, 1]
    full_predictions = (probabilities >= 0.5).astype(int)

    report_metrics("full_automation", full_predictions, y_test)

    review_budget = int(0.25 * len(y_test))
    uncertainty = np.abs(probabilities - 0.5)
    review_indices = np.argsort(uncertainty)[:review_budget]
    automated_mask = np.ones(len(y_test), dtype=bool)
    automated_mask[review_indices] = False

    selective_predictions = full_predictions.copy()
    selective_predictions[review_indices] = simulate_reviewer_predictions(
        y_test[review_indices], accuracy=0.92
    )

    report_metrics("selective_system", selective_predictions, y_test)
    print(f"automation_rate={automated_mask.mean():.3f}")
    print(f"review_rate={(~automated_mask).mean():.3f}")
    print(
        f"automated_subset_accuracy="
        f"{accuracy_score(y_test[automated_mask], selective_predictions[automated_mask]):.3f}"
    )
    print(
        f"reviewed_subset_accuracy="
        f"{accuracy_score(y_test[~automated_mask], selective_predictions[~automated_mask]):.3f}"
    )


if __name__ == "__main__":
    main()
