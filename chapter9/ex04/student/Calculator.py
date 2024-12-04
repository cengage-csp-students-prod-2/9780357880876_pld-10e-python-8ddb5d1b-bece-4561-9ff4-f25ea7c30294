# Calculator.py - This program performs arithmetic (+, -, *, /, %) on two numbers
# Input:  Interactive.
# Output:  Result of arithmetic operation

def main():
    numberOneString = input("Enter the first number: ")
    numberOne = float(numberOneString)
    numberTwoString = input("Enter the second number: ")
    numberTwo = float(numberTwoString)
    operation = input("Enter an operator (+, -, *, /, %): ")

    # Call performOperation function here
    result = performOperation(numberOne, numberTwo, operation)

    print(f"{numberOne:.2f}")
    print(" " + operation + " ")
    print(f"{numberTwo:.2f}")
    print(" = ")
    print(f"{result:.2f}")

# End of main() function.

# Write performOperation function here.
def performOperation(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    elif op == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
# End of performOperation function

if __name__ == '__main__':
    # Call the main function to run the program
    main()