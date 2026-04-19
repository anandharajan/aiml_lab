# AIML Lab Experiments

Python-based Artificial Intelligence and Machine Learning lab programs with organized datasets, original reference notes, and VS Code friendly folder structure.

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

## Repository Layout

- [experiments/](experiments/) contains the runnable scripts and the original note files.
- [datasets/](datasets/) contains the shared datasets used by the scripts.

## Experiments

| No. | Folder | Runnable Script | Reference Note | Dataset |
| --- | --- | --- | --- | --- |
| 1(a) | [Ex01_Search](experiments/Ex01_Search/) | [bfs.py](experiments/Ex01_Search/bfs.py) | [Ex.No1a.txt](experiments/Ex01_Search/Ex.No1a.txt) | No external dataset |
| 1(b) | [Ex01_Search](experiments/Ex01_Search/) | [dfs.py](experiments/Ex01_Search/dfs.py) | [Ex.No1b.txt](experiments/Ex01_Search/Ex.No1b.txt) | No external dataset |
| 2(a) | [Ex02_Informed_Search](experiments/Ex02_Informed_Search/) | [a_star.py](experiments/Ex02_Informed_Search/a_star.py) | [Ex.No2a.txt](experiments/Ex02_Informed_Search/Ex.No2a.txt) | No external dataset |
| 2(b) | [Ex02_Informed_Search](experiments/Ex02_Informed_Search/) | [ao_star.py](experiments/Ex02_Informed_Search/ao_star.py) | [Ex.No2b.txt](experiments/Ex02_Informed_Search/Ex.No2b.txt) | No external dataset |
| 3 | [Ex03_Naive_Bayes](experiments/Ex03_Naive_Bayes/) | [naive_bayes_tennis.py](experiments/Ex03_Naive_Bayes/naive_bayes_tennis.py) | [Ex.No3.txt](experiments/Ex03_Naive_Bayes/Ex.No3.txt) | [tennisdata.csv](datasets/tennisdata.csv) |
| 4 | [Ex04_Bayesian_Networks](experiments/Ex04_Bayesian_Networks/) | [bayesian_network_heart.py](experiments/Ex04_Bayesian_Networks/bayesian_network_heart.py) | [Ex.No4.txt](experiments/Ex04_Bayesian_Networks/Ex.No4.txt) | [heartdisease.csv](datasets/heartdisease.csv) |
| 5(a) | [Ex05_Regression](experiments/Ex05_Regression/) | [linear_regression_homeprices.py](experiments/Ex05_Regression/linear_regression_homeprices.py) | [Ex.No5a.txt](experiments/Ex05_Regression/Ex.No5a.txt) | [homeprices.csv](datasets/homeprices.csv) |
| 5(b) | [Ex05_Regression](experiments/Ex05_Regression/) | [logistic_regression_insurance.py](experiments/Ex05_Regression/logistic_regression_insurance.py) | [Ex.No5b.txt](experiments/Ex05_Regression/Ex.No5b.txt) | [insurance_data.csv](datasets/insurance_data.csv) |
| 6(a) | [Ex06_Trees](experiments/Ex06_Trees/) | [decision_tree_covid.py](experiments/Ex06_Trees/decision_tree_covid.py) | [Ex.No6a.txt](experiments/Ex06_Trees/Ex.No6a.txt) | [covid19.csv](datasets/covid19.csv) |
| 6(b) | [Ex06_Trees](experiments/Ex06_Trees/) | [random_forest_covid.py](experiments/Ex06_Trees/random_forest_covid.py) | [Ex.No6b.txt](experiments/Ex06_Trees/Ex.No6b.txt) | [covid19.csv](datasets/covid19.csv) |
| 7 | [Ex07_SVM](experiments/Ex07_SVM/) | [svm_covid.py](experiments/Ex07_SVM/svm_covid.py) | [Ex.No7.txt](experiments/Ex07_SVM/Ex.No7.txt) | [covid19.csv](datasets/covid19.csv) |
| 8 | [Ex08_Ensembling_KMeans](experiments/Ex08_Ensembling_KMeans/) | [kmeans_gmm_iris.py](experiments/Ex08_Ensembling_KMeans/kmeans_gmm_iris.py) | [Ex.No8.txt](experiments/Ex08_Ensembling_KMeans/Ex.No8.txt) | Uses `sklearn.datasets.load_iris()` |
| 9 | [Ex09_Clustering](experiments/Ex09_Clustering/) | [kmeans_income.py](experiments/Ex09_Clustering/kmeans_income.py) | [Ex.No9.txt](experiments/Ex09_Clustering/Ex.No9.txt) | [income.csv](datasets/income.csv) |
| 10 | [Ex10_EM_Bayesian](experiments/Ex10_EM_Bayesian/) | [em_coin_toss.py](experiments/Ex10_EM_Bayesian/em_coin_toss.py) | [Ex.No10.txt](experiments/Ex10_EM_Bayesian/Ex.No10.txt) | No external dataset |
| 11 | [Ex11_Simple_NN](experiments/Ex11_Simple_NN/) | [simple_neural_network_digits.py](experiments/Ex11_Simple_NN/simple_neural_network_digits.py) | [Ex.No11.txt](experiments/Ex11_Simple_NN/Ex.No11.txt) | [digit.jpg](datasets/digit.jpg) |
| 12 | [Ex12_DeepLearning_CNN](experiments/Ex12_DeepLearning_CNN/) | [cnn_cellimage.py](experiments/Ex12_DeepLearning_CNN/cnn_cellimage.py) | [Ex.No12.txt](experiments/Ex12_DeepLearning_CNN/Ex.No12.txt) | [cellimage/](datasets/cellimage/) |

## Notes

- The original lab-note text files are preserved for reference.
- The runnable scripts are the source of truth for execution.
- Experiment 11 uses a simple neural network with PyTorch on the handwritten digits dataset.
- Experiment 12 uses a CNN with PyTorch and the included `cellimage` folder dataset.

## Share With Students

Share the repository link directly. Students can:

1. Clone the repository in VS Code.
2. Open any script from the table above.
3. Run the script with the dataset linked in the table.
