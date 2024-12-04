# Reverse.py - This program reverses numbers stored in a list.
# Input:  Interactive.
# Output:  Original contents of list and the reversed contents of the list.

def main():
    numbers = [9, 8, 7, 6, 5]

    # Print contents of the original list
    print("Original contents of list:")
    for number in numbers:
        print(number)

    # Call reverseList function
    reverseList(numbers)

    # Print contents of the reversed list
    print("Reversed contents of list:")
    for number in numbers:
        print(number)

# End of main() function.

# Write reverseList function here
def reverseList(lst):
    """Reverses the order of the elements in the provided list."""
    lst.reverse()

# End of reverseList function.

if __name__ == '__main__':
    # Call the main function to run the program
    main()
