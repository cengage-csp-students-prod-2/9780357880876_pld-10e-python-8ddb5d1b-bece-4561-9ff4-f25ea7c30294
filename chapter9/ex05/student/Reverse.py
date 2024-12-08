# Reverse.py - This program reverses numbers stored in a list.
# Input: Interactive.
# Output: Original contents of list and the reversed contents of the list.

def main():
    # Initialize the list with five numbers
    numbers = [9, 8, 7, 6, 5]

    # Print contents of the original list
    print("Original contents of list:")
    for number in numbers:
        print(number)

    # Call reverseList function to reverse the list
    reverseList(numbers)

    # Print contents of the reversed list
    print("Reversed contents of list:")
    for number in numbers:
        print(number)

# End of main() function.

# Define the reverseList function
def reverseList(lst):
    """
    Reverses the order of elements in the provided list.
    This modifies the list in place.
    """
    lst.reverse()  # Reverse the list in place

# End of reverseList function.

if __name__ == '__main__':
    # Call the main function to run the program
    main()