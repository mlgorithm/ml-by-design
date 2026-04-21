import numpy as np
from sklearn.mixture import GaussianMixture


def responsibility_entropy(responsibilities):
    clipped = np.clip(responsibilities, 1e-12, 1.0)
    return -np.sum(clipped * np.log(clipped), axis=1)


def main():
    rng = np.random.default_rng(2)

    means = np.array([[-2.0, 0.0], [1.8, 0.4], [0.0, 2.6]])
    covariances = [
        np.array([[0.35, 0.05], [0.05, 0.45]]),
        np.array([[0.55, -0.15], [-0.15, 0.35]]),
        np.array([[0.45, 0.0], [0.0, 0.5]]),
    ]
    data = np.vstack(
        [rng.multivariate_normal(mean, covariance, size=90) for mean, covariance in zip(means, covariances)]
    )

    print("BIC by number of mixture components")
    models = []
    for k in range(1, 7):
        model = GaussianMixture(n_components=k, covariance_type="full", random_state=0)
        model.fit(data)
        models.append(model)
        print(f"  K={k}: bic={model.bic(data):8.1f}")

    best = min(models, key=lambda model: model.bic(data))
    responsibilities = best.predict_proba(data)
    entropy = responsibility_entropy(responsibilities)
    max_probability = responsibilities.max(axis=1)

    print()
    print(f"selected K={best.n_components}")
    print(f"mean max responsibility={max_probability.mean():.3f}")
    print(f"90th percentile entropy={np.quantile(entropy, 0.90):.3f}")

    review_count = 8
    review_indices = np.argsort(entropy)[-review_count:][::-1]
    print()
    print("highest-entropy points to review")
    for index in review_indices:
        row = responsibilities[index]
        print(
            f"  point={data[index].round(2).tolist()} "
            f"entropy={entropy[index]:.3f} "
            f"responsibilities={row.round(3).tolist()}"
        )

    print()
    print("audit note")
    print(
        "If high-entropy points trigger manual review, the uncertainty signal "
        "changes the downstream action. If every point receives the same action, "
        "the uncertainty estimate is documentation rather than a policy."
    )


if __name__ == "__main__":
    main()
