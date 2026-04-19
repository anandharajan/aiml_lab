from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "datasets" / "covid19.csv"


def prepare_features(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    features = data.drop(columns=["Label"]).copy()
    for column in features.select_dtypes(include="object").columns:
        features[column] = LabelEncoder().fit_transform(features[column])
    return features, data["Label"]


def main() -> None:
    data = pd.read_csv(DATA_PATH)
    X, y = prepare_features(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=42, stratify=y
    )

    model = DecisionTreeClassifier(random_state=42, max_depth=4)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    cv_scores = cross_val_score(model, X, y, cv=5)

    print("Experiment 6(a): Decision Tree")
    print(f"Test accuracy: {accuracy_score(y_test, predictions):.4f}")
    print(f"Cross-validation mean accuracy: {cv_scores.mean():.4f}")
    print(f"Cross-validation scores: {[round(score, 4) for score in cv_scores]}")


if __name__ == "__main__":
    main()
