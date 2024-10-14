# This program calculates an employee's take home pay.

salary = 1250.00
numDependents = 2

# Calculate state tax here
stateTax = 0.05 * salary  # 5% state tax
print(f"State Tax: ${stateTax:.2f}")

# Calculate federal tax here
federalTax = 0.10 * salary  # 10% federal tax
print(f"Federal Tax: ${federalTax:.2f}")

# Calculate dependent deduction here
dependentDeduction = 100 * numDependents  # $100 per dependent
print(f"Dependents Deduction: ${dependentDeduction:.2f}")

# Calculate take-home pay here
takeHomePay = salary - stateTax - federalTax + dependentDeduction

# Output the final results
print(f"Salary: ${salary:.2f}")
print(f"Take-Home Pay: ${takeHomePay:.2f}")
