# Input statements (pre-written)
employee_name = input("Employee's first name: ")
num_shifts = int(input("Number of shifts: "))
num_transactions = int(input("Number of transactions: "))
transaction_value = float(input("Transaction dollar value: "))

# Task 1: Calculate productivity score
productivity_score = (transaction_value / num_transactions) / num_shifts

# Task 2: Determine the bonus using nested if statements
if productivity_score <= 30:
    bonus = 50
else:
    if productivity_score <= 69:
        bonus = 75
    else:
        if productivity_score <= 199:
            bonus = 100
        else:
            bonus = 200

# Output (pre-written)
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus}")
