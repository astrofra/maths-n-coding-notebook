# Align a list of 3D points (with rotation, translation, and scale)

If you want to align a list of 3D points (`source`) to another list (`destination`) using a transformation composed of **rotation**, **translation**, and **uniform scale**, you can use a method based on **Singular Value Decomposition (SVD)** — a reliable mathematical tool for estimating optimal transformations between point clouds.

> 🛑 Note: Traditional ICP (Iterative Closest Point) does not handle scale. Below, we show how to include uniform scale estimation.

---

## 🧠 How does it work?

The transformation aims to compute:
- a **rotation matrix** `R` (3×3),
- a **translation vector** `t` (3×1),
- a **scaling factor** `s` (same in all directions).

Such that:
```math
destination ≈ s × (R × source) + t
```

This is done in three steps:
1. Center the point clouds (remove their centroids).
2. Compute the optimal rotation using **SVD**.
3. Estimate the scale using the **norm ratio**.
4. Compute the translation to align the centroids after scaling and rotation.

---

## 📦 Requirements

```bash
pip install numpy scipy
```

---

## ✅ Python Code: Best-fit transform with scale

```python
import numpy as np
from scipy.spatial.transform import Rotation as R

def best_fit_transform(A, B):
    centroid_A = np.mean(A, axis=0)
    centroid_B = np.mean(B, axis=0)

    # Center the point sets
    A_centered = A - centroid_A
    B_centered = B - centroid_B

    # Compute scale using Frobenius norm
    norm_A = np.linalg.norm(A_centered)
    norm_B = np.linalg.norm(B_centered)
    scale = norm_B / norm_A

    # Normalize both sets
    A_normalized = A_centered / norm_A
    B_normalized = B_centered / norm_B

    # Compute rotation using SVD
    H = A_normalized.T @ B_normalized
    U, _, Vt = np.linalg.svd(H)
    R_mat = Vt.T @ U.T

    # Ensure right-handed coordinate system
    if np.linalg.det(R_mat) < 0:
        Vt[-1, :] *= -1
        R_mat = Vt.T @ U.T

    # Compute translation
    t_vec = centroid_B - scale * R_mat @ centroid_A

    return R_mat, t_vec, scale
```

---

## 🔄 Example usage

```python
source = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
destination = np.array([[1, 1, 1], [2, 1, 1], [1, 2, 1]])

R_mat, t_vec, scale = best_fit_transform(source, destination)

print("Rotation matrix:\n", R_mat)
print("Translation vector:\n", t_vec)
print("Scaling factor:\n", scale)
```

---

## 📘 Mathematical Notes

- **Frobenius norm**: Measures how spread out the points are from the centroid (think of it as a generalization of Pythagoras).
- **SVD**: Decomposes a matrix into orthogonal directions and scaling along those directions. Here, it gives the optimal rotation that best aligns two sets of points in the least-squares sense.

---

## 🧪 For noisy or partial data

If your point sets are not in perfect correspondence (e.g., from a 3D scanner), you may need to use the full **ICP algorithm** with nearest-neighbor matching. The above method assumes the two sets of points are already matched in order.
