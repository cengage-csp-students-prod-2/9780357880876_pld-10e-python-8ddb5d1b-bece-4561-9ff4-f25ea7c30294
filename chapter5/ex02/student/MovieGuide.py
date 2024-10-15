# Variable declarations
total_rating = 0
count = 0

# Input from the user
rating = int(input("Enter rating for featured movie (0-4, -1 to quit): "))

# While loop using a sentinel value
while rating >= 0:  # Sentinel value is -1
    total_rating += rating  # Add the rating to the total
    count += 1  # Increment the count of ratings
    rating = int(input("Enter rating for featured movie (0-4, -1 to quit): "))  # Get the next rating

# Calculate and display the average star rating
if count > 0:  # To avoid division by zero
    average_rating = total_rating / count
    print(f"Average Star Value: {average_rating:.3f}")  # Display average to three decimal places
else:
    print("No ratings were entered.")
