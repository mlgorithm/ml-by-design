import numpy as np
import torch
from sklearn.datasets import load_digits
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


class TinyVAE(nn.Module):
    def __init__(self, input_dim=64, hidden_dim=32, latent_dim=2):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
        )
        self.mean = nn.Linear(hidden_dim, latent_dim)
        self.logvar = nn.Linear(hidden_dim, latent_dim)
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, input_dim),
            nn.Sigmoid(),
        )

    def forward(self, x):
        hidden = self.encoder(x)
        mean = self.mean(hidden)
        logvar = self.logvar(hidden)
        std = torch.exp(0.5 * logvar)
        epsilon = torch.randn_like(std)
        z = mean + std * epsilon
        reconstruction = self.decoder(z)
        return reconstruction, mean, logvar

    def sample(self, count):
        z = torch.randn(count, self.mean.out_features)
        return self.decoder(z)


def vae_loss(reconstruction, x, mean, logvar):
    recon_loss = nn.functional.binary_cross_entropy(reconstruction, x, reduction="sum")
    kl = -0.5 * torch.sum(1.0 + logvar - mean.pow(2) - logvar.exp())
    return recon_loss + kl, recon_loss, kl


def main():
    torch.manual_seed(0)
    np.random.seed(0)

    digits = load_digits()
    x = digits.data.astype("float32") / 16.0
    dataset = TensorDataset(torch.from_numpy(x))
    loader = DataLoader(dataset, batch_size=128, shuffle=True)

    model = TinyVAE()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    for epoch in range(1, 26):
        total_loss = 0.0
        total_recon = 0.0
        total_kl = 0.0
        for (batch,) in loader:
            optimizer.zero_grad()
            reconstruction, mean, logvar = model(batch)
            loss, recon_loss, kl = vae_loss(reconstruction, batch, mean, logvar)
            loss.backward()
            optimizer.step()
            total_loss += float(loss.item())
            total_recon += float(recon_loss.item())
            total_kl += float(kl.item())

        if epoch in {1, 5, 10, 25}:
            count = len(dataset)
            print(
                f"epoch={epoch:02d} "
                f"loss={total_loss / count:.3f} "
                f"recon={total_recon / count:.3f} "
                f"kl={total_kl / count:.3f}"
            )

    with torch.no_grad():
        generated = model.sample(5).reshape(5, 8, 8).numpy()

    print()
    print("generated sample summaries")
    for index, image in enumerate(generated):
        print(
            f"  sample={index} "
            f"min={image.min():.3f} max={image.max():.3f} "
            f"mean_pixel={image.mean():.3f}"
        )

    print()
    print(
        "audit note: these samples are not evidence that the VAE is useful for a "
        "downstream task. They still need visual inspection, diversity checks, "
        "and held-out evaluation."
    )


if __name__ == "__main__":
    main()
