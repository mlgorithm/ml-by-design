from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs, make_moons
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


def classification_demo():
    x, y = make_moons(n_samples=360, noise=0.28, random_state=7)
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

    models = [
        ("logistic_regression", Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression(random_state=7))])),
        ("decision_tree_depth_3", DecisionTreeClassifier(max_depth=3, random_state=7)),
        ("random_forest", RandomForestClassifier(n_estimators=200, random_state=7)),
        ("gradient_boosting", GradientBoostingClassifier(random_state=7)),
        ("knn_k_7", Pipeline([("scaler", StandardScaler()), ("model", KNeighborsClassifier(n_neighbors=7))])),
    ]

    print("Classification comparison on nonlinear data")
    print(
        f"train={len(y_train)} validation={len(y_validation)} test={len(y_test)}"
    )
    best_name = None
    best_model = None
    best_validation_accuracy = -1.0
    for name, model in models:
        model.fit(x_train, y_train)
        validation_accuracy = accuracy_score(y_validation, model.predict(x_validation))
        print(f"  {name}: validation_accuracy={validation_accuracy:.3f}")
        if validation_accuracy > best_validation_accuracy:
            best_validation_accuracy = validation_accuracy
            best_name = name
            best_model = model
    selected_test_accuracy = accuracy_score(y_test, best_model.predict(x_test))
    print(f"  selected_on_validation={best_name}")
    print(f"  test_accuracy_after_selection={selected_test_accuracy:.3f}")
    print()

    print("Decision-tree depth sweep")
    best_depth = None
    best_validation = -1.0
    for depth in [1, 2, 3, 4, 5, None]:
        model = DecisionTreeClassifier(max_depth=depth, random_state=7)
        model.fit(x_train, y_train)
        train_accuracy = accuracy_score(y_train, model.predict(x_train))
        validation_accuracy = accuracy_score(
            y_validation,
            model.predict(x_validation),
        )
        label = "None" if depth is None else str(depth)
        print(
            f"  max_depth={label:>4} "
            f"train_accuracy={train_accuracy:.3f} "
            f"validation_accuracy={validation_accuracy:.3f}"
        )
        if validation_accuracy > best_validation:
            best_validation = validation_accuracy
            best_depth = depth

    selected = DecisionTreeClassifier(max_depth=best_depth, random_state=7)
    selected.fit(x_train, y_train)
    test_accuracy = accuracy_score(y_test, selected.predict(x_test))
    print()
    print(f"selected max_depth={best_depth}")
    print(f"test_accuracy_after_validation_selection={test_accuracy:.3f}")
    print()


def clustering_demo():
    x, _ = make_blobs(
        n_samples=150,
        centers=[
            (-2.0, 0.0, 0.5, 1.0),
            (1.5, 1.0, -1.0, 0.0),
            (3.0, 4.0, 1.5, -0.5),
        ],
        cluster_std=[0.6, 0.9, 0.7],
        random_state=7,
    )
    kmeans = KMeans(n_clusters=3, random_state=7, n_init=10)
    kmeans.fit(x)

    pca = PCA(n_components=2, random_state=7)
    projection = pca.fit_transform(x)

    print("Clustering and PCA demo")
    print(f"  kmeans_inertia={kmeans.inertia_:.2f}")
    for idx, center in enumerate(kmeans.cluster_centers_):
        rounded = [round(float(value), 2) for value in center]
        print(f"  center_{idx}={rounded}")
    explained = [round(float(value), 3) for value in pca.explained_variance_ratio_]
    print(f"  pca_explained_variance_ratio={explained}")
    print(f"  original_dimension={x.shape[1]} projected_dimension={projection.shape[1]}")
    first_projection = [round(float(value), 2) for value in projection[0]]
    print(f"  first_projected_point={first_projection}")


def main():
    classification_demo()
    clustering_demo()


if __name__ == "__main__":
    main()
