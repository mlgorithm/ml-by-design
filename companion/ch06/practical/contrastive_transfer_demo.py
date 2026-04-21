import copy

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


NUM_CLASSES = 4
SIGNAL_DIM = 6
STYLE_DIM = 6
FEATURE_DIM = 24
EMBED_DIM = 8


def make_dataset(
    n_samples,
    rng,
    prototypes,
    signal_projection,
    style_projection,
    signal_noise=0.25,
    style_scale=2.5,
):
    labels = rng.integers(0, NUM_CLASSES, size=n_samples)
    signal = prototypes[labels] + signal_noise * rng.normal(size=(n_samples, SIGNAL_DIM)).astype(np.float32)

    style_view_a = style_scale * rng.normal(size=(n_samples, STYLE_DIM)).astype(np.float32)
    style_view_b = style_scale * rng.normal(size=(n_samples, STYLE_DIM)).astype(np.float32)

    signal_part = np.einsum("ij,jk->ik", signal.astype(np.float64), signal_projection.astype(np.float64))
    style_projection64 = style_projection.astype(np.float64)

    def make_view(style_view):
        combined = (
            signal_part
            + np.einsum("ij,jk->ik", style_view.astype(np.float64), style_projection64)
            + 0.2 * rng.normal(size=(n_samples, FEATURE_DIM))
        )
        return np.tanh(combined).astype(np.float32)

    view_a = make_view(style_view_a)
    view_b = make_view(style_view_b)
    return view_a, view_b, labels.astype(np.int64)


class Encoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.input = nn.Linear(FEATURE_DIM, 64)
        self.hidden = nn.Linear(64, 32)
        self.output = nn.Linear(32, EMBED_DIM)

    def forward(self, inputs):
        hidden = F.relu(self.input(inputs))
        hidden = F.relu(self.hidden(hidden))
        return self.output(hidden)


class Classifier(nn.Module):
    def __init__(self, encoder):
        super().__init__()
        self.encoder = encoder
        self.head = nn.Linear(EMBED_DIM, NUM_CLASSES)

    def forward(self, inputs):
        embeddings = self.encoder(inputs)
        return self.head(embeddings)


def nt_xent_loss(z_a, z_b, temperature=0.2):
    z_a = F.normalize(z_a, dim=1)
    z_b = F.normalize(z_b, dim=1)
    joined = torch.cat([z_a, z_b], dim=0)
    similarities = joined @ joined.T / temperature

    batch_size = z_a.shape[0]
    mask = torch.eye(2 * batch_size, device=joined.device, dtype=torch.bool)
    similarities = similarities.masked_fill(mask, -1e9)

    targets = torch.cat(
        [
            torch.arange(batch_size, 2 * batch_size, device=joined.device),
            torch.arange(0, batch_size, device=joined.device),
        ]
    )
    return F.cross_entropy(similarities, targets)


def balanced_small_subset(features, labels, per_class):
    selected = []
    for class_id in range(NUM_CLASSES):
        class_indices = np.where(labels == class_id)[0][:per_class]
        selected.extend(class_indices.tolist())
    selected = np.array(selected)
    return features[selected], labels[selected]


def split_target_data(features, labels, train_per_class, val_per_class):
    train_indices = []
    val_indices = []
    test_indices = []
    for class_id in range(NUM_CLASSES):
        class_indices = np.where(labels == class_id)[0]
        train_indices.extend(class_indices[:train_per_class].tolist())
        val_indices.extend(class_indices[train_per_class : train_per_class + val_per_class].tolist())
        test_indices.extend(class_indices[train_per_class + val_per_class :].tolist())

    train_indices = np.array(train_indices)
    val_indices = np.array(val_indices)
    test_indices = np.array(test_indices)
    return (
        (features[train_indices], labels[train_indices]),
        (features[val_indices], labels[val_indices]),
        (features[test_indices], labels[test_indices]),
    )


