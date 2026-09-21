from pathlib import Path
import argparse

import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model


IMG_SIZE = (224, 224)
DEFAULT_THRESHOLD = 0.5


def predict_face(image_path, model, threshold=DEFAULT_THRESHOLD):
    image = Image.open(image_path).convert("RGB")
    image = image.resize(IMG_SIZE)

    image_array = np.array(image, dtype=np.float32) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    probability = float(
        model.predict(image_array, verbose=0)[0][0]
    )

    if probability >= threshold:
        prediction = "Operator"
        access = "Access Granted: Operator"
    else:
        prediction = "Non-operator"
        access = "Access Denied"

    return prediction, probability, access


def main():
    parser = argparse.ArgumentParser(
        description="Biometric Scanner inference"
    )

    parser.add_argument(
        "--image",
        required=True,
        help="Path to the image to classify"
    )

    parser.add_argument(
        "--model",
        default="models/biometric_scanner.keras",
        help="Path to the trained Keras model"
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        help="Classification threshold (default: 0.5)"
    )

    args = parser.parse_args()

    image_path = Path(args.image)
    model_path = Path(args.model)

    if not image_path.exists():
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    model = load_model(model_path)

    prediction, probability, access = predict_face(
        image_path,
        model,
        args.threshold
    )

    print(f"Prediction: {prediction}")
    print(f"Operator probability: {probability:.4f}")
    print(access)


if __name__ == "__main__":
    main()