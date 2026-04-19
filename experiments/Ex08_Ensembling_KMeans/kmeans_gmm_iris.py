from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler


def main() -> None:
    iris = load_iris(as_frame=True)
    X = iris.data
    y = iris.target

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans_labels = kmeans.fit_predict(X)

    scaled = StandardScaler().fit_transform(X)
    gmm = GaussianMixture(n_components=3, random_state=42)
    gmm_labels = gmm.fit_predict(scaled)

    print("Experiment 8: K-Means and GMM on Iris")
    print(f"KMeans inertia: {kmeans.inertia_:.4f}")
    print(f"KMeans adjusted rand index: {adjusted_rand_score(y, kmeans_labels):.4f}")
    print(f"GMM adjusted rand index: {adjusted_rand_score(y, gmm_labels):.4f}")


if __name__ == "__main__":
    main()
