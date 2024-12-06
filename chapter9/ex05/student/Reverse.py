# Reverse.py - This program reverses numbers stored in a list.
# Input:  Interactive.
# Output:  Original contents of list and the reversed contents of the list.

def main():
    # Initialize the list
    numbers = [9, 8, 7, 6, 5]

    # Print contents of the original list
    print("Original contents of list:")
    for number in numbers:
        print(number)

    # Call reverseList function here
    reverseList(numbers)

    # Print contents of the reversed list
    print("\nReversed contents of list:")
    for number in numbers:
        print(number)

# End of main() function.


# Write reverseList function here.
def reverseList(numbers):
    # Reverse the list in place
    numbers.reverse()

# End of Reverse class.

if __name__ == '__main__':
    # Call the main function to run the program
    main()
