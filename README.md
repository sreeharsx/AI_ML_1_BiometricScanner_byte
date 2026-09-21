# 🔐 Biometric Scanner — AI/ML Task 1

A facial biometric classification system developed as part of **AVIP 2026 — B.Y.T.E by Arithmatrix**.

The system is trained to distinguish between:

- 👤 **Operator** — authorized person
- 🚫 **Non-operator** — other people

The model uses **MobileNetV2 transfer learning** with image augmentation and binary classification.

---

## 🎯 Objective

The objective of this task is to build a biometric scanner that grants access only when the trained model recognizes the authorized operator.

Expected behavior:

```text
Operator detected
→ Access Granted: Operator

Non-operator detected
→ Access Denied
```

---

## 📊 Dataset

The dataset contains **60 face images**:

| Class | Images |
|---|---:|
| Operator | 30 |
| Non-operator | 30 |
| **Total** | **60** |

### Operator Dataset

The operator images were collected specifically for this project.

### Non-operator Dataset

The non-operator images were selected from the **Labeled Faces in the Wild (LFW)** face dataset, using images from different identities.

The raw face images are kept locally and are **not uploaded to this repository**.

Dataset source and access instructions are documented in:

```text
data/README.md
```

---

## 🧠 Model

Because the dataset is small, this project uses **MobileNetV2 transfer learning** rather than training a deep CNN completely from scratch.

### Architecture

```text
Input Image
    ↓
224 × 224 RGB
    ↓
Data Augmentation
    ├── Random Flip
    ├── Random Rotation
    ├── Random Zoom
    └── Random Contrast
    ↓
MobileNetV2
(ImageNet pretrained weights)
    ↓
Global Average Pooling
    ↓
Dropout (0.3)
    ↓
Dense Layer
(1 neuron, Sigmoid)
    ↓
Operator Probability
```

The MobileNetV2 base model was frozen during training, while the final classification layer was trained for binary classification.

---

## ⚙️ Preprocessing

All images are:

- Converted to RGB
- Resized to `224 × 224`
- Converted to NumPy arrays
- Normalized to `[0, 1]`

Labels:

```text
Operator     = 1
Non-operator = 0
```

---

## 📚 Train/Test Split

```text
Total images    : 60
Training images : 48
Test images     : 12
```

A stratified split with `random_state=42` was used to maintain class balance.

A validation split was additionally created from the training data during model training.

---

## 📈 Training

The model was trained using:

- Optimizer: Adam
- Learning rate: `0.0001`
- Loss: Binary Cross Entropy
- Batch size: `8`
- Maximum epochs: `30`
- Early stopping: Enabled
- Best validation weights: Restored

---

# 📊 Model Evaluation

The final model was evaluated on the **held-out test set of 12 images**.

| Metric | Score |
|---|---:|
| Accuracy | **83.33%** |
| Precision | **75.00%** |
| Recall | **100.00%** |
| F1 Score | **85.71%** |

### Confusion Matrix

```text
                    Predicted
                 Non-operator  Operator
Actual
Non-operator          4           2
Operator              0           6
```

Therefore:

```text
True Negatives  = 4
False Positives = 2
False Negatives = 0
True Positives  = 6
```

The confusion matrix is available at:

```text
results/confusion_matrix.png
```

Metrics visualization:

```text
results/metrics.png
```

---

## 🔎 Interpretation

The model correctly classified **10 out of 12 test images**, resulting in an accuracy of **83.33%** on this small held-out test set.

The model correctly identified all 6 operator images in the test set, resulting in a recall of **100%** for the operator class.

There were 2 non-operator images that were incorrectly classified as operators.

These results should be interpreted cautiously because the dataset and test set are small.

---

# 🧪 Sample Predictions

Sample inference results are stored in:

```text
results/sample_predictions/
```

The samples include examples of:

- Correctly detected operator
- Correctly detected non-operator
- Misclassified non-operator
- Model confidence/probability

---

# 💾 Trained Model

The trained model is saved as:

```text
models/biometric_scanner.keras
```

The model can be loaded using TensorFlow/Keras:

```python
from tensorflow.keras.models import load_model

model = load_model("models/biometric_scanner.keras")
```

---

# 🚀 Inference

The model uses a threshold of:

```text
0.5
```

If the predicted operator probability is greater than or equal to `0.5`:

```text
Access Granted: Operator
```

Otherwise:

```text
Access Denied
```

### Example

