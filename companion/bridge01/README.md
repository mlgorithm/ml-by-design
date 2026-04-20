# Bridge I Companion

This bridge supports the foundational linear algebra concepts essential to machine learning.

It focuses on four ideas:

- vectors as data points and dot products as similarity proxies when norms are meaningful or controlled
- norms, distance metrics, and geometric intuition
- matrix-vector multiplication as linear transformations
- projections, orthogonality, and linear separability

## Practical example

`practical/linear_algebra_lab.ipynb`

What it shows:

- student profiles as 2D feature vectors, with dot products showing alignment and magnitude effects
- L1 and L2 norms, pairwise Euclidean distances, unit circles
- matrix transformations that stretch, rotate, and shear the unit circle
- vector projection onto a line and decomposition into parallel and orthogonal components
- linearly separable clusters with a learned decision boundary
- the XOR pattern as a canonical non-linearly-separable problem

Run it with:

```bash
jupyter notebook companion/bridge01/practical/linear_algebra_lab.ipynb
```

What to notice:

- dot products can reveal alignment, but vector length also matters; use cosine similarity when you need a norm-normalized comparison
- Euclidean distance is intuitive; Manhattan distance forms a different metric
- matrices map basis vectors to new coordinates, defining the transformation
- the residual from a projection is always perpendicular to the projection
- linear separability determines whether a simple line can partition two clusters
- XOR shows that raw linear boundaries cannot solve every problem; nonlinear features or nonlinear classifiers may be needed

Prerequisites:

- basic vectors and matrix notation
- understanding of dot product and matrix multiplication
- familiarity with 2D plotting and visualization
