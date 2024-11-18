# Swap.py - This program determines the minimum and maximum of three values input by
# the user and performs necessary swaps.
# Input:  Three int values.
# Output:  The numbers in numerical order.

# Initialize variables.
first = 0
second = 0
third = 0

# Get user input.
firstNumber = input("Enter first number: ")
if firstNumber != "":
    secondNumber = input("Enter second number: ")
    thirdNumber = input("Enter third number: ")

    # Convert strings to int.
    first = int(firstNumber)
    second = int(secondNumber)
    third = int(thirdNumber)

    # Test to see if the first number is greater than the second number.
    if first > second:
        first, second = second, first  # Swap values

    # Test to see if the second number is greater than the third number.
    if second > third:
        second, third = third, second  # Swap values

    # Test to see if the first number is greater than the second number again.
    if first > second:
        first, second = second, first  # Swap values

# Print values in numerical order.
print("Smallest:", first)
print("Next largest:", second)
print("Largest:", third)