```python
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model("models/biometric_scanner.keras")

def predict_face(image_path, threshold=0.5):

    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))

    image_array = np.array(
        image,
        dtype=np.float32
    ) / 255.0

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    probability = model.predict(
        image_array,
        verbose=0
    )[0][0]

    if probability >= threshold:
        result = "Access Granted: Operator"
    else:
        result = "Access Denied"

    return result, probability
```

Example:

```python
result, probability = predict_face("path/to/image.jpg")

print(result)
print(f"Operator probability: {probability:.4f}")
```

---

# 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/sreeharsx/AI_ML_1_BiometricScanner_byte.git
```

Move into the project directory:

```bash
cd AI_ML_1_BiometricScanner_byte
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📓 Running the Notebook

Start Jupyter:

```bash
jupyter notebook
```

or open the project in **Visual Studio Code** and open:

```text
notebooks/biometric_scanner.ipynb
```

Select the `.venv` Python environment as the notebook kernel.

The notebook contains:

1. Dataset inspection
2. Image preprocessing
3. Train/test split
4. Data augmentation
5. MobileNetV2 model creation
6. Model training
7. Training/validation plots
8. Test evaluation
9. Classification metrics
10. Confusion matrix
11. Misclassification analysis
12. Model saving
13. Model loading
14. Sample inference

---

# 📁 Project Structure

```text
AI_ML_1_BiometricScanner_byte/
│
├── data/
│   ├── README.md
│   └── raw/
│       ├── operator/
│       │   ├── operator_01.jpg
│       │   ├── operator_02.jpg
│       │   └── ...
│       │
│       └── non_operator/
│           ├── non_operator_01.jpg
│           ├── non_operator_02.jpg
│           └── ...
│
├── models/
│   └── biometric_scanner.keras
│
├── notebooks/
│   └── biometric_scanner.ipynb
│
├── results/
│   ├── confusion_matrix.png
│   ├── metrics.png
│   └── sample_predictions/
│
├── src/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# 🔒 Privacy

The raw face dataset is intentionally excluded from Git using `.gitignore`.

The following should remain local:

```text
data/raw/
.venv/
```

This repository contains the trained model, code, notebook, evaluation results, and sample outputs rather than the complete raw face dataset.

---

# ⚠️ Limitations

This project is an experimental biometric classification system and should **not be considered a production-ready security system**.

Important limitations include:

- Only 60 images were used.
- The held-out test set contains only 12 images.
- The dataset has limited variation in lighting, pose, expression, and background.
- A small dataset can lead to overfitting.
- The operator images and LFW non-operator images may have different image characteristics.
- The model may not generalize reliably to completely unseen real-world conditions.
- The system does not implement liveness detection or anti-spoofing.
- A photograph or screen displaying the operator's face could potentially be classified as the operator.
- The reported metrics represent this particular small test set and should not be interpreted as real-world biometric security performance.

---

# 🔮 Future Improvements

Possible improvements include:

- Collecting a substantially larger dataset
- Using multiple images per person under different conditions
- Adding different lighting and background conditions
- Using face detection before classification
- Implementing face embeddings
- Using a larger identity dataset
- Performing cross-validation
- Adding liveness detection
- Adding anti-spoofing mechanisms
- Testing on a completely independent dataset
- Deploying the model as a web or mobile application

---

# 💻 Technologies Used

- Python
- TensorFlow
- Keras
- MobileNetV2
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Pillow
- Jupyter Notebook
- Git
- GitHub

---

# 📦 Requirements

The required Python packages are listed in:

```text
requirements.txt
```

Install them with:

```bash
pip install -r requirements.txt
```

---

# 📝 Task Summary

This project implements a facial biometric scanner using transfer learning with MobileNetV2. A dataset of 30 operator images and 30 non-operator images was prepared, preprocessed, and divided into training and held-out test sets. Data augmentation was used to improve robustness, while the pretrained MobileNetV2 feature extractor was frozen and a binary classification head was trained.

On the 12-image held-out test set, the model achieved 83.33% accuracy, 75.00% precision, 100.00% recall, and an 85.71% F1 score. The confusion matrix contained 6 true positives, 4 true negatives, 2 false positives, and 0 false negatives.

The trained model is saved as `models/biometric_scanner.keras`, while the notebook contains the complete training, evaluation, and inference workflow.

Because the dataset is small, these results are experimental and do not represent production-level biometric security performance.

---

# 👨‍💻 Author

**Sreeharsh**

AVIP 2026 — B.Y.T.E by Arithmatrix

**Domain:** AI/ML

**Task:** Task 1 — Biometric Scanner
