# JumpinJive.py - This program looks up and prints the names and prices of coffee orders.
# Input:  Interactive.
# Output:  Name and price of coffee orders or error message if add-in is not found.

# Initialize variables.
NUM_ITEMS = 5

# Initialized list of add-ins.
addIns = ["Cream", "Cinnamon", "Chocolate", "Amaretto", "Whiskey"]

# Initialized list of add-in prices.
addInPrices = [0.89, 0.25, 0.59, 1.50, 1.75]
orderTotal = 2.00  # All orders start with a 2.00 charge

# Get user input.
addIn = input("Enter coffee add-in or XXX to quit: ")

# Task 1: Write the code that searches the list for the name of the add-in ordered by the customer.
while addIn != "XXX":
    found = False  # Initialize a flag to check if the add-in is found

    for i in range(NUM_ITEMS):
        if addIn.lower() == addIns[i].lower():  # Case insensitive comparison
            print(f"{addIns[i]} price is ${addInPrices[i]:.2f}")
            orderTotal += addInPrices[i]  # Add the price to the total
            found = True  # Set the flag to True if the add-in is found
            break  # Exit the loop since we found the add-in

    # Task 2: Print the name and price of the add-in or the error message
    if not found:  # If the add-in was not found
        print("Sorry we do not carry that.")

    # Ask for the next add-in
    addIn = input("Enter coffee add-in or XXX to quit: ")

# Print the total order cost when user quits
print(f"Order Total is ${orderTotal:.2f}")
