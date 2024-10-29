# SuperMarket.py - This program creates a report that lists weekly hours worked
# by employees of a supermarket. The report lists total hours for
# each day of one week.
# Input:  Interactive
# Output: Report.

# Initialize variables.
HEAD1 = "WEEKLY HOURS WORKED"
DAY_FOOTER = "              Previous Day Total"  # Leading spaces are intentional.
SENTINEL = "done"  # Sentinel value to quit.
hoursTotal = 0  # Total hours worked across all days.
dailyTotal = 0  # Hours total for a specific day.
done = False  # Loop control variable

# Print heading.
print("\n" + HEAD1 + "\n\n")

# Try to read the first record
try:
    dayOfWeek = input("Enter day of week or done to quit: ").capitalize()
except EOFError:
    print("\nEnd of input detected. Exiting program.")
    dayOfWeek = SENTINEL
    done = True

if dayOfWeek == SENTINEL:
    done = True
else:
    try:
        hoursWorkedString = input("Enter hours worked: ")
        hoursWorked = int(hoursWorkedString)
        prevDay = dayOfWeek
        dailyTotal = hoursWorked  # Set initial total for the first day
    except EOFError:
        print("\nEnd of input detected. Exiting program.")
        done = True

# Main loop to process each day's input
while not done:
    try:
        dayOfWeek = input("Enter day of week or done to quit: ").capitalize()
    except EOFError:
        print("\nEnd of input detected. Exiting program.")
        dayOfWeek = SENTINEL

    if dayOfWeek == SENTINEL:
        done = True
        print(f"{DAY_FOOTER}: {dailyTotal}")
        hoursTotal += dailyTotal
    else:
        try:
            hoursWorkedString = input("Enter hours worked: ")
            hoursWorked = int(hoursWorkedString)
        except EOFError:
            print("\nEnd of input detected. Exiting program.")
            break

        if dayOfWeek != prevDay:
            print(f"{DAY_FOOTER}: {dailyTotal}")
            hoursTotal += dailyTotal
            prevDay = dayOfWeek
            dailyTotal = hoursWorked
        else:
            dailyTotal += hoursWorked

        print(f"{dayOfWeek}: {hoursWorked}")

# Display the grand total
print(f"Total hours worked by all employees for the week: {hoursTotal}")
