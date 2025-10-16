#
# Nathania, 2025/10/15
# File: Nathania_If.py
# Short description of the task
#

# 1. Input
fruits = ["apple", "banana", "orange", "mango"]

# 2. Process
for fruit in fruits:
    print (f"I like {fruit}")

# 3. Output

-- for range example --
# 1. Input

# 2. Process
for i in range (1,6):
    print(f"Count: {i}")

# 3. Output

-- for example 
# 1. Input
order_values = [120,450,80,300,650]
total_revenue = 0

# 2. Process
for order in order_values:
    total_revenue += order
    print(f"Processing order: ${order}")

print(f"\nTotal Revenue: ${total_revenue}")

# 3. Output
