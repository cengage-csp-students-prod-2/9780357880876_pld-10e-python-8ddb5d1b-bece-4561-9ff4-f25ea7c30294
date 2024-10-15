# Task 1: Initialize variables
charge = 35.00       # Base charge for any sign
num_chars = 8        # Number of characters on the sign
color = "gold"       # Color of the characters
wood_type = "oak"    # Type of wood

# Task 2: Add charges based on the conditions
# Charge for additional characters (first 5 are free)
if num_chars > 5:
    charge += (num_chars - 5) * 4.00

# Add charge for oak wood
if wood_type == "oak":
    charge += 20.00

# Add charge for gold-leaf lettering
if color == "gold":
    charge += 15.00

# Output the total charge for the sign
print(f"The charge for this sign is ${charge:.2f}")
