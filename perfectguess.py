import random

# Generate a random number between 1 and 100
num = random.randint(1, 100)
guess_count = 1

# First guess input
guess = int(input("Guess the number (1-100): "))

# Loop until the correct number is guessed
while guess != num:
    if guess > num:
        print("Lower")
    else:
        print("Higher")
    
    guess_count += 1
    guess = int(input("Guess the number (1-100): "))

# Success message
print(f"Congratulations! You guessed the number {num} in {guess_count} attempts.")
