#
# Nathania, 2025/10/22
# File: Nathania_Correlation_Analysis.py
# Apply correlation analysis to business problems 
#

# Data manipulation and analysis
import pandas as pd
from scipy import stats

# 1. Input
# Read the CSV file
df = pd.read_csv('Correlation_Analysis_Data.csv')

correlation, pvalue = stats.pearsonr(df['Marketing_Spend'], df['Sales_Revenue']
)

# 2. Process
# print(df.isnull().sum())
# print(df.isnull().sum().sum())

# 3. Output
# print('Data loaded successfully!')
# print(f'Dataset shape: {df.shape}')
# print(f'Correlation: {correlation}')
# print(f'P value: {pvalue}')
print(f'Correlation: {correlation:.2f}')
print(f'P value: {pvalue:.4e}')