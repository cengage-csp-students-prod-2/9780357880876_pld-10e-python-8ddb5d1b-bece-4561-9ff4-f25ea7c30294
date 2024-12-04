# Computation.py - This program calculates sum, difference, and product of two values.
# Input:  Interactive.
# Output:  Sum, difference, and product of two values.

def main():
    value1String = input("Enter first numeric value: ")
    value1 = float(value1String)
    value2String = input("Enter second numeric value: ")
    value2 = float(value2String)

    # Call calculateSum() here
    calculateSum(value1, value2)

    # Call calculateDifference() here
    calculateDifference(value1, value2)

    # Call calculateProduct() here
    calculateProduct(value1, value2)

# End of main() function.

# Write calculateSum() function here.
def calculateSum(num1, num2):
    sum_result = num1 + num2
    print(f"Sum is: {sum_result}")

# Write calculateDifference() function here.
def calculateDifference(num1, num2):
    difference_result = num1 - num2
    print(f"Difference is: {difference_result}")

# Write calculateProduct() function here.
def calculateProduct(num1, num2):
    product_result = num1 * num2
    print(f"Product is: {product_result}")

if __name__ == '__main__':
    # Call the main function to run program
    main()