# Declare and initialize the variables
salary = 1250.00  # Salary in dollars
numDependents = 2  # Number of dependents

# Calculate the state withholding tax
stateTax = salary * 0.065  # 6.5% state tax
print(f"State Tax: ${stateTax:.2f}")

# Calculate the federal withholding tax
federalTax = salary * 0.28  # 28% federal tax
print(f"Federal Tax: ${federalTax:.2f}")

# Calculate the dependent deductions
dependentDeduction = salary * 0.025 * numDependents  # 2.5% deduction per dependent
print(f"Dependents: ${dependentDeduction:.2f}")

# Calculate the total withholding (only taxes)
totalWithholding = stateTax + federalTax  # Only the taxes
print(f"Total Withholding: ${totalWithholding:.2f}")

# Calculate the take-home pay (adding back the dependent deduction)
takeHomePay = salary - totalWithholding + dependentDeduction
print(f"Salary: ${salary:.2f}")
print(f"Take-Home Pay: ${takeHomePay:.2f}")
