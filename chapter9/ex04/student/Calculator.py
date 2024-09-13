# Calculator.py - This program performs arithmetic, ( +. -, *. /, % ) on two numbers
# Input:  Interactive.
# Output:  Result of arithmetic operation

def main():

    numberOneString = input("Enter the first number: ")
    numberOne = float(numberOneString)
    numberTwoString = input("Enter the second number: ")
    numberTwo = float(numberTwoString)
    operation = input("Enter an operator (+.-.*,/,%): ")

    # Call performOperation function here


    print(f"{numberOne:.2f}")
    print(" " + operation + " ")
    format(f"{numberTwo:.2f}")
    print(" = ")
    format(f"{result:.2f}")
# End of main() function.

# Write performOperation function here.

# End of performOperation function

if __name__ == '__main__':
# Call the main function to run program