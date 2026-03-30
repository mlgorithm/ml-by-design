import csv
import random
from collections import Counter
from pathlib import Path


def load_examples(path):
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def train_validation_test_split(rows, seed=7):
    rows = rows[:]
    random.Random(seed).shuffle(rows)
    n = len(rows)
    n_train = int(0.6 * n)
    n_val = int(0.2 * n)
    train = rows[:n_train]
    validation = rows[n_train:n_train + n_val]
    test = rows[n_train + n_val:]
    return train, validation, test


def accuracy(rows, predictor):
    correct = 0
    for row in rows:
        if predictor(row["text"]) == row["label"]:
            correct += 1
    return correct / len(rows)


def majority_label(rows):
    counts = Counter(row["label"] for row in rows)
    return counts.most_common(1)[0][0]


def keyword_predictor(keywords):
    def predict(text):
        lowered = text.lower()
        for word in keywords:
            if word in lowered:
                return "spam"
        return "ham"

    return predict


def main():
    data_path = Path(__file__).resolve().parents[1] / "data" / "toy_spam.csv"
    rows = load_examples(data_path)
    train, validation, test = train_validation_test_split(rows)

    majority = majority_label(train)
    majority_predict = lambda _text: majority

    spam_keywords = [
        "free",
        "win",
        "urgent",
        "reward",
        "offer",
        "discount",
        "money",
        "gift",
        "cash",
        "verify",
        "reset",
    ]
    keyword_model = keyword_predictor(spam_keywords)

    print("Toy spam dataset")
    print(f"train={len(train)} validation={len(validation)} test={len(test)}")
    print()
    print(f"Majority baseline predicts: {majority}")
    print(f"Majority baseline train accuracy: {accuracy(train, majority_predict):.2f}")
    print(
        f"Majority baseline validation accuracy: "
        f"{accuracy(validation, majority_predict):.2f}"
    )
    print(f"Majority baseline test accuracy: {accuracy(test, majority_predict):.2f}")
    print()
    print("Keyword baseline keywords:")
    print(", ".join(spam_keywords))
    print(f"Keyword baseline train accuracy: {accuracy(train, keyword_model):.2f}")
    print(
        f"Keyword baseline validation accuracy: "
        f"{accuracy(validation, keyword_model):.2f}"
    )
    print(f"Keyword baseline test accuracy: {accuracy(test, keyword_model):.2f}")


if __name__ == "__main__":
    main()
