import math

import numpy as np


def ncr(n: int, r: int) -> float:
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def binomial(x: int, n: int, p: float) -> float:
    return ncr(n, x) * (p**x) * ((1 - p) ** (n - x))


def main() -> None:
    observations = np.array([5, 9, 8, 4, 7])
    tosses_per_trial = 10
    mixing_weight = 0.5
    p_a = 0.6
    p_b = 0.5

    print("Experiment 10: Expectation Maximization for Coin Tosses")
    print(f"Initial parameters: p_a={p_a:.6f}, p_b={p_b:.6f}")

    for iteration in range(1, 11):
        responsibilities = np.zeros((len(observations), 2))
        for index, heads in enumerate(observations):
            responsibilities[index, 0] = mixing_weight * binomial(heads, tosses_per_trial, p_a)
            responsibilities[index, 1] = (1 - mixing_weight) * binomial(heads, tosses_per_trial, p_b)
            responsibilities[index, :] /= responsibilities[index, :].sum()

        p_a = float(np.sum((observations / tosses_per_trial) * responsibilities[:, 0]) / responsibilities[:, 0].sum())
        p_b = float(np.sum((observations / tosses_per_trial) * responsibilities[:, 1]) / responsibilities[:, 1].sum())

        print(f"Iteration {iteration:02d}: p_a={p_a:.6f}, p_b={p_b:.6f}")


if __name__ == "__main__":
    main()