def pretrain_encoder(train_view_a, train_view_b):
    torch.manual_seed(0)
    encoder = Encoder()
    optimizer = torch.optim.AdamW(encoder.parameters(), lr=0.003, weight_decay=1e-4)

    train_a_tensor = torch.tensor(train_view_a)
    train_b_tensor = torch.tensor(train_view_b)
    batch_size = 256

    print("Self-supervised contrastive pretraining")
    for epoch in range(120):
        permutation = torch.randperm(train_a_tensor.shape[0])
        epoch_loss = 0.0
        for start in range(0, train_a_tensor.shape[0], batch_size):
            batch_indices = permutation[start : start + batch_size]
            z_a = encoder(train_a_tensor[batch_indices])
            z_b = encoder(train_b_tensor[batch_indices])
            loss = nt_xent_loss(z_a, z_b)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            epoch_loss += float(loss.item()) * len(batch_indices)

        if epoch in {0, 19, 59, 119}:
            average_loss = epoch_loss / train_a_tensor.shape[0]
            print(f"  epoch={epoch + 1:3d} contrastive_loss={average_loss:.4f}")

    return encoder


def encode_numpy(encoder, features):
    with torch.no_grad():
        return encoder(torch.tensor(features, dtype=torch.float32)).numpy()


def accuracy_score(labels, predictions):
    return float(np.mean(np.asarray(labels) == np.asarray(predictions)))


