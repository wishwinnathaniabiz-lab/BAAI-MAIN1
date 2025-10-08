#
# Nathania, 2025/09/24
# File: 0_template.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_excel('Financial_Sample.xlsx')

# 2. Process
sums = df.select_dtypes(include='number').sum()

# Optionally give a label for the row (e.g., 'Total')
sums['Name'] = 'Total' # Add a value for the non-numeric column

# Append the total row to the DataFrama
df_with_total = pd.concat([df, pd.DataFrame([sums])], ignore_index=True)

# 3. Output
print(df_with_total)
df_with_total.to_excel('result_with_total.xlsx', index=False)