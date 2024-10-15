# Task 1: Initialize the loop control variable
number = 0

print("0 through 10 multiplied by 2 and by 10.")

# Task 1: Write a counter-controlled while loop
while number <= 10:
    # Task 2: Multiply the value of the loop control variable
    multiplied_by_2 = number * 2
    multiplied_by_10 = number * 10
    
    # Display the results
    print(f"Number: {number}")
    print(f"Multiplied by 2: {multiplied_by_2}")
    print(f"Multiplied by 10: {multiplied_by_10}")
    
    # Change the value of the loop control variable
    number += 1  # Increment the variable to avoid an infinite loop