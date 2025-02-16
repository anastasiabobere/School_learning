import random

def game():
    number = random.randint(1, 100)
    attempt = 0
    max_attempts = 20

    while attempt < max_attempts:
        try:
            user_input = int(input("Please guess the number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempt += 1

        if user_input == number:
            print(f"You guessed correctly! The number was {number}. You guessed it in {attempt} attempts.")
            return
        elif user_input > number:
            print("Number too high.")
        else:
            print("Number too low.")

        print(f"You are on attempt {attempt} of {max_attempts}.")

    answer = input("You've reached the maximum number of attempts. Do you want to give up? (y/n): ")
    if answer.lower() == 'y':
        print(f"The number was {number}. Better luck next time!")
    else:
        print("Let's continue!")
        game()

game()