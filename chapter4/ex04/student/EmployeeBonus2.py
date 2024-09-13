# EmployeeBonus2.py - This program calculates an employee's yearly bonus.

# initialize variables.
bonus_1 = .25
bonus_2 = .15
bonus_3 = .10
no_bonus = 0.00

# Get user input.
employee_name = input("Enter employee's name: ")
salary_string = input("Enter employee's yearly salary: ")
rating_string = input("Enter employee's performance rating: ")

# Convert Strings to int or double.
employee_salary = float(salary_string)
employee_rating = int(rating_string)

# Use match statement here to calculate bonus based on rating.

# Output.
print("Employee Name: ", employee_name)
print(f"Employee Salary: ${employee_salary:.2f}")
print("Employee Rating: ", employee_rating)
print(f"Employee Bonus: ${employee_bonus:.2f}")