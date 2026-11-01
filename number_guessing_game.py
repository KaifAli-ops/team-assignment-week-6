# Module 6: Number Guessing Game
# Individual submission

import random

print("Welcome to the Number Guessing Game!")
print("I will choose a number between 1 and 100.")
print("Try to guess the number.")

play_again = "Y"

# Extra credit: continue playing until the user enters N.
while play_again == "Y":
    secret_number = random.randint(1, 100)
    guess = 0

    print("\nI have picked a new number.")

    # Keep asking until the user guesses correctly.
    while guess != secret_number:
        user_input = input("Enter your guess (1-100): ")

        if user_input.isdigit():
            guess = int(user_input)

            if guess >= 1:
                if guess <= 100:
                    # Nested if/else statements compare the guess.
                    if guess < secret_number:
                        print("Guess higher.")
                    else:
                        if guess > secret_number:
                            print("Guess lower.")
                        else:
                            print("Correct! You guessed the number.")
                else:
                    print("Please enter a number from 1 to 100.")
            else:
                print("Please enter a number from 1 to 100.")
        else:
            print("Invalid input. Please enter a whole number.")

    play_again = input("Would you like to guess another number (Y/N)? ")
    play_again = play_again.upper()

    while play_again != "Y":
        if play_again == "N":
            break
        else:
            print("Please enter Y for yes or N for no.")
            play_again = input("Would you like to guess another number (Y/N)? ")
            play_again = play_again.upper()

print("\nThank you for playing!")
print("Goodbye!")
