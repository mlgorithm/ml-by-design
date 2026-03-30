# IOAI Gap Analysis

This document maps **Solving AI Problems** against the official **IOAI 2026 syllabus** and defines what should live in a separate coding-first companion track rather than in the main published book.

Primary sources:

- [IOAI 2026 syllabus page](https://ioai-official.org/united-arab-emirates-2026/syllabus-2026/)
- [Official syllabus PDF](https://ioai-official.org/wp-content/uploads/2025/10/Syllabus.pdf)

## Recommendation

Do **not** expand the main book until it tries to cover the full IOAI syllabus.

Instead:

- keep the book as the problem-driven, undergraduate-first conceptual core
- use a separate coding-first companion track or repo to close the IOAI competition gap

Reason:

- the book's strength is framing, evidence, reliability, and systems
- IOAI completeness requires fast-moving practical coverage that belongs in code and exercises, not in the main manuscript

## Coverage Categories

Use three labels:

- `Covered well`
- `Partially covered`
- `Not covered enough`

## Official IOAI Topic Map Versus The Book

### 1. Foundational Skills And Classical Machine Learning

`Covered well`

- linear regression
- logistic regression
- L1 and L2 regularization
- k-nearest neighbors
- decision trees
- k-means
- PCA
- evaluation metrics
- underfitting and overfitting
- train, validation, and test logic

`Partially covered`

- NumPy and Python-based implementation ideas through companion scripts
- feature engineering
- data processing
- random forests and gradient boosting

`Not covered enough`

- Pandas
- Matplotlib and Seaborn as explicit competition tools
- scikit-learn workflow breadth
- PyTorch basics as an explicit practical toolkit layer
- tensor manipulation
- CPU and GPU training workflow
- SVM
- t-SNE and UMAP
- DBSCAN, hierarchical clustering, spectral clustering
- hyperparameter tuning
- cross-validation
- ROC curves as a practical competition tool

### 2. Neural Networks And Deep Learning

`Covered well`

- perceptron-level intuition
- gradient descent
- backpropagation
- activation functions
- loss functions
- MLPs
- embeddings
- pooling
- attention
- transformer intuition
- early stopping

`Partially covered`

- SGD and mini-batch logic
- transfer and fine-tuning concepts
- regularization

`Not covered enough`

- Adam and AdamW as practical competition tools
- convergence and learning-rate tuning as hands-on workflow
- dropout
- weight initialization
- batch normalization
- parameter-efficient fine-tuning as practice

### 3. Computer Vision

`Covered well`

- convolutional layers
- image augmentation as a modeling claim
- transfer and deployment realism

`Partially covered`

- image classification
- object detection conceptually
- segmentation conceptually
- pretrained encoders in a broad sense

`Not covered enough`

- YOLO, SSD, DETR
- U-Net
- ResNet as an explicit practical model family
- self-supervised vision workflow in practice
- CLIP
- GANs
- diffusion models

### 4. NLP And Audio

`Covered well`

- text classification concepts
- language modeling concepts
- grounding and retrieval thinking
- audio/time-series representation concepts

`Partially covered`

- contextual encoders
- transformers in NLP
- audio encoders as a category

`Not covered enough`

- BERT as a practical competition tool
- encoder-decoder models
- open-source and API-based language model workflow
- HuBERT
- Whisper
- Qwen-Audio
- Voxtral

## What The Book Should Remain Responsible For

The main book should stay responsible for:

- problem framing
- proxy targets
- baselines
- evaluation
- claim discipline
- reliability
- system design

It should also continue covering:

- core model families at a durable conceptual level
- modality-specific reasoning at a durable conceptual level

## What The IOAI Companion Track Should Add

The separate coding-first track should add:

- tooling fluency in `NumPy`, `Pandas`, `Matplotlib/Seaborn`, `scikit-learn`, and `PyTorch`
- practical model-selection and validation workflow
- competition-relevant implementations for missing topic families
- IOAI-style exercises and timed practice
- cookbook-level usage where that is useful for competition preparation

## Highest-Priority Gaps To Close First

If the goal is to make the companion useful for IOAI prep quickly, add these first:

1. `Tooling layer`
   `NumPy`, `Pandas`, `Matplotlib/Seaborn`, `scikit-learn`, `PyTorch`
2. `Validation layer`
   cross-validation, hyperparameter tuning, ROC workflow
3. `Missing classical methods`
   SVM, UMAP/t-SNE, DBSCAN/hierarchical clustering
4. `Practical deep learning layer`
   Adam/AdamW, dropout, batch norm, initialization, fine-tuning
5. `Competition-practical model families`
   ResNet, BERT, YOLO/SSD/DETR, U-Net, Whisper-level orientation

## Structural Consequence

The best split is:

- `book`: concept-first, durable, publishable
- `IOAI repo`: coding-first, fast-moving, competition-practical

That keeps the main manuscript coherent while still letting you build a serious IOAI preparation track.
