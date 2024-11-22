# Initialize variables
batting_averages = []  # List to store the batting averages
NUM_BATTING_AVERAGES = 8  # Number of batting averages to be entered

# Input: Prompt the user to enter 8 batting averages
for i in range(NUM_BATTING_AVERAGES):
    while True:
        try:
            average = float(input(f"Enter a batting average: "))
            if 0 <= average <= 1:  # Validate that the average is between 0 and 1
                batting_averages.append(average)
                break
            else:
                print("Batting average must be between 0 and 1. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Output each batting average with its index
for i in range(len(batting_averages)):
    print(f"averages[{i}] is: {batting_averages[i]}")

# Process: Calculate the minimum, maximum, and average batting averages
min_average = min(batting_averages)
max_average = max(batting_averages)
average_of_averages = sum(batting_averages) / len(batting_averages)

# Output the results
print(f"Minimum batting average is {min_average}")
print(f"Maximum batting average is {max_average}")
print(f"Average batting average is {average_of_averages:.4f}")
