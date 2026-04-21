import warnings

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings(
    "ignore",
    category=RuntimeWarning,
    message=r".*encountered in matmul.*",
)


def root_mean_squared_error(y_true, y_pred):
    return mean_squared_error(y_true, y_pred) ** 0.5


def build_series(length=700, regime_start=560, regime_shift=2.5):
    rng = np.random.default_rng(0)
    seasonality = np.sin(np.arange(length) * 2 * np.pi / 24)
    trend = 0.01 * np.arange(length)
    noise = 0.2 * rng.normal(size=length)

    series = np.zeros(length)
    for index in range(24, length):
        shift = 0.0 if index < regime_start else regime_shift
        series[index] = (
            0.65 * series[index - 1]
            - 0.15 * series[index - 24]
            + 0.8 * seasonality[index]
            + trend[index]
            + shift
            + noise[index]
        )
    return series


def make_lagged_dataset(series, lag_count=24):
    features = []
    targets = []
    times = []
    for index in range(lag_count - 1, len(series) - 1):
        features.append(series[index - lag_count + 1 : index + 1])
        targets.append(series[index + 1])
        times.append(index)
    return np.array(features), np.array(targets), np.array(times)


def main():
    series = build_series()
    features, targets, times = make_lagged_dataset(series, lag_count=24)

    random_train_x, random_test_x, random_train_y, random_test_y = train_test_split(
        features,
        targets,
        test_size=0.25,
        random_state=0,
    )
    random_model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
    random_model.fit(random_train_x, random_train_y)
    random_rmse = root_mean_squared_error(
        random_test_y,
        random_model.predict(random_test_x),
    )

    split_index = int(0.75 * len(features))
    chronological_train_x = features[:split_index]
    chronological_test_x = features[split_index:]
    chronological_train_y = targets[:split_index]
    chronological_test_y = targets[split_index:]

    chronological_model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))
    chronological_model.fit(chronological_train_x, chronological_train_y)
    chronological_rmse = root_mean_squared_error(
        chronological_test_y,
        chronological_model.predict(chronological_test_x),
    )

    naive_predictions = chronological_test_x[:, -1]
    naive_rmse = root_mean_squared_error(chronological_test_y, naive_predictions)

    print("Forecasting with lag features")
    print(f"  training_period_end_time={times[split_index - 1]}")
    print(f"  test_period_start_time={times[split_index]}")
    print()
    print("Evaluation")
    print(f"  random_split_ridge_rmse={random_rmse:.3f}")
    print(f"  chronological_split_ridge_rmse={chronological_rmse:.3f}")
    print(f"  chronological_naive_persistence_rmse={naive_rmse:.3f}")


if __name__ == "__main__":
    main()
