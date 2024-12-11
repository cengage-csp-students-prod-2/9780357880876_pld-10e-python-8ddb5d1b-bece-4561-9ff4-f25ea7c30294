# Reverse.py - This program reverses numbers stored in a list.
# Input: User input for list of numbers.
# Output: Original contents of list and the reversed contents of the list.

def main():
    # Prompt the user to enter five numbers separated by spaces
    user_input = input("Enter five numbers separated by spaces: ")

    # Convert the input string to a list of integers
    numbers = [int(num) for num in user_input.split()]

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

    # Pause the program to keep the terminal open
    input("Press Enter to exit...")

# Define the reverseList function
def reverseList(lst):
    """
    Reverses the order of elements in the provided list.
    This modifies the list in place.
    """
    lst.reverse()  # Reverse the list in place

# Call the main function to run the program
if __name__ == '__main__':
    main()
