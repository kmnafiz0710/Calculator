import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 10)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please guess a number within the range (1-10).")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                guessed = True

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    number_guessing_game()


