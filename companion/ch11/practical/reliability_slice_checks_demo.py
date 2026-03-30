import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def make_group(rng, n_samples, group_id, shift=0.0, noise_scale=1.0):
    x1 = rng.normal(loc=shift, scale=1.0, size=n_samples)
    x2 = rng.normal(loc=-0.3 * shift, scale=1.0, size=n_samples)
    score = (
        1.2 * x1
        - 0.8 * x2
        + 0.5 * np.sin(x1)
        + rng.normal(scale=0.6 * noise_scale, size=n_samples)
    )
    labels = (score > 0.2).astype(int)
    features = np.column_stack(
        [
            x1 + rng.normal(scale=0.15 * noise_scale, size=n_samples),
            x2 + rng.normal(scale=0.15 * noise_scale, size=n_samples),
        ]
    )
    groups = np.full(n_samples, group_id)
    return features, labels, groups


def subgroup_accuracy(y_true, y_pred, groups, group_id):
    mask = groups == group_id
    return accuracy_score(y_true[mask], y_pred[mask])


def evaluate(label, model, features, labels, groups):
    predictions = model.predict(features)
    print(label)
    print(f"  overall_accuracy={accuracy_score(labels, predictions):.3f}")
    print(f"  group_0_accuracy={subgroup_accuracy(labels, predictions, groups, 0):.3f}")
    print(f"  group_1_accuracy={subgroup_accuracy(labels, predictions, groups, 1):.3f}")
    print()


def main():
    rng = np.random.default_rng(0)

    majority_x, majority_y, majority_g = make_group(
        rng=rng,
        n_samples=1400,
        group_id=0,
        shift=0.0,
        noise_scale=1.0,
    )
    minority_x, minority_y, minority_g = make_group(
        rng=rng,
        n_samples=120,
        group_id=1,
        shift=0.3,
        noise_scale=2.0,
    )

    features = np.vstack([majority_x, minority_x])
    labels = np.concatenate([majority_y, minority_y])
    groups = np.concatenate([majority_g, minority_g])
    stratify_labels = np.array([f"{label}_{group}" for label, group in zip(labels, groups)])

    train_x, test_x, train_y, test_y, train_g, test_g = train_test_split(
        features,
        labels,
        groups,
        test_size=0.3,
        stratify=stratify_labels,
        random_state=0,
    )

    shifted_test_x = test_x.copy()
    minority_mask = test_g == 1
    shifted_test_x[minority_mask, 0] += 0.8
    shifted_test_x[minority_mask, 1] -= 0.4

    baseline = LogisticRegression(max_iter=5000)
    baseline.fit(train_x, train_y)

    majority_indices = np.where(train_g == 0)[0]
    minority_indices = np.where(train_g == 1)[0]
    repeats = int(np.ceil(len(majority_indices) / len(minority_indices)))
    balanced_indices = np.concatenate(
        [
            majority_indices,
            np.tile(minority_indices, repeats)[: len(majority_indices)],
        ]
    )

    balanced = LogisticRegression(max_iter=5000)
    balanced.fit(train_x[balanced_indices], train_y[balanced_indices])

    print("Reliability checks across subgroup and shift slices")
    print()
    evaluate("Baseline on clean test data", baseline, test_x, test_y, test_g)
    evaluate("Baseline on shifted minority-group slice", baseline, shifted_test_x, test_y, test_g)
    evaluate("Group-balanced training on clean test data", balanced, test_x, test_y, test_g)
    evaluate("Group-balanced training on shifted minority-group slice", balanced, shifted_test_x, test_y, test_g)


if __name__ == "__main__":
    main()
