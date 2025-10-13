# fintech-risk-seed

This repository contains a minimal starting point for exploring the ULB credit card fraud detection dataset and building a simple fraud risk pipeline.

## Data

The dataset used here (`creditcard.csv`) is not included in this repository due to its size. You can download it from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download) and place it in the root of this project. The CSV contains 284 807 transactions from European cardholders over two days, with a `Class` column indicating whether a transaction is fraudulent.

## Usage

Run the Python script `project.py` after placing `creditcard.csv` in the project directory. The script will:

- load the dataset into a pandas DataFrame;
- print the number of rows and columns and show a preview of the first two rows;
- report the number of null values in each column;
- check for any negative values in the `Amount` field;
- display the distribution of the `Class` labels (0 = normal, 1 = fraud);
- show basic statistics for the `Time` and `Amount` columns

Feel free to extend the script with feature engineering, model training, and thresholding based on your analysis plan.
