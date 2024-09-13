# GuessNumber.py - This program allows a user to guess a number between 1 and 1000.
# Input:  User guesses numbers until they get it right.
# Output: Tells users if they are right or wrong.

from random import randint

number = randint(1, 10) # Generate random number.

# Prime the loop.
keepGoing = input("Do you want to guess a number? Enter Y or N")

# Validate input.

# Enter loop if they want to play.
while keepGoing == "Y":
    # Get user's guess.
    stringNumber = input("I'm thinking of a number...\nTry to guess by entering a number between 1 and 10")
    userNumber = int(stringNumber)

    # Validate input.

    # Test to see if the user guessed correctly.
    if userNumber == number:
        keepGoing = "N"
        print("You are a genius. That's correct!")

    else:
        keepGoing = input("That's not correct. Do you want to guess again? Enter Y or N")

        # Validate input.

# End of while loop.