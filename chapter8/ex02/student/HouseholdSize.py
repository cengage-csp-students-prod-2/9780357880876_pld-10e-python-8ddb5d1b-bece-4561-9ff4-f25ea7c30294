# HouseholdSize.py - This program uses a bubble sort to arrange up to 300 household sizes in
# descending order and then prints the mean and median household size.
# Input: Interactive.
# Output: Mean and median household size.

# Initialize variables.
SIZE = 300 # Maximum number of household sizes.
householdSizes = [] # List used to store up to 300 household sizes.
householdSize = 0
total = 0
mean = 0
median = 0

# Input household size
householdSizeString = input("Enter household size or 999 to quit: ")
householdSize = int(householdSizeString)

# This is the work done in the fillList() function
x = 0
while (x < SIZE) and (householdSize != 999):

    # Place value in list.
    householdSizes[x] = householdSize

    # Calculate total of household sizes


    # Get ready for next input item.
    x += 1

    householdSizeString = input("Enter household size or 999 to quit: ")
    householdSize = int(householdSizeString)
    # End of input loop.

# new size of households


# Find the mean


# This is the work done in the sortList() method
# Number of items to compare.

# Set flag to False.

# Outer loop controls number of passes over data.
# Test flag.

# This is the work done in the displayList() method


# Calculate the median depending on size of list
# Print the median