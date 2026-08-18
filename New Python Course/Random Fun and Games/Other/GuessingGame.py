import random
number=random.randint(1,100)
guess=int(input("Guess a number between 1 and 100: "))
while guess!=number:
    if guess<number:
        print(guess, "is too low")
    else:
        print(guess, "is too high")
    guess=int(input("Guess again: "))
print("Congratulations! You guessed the number!")