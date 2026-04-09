import math


EXAMPLES = [
    {"p": 0.95, "y": 1},
    {"p": 0.87, "y": 1},
    {"p": 0.81, "y": 1},
    {"p": 0.72, "y": 0},
    {"p": 0.63, "y": 1},
    {"p": 0.58, "y": 0},
    {"p": 0.44, "y": 1},
    {"p": 0.35, "y": 0},
    {"p": 0.22, "y": 0},
    {"p": 0.12, "y": 0},
]

LOG_LOSS_LABELS = [1, 1, 0, 0]
CAUTIOUS_MODEL = [0.51, 0.52, 0.49, 0.48]
CONFIDENT_MODEL = [0.99, 0.98, 0.01, 0.02]


def binary_cross_entropy(examples):
    total = 0.0
    for example in examples:
        p = min(max(example["p"], 1e-12), 1 - 1e-12)
        y = example["y"]
        total += -(y * math.log(p) + (1 - y) * math.log(1 - p))
    return total / len(examples)


def accuracy_from_probabilities(labels, probabilities, threshold=0.5):
    correct = 0
    for label, probability in zip(labels, probabilities):
        prediction = 1 if probability >= threshold else 0
        correct += int(prediction == label)
    return correct / len(labels)


def average_log_loss(labels, probabilities):
    total = 0.0
    for label, probability in zip(labels, probabilities):
        p = min(max(probability, 1e-12), 1 - 1e-12)
        total += -(label * math.log(p) + (1 - label) * math.log(1 - p))
    return total / len(labels)


def metrics_at_threshold(examples, threshold):
    tp = fp = tn = fn = 0

    for example in examples:
        prediction = 1 if example["p"] >= threshold else 0
        label = example["y"]

        if prediction == 1 and label == 1:
            tp += 1
        elif prediction == 1 and label == 0:
            fp += 1
        elif prediction == 0 and label == 0:
            tn += 1
        else:
            fn += 1

    total = tp + fp + tn + fn
    accuracy = (tp + tn) / total
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall
        else 0.0
    )

    return {
        "threshold": threshold,
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def calibration_bins(examples, num_bins=5):
    bins = [[] for _ in range(num_bins)]

    for example in examples:
        index = min(int(example["p"] * num_bins), num_bins - 1)
        bins[index].append(example)

    summaries = []
    for index, bucket in enumerate(bins):
        lower = index / num_bins
        upper = (index + 1) / num_bins
        if bucket:
            mean_probability = sum(item["p"] for item in bucket) / len(bucket)
            observed_frequency = sum(item["y"] for item in bucket) / len(bucket)
            count = len(bucket)
        else:
            mean_probability = 0.0
            observed_frequency = 0.0
            count = 0

        summaries.append(
            {
                "interval": f"[{lower:.1f}, {upper:.1f})",
                "count": count,
                "mean_probability": mean_probability,
                "observed_frequency": observed_frequency,
            }
        )
    return summaries


def main():
    print("Same accuracy, different log loss")
    cautious_accuracy = accuracy_from_probabilities(
        LOG_LOSS_LABELS,
        CAUTIOUS_MODEL,
    )
    confident_accuracy = accuracy_from_probabilities(
        LOG_LOSS_LABELS,
        CONFIDENT_MODEL,
    )
    cautious_log_loss = average_log_loss(LOG_LOSS_LABELS, CAUTIOUS_MODEL)
    confident_log_loss = average_log_loss(LOG_LOSS_LABELS, CONFIDENT_MODEL)

    print(
        f"cautious_model accuracy={cautious_accuracy:.2f} "
        f"log_loss={cautious_log_loss:.3f}"
    )
    print(
        f"confident_model accuracy={confident_accuracy:.2f} "
        f"log_loss={confident_log_loss:.3f}"
    )
    print()

    print("Threshold trade-offs on fixed predicted probabilities")
    print(f"binary cross-entropy: {binary_cross_entropy(EXAMPLES):.3f}")
    print()

    for threshold in [0.30, 0.50, 0.70]:
        result = metrics_at_threshold(EXAMPLES, threshold)
        print(f"threshold={result['threshold']:.2f}")
        print(
            f"  tp={result['tp']} fp={result['fp']} "
            f"tn={result['tn']} fn={result['fn']}"
        )
        print(f"  accuracy={result['accuracy']:.2f}")
        print(f"  precision={result['precision']:.2f}")
        print(f"  recall={result['recall']:.2f}")
        print(f"  f1={result['f1']:.2f}")
        print()

    print("Calibration bins")
    for summary in calibration_bins(EXAMPLES):
        if summary["count"] == 0:
            continue
        print(
            f"bin={summary['interval']} count={summary['count']} "
            f"mean_pred={summary['mean_probability']:.2f} "
            f"observed_pos_rate={summary['observed_frequency']:.2f}"
        )


if __name__ == "__main__":
    main()
