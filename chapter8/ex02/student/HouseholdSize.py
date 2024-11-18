# HouseholdSize.py - This program uses a bubble sort to arrange up to 300 household sizes in
# descending order and then prints the mean and median household size.
# Input: Interactive.
# Output: Mean and median household size.

# Initialize variables.
SIZE = 300  # Maximum number of household sizes.
householdSizes = []  # List used to store up to 300 household sizes.
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
    householdSizes.append(householdSize)

    # Calculate total of household sizes
    total += householdSize

    # Get ready for next input item.
    x += 1
    householdSizeString = input("Enter household size or 999 to quit: ")
    householdSize = int(householdSizeString)
# End of input loop.

# New size of households
size = len(householdSizes)

# Find the mean
if size > 0:
    mean = total / size

# This is the work done in the sortList() method
# Bubble sort in descending order
for i in range(size):
    for j in range(0, size - i - 1):
        if householdSizes[j] < householdSizes[j + 1]:
            # Swap elements
            householdSizes[j], householdSizes[j + 1] = householdSizes[j + 1], householdSizes[j]

# Calculate the median depending on size of list
if size > 0:
    if size % 2 == 0:  # Even number of elements
        median = (householdSizes[size // 2 - 1] + householdSizes[size // 2]) / 2
    else:  # Odd number of elements
        median = householdSizes[size // 2]

# This is the work done in the displayList() method
# Print the results
print(f"Mean household size in Marengo is: {mean}")
print(f"Median household size in Marengo is: {median}")