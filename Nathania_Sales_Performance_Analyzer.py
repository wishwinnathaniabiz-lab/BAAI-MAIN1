#
# Nathania, 2025/10/19
# File: Nathania_Sales_Analyzer.py
# Sales Performance Report
#

import pandas as pd

# 1. Input
# Read the excel file
df = pd.read_excel('sales_data.xlsx')

# For counting total bonus
total_bonus = 0

# 2. Process
def Achievement (row):
    if row["Monthly_Sales"] >= ["Sales_Target"]:
        target = ("MET")
        bonus = row["Monthly_Sales"] * 0.10
    else:
        target = ("NOT MET")
        bonus = row["Monthly_Sales"] * 0.05

    sales_performance.append({
        "name": row["Employee_Name"],
        "target": target,
        "sales": row["Monthly_Sales"],
        "bonus": bonus 
    })

# 3. Output
print("=== SALES PERFORMANCE REPORT ===\n")

print(f"{row["Employee_Name"]}: {status} | Sales: ${row["Monthly_Sales"]})


