from random import randint

def guessing_game():
    number = randint(1, 10)  # Generate random number between 1 and 10.

    # Prime the loop.
    keepGoing = input("Do you want to guess a number? Enter Y or N: ").strip().upper()

    # Validate input for 'Y' or 'N'
    while keepGoing not in ('Y', 'N'):
        keepGoing = input("Invalid input. Please enter Y or N: ").strip().upper()

    # Enter loop if they want to play.
    while keepGoing == "Y":
        # Get user's guess and validate input.
        while True:
            try:
                stringNumber = input("I'm thinking of a number...\nTry to guess by entering a number between 1 and 10: ")
                userNumber = int(stringNumber)

                # Validate if the number is in range
                if 1 <= userNumber <= 10:
                    break  # Correct range, continue to checking if correct guess
                else:
                    print("Number must be in the range of 1 to 10: Please try again.")  # Ensures this message is printed
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Test to see if the user guessed correctly.
        if userNumber == number:
            print("You are a genius. That's correct!")
            break  # Exit the loop if correct guess is made.

        else:
            # Ask if the user wants to guess again.
            keepGoing = input("That's not correct. Do you want to guess again? Enter Y or N: ").strip().upper()

            # Validate input for 'Y' or 'N'
            while keepGoing not in ('Y', 'N'):
                keepGoing = input("Invalid input. Please enter Y or N: ").strip().upper()

    # End of the game.
    print("Thank you for playing!")

if __name__ == "__main__":
    guessing_game()