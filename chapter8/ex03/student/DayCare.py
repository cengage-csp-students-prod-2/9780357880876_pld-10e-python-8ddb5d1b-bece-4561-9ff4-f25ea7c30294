# DayCareRate.py - This program calculates the weekly rate for Building Block Day Care Center.
# Input: Interactive.
# Output: Weekly rate.

# Initialize two-dimensional array here.
rates = [
    [30.00, 60.00, 88.00, 115.00, 140.00],  # 0 years
    [26.00, 52.00, 70.00, 96.00, 120.00],  # 1 year
    [24.00, 46.00, 67.00, 89.00, 110.00],  # 2 years
    [22.00, 40.00, 60.00, 75.00, 88.00],   # 3 years
    [20.00, 35.00, 50.00, 66.00, 84.00]    # 4+ years
]

# Initialize variable to quit.
QUIT = 99

# This is the work done in the getReady() function
# Perform a priming read to get the age of the child.
age = int(input("Enter the age of the child or 99 to quit: "))

while age != QUIT:

    # This is the work done in the determineRateCharge() function
    # Ask the user to enter the number of days
    days = int(input("Enter number of days: "))

    if 1 <= days <= 5:  # Valid number of days
        # Determine the appropriate row for the age group.
        if age >= 4:
            age_row = 4
        else:
            age_row = age

        # Determine the appropriate column for the number of days.
        day_col = days - 1

        # Retrieve the weekly charge from the rates table.
        weekly_rate = rates[age_row][day_col]

        # Print the weekly rate
        print(f"Weekly charge is ${weekly_rate:.2f}")
    else:
        print("Invalid number of days. Please enter a value between 1 and 5.")

    # Ask the user to enter the next child's age
    age = int(input("Enter the age of the child or 99 to quit: "))

# This is the work done in the finish() function
print("End of program")