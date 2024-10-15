import random

def guessing_game():
    while True:
        number = random.randint(1, 10)  # Generate a random number between 1 and 10
        print("I'm thinking of a number between 1 and 10...")

        while True:
            user_input = input("Try to guess by entering a number between 1 and 10: ")

            # Validate user input
            try:
                user_number = int(user_input)  # Convert input to integer
                if 1 <= user_number <= 10:  # Check if within valid range
                    break  # Exit loop if input is valid
                else:
                    print("Number must be in the range of 1 to 10: Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Check if the user guessed correctly
        if user_number == number:
            print("You are a genius. That's correct!")
        else:
            print("That's not correct.")

        # Ask if the user wants to guess again
        while True:
            keep_going = input("Do you want to guess again? Enter Y or N: ").strip().upper()
            if keep_going in ('Y', 'N'):
                break
            else:
                print("Invalid input. Please enter Y or N.")

        if keep_going == 'N':
            print("Thank you for playing!")
            break  # Exit the game loop

if __name__ == "__main__":
    guessing_game()
