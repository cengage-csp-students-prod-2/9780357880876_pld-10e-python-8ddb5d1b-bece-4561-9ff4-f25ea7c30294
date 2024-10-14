salary = 1250.00
numDependents = 2

# Calculate state tax here
stateTax = 0.05 * salary

print(f"State Tax: ${stateTax:.2f}")

# Calculate federal tax here
federalTax = 0.10 * salary

print(f"Federal Tax: ${federalTax:.2f}")

# Calculate dependent deduction here
dependentDeduction = 100 * numDependents

print(f"Dependents Deduction: ${dependentDeduction:.2f}")
