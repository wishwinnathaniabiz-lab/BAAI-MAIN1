#
# Nathania, 2025/09/24
# File: 0_template.py
# Short description of the task
#

import pandas as pd

# 1. Input
df = pd.read_excel('Financial_Sample.xlsx')

# 2. Process
sum = df['Units Sold'].sum()

# 3. Output
print(f'Sum {sum}')