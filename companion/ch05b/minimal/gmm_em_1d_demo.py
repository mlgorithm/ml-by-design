import math
import random


def normal_pdf(x, mean, variance):
    variance = max(variance, 1e-9)
    scale = math.sqrt(2.0 * math.pi * variance)
    exponent = -((x - mean) ** 2) / (2.0 * variance)
    return math.exp(exponent) / scale


def e_step(data, weights, means, variances):
    responsibilities = []
    for x in data:
        unnormalized = [
            weights[k] * normal_pdf(x, means[k], variances[k])
            for k in range(len(weights))
        ]
        total = sum(unnormalized)
        responsibilities.append([value / total for value in unnormalized])
    return responsibilities


def m_step(data, responsibilities):
    component_count = len(responsibilities[0])
    n = len(data)
    weights = []
    means = []
    variances = []

    for k in range(component_count):
        effective_count = sum(row[k] for row in responsibilities)
        weight = effective_count / n
        mean = sum(row[k] * x for row, x in zip(responsibilities, data)) / effective_count
        variance = (
            sum(row[k] * (x - mean) ** 2 for row, x in zip(responsibilities, data))
            / effective_count
        )
        weights.append(weight)
        means.append(mean)
        variances.append(max(variance, 1e-6))

    return weights, means, variances


def log_likelihood(data, weights, means, variances):
    total = 0.0
    for x in data:
        mixture_density = sum(
            weights[k] * normal_pdf(x, means[k], variances[k])
            for k in range(len(weights))
        )
        total += math.log(max(mixture_density, 1e-300))
    return total


def run_em(data, initial_means, iterations=12):
    weights = [0.5, 0.5]
    means = list(initial_means)
    variances = [1.0, 1.0]

    for step in range(iterations + 1):
        ll = log_likelihood(data, weights, means, variances)
        print(
            f"iter={step:02d} ll={ll:7.2f} "
            f"weights={[round(w, 3) for w in weights]} "
            f"means={[round(m, 3) for m in means]} "
            f"vars={[round(v, 3) for v in variances]}"
        )
        if step == iterations:
            break
        responsibilities = e_step(data, weights, means, variances)
        weights, means, variances = m_step(data, responsibilities)

    print("soft assignments for overlap points")
    responsibilities = e_step(data, weights, means, variances)
    for x, row in zip(data, responsibilities):
        if -0.5 <= x <= 1.5:
            print(f"  x={x:5.2f} responsibilities={[round(value, 3) for value in row]}")


def main():
    random.seed(7)
    left = [random.gauss(-2.0, 0.55) for _ in range(16)]
    right = [random.gauss(2.0, 0.75) for _ in range(16)]
    bridge = [-0.2, 0.2, 0.7, 1.1]
    data = sorted(left + bridge + right)

    print("Run A: separated initialization")
    run_em(data, initial_means=(-3.0, 3.0))
    print()
    print("Run B: crowded initialization")
    run_em(data, initial_means=(-0.25, 0.25))


if __name__ == "__main__":
    main()
