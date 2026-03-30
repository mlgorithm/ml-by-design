from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main():
    x, y = make_moons(n_samples=300, noise=0.35, random_state=7)

    x_train, x_temp, y_train, y_temp = train_test_split(
        x,
        y,
        test_size=0.4,
        random_state=7,
        stratify=y,
    )
    x_validation, x_test, y_validation, y_test = train_test_split(
        x_temp,
        y_temp,
        test_size=0.5,
        random_state=7,
        stratify=y_temp,
    )

    depths = [1, 2, 3, 5, 8, None]
    results = []

    print("Decision tree depth sweep")
    print(
        f"train={len(y_train)} validation={len(y_validation)} test={len(y_test)}"
    )
    print()

    for depth in depths:
        model = DecisionTreeClassifier(max_depth=depth, random_state=7)
        model.fit(x_train, y_train)

        train_accuracy = accuracy_score(y_train, model.predict(x_train))
        validation_accuracy = accuracy_score(
            y_validation,
            model.predict(x_validation),
        )

        depth_label = "None" if depth is None else str(depth)
        print(
            f"max_depth={depth_label:>4}  "
            f"train_accuracy={train_accuracy:.3f}  "
            f"validation_accuracy={validation_accuracy:.3f}"
        )

        results.append((depth, validation_accuracy))

    best_depth = max(results, key=lambda item: item[1])[0]
    best_model = DecisionTreeClassifier(max_depth=best_depth, random_state=7)
    best_model.fit(x_train, y_train)
    test_accuracy = accuracy_score(y_test, best_model.predict(x_test))

    print()
    print(f"selected max_depth={best_depth}")
    print(f"test accuracy after validation-based selection: {test_accuracy:.3f}")


if __name__ == "__main__":
    main()
