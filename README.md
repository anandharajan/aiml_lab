# AIML Lab Experiments

This repository is organized for students to open in VS Code and run the experiments with the required datasets.

## Open In VS Code

1. Clone the repo or use GitHub `Code` -> `Download ZIP`.
2. Open the repository folder in VS Code.
3. Create and activate a virtual environment.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

4. Open the required experiment folder from the table below.
5. If the experiment is still saved as `.txt`, copy the `Program:` section into a `.py` file in the same folder.
6. Run the Python file from that folder so the local dataset copy is found correctly.

## Experiments

| No. | Experiment Folder | Experiment File | Dataset |
| --- | --- | --- | --- |
| 1(a) | [Ex01_Search](experiments/Ex01_Search/) | [Ex.No1a.txt](experiments/Ex01_Search/Ex.No1a.txt) | No external dataset |
| 1(b) | [Ex01_Search](experiments/Ex01_Search/) | [Ex.No1b.txt](experiments/Ex01_Search/Ex.No1b.txt) | No external dataset |
| 2(a) | [Ex02_Informed_Search](experiments/Ex02_Informed_Search/) | [Ex.No2a.txt](experiments/Ex02_Informed_Search/Ex.No2a.txt) | No external dataset |
| 2(b) | [Ex02_Informed_Search](experiments/Ex02_Informed_Search/) | [Ex.No2b.txt](experiments/Ex02_Informed_Search/Ex.No2b.txt) | No external dataset |
| 3 | [Ex03_Naive_Bayes](experiments/Ex03_Naive_Bayes/) | [Ex.No3.txt](experiments/Ex03_Naive_Bayes/Ex.No3.txt) | [tennisdata.csv](experiments/Ex03_Naive_Bayes/tennisdata.csv) |
| 4 | [Ex04_Bayesian_Networks](experiments/Ex04_Bayesian_Networks/) | [Ex.No4.txt](experiments/Ex04_Bayesian_Networks/Ex.No4.txt) | [heartdisease.csv](experiments/Ex04_Bayesian_Networks/heartdisease.csv) |
| 5(a) | [Ex05_Regression](experiments/Ex05_Regression/) | [Ex.No5a.txt](experiments/Ex05_Regression/Ex.No5a.txt) | [homeprices.csv](experiments/Ex05_Regression/homeprices.csv) |
| 5(b) | [Ex05_Regression](experiments/Ex05_Regression/) | [Ex.No5b.txt](experiments/Ex05_Regression/Ex.No5b.txt) | [insurance_data.csv](experiments/Ex05_Regression/insurance_data.csv) |
| 6(a) | [Ex06_Trees](experiments/Ex06_Trees/) | [Ex.No6a.txt](experiments/Ex06_Trees/Ex.No6a.txt) | [covid19.csv](experiments/Ex06_Trees/covid19.csv) |
| 6(b) | [Ex06_Trees](experiments/Ex06_Trees/) | [Ex.No6b.txt](experiments/Ex06_Trees/Ex.No6b.txt) | [covid19.csv](experiments/Ex06_Trees/covid19.csv) |
| 7 | [Ex07_SVM](experiments/Ex07_SVM/) | [Ex.No7.txt](experiments/Ex07_SVM/Ex.No7.txt) | [covid19.csv](experiments/Ex07_SVM/covid19.csv) |
| 8 | [Ex08_Ensembling_KMeans](experiments/Ex08_Ensembling_KMeans/) | [Ex.No8.txt](experiments/Ex08_Ensembling_KMeans/Ex.No8.txt) | Uses `sklearn.datasets.load_iris()` |
| 9 | [Ex09_Clustering](experiments/Ex09_Clustering/) | [Ex.No9.txt](experiments/Ex09_Clustering/Ex.No9.txt) | [income.csv](experiments/Ex09_Clustering/income.csv) |
| 10 | [Ex10_EM_Bayesian](experiments/Ex10_EM_Bayesian/) | [Ex.No10.txt](experiments/Ex10_EM_Bayesian/Ex.No10.txt) | No external dataset |
| 11 | [Ex11_Simple_NN](experiments/Ex11_Simple_NN/) | [Ex.No11.txt](experiments/Ex11_Simple_NN/Ex.No11.txt) | [digit.jpg](experiments/Ex11_Simple_NN/digit.jpg) and MNIST auto-download |
| 12 | [Ex12_DeepLearning_CNN](experiments/Ex12_DeepLearning_CNN/) | [Ex.No12.txt](experiments/Ex12_DeepLearning_CNN/Ex.No12.txt) | [cellimage/](experiments/Ex12_DeepLearning_CNN/cellimage/) |

## Master Dataset Folder

If students want one common location for all datasets, use [datasets/](datasets/).

- [tennisdata.csv](datasets/tennisdata.csv)
- [heartdisease.csv](datasets/heartdisease.csv)
- [homeprices.csv](datasets/homeprices.csv)
- [insurance_data.csv](datasets/insurance_data.csv)
- [covid19.csv](datasets/covid19.csv)
- [income.csv](datasets/income.csv)
- [digit.jpg](datasets/digit.jpg)
- [cellimage/](datasets/cellimage/)

## Requirements

Install the shared packages from [requirements.txt](requirements.txt).

## Sharing This Repo

Share this GitHub repository URL directly with students. They can either clone it or download it as a ZIP from GitHub.
