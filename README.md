# AIML Lab Experiments

This repository contains clean, runnable AIML lab programs, the required datasets, and a verified expected-results report.

## Quick Start In VS Code

1. Clone the repo or use GitHub `Code` -> `Download ZIP`.
2. Open the repository in VS Code.
3. Create and activate a virtual environment.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

4. Open any script from the table below and run it in the VS Code terminal.
5. To verify the whole lab at once, run:

```powershell
python verify_all.py
```

Verified outputs are tracked in [EXPECTED_RESULTS.md](EXPECTED_RESULTS.md).

## Repository Layout

- [experiments/](experiments/) contains the runnable scripts and the original note files.
- [datasets/](datasets/) contains the shared datasets used by the scripts.
- [verification/outputs/](verification/outputs/) contains the captured output from the last full verification run.

## Verified Experiments

| No. | Folder | Runnable Script | Reference Note | Dataset | Verified Output |
| --- | --- | --- | --- | --- | --- |
| 1(a) | [Ex01_Search](experiments/Ex01_Search/) | [bfs.py](experiments/Ex01_Search/bfs.py) | [Ex.No1a.txt](experiments/Ex01_Search/Ex.No1a.txt) | No external dataset | [ex01a_bfs.txt](verification/outputs/ex01a_bfs.txt) |
| 1(b) | [Ex01_Search](experiments/Ex01_Search/) | [dfs.py](experiments/Ex01_Search/dfs.py) | [Ex.No1b.txt](experiments/Ex01_Search/Ex.No1b.txt) | No external dataset | [ex01b_dfs.txt](verification/outputs/ex01b_dfs.txt) |
| 2(a) | [Ex02_Informed_Search](experiments/Ex02_Informed_Search/) | [a_star.py](experiments/Ex02_Informed_Search/a_star.py) | [Ex.No2a.txt](experiments/Ex02_Informed_Search/Ex.No2a.txt) | No external dataset | [ex02a_a_star.txt](verification/outputs/ex02a_a_star.txt) |
| 2(b) | [Ex02_Informed_Search](experiments/Ex02_Informed_Search/) | [ao_star.py](experiments/Ex02_Informed_Search/ao_star.py) | [Ex.No2b.txt](experiments/Ex02_Informed_Search/Ex.No2b.txt) | No external dataset | [ex02b_ao_star.txt](verification/outputs/ex02b_ao_star.txt) |
| 3 | [Ex03_Naive_Bayes](experiments/Ex03_Naive_Bayes/) | [naive_bayes_tennis.py](experiments/Ex03_Naive_Bayes/naive_bayes_tennis.py) | [Ex.No3.txt](experiments/Ex03_Naive_Bayes/Ex.No3.txt) | [tennisdata.csv](datasets/tennisdata.csv) | [ex03_naive_bayes.txt](verification/outputs/ex03_naive_bayes.txt) |
| 4 | [Ex04_Bayesian_Networks](experiments/Ex04_Bayesian_Networks/) | [bayesian_network_heart.py](experiments/Ex04_Bayesian_Networks/bayesian_network_heart.py) | [Ex.No4.txt](experiments/Ex04_Bayesian_Networks/Ex.No4.txt) | [heartdisease.csv](datasets/heartdisease.csv) | [ex04_bayesian_network.txt](verification/outputs/ex04_bayesian_network.txt) |
| 5(a) | [Ex05_Regression](experiments/Ex05_Regression/) | [linear_regression_homeprices.py](experiments/Ex05_Regression/linear_regression_homeprices.py) | [Ex.No5a.txt](experiments/Ex05_Regression/Ex.No5a.txt) | [homeprices.csv](datasets/homeprices.csv) | [ex05a_linear_regression.txt](verification/outputs/ex05a_linear_regression.txt) |
| 5(b) | [Ex05_Regression](experiments/Ex05_Regression/) | [logistic_regression_insurance.py](experiments/Ex05_Regression/logistic_regression_insurance.py) | [Ex.No5b.txt](experiments/Ex05_Regression/Ex.No5b.txt) | [insurance_data.csv](datasets/insurance_data.csv) | [ex05b_logistic_regression.txt](verification/outputs/ex05b_logistic_regression.txt) |
| 6(a) | [Ex06_Trees](experiments/Ex06_Trees/) | [decision_tree_covid.py](experiments/Ex06_Trees/decision_tree_covid.py) | [Ex.No6a.txt](experiments/Ex06_Trees/Ex.No6a.txt) | [covid19.csv](datasets/covid19.csv) | [ex06a_decision_tree.txt](verification/outputs/ex06a_decision_tree.txt) |
| 6(b) | [Ex06_Trees](experiments/Ex06_Trees/) | [random_forest_covid.py](experiments/Ex06_Trees/random_forest_covid.py) | [Ex.No6b.txt](experiments/Ex06_Trees/Ex.No6b.txt) | [covid19.csv](datasets/covid19.csv) | [ex06b_random_forest.txt](verification/outputs/ex06b_random_forest.txt) |
| 7 | [Ex07_SVM](experiments/Ex07_SVM/) | [svm_covid.py](experiments/Ex07_SVM/svm_covid.py) | [Ex.No7.txt](experiments/Ex07_SVM/Ex.No7.txt) | [covid19.csv](datasets/covid19.csv) | [ex07_svm.txt](verification/outputs/ex07_svm.txt) |
| 8 | [Ex08_Ensembling_KMeans](experiments/Ex08_Ensembling_KMeans/) | [kmeans_gmm_iris.py](experiments/Ex08_Ensembling_KMeans/kmeans_gmm_iris.py) | [Ex.No8.txt](experiments/Ex08_Ensembling_KMeans/Ex.No8.txt) | Uses `sklearn.datasets.load_iris()` | [ex08_kmeans_gmm.txt](verification/outputs/ex08_kmeans_gmm.txt) |
| 9 | [Ex09_Clustering](experiments/Ex09_Clustering/) | [kmeans_income.py](experiments/Ex09_Clustering/kmeans_income.py) | [Ex.No9.txt](experiments/Ex09_Clustering/Ex.No9.txt) | [income.csv](datasets/income.csv) | [ex09_kmeans_income.txt](verification/outputs/ex09_kmeans_income.txt) |
| 10 | [Ex10_EM_Bayesian](experiments/Ex10_EM_Bayesian/) | [em_coin_toss.py](experiments/Ex10_EM_Bayesian/em_coin_toss.py) | [Ex.No10.txt](experiments/Ex10_EM_Bayesian/Ex.No10.txt) | No external dataset | [ex10_em.txt](verification/outputs/ex10_em.txt) |
| 11 | [Ex11_Simple_NN](experiments/Ex11_Simple_NN/) | [simple_neural_network_digits.py](experiments/Ex11_Simple_NN/simple_neural_network_digits.py) | [Ex.No11.txt](experiments/Ex11_Simple_NN/Ex.No11.txt) | [digit.jpg](datasets/digit.jpg) | [ex11_simple_nn.txt](verification/outputs/ex11_simple_nn.txt) |
| 12 | [Ex12_DeepLearning_CNN](experiments/Ex12_DeepLearning_CNN/) | [cnn_cellimage.py](experiments/Ex12_DeepLearning_CNN/cnn_cellimage.py) | [Ex.No12.txt](experiments/Ex12_DeepLearning_CNN/Ex.No12.txt) | [cellimage/](datasets/cellimage/) | [ex12_cnn.txt](verification/outputs/ex12_cnn.txt) |

## Notes

- The original lab-note text files are preserved for reference.
- The runnable scripts are deterministic and are the source of truth for execution.
- Experiment 11 uses a simple neural network with PyTorch on the handwritten digits dataset.
- Experiment 12 uses a CNN with PyTorch and the included `cellimage` folder dataset.

## Share With Students

Share the repository link directly. Students can:

1. Clone the repository in VS Code.
2. Open any script from the table above.
3. Compare their run with the linked verified output file.
