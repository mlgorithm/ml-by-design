# Chapter 10 Companion: Generative Representations (`ch06a`)

This chapter supports the move from representations that describe data to representations that generate data.

It focuses on three ideas:

- latent sampling in variational autoencoders
- reconstruction plus latent regularization
- evaluating generated data before using it downstream

## Minimal example

`minimal/vae_reparameterization_toy.py`

What it shows:

- encoder outputs as means and log variances
- the reparameterization trick `z = mu + sigma * epsilon`
- the KL term that keeps latent codes near a standard normal prior
- why repeated samples from the same input can decode differently

Run it with:

```bash
python3 companion/ch06a/minimal/vae_reparameterization_toy.py
```

What to notice:

- the same input can produce several latent samples
- larger log variance increases sample spread
- the KL penalty grows when the approximate posterior moves far from the prior

Prerequisites:

- Gaussian random variables
- vector dot products
- sigmoid function

## Practical example

`practical/digits_vae_pytorch_demo.py`

What it shows:

- a compact VAE trained on scikit-learn's built-in digits dataset
- reconstruction loss and KL divergence during training
- generated digit-like samples from random latent vectors
- a small check that generated data is an object to audit, not automatic evidence

Run it with:

```bash
python3 companion/ch06a/practical/digits_vae_pytorch_demo.py
```

What to notice:

- reconstruction improves as the encoder and decoder learn
- the KL term keeps latent codes organized enough to sample from
- generated samples need qualitative and downstream evaluation before they are trusted

Prerequisites:

- neural networks
- binary cross-entropy
- PyTorch tensors
