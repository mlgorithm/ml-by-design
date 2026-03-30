import math

import numpy as np


CORPUS = [
    ["student", "studies", "for", "exam"],
    ["student", "reviews", "for", "quiz"],
    ["exam", "and", "quiz", "are", "graded"],
    ["teacher", "grades", "exam", "and", "quiz"],
    ["guitar", "and", "music", "fill", "the", "room"],
    ["dance", "follows", "music", "and", "rhythm"],
    ["guitar", "creates", "rhythm", "for", "dance"],
]

STOPWORDS = {"and", "for", "the", "are"}


def build_vocabulary(corpus):
    tokens = sorted({token for sentence in corpus for token in sentence})
    return {token: index for index, token in enumerate(tokens)}


def cooccurrence_matrix(corpus, vocab, window_size=2):
    matrix = np.zeros((len(vocab), len(vocab)), dtype=float)
    for sentence in corpus:
        for index, token in enumerate(sentence):
            left = max(0, index - window_size)
            right = min(len(sentence), index + window_size + 1)
            token_index = vocab[token]
            for context_index in range(left, right):
                if context_index == index:
                    continue
                context_token = sentence[context_index]
                matrix[token_index, vocab[context_token]] += 1.0
    return matrix


def ppmi_matrix(counts):
    total = counts.sum()
    row_sums = counts.sum(axis=1, keepdims=True)
    col_sums = counts.sum(axis=0, keepdims=True)
    probabilities = counts / total
    expected = (row_sums @ col_sums) / (total * total)

    with np.errstate(divide="ignore"):
        pmi = np.log(probabilities / expected)
    pmi[np.isinf(pmi)] = 0.0
    pmi[np.isnan(pmi)] = 0.0
    return np.maximum(pmi, 0.0)


def cosine_similarity(a, b):
    denominator = np.linalg.norm(a) * np.linalg.norm(b)
    if denominator == 0.0:
        return 0.0
    return float(np.dot(a, b) / denominator)


def euclidean_distance(a, b):
    return float(np.linalg.norm(a - b))


def top_neighbors(token, embeddings, vocab, top_k=3):
    inverse_vocab = {index: word for word, index in vocab.items()}
    index = vocab[token]
    query = embeddings[index]
    scores = []
    for other_index in range(len(vocab)):
        other_word = inverse_vocab[other_index]
        if other_index == index or other_word in STOPWORDS:
            continue
        similarity = cosine_similarity(query, embeddings[other_index])
        scores.append((similarity, other_word))
    scores.sort(reverse=True)
    return scores[:top_k]


def top_neighbors_by_distance(token, embeddings, vocab, top_k=3):
    inverse_vocab = {index: word for word, index in vocab.items()}
    index = vocab[token]
    query = embeddings[index]
    scores = []
    for other_index in range(len(vocab)):
        other_word = inverse_vocab[other_index]
        if other_index == index or other_word in STOPWORDS:
            continue
        distance = euclidean_distance(query, embeddings[other_index])
        scores.append((distance, other_word))
    scores.sort()
    return scores[:top_k]


def main():
    vocab = build_vocabulary(CORPUS)
    counts = cooccurrence_matrix(CORPUS, vocab, window_size=2)
    ppmi = ppmi_matrix(counts)

    u, singular_values, _ = np.linalg.svd(ppmi)
    embeddings = u[:, :3] * np.sqrt(singular_values[:3])

    print("Vocabulary size:", len(vocab))
    print()
    print("Nearest neighbors in the learned embedding space")
    for token in ["exam", "quiz", "guitar", "dance"]:
        neighbors = top_neighbors(token, embeddings, vocab)
        formatted = ", ".join(f"{word} ({score:.2f})" for score, word in neighbors)
        print(f"  {token}: {formatted}")

    print()
    print("Selected cosine similarities")
    for first, second in [("exam", "quiz"), ("exam", "music"), ("music", "dance")]:
        score = cosine_similarity(embeddings[vocab[first]], embeddings[vocab[second]])
        print(f"  {first:>5s} vs {second:<5s}: {score:.2f}")

    print()
    print("Exam neighbors under two geometry choices")
    cosine_neighbors = top_neighbors("exam", embeddings, vocab)
    euclidean_neighbors = top_neighbors_by_distance("exam", embeddings, vocab)
    print("  cosine:", ", ".join(f"{word} ({score:.2f})" for score, word in cosine_neighbors))
    print("  euclid:", ", ".join(f"{word} ({distance:.2f})" for distance, word in euclidean_neighbors))


if __name__ == "__main__":
    main()
