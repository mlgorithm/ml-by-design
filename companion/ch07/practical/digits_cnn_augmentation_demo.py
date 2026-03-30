import copy

import numpy as np
import torch
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from torch import nn


def shift_images(images, dx, dy):
    shifted = np.zeros_like(images)
    x_from = max(0, -dx)
    x_to = images.shape[2] - max(0, dx)
    y_from = max(0, -dy)
    y_to = images.shape[1] - max(0, dy)
    shifted[:, y_from + dy : y_to + dy, x_from + dx : x_to + dx] = images[
        :,
        y_from:y_to,
        x_from:x_to,
    ]
    return shifted


def random_shift_batch(images, max_shift=1):
    shifted = []
    for image in images:
        dx = np.random.randint(-max_shift, max_shift + 1)
        dy = np.random.randint(-max_shift, max_shift + 1)
        shifted.append(shift_images(image[None], dx, dy)[0])
    return np.stack(shifted)


class SmallCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 8, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(8, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(16 * 2 * 2, 32),
            nn.ReLU(),
            nn.Linear(32, 10),
        )

    def forward(self, inputs):
        return self.classifier(self.features(inputs))


def tensor_accuracy(logits, targets):
    predictions = logits.argmax(dim=1)
    return float((predictions == targets).float().mean().item())


def prepare_digits_data():
    features, labels = load_digits(return_X_y=True)
    images = features.reshape(-1, 8, 8).astype(np.float32) / 16.0

    x_train, x_test, y_train, y_test = train_test_split(
        images,
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
    x_train, _, y_train, _ = train_test_split(
        x_train,
        y_train,
        train_size=700,
        stratify=y_train,
        random_state=2,
    )
    return x_train, x_val, x_test, y_train, y_val, y_test


def train_cnn(x_train, y_train, x_val, y_val, augment, epochs=30):
    torch.manual_seed(0)
    np.random.seed(0)

    model = SmallCNN()
    optimizer = torch.optim.AdamW(model.parameters(), lr=0.01, weight_decay=1e-4)
    criterion = nn.CrossEntropyLoss()

    val_inputs = torch.tensor(x_val[:, None, :, :], dtype=torch.float32)
    val_targets = torch.tensor(y_val, dtype=torch.long)

    best_state = None
    best_epoch = None
    best_val_accuracy = -1.0

    for epoch in range(epochs):
        permutation = np.random.permutation(len(x_train))
        for start in range(0, len(x_train), 64):
            batch_indices = permutation[start : start + 64]
            batch_images = x_train[batch_indices]
            if augment:
                batch_images = random_shift_batch(batch_images, max_shift=1)

            batch_inputs = torch.tensor(batch_images[:, None, :, :], dtype=torch.float32)
            batch_targets = torch.tensor(y_train[batch_indices], dtype=torch.long)

            logits = model(batch_inputs)
            loss = criterion(logits, batch_targets)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        with torch.no_grad():
            val_logits = model(val_inputs)
            val_accuracy = tensor_accuracy(val_logits, val_targets)

        if val_accuracy > best_val_accuracy:
            best_val_accuracy = val_accuracy
            best_epoch = epoch + 1
            best_state = copy.deepcopy(model.state_dict())

    model.load_state_dict(best_state)
    return model, best_epoch, best_val_accuracy


def evaluate_cnn(model, images, labels):
    with torch.no_grad():
        logits = model(torch.tensor(images[:, None, :, :], dtype=torch.float32))
        return tensor_accuracy(logits, torch.tensor(labels, dtype=torch.long))


def main():
    x_train, x_val, x_test, y_train, y_val, y_test = prepare_digits_data()
    shifted_test = shift_images(x_test, dx=1, dy=1)

    logistic_regression = LogisticRegression(max_iter=5000)
    logistic_regression.fit(x_train.reshape(len(x_train), -1), y_train)

    print("Vision robustness under image shifts")
    print("Raw-pixel logistic regression")
    print(
        "  clean_test_accuracy="
        f"{accuracy_score(y_test, logistic_regression.predict(x_test.reshape(len(x_test), -1))):.3f}"
    )
    print(
        "  shifted_test_accuracy="
        f"{accuracy_score(y_test, logistic_regression.predict(shifted_test.reshape(len(shifted_test), -1))):.3f}"
    )
    print()

    for augment in [False, True]:
        model, best_epoch, val_accuracy = train_cnn(
            x_train=x_train,
            y_train=y_train,
            x_val=x_val,
            y_val=y_val,
            augment=augment,
            epochs=30,
        )
        label = "CNN with shift augmentation" if augment else "CNN without augmentation"
        print(label)
        print(f"  best_epoch={best_epoch}")
        print(f"  validation_accuracy={val_accuracy:.3f}")
        print(f"  clean_test_accuracy={evaluate_cnn(model, x_test, y_test):.3f}")
        print(f"  shifted_test_accuracy={evaluate_cnn(model, shifted_test, y_test):.3f}")
        print()


if __name__ == "__main__":
    main()
