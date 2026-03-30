import numpy as np
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def shift_images(images, dx, dy):
    shifted = np.zeros_like(images)
    x_from = max(0, -dx)
    x_to = images.shape[2] - max(0, dx)
    y_from = max(0, -dy)
    y_to = images.shape[1] - max(0, dy)
    shifted[:, y_from + dy : y_to + dy, x_from + dx : x_to + dx] = images[
        :,
        y_from:y_to,
        x_from:x_to,
    ]
    return shifted


def summarize(values):
    values = np.array(values, dtype=float)
    return values.mean(), values.std(ddof=1)


def main():
    features, labels = load_digits(return_X_y=True)
    images = features.reshape(-1, 8, 8).astype(np.float32) / 16.0

    baseline_clean_scores = []
    baseline_shift_scores = []
    augmented_clean_scores = []
    augmented_shift_scores = []

    print("Repeated-run ablation on a shifted-image slice")
    for seed in range(5):
        x_train, x_test, y_train, y_test = train_test_split(
            images,
            labels,
            test_size=0.25,
            stratify=labels,
            random_state=seed,
        )
        x_train, _, y_train, _ = train_test_split(
            x_train,
            y_train,
            train_size=500,
            stratify=y_train,
            random_state=seed,
        )
        shifted_test = shift_images(x_test, dx=1, dy=1)

        baseline = LogisticRegression(max_iter=5000)
        baseline.fit(x_train.reshape(len(x_train), -1), y_train)
        baseline_clean = accuracy_score(y_test, baseline.predict(x_test.reshape(len(x_test), -1)))
        baseline_shift = accuracy_score(
            y_test,
            baseline.predict(shifted_test.reshape(len(shifted_test), -1)),
        )

        augmented_train = np.concatenate(
            [
                x_train,
                shift_images(x_train, dx=1, dy=1),
                shift_images(x_train, dx=-1, dy=0),
            ],
            axis=0,
        )
        augmented_labels = np.concatenate([y_train, y_train, y_train], axis=0)

        augmented = LogisticRegression(max_iter=5000)
        augmented.fit(augmented_train.reshape(len(augmented_train), -1), augmented_labels)
        augmented_clean = accuracy_score(
            y_test,
            augmented.predict(x_test.reshape(len(x_test), -1)),
        )
        augmented_shift = accuracy_score(
            y_test,
            augmented.predict(shifted_test.reshape(len(shifted_test), -1)),
        )

        baseline_clean_scores.append(baseline_clean)
        baseline_shift_scores.append(baseline_shift)
        augmented_clean_scores.append(augmented_clean)
        augmented_shift_scores.append(augmented_shift)

        print(
            f"  seed={seed} "
            f"baseline_clean={baseline_clean:.3f} baseline_shift={baseline_shift:.3f} "
            f"augmented_clean={augmented_clean:.3f} augmented_shift={augmented_shift:.3f}"
        )

    print()
    for label, scores in [
        ("baseline_clean", baseline_clean_scores),
        ("baseline_shift", baseline_shift_scores),
        ("augmented_clean", augmented_clean_scores),
        ("augmented_shift", augmented_shift_scores),
    ]:
        mean, std = summarize(scores)
        print(f"{label}: mean={mean:.3f} std={std:.3f}")


if __name__ == "__main__":
    main()
