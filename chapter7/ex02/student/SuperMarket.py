# SuperMarket.py - This program creates a report that lists weekly hours worked
# by employees of a supermarket. The report lists total hours for
# each day of one week.
# Input:  Interactive
# Output: Report.

# Initialize variables.
HEAD1 = "WEEKLY HOURS WORKED"
DAY_FOOTER = "              Previous Day Total"  # Leading spaces are intentional.
SENTINEL = "done"  # sentinel value.
hoursTotal = 0  # Total hours worked across all days.
dailyTotal = 0  # Hours total for a specific day.
done = False  # loop control

# Print one blank line.
print()

# Print heading.
print(HEAD1)

# Print two blank lines.
print()
print()

# Read the first record
dayOfWeek = input("Enter day of week or done to quit: ").capitalize()

if dayOfWeek == SENTINEL:
    done = True
else:
    hoursWorkedString = input("Enter hours worked: ")
    hoursWorked = int(hoursWorkedString)
    prevDay = dayOfWeek
    dailyTotal = hoursWorked  # Set the initial total for the first day

# Main loop to process each day's input
while not done:
    # Prompt for the next day and hours worked
    dayOfWeek = input("Enter day of week or done to quit: ").capitalize()

    if dayOfWeek == SENTINEL:
        done = True
        # Display the last day's total before ending
        print(f"{DAY_FOOTER}: {dailyTotal}")
        hoursTotal += dailyTotal
    else:
        hoursWorkedString = input("Enter hours worked: ")
        hoursWorked = int(hoursWorkedString)

        # Control break: Check if the day has changed
        if dayOfWeek != prevDay:
            # Display the total hours for the previous day
            print(f"{DAY_FOOTER}: {dailyTotal}")
            hoursTotal += dailyTotal  # Add to overall total

            # Reset for the new day
            prevDay = dayOfWeek
            dailyTotal = hoursWorked  # Start new total for this day
        else:
            # If the same day, add to the current daily total
            dailyTotal += hoursWorked

        # Display the current entry for this day
        print(f"{dayOfWeek}: {hoursWorked}")

# After exiting the loop, display the grand total
print(f"Total hours worked by all employees for the week: {hoursTotal}")
