# Variables provided in the assignment
firstNumber = -50
secondNumber = 53
thirdNumber = 78

# Declaring variables for largest and smallest
largest = None
smallest = None

# Your logic starts here

# Find the largest number
if firstNumber >= secondNumber and firstNumber >= thirdNumber:
    largest = firstNumber
elif secondNumber >= firstNumber and secondNumber >= thirdNumber:
    largest = secondNumber
else:
    largest = thirdNumber

# Find the smallest number
if firstNumber <= secondNumber and firstNumber <= thirdNumber:
    smallest = firstNumber
elif secondNumber <= firstNumber and secondNumber <= thirdNumber:
    smallest = secondNumber
else:
    smallest = thirdNumber

# Output the results (this part is already provided)
print("The largest value is", largest)
print("The smallest value is", smallest)
