# SuperMarket.py - This program creates a report that lists weekly hours worked
# by employees of a supermarket. The report lists total hours for
# each day of one week.
# Input:  Interactive
# Output: Report.

# Initialize variables.
HEAD1 = "WEEKLY HOURS WORKED"
DAY_FOOTER = "              Previous Day Total"  # Leading spaces are intentional.
SENTINEL = "done"  # sentinel value.
hoursTotal = 0  # Weekly hours total
dailyTotal = 0  # Hours total for the current day
done = False  # loop control

# Print one blank line.
print()

# Print heading.
print(HEAD1)

# Print two blank lines.
print()
print()

# Read first record
dayOfWeek = input("Enter day of week or done to quit: ")

if dayOfWeek == SENTINEL:
    done = True
else:
    hoursWorkedString = input("Enter hours worked: ")
    hoursWorked = int(hoursWorkedString)
    prevDay = dayOfWeek
    dailyTotal = hoursWorked  # Set initial total for the first day

while not done:
    # Prompt for the next day of the week
    dayOfWeek = input("Enter day of week or done to quit: ")

    if dayOfWeek == SENTINEL:
        done = True
        # Final display of the previous day's total when quitting
        print(f"{DAY_FOOTER}: {dailyTotal}")
        hoursTotal += dailyTotal  # Add last day's total to weekly total
    else:
        hoursWorkedString = input("Enter hours worked: ")
        hoursWorked = int(hoursWorkedString)

        # Implement control break: check if the day has changed
        if dayOfWeek != prevDay:
            # Display the total hours for the previous day
            print(f"{DAY_FOOTER}: {dailyTotal}")
            hoursTotal += dailyTotal  # Add to weekly total

            # Reset for the new day
            prevDay = dayOfWeek
            dailyTotal = hoursWorked  # Start new total for this day
        else:
            # If the same day, add to the current daily total
            dailyTotal += hoursWorked

        # Display the current entry for this day
        print(f"{dayOfWeek}: {hoursWorked}")

# Display the grand total after the loop ends
print(f"\nTotal hours worked by all employees for the week: {hoursTotal}")
