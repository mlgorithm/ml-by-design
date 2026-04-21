import math
import random


def sigmoid(value):
    value = max(min(value, 50.0), -50.0)
    return 1.0 / (1.0 + math.exp(-value))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def encode(x):
    mean_weights = [[0.8, -0.3, 0.4], [-0.2, 0.7, 0.5]]
    logvar_weights = [[-0.4, 0.2, 0.1], [0.3, -0.5, 0.2]]
    mean_bias = [0.1, -0.2]
    logvar_bias = [-1.2, -0.8]
    mean = [dot(weights, x) + bias for weights, bias in zip(mean_weights, mean_bias)]
    logvar = [dot(weights, x) + bias for weights, bias in zip(logvar_weights, logvar_bias)]
    return mean, logvar


def reparameterize(mean, logvar):
    latent = []
    epsilons = []
    for mu, log_sigma_squared in zip(mean, logvar):
        epsilon = random.gauss(0.0, 1.0)
        sigma = math.exp(0.5 * log_sigma_squared)
        latent.append(mu + sigma * epsilon)
        epsilons.append(epsilon)
    return latent, epsilons


def decode(z):
    decoder_weights = [
        [1.2, -0.4],
        [-0.7, 1.1],
        [0.5, 0.8],
    ]
    decoder_bias = [-0.1, 0.2, 0.0]
    return [sigmoid(dot(weights, z) + bias) for weights, bias in zip(decoder_weights, decoder_bias)]


def kl_to_standard_normal(mean, logvar):
    total = 0.0
    for mu, log_sigma_squared in zip(mean, logvar):
        variance = math.exp(log_sigma_squared)
        total += variance + mu * mu - 1.0 - log_sigma_squared
    return 0.5 * total


def main():
    random.seed(4)
    x = [1.0, 0.0, 1.0]
    mean, logvar = encode(x)
    kl = kl_to_standard_normal(mean, logvar)

    print("input:", x)
    print("encoder mean:", [round(value, 3) for value in mean])
    print("encoder log variance:", [round(value, 3) for value in logvar])
    print(f"KL to standard normal prior: {kl:.3f}")
    print()
    print("three latent samples from the same encoded input")
    for sample_index in range(3):
        z, epsilons = reparameterize(mean, logvar)
        reconstruction = decode(z)
        print(
            f"  sample={sample_index} "
            f"epsilon={[round(value, 3) for value in epsilons]} "
            f"z={[round(value, 3) for value in z]} "
            f"decoded={[round(value, 3) for value in reconstruction]}"
        )


if __name__ == "__main__":
    main()
