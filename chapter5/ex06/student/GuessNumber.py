mport random

while True:
    try:
        number_in = int(input("Please insert a number between 1-10: "))
        if 1 <= number_in <= 10:
            break
        else:
            print("Your input was invalid. Please insert a number from 1 to 10")
    except ValueError:
        print("Sorry. Try again to insert a number from 1 to 10")

game_1 = random.randint(1, 10)

if number_in == game_1:
    print(f"The result was {game_1}. Your guess was correct, congratulations!")
else:
    print(f"The result was {game_1}. Your guess was NOT correct. Try again")