from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "datasets" / "tennisdata.csv"


def encode_frame(frame: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, LabelEncoder]]:
    encoders: dict[str, LabelEncoder] = {}
    encoded = frame.copy()
    for column in encoded.columns:
        encoder = LabelEncoder()
        encoded[column] = encoder.fit_transform(encoded[column])
        encoders[column] = encoder
    return encoded, encoders


def main() -> None:
    data = pd.read_csv(DATA_PATH)
    encoded, encoders = encode_frame(data)

    X = encoded.drop(columns=["PlayTennis"])
    y = encoded["PlayTennis"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = GaussianNB()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)

    sample = pd.DataFrame(
        [{"Outlook": "Sunny", "Temperature": "Cool", "Humidity": "High", "Windy": "Strong"}]
    )
    for column in sample.columns:
        sample[column] = encoders[column].transform(sample[column])
    prediction = encoders["PlayTennis"].inverse_transform(model.predict(sample))[0]

    print("Experiment 3: Naive Bayes on PlayTennis")
    print(f"Dataset rows: {len(data)}")
    print(f"Test accuracy: {accuracy:.4f}")
    print(f"Prediction for Sunny/Cool/High/Strong: {prediction}")


if __name__ == "__main__":
    main()
