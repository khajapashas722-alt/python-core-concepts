import random

n = random.randrange(0,101)
attempts = 0
print("Welcome to number guessing game")
print("I am thinking of a number between 0 and 100")
while True:
    try:
        a = int(input("Guess the number : "))
        attempts += 1
        if a == n:
            print(f"Congratulations, The correct answer was {n}.")
            print(f"It took you {attempts} attempts to guess the number")
            break
        elif a<n:
            print("Too low! Try again")
        else:
            print("Too high! Try again")
    except ValueError:
        print("Invalid input. Enter a valid number")