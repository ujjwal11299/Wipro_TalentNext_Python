#House Price Prediction,Dataset: melb data.csv

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("melb_data.csv")

df = df.drop_duplicates()

df = df.drop(columns=['BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude', 'Longtitude'], errors='ignore')

df = df.dropna()

cat_cols = df.select_dtypes(include='object').columns

for col in cat_cols:
    if df[col].nunique() < 20:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))
    else:
        df = df.drop(columns=[col])

print(df.info())


