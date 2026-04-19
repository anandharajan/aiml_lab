from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "datasets" / "homeprices.csv"


def main() -> None:
    data = pd.read_csv(DATA_PATH)
    data["bedrooms"] = data["bedrooms"].fillna(data["bedrooms"].median())

    model = LinearRegression()
    X = data[["area", "bedrooms", "age"]]
    y = data["price"]
    model.fit(X, y)

    prediction_one = model.predict([[3000, 3, 40]])[0]
    prediction_two = model.predict([[2500, 4, 5]])[0]

    print("Experiment 5(a): Linear Regression")
    print(f"Coefficients: {model.coef_.round(4).tolist()}")
    print(f"Intercept: {model.intercept_:.4f}")
    print(f"Predicted price for [3000, 3, 40]: {prediction_one:.2f}")
    print(f"Predicted price for [2500, 4, 5]: {prediction_two:.2f}")


if __name__ == "__main__":
    main()