def linear_probe_accuracy(train_features, train_labels, test_features, test_labels):
    torch.manual_seed(0)
    classifier = nn.Linear(train_features.shape[1], NUM_CLASSES)
    optimizer = torch.optim.AdamW(classifier.parameters(), lr=0.03, weight_decay=1e-3)
    criterion = nn.CrossEntropyLoss()

    x_train = torch.tensor(train_features, dtype=torch.float32)
    y_train = torch.tensor(train_labels, dtype=torch.long)

    for _ in range(500):
        logits = classifier(x_train)
        loss = criterion(logits, y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    classifier.eval()
    with torch.no_grad():
        test_logits = classifier(torch.tensor(test_features, dtype=torch.float32))
        predictions = test_logits.argmax(dim=1).numpy()
    return accuracy_score(test_labels, predictions)


def evaluate_classifier(model, dataset):
    inputs, labels = dataset
    model.eval()
    with torch.no_grad():
        logits = model(torch.tensor(inputs, dtype=torch.float32))
        predictions = logits.argmax(dim=1).numpy()
    return accuracy_score(labels, predictions)


def fine_tune(
    pretrained_encoder,
    train_set,
    val_set,
    test_set,
    mode,
):
    torch.manual_seed(0)
    encoder = copy.deepcopy(pretrained_encoder)
    classifier = Classifier(encoder)

    if mode == "frozen":
        for parameter in classifier.encoder.parameters():
            parameter.requires_grad = False
    elif mode == "partial":
        for parameter in classifier.encoder.input.parameters():
            parameter.requires_grad = False
    elif mode == "full":
        pass
    else:
        raise ValueError(f"Unknown fine-tuning mode: {mode}")

    optimizer = torch.optim.AdamW(
        [parameter for parameter in classifier.parameters() if parameter.requires_grad],
        lr=0.01,
        weight_decay=1e-4,
    )
    criterion = nn.CrossEntropyLoss()

    x_train, y_train = train_set
    loader = DataLoader(
        TensorDataset(
            torch.tensor(x_train, dtype=torch.float32),
            torch.tensor(y_train, dtype=torch.long),
        ),
        batch_size=16,
        shuffle=True,
    )

    best_state = None
    best_val_accuracy = -1.0
    best_val_loss = float("inf")
    best_epoch = None

    for epoch in range(160):
        classifier.train()
        for batch_inputs, batch_labels in loader:
            logits = classifier(batch_inputs)
            loss = criterion(logits, batch_labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        classifier.eval()
        with torch.no_grad():
            val_logits = classifier(torch.tensor(val_set[0], dtype=torch.float32))
            val_loss = float(criterion(val_logits, torch.tensor(val_set[1], dtype=torch.long)).item())
            val_predictions = val_logits.argmax(dim=1).numpy()
            val_accuracy = accuracy_score(val_set[1], val_predictions)

        if (
            val_accuracy > best_val_accuracy
            or (val_accuracy == best_val_accuracy and val_loss < best_val_loss)
        ):
            best_state = copy.deepcopy(classifier.state_dict())
            best_val_accuracy = val_accuracy
            best_val_loss = val_loss
            best_epoch = epoch + 1

    classifier.load_state_dict(best_state)
    train_accuracy = evaluate_classifier(classifier, train_set)
    test_accuracy = evaluate_classifier(classifier, test_set)
    return {
        "mode": mode,
        "best_epoch": best_epoch,
        "train_accuracy": train_accuracy,
        "val_accuracy": best_val_accuracy,
        "test_accuracy": test_accuracy,
    }


def print_metrics(label, metrics):
    print(label)
    print(f"  best_epoch={metrics['best_epoch']}")
    print(f"  train_accuracy={metrics['train_accuracy']:.3f}")
    print(f"  val_accuracy={metrics['val_accuracy']:.3f}")
    print(f"  test_accuracy={metrics['test_accuracy']:.3f}")


def main():
    rng = np.random.default_rng(0)
    prototypes = rng.normal(size=(NUM_CLASSES, SIGNAL_DIM)).astype(np.float32)
    signal_projection_source = rng.normal(size=(SIGNAL_DIM, FEATURE_DIM)).astype(np.float32)
    style_projection_source = rng.normal(size=(STYLE_DIM, FEATURE_DIM)).astype(np.float32)

    train_view_a, train_view_b, _ = make_dataset(
        n_samples=4000,
        rng=rng,
        prototypes=prototypes,
        signal_projection=signal_projection_source,
        style_projection=style_projection_source,
    )

    signal_projection_target = signal_projection_source + 0.35 * rng.normal(
        size=(SIGNAL_DIM, FEATURE_DIM)
    ).astype(np.float32)
    style_projection_target = style_projection_source + 0.20 * rng.normal(
        size=(STYLE_DIM, FEATURE_DIM)
    ).astype(np.float32)
    target_view_a, _, target_labels = make_dataset(
        n_samples=1200,
        rng=rng,
        prototypes=prototypes,
        signal_projection=signal_projection_target,
        style_projection=style_projection_target,
        signal_noise=0.30,
        style_scale=2.8,
    )

    train_set, val_set, test_set = split_target_data(
        target_view_a,
        target_labels,
        train_per_class=8,
        val_per_class=20,
    )

    raw_accuracy = linear_probe_accuracy(train_set[0], train_set[1], test_set[0], test_set[1])

    encoder = pretrain_encoder(train_view_a, train_view_b)

    embedded_train = encode_numpy(encoder, train_set[0])
    embedded_test = encode_numpy(encoder, test_set[0])
    probe_accuracy = linear_probe_accuracy(embedded_train, train_set[1], embedded_test, test_set[1])

    frozen_metrics = fine_tune(encoder, train_set, val_set, test_set, mode="frozen")
    partial_metrics = fine_tune(encoder, train_set, val_set, test_set, mode="partial")
    full_metrics = fine_tune(encoder, train_set, val_set, test_set, mode="full")

    print()
    print("Few-label downstream evaluation under domain shift")
    print(f"  raw_feature_logistic_regression_accuracy={raw_accuracy:.3f}")
    print(f"  frozen_encoder_linear_probe_accuracy={probe_accuracy:.3f}")
    print_metrics("Classifier with frozen encoder", frozen_metrics)
    print_metrics("Classifier with partial fine-tuning", partial_metrics)
    print_metrics("Classifier with full fine-tuning", full_metrics)


if __name__ == "__main__":
    main()
