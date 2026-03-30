import math


TREE_DATA = [
    ([0.52, 5], "risk"),
    ([0.58, 4], "risk"),
    ([0.61, 4], "risk"),
    ([0.68, 3], "safe"),
    ([0.72, 1], "safe"),
    ([0.78, 2], "safe"),
    ([0.81, 3], "risk"),
    ([0.88, 1], "safe"),
]


def gini(labels):
    total = len(labels)
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    return 1.0 - sum((count / total) ** 2 for count in counts.values())


def split_summary(dataset, feature_index, threshold):
    parent_labels = [label for _, label in dataset]
    left = [label for row, label in dataset if row[feature_index] <= threshold]
    right = [label for row, label in dataset if row[feature_index] > threshold]
    weighted_gini = (
        len(left) * gini(left) + len(right) * gini(right)
    ) / len(dataset)
    reduction = gini(parent_labels) - weighted_gini
    return {
        "left_count": len(left),
        "right_count": len(right),
        "left_gini": gini(left),
        "right_gini": gini(right),
        "weighted_gini": weighted_gini,
        "reduction": reduction,
    }


def euclidean_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def knn_prediction(train_data, query, k):
    ranked = sorted(
        train_data,
        key=lambda item: euclidean_distance(item[0], query),
    )
    neighbors = ranked[:k]
    votes = {}
    for _, label in neighbors:
        votes[label] = votes.get(label, 0) + 1
    prediction = max(votes.items(), key=lambda item: item[1])[0]
    return prediction, neighbors


def scale_income_examples(data):
    scaled = []
    for features, label in data:
        income, late_submissions = features
        scaled.append(([income / 10000.0, late_submissions], label))
    return scaled


def kmeans_one_iteration(points, centers):
    assignments = [[] for _ in centers]
    for point in points:
        index = min(
            range(len(centers)),
            key=lambda idx: euclidean_distance(point, centers[idx]),
        )
        assignments[index].append(point)

    new_centers = []
    for cluster in assignments:
        new_centers.append(
            [
                sum(point[dim] for point in cluster) / len(cluster)
                for dim in range(len(cluster[0]))
            ]
        )
    return assignments, new_centers


def tree_demo():
    print("Decision-tree split demo")
    parent_labels = [label for _, label in TREE_DATA]
    print(f"  parent_gini={gini(parent_labels):.3f}")

    candidates = [
        ("attendance_rate <= 0.65", 0, 0.65),
        ("late_submissions <= 1.5", 1, 1.5),
    ]
    for name, feature_index, threshold in candidates:
        summary = split_summary(TREE_DATA, feature_index, threshold)
        print(f"  candidate={name}")
        print(
            f"    left_count={summary['left_count']} "
            f"right_count={summary['right_count']}"
        )
        print(
            f"    left_gini={summary['left_gini']:.3f} "
            f"right_gini={summary['right_gini']:.3f}"
        )
        print(
            f"    weighted_gini={summary['weighted_gini']:.3f} "
            f"reduction={summary['reduction']:.3f}"
        )
    print()


def knn_demo():
    raw_train = [
        ([50000, 0], "safe"),
        ([52000, 1], "safe"),
        ([20000, 4], "risk"),
        ([22000, 5], "risk"),
    ]
    raw_query = [51000, 5]

    print("k-nearest-neighbor scaling demo")
    print(f"  raw_query={raw_query}")
    for k in [1, 3]:
        prediction, neighbors = knn_prediction(raw_train, raw_query, k)
        distances = [
            round(euclidean_distance(features, raw_query), 2)
            for features, _ in neighbors
        ]
        print(f"  raw k={k} prediction={prediction} distances={distances}")

    scaled_train = scale_income_examples(raw_train)
    scaled_query = [raw_query[0] / 10000.0, raw_query[1]]
    for k in [1, 3]:
        prediction, neighbors = knn_prediction(scaled_train, scaled_query, k)
        distances = [
            round(euclidean_distance(features, scaled_query), 2)
            for features, _ in neighbors
        ]
        print(f"  scaled k={k} prediction={prediction} distances={distances}")
    print()


def kmeans_demo():
    points = [
        [1.0, 1.0],
        [1.2, 1.1],
        [0.8, 1.3],
        [4.7, 5.1],
        [5.2, 4.9],
        [5.0, 5.4],
    ]
    centers = [[1.0, 1.0], [5.0, 5.0]]
    assignments, new_centers = kmeans_one_iteration(points, centers)

    print("k-means one-iteration demo")
    print(f"  initial_centers={centers}")
    for idx, cluster in enumerate(assignments):
        print(f"  cluster_{idx}_points={cluster}")
    print(
        "  recomputed_centers="
        + str([[round(value, 2) for value in center] for center in new_centers])
    )


def main():
    tree_demo()
    knn_demo()
    kmeans_demo()


if __name__ == "__main__":
    main()
