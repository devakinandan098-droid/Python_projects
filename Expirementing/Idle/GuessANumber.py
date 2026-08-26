import random as r
logo="""
   _____                               _   _                 _               
  / ____|                             | \ | |               | |              
 | |  __ _   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__,_| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                             
                                                                             
"""
print("Welcome to Guess a Number!")
import random as r
print(logo)
global number
Hello=print("Hello")
Hello
guess=""
print("Welcome to the guessing game!")
print("I am thinking of a number between 1 and 100.")
easy_hard=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
play_again="y"
number=r.randint(1,100)
def play():
    if easy_hard=="easy":
        number=r.randint(1,100)
        health=10
        print("You have ",health,"attempts to guess the number.")
        guess=int(input("Make a guess: "))
        while health>0 and guess!=number:
            if guess!=number:
                health-=1
                print("You have ", health, "attempts to guess the number.")
                guess = int(input("Make a guess: "))
        if guess==number:
            print("Congratulations, you guessed the number.")
        if health==0:
                print("You lose.")
                print("The number was",number,".")
    elif easy_hard=="hard":
        number=r.randint(1,100)
        health=5
        while health>0 and guess!=number:
            print("You have ", health, "attempts.")
            guess = int(input("Make a guess: "))
            if guess!=number:
                health-=1
                print("You have ", health, "attempts to guess the number.")
                guess = int(input("Make a guess: "))
        if guess==number:
            print("Congratulations, you guessed the number.")
        if health==0:
                print("You lose.")
                print("The number was",number,".")
    play_again=input("Do you want to play again? Type 'y' or 'no': ")
while play_again=="y":
    number=r.randint(1,100)
    print("\n" * 100)
    print(logo)
    play()