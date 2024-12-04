# SumAndProduct.py - This program computes sums and products.
# Input:  Interactive.
# Output:  Computed sum and product.

def main():
    numberString = input("Enter a positive integer or 0 to quit: ")
    number = int(numberString)

    while number != 0:
        sums(number)  # Call sums() function
        products(number)  # Call products() function

        numberString = input("Enter a positive integer or 0 to quit: ")
        number = int(numberString)
# End of main() function.

# Define the sums() function.
def sums(number):
    total = sum(range(1, number + 1))  # Compute the sum of whole numbers from 1 to 'number'
    print(f"The sum is {total}.")  # Display the result

# Define the products() function.
def products(number):
    product = 1
    for i in range(1, number + 1):  # Compute the product of whole numbers from 1 to 'number'
        product *= i
    print(f"The product is {product}.")  # Display the result

# Ensure the program runs when executed
if __name__ == '__main__':
    main()