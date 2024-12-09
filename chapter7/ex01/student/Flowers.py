# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input
# file and prints the information to the user's screen.
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.

# Open input file using with...open...as.
with open("flowers.dat", "r") as input_file:
    # Read the first line (flower name).
    flower = input_file.readline().strip()
    
    # Write while loop that reads records from file and test for EOF.
    while flower != "":  # While not end of file.
        # Read the next line (condition: Sun or Shade).
        condition = input_file.readline().strip()
        
        # Print flower name and the words sun or shade.
        print(f"{flower} is grown in the {condition}")
        
        # Read the next flower name.
        flower = input_file.readline().strip()