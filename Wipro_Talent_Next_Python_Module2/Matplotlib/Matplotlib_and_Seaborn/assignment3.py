#Perform Exploratory Data Analysis for the dataset Social_Network_Ads.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Social_Network_Ads.csv")

print(df.info())
print(df.describe())

sns.histplot(data=df, x='Age', hue='Purchased', kde=True)
plt.show()

sns.boxplot(data=df, x='Purchased', y='EstimatedSalary')
plt.show()

sns.countplot(data=df, x='Gender', hue='Purchased')
plt.show()

sns.pairplot(df[['Age', 'EstimatedSalary', 'Purchased']], hue='Purchased')
plt.show()
