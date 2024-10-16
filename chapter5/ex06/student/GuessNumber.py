from random import randint

# Function to validate the input number
def validateNumber(number):
    if 1 <= number <= 10:  # Include both 1 and 10 in the range
        return True
    else:
        return False

# Generate a random number between 1 and 10
game_1 = randint(1, 10)

while True:
    try:
        # Prompt user for input
        number_in = int(input("Please insert a number between 1-10: "))

        # Validate the number
        if not validateNumber(number_in):
            print("Number must be in the range of 1 to 10: Please try again.")
            continue  # Go back to the input prompt

        # Check if the guess is correct
        if number_in == game_1:
            print(f"The result was {game_1}. Your guess was correct, congratulations!")
            break  # Exit the loop after a correct guess
        else:
            print(f"The result was {game_1}. Your guess was NOT correct. Try again.")

    except ValueError:
        print("Invalid input. Please enter a valid integer between 1 and 10.")