# Number of rows and columns for the letter E
rows = 5
columns = 3

# Loop through each row
for i in range(rows):
    # Loop through each column
    for j in range(columns):
        # Use nested if statements to determine when to print an asterisk
        if j == 0:  # First column
            print("*", end="")  # Always print an asterisk
        elif i == 0 or i == 2 or i == 4:  # First, third, and last rows
            if j < columns:  # Print asterisk in the top, middle, and bottom rows
                print("*", end="")
            else:
                print(" ", end="")  # Not needed, as j will not be greater than 2
        else:  # Second and fourth rows
            if j == 2:  # Only print an asterisk in the last column for second and fourth rows
                print("*", end="")
            else:
                print(" ", end="")  # Print space for the middle column

    print()  # Move to the next line after finishing a row
    