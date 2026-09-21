# Biometric Scanner

A face image classification project developed as part of the **Arithmatrix Virtual Internship Program (AVIP) 2026 – AI/ML Engineering**.

## Overview

The Biometric Scanner is a binary image classification system designed to distinguish between the authorized operator and non-operator faces.

The system is trained using a small custom dataset consisting of images of the operator and other individuals.

## Objective

The objective of this project is to build an image classification model that outputs:

- `Access Granted: Operator` when the input image is classified as the operator.
- `Access Denied` when the input image is classified as a non-operator.

## Dataset

The dataset consists of:

- 30 images of the operator
- 30 images of non-operators

The raw face images are kept locally and are not included in this public repository.

See [`data/README.md`](data/README.md) for dataset organization and preparation details.

## Project Structure

```text
AI_ML_1_BiometricScanner_byte/
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── biometric_scanner.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── inference.py
│
├── models/
│
├── results/
│   ├── confusion_matrix.png
│   ├── metrics.png
│   └── sample_predictions/
│
├── .gitignore
├── README.md
└── requirements.txt