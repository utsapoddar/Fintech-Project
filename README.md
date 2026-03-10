# Fintech Fraud‑Detection Project

This project is a starting point for exploring credit‑card transaction data and building a simple fraud‑detection pipeline.

## Overview

The repository contains an **exploratory data analysis script (`project.py`)** and a **Random Forest fraud detection model (`model.py`)**. The EDA script surfaces basic descriptive statistics, while the model trains a balanced Random Forest classifier that achieves **96% precision and 74% recall** on fraud detection.

## Dataset

The project uses the public **ULB credit‑card fraud dataset**, which contains **284,807 transactions** from European cardholders over two days and a `Class` column indicating whether a transaction is fraudulent. Because the dataset (~150 MB) is too large to include in the repository, please download it from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download) and place the `creditcard.csv` file in the root of this project.

## Getting started

1. **Clone this repository** or download the source code.
2. Create and activate a virtual environment (Python 3.14):

   ```bash
   python -m venv fintechproject
   source fintechproject/Scripts/activate    # Windows (Git Bash)
   source fintechproject/bin/activate        # macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install pandas scikit-learn
   ```

4. Download `creditcard.csv` from Kaggle and save it in the project root.
5. Run the EDA script:

   ```bash
   python project.py
   ```

   This will print dataset shape, null values, class distribution, and basic statistics.

6. Run the fraud detection model:

   ```bash
   python model.py
   ```

   This will train a Random Forest classifier and print the confusion matrix and classification report (precision, recall, F1-score).

## Next steps

- **Feature engineering** – extract useful features such as time‑based aggregates, rolling averages, or customer behaviour metrics.
- **Additional models** – compare performance with logistic regression, gradient boosting, or neural networks using metrics such as AUC and F1-score.
- **Thresholding and evaluation** – explore how different classification thresholds affect false positives/negatives and overall risk.

## Contributing

Feel free to fork this repository and open pull requests with improvements. Suggestions for feature engineering or model architectures are always welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
