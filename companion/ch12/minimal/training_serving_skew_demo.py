"""Illustrate training-serving skew from inconsistent preprocessing."""

from __future__ import annotations

import math

TRAIN_MEAN = (4.0, 10.0)
TRAIN_STD = (2.0, 5.0)

# Buggy live preprocessing stats from a small, shifted serving batch.
SERVING_MEAN = (6.0, 14.0)
SERVING_STD = (3.0, 7.0)

WEIGHTS = (1.7, 1.3)
BIAS = -0.2

EXAMPLES = [
    ("s1", (2.0, 6.0), 0),
    ("s2", (3.0, 9.0), 0),
    ("s3", (5.0, 10.0), 1),
    ("s4", (6.0, 14.0), 1),
    ("s5", (7.0, 18.0), 1),
    ("s6", (4.5, 11.0), 0),
]


def standardize(values: tuple[float, float], mean: tuple[float, float], std: tuple[float, float]) -> tuple[float, float]:
    return tuple((x - m) / s for x, m, s in zip(values, mean, std))


def sigmoid(value: float) -> float:
    return 1.0 / (1.0 + math.exp(-value))


def predict_probability(values: tuple[float, float], mean: tuple[float, float], std: tuple[float, float]) -> float:
    z = standardize(values, mean, std)
    logit = sum(w * feature for w, feature in zip(WEIGHTS, z)) + BIAS
    return sigmoid(logit)


def accuracy(probabilities: list[float], labels: list[int], threshold: float = 0.5) -> float:
    correct = 0
    for probability, label in zip(probabilities, labels):
        prediction = int(probability >= threshold)
        correct += int(prediction == label)
    return correct / len(labels)


def main() -> None:
    labels = [label for _, _, label in EXAMPLES]
    correct_probs = []
    buggy_probs = []

    print("id  raw_features   correct_p  buggy_p  correct_pred  buggy_pred")
    for example_id, features, label in EXAMPLES:
        correct_probability = predict_probability(features, TRAIN_MEAN, TRAIN_STD)
        buggy_probability = predict_probability(features, SERVING_MEAN, SERVING_STD)
        correct_probs.append(correct_probability)
        buggy_probs.append(buggy_probability)
        print(
            f"{example_id:>2}  {features!s:<12}  "
            f"{correct_probability:.3f}      {buggy_probability:.3f}      "
            f"{int(correct_probability >= 0.5)}             {int(buggy_probability >= 0.5)}"
        )

    print()
    print(f"accuracy_with_training_stats={accuracy(correct_probs, labels):.3f}")
    print(f"accuracy_with_buggy_serving_stats={accuracy(buggy_probs, labels):.3f}")


if __name__ == "__main__":
    main()
