import numpy as np


def dcg(relevances):
    discounts = 1.0 / np.log2(np.arange(2, len(relevances) + 2))
    return float(np.sum(np.asarray(relevances) * discounts))


def ndcg_at_k(ranking, relevant_items, k):
    gains = [1.0 if item in relevant_items else 0.0 for item in ranking[:k]]
    ideal_count = min(len(relevant_items), k)
    ideal = [1.0] * ideal_count + [0.0] * (k - ideal_count)
    ideal_dcg = dcg(ideal)
    if ideal_dcg == 0.0:
        return 0.0
    return dcg(gains) / ideal_dcg


def train_matrix_factorization(observations, user_count, item_count, factors=6, epochs=25):
    rng = np.random.default_rng(0)
    user_factors = 0.1 * rng.normal(size=(user_count, factors))
    item_factors = 0.1 * rng.normal(size=(item_count, factors))
    user_bias = np.zeros(user_count)
    item_bias = np.zeros(item_count)
    global_bias = np.mean([rating for _, _, rating in observations])

    learning_rate = 0.04
    regularization = 0.02

    for epoch in range(1, epochs + 1):
        rng.shuffle(observations)
        squared_error = 0.0
        for user, item, rating in observations:
            prediction = (
                global_bias
                + user_bias[user]
                + item_bias[item]
                + float(user_factors[user] @ item_factors[item])
            )
            error = rating - prediction
            squared_error += error * error

            old_user = user_factors[user].copy()
            user_bias[user] += learning_rate * (error - regularization * user_bias[user])
            item_bias[item] += learning_rate * (error - regularization * item_bias[item])
            user_factors[user] += learning_rate * (
                error * item_factors[item] - regularization * user_factors[user]
            )
            item_factors[item] += learning_rate * (
                error * old_user - regularization * item_factors[item]
            )

        if epoch in {1, 5, 25}:
            rmse = (squared_error / len(observations)) ** 0.5
            print(f"epoch={epoch:02d} train_rmse={rmse:.3f}")

    return global_bias, user_bias, item_bias, user_factors, item_factors


def score_all(model):
    global_bias, user_bias, item_bias, user_factors, item_factors = model
    dot_scores = np.sum(user_factors[:, None, :] * item_factors[None, :, :], axis=2)
    return global_bias + user_bias[:, None] + item_bias[None, :] + dot_scores


def main():
    rng = np.random.default_rng(3)
    user_count = 36
    item_count = 48
    factors = 5

    true_users = rng.normal(size=(user_count, factors))
    true_items = rng.normal(size=(item_count, factors))
    utility = (
        np.sum(true_users[:, None, :] * true_items[None, :, :], axis=2)
        + 0.25 * rng.normal(size=(user_count, item_count))
    )

    observations = []
    held_out = {}
    for user in range(user_count):
        preferred = np.argsort(utility[user])[-10:]
        exposed = rng.choice(preferred, size=6, replace=False)
        test_item = int(exposed[0])
        held_out[user] = {test_item}
        for item in exposed[1:]:
            rating = 1.0 + 4.0 / (1.0 + np.exp(-utility[user, item]))
            observations.append([user, int(item), float(rating)])

    popularity = np.zeros(item_count)
    for _, item, rating in observations:
        popularity[item] += rating

    model = train_matrix_factorization(observations, user_count, item_count)
    scores = score_all(model)

    mf_scores = []
    popularity_scores = []
    for user in range(user_count):
        seen = {item for seen_user, item, _ in observations if seen_user == user}
        candidates = [item for item in range(item_count) if item not in seen]
        mf_ranking = sorted(candidates, key=lambda item: scores[user, item], reverse=True)
        popularity_ranking = sorted(candidates, key=lambda item: popularity[item], reverse=True)
        mf_scores.append(ndcg_at_k(mf_ranking, held_out[user], k=5))
        popularity_scores.append(ndcg_at_k(popularity_ranking, held_out[user], k=5))

    print()
    print(f"mean NDCG@5 matrix factorization={np.mean(mf_scores):.3f}")
    print(f"mean NDCG@5 popularity baseline={np.mean(popularity_scores):.3f}")
    print()
    print(
        "claim boundary: this evaluates recovery of held-out observed items in a "
        "synthetic log. It does not prove that unexposed items were irrelevant."
    )


if __name__ == "__main__":
    main()
