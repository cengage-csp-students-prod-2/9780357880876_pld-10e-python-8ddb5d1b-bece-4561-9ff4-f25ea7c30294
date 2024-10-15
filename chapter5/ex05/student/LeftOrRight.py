# LeftOrRight.py - This program calculates the total number of left-handed and right-handed
# students in a class.
# Input:  L for left-handed; R for right-handed; X to quit.
# Output: Prints the number of left-handed students and the number of right-handed students.

rightTotal = 0  # Number of right-handed students.
leftTotal = 0   # Number of left-handed students.

# Start a loop that continues until the user enters 'X'
while True:
    leftOrRight = input("Enter L if you are left-handed, R if you are right-handed or X to quit: ").strip().upper()

    # Check the user input
    if leftOrRight == 'L':
        leftTotal += 1  # Increment left-handed counter
    elif leftOrRight == 'R':
        rightTotal += 1  # Increment right-handed counter
    elif leftOrRight == 'X':
        break  # Exit the loop if the user enters 'X'
    else:
        print("Invalid input. Please enter L, R, or X.")

# Output number of left or right-handed students.
print("Number of left-handed students:", leftTotal)
print("Number of right-handed students:", rightTotal)
