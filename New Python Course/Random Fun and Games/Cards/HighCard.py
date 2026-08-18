import random as r
suits=["Clubs","Diamonds","Hearts","Spades"]
faces=["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
keep_going=True
while keep_going:
    my_face=r.choice(faces)
    my_suit=r.choice(suits)
    your_face=r.choice(faces)
    your_suit=r.choice(suits)
    print("I have the",my_face,"of",my_suit)
    print("You have the",your_face,"of",your_suit)
    if faces.index(my_face)>faces.index(your_face):
        print("I win")
    elif faces.index(my_face)<faces.index(your_face):
        print("You win")
    else:
        print("It's a tie!")
    answer=input("Hit [Enter] to keep going, and hit any key to exit: ")
    keep_going=(answer=="")