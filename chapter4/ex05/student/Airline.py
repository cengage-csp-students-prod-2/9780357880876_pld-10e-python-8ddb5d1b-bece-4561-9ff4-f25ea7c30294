# Input: Get customer's name and age
name = input("Customer Name: ")
age = int(input("Customer Age: "))

# Decision statement: Check if eligible for discount
if age <= 6 or age >= 65:
    print(f"Passenger {name} is eligible for a discount.")
else:
    print(f"Passenger {name} is not eligible for a discount.")
