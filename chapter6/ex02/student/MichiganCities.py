# MichiganCities.py - This program prints a message for invalid cities in Michigan.
# Input:  Interactive.
# Output:  Error message or nothing.

# Initialized array of cities in Michigan.
citiesInMichigan = ["Acme", "Albion", "Detroit", "Watervliet", "Coloma", "Saginaw", "Richland", "Glenn", "Midland", "Brooklyn"]
foundIt = False  # Flag variable.

# Get user input.
# name of city to look up in array.
inCity = input("Enter name of city: ")

# Write your loop here.
for city in citiesInMichigan:
    # Write your test statement here to see if there is
    # a match. Set the flag to true if city is found.
    if city.lower() == inCity.lower():  # Case-insensitive comparison
        foundIt = True
        break  # Exit the loop since we found a match

# Test to see if city was not found to determine if
# "Not a city in Michigan." message should be printed.
if foundIt:
    print("City found.")
else:
    print("Not a city in Michigan.")
