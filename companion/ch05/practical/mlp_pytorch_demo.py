import copy

import torch
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def accuracy_from_logits(logits, targets):
    probabilities = torch.sigmoid(logits)
    predictions = (probabilities >= 0.5).float()
    return float((predictions == targets).float().mean().item())


def prepare_data():
    features, labels = make_moons(n_samples=500, noise=0.25, random_state=7)

    x_train, x_temp, y_train, y_temp = train_test_split(
        features,
        labels,
        train_size=40,
        stratify=labels,
        random_state=0,
    )
    x_val, x_test, y_val, y_test = train_test_split(
        x_temp,
        y_temp,
        test_size=200,
        stratify=y_temp,
        random_state=1,
    )

    scaler = StandardScaler().fit(x_train)
    x_train = scaler.transform(x_train)
    x_val = scaler.transform(x_val)
    x_test = scaler.transform(x_test)

    return {
        "train": (
            torch.tensor(x_train, dtype=torch.float32),
            torch.tensor(y_train, dtype=torch.float32),
        ),
        "val": (
            torch.tensor(x_val, dtype=torch.float32),
            torch.tensor(y_val, dtype=torch.float32),
        ),
        "test": (
            torch.tensor(x_test, dtype=torch.float32),
            torch.tensor(y_test, dtype=torch.float32),
        ),
    }


class LinearClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(2, 1)

    def forward(self, inputs):
        return self.layer(inputs).squeeze(-1)


class MLPClassifier(nn.Module):
    def __init__(self, hidden_dim=128):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, inputs):
        return self.network(inputs).squeeze(-1)


def evaluate(model, dataset, criterion):
    inputs, targets = dataset
    logits = model(inputs)
    loss = float(criterion(logits, targets).item())
    accuracy = accuracy_from_logits(logits, targets)
    return loss, accuracy


def build_optimizer(model, optimizer_name, learning_rate, weight_decay):
    if optimizer_name == "sgd":
        return torch.optim.SGD(
            model.parameters(),
            lr=learning_rate,
            momentum=0.9,
            weight_decay=weight_decay,
        )
    if optimizer_name == "adamw":
        return torch.optim.AdamW(
            model.parameters(),
            lr=learning_rate,
            weight_decay=weight_decay,
        )
    raise ValueError(f"Unknown optimizer: {optimizer_name}")


def train_model(
    model,
    datasets,
    optimizer_name,
    learning_rate,
    weight_decay,
    epochs,
    batch_size,
):
    criterion = nn.BCEWithLogitsLoss()
    optimizer = build_optimizer(model, optimizer_name, learning_rate, weight_decay)
    x_train, y_train = datasets["train"]
    loader = DataLoader(
        TensorDataset(x_train, y_train),
        batch_size=batch_size,
        shuffle=True,
    )

    best_state = None
    best_epoch = None
    best_val_accuracy = -1.0
    best_val_loss = float("inf")

    for epoch in range(epochs):
        model.train()
        for batch_inputs, batch_targets in loader:
            logits = model(batch_inputs)
            loss = criterion(logits, batch_targets)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_loss, val_accuracy = evaluate(model, datasets["val"], criterion)

        if (
            val_accuracy > best_val_accuracy
            or (val_accuracy == best_val_accuracy and val_loss < best_val_loss)
        ):
            best_state = copy.deepcopy(model.state_dict())
            best_epoch = epoch + 1
            best_val_accuracy = val_accuracy
            best_val_loss = val_loss

    model.load_state_dict(best_state)
    model.eval()
    with torch.no_grad():
        train_loss, train_accuracy = evaluate(model, datasets["train"], criterion)
        val_loss, val_accuracy = evaluate(model, datasets["val"], criterion)
        test_loss, test_accuracy = evaluate(model, datasets["test"], criterion)

    return {
        "optimizer": optimizer_name,
        "batch_size": batch_size,
        "best_epoch": best_epoch,
        "train_loss": train_loss,
        "train_accuracy": train_accuracy,
        "val_loss": val_loss,
        "val_accuracy": val_accuracy,
        "test_loss": test_loss,
        "test_accuracy": test_accuracy,
    }


def print_metrics(label, metrics):
    print(label)
    print(
        f"  optimizer={metrics['optimizer']} batch_size={metrics['batch_size']} "
        f"best_epoch={metrics['best_epoch']}"
    )
    print(
        f"  train_loss={metrics['train_loss']:.3f} "
        f"train_accuracy={metrics['train_accuracy']:.3f}"
    )
    print(
        f"  val_loss={metrics['val_loss']:.3f} "
        f"val_accuracy={metrics['val_accuracy']:.3f}"
    )
    print(
        f"  test_loss={metrics['test_loss']:.3f} "
        f"test_accuracy={metrics['test_accuracy']:.3f}"
    )
    print()


def main():
    datasets = prepare_data()

    torch.manual_seed(0)
    linear_metrics = train_model(
        model=LinearClassifier(),
        datasets=datasets,
        optimizer_name="adamw",
        learning_rate=0.05,
        weight_decay=0.0,
        epochs=300,
        batch_size=16,
    )

    torch.manual_seed(0)
    mlp_sgd_metrics = train_model(
        model=MLPClassifier(hidden_dim=128),
        datasets=datasets,
        optimizer_name="sgd",
        learning_rate=0.03,
        weight_decay=0.0,
        epochs=400,
        batch_size=16,
    )

    torch.manual_seed(0)
    mlp_adamw_metrics = train_model(
        model=MLPClassifier(hidden_dim=128),
        datasets=datasets,
        optimizer_name="adamw",
        learning_rate=0.01,
        weight_decay=0.0,
        epochs=400,
        batch_size=16,
    )

    torch.manual_seed(0)
    mlp_regularized_metrics = train_model(
        model=MLPClassifier(hidden_dim=128),
        datasets=datasets,
        optimizer_name="adamw",
        learning_rate=0.01,
        weight_decay=0.05,
        epochs=400,
        batch_size=16,
    )

    print("Nonlinear classification with a small training set")
    print_metrics("Linear baseline", linear_metrics)
    print_metrics("MLP with SGD", mlp_sgd_metrics)
    print_metrics("MLP with AdamW", mlp_adamw_metrics)
    print_metrics("MLP with AdamW + weight decay", mlp_regularized_metrics)


if __name__ == "__main__":
    main()
