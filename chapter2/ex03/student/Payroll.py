# Declare and initialize the variables
salary = 1250.00  # Salary in dollars
numDependents = 2  # Number of dependents
stateTax = 0.0  # State tax initialized to 0
federalTax = 0.0  # Federal tax initialized to 0
dependentDeduction = 0.0  # Dependent deduction initialized to 0
totalWithholding = 0.0  # Total withholding initialized to 0
takeHomePay = 0.0  # Take-home pay initialized to 0

# Calculate the state withholding tax
stateTax = salary * 0.065  # 6.5% state tax
print(f"State Tax: ${stateTax:.2f}")

# Calculate the federal withholding tax
federalTax = salary * 0.28  # 28% federal tax
print(f"Federal Tax: ${federalTax:.2f}")

# Calculate the dependent deductions
dependentDeduction = salary * 0.025 * numDependents  # 2.5% deduction per dependent
print(f"Dependent Deduction: ${dependentDeduction:.2f}")

# Calculate the total withholding
totalWithholding = stateTax + federalTax + dependentDeduction
print(f"Total Withholding: ${totalWithholding:.2f}")

# Calculate the take-home pay
takeHomePay = salary - totalWithholding
print(f"Salary: ${salary:.2f}")
print(f"Take-Home Pay: ${takeHomePay:.2f}")
