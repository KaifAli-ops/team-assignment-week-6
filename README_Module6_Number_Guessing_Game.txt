# Module 6: Number Guessing Game

## Assignment overview
The computer randomly selects a number from 1 to 100. The user enters guesses, and the program gives a hint to guess higher or lower until the user finds the correct number.

## Requirements included
- Uses Python's built-in `random` module.
- Uses `random.randint(1, 100)` to generate a random number.
- Accepts a guess from the user.
- Gives higher/lower hints.
- Uses nested `if/else` statements.
- Checks for non-numeric input and guesses outside the 1–100 range.
- Includes the extra-credit replay feature. The user can enter `Y` to play another round or `N` to end the program.

## How to run
1. Save or open `number_guessing_game.py`.
2. Run it in IDLE, VS Code, PyCharm, or another Python editor.
3. Enter whole-number guesses from 1 through 100.
4. Follow the hints until the number is guessed.
5. Enter `Y` to play again or `N` to stop.

## Example output
The random number changes each time. This is one possible run.

```text
Welcome to the Number Guessing Game!
I will choose a number between 1 and 100.
Try to guess the number.

I have picked a new number.
Enter your guess (1-100): 25
Guess higher.
Enter your guess (1-100): 70
Guess lower.
Enter your guess (1-100): 52
Correct! You guessed the number.
Would you like to guess another number (Y/N)? Y

I have picked a new number.
Enter your guess (1-100): 40
Guess higher.
Enter your guess (1-100): 60
Correct! You guessed the number.
Would you like to guess another number (Y/N)? N

Thank you for playing!
Goodbye!
```

## How the program works
The `random` module selects a new secret number for each round. A `while` loop keeps the round active until the user guesses correctly. Nested `if/else` statements compare the guess with the secret number and display a hint. The replay loop provides the extra-credit feature and ends when the user enters `N`.

## Testing checklist
- [ ] A lower guess displays "Guess higher."
- [ ] A higher guess displays "Guess lower."
- [ ] A correct guess displays the success message.
- [ ] Letters and symbols are rejected.
- [ ] Numbers outside 1–100 are rejected.
- [ ] `Y` starts another round.
- [ ] `N` ends the program.
- [ ] Lowercase `y` and `n` are accepted.
