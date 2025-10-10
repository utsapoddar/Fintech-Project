import pandas as pd
import numpy as np


df = pd.read_csv("creditcard.csv")
print("There are nulls." if df.isnull().any().any() else "No nulls.")
