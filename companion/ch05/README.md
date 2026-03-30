# Chapter 5 Companion

This chapter supports the transition from fixed features to learned internal representations.

It focuses on three ideas:

- forward passes through layered nonlinear models
- gradient-based training and backpropagation
- the difference between expressive models and well-regularized models

## Minimal example

`minimal/tiny_network_from_scratch.py`

What it shows:

- a tiny neural network trained from scratch on the XOR problem
- manual forward passes with sigmoid hidden and output units
- manual backpropagation and gradient descent updates

Run it with:

```bash
python3 companion/ch05/minimal/tiny_network_from_scratch.py
```

What to notice:

- the loss steadily decreases
- the network learns a nonlinear pattern that a single linear separator cannot solve
- the final probabilities become confidently correct on the four XOR inputs

Prerequisites:

- weighted sums
- sigmoid function
- basic derivatives and the chain rule

## Practical example

`practical/mlp_pytorch_demo.py`

What it shows:

- a linear classifier and multilayer perceptron on a nonlinear `make_moons` dataset
- the effect of adding hidden layers beyond a linear baseline
- mini-batch training with validation-based model selection
- the difference between `SGD`, `AdamW`, and `AdamW` with weight decay on a small training set

Run it with:

```bash
python3 companion/ch05/practical/mlp_pytorch_demo.py
```

What to notice:

- the linear model leaves nonlinear structure unexplained
- optimizer choice changes how easily the same architecture trains
- the MLP improves validation and test accuracy when the representation is flexible enough
- regularization changes the balance between fitting the training set and generalizing

Prerequisites:

- train, validation, and test splits
- binary cross-entropy
- gradient-based optimization
- mini-batches and learning-rate choice
