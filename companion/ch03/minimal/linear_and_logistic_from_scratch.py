import numpy as np


def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def fit_linear_regression(x, y):
    x_bias = np.column_stack([np.ones(len(x)), x])
    weights = np.linalg.inv(x_bias.T @ x_bias) @ x_bias.T @ y
    return weights


def fit_ridge_regression(x, y, alpha):
    x_bias = np.column_stack([np.ones(len(x)), x])
    identity = np.eye(x_bias.shape[1])
    identity[0, 0] = 0.0
    weights = np.linalg.inv(x_bias.T @ x_bias + alpha * identity) @ x_bias.T @ y
    return weights


def predict_linear(weights, x):
    x_bias = np.column_stack([np.ones(len(x)), x])
    return x_bias @ weights


def standardize_train_test(x_train, x_test):
    mean = x_train.mean(axis=0)
    std = x_train.std(axis=0)
    std[std == 0] = 1.0
    return (x_train - mean) / std, (x_test - mean) / std, mean, std


def fit_logistic_regression(x, y, learning_rate=0.1, epochs=4000, alpha=0.01):
    n_samples, n_features = x.shape
    weights = np.zeros(n_features)
    bias = 0.0

    for _ in range(epochs):
        scores = x @ weights + bias
        probs = sigmoid(scores)

        error = probs - y
        grad_w = (x.T @ error) / n_samples + 2 * alpha * weights
        grad_b = error.mean()

        weights -= learning_rate * grad_w
        bias -= learning_rate * grad_b

    return weights, bias


def predict_logistic(weights, bias, x, threshold=0.5):
    probs = sigmoid(x @ weights + bias)
    return (probs >= threshold).astype(int), probs


def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)


def regression_demo():
    feature_names = ["area_m2", "bedrooms", "age_years"]
    x = np.array(
        [
            [48, 1, 30],
            [52, 1, 18],
            [60, 2, 20],
            [67, 2, 12],
            [72, 2, 10],
            [80, 3, 8],
            [88, 3, 6],
            [95, 3, 5],
            [105, 4, 4],
            [115, 4, 3],
            [120, 4, 2],
            [135, 5, 1],
        ],
        dtype=float,
    )
    y = np.array(
        [167, 192, 214, 252, 268, 305, 322, 344, 388, 421, 436, 489],
        dtype=float,
    )

    x_train, x_test = x[:9], x[9:]
    y_train, y_test = y[:9], y[9:]

    weights_ols = fit_linear_regression(x_train, y_train)
    weights_ridge = fit_ridge_regression(x_train, y_train, alpha=25.0)

    pred_ols = predict_linear(weights_ols, x_test)
    pred_ridge = predict_linear(weights_ridge, x_test)

    print("Regression demo")
    print("ordinary least squares coefficients:")
    print(f"  intercept={weights_ols[0]:.2f}")
    for name, weight in zip(feature_names, weights_ols[1:]):
        print(f"  {name}={weight:.2f}")
    print(f"  test_mse={mse(y_test, pred_ols):.2f}")
    print()

    print("ridge-style coefficients:")
    print(f"  intercept={weights_ridge[0]:.2f}")
    for name, weight in zip(feature_names, weights_ridge[1:]):
        print(f"  {name}={weight:.2f}")
    print(f"  test_mse={mse(y_test, pred_ridge):.2f}")
    print()


def classification_demo():
    feature_names = ["study_hours", "attendance_rate", "late_assignments"]
    x = np.array(
        [
            [3.0, 0.58, 5],
            [4.0, 0.61, 4],
            [5.0, 0.66, 4],
            [5.5, 0.71, 3],
            [6.0, 0.73, 3],
            [6.5, 0.78, 2],
            [7.0, 0.81, 2],
            [7.5, 0.83, 2],
            [8.0, 0.86, 1],
            [8.5, 0.88, 1],
            [9.0, 0.89, 1],
            [9.5, 0.91, 1],
            [10.0, 0.92, 0],
            [11.0, 0.94, 0],
            [12.0, 0.95, 0],
            [13.0, 0.97, 0],
        ],
        dtype=float,
    )
    y = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float)

    x_train, x_test = x[:12], x[12:]
    y_train, y_test = y[:12], y[12:]

    x_train_std, x_test_std, mean, std = standardize_train_test(x_train, x_test)
    weights, bias = fit_logistic_regression(x_train_std, y_train)
    predictions, probs = predict_logistic(weights, bias, x_test_std)

    print("Logistic regression demo")
    print("standardized-feature coefficients:")
    for name, weight in zip(feature_names, weights):
        print(f"  {name}={weight:.2f}")
    print(f"  bias={bias:.2f}")
    print(f"  test_accuracy={accuracy(y_test, predictions):.2f}")
    print("  test_probabilities=" + ", ".join(f"{p:.2f}" for p in probs))
    print()


def main():
    regression_demo()
    classification_demo()


if __name__ == "__main__":
    main()
