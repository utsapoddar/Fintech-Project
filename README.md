# Fintech Fraud‑Detection Project

This project is a starting point for exploring credit‑card transaction data and building a simple fraud‑detection pipeline.

## Overview

The repository centres around a **Jupyter friendly Python script (`project.py`)** that reads a credit‑card transaction dataset and surfaces basic descriptive statistics. It provides a foundation for further feature engineering, model training, and evaluation. The goal of this project is to help you familiarise yourself with the dataset and to encourage you to develop your own fraud‑risk models.

## Dataset

The project uses the public **ULB credit‑card fraud dataset**, which contains **284,807 transactions** from European cardholders over two days and a `Class` column indicating whether a transaction is fraudulent. Because the dataset (~150 MB) is too large to include in the repository, please download it from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download) and place the `creditcard.csv` file in the root of this project.

## Getting started

1. **Clone this repository** or download the source code.
2. Install the required dependencies. A minimal Python environment (Python 3.8+) with **pandas** is sufficient:

   ```bash
   pip install pandas
   ```

3. Download `creditcard.csv` from Kaggle and save it alongside `project.py`.
4. Run the script:

   ```bash
   python project.py
   ```

   The script will:

   - load the dataset into a pandas DataFrame;
   - print the shape and preview of the first few rows;
   - report the number of null values per column;
   - check for negative values in the `Amount` field;
   - display the distribution of fraud vs. normal transactions;
   - show basic statistics for the `Time` and `Amount` columns.

5. Extend the code with your own analysis: try creating new features (e.g., transaction amount ratios), building classification models, or experimenting with thresholding techniques.

## Next steps

- **Feature engineering** – extract useful features such as time‑based aggregates, rolling averages, or customer behaviour metrics.
- **Model training** – implement models like logistic regression, random forests, or gradient boosting. Compare their performance using metrics such as precision, recall and AUC.
- **Thresholding and evaluation** – explore how different classification thresholds affect false positives/negatives and overall risk.

## Contributing

Feel free to fork this repository and open pull requests with improvements. Suggestions for feature engineering or model architectures are always welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
