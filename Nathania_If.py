#
# Nathania, 2025/10/15
# File: Nathania_If.py
# Short description of the task
#

# 1. Input
#print numbers from 1 to 5

# 2. Process
print("Output:", end=" ")
for i in range (1, 6):
    if i < 5:
        print (f"count: {i}", ends=", ")
    else:
        print(f"count:{i}")

# 3. Output

-- if example 1 -- 
# 1. Input
sales = 15000
target = 10000

# 2. Process
if sales > target:
    print ("Congratulations! Sales target achieved!")
    bonus = sales * 0.05
    print (f"Bonus earned: ${bonus}")

# 3. Output

-- if else example 1 -- 
# 1. Input
age = 16 

# 2. Process
if age >= 18:
    print ("You are eligible to vote")
else:
    print ("You are not eligible to vote yet")

# 3. Output

-- if else example 2 --
# 1. Input
account_balance = 5000
withdrawal = 6000

# 2. Process
if withdrawal <= account_balance:
    account_balance -= withdrawal
    print (f"Withdrawal successful. New balance: ${account_balance}")
else:
    print ("Insufficient funds!")

# 3. Output

-- if elif else example -- 
# 1. Input
score = 85

# 2. Process
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print (f"score: {score}, Grade: {grade}")

# 3. Output

-- if elif else example 2 --
# 1. Input
purchase_amount = 1500

# 2. Process
if purchase_amount >= 5000:
    tier = "Platinum"
    discount = 0.20
elif purchase_amount >= 2000:
    tier = "Gold"
    discount = 0.15
elif purchase_amount >= 1000:
    tier = "Silver"
    discount = 0.10 
else:
    tier = "Bronze"
    discount = 0.05

print (f"Customer Tier: {tier}, Discount: {discount*100}%")

# 3. Output

