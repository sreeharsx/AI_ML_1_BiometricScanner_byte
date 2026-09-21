# Dataset Documentation

## Overview

This folder documents the dataset used for **AVIP 2026 — AI/ML Task 1: Biometric Scanner**.

The project uses two classes:

| Class | Number of Images | Description |
|---|---:|---|
| `operator` | 30 | Face images of the authorized operator collected for this project |
| `non_operator` | 30 | Face images selected from the Labeled Faces in the Wild (LFW) dataset |

**Total images:** 60

---

## Dataset Structure

```text
data/
├── README.md
└── raw/
    ├── operator/
    │   ├── operator_01.jpg
    │   ├── operator_02.jpg
    │   └── ...
    │
    └── non_operator/
        ├── non_operator_01.jpg
        ├── non_operator_02.jpg
        └── ...
```

---

## Operator Dataset

The 30 operator images were collected specifically for this project.

They represent the authorized operator that the biometric scanner is trained to recognize.

The images are stored locally in:

```text
data/raw/operator/
```

The raw operator images are excluded from the public GitHub repository for privacy reasons.

---

## Non-operator Dataset

The 30 non-operator images were selected from the **Labeled Faces in the Wild (LFW)** dataset.

The dataset version used for this project is the **LFW Deep-Funneled** image set.

The images were selected from different identities and renamed according to this project's naming convention:

```text
non_operator_01.jpg
non_operator_02.jpg
...
non_operator_30.jpg
```

The selected images are stored locally in:

```text
data/raw/non_operator/
```

The raw non-operator images are excluded from the public GitHub repository.

---

## Dataset Source

**Source:** Kaggle — Labelled Faces in the Wild (LFW) Dataset

**Kaggle dataset:**

https://www.kaggle.com/datasets/jessicali9530/lfw-dataset

**Dataset section used:**

`lfw-deepfunneled`

The Kaggle dataset contains the deep-funneled version of LFW. The dataset page describes LFW as a face-image database containing images collected from the web for studying unconstrained face recognition. It provides the `lfw-deepfunneled` image archive along with metadata files.

---

## Access Instructions

To obtain the non-operator source dataset:

1. Open the Kaggle LFW dataset:
   https://www.kaggle.com/datasets/jessicali9530/lfw-dataset

2. Download the dataset from Kaggle.

3. Extract the downloaded files.

4. Open the:

```text
lfw-deepfunneled/
```

directory.

5. Select 30 face images from different identities for the non-operator class.

6. Rename the selected images using:

```text
non_operator_01.jpg
non_operator_02.jpg
...
non_operator_30.jpg
```

7. Place them inside:

```text
data/raw/non_operator/
```

The exact selected images used in this experiment are not committed to GitHub.

---

## Data Preparation

The selected images were renamed to provide a consistent project-specific naming convention.

Before training, images were:

- Loaded using Pillow
- Converted to RGB
- Resized to `224 × 224`
- Converted to NumPy arrays
- Normalized to the `[0, 1]` range

The operator class was assigned label:

```text
1 = Operator
```

The non-operator class was assigned label:

```text
0 = Non-operator
```

---

## Privacy

Face images are biometric data. The raw face images are therefore kept locally and excluded from version control.

The repository contains the project code, notebook, trained model, evaluation results, and sample outputs rather than the complete raw dataset.

---

## Dataset Limitations

This experiment uses a small dataset of only 60 images.

Potential limitations include:

- Limited number of images
- Limited variation in lighting
- Limited variation in facial pose
- Limited variation in facial expression
- Limited background variation
- Limited image-quality variation
- Possible differences between the operator images and LFW images

The non-operator images originate from LFW, while the operator images were collected separately. This difference in data sources may introduce dataset-specific visual characteristics that can influence model performance.

Therefore, the reported evaluation results should be considered experimental results for this particular dataset and should not be interpreted as production-level biometric security performance.
