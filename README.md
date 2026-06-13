# Number Guessing Game (CLI)

A simple Command Line Interface (CLI) number guessing game built using Python. The program randomly selects a number between 1 and 100, and the player must guess the correct number with the help of hints.

# Features

- Randomly generates a number between 1 and 100
- Displays "Too high!" if the guess is greater than the secret number
- Displays "Too low!" if the guess is smaller than the secret number
- Counts the number of attempts taken to guess correctly

# How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Angad1955/synent-task2-numberguessinggame-angad
   ```

2. Navigate to the project directory:
   ```bash
   cd synent-task2-numberguessinggame-angad
   ```

3. Run the program:
   ```bash
   python task-2.py
   ```

# Example Output

```
Welcome to the Number Guessing Game!
I have picked a number between 1 and 100. Can you guess it?

Enter your guess: 50
Too low! Try again.

Enter your guess: 75
Too high! Try again.

Enter your guess: 62
Congratulations! You guessed the number 62 in 3 attempts!
```

If an invalid input is entered:

```
Enter your guess: abc
Invalid input. Please enter an integer.
```

# Technologies Used

- Python 3
- Random module (`random`)

# Concepts Demonstrated

- Random number generation using `random.randint()`
- User input with `input()`
- Type conversion using `int()`
- `while` loops
- Conditional statements (`if`, `elif`, `else`)
- Exception handling with `try-except`
- Variables, counters, and boolean flags
