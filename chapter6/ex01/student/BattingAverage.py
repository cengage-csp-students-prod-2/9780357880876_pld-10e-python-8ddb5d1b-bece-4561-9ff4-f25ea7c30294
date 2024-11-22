# Initialize an integer for list size here.
list_size = 8

# Initialize list here.
averages = []

# Write a loop to get batting averages from user and add to list.
for i in range(list_size):
    # String version of batting average input by user.
    averageString = input("Enter a batting average: ")

    # Use this variable to store the batting average input by user.
    battingAverage = float(averageString)

    # Add value to list.
    averages.append(battingAverage)

# Use these variables to store the minimum and maximum batting averages.
# Assign the first element in the list to be the minimum and the maximum.
min = averages[0]
max = averages[0]

# Start out your total initialized to 0.
total = 0

# Write a loop here to access list values starting with averages[1]
for value in averages:
    # Within the loop test for minimum and maximum batting averages.
    if value < min:
        min = value
    if value > max:
        max = value

    # Also accumulate a total of all batting averages.
    total += value

# Calculate the average of the 8 averages.
average_of_averages = total / list_size

# Print the averages stored in the averages list.
for i in range(len(averages)):
    print(f"averages[{i}] is: {averages[i]}")

# Print the maximum batting average, minimum batting average, and average batting average.
print("Results:")
print(f"Minimum batting average: {min}")
print(f"Maximum batting average: {max}")
print(f"Average batting average: {average_of_averages:.4f}")
