import csv
from pathlib import Path

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def load_dataset(path):
    texts = []
    labels = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            texts.append(row["text"])
            labels.append(row["label"])
    return texts, labels


def main():
    data_path = Path(__file__).resolve().parents[1] / "data" / "toy_spam.csv"
    texts, labels = load_dataset(data_path)

    x_train_text, x_temp_text, y_train, y_temp = train_test_split(
        texts,
        labels,
        test_size=0.4,
        random_state=7,
        stratify=labels,
    )
    x_validation_text, x_test_text, y_validation, y_test = train_test_split(
        x_temp_text,
        y_temp,
        test_size=0.5,
        random_state=7,
        stratify=y_temp,
    )

    vectorizer = CountVectorizer(lowercase=True, stop_words="english")
    x_train = vectorizer.fit_transform(x_train_text)
    x_validation = vectorizer.transform(x_validation_text)
    x_test = vectorizer.transform(x_test_text)

    model = LogisticRegression(max_iter=1000, random_state=7)
    model.fit(x_train, y_train)

    train_predictions = model.predict(x_train)
    validation_predictions = model.predict(x_validation)
    test_predictions = model.predict(x_test)

    print("Scikit-learn spam baseline")
    print(f"train={len(y_train)} validation={len(y_validation)} test={len(y_test)}")
    print(f"train accuracy: {accuracy_score(y_train, train_predictions):.2f}")
    print(
        "validation accuracy: "
        f"{accuracy_score(y_validation, validation_predictions):.2f}"
    )
    print(f"test accuracy: {accuracy_score(y_test, test_predictions):.2f}")


if __name__ == "__main__":
    main()
