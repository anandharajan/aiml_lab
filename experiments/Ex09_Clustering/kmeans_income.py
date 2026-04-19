from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "datasets" / "income.csv"


def main() -> None:
    data = pd.read_csv(DATA_PATH)
    scaled = data.copy()

    scaled["Age"] = MinMaxScaler().fit_transform(data[["Age"]])
    scaled["Income($)"] = MinMaxScaler().fit_transform(data[["Income($)"]])

    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = model.fit_predict(scaled[["Age", "Income($)"]])
    scaled["cluster"] = clusters

    sse = []
    for k in range(1, 10):
        current_model = KMeans(n_clusters=k, random_state=42, n_init=10)
        current_model.fit(scaled[["Age", "Income($)"]])
        sse.append(round(current_model.inertia_, 4))

    print("Experiment 9: K-Means Clustering on Income")
    print(f"Cluster centers: {model.cluster_centers_.round(4).tolist()}")
    print(f"Cluster counts: {scaled['cluster'].value_counts().sort_index().to_dict()}")
    print(f"Elbow SSE: {sse}")


if __name__ == "__main__":
    main()
