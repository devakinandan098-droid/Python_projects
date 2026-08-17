logo="""
  ___    _______         _   _                           _           _      _      
 |__ \  |__   __|       | | | |                         | |         | |    (_)     
    ) |    | |_ __ _   _| |_| |__  ___    __ _ _ __   __| |   __ _  | |     _  ___ 
   / /     | | '__| | | | __| '_ \/ __|  / _` | '_ \ / _` |  / _` | | |    | |/ _ \
  / /_     | | |  | |_| | |_| | | \__ \ | (_| | | | | (_| | | (_| | | |____| |  __/
 |____|    |_|_|   \__,_|\__|_| |_|___/  \__,_|_| |_|\__,_|  \__,_| |______|_|\___|
                                                                                   
                                                                                   """
def statements():
    global statment1, statment2, statment3, statment4, statment5, statment6
    statment1=input("Enter a statement: ")
    statment2=input("Enter a statement: ")
    statment3=input("Enter a statement: ")
    print("Next player's turn")
    statment4=input("Enter a statement: ")
    statment5=input("Enter a statement: ")
    statment6=input("Enter a statement: ")
def player_2():
    global guess2
    try:
        print("Player 2's statements are:",statment4,",",statment5,",",statment6)
        guess2=int(input("Player 1, please guess which statement is a lie('1', '2', or '3'): "))
    except ValueError:
        print("Invalid statement. Please Rerun.")
    if guess2==lie2:
        print("Correct!")
        print("Correct! You have gotten the correct answer Player 1. Statement:",lie2,"was a lie!")
        print("Thank you for playing 2 Truths and a Lie")
    elif guess2 != lie2:
        print("Incorrect.")
        print("The correct answer was:",lie2)
        print("Thank you for playing 2 Truths and a Lie")
print(logo)
print("Welcome to 2 Truths and a Lie!")
print("This game requires 2 players to play.")
statements()
print("Now, player one. Move forward and player two should not look.")
try:
    lie1=int(input("Please enter which statement of yours is false('1','2', or '3'): "))
except ValueError:
    print("Invalid statement, please rerun")
print("\n"*100)
print(logo)
print("Player one, please tell Player 2 to step forward and player one should not be looking.")
print(statment4,",",statment5,",",statment6)
try:
    lie2=int(input("Please enter which statement of yours is false('1','2', or '3'): "))
    print("\n"*100)
    print(logo)
except ValueError:
    print("Invalid statement, please rerun")
print("Now, both players come to face the screen.")
print("Player one's statements are:",statment1,",",statment2,",",statment3)
try:
    guess1=int(input("Please enter which statement you think is a lie player 2('1', '2', or'3'): "))
except ValueError:
    print("Invalid statement, please rerun")
if guess1==lie1:
    print("Correct! You have gotten the correct answer Player 2. Statement:",guess1,"was a lie!")
    player_2()
elif guess1 != lie1:
        print("Incorrect.")
        print("The correct answer was:",lie1)
        player_2()