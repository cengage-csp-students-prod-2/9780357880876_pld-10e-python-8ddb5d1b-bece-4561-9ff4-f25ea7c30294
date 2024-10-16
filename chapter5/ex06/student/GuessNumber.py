import random

def guessing_game():
    while True:
        # Input validation loop
        while True:
            try:
                number_in = int(input("Try to guess by entering a number between 1 and 10: "))
                if 1 <= number_in <= 10:
                    break
                else:
                    print("Number must be in the range of 1 to 10: Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        game_1 = random.randint(1, 10)

        # Check if the user guessed correctly
        if number_in == game_1:
            print("You are a genius. That's correct!")
        else:
            print("That's not correct.")

        # Ask if the user wants to play again
        play_again = input("Do you want to guess again? Enter Y or N: ").strip().upper()
        if play_again != 'Y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    guessing_game()