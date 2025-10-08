#
# Nathania, 2025/09/24
# File: 0_template.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_excel('Financial_Sample.xlsx')

# 2. Process
Sum = df.sum(numeric_only=True)
Sum[df.columns[0]] = 'Total'
df_with_total = pd.concat([df, pd.DataFrame([Sum])], ignore_index=True)

# 3. Output
print(df_with_total)

# 4. Save to Excel
df_with_total.to_excel('result_with_total.xlsx', index=False)