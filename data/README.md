# Dataset

This directory contains the dataset information and documentation for the Biometric Scanner project.

## Dataset Composition

The dataset follows the requirements of Task 1 of the AVIP 2026 AI/ML Engineering track.

It consists of:

- 30 images of the operator
- 30 images of non-operators

## Local Dataset Structure

The dataset is maintained locally in the following structure:

```text
data/
├── raw/
│   ├── operator/
│   │   ├── image_01.jpg
│   │   ├── image_02.jpg
│   │   └── ...
│   │
│   └── non_operator/
│       ├── image_01.jpg
│       ├── image_02.jpg
│       └── ...
│
└── processed/
    ├── operator/
    └── non_operator/