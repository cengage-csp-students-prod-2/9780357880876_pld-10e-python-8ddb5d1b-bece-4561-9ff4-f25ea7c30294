# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input
# file and prints the information to the user's screen.
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.

# Open input file using with...open...as.
with open("flowers.dat", "r") as input_file:
    # Read record from file.
    line = input_file.readline()
    
    # Write while loop that reads records from file and test for EOF.
    while line != "":  # While not end of file.
        # Strip whitespace and check for valid format.
        line = line.strip()
        if "," in line:  # Ensure line contains a comma.
            flower, condition = line.split(",", 1)  # Split into two parts only.
            # Print flower name and the words sun or shade.
            print(f"{flower} is grown in the {condition}")
        else:
            print(f"Invalid line format: {line}")  # Handle improperly formatted lines.

        # Read the next record from the file.
        line = input_file.readline()
