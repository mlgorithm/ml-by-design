# Chapter 7 Companion

This chapter supports the move from general representation learning to image-specific modeling.

It focuses on three ideas:

- local feature detection through convolution
- pooling and approximate translation robustness
- augmentation as a way to teach visual invariances

## Minimal example

`minimal/convolution_and_pooling_demo.py`

What it shows:

- a handcrafted vertical-edge filter
- its response on a simple binary image and a shifted version of the same image
- how max pooling preserves strong local evidence even when exact positions change

Run it with:

```bash
python3 companion/ch07/minimal/convolution_and_pooling_demo.py
```

What to notice:

- the convolution map moves when the pattern moves
- the strongest activation remains similar
- pooling compresses location while preserving useful evidence

Prerequisites:

- weighted sums
- small matrix multiplication ideas
- the concept of a local image patch

## Practical example

`practical/digits_cnn_augmentation_demo.py`

What it shows:

- a logistic-regression baseline on raw pixels
- a small CNN trained without augmentation
- the same CNN trained with random one-pixel shift augmentation
- evaluation on both clean and shifted test images

Run it with:

```bash
python3 companion/ch07/practical/digits_cnn_augmentation_demo.py
```

What to notice:

- clean accuracy alone hides a major robustness problem
- the unaugmented CNN performs well on clean digits but collapses on shifted digits
- augmentation dramatically improves shifted-test accuracy by teaching the right invariance

Prerequisites:

- train, validation, and test splits
- convolution and pooling
- basic supervised training with cross-entropy
