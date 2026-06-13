import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0
guessed_correctly = False

print("Welcome to the Number Guessing Game!")
print("I have picked a number between 1 and 100. Can you guess it?")

while not guessed_correctly:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            guessed_correctly = True
    except ValueError:
        print("Invalid input. Please enter an integer.")