#Perform Exploratory Data Analysis for the dataset salary_data.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("salary_data.csv")

print(df.info())
print(df.describe())

sns.scatterplot(data=df, x='YearsExperience', y='Salary')
plt.show()

sns.regplot(data=df, x='YearsExperience', y='Salary')
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='YlGnBu')
plt.show()
