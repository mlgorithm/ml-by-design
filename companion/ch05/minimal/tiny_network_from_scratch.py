import math
import random


def sigmoid(value):
    value = max(min(value, 50.0), -50.0)
    return 1.0 / (1.0 + math.exp(-value))


def binary_cross_entropy(target, prediction):
    prediction = min(max(prediction, 1e-9), 1.0 - 1e-9)
    return -(target * math.log(prediction) + (1.0 - target) * math.log(1.0 - prediction))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def forward_pass(x, hidden_weights, hidden_biases, output_weights, output_bias):
    hidden_pre = [dot(weights, x) + bias for weights, bias in zip(hidden_weights, hidden_biases)]
    hidden_act = [sigmoid(value) for value in hidden_pre]
    output_pre = dot(output_weights, hidden_act) + output_bias
    output_act = sigmoid(output_pre)
    return hidden_pre, hidden_act, output_pre, output_act


def main():
    random.seed(0)

    data = [
        ([0.0, 0.0], 0.0),
        ([0.0, 1.0], 1.0),
        ([1.0, 0.0], 1.0),
        ([1.0, 1.0], 0.0),
    ]

    hidden_weights = [
        [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)],
        [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)],
    ]
    hidden_biases = [0.0, 0.0]
    output_weights = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]
    output_bias = 0.0

    learning_rate = 1.5
    epochs = 8000

    for epoch in range(epochs):
        grad_hidden_weights = [[0.0, 0.0], [0.0, 0.0]]
        grad_hidden_biases = [0.0, 0.0]
        grad_output_weights = [0.0, 0.0]
        grad_output_bias = 0.0
        total_loss = 0.0

        for x, target in data:
            hidden_pre, hidden_act, _, prediction = forward_pass(
                x,
                hidden_weights,
                hidden_biases,
                output_weights,
                output_bias,
            )

            total_loss += binary_cross_entropy(target, prediction)

            delta_output = prediction - target
            for j in range(2):
                grad_output_weights[j] += delta_output * hidden_act[j]
            grad_output_bias += delta_output

            for j in range(2):
                hidden_derivative = hidden_act[j] * (1.0 - hidden_act[j])
                delta_hidden = delta_output * output_weights[j] * hidden_derivative
                for k in range(2):
                    grad_hidden_weights[j][k] += delta_hidden * x[k]
                grad_hidden_biases[j] += delta_hidden

        scale = 1.0 / len(data)
        for j in range(2):
            for k in range(2):
                hidden_weights[j][k] -= learning_rate * grad_hidden_weights[j][k] * scale
            hidden_biases[j] -= learning_rate * grad_hidden_biases[j] * scale
            output_weights[j] -= learning_rate * grad_output_weights[j] * scale
        output_bias -= learning_rate * grad_output_bias * scale

        if epoch % 1000 == 0 or epoch == epochs - 1:
            print(f"epoch={epoch:4d} loss={total_loss * scale:.4f}")

    print()
    print("Final XOR predictions")
    for x, target in data:
        _, hidden_act, _, prediction = forward_pass(
            x,
            hidden_weights,
            hidden_biases,
            output_weights,
            output_bias,
        )
        print(
            f"  input={x} target={int(target)} "
            f"hidden={[round(value, 3) for value in hidden_act]} "
            f"prediction={prediction:.3f}"
        )


if __name__ == "__main__":
    main()
