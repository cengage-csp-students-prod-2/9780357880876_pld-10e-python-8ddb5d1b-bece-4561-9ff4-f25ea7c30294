class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers

    def reverselist(self):
        self.numbers.reverse()  # Reverse the list in place

    def display(self):
        for number in self.numbers:
            print(number)

# Example usage
if __name__ == "__main__":
    # Original list
    original_list = [9, 8, 7, 6, 5]
    
    print("Original contents of list:")
    num_list = NumberList(original_list)
    num_list.display()

    # Reverse the list
    num_list.reverselist()

    print("\nReversed contents of list:")
    num_list.display()
