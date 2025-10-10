import pandas as pd

# Load the credit card transaction data (make sure creditcard.csv is present locally)
df = pd.read_csv("creditcard.csv")

# Print basic shape and preview of data
print("rows, cols:", df.shape)
print(df.head(2))

# Null values summary
print("\nNulls per column:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Negative amounts check
print("\nAny negative amounts?:", (df["Amount"] < 0).any())

# Class distribution (0 = normal, 1 = fraud)
print("\nClass distribution (0=normal, 1=fraud):")
print(df["Class"].value_counts())

# Describe 'Time' and 'Amount' columns
print("\nDescribe Time & Amount:")
print(df[["Time", "Amount"]].describe())

# lets try to add some more lines
# lets try this again
