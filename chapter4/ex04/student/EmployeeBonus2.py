# Pre-written input statements
employee_name = input("Enter the employee's name: ")
employee_salary = float(input("Enter the employee's yearly salary: "))
performance_rating = int(input("Enter the employee's performance rating (1-4): "))

# Initialize bonus percentage
bonus_percentage = 0.0

# Task 1: Use match statement to determine bonus percentage
match performance_rating:
    case 1:
        bonus_percentage = 0.25
    case 2:
        bonus_percentage = 0.15
    case 3:
        bonus_percentage = 0.10
    case 4:
        bonus_percentage = 0.0
    case _:
        print("Invalid performance rating entered.")

# Calculate the bonus
employee_bonus = employee_salary * bonus_percentage

# Output the results
print(f"\nEmployee Name: {employee_name}")
print(f"Employee Salary: ${employee_salary:.2f}")
print(f"Employee Rating: {performance_rating}")
print(f"Employee Bonus: ${employee_bonus:.2f}")
