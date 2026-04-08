import itertools

import numpy as np
import torch
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from torch import nn


def build_dataset(repetitions=10):
    nouns = ["alice", "bob", "carol", "dave", "erin", "frank", "gina", "harry"]
    verbs = ["called", "helped", "pushed"]

    texts = []
    labels = []
    for first, second in itertools.combinations(nouns, 2):
        for verb in verbs:
            for _ in range(repetitions):
                texts.append(f"{first} {verb} {second}")
                labels.append(1)
                texts.append(f"{second} {verb} {first}")
                labels.append(0)
    return np.array(texts), np.array(labels)


def encode_sequences(texts, vocabulary):
    return torch.tensor(
        [[vocabulary[token] for token in text.split()] for text in texts],
        dtype=torch.long,
    )


class GRUClassifier(nn.Module):
    def __init__(self, vocabulary_size):
        super().__init__()
        self.embedding = nn.Embedding(vocabulary_size + 1, 16)
        self.gru = nn.GRU(16, 32, batch_first=True)
        self.output = nn.Linear(32, 1)

    def forward(self, inputs):
        embedded = self.embedding(inputs)
        _, hidden = self.gru(embedded)
        return self.output(hidden[-1]).squeeze(-1)


def main():
    texts, labels = build_dataset(repetitions=10)
    x_train, x_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.25,
        stratify=labels,
        random_state=0,
    )
    x_train, x_val, y_train, y_val = train_test_split(
        x_train,
        y_train,
        test_size=0.2,
        stratify=y_train,
        random_state=1,
    )

    print("Order-sensitive text classification")
    print("Example pair:")
    print("  alice helped bob -> label 1")
    print("  bob helped alice -> label 0")
    print()

    best_label = None
    best_vectorizer = None
    best_classifier = None
    best_val_accuracy = -1.0

    for label, ngrams in [("Unigram logistic regression", (1, 1)), ("Unigram+bigram logistic regression", (1, 2))]:
        vectorizer = CountVectorizer(ngram_range=ngrams)
        x_train_features = vectorizer.fit_transform(x_train)
        x_val_features = vectorizer.transform(x_val)

        classifier = LogisticRegression(max_iter=5000)
        classifier.fit(x_train_features, y_train)
        accuracy = accuracy_score(y_val, classifier.predict(x_val_features))
        print(f"{label}")
        print(f"  validation_accuracy={accuracy:.3f}")
        print()
        if accuracy > best_val_accuracy:
            best_val_accuracy = accuracy
            best_label = label
            best_vectorizer = vectorizer
            best_classifier = classifier

    x_test_features = best_vectorizer.transform(x_test)
    selected_test_accuracy = accuracy_score(y_test, best_classifier.predict(x_test_features))
    print(f"Selected n-gram baseline: {best_label}")
    print(f"  test_accuracy_after_validation_selection={selected_test_accuracy:.3f}")
    print()

    vocabulary = {
        token: index + 1 for index, token in enumerate(sorted(set(" ".join(texts).split())))
    }
    train_sequences = encode_sequences(x_train, vocabulary)
    val_sequences = encode_sequences(x_val, vocabulary)
    test_sequences = encode_sequences(x_test, vocabulary)
    train_labels = torch.tensor(y_train, dtype=torch.float32)
    val_labels = torch.tensor(y_val, dtype=torch.float32)
    test_labels = torch.tensor(y_test, dtype=torch.float32)

    torch.manual_seed(0)
    model = GRUClassifier(vocabulary_size=len(vocabulary))
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.02, weight_decay=1e-4)
    criterion = nn.BCEWithLogitsLoss()

    best_state = None
    best_epoch = None
    best_val_accuracy = -1.0

    for epoch in range(80):
        logits = model(train_sequences)
        loss = criterion(logits, train_labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            val_predictions = (torch.sigmoid(model(val_sequences)) >= 0.5).float()
            val_accuracy = float((val_predictions == val_labels).float().mean().item())

        if val_accuracy > best_val_accuracy:
            best_val_accuracy = val_accuracy
            best_epoch = epoch + 1
            best_state = {name: tensor.clone() for name, tensor in model.state_dict().items()}

    model.load_state_dict(best_state)
    with torch.no_grad():
        test_predictions = (torch.sigmoid(model(test_sequences)) >= 0.5).float()
        test_accuracy = float((test_predictions == test_labels).float().mean().item())

    print("GRU sequence classifier")
    print(f"  best_epoch={best_epoch}")
    print(f"  validation_accuracy={best_val_accuracy:.3f}")
    print(f"  test_accuracy={test_accuracy:.3f}")


if __name__ == "__main__":
    main()
