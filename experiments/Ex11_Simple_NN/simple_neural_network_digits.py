from pathlib import Path
import random
import warnings

import cv2
import numpy as np
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.cuda")
import torch
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


REPO_ROOT = Path(__file__).resolve().parents[2]
IMAGE_PATH = REPO_ROOT / "datasets" / "digit.jpg"


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def prepare_custom_image(path: Path) -> np.ndarray:
    image = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(path)

    _, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    points = cv2.findNonZero(thresholded)
    x, y, width, height = cv2.boundingRect(points)
    cropped = thresholded[y : y + height, x : x + width]

    side = max(width, height) + 8
    canvas = np.zeros((side, side), dtype=np.uint8)
    offset_x = (side - width) // 2
    offset_y = (side - height) // 2
    canvas[offset_y : offset_y + height, offset_x : offset_x + width] = cropped

    resized = cv2.resize(canvas, (8, 8), interpolation=cv2.INTER_AREA)
    return resized.astype(np.float32).reshape(1, -1) / 255.0


def main() -> None:
    set_seed(42)
    digits = load_digits()
    X = digits.data.astype(np.float32) / 16.0
    y = digits.target.astype(np.int64)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    train_loader = DataLoader(
        TensorDataset(torch.tensor(X_train), torch.tensor(y_train)),
        batch_size=64,
        shuffle=True,
        generator=torch.Generator().manual_seed(42),
    )

    model = nn.Sequential(
        nn.Linear(64, 64),
        nn.ReLU(),
        nn.Linear(64, 32),
        nn.ReLU(),
        nn.Linear(32, 10),
    )

    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.CrossEntropyLoss()

    model.train()
    for _ in range(20):
        for batch_features, batch_labels in train_loader:
            optimizer.zero_grad()
            logits = model(batch_features)
            loss = criterion(logits, batch_labels)
            loss.backward()
            optimizer.step()

    model.eval()
    with torch.no_grad():
        test_logits = model(torch.tensor(X_test))
        test_predictions = torch.argmax(test_logits, dim=1)
        test_accuracy = (test_predictions == torch.tensor(y_test)).float().mean().item()

        custom_features = torch.tensor(prepare_custom_image(IMAGE_PATH))
        custom_logits = model(custom_features)
        custom_probabilities = torch.softmax(custom_logits, dim=1).numpy()[0]
        custom_prediction = int(np.argmax(custom_probabilities))

    print("Experiment 11: Simple Neural Network on Handwritten Digits")
    print(f"Test accuracy: {test_accuracy:.4f}")
    print(f"Prediction for digit.jpg: {custom_prediction}")
    print(f"Prediction confidence: {custom_probabilities[custom_prediction]:.4f}")


if __name__ == "__main__":
    main()
