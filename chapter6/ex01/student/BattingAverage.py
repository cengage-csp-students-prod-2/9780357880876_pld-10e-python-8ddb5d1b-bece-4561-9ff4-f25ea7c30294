# Initialize an integer for list size here.
size = 8

# Initialize list here.
averages = [0] * size

# Write a loop to get batting averages from user and add to list.
for i in range(size):
    # String version of batting average input by user.
    averageString = input("Enter a batting average: ")
    
    # Use this variable to store the batting average input by user.
    battingAverage = float(averageString)
    
    # Add value to list.
    averages[i] = battingAverage

# Use these variables to store the minimum and maximum batting averages.
# Assign the first element in the list to be the minimum and the maximum.
min_average = averages[0]
max_average = averages[0]

# Start out your total initialized to 0.
total = 0

# Write a loop here to access list values starting with averages[1]
for i in range(1, size):
    # Within the loop, test for minimum and maximum batting averages.
    if averages[i] < min_average:
        min_average = averages[i]
    if averages[i] > max_average:
        max_average = averages[i]
    
    # Also accumulate a total of all batting averages.
    total += averages[i]

# Calculate the average of the 8 averages.
average_of_averages = total / size

# Print the averages stored in the averages list.
for i in range(size):
    print(f"averages[{i}] is: {averages[i]}")

# Print the maximum batting average, minimum batting average, and average batting average.
print(f"Minimum batting average is {min_average}")
print(f"Maximum batting average is {max_average}")
print(f"Average batting average is {average_of_averages}")
