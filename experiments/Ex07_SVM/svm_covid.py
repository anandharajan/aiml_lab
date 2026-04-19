from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC


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

    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("svm", SVC(kernel="linear", probability=False, random_state=42)),
        ]
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    decision_scores = model.decision_function(X_test)

    print("Experiment 7: Support Vector Machine")
    print(f"Test accuracy: {accuracy_score(y_test, predictions):.4f}")
    print(f"ROC AUC: {roc_auc_score(y_test, decision_scores):.4f}")


if __name__ == "__main__":
    main()
