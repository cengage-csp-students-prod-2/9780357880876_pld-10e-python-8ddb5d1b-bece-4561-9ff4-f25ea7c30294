# LetterE.py - This program prints the letter E with 3 asterisks
# across and 5 asterisks down.
# Input:  None.
# Output: Prints the letter E.

num_across = 3  # Number of asterisks to print across.
num_down = 5    # Number of asterisks to print down.

# Loop through each row
for i in range(num_down):
    # Loop through each column
    for j in range(num_across):
        # Print an asterisk in the first column
        if j == 0:
            print("*", end="")
        # Print asterisks in the first, third, and last rows
        elif (i == 0 or i == 2 or i == 4) and j < num_across:
            print("*", end="")
        # Print a space in the middle column for second and fourth rows
        elif (i == 1 or i == 3) and j == 1:
            print(" ", end="")
        # Print an asterisk in the last column for the second and fourth rows
        elif (i == 1 or i == 3) and j == 2:
            print(" ", end="")
        else:
            print(" ", end="")  # Print space for any other case

    print()  # Move to the next line after finishing a row
