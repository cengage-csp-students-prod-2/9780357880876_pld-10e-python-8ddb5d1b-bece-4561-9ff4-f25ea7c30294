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
min_average = averages[0]
max_average = averages[0]

# Start out your total initialized to 0.
total = 0

# Write a loop here to access list values starting with averages[1]
for average in averages:
    # Accumulate a total of all batting averages.
    total += average

    # Within the loop, test for minimum and maximum batting averages.
    if average < min_average:
        min_average = average
    if average > max_average:
        max_average = average

# Calculate the average of the 8 averages.
average_of_averages = total / list_size

# Print the averages stored in the averages list.
for index in range(len(averages)):
    print(f"averages[{index}] is: {averages[index]}")

# Print the minimum batting average, maximum batting average, and average batting average.
# Ensure the output matches the expected format.
print(f"[minimum batting average is {min_average:.3f}]")
print(f"[maximum batting average is {max_average:.3f}]")
print(f"[average batting average is {average_of_averages:.4f}]")
