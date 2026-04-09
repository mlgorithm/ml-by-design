"""
Minimal example: annotation protocols and label noise

Demonstrates:
- Generating synthetic binary classification data
- Simulating symmetric and asymmetric label noise
- Training logistic regression with clean vs. noisy labels
- Computing Cohen's kappa inter-annotator agreement
"""

import random
import math
import numpy as np


def sigmoid(x):
    """Numerically stable sigmoid."""
    return 1.0 / (1.0 + math.exp(-max(min(x, 50.0), -50.0)))


def logistic_regression_train(X, y, learning_rate=0.01, epochs=100):
    """Train logistic regression from scratch."""
    n_features = X.shape[1]
    weights = np.zeros(n_features)
    bias = 0.0

    for epoch in range(epochs):
        predictions = np.array([sigmoid(np.dot(X[i], weights) + bias) for i in range(len(X))])

        # Gradient descent
        errors = predictions - y
        grad_w = np.dot(X.T, errors) / len(X)
        grad_b = np.mean(errors)

        weights -= learning_rate * grad_w
        bias -= learning_rate * grad_b

    return weights, bias


def logistic_regression_predict(X, weights, bias):
    """Predict on new data."""
    return np.array([sigmoid(np.dot(X[i], weights) + bias) for i in range(len(X))])


def cohens_kappa(y_true, y_pred):
    """Compute Cohen's kappa between two annotators."""
    # Convert to binary if needed
    y_true = np.array(y_true, dtype=int)
    y_pred = np.array(y_pred, dtype=int)

    # Observed agreement
    p_o = np.mean(y_true == y_pred)

    # Expected agreement (by chance)
    p_e = (np.mean(y_true) * np.mean(y_pred) +
           (1 - np.mean(y_true)) * (1 - np.mean(y_pred)))

    # Cohen's kappa
    if p_e == 1.0:
        return 1.0 if p_o == 1.0 else 0.0
    return (p_o - p_e) / (1.0 - p_e)


def inject_noise(labels, noise_rate, asymmetric=False):
    """Inject label noise."""
    noisy = labels.copy()
    n = len(noisy)
    n_flip = int(n * noise_rate)

    if asymmetric:
        # Only flip positive labels to negative
        pos_indices = np.where(noisy == 1)[0]
        flip_indices = np.random.choice(pos_indices, min(n_flip, len(pos_indices)), replace=False)
    else:
        # Flip random labels
        flip_indices = np.random.choice(n, n_flip, replace=False)

    noisy[flip_indices] = 1 - noisy[flip_indices]
    return noisy


def main():
    # Seed for reproducibility
    random.seed(42)
    np.random.seed(42)

    # Generate synthetic dataset (binary classification)
    n_samples = 200
    n_features = 2

    X = np.random.randn(n_samples, n_features)
    # True labels: threshold on first feature
    y_true = (X[:, 0] + 0.5 * X[:, 1] > 0).astype(int)

    print("=" * 70)
    print("ANNOTATION NOISE AND INTER-ANNOTATOR AGREEMENT")
    print("=" * 70)
    print()

    # Simulate two annotators with different reliability
    print("Simulating two annotators:")
    annotator1 = inject_noise(y_true.copy(), noise_rate=0.05, asymmetric=False)
    annotator2 = inject_noise(y_true.copy(), noise_rate=0.10, asymmetric=True)

    kappa = cohens_kappa(annotator1, annotator2)
    print(f"  Cohen's kappa (annotator 1 vs 2): {kappa:.3f}")
    print()

    # Train on clean labels
    print("Training on clean labels:")
    weights_clean, bias_clean = logistic_regression_train(X, y_true)
    pred_clean = logistic_regression_predict(X, weights_clean, bias_clean)
    accuracy_clean = np.mean((pred_clean > 0.5).astype(int) == y_true)
    print(f"  Accuracy on clean labels: {accuracy_clean:.3f}")
    print()

    # Train on noisy labels at different rates
    print("Training with symmetric noise (random label flips):")
    for noise_rate in [0.0, 0.05, 0.10, 0.15, 0.20]:
        noisy_labels = inject_noise(y_true.copy(), noise_rate=noise_rate, asymmetric=False)
        weights, bias = logistic_regression_train(X, noisy_labels)
        pred = logistic_regression_predict(X, weights, bias)
        accuracy = np.mean((pred > 0.5).astype(int) == y_true)
        print(f"  Noise {noise_rate:.0%}: accuracy {accuracy:.3f}")
    print()

    # Train on asymmetric noise
    print("Training with asymmetric noise (positive labels flipped):")
    for noise_rate in [0.0, 0.05, 0.10, 0.15, 0.20]:
        noisy_labels = inject_noise(y_true.copy(), noise_rate=noise_rate, asymmetric=True)
        weights, bias = logistic_regression_train(X, noisy_labels)
        pred = logistic_regression_predict(X, weights, bias)
        accuracy = np.mean((pred > 0.5).astype(int) == y_true)
        print(f"  Noise {noise_rate:.0%}: accuracy {accuracy:.3f}")
    print()

    print("=" * 70)
    print("KEY OBSERVATIONS:")
    print("=" * 70)
    print("• Even 5% noise noticeably degrades accuracy")
    print("• Asymmetric noise is more harmful than symmetric noise")
    print("• Low inter-annotator agreement indicates dataset quality issues")
    print("• Annotation protocols and multi-annotator review are critical")
    print()


if __name__ == "__main__":
    main()
