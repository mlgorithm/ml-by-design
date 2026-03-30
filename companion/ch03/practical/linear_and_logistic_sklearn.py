import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


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

    linear = LinearRegression()
    ridge = Ridge(alpha=25.0)
    linear.fit(x_train, y_train)
    ridge.fit(x_train, y_train)

    print("Scikit-learn regression demo")
    print("linear regression coefficients:")
    print(f"  intercept={linear.intercept_:.2f}")
    for name, weight in zip(feature_names, linear.coef_):
        print(f"  {name}={weight:.2f}")
    print(f"  test_mse={mean_squared_error(y_test, linear.predict(x_test)):.2f}")
    print()

    print("ridge regression coefficients:")
    print(f"  intercept={ridge.intercept_:.2f}")
    for name, weight in zip(feature_names, ridge.coef_):
        print(f"  {name}={weight:.2f}")
    print(f"  test_mse={mean_squared_error(y_test, ridge.predict(x_test)):.2f}")
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
    y = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int)

    x_train, x_test = x[:12], x[12:]
    y_train, y_test = y[:12], y[12:]

    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("logistic", LogisticRegression(random_state=7)),
        ]
    )
    model.fit(x_train, y_train)

    logistic = model.named_steps["logistic"]
    predictions = model.predict(x_test)
    probabilities = model.predict_proba(x_test)[:, 1]

    print("Scikit-learn logistic regression demo")
    print("standardized-feature coefficients:")
    for name, weight in zip(feature_names, logistic.coef_[0]):
        print(f"  {name}={weight:.2f}")
    print(f"  intercept={logistic.intercept_[0]:.2f}")
    print(f"  test_accuracy={accuracy_score(y_test, predictions):.2f}")
    print("  test_probabilities=" + ", ".join(f"{p:.2f}" for p in probabilities))
    print()


def main():
    regression_demo()
    classification_demo()


if __name__ == "__main__":
    main()
