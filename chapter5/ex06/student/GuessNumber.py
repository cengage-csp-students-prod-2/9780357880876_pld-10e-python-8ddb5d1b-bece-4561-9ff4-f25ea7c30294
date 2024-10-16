import random

def guessing_game():
    while True:  # Loop for multiple game rounds
        number_to_guess = random.randint(1, 10)  # Generate a random number between 1 and 10
        print("I'm thinking of a number...")

        while True:  # Loop for guessing the number
            try:
                # Get user input for guessing
                guess = int(input("Try to guess by entering a number between 1 and 10: "))
                if 1 <= guess <= 10:  # Validate guess
                    break  # Valid guess, exit loop
                else:
                    print("Invalid input. Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        if guess == number_to_guess:
            print("Congratulations! You've guessed the correct number.")
        else:
            print(f"That's not correct. The correct number was {number_to_guess}.")

        while True:  # Loop for asking if the user wants to guess again
            again = input("Do you want to guess again? Enter Y or N: ").strip().upper()
            if again in ('Y', 'N'):  # Validate the input
                break  # Valid input, exit loop
            else:
                print("Invalid input. Please enter Y or N.")

        if again == 'N':
            print("Thank you for playing!")
            break  # Exit the main game loop

# Call the guessing game function to start the game
guessing_game()
