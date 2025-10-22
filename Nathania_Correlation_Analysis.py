#
# Nathania, 2025/10/22
# File: Nathania_Correlation_Analysis.py
# Apply correlation analysis to business problems 
#

# Data manipulation and analysis
import pandas as pd
import numpy as np
from scipy import stats
# import matplotlib.pyplot as plt
# import seaborn as sns

# 1. Input
# Read the CSV file
df = pd.read_csv('Correlation_Analysis_Data.csv')
# df.head()
# df.iloc[:,1]
# df.info()
# df.describe()
# print(df.iloc[:,1:6])
# Calculate correlation between Marketing Spend and Sales Revenue
# correlation, pvalue = stats.pearsonr(df['Marketing_Spend'], df['Sales_Revenue']
#  )

# 2. Process
# print(df.isnull().sum())
# print(df.isnull().sum().sum())
correlation_matrix = df.corr()
# correlation_matrix = df.iloc[:,1:6].corr()

# 3. Output
# print(df.head())
# print(df.iloc[:,1])
# print(df.info())
# print(df.describe())
# print('Data loaded successfully!')
# print(f'Dataset shape: {df.shape}')
# print(f'Correlation: {correlation}')
# print(f'P value: {pvalue}')
# print(f'Correlation: {correlation:.2f}')
# print(f'P value: {pvalue:.4e}')
# if pvalue < 0.05:
#     print ("The correlation is statistically significant!")
print(correlation_matrix.round(3))
# sns.heatmap(correlation_matrix)
# plt.tight_layout()
# plt.show()