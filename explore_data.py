import pandas as pd

df = pd.read_csv("Churn_Modelling.csv")
print(df.head())
print("\nSütunlar:\n", df.columns)
print("\nEksik veri var mı?\n", df.isnull().sum())