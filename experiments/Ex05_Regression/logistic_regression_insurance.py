from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "datasets" / "insurance_data.csv"


def main() -> None:
    data = pd.read_csv(DATA_PATH)
    X = data[["age"]]
    y = data["bought_insurance"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.8, random_state=42, stratify=y
    )

    model = LogisticRegression(solver="liblinear", random_state=42)
    model.fit(X_train, y_train)

    age_35_probability = model.predict_proba([[35]])[0, 1]
    age_43_probability = model.predict_proba([[43]])[0, 1]

    print("Experiment 5(b): Logistic Regression")
    print(f"Test accuracy: {model.score(X_test, y_test):.4f}")
    print(f"P(buy insurance | age=35): {age_35_probability:.4f}")
    print(f"P(buy insurance | age=43): {age_43_probability:.4f}")
    print(f"Coefficient: {model.coef_[0, 0]:.4f}")
    print(f"Intercept: {model.intercept_[0]:.4f}")


if __name__ == "__main__":
    main()
