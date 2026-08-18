import random as r
suits=["Clubs","Diamonds","Hearts","Spades"]
faces=["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
my_face=r.choice(faces)
my_suit=r.choice(suits)
print("I have the", my_face,"of", my_suit)