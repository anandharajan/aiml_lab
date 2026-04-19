from itertools import product
from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "datasets" / "heartdisease.csv"


def estimate_cpt(data: pd.DataFrame, child: str, parents: list[str], alpha: float = 1.0) -> dict[tuple, dict[int, float]]:
    child_states = sorted(data[child].unique())
    if not parents:
        counts = data[child].value_counts()
        total = len(data)
        return {
            (): {
                state: (counts.get(state, 0) + alpha) / (total + alpha * len(child_states))
                for state in child_states
            }
        }

    parent_state_space = [sorted(data[parent].unique()) for parent in parents]
    table: dict[tuple, dict[int, float]] = {}
    for parent_values in product(*parent_state_space):
        subset = data
        for parent, value in zip(parents, parent_values):
            subset = subset[subset[parent] == value]
        total = len(subset)
        denominator = total + alpha * len(child_states)
        table[parent_values] = {
            state: (subset[child].eq(state).sum() + alpha) / denominator for state in child_states
        }
    return table


def main() -> None:
    data = pd.read_csv(DATA_PATH)

    p_age = estimate_cpt(data, "age", [])
    p_gender = estimate_cpt(data, "Gender", [])
    p_family = estimate_cpt(data, "Family", [])
    p_lifestyle = estimate_cpt(data, "Lifestyle", ["age", "Gender"])
    p_diet = estimate_cpt(data, "diet", ["Lifestyle"])
    p_cholestrol = estimate_cpt(data, "cholestrol", ["diet"])
    p_heart = estimate_cpt(data, "heartdisease", ["Family", "cholestrol"])

    evidence = {"age": 1, "Gender": 1, "Family": 0, "diet": 1, "Lifestyle": 0, "cholestrol": 1}
    posterior = {}
    for state in sorted(data["heartdisease"].unique()):
        probability = (
            p_age[()][evidence["age"]]
            * p_gender[()][evidence["Gender"]]
            * p_family[()][evidence["Family"]]
            * p_lifestyle[(evidence["age"], evidence["Gender"])][evidence["Lifestyle"]]
            * p_diet[(evidence["Lifestyle"],)][evidence["diet"]]
            * p_cholestrol[(evidence["diet"],)][evidence["cholestrol"]]
            * p_heart[(evidence["Family"], evidence["cholestrol"])][state]
        )
        posterior[state] = probability

    normalizer = sum(posterior.values())
    posterior = {state: value / normalizer for state, value in posterior.items()}

    print("Experiment 4: Bayesian Network Inference")
    print(f"Evidence: {evidence}")
    print("Posterior distribution for heartdisease:")
    for state, probability in sorted(posterior.items()):
        print(f"  heartdisease={state}: {probability:.4f}")


if __name__ == "__main__":
    main()
