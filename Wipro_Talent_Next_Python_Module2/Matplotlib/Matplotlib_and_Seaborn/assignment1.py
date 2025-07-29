#Perform Exploratory Data Analysis for the dataset Mall_Customers.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Mall_Customers.csv")

print(df.info())
print(df.describe())

sns.histplot(data=df, x='Age', kde=True)
plt.show()

sns.boxplot(data=df, x='Gender', y='Spending Score (1-100)')
plt.show()

sns.pairplot(df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']])
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
