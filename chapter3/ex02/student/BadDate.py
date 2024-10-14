def housekeeping():
    # Retrieve year, month, and day from the user
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    return year, month, day

def endOfJob(month, day, year, is_valid):
    # Output whether the date is valid or invalid
    if is_valid:
        print(f"{month}/{day}/{year} is a valid date.")
    else:
        print(f"{month}/{day}/{year} is an invalid date.")

def is_valid_date(year, month, day):
    # Check if the year, month, and day are valid
    if year <= 0:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    # Additional validation for specific months
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        # Check for leap years for February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True

# Main program execution
year, month, day = housekeeping()
valid = is_valid_date(year, month, day)
endOfJob(month, day, year, valid)
