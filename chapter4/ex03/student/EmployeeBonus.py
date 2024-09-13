# EmployeeBonus.py - This program calculates an employee's productivity bonus.

# initialize variables here.
bonus_1 = 50.00
bonus_2 = 75.00
bonus_3 = 100.00
bonus_4 = 200.00

employee_name = input("Enter employee's name: ")
shift_string = input("Enter number of shifts: ")
transact_string = input("Enter number of transactions: ")
dollar_string = input("Enter transactions dollar value: ")

num_shifts = float(shift_string)
num_transactions = float(transact_string)
dollar_value = float(dollar_string)

# Write your code here

# Output.
print("Employee Name:", employee_name)
print(f"Employee Bonus: ${bonus:.2f}")