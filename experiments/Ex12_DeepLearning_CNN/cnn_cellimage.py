from pathlib import Path
import random
import warnings

import numpy as np
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.cuda")
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "datasets" / "cellimage"


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)


def accuracy(model: nn.Module, data_loader: DataLoader) -> float:
    correct = 0
    total = 0
    model.eval()
    with torch.no_grad():
        for images, labels in data_loader:
            logits = model(images)
            predictions = torch.argmax(logits, dim=1)
            correct += int((predictions == labels).sum().item())
            total += len(labels)
    return correct / total


def main() -> None:
    set_seed(42)
    transform = transforms.Compose([transforms.Resize((64, 64)), transforms.ToTensor()])

    train_dataset = datasets.ImageFolder(DATA_DIR / "train", transform=transform)
    val_dataset = datasets.ImageFolder(DATA_DIR / "val", transform=transform)
    test_dataset = datasets.ImageFolder(DATA_DIR / "test", transform=transform)

    train_loader = DataLoader(
        train_dataset,
        batch_size=8,
        shuffle=True,
        num_workers=0,
        generator=torch.Generator().manual_seed(42),
    )
    val_loader = DataLoader(val_dataset, batch_size=8, shuffle=False, num_workers=0)
    test_loader = DataLoader(test_dataset, batch_size=8, shuffle=False, num_workers=0)

    model = nn.Sequential(
        nn.Conv2d(3, 16, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2),
        nn.Conv2d(16, 32, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2),
        nn.Flatten(),
        nn.Linear(32 * 16 * 16, 64),
        nn.ReLU(),
        nn.Linear(64, 4),
    )

    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(1, 9):
        model.train()
        epoch_loss = 0.0
        for images, labels in train_loader:
            optimizer.zero_grad()
            logits = model(images)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()
            epoch_loss += float(loss.item())
        val_accuracy = accuracy(model, val_loader)
        print(f"Epoch {epoch:02d}: train_loss={epoch_loss / len(train_loader):.4f}, val_accuracy={val_accuracy:.4f}")

    test_accuracy = accuracy(model, test_loader)

    print("Experiment 12: CNN on Cell Image Dataset")
    print(f"Classes: {train_dataset.classes}")
    print(f"Test accuracy: {test_accuracy:.4f}")


if __name__ == "__main__":
    main()
