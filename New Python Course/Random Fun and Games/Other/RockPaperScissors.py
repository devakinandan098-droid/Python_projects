import random as r
choices=["rock","paper","scissors"]
print("Rock crushes scissors. Scissors cut paper. Paper covers rock.")
player=input("Enter your choice(Rock, Paper, or Scissors): ")
while player !="quit":
    player=player.lower()
    computer=r.choice(choices)
    print("You chose "+ player +",and the computer chose", computer,"." )
    if player==computer:
        print("It's a tie")
    elif player=="rock":
        if computer=="scissors":
            print("You win")
        else:
            print("The computer won")
    elif player=="paper":
        if computer=="rock":
            print("You win")
        else:
            print("The computer won")
    elif player=="scissors":
        if computer=="paper":
            print("You win")
        else:
            print("The computer won")
    else:
        print("Invalid Input. Please try again")
    print()
    player=input("Enter your choice(Rock, Paper, or Scissors): ")