"""
Reverse.py - This program reverses numbers stored in an array.
Input: Interactive.
Output: Original contents of array and the reversed contents of the array.
"""

# Write reverseArray function here.
def reverseArray(numbers):
    # Reverse the array in place
    numbers.reverse()

# Array of numbers
numbers = [9, 8, 7, 6, 5]

# Print contents of the original list.
print("Original contents of list:")
for number in numbers:
    print(number)

# Call reverseArray function here.
reverseArray(numbers)

# Print contents of the reversed list.
print("\nReversed contents of list:")
for number in numbers:
    print(number)
