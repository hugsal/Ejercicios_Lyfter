import random

secret_number = random.randint(1, 10)
print("Guess the number between 1 and 10")
number = int(input("Enter your guess: "))
while number != secret_number:
    number = int(input("Enter your guess: "))
print("You got it! The number was " + str(secret_number))
