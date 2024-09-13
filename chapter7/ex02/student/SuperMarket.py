# SuperMarket.py - This program creates a report that lists weekly hours worked
# by employees of a supermarket. The report lists total hours for
# each day of one week.
# Input:  Interactive
# Output: Report.

# Initialize variables.
HEAD1 = "WEEKLY HOURS WORKED"
DAY_FOOTER = "              Previous Day Total"  # Leading spaces are intentional.
SENTINEL = "done"  # sentinel value.
hoursTotal = 0  # Hours total for a day.
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

while not done:

    # Implement control break logic here
    # Include work done in the dayChange() method

print(f"{DAY_FOOTER}: {hoursTotal}")