# GuessNumber.py - This program allows a user to guess a number between 1 and 10.
# Input:  User guesses numbers until they get it right.
# Output: Tells users if they are right or wrong.

from random import randint

def guessing_game():
    while True:  # Loop to allow for multiple rounds of guessing
        number = randint(1, 10)  # Generate random number between 1 and 10

        # Prime the loop.
        keepGoing = input("Do you want to guess a number? Enter Y or N: ").strip().upper()

        # Validate initial input
        while keepGoing not in ("Y", "N"):
            keepGoing = input("Invalid input. Please enter Y or N: ").strip().upper()

        # Enter loop if they want to play.
        while keepGoing == "Y":
            # Get user's guess.
            stringNumber = input("I'm thinking of a number...\nTry to guess by entering a number between 1 and 10: ")

            # Validate user input for guess
            while True:
                try:
                    userNumber = int(stringNumber)
                    if 1 <= userNumber <= 10:  # Validate the number is in the correct range
                        break  # Valid input, exit loop
                    else:
                        stringNumber = input("Number must be in the range of 1 to 10: Please try again: ")
                except ValueError:
                    stringNumber = input("Invalid input. Please enter a valid integer: ")

            # Test to see if the user guessed correctly.
            if userNumber == number:
                print("You are a genius. That's correct!")
                break  # Exit the loop after a correct guess
            else:
                keepGoing = input("That's not correct. Do you want to guess again? Enter Y or N: ").strip().upper()

                # Validate input for continuing the game
                while keepGoing not in ("Y", "N"):
                    keepGoing = input("Invalid input. Please enter Y or N: ").strip().upper()

# Call the guessing game function to start the game
guessing_game()