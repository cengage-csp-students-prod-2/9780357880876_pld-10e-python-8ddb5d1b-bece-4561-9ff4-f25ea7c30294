# This program calculates an employee's take home pay.


salary = 1250.00
numDependents = 2
def calculate_withholding_tax(salary):
    state_tax_rate = 0.065  # 6.5% state tax
    federal_tax_rate = 0.28  # 28% federal tax
    
    state_tax = salary * state_tax_rate
    federal_tax = salary * federal_tax_rate
    return state_tax, federal_tax

print(f"State Tax: ${stateTax:.2f}")

def calculate_dependent_deductions(salary, dependents):
    dependent_deduction_rate = 0.025  # 2.5% deduction per dependent
    return salary * dependent_deduction_rate * dependents

print(f"Federal Tax: ${federalTax:.2f}")

def calculate_total_withholding(state_tax, federal_tax):
    return state_tax + federal_tax

print(f"Dependents: ${dependentDeduction:.2f}")

def calculate_take_home_pay(salary, total_withholding, dependent_deductions):
    return salary - total_withholding + dependent_deductions

print(f"Total withholding ${totalWithholding:.2f}")


# Main program
def main():
    # User inputs
    salary = float(input("Enter the employee's weekly salary: $"))
    dependents = int(input("Enter the number of dependents: "))

print(f"Salary: ${salary:.2f}")
print(f"Take-Home Pay: ${takeHomePay:.2f}")