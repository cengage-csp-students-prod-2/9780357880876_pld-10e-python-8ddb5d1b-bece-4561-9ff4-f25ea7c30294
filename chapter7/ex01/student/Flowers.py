# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input
# file and prints the information to the user's screen.
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.

# Open input file.
input_file = open("flowers.dat", "r")

# Read record from file.
line = input_file.readline()

# Write while loop that reads records from file and test for EOF.
while line != "":  # While not end of file.
    # Split the line into flower name and condition.
    flower, condition = line.strip().split(",")  # Assuming comma-separated values.
    
    # Print flower name and the words sun or shade.
    print(f"{flower} is grown in the {condition}")

    # Read the next record from the file.
    line = input_file.readline()

# Close the file.
input_file.close()